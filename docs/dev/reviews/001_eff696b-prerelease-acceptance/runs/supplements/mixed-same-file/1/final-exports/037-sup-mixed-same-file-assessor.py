import os, sys, json, hashlib, subprocess, shutil, importlib.util, stat
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6'); repo=R/'037-sup-mixed-same-file'; out=R/'037-sup-mixed-same-file-final-artifacts'; base='639e7e0cb54d5dd1f9c1a6e73de31e76301ae932'
core=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
spec=importlib.util.spec_from_file_location('evidencecore',core); c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
phase=sys.argv[1]; dest=out/phase; dest.mkdir(parents=True,exist_ok=False); logs=[]
def save(p,b):
 c.clean_bytes(b); p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
def gj(args,cwd=repo):
 argv=['git','--no-optional-locks',*args]; q=subprocess.run(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1'}); n=len(logs); save(dest/'commands'/f'{n:03}-stdout.bin',q.stdout);save(dest/'commands'/f'{n:03}-stderr.bin',q.stderr); logs.append({'argv':argv,'cwd':str(cwd),'exit':q.returncode,'stdout_sidecar':f'commands/{n:03}-stdout.bin','stderr_sidecar':f'commands/{n:03}-stderr.bin'});return q.stdout
ref=base if phase=='baseline' else gj(['rev-parse','HEAD']).decode().strip()
for args in [['status','--porcelain=v2','-z'],['show-ref'],['ls-files','--stage','-z'],['diff','--binary'],['diff','--cached','--binary'],['log','--format=fuller',base+'..HEAD'],['ls-remote','trial-delivery','refs/heads/phase/1-named-file-utility'],['remote','-v']]:gj(args)
tree=gj(['ls-tree','-rz','--full-tree',ref]); manifest={}
for row in tree.split(b'\0'):
 if not row:continue
 meta,name=row.split(b'\t',1); mode,kind,oid=meta.decode().split(); name=name.decode(); b=gj(['cat-file','blob',oid]);save(dest/'tracked-files'/name,b);manifest[name]={'mode':mode,'blob':oid,'sha256':hashlib.sha256(b).hexdigest()}
objects=gj(['rev-list','--objects',ref]).decode().splitlines(); objm={}
for row in objects:
 oid=row.split()[0]; kind=gj(['cat-file','-t',oid]).decode().strip();b=gj(['cat-file',kind,oid]);save(dest/'objects'/oid,b);objm[oid]={'type':kind,'length':len(b),'sha256':hashlib.sha256(b).hexdigest()}
if phase=='final':
 for p in sorted(repo.rglob('*')):
  rel=p.relative_to(repo)
  if '.git' in rel.parts or '__pycache__' in rel.parts or not p.is_file():continue
  save(dest/'workfiles'/rel,p.read_bytes())
 save(dest/'ordinary-index.bin',(repo/'.git/index').read_bytes())
 for p in R.glob('037-sup-mixed-same-file-consumer-observations*'):
  if p.is_file():save(dest/'consumer'/p.name,p.read_bytes())
else:
 for p in (R/'037-sup-mixed-same-file-setup').iterdir():
  if p.is_file():save(dest/'setup'/p.name,p.read_bytes())
metadata={'phase':phase,'ref':ref,'files':manifest,'objects':objm,'commands':logs,'core':{'path':str(core),'sha256':hashlib.sha256(core.read_bytes()).hexdigest()},'limits':['Readonly actual Git and file inspection; LOCAL remote only, no provider behavior inferred.','Shared filesystem means snapshots do not establish isolated process or concurrency guarantees.','Outside original 32-case acceptance scope.']}
c.no_secret(metadata);save(dest/'snapshot.json',(json.dumps(metadata,indent=2)+'\n').encode())
print(json.dumps({'phase':phase,'ref':ref,'files':len(manifest),'objects':len(objm),'commands':len(logs)}))
