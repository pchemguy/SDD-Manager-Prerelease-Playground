"""Portable, stdlib-only TextStats coordinator helpers.

Own non-secret configuration, source pinning, bounded fresh preparation, actual
Git/recovery observation and deterministic assessment. HELPER-INTERFACES.md is the
canonical machine/operational contract. Helpers never perform an agent/product
workflow or authenticate, commit, push or mutate hosted task objects. Preparation
and recovery exports have explicit filesystem effects and are not transactions.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from urllib.parse import parse_qsl, urlsplit

BUNDLE = Path(__file__).resolve().parents[1]
SOURCE = Path(__file__).resolve().parents[3]
PACKAGE_PATHS = ('plugin.json', '.codex-plugin', 'README.md', 'AGENTS.md', 'Greenfield Project Prompt Template.md', 'LICENSE', 'SDD-MANAGER.md', 'AI_DISCLOSURE.md', 'skills', 'assets')
MISSING = 'Which dedicated test repository should this run use? Supply its URL or local checkout path.'
SECRET = re.compile(r'(?:github_pat_|gh[pousr]_|Bearer\s+)[A-Za-z0-9_\-]+', re.I)

class Stop(Exception):
    """Report a sanitized prerequisite or contract failure to the CLI.

    Attributes:
        cause: Stable non-secret failure category.
        action: Safe continuation guidance, never a failed input or provider body."""
    def __init__(self, cause, action='Resolve the reported prerequisite before retrying.'):
        self.cause, self.action = cause, action


def protected(path):
    """Classify a credential or Git-metadata path without reading its content.

    Args:
        path: A path whose components are checked case-insensitively.

    Returns:
        Whether a component matches a protected name, prefix or extension."""
    parts = Path(path).parts
    return any(p.lower() in {'.git', '.ssh', '.aws', '.credentials', 'credentials', '.env', 'gh.tkn', '.netrc', '.npmrc', '.pypirc', '.git-credentials', 'id_rsa', 'id_ed25519'} or p.lower().endswith(('.tkn', '.pem', '.key')) or p.lower().startswith('.env.') for p in parts)


def sensitive_text(value):
    """Detect recognizable token patterns and credential-bearing URLs in text.

    Username-only SSH URLs are allowed; URL parse errors are treated as unsafe.
    This is a conservative pattern check, not a general secret detector."""
    if SECRET.search(value): return True
    for matched in re.finditer(r"[A-Za-z][A-Za-z0-9+.-]*://[^\s<>\"'`]+", value):
        try:
            url = urlsplit(matched.group())
            if url.password is not None: return True
            if url.username is not None and url.scheme.lower() != 'ssh': return True
            if url.scheme.lower() == 'ssh' and url.query: return True
            if any(key.lower() in {'token','access_token','password','credential','credentials','api_key','auth','authorization'} for key,_ in parse_qsl(url.query)): return True
        except ValueError:
            return True
    return False


def no_secret(value):
    """Reject protected keys, recognizable secrets and NULs in JSON-like data.

    Recurses through dictionaries/lists without mutating the value. Raises Stop
    with invalid_nonsecret_configuration instead of echoing the failed value."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key != 'protected_credentials' and re.fullmatch(r'(?:token|password|credentials?|secret|access_token|credential_path)', key, re.I):
                raise Stop('invalid_nonsecret_configuration')
            no_secret(item)
    elif isinstance(value, list):
        for item in value: no_secret(item)
    elif isinstance(value, str) and (sensitive_text(value) or '\x00' in value):
        raise Stop('invalid_nonsecret_configuration')


def clean_bytes(data):
    """Return bytes unchanged after screening their decoded text for secrets.

    UTF-8 replacement decoding is used only for screening; binary bytes remain
    intact. Raises Stop for recognizable sensitive content before export."""
    if sensitive_text(data.decode('utf-8', errors='replace')):
        raise Stop('sensitive_content_not_exportable', 'Retain protected content separately; do not publish it as test evidence.')
    return data


def exact(left, right):
    """Compare JSON-like values without type coercion.

    Dictionary key order is irrelevant; array order and exact value types are
    significant, so booleans cannot satisfy integer expectations."""
    if type(left) is not type(right): return False
    if isinstance(left, dict): return left.keys() == right.keys() and all(exact(left[k], right[k]) for k in left)
    if isinstance(left, list): return len(left) == len(right) and all(exact(a,b) for a,b in zip(left,right))
    return left == right


def validate(value, schema):
    """Validate the bounded keywords used by the bundle's version 1 schemas.

    Args:
        value: JSON-like data to check without mutation or type coercion.
        schema: A trusted bundle schema using the supported keyword subset.

    Raises:
        Stop: The data violates a supported constraint (invalid_schema).

    This is not a general JSON Schema implementation."""
    if 'anyOf' in schema:
        for child in schema['anyOf']:
            try: validate(value, child); break
            except Stop: pass
        else: raise Stop('invalid_schema')
    kinds = {'object':dict, 'array':list, 'string':str, 'integer':int, 'boolean':bool, 'null':type(None)}
    if 'type' in schema and type(value) is not kinds[schema['type']]: raise Stop('invalid_schema')
    if 'const' in schema and not exact(value, schema['const']): raise Stop('invalid_schema')
    if 'enum' in schema and not any(exact(value,x) for x in schema['enum']): raise Stop('invalid_schema')
    if isinstance(value, dict):
        if any(k not in value for k in schema.get('required',[])): raise Stop('invalid_schema')
        props = schema.get('properties',{})
        extra = schema.get('additionalProperties',True)
        for key, child in value.items():
            if 'propertyNames' in schema: validate(key,schema['propertyNames'])
            if key in props: validate(child,props[key])
            elif extra is False: raise Stop('invalid_schema')
            elif isinstance(extra,dict): validate(child,extra)
    if isinstance(value,list):
        if schema.get('uniqueItems') and any(exact(x,y) for i,x in enumerate(value) for y in value[:i]): raise Stop('invalid_schema')
        for child in value:
            if 'items' in schema: validate(child,schema['items'])
    if isinstance(value,str):
        if len(value) < schema.get('minLength',0): raise Stop('invalid_schema')
        if 'pattern' in schema and not re.search(schema['pattern'],value): raise Stop('invalid_schema')
        if schema.get('format') == 'date-time':
            try:
                dt = datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
                if dt.tzinfo is None or 'T' not in value: raise ValueError()
            except ValueError: raise Stop('invalid_schema')
    if type(value) in (int,float) and value < schema.get('minimum',float('-inf')): raise Stop('invalid_schema')


def load(path):
    """Read JSON and screen it for protected values before returning it.

    Raises Stop with invalid_json for read/parse errors, or a sanitized secret
    failure. The caller controls the path; no file is modified."""
    try:
        data = json.loads(Path(path).read_text())
    except (OSError, ValueError): raise Stop('invalid_json')
    no_secret(data)
    return data


def configuration(path):
    """Load strict version 1 inputs and apply non-secret helper defaults.

    Missing repository input raises Stop with the dedicated setup question.
    Successful validation returns a new dictionary without modifying inputs."""
    data = load(path)
    if isinstance(data,dict) and not str(data.get('test_repository','')).strip():
        raise Stop('missing_repository',MISSING)
    validate(data,load(BUNDLE/'schemas/inputs.schema.json'))
    resolved = {'plugin_revision':'HEAD','source_mode':'committed','scope':{},'stop_after':None,'profile':'full-github'}
    resolved.update(data)
    if 'variants' in resolved:
        import campaign
        cases={c['id']:c for c in load(BUNDLE/'cases/catalog.json')['cases']}
        scope=resolved['scope']
        cases={k:c for k,c in cases.items() if (not scope.get('cases') or k in scope['cases']) and (not scope.get('phases') or c['phase'] in scope['phases'])}
        try: campaign.select(cases,resolved['variants'])
        except (ValueError,TypeError): raise Stop('invalid_variant_selection') from None
    return resolved


def checkpoint(path, inputs):
    """Load an optional strict checkpoint and check supplied run/repo identity.

    Args:
        path: Checkpoint JSON path, or None to return None.
        inputs: Resolved configuration used for identity comparisons.

    Returns:
        Validated checkpoint data, not proof of its freshness or actual effects.

    Raises:
        Stop: Invalid data or conflicting recorded run/repository identity."""
    if path is None: return None
    state = load(path)
    validate(state,load(BUNDLE/'schemas/run-state.schema.json'))
    if inputs.get('run_id') and inputs['run_id'] != state['run_id']: raise Stop('run_identity_mismatch')
    identity = state.get('repository',{}).get('identity')
    if identity and normalize(identity) != normalize(inputs['test_repository']): raise Stop('repository_identity_mismatch')
    return state


def git(repo, *args, required=True, binary=False):
    """Run one bounded Git command with captured output and no terminal prompt.

    Args:
        repo: Git command working directory.
        *args: Already selected Git arguments; credential values are forbidden.
        required: Raise Stop on a nonzero exit when true.
        binary: Capture bytes instead of decoded text when true.

    Returns:
        subprocess.CompletedProcess for the attempted command.

    Raises:
        Stop: Launch/30-second timeout failure, or required command failure.

    Optional locks and fsmonitor are disabled. This wrapper does not make an
    arbitrary command read-only; callers own permitted Git effects."""
    env = dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
    try:
        result = subprocess.run(['git','-c','core.fsmonitor=false','-C',str(repo),*args],capture_output=True,text=not binary,env=env,timeout=30)
    except (OSError,subprocess.TimeoutExpired): raise Stop('git_unavailable')
    if result.returncode and required: raise Stop('git_operation_unavailable','Inspect repository/access prerequisites using the pinned plugin protocols; retain pending work.')
    return result


def normalize(value):
    """Normalize a repository locator for the helper's identity comparisons.

    Local paths are expanded/resolved; transport locators lose a trailing slash
    and .git suffix. SSH and HTTPS spellings are not unified by this helper."""
    if '://' in value or re.match(r'^[^/]+@[^:]+:',value): return value.rstrip('/').removesuffix('.git')
    return str(Path(value).expanduser().resolve())


def remote_read(repo, remote):
    """Read actual remote refs/default branch without fetching or writing.

    Args:
        repo: Git working directory used for ls-remote.
        remote: Established remote name or non-secret locator.

    Returns:
        Status, full observed SHA-1 refs and optional symbolic default branch.
        A nonzero response is unavailable, never evidence of absent refs.

    Raises:
        Stop: Git cannot be launched or completes beyond its bounded timeout."""
    result = git(repo,'ls-remote','--symref',remote,required=False)
    refs, default = {}, None
    if result.returncode: return {'status':'unavailable','refs':{},'default_branch':None}
    for line in result.stdout.splitlines():
        if line.startswith('ref: '):
            ref, name = line[5:].split('\t')
            if name == 'HEAD' and ref.startswith('refs/heads/'): default=ref[11:]
        elif '\t' in line:
            sha, name = line.split('\t')
            if re.fullmatch('[0-9a-f]{40}',sha): refs[name]=sha
    return {'status':'observed','refs':refs,'default_branch':default}


def repository(inputs, observe_remote=True):
    """Resolve the requested checkout and uniquely matching authorized remote.

    Args:
        inputs: Validated configuration with test_repository/local_checkout.

    Returns:
        Repository identity, local state, retained run paths and live remote
        readback. URL/bare-remote input can return no local checkout. The local
        branch is a fallback integration candidate when no default is observed.

    Raises:
        Stop: Ineligible/ambiguous checkout, mismatched or ambiguous remotes,
            protected locators, or unavailable required Git operations.

    Reads only; ref discovery does not certify write access or authorization."""
    identified = inputs['test_repository']
    explicit = inputs.get('local_checkout')
    local = Path(explicit or identified).expanduser()
    if not explicit and (not local.is_dir() or git(local,'rev-parse','--is-bare-repository',required=False).stdout.strip()=='true'):
        if not observe_remote:raise Stop('local_checkout_required')
        read = remote_read(SOURCE,identified)
        return {'identity':identified,'local_checkout':None,'remote':None,'remote_url':identified,'integration_branch':read['default_branch'],'remote_observation':read,'head':None,'existing_runs':[]}
    root = git(local,'rev-parse','--show-toplevel',required=False)
    if root.returncode: raise Stop('repository_not_checkout')
    checkout = Path(root.stdout.strip()).resolve()
    if checkout != local.resolve(): raise Stop('repository_ambiguous')
    names = git(checkout,'remote').stdout.splitlines()
    remotes = []
    identity_is_checkout = normalize(identified) == str(checkout)
    for name in names:
        url = git(checkout,'remote','get-url',name).stdout.strip()
        no_secret(url)
        if identity_is_checkout or normalize(url)==normalize(identified): remotes.append((name,url))
    if not remotes: raise Stop('repository_identity_mismatch')
    if len(remotes) != 1: raise Stop('repository_ambiguous','Select one unambiguous dedicated repository and authorized remote before writes.')
    name,url=remotes[0]
    read=remote_read(checkout,name) if observe_remote else {'status':'not-requested','refs':{},'default_branch':None}
    branch=git(checkout,'symbolic-ref','--quiet','--short','HEAD',required=False).stdout.strip() or None
    refs=git(checkout,'for-each-ref','--format=%(refname)','refs/heads').stdout.splitlines()
    integration = read['default_branch']
    if not integration and branch and ('refs/heads/'+branch in refs): integration=branch
    runs=sorted(str(p.relative_to(checkout)) for p in (checkout/'docs/dev/reviews').glob('*/RUN-STATE.json'))
    head=git(checkout,'rev-parse','--verify','HEAD',required=False).stdout.strip() or None
    return {'identity':identified,'local_checkout':str(checkout),'remote':name,'remote_url':url,'integration_branch':integration,'remote_observation':read,'head':head,'existing_runs':runs}


def package(source, inputs):
    """Pin supported package files to Git objects or an explicit dirty snapshot.

    Args:
        source: Eligible source Git checkout.
        inputs: Resolved plugin_revision and committed/dirty source_mode.

    Returns:
        A (provenance, files) pair. Provenance records full commit, exact hashes,
        modes, changed paths and mode-sensitive fingerprint; files maps relative
        package paths to exact binary bytes.

    Raises:
        Stop: Missing manifest/revision, unsupported modes/symlinks, protected
            paths/content, or dirty mode requested against a non-current HEAD.

    Reads source only. Dirty snapshots include nonignored untracked package
    files; default committed snapshots ignore pending source edits."""
    source=Path(source).resolve()
    commit=git(source,'rev-parse','--verify',inputs['plugin_revision']+'^{commit}').stdout.strip()
    if not re.fullmatch('[0-9a-f]{40}',commit): raise Stop('source_revision_unavailable')
    names=git(source,'ls-tree','-rz','--name-only',commit,*PACKAGE_PATHS,binary=True).stdout.decode().split('\x00')
    files={}
    modes={}
    for row in git(source,'ls-tree','-rz',commit,*PACKAGE_PATHS,binary=True).stdout.decode().split('\x00'):
        if row:
            metadata,name=row.split('\t',1)
            modes[name]=metadata.split()[0]
    for name in filter(None,names):
        if protected(name): raise Stop('protected_package_path')
        if modes[name] not in {'100644','100755'}: raise Stop('package_mode_unsupported')
        files[name]=clean_bytes(git(source,'show',commit+':'+name,binary=True).stdout)
    changed=[]
    committed_modes=dict(modes)
    if inputs['source_mode']=='dirty':
        if commit != git(source,'rev-parse','HEAD').stdout.strip(): raise Stop('dirty_source_requires_current_head')
        candidates=git(source,'ls-files','-z','--cached','--others','--exclude-standard',*PACKAGE_PATHS,binary=True).stdout.decode().split('\x00')
        dirty={}
        dirty_modes={}
        for name in set(filter(None,candidates)):
            if protected(name): raise Stop('protected_package_path')
            path=Path(source)/name
            if any(parent.is_symlink() for parent in path.parents if parent != Path(source).resolve() and parent.is_relative_to(Path(source).resolve())): raise Stop('package_symlink_unsupported')
            if not path.parent.resolve().is_relative_to(Path(source).resolve()): raise Stop('unsafe_package_path')
            if path.is_symlink(): raise Stop('package_symlink_unsupported')
            if path.is_file():
                dirty[name]=clean_bytes(path.read_bytes())
                dirty_modes[name]='100755' if path.stat().st_mode & 0o111 else '100644'
        changed=sorted(name for name in set(files)|set(dirty) if files.get(name)!=dirty.get(name) or committed_modes.get(name)!=dirty_modes.get(name))
        files=dirty
        modes=dirty_modes
    if not any(name in files for name in ('plugin.json', '.codex-plugin/plugin.json')): raise Stop('package_unavailable')
    hashes={name:hashlib.sha256(data).hexdigest() for name,data in sorted(files.items())}
    fingerprint=hashlib.sha256(json.dumps({'hashes':hashes,'modes':modes},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'revision':inputs['plugin_revision'],'commit':commit,'source_mode':inputs['source_mode'],'package_hashes':hashes,'package_file_modes':modes,'fingerprint':fingerprint,'changed_package_paths':changed},files


def preflight(inputs, source):
    """Observe repository/source/runtime prerequisites without certification.

    Returns non-secret provenance and conservative false capability flags.
    Remote read access cannot establish publication/API/agent/client facilities.
    Repository or package prerequisite failures propagate as Stop."""
    repo=repository(inputs)
    pinned,_=package(source,inputs)
    return {'schema_version':1,'resolved_inputs':inputs,'repository':repo,'plugin_source':pinned,'runtime':{'python':sys.version.split()[0],'git':git(source,'--version').stdout.strip()},'capabilities':{'git_publication':False,'github_api':False,'fresh_consumers':False,'independent_assessor':False,'installed_client':False,'notes':['Remote refs are read-only observations; write access and external agent/API facilities are not certified by this helper.']},'next_action':'Reconcile an existing run before continuation; otherwise reserve a distinct isolated workspace.'}


def write_new(path, value):
    """Write screened JSON exclusively to a new evidence path.

    Args:
        path: Caller-selected output path; missing parents are created.
        value: JSON-serializable non-secret content.

    Raises:
        Stop: Output already exists (including dangling symlinks) or screening
            rejects a value.
        OSError: Directory/file creation or writing fails.

    An exclusive leaf create preserves older attempts. The JSON write is not
    atomic; an interrupted write can leave a new incomplete attempt."""
    path=Path(path)
    if path.exists() or path.is_symlink(): raise Stop('output_occupied','Retain existing evidence and choose a new output path.')
    no_secret(value)
    path.parent.mkdir(parents=True,exist_ok=True)
    # Exclusive create preserves original attempts rather than silently replacing them.
    with path.open('x') as stream: json.dump(value,stream,indent=2,sort_keys=True); stream.write('\n')


def prepare(inputs, source, workspace):
    """Create a fresh isolated clone containing pinned package/provenance only.

    Args:
        inputs: Validated fresh-run configuration; run_id is not allowed.
        source: Source package checkout used for pinning.
        workspace: Explicit absent destination, including no dangling symlink.

    Returns:
        Preflight data updated with new workspace and pinned resource paths.

    Raises:
        Stop: Discovery/pinning failure, resume request, occupied destination or
            run resources, or clone/remote configuration failure.
        OSError: Workspace or resource writing fails.

    Writes only the new clone/resources and bounded empty-repository operating
    files; preserves its authorized origin. Never commits, pushes, authenticates
    or implements TextStats. Failure may leave a partial new workspace; this is
    not a rollback or resume driver."""
    info=preflight(inputs,source)
    if inputs.get('run_id'): raise Stop('resume_not_fresh','Use observe with the retained checkpoint; do not replay setup.')
    if workspace is None: raise Stop('workspace_required','Select an explicit new isolated workspace using --workspace.')
    requested=Path(workspace).expanduser()
    if requested.exists() or requested.is_symlink(): raise Stop('workspace_occupied')
    target=requested.resolve()
    if target.exists() or target.is_symlink(): raise Stop('workspace_occupied')
    target.parent.mkdir(parents=True,exist_ok=True)
    source_repo=info['repository']['local_checkout'] or inputs['test_repository']
    git(source,'clone','--no-hardlinks','--',source_repo,str(target))
    # Never copy source workfiles, staging, credentials or consumer implementation fixtures.
    vendor=target/'textstats-run-resources/plugin'
    if vendor.parent.exists(): raise Stop('run_resources_occupied')
    pinned,files=package(source,inputs)
    for name,data in files.items():
        path=vendor/name
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
        path.chmod(0o755 if pinned['package_file_modes'][name]=='100755' else 0o644)
    pinned['snapshot_path']=str(vendor)
    manifest=vendor.parent/'PLUGIN-SOURCE.json'
    pinned['manifest_path']=str(manifest)
    if inputs['source_mode']=='dirty':
        diff=git(source,'diff','--binary',pinned['commit'],'--',*PACKAGE_PATHS,binary=True).stdout
        clean_bytes(diff)
        (vendor.parent/'DIRTY-DIFF.patch').write_bytes(diff)
        pinned['dirty_diff_path']=str(vendor.parent/'DIRTY-DIFF.patch')
        # Untracked package paths are represented exactly by the snapshot and hash manifest.
    write_new(manifest,pinned)
    if not info['repository']['head']:
        if not (target/'AGENTS.md').exists(): (target/'AGENTS.md').write_text('This is a dedicated SDD Manager plugin test repository. Follow the pinned skills in textstats-run-resources/plugin/skills. Product documents and implementation must be generated through the authorized consumer workflows. Credentials remain protected and outside evidence.\n')
        if not (target/'.gitignore').exists(): (target/'.gitignore').write_text('*.tkn\n.env\n.env.*\n')
    # Preserve the authorized hosted destination when the clone origin is a local checkout.
    if info['repository']['local_checkout']:
        git(target,'remote','set-url','origin',info['repository']['remote_url'])
    info['plugin_source']=pinned
    info['workspace']=str(target)
    info['next_action']='Inspect preserved repository instructions and reserve/publish owned setup evidence through the pinned plugin protocols; no helper commit or push occurred.'
    return info


def paths(repo,*args):
    """Return sorted nonempty paths from a selected NUL-delimited Git query.

    Arguments must request NUL-delimited path output. UTF-8 path decoding and
    required Git errors propagate; no workspace write is performed here."""
    return sorted(filter(None,git(repo,*args,binary=True).stdout.decode('utf-8').split('\x00')))


def ancestor_containment(root, candidate, destination):
    """Prove commit containment/non-containment locally, or return None.

    Args:
        root: Checkout containing the candidate/destination commit objects.
        candidate: Commit whose publication is being assessed.
        destination: Observed remote destination tip.

    Returns:
        True for proven ancestry; False for non-ancestry with usable complete
        local graphs; None for unavailable objects/ancestry or shallow uncertainty.

    Does not fetch missing objects or authorize an operation retry."""
    try:
        if any(git(root,'cat-file','-e',commit+'^{commit}',required=False).returncode for commit in (candidate,destination)): return None
        result=git(root,'merge-base','--is-ancestor',candidate,destination,required=False)
        if result.returncode==0: return True
        if result.returncode!=1: return None
        shallow=git(root,'rev-parse','--is-shallow-repository',required=False)
        if shallow.returncode or shallow.stdout.strip()!='false': return None
        # Endpoint availability alone does not establish a complete usable commit graph.
        if git(root,'rev-list','--parents',candidate,destination,required=False).returncode: return None
        return False
    except Stop:
        return None


def observe_git(repo_info):
    """Capture actual checkout/index/merge state against supplied remote readback.

    Args:
        repo_info: repository() result with local_checkout/remote_observation.

    Returns:
        HEAD/branch/parents, exact index stages, changed paths, local refs/worktrees
        and publication/containment assessment. Unknown ancestry/access remains
        unknown; local tracking refs do not establish publication.

    Raises:
        Stop: No local checkout, unavailable required Git data or unsafe metadata.

    Reads the checkout and uses the provided remote observation; it does not
    fetch, mutate index/files or independently refresh that observation."""
    root=repo_info['local_checkout']
    if not root: raise Stop('local_checkout_required')
    head=git(root,'rev-parse','--verify','HEAD',required=False).stdout.strip() or None
    branch=git(root,'symbolic-ref','--quiet','--short','HEAD',required=False).stdout.strip() or None
    parents=git(root,'rev-list','--parents','-n','1',head).stdout.split()[1:] if head else []
    merge_path=Path(git(root,'rev-parse','--git-path','MERGE_HEAD').stdout.strip())
    if not merge_path.is_absolute(): merge_path=Path(root)/merge_path
    merges=merge_path.read_text().splitlines() if merge_path.exists() else []
    index=[]
    for row in git(root,'ls-files','--stage','-z',binary=True).stdout.decode().split('\x00'):
        if not row: continue
        metadata,path=row.split('\t',1)
        mode,oid,stage=metadata.split()
        index.append({'path':path,'mode':mode,'oid':oid,'stage':int(stage)})
    no_secret(index)
    remote=repo_info['remote_observation']
    destination=remote['refs'].get('refs/heads/'+branch) if branch else None
    publication='unknown'
    containment='unavailable'
    if remote['status']=='observed' and branch and head:
        publication='unpublished'
        containment='absent'
        if destination==head: publication='published'; containment='equal'
        elif destination:
            proven=ancestor_containment(root,head,destination)
            if proven is True:
                publication='published'; containment='ancestor'
            elif proven is None:
                publication='unknown'; containment='ancestry-unavailable'
    return {'head':head,'branch':branch,'parents':parents,'merge_heads':merges,'index':index,'staged_paths':paths(root,'diff','--cached','--name-only','-z'),'unstaged_paths':paths(root,'diff','--name-only','-z'),'untracked_paths':paths(root,'ls-files','--others','--exclude-standard','-z'),'conflict_paths':sorted({e['path'] for e in index if e['stage']}),'refs':git(root,'for-each-ref','--format=%(objectname) %(refname)').stdout.splitlines(),'worktrees':git(root,'worktree','list','--porcelain').stdout.splitlines(),'publication':publication,'remote_containment':containment,'remote_heads':remote['refs'],'remote_observation_status':remote['status']}


def reconcile(actual, state, repo_info):
    """Assess a recorded pending effect from actual destination evidence.

    Args:
        actual: Current observe_git() result.
        state: Validated checkpoint, or None.
        repo_info: Resolved repository and remote identity.

    Returns:
        Effect category and retry_safe false. An explicit pending ref overrides
        branch fallback; repository mismatch/unavailable containment stays unknown.
        Uncertain API effects require separate hosted readback.

    Never replays a write or infers that readback itself authorizes replay."""
    operation=(state or {}).get('pending_operation')
    result={'effect':'none','retry_safe':False}
    if not operation: return result
    if operation['kind']=='push':
        identity=operation.get('identity',{})
        recorded_repository=identity.get('repository')
        if recorded_repository and normalize(recorded_repository) not in {normalize(repo_info['identity']), normalize(repo_info['remote_url'])}:
            result['effect']='unknown'
            return result
        branch=identity.get('branch') or actual['branch']
        commit=identity.get('commit') or actual['head']
        ref=identity.get('ref') or ('refs/heads/'+branch if branch else None)
        remote=actual['remote_heads'].get(ref)
        if commit and remote==commit: result['effect']='observed-published'
        elif actual['remote_observation_status']=='observed' and ref and commit:
            if remote is None: result['effect']='not-observed-at-destination'
            else:
                proven=ancestor_containment(repo_info['local_checkout'],commit,remote)
                result['effect']='observed-published' if proven is True else 'not-observed-at-destination' if proven is False else 'unknown'
        else: result['effect']='unknown'
    elif operation['status']=='uncertain': result['effect']='unknown'
    else: result['effect']='unfinished'
    return result


def export_recovery(root, actual, output, state=None):
    # Git runs in the consumer checkout; Python and Git must share the caller's path.
    # Keep the lexical target so dangling symlinks still count as occupied evidence.
    """Export bounded Git/index/nonignored work state beside a new output path.

    Args:
        root: Consumer checkout; its files/index/refs remain unchanged.
        actual: Current observe_git() state to export, not a stale checkpoint.
        output: Observation path; export is an adjacent .recovery directory.
        state: Optional checkpoint supplying additional retained commit roots.

    Returns:
        Absolute export path, manifest hash, declared completeness and local-only
        publication. Completeness covers declared eligible state, not credentials,
        ignored files, submodule working state or arbitrary machine resources.

    Raises:
        Stop: Occupied export, sensitive content, unsafe work paths or unavailable
            required Git operations.
        OSError: Artifact reading/writing fails.

    Writes hashed blobs/workfiles, patches, merge metadata and, when eligible, a
    verified bundle. Protected paths are omitted without reading content;
    protected history or unavailable required roots prevent a complete export.
    Failure may leave partial new artifacts. Restoration/publication is external
    coordinator work and requires independent integrity/equivalence checks."""
    destination=Path(str(output)+'.recovery').absolute()
    if destination.exists() or destination.is_symlink(): raise Stop('recovery_export_occupied')
    # Inspect eligible content before writing an export, excluding protected paths entirely.
    index=[e for e in actual['index'] if not protected(e['path'])]
    omitted=any(protected(e['path']) for e in actual['index'])
    objects={}
    for entry in index:
        if entry['mode']=='160000': omitted=True; continue
        objects[entry['oid']]=clean_bytes(git(root,'cat-file','blob',entry['oid'],binary=True).stdout)
    workfiles=[]
    files={}
    eligible=sorted({e['path'] for e in index}|set(actual['untracked_paths']))
    for name in eligible:
        if protected(name): continue
        path=Path(root)/name
        if not path.parent.resolve().is_relative_to(Path(root).resolve()): raise Stop('unsafe_recovery_path')
        if path.is_symlink():
            target=os.readlink(path)
            no_secret(target)
            workfiles.append({'path':name,'kind':'symlink','target':target})
        elif path.is_file():
            content=clean_bytes(path.read_bytes())
            sha=hashlib.sha256(content).hexdigest()
            files[sha]=content
            workfiles.append({'path':name,'kind':'file','sha256':sha,'mode':stat.S_IMODE(path.stat().st_mode)})
        elif not path.exists(): workfiles.append({'path':name,'kind':'deleted'})
        else: omitted=True
    merge_metadata={}
    for name in ('MERGE_HEAD','MERGE_MSG','MERGE_MODE','ORIG_HEAD'):
        path=Path(git(root,'rev-parse','--git-path',name).stdout.strip())
        if not path.is_absolute(): path=Path(root)/path
        if path.exists(): merge_metadata[name]=clean_bytes(path.read_bytes()).decode()
    extra_roots=set(actual['merge_heads'])
    if merge_metadata.get('ORIG_HEAD'): extra_roots.update(merge_metadata['ORIG_HEAD'].splitlines())
    for key,value in (state or {}).get('checkpoint_refs',{}).items():
        if key.endswith('_commit'): extra_roots.add(value)
        elif key=='merge_parents': extra_roots.update(value)
    pending=(state or {}).get('pending_operation') or {}
    if pending.get('identity',{}).get('commit'): extra_roots.add(pending['identity']['commit'])
    available_roots=[]
    for sha in sorted(extra_roots):
        if git(root,'cat-file','-e',sha+'^{commit}',required=False).returncode: omitted=True
        else: available_roots.append(sha)
    # A bundle contains reachable history, not merely the current tree: reject protected historical paths/content.
    history=git(root,'rev-list','--objects','--all',*(['HEAD'] if actual['head'] else []),*available_roots,required=False).stdout.splitlines()
    safe_bundle=not omitted
    for line in history:
        oid,_,name=line.partition(' ')
        if name and protected(name): safe_bundle=False; continue
        typ=git(root,'cat-file','-t',oid).stdout.strip()
        if typ in {'blob','commit','tag'} and safe_bundle: clean_bytes(git(root,'cat-file',typ,oid,binary=True).stdout)
    destination.mkdir(parents=True)
    for directory,contents in [('blobs',objects),('files',files)]:
        (destination/directory).mkdir()
        for name,content in contents.items(): (destination/directory/name).write_bytes(content)
    bundle=None
    if actual['head'] and safe_bundle:
        bundle=destination/'objects.bundle'
        git(root,'bundle','create',str(bundle),'--all','HEAD',*available_roots)
        git(root,'bundle','verify',str(bundle))
    patches={}
    for label,args in [('staged',['diff','--cached','--binary']),('unstaged',['diff','--binary'])]:
        # Protected paths stay out of patches. Index/blob/workfile exports are authoritative.
        allowed=sorted({e['path'] for e in index})
        if allowed:
            content=clean_bytes(git(root,*args,'--',*allowed,binary=True).stdout)
            filename=label+'.patch'
            (destination/filename).write_bytes(content)
            patches[label]=filename
    manifest={'schema_version':1,'head':actual['head'],'branch':actual['branch'],'parents':actual['parents'],'merge_heads':actual['merge_heads'],'index':index,'tracked_paths':paths(root,'ls-tree','-r','--name-only','-z',actual['head']) if actual['head'] else [],'merge_metadata':merge_metadata,'retained_commit_roots':available_roots,'workfiles':workfiles,'patches':patches,'complete':safe_bundle,'bundle':'objects.bundle' if bundle else None,'omitted_protected_state':omitted,'publication':'local-only'}
    manifest['artifact_hashes']={str(p.relative_to(destination)):hashlib.sha256(p.read_bytes()).hexdigest() for p in destination.rglob('*') if p.is_file()}
    write_new(destination/'manifest.json',manifest)
    return {'path':str(destination),'complete':safe_bundle,'publication':'local-only','manifest_sha256':hashlib.sha256((destination/'manifest.json').read_bytes()).hexdigest()}


def observation(inputs,state,output,exports=True):
    """Combine real repository/Git state, pending-effect assessment and exports.

    Args:
        inputs: Resolved configuration.
        state: Validated checkpoint used only as pending-operation context.
        output: Caller-selected new observation path for export placement.
        exports: Whether to create adjacent recovery artifacts.

    Returns:
        Non-secret observation and continuation advice; recorded checkpoint state
        is explicitly not trusted as current reality. Does not write output JSON.

    Reads the consumer and optionally writes recovery artifacts; no operation is
    replayed. Discovery/export failures propagate to the CLI."""
    repo=repository(inputs)
    actual=observe_git(repo)
    effect=reconcile(actual,state,repo)
    if actual['conflict_paths'] or actual['merge_heads']: action='Preserve merge/index stages and continue the same scoped resolution and required checks.'
    elif actual['staged_paths'] or actual['unstaged_paths'] or actual['untracked_paths']: action='Preserve actual staged/unstaged ownership and continue the same unfinished work; do not replay setup.'
    elif actual['publication']=='unpublished': action='Reconcile and publish the existing commit before selecting new work.'
    elif effect['effect']=='unknown': action='Read the exact established destination identity before retry; retain unknown effect if unavailable.'
    else: action='Verify retained assessment/source/scope and select the next authorized action.'
    data={'schema_version':1,'repository':repo,'git':actual,'reconciliation':effect,'next_action':action,'checkpoint_trusted_as_actual_state':False}
    if exports: data['recovery']=export_recovery(repo['local_checkout'],actual,output,state)
    return data


def relative(root,name):
    """Resolve a safe nonprotected check path beneath a repository root.

    Rejects absolute/parent-traversal paths, leaf symlinks and resolved escapes.
    Existence is caller-specific. Ownership additionally rejects symlink parents.
    Raises Stop with invalid_check_path without exposing the failed value."""
    if not isinstance(name,str) or not name or Path(name).is_absolute() or '..' in Path(name).parts or protected(name): raise Stop('invalid_check_path')
    path=Path(root)/name
    if path.is_symlink() or not path.resolve().is_relative_to(Path(root).resolve()): raise Stop('invalid_check_path')
    return path


def task_history(path):
    """Classify historical/vendor parent directories excluded from active owners.

    The filename itself is not a history marker. This is the retained bundle
    convention, not a general repository archival detector."""
    return any('archive' in part.lower() or part.lower() in {'.git', 'features', 'reviews', 'textstats-run-resources'} for part in Path(path).parts[:-1])


def validate_task_documents(documents):
    """Validate the additive ownership option without opening any document.

    Args:
        documents: Nonempty list of unique normalized slash-separated Markdown
            paths, relative to the consumer repository root.

    Returns:
        The original list when syntax, protection and history exclusions hold.

    Raises:
        Stop: Invalid option shape/path (invalid_contract).

    Catalog and runtime use this same syntax contract; runtime separately checks
    existence, file kind and symlinks. This does not certify list completeness."""
    if not isinstance(documents, list) or not documents: raise Stop('invalid_contract')
    seen = set()
    for name in documents:
        if not isinstance(name, str) or not name or any(c in name for c in ('\\', ':', '\x00')):
            raise Stop('invalid_contract')
        path = PurePosixPath(name)
        if path.is_absolute() or str(path) != name or any(part in {'.', '..'} for part in path.parts) or not name.endswith('.md') or protected(name) or task_history(name) or name in seen:
            raise Stop('invalid_contract')
        seen.add(name)
    return documents


def task_identifier(value):
    """Return exact case-sensitive ID from a supported plain/code/bold token.

    Accepts ASCII alphanumeric segments joined by hyphens/underscores, beginning
    with a letter and containing a digit or separator. Raises Stop for malformed
    or ambiguous tokens; never truncates a bad ID into a valid prefix."""
    value = value.strip()
    if value.startswith('`') and value.endswith('`'): value = value[1:-1]
    elif value.startswith('**') and value.endswith('**'): value = value[2:-2]
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*', value) or not any(c.isdigit() or c in '-_' for c in value):
        raise Stop('invalid_task_identifier')
    return value


def task_lines(content):
    """Yield original line numbers/text outside supported fenced examples.

    Backtick/tilde fences may be indented in task details. Closing markers must
    match kind, meet opening length and have no text suffix. Unclosed/malformed
    fences raise Stop; the generator must be exhausted to establish validity."""
    fence = None
    for number, line in enumerate(content.splitlines(), 1):
        marker = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip(): fence = None
            continue
        if marker:
            if marker[1][0] == '`' and '`' in marker[2]: raise Stop('invalid_task_collection')
            fence = (marker[1][0], len(marker[1]))
            continue
        yield number, line
    if fence: raise Stop('invalid_task_collection')


def task_rows(content):
    """Yield (line, ID, status) from supported executable checkbox/table rows.

    Phase/milestone checkbox parents are excluded; task IDs preserve identity.
    Tables need one ID/Task ID and Status column plus a separator row. Fenced
    examples are skipped; malformed candidates raise Stop instead of disappearing.
    Status strings represent source claims, not verified completion."""
    headers = None
    separator = False
    for number, line in task_lines(content):
        checkbox = re.match(r'^\s*[-*+]\s+\[([^]]*)\](?:\s+(.*))?$', line)
        if checkbox:
            if headers is not None and not separator: raise Stop('invalid_task_collection')
            headers = None
            text = checkbox[2] or ''
            if checkbox[1] not in {' ', 'x', 'X'}: raise Stop('invalid_task_collection')
            if re.match(r'^(?:Phase|Milestone)\s+[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*(?:\s|$)', text): continue
            token = text.split()[0] if text.split() else ''
            yield number, task_identifier(token), 'Checked' if checkbox[1].lower() == 'x' else 'Unchecked'
        elif line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
            normalized = [cell.strip('`*').lower().replace(' ', '_') for cell in cells]
            if 'id' in normalized or 'task_id' in normalized:
                if headers is not None and not separator: raise Stop('invalid_task_collection')
                if sum(normalized.count(key) for key in ('id', 'task_id')) != 1 or normalized.count('status') != 1 or len(set(normalized)) != len(normalized):
                    raise Stop('invalid_task_collection')
                headers, separator = normalized, False
            elif headers is not None:
                if len(cells) != len(headers): raise Stop('invalid_task_collection')
                is_separator = all(re.fullmatch(r':?-+:?', cell) for cell in cells)
                if not separator:
                    if not is_separator: raise Stop('invalid_task_collection')
                    separator = True
                else:
                    if is_separator: raise Stop('invalid_task_collection')
                    row = dict(zip(headers, cells))
                    if not row['status']: raise Stop('invalid_task_collection')
                    yield number, task_identifier(row.get('id', row.get('task_id'))), row['status']
            elif 'status' in normalized:
                raise Stop('invalid_task_collection')
        else:
            if headers is not None and not separator: raise Stop('invalid_task_collection')
            headers = None
    if headers is not None and not separator: raise Stop('invalid_task_collection')


def ownership(root, documents=None):
    """Collect actual executable owners from active roots and explicit children.

    Args:
        root: Consumer repository root.
        documents: Optional additive list validated by validate_task_documents().

    Returns:
        Inspected relative document paths and a map from exact task ID to its
        document, original line number and source status.

    Raises:
        Stop: Unsafe/missing document, malformed candidate/fence, duplicate task
            ID or empty task collection.

    Reads non-secret Markdown only. History/vendor roots and ordinary links are
    excluded; repeated selection of one document is deduplicated. Independent
    assessment must establish whether the selected lists cover the project."""
    root = Path(root).resolve()
    selected = sorted(p for p in root.rglob('*.md') if p.name in {'TASKS.md', 'FEATURE-TASKS.md'} and not task_history(p.relative_to(root)))
    if documents is not None:
        selected.extend(root / name for name in validate_task_documents(documents))
    owners, inspected, seen = {}, [], set()
    for path in selected:
        rel = path.relative_to(root)
        path = relative(root, str(rel))
        if any(parent.is_symlink() for parent in path.parents if parent.is_relative_to(root)) or not path.is_file():
            raise Stop('invalid_task_document')
        if path in seen: continue
        seen.add(path)
        inspected.append(str(rel))
        content = clean_bytes(path.read_bytes()).decode()
        for number, identifier, status in task_rows(content):
            if identifier in owners: raise Stop('duplicate_task_ownership')
            owners[identifier] = {'document': str(rel), 'line': number, 'status': status}
    if not owners: raise Stop('empty_task_collection')
    return {'documents': inspected, 'owners': owners}


def assessment(inputs,state,contract_path,evidence_path):
    """Evaluate strict deterministic checks without running product commands.

    Args:
        inputs: Resolved repository configuration.
        state: Validated checkpoint for optional expected_ref bindings.
        contract_path: Optional version 1 DSL path; None yields Not run.
        evidence_path: Optional independently captured literal evidence path.

    Returns:
        (result, exit_code): code 0 for passed/Not run, 1 for failed invariants.
        Result always states agent_behavior_assessed false.

    Raises:
        Stop: Invalid contract/path/source evidence or prerequisite data. Ordinary
            missing literal/ownership invariants are recorded as failed checks.

    Reads actual files/Git/owners and supplied literals, never authenticates,
    commits, repairs or writes the result. Expected refs do not prove freshness."""
    if not contract_path:
        return {'schema_version':1,'status':'Not run','checks':[],'agent_behavior_assessed':False,'reason':'No deterministic contract supplied.'},0
    contract=load(contract_path)
    if type(contract) is not dict or set(contract)-{'schema_version','checks','required_agent_checks','case_id','variant_agent_checks'} or not exact(contract.get('schema_version'),1): raise Stop('invalid_contract')
    checks=contract.get('checks')
    if not isinstance(checks,list) or not checks: raise Stop('empty_check_collection')
    if 'required_agent_checks' in contract and (not isinstance(contract['required_agent_checks'],list) or not all(isinstance(x,str) and x for x in contract['required_agent_checks'])): raise Stop('invalid_contract')
    if 'case_id' in contract and not re.fullmatch(r'A-0(0[1-9]|1[0-9]|2[0-7])',str(contract['case_id'])): raise Stop('invalid_contract')
    variant_checks=contract.get('variant_agent_checks',{})
    if not isinstance(variant_checks,dict) or any(not re.fullmatch('[a-z][a-z0-9-]*',str(k)) or not isinstance(v,list) or not v or any(not isinstance(x,str) or not x for x in v) for k,v in variant_checks.items()):raise Stop('invalid_contract')
    selected_variant=(state or {}).get('variant')
    if selected_variant and variant_checks and selected_variant not in variant_checks:raise Stop('invalid_contract')
    agent_checks=contract.get('required_agent_checks',[])+variant_checks.get(selected_variant,[])
    evidence=load(evidence_path) if evidence_path else None
    if evidence is not None and (type(evidence) is not dict or set(evidence)!={'schema_version','literals'} or not exact(evidence['schema_version'],1) or type(evidence['literals']) is not dict): raise Stop('invalid_evidence')
    needs_remote=any(c.get('kind')=='git' and c.get('field') in {'publication','remote_containment'} for c in checks)
    repo=repository(inputs,observe_remote=needs_remote)
    if not repo['local_checkout']: raise Stop('local_checkout_required')
    actual_git=None
    rows=[]
    identifiers=set()
    for check in checks:
        if type(check) is not dict or type(check.get('id')) is not str or not check['id'] or check['id'] in identifiers: raise Stop('invalid_contract')
        identifiers.add(check['id'])
        kind=check.get('kind')
        allowed={'literal':{'id','kind','key','expected'},'git':{'id','kind','field','expected','expected_ref'},'file':{'id','kind','path','exists','sha256'},'task_ownership':{'id','kind','documents'}}
        if kind not in allowed or set(check)-allowed[kind]: raise Stop('invalid_contract')
        if kind == 'task_ownership' and 'documents' in check: validate_task_documents(check['documents'])
        expected=check.get('expected')
        if kind=='git':
            if ('expected' in check)==('expected_ref' in check): raise Stop('invalid_contract')
            if 'expected_ref' in check:
                ref=check['expected_ref']
                if not isinstance(ref,str) or not re.fullmatch(r'checkpoint_refs\.[A-Za-z_]+',ref) or state is None: raise Stop('invalid_expected_ref')
                field=ref.split('.')[1]
                if field not in state['checkpoint_refs']: raise Stop('invalid_expected_ref')
                expected=state['checkpoint_refs'][field]
        try:
            if kind=='literal':
                if 'expected' not in check or not isinstance(check.get('key'),str): raise Stop('invalid_contract')
                if evidence is None or check['key'] not in evidence['literals']: raise Stop('missing_literal_evidence')
                passed=exact(evidence['literals'][check['key']],expected)
            elif kind=='git':
                fields={'head','branch','parents','merge_heads','staged_paths','unstaged_paths','untracked_paths','conflict_paths','publication','remote_containment'}
                if check.get('field') not in fields: raise Stop('invalid_contract')
                if actual_git is None: actual_git=observe_git(repo)
                passed=exact(actual_git[check['field']],expected)
            elif kind=='file':
                path=relative(repo['local_checkout'],check.get('path'))
                if 'exists' not in check and 'sha256' not in check: raise Stop('invalid_contract')
                if 'exists' in check and type(check['exists']) is not bool: raise Stop('invalid_contract')
                if 'sha256' in check and not re.fullmatch('[0-9a-f]{64}',str(check['sha256'])): raise Stop('invalid_contract')
                passed=('exists' not in check or path.exists()==check['exists'])
                if 'sha256' in check: passed=passed and path.is_file() and hashlib.sha256(clean_bytes(path.read_bytes())).hexdigest()==check['sha256']
            else:
                ownership(repo['local_checkout'], check.get('documents')); passed=True
            rows.append({'id':check['id'],'status':'Passed' if passed else 'Failed','reason':'Literal invariant satisfied.' if passed else 'Literal invariant differs.'})
        except Stop as error:
            if error.cause in {'invalid_contract','invalid_check_path','invalid_expected_ref','sensitive_content_not_exportable'}: raise
            rows.append({'id':check['id'],'status':'Failed','reason':error.cause})
    failed=any(row['status']=='Failed' for row in rows)
    result={'schema_version':1,'status':'Checks failed' if failed else 'Checks passed','checks':rows,'agent_behavior_assessed':False,'required_agent_checks':agent_checks}
    if variant_checks:
        result['variant_selection_required']=selected_variant is None
        result['selected_variant']=selected_variant
        if selected_variant is None:
            result['available_variant_agent_checks']=variant_checks
            result['agent_assessment_limit']='Select a declared variant before independent grading; deterministic compatibility is not complete variant criteria.'
    return result,int(failed)


def main(command):
    """Dispatch one helper CLI and publish only a new screened output artifact.

    Args:
        command: preflight, prepare, observe or assess; argv supplies its inputs.

    Returns:
        0 for successful helper output, 1 for failed deterministic checks, or 2
        with generic non-secret stdout for blocked/invalid operations. argparse
        handles CLI usage failures separately.

    A failure never replaces existing evidence. Prepare/recovery side effects
    follow their own contracts; partial newly created artifacts may remain."""
    parser=argparse.ArgumentParser(description='TextStats portable coordinator support; no authentication, publication or agent workflow execution.')
    parser.add_argument('--inputs',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    if command in {'preflight','prepare'}: parser.add_argument('--source-root',type=Path,default=SOURCE)
    if command=='prepare': parser.add_argument('--workspace',type=Path)
    if command in {'observe','assess'}: parser.add_argument('--run-state',required=True,type=Path)
    if command=='assess':
        parser.add_argument('--contract',type=Path)
        parser.add_argument('--evidence',type=Path)
    args=parser.parse_args()
    try:
        inputs=configuration(args.inputs)
        state=checkpoint(getattr(args,'run_state',None),inputs)
        if args.output.exists() or args.output.is_symlink(): raise Stop('output_occupied')
        code=0
        if command=='preflight': result=preflight(inputs,args.source_root)
        elif command=='prepare': result=prepare(inputs,args.source_root,args.workspace)
        elif command=='observe': result=observation(inputs,state,args.output)
        else: result,code=assessment(inputs,state,args.contract,args.evidence)
        write_new(args.output,result)
        return code
    except Stop as error:
        print(json.dumps({'schema_version':1,'status':'Blocked','cause':error.cause,'next_action':error.action}))
        return 2
    except (OSError,ValueError,TypeError,KeyError,UnicodeError):
        # Never interpolate failed values, provider bodies, Git stderr or credential paths.
        print(json.dumps({'schema_version':1,'status':'Blocked','cause':'support_operation_failed','next_action':'Inspect sanitized prerequisites and retain existing work before retrying.'}))
        return 2
