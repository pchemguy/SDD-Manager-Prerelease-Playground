import base64, hashlib, json, subprocess, sys, shutil, re, importlib.util
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6'); P=R/'037-sup-qc-recovery'; D=R/'037-sup-qc-recovery-final-artifacts'; D.mkdir(exist_ok=True)
cp=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
sp=importlib.util.spec_from_file_location('pinned_core',cp);core=importlib.util.module_from_spec(sp);sp.loader.exec_module(core)
phase=sys.argv[1]; out=D/phase
if out.exists(): raise RuntimeError('Immutable phase already exported')
out.mkdir(); logs=[]
def write(name,data):
 q=out/name;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)
def run(args,cwd=P):
 q=subprocess.run(args,cwd=cwd,capture_output=True);i=len(logs);write(f'commands/{i:03d}-stdout.bin',q.stdout);write(f'commands/{i:03d}-stderr.bin',q.stderr);logs.append({'argv':args,'cwd':str(cwd),'returncode':q.returncode,'stdout':f'commands/{i:03d}-stdout.bin','stderr':f'commands/{i:03d}-stderr.bin'});return q
G=['git','--no-optional-locks']; start=json.loads((R/'037-sup-qc-recovery-setup/START.json').read_text());head=run(G+['rev-parse','HEAD']).stdout.decode().strip()
for args in [['show-ref'],['status','--porcelain=v1','-z'],['ls-files','--stage','-z'],['diff','--binary'],['diff','--cached','--binary'],['log','--format=%H %P %s',start['HEAD']+'..HEAD'],['ls-remote','trial-delivery','refs/heads/trial/qc-recovery']]:run(G+args)
for n in run(G+['ls-files','-z']).stdout.split(b'\0'):
 if n: name=n.decode();write('workfiles/'+name,(P/name).read_bytes())
write('index.bin',(P/'.git/index').read_bytes());write('HEAD.bin',(P/'.git/HEAD').read_bytes())
objids=run(G+['rev-list','--objects','--all']).stdout.decode().splitlines(); objects=[]
for line in objids:
 oid=line.split()[0]; q=subprocess.run(G+['cat-file','-t',oid],cwd=P,capture_output=True);assert q.returncode==0; typ=q.stdout.decode().strip();q=subprocess.run(G+['cat-file',typ,oid],cwd=P,capture_output=True);assert q.returncode==0;write('objects/'+oid,q.stdout);objects.append({'oid':oid,'type':typ,'bytes':len(q.stdout)})
remote=R/'037-sup-qc-recovery-delivery.git';run(G+['show-ref'],remote)
hook=remote/'hooks/pre-receive';write('LOCAL-PRE-RECEIVE.bin',hook.read_bytes() if hook.exists() else b'')
obs=R/'037-sup-qc-recovery-consumer-observations.json'
if obs.exists():write('consumer-observations.json',obs.read_bytes());json.loads(obs.read_text())
write('commands.json', (json.dumps(logs,indent=2)+'\n').encode());write('objects.json',(json.dumps(objects,indent=2)+'\n').encode())
state={'phase':phase,'start':start['HEAD'],'HEAD':head,'local_native_controlled_bare_hook':True,'live_provider_or_native_client':False,'shared_filesystem_precludes_strong_isolation':True,'objects':len(objects),'product_mutated_by_assessor':False};write('snapshot.json',(json.dumps(state,indent=2)+'\n').encode())
files={};violations=[]
for p in out.rglob('*'):
 if not p.is_file():continue
 b=p.read_bytes();n=p.relative_to(out).as_posix();files[n]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
 try:
  core.clean_bytes(b)
  if p.suffix=='.json':core.no_secret(json.loads(b))
 except core.Stop as e:violations.append({'path':n,'cause':e.cause})
write('manifest.json',(json.dumps({'all_bytes_pinned':True,'no_secret':not violations,'secret_findings':violations,'files':files},indent=2)+'\n').encode());assert not violations
print(json.dumps(state))
