import base64,hashlib,importlib.util,json,os,subprocess
from pathlib import Path
R=Path('/workspace/scratch/46b31bb4dff6');out=R/'037-sup-split-boundary-final-artifacts';e=R/'037-test-evidence';p=R/'037-sup-split-boundary'
core=e/'docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
s=importlib.util.spec_from_file_location('pinnedcore',core);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
logs=[]
def put(name,b):
 c.clean_bytes(b)
 if name.endswith('.json'):c.no_secret(json.loads(b))
 f=out/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
def run(args,cwd):
 q=subprocess.run(['git','--no-optional-locks',*args],cwd=cwd,capture_output=True,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'});i=len(logs);put(f'publication-audit/{i:02}-stdout.bin',q.stdout);put(f'publication-audit/{i:02}-stderr.bin',q.stderr);logs.append({'argv':['git','--no-optional-locks',*args],'cwd':str(cwd),'exit':q.returncode,'stdout_sidecar':f'publication-audit/{i:02}-stdout.bin','stderr_sidecar':f'publication-audit/{i:02}-stderr.bin'});assert q.returncode==0;return q.stdout
pub='62d4ee5900e0ea3d6ddff917f33eb9f41a58e162';prefix='docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/supplements/split-boundary/1/setup/'
put('publication-audit/setup-publication-commit.txt',run(['cat-file','commit',pub],e));manifest=run(['show',pub+':'+prefix+'MANIFEST.json'],e);put('publication-audit/published-setup-MANIFEST.json',manifest)
for f in (R/'037-sup-split-boundary-setup').iterdir():
 if f.is_file():assert run(['show',pub+':'+prefix+f.name],e)==f.read_bytes()
assert run(['show',pub+':'+str(core.relative_to(e))],e)==core.read_bytes()
start=json.loads((R/'037-sup-split-boundary-setup/START.json').read_bytes())
assert run(['rev-parse','HEAD'],p).decode().strip()==start['HEAD'];assert run(['show-ref'],p)==base64.b64decode(start['refs_base64']);assert run(['status','--porcelain=v1','-z'],p)==base64.b64decode(start['status_base64']);assert hashlib.sha256((p/'.git/index').read_bytes()).hexdigest()==start['index_sha256']
for name,v in start['files'].items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==v['sha256']
put('publication-audit/audit.json',(json.dumps({'commands':logs,'setup_published_object':pub,'setup_bytes_exact_object_match':True,'pinned_core_exact_published_object_match':True,'final_product_preservation_rechecked':True,'provider_calls':False,'live_publication_limit':'Publication parent-reported; exact retained setup commit contents independently checked locally. LOCAL delivery readback independently observed.'},indent=2)+'\n').encode())
put('037-sup-split-boundary-export-qc.py',Path(__file__).read_bytes())
manifest={}
for f in sorted(out.rglob('*')):
 if f.is_file() and f.name!='safe-hash-manifest.json':
  b=f.read_bytes();c.clean_bytes(b)
  if f.suffix=='.json':c.no_secret(json.loads(b))
  manifest[str(f.relative_to(out))]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
put('safe-hash-manifest.json',(json.dumps({'schema_version':1,'screening':'Every exported byte payload clean_bytes; every JSON parsed and no_secret checked using exact pinned published core. Manifest excludes itself.','files':manifest},indent=2)+'\n').encode())
print(json.dumps({'files':len(manifest),'manifest_sha256':hashlib.sha256((out/'safe-hash-manifest.json').read_bytes()).hexdigest(),'json_files':sum(k.endswith('.json') for k in manifest)}))
