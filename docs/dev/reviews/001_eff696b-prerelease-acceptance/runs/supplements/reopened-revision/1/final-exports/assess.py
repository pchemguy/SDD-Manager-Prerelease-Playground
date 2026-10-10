import pathlib,subprocess,json,hashlib,shutil,sys,os
B=pathlib.Path('/workspace/scratch/46b31bb4dff6');R=B/'037-sup-reopened-revision';O=B/'037-sup-reopened-final-artifacts';P=O/'private-original';U=O/'public';records=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def cmd(args,cwd=R):
 i=len(records);r=subprocess.run(args,cwd=cwd,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});p=f'commands/{i:03}';(P/'commands').mkdir(exist_ok=True);(P/(p+'.stdout')).write_bytes(r.stdout);(P/(p+'.stderr')).write_bytes(r.stderr);records.append({'argv':args,'cwd':str(cwd),'exit':r.returncode,'stdout':p+'.stdout','stderr':p+'.stderr'});return r
def git(*args):return cmd(['git','--no-optional-locks',*args])
S=json.loads((B/'037-sup-reopened-setup/START.json').read_bytes());Dbytes=(B/'037-sup-reopened-consumer-observations.json').read_bytes();D=json.loads(Dbytes);(P/'consumer-observations.json').write_bytes(Dbytes);assert sha(Dbytes)=='9b2c329f976b46bfa5ff09ae52efbc748dfba2cd9e9baa6e3054d4edd3a14777'
Gpath='docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/supplements/reopened-revision/1/artifact-acceptance/ARTIFACT-DECISION.json';E=B/'037-test-evidence';gbytes=cmd(['git','--no-optional-locks','show','6eca5ef55b0d8c6068a611ad1bbdd1763df3f8b0:'+Gpath],E).stdout;G=json.loads(gbytes);(P/'ARTIFACT-DECISION.json').write_bytes(gbytes)
for name,h in D['sidecars'].items():
 data=(B/name).read_bytes();assert sha(data)==h;(P/name).write_bytes(data)
checks={};checks['seal_hash']=sha(Dbytes);checks['latest_first_parent_merge']=git('log','--first-parent','--merges','-1','--format=%H',S['head']).stdout.decode().strip()==S['head'];checks['previous_merge_parents']=git('show','-s','--format=%P',S['head']).stdout.decode().split()==S['parents']
head=git('rev-parse','HEAD').stdout.decode().strip();branch=git('branch','--show-current').stdout.decode().strip();checks['returned_head']=head==D['integration']['merge'];checks['returned_parent_branch']=branch==S['branch'];checks['clean_worktree']=git('status','--porcelain=v1').stdout==b'';checks['no_unmerged']=git('ls-files','-u').stdout==b''
parents=git('show','-s','--format=%P',head).stdout.decode().split();checks['explicit_amended_tip_integration']=parents==[S['head'],D['candidate']];checks['retained_original_opening']=git('merge-base','--is-ancestor',S['original_opening'],head).returncode==0
owned=[a['path'] for a in G['artifacts']];changed=git('diff','--name-only',S['head'],head).stdout.decode().splitlines();checks['exact_accepted_scope']=sorted(changed)==sorted(owned)
changed_files=[]
for p,m in S['tracked_files'].items():
 data=(R/p).read_bytes();dest=P/'tracked-files'/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 if sha(data)!=m['sha256'] or oct((R/p).stat().st_mode&0o777)!=m['mode']:changed_files.append(p)
checks['baseline_587_preservation_except_owned']=len(S['tracked_files'])==587 and sorted(changed_files)==sorted(owned)
index=git('ls-files','-s','-z').stdout;(P/'index-entries.nul').write_bytes(index);gitdir=pathlib.Path(git('rev-parse','--absolute-git-dir').stdout.decode().strip());(P/'index').write_bytes((gitdir/'index').read_bytes());checks['index_matches_head']=git('diff','--cached','--quiet').returncode==0
frozen=[p for p in S['tracked_files'] if any('/'+n in p for n in ['038_','039_','040_','041_'])];checks['frozen_038_041_entries_preserved']=git('diff','--raw',S['head'],head,'--',*frozen).stdout==b'';checks['frozen_path_count']=len(frozen)
for a in G['artifacts']:
 p=a['path'];data=(R/p).read_bytes();old=git('show',S['head']+':'+p).stdout;checks['retained_prefix:'+p]=data.startswith(old);checks['accepted_hash:'+p]=sha(data)==a['sha256'];checks['accepted_blob:'+p]=git('rev-parse',D['candidate']+':'+p).stdout.decode().strip()==a['git_blob']
summary=git('show','-s','--format=%B',head).stdout.decode();checks['cumulative_provenance_summary']=all(x in summary for x in [S['original_opening'],S['original_baseline'],S['head'],'V-001','V-002','eight','zero','retained','publication/readback','suspended'])
refs=git('show-ref').stdout;(P/'refs.txt').write_bytes(refs);checks['local_remote_exact_refs']=True
for entry in D['per_owned_commit_publication']:
 rb=git('ls-remote','trial-delivery',entry['ref']).stdout.decode().strip();checks['local_remote_exact_refs'] &= rb==entry['commit']+'\t'+entry['ref']
checks['candidate_parent_reopening']=git('show','-s','--format=%P',D['candidate']).stdout.decode().strip()==S['head'];checks['owned_commits_exactly_action_and_merge']=set(git('rev-list',S['head']+'..'+head).stdout.decode().split())=={D['candidate'],head};checks['source_hashes_unchanged']=all(sha((R/p).read_bytes())==h for p,h in D['loaded_resource_sha256'].items())
checks['diff_check']=git('diff','--check',S['head'],head).returncode==0
checks['complete_bundle_created']=git('bundle','create',str(P/'repository.bundle'),'--all').returncode==0;checks['complete_bundle_verified']=git('bundle','verify',str(P/'repository.bundle')).returncode==0
(P/'commands.json').write_text(json.dumps(records,indent=2)+'\n');(P/'checks.json').write_text(json.dumps(checks,indent=2)+'\n');(P/'assess.py').write_bytes(pathlib.Path(__file__).read_bytes())
# Retain original manifest before making public derivative.
def manifest(root):return {str(p.relative_to(root)):{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(root.rglob('*')) if p.is_file() and p.name!='HASH-MANIFEST.json'}
(P/'HASH-MANIFEST.json').write_text(json.dumps(manifest(P),indent=2)+'\n');original_manifest_hash=sha((P/'HASH-MANIFEST.json').read_bytes())
omit=['tracked-files/acceptance/textstats/tests/test_preflight.py','tracked-files/acceptance/textstats/tests/test_recovery.py']
for p in P.rglob('*'):
 if p.is_file() and str(p.relative_to(P)) not in omit:
  dest=U/p.relative_to(P);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
(U/'ORIGINAL-PROVENANCE.json').write_text(json.dumps({'private_original_manifest_sha256':original_manifest_hash,'public_derivative':'two exact source copies omitted; original unchanged','omissions':[{'path':p,**manifest(P)[p],'reason':'synthetic historical negative fixture literal flagged by unchanged clean_bytes'} for p in omit],'consumer_seal_sha256':sha(Dbytes)},indent=2)+'\n')
guard=B/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';sys.path.insert(0,str(guard.parent));import core
fail=[]
for p in U.rglob('*'):
 if p.is_file():
  try:
   core.clean_bytes(p.read_bytes())
   if p.suffix=='.json':core.no_secret(json.loads(p.read_bytes()))
  except Exception:fail.append(str(p.relative_to(U)))
(U/'GUARD-RESULT.json').write_text(json.dumps({'guard_path':str(guard),'guard_sha256':sha(guard.read_bytes()),'clean_bytes_all_public_files':not fail,'no_secret_json':not fail,'failure_paths':fail,'raw_matches_printed':False},indent=2)+'\n')
(U/'HASH-MANIFEST.json').write_text(json.dumps(manifest(U),indent=2)+'\n')
print(json.dumps({'boolean_failures':[k for k,v in checks.items() if v is False],'guard_failure_paths':fail,'files':len(manifest(U)),'original_manifest_sha256':original_manifest_hash,'head':head,'branch':branch}))
