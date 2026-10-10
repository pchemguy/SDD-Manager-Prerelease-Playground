import base64,hashlib,importlib.util,json,os,shutil,subprocess
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6'); p=R/'037-sup-split-boundary'; out=R/'037-sup-split-boundary-final-artifacts'
core=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
spec=importlib.util.spec_from_file_location('pinnedcore',core); c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
seal=R/'037-sup-split-boundary-consumer-observations.json'
assert hashlib.sha256(seal.read_bytes()).hexdigest()=='c18d0d725d7542054d297cfd50792ced9a3dd3a752066b3079141ba8f91b147e'
completed=json.loads(seal.read_bytes())
assert completed['finish_seal']['head']=='cdd50b67045f2811a529d3df5e66c91a23947650'
assert completed['continuation']['may_advance_to_T003'] is False
assert completed['continuation']['may_integrate'] is False
out.mkdir(exist_ok=False); logs=[]
def put(rel,b):
 c.clean_bytes(b)
 if str(rel).endswith('.json'):c.no_secret(json.loads(b))
 dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
def js(rel,v):c.no_secret(v);put(rel,(json.dumps(v,indent=2)+'\n').encode())
def git(args,cwd=p):
 argv=['git','--no-optional-locks',*args];q=subprocess.run(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1'})
 n=len(logs);put(f'commands/{n:03}-stdout.bin',q.stdout);put(f'commands/{n:03}-stderr.bin',q.stderr);logs.append({'argv':argv,'cwd':str(cwd),'exit':q.returncode,'stdout_sidecar':f'commands/{n:03}-stdout.bin','stderr_sidecar':f'commands/{n:03}-stderr.bin'});assert q.returncode==0;return q.stdout
start=json.loads((R/'037-sup-split-boundary-setup/START.json').read_bytes()); refs={k:start[k] for k in ('base','first','HEAD','actual_source')}
for f in (R/'037-sup-split-boundary-setup').iterdir():
 if f.is_file():put('setup/'+f.name,f.read_bytes())
for name in ('037-sup-split-boundary-consumer-observations.json',seal.name):put('consumer/'+name,(R/name).read_bytes())
put('selected-source/COMMON.md',(R/'SDD-Manager/acceptance/textstats/cases/assessor/COMMON.md').read_bytes())
put('selected-source/completion-and-checkpoints.md',(R/'SDD-Manager/skills/sdd-implement/references/completion-and-checkpoints.md').read_bytes())
put('selected-source/pinned-published-core.py',core.read_bytes())
for args in (['rev-parse','HEAD'],['show-ref'],['status','--porcelain=v1','-z'],['ls-files','--stage','-z'],['diff','--binary'],['diff','--cached','--binary'],['remote','-v'],['ls-remote','trial-delivery','refs/heads/trial/split-boundary']):git(args)
assert git(['rev-parse','HEAD']).decode().strip()==start['HEAD']
assert git(['show-ref'])==base64.b64decode(start['refs_base64'])
assert git(['status','--porcelain=v1','-z'])==base64.b64decode(start['status_base64'])
assert hashlib.sha256((p/'.git/index').read_bytes()).hexdigest()==start['index_sha256'];put('preserved/ordinary-index.bin',(p/'.git/index').read_bytes())
for name,info in start['files'].items():
 b=(p/name).read_bytes();assert hashlib.sha256(b).hexdigest()==info['sha256'];assert (p/name).stat().st_mode&0o777==info['mode'];put('preserved/workfiles/'+name,b)
for label,ref in refs.items():
 git(['show','--format=fuller','--stat',ref]);git(['show','--format=fuller','--binary',ref]);tree=git(['ls-tree','-rz','--full-tree',ref])
 for row in tree.split(b'\0'):
  if not row:continue
  meta,name=row.split(b'\t',1);mode,kind,oid=meta.decode().split();put('trees/'+label+'/'+name.decode(),git(['cat-file','blob',oid]))
objects={}
for row in git(['rev-list','--objects',*refs.values()]).decode().splitlines():
 oid=row.split()[0];kind=git(['cat-file','-t',oid]).decode().strip();b=git(['cat-file',kind,oid]);put('objects/'+oid,b);objects[oid]={'type':kind,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
# Inspect exact owning transitions, remaining result paths, source reconstruction and delivery.
first_paths=git(['diff-tree','--no-commit-id','--name-only','-r',refs['first']]).decode().splitlines();second_paths=git(['diff-tree','--no-commit-id','--name-only','-r',refs['HEAD']]).decode().splitlines()
assert first_paths==sorted(['AGENTS.md','README.md','tests/integration/test_api.py','tests/unit/test_io.py','textstats/__init__.py','textstats/io.py']);assert second_paths==['docs/dev/TASKS.md']
assert git(['rev-parse',refs['first']+'^']).decode().strip()==refs['base'];assert git(['rev-parse',refs['HEAD']+'^']).decode().strip()==refs['first'];assert git(['diff',refs['actual_source'],refs['HEAD']])==b''
a=git(['show',refs['first']+':docs/dev/TASKS.md']);b=git(['show',refs['HEAD']+':docs/dev/TASKS.md']);assert b'- [ ] T-002' in a;assert b'- [x] T-002' in b
remote=git(['ls-remote','trial-delivery','refs/heads/trial/split-boundary']).decode().split()[0];assert remote==refs['HEAD']
obs=json.loads((R/'037-sup-split-boundary-consumer-observations.json').read_bytes())
js('independent-assessment.json',{'case_id':'SUP-SPLIT-BOUNDARY','status':'Passed','agent_behavior_assessed':True,'product_history_contract':'Failed','consumer_required_behavior':'Detect published split result/status and block affected advancement/integration pending scoped manager recovery or explicit exception.','actual_checkpoint_refs':refs,'first_result_paths':first_paths,'closing_paths':second_paths,'closing_owner':'docs/dev/TASKS.md T-002 initial unchecked-to-checked transition','publication':{'kind':'LOCAL bare','ref':'refs/heads/trial/split-boundary','readback':remote,'setup_evidence_commit':'62d4ee5900e0ea3d6ddff917f33eb9f41a58e162'},'findings':['Actual first commit delivers six result/test/documentation paths while T-002 remains unchecked.','Actual second commit changes only TASKS, initially checks executable T-002 and adds current evidence; result remains in prior commit.','No explicit partial checkpoint authorization exists; no parent-only exception applies to this initial executable checkbox.','Conforming owning-ID subjects and immediate LOCAL publication do not repair closing composition.','TASKS inherited assertion that all result/evidence/initial completion close atomically contradicts observed history. Original evidence and gaps retained unchanged.','Both caller-generated commits reconstruct the complete genuine accepted T-002 source tree; genuine source 7cf remains preserved and is not regraded or replayed.','Read-only consumer correctly reports split closure and manager block without reset/rebase/force-push/replay or retrospective relabeling.'],'preservation':{'HEAD':True,'refs':True,'raw_status':True,'index_bytes':True,'tracked_file_bytes_and_modes':True},'original_consumer_gaps':obs.get('limits',[]),'limits':['Synthetic caller-authored LOCAL split reconstruction; not original implementation or authorized partial checkpoint.','Shared filesystem exposure prevents isolation certification.','No product tests or API execution performed; retained verification statements are historical and not independently rerun.','No live hosted/provider behavior established.','Supplemental evidence outside original 32-case matrix; original failures and gaps remain.']})
js('snapshot.json',{'refs':refs,'objects':objects,'commands':logs,'pinned_core':{'path':str(core),'sha256':hashlib.sha256(core.read_bytes()).hexdigest()},'consumer_seal_sha256':hashlib.sha256(seal.read_bytes()).hexdigest(),'embedded_completed_seal':completed['finish_seal'],'consumer_final_turn_confirmation':'Parent confirmed completed consumer final turn and exact whole-file seal SHA before assessment.'})
put('037-sup-split-boundary-assessor.py',Path(__file__).read_bytes())
manifest={}
for f in sorted(out.rglob('*')):
 if f.is_file():
  data=f.read_bytes();c.clean_bytes(data)
  if f.suffix=='.json':c.no_secret(json.loads(data))
  manifest[str(f.relative_to(out))]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
js('safe-hash-manifest.json',{'schema_version':1,'screening':'Every exported byte payload clean_bytes; every JSON parsed and no_secret checked using pinned published core.','files':manifest})
print(json.dumps({'status':'exported','objects':len(objects),'artifacts':len(manifest),'out':str(out)}))
