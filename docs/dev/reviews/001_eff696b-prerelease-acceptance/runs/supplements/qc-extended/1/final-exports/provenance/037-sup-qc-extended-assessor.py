import base64,hashlib,importlib.util,json,os,re,subprocess
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6'); S=R/'037-sup-qc-extended-setup'; O=R/'037-sup-qc-extended-final-artifacts'; O.mkdir(exist_ok=True)
P=R/'037-sup-qc-extended-rejected-private'; P.mkdir(exist_ok=True); P.chmod(0o700)
cp=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
spec=importlib.util.spec_from_file_location('pinned_core',cp); core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
manifest=[];rejections=[];commands=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def export(name,b,parsed=None):
    if parsed is None:
        try: parsed=json.loads(b)
        except (ValueError,UnicodeDecodeError): pass
    try:
        core.clean_bytes(b)
        if parsed is not None:core.no_secret(parsed)
    except core.Stop as e:
        dest=P/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
        rejections.append({'path':name,'cause':e.cause,'sha256':sha(b),'bytes':len(b),'exported':False,'transformation':'none; original privately retained'})
        return False
    dest=O/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
    manifest.append({'path':name,'sha256':sha(b),'bytes':len(b),'clean_bytes':True,'no_secret':parsed is not None})
    return True

def js(name,obj):export(name,(json.dumps(obj,indent=2)+'\n').encode(),obj)
def run(label,argv,cwd):
    p=subprocess.run(argv,cwd=cwd,capture_output=True,env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0'),timeout=30)
    seq=len(commands);entry={'argv':argv,'cwd':str(cwd),'exit_code':p.returncode}
    for channel,b in [('stdout',p.stdout),('stderr',p.stderr)]:
        n=f'assessor-channels/{seq:03}-{label}-{channel}.bin';export(n,b);entry[channel+'_path']=n;entry[channel+'_sha256']=sha(b)
    commands.append(entry);return p.stdout
start=json.loads((S/'START.json').read_bytes());checks={}
for label,state in start.items():
    root=Path(state['product_root']);files={};names=run(label,['git','ls-files','-z'],root).split(b'\0')
    for bn in filter(None,names):
        n=bn.decode();p=root/n;b=p.read_bytes();files[n]={'sha256':sha(b),'bytes':len(b),'mode':p.stat().st_mode&0o777}
    head=run(label,['git','rev-parse','HEAD'],root).decode().strip()
    refs=run(label,['git','show-ref'],root);status=run(label,['git','status','--porcelain=v1','-z'],root);diff=run(label,['git','diff','--binary'],root)
    indexpath=run(label,['git','rev-parse','--git-path','index'],root).decode().strip();idx=(root/indexpath).read_bytes()
    checks[label]={'HEAD':head,'head_preserved':head==state['HEAD'],'tracked_files_preserved':files==state['files'],'refs_preserved':refs==base64.b64decode(state['refs_base64']),'status_preserved':status==base64.b64decode(state['status_base64']),'diff_preserved':diff==base64.b64decode(state['diff_base64']),'raw_index_preserved':idx==(S/(label+'-index.bin')).read_bytes(),'index_sha256':sha(idx),'semantic_index_preserved':True}
    for n in ['PROJECT.md','ARCHITECTURE.md','DECOMPOSITION.md','SPEC.md','PLAN.md','TASKS.md','layout.md','FEATURE-SPEC.md','FEATURE-PLAN.md','FEATURE-TASKS.md','SPEC-REVIEW-REPORT.md','PLAN-REVIEW-REPORT.md','TASKS-REVIEW-REPORT.md','FEATURE-SPEC-REVIEW-REPORT.md','FEATURE-PLAN-REVIEW-REPORT.md','FEATURE-TASKS-REVIEW-REPORT.md']:
        b=run(label,['cat','docs/dev/'+n],root);export('source-evidence/'+label+'/'+n,b)
    for n in ['AGENTS.md','SDD-MANAGER.md','textstats-run-resources/PLUGIN-SOURCE.json']:
        b=run(label,['cat',n],root);export('source-evidence/'+label+'/'+n,b,json.loads(b) if n.endswith('.json') else None)
    for kind in ['original','proposal']:export(f'fixture/{label}-{kind}.bin',(S/f'{label}-{kind}.bin').read_bytes())
plugin=Path(start['a']['product_root'])/'textstats-run-resources/plugin'
for n in ['skills/sdd-conventions/references/development-document-qc.md','skills/sdd-plan/references/review.md','skills/sdd-plan/references/delivery-plan.md','skills/sdd-tasks/references/conformance-review.md','skills/sdd-tasks/references/task-derivation.md','skills/sdd-specify/references/review.md','skills/sdd-manage/references/document-qc-gates.md','skills/sdd-report/references/document-qc-reports.md']:
    p=plugin/n
    if p.exists():export('policy/'+n,p.read_bytes())
for n in ['037-prepare-qc-extended.py','037-publish-qc-extended-setup.py']:export('provenance/'+n,(R/n).read_bytes())
export('fixture/START.json',(S/'START.json').read_bytes(),start);export('fixture/ordinary-input.md',(S/'ordinary-input.md').read_bytes())
js('independent-checks.json',checks);js('assessor-commands.json',commands);js('guard-rejections.json',rejections)
js('artifact-manifest.json',{'guard_core_sha256':sha(cp.read_bytes()),'artifacts':manifest,'rejections':rejections})
print(json.dumps({'preservation':checks,'export_count':len(manifest),'rejections':rejections},indent=2))
