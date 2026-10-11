import pathlib,subprocess,json,hashlib,importlib.util,shutil,os,datetime
R=pathlib.Path('/workspace/scratch/46b31bb4dff6');W=R/'037-a014-cross-phase';O=R/'037-a014-authorized-independent/t010-candidate';O.mkdir(exist_ok=True)
C=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';s=importlib.util.spec_from_file_location('c',C);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
def write(p,b):
 c.clean_bytes(b)
 try:v=json.loads(b)
 except (ValueError,UnicodeError):pass
 else:c.no_secret(v)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def git(*a):return subprocess.check_output(['git',*a],cwd=W)
shutil.copytree(R/'037-a014-authorized-independent/t009-candidate/files',O/'files',dirs_exist_ok=True)
paths=git('diff','--cached','--name-only').decode().splitlines();hashes={}
for p in paths:
 b=git('show',':'+p);write(O/'files'/p,b);hashes[p]=hashlib.sha256(b).hexdigest()
for n,a in [('head',['rev-parse','HEAD']),('branch',['branch','--show-current']),('index',['ls-files','--stage']),('diff',['diff','--cached','--binary']),('status',['status','--porcelain=v2']),('protected',['diff','--cached','--','textstats-run-resources','.github','docs/testing/publisher-037','docs/dev/SPEC.md','docs/dev/PLAN.md','docs/dev/layout.md','tools/check_distribution.py','tests/integration/test_distribution.py'])]:write(O/(n+'.stdout'),git(*a))
cp=subprocess.run(['python','-B','tools/check_tests.py'],cwd=O/'files',env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=subprocess.PIPE,stderr=subprocess.PIPE);write(O/'tests.stdout',cp.stdout);write(O/'tests.stderr',cp.stderr)
v={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'staged_tree':'6fa480a4a168292ec49061e099c05ec02d200fa5','source_head':git('rev-parse','HEAD').decode().strip(),'paths':paths,'sha256':hashes,'independent_private_test_status':cp.returncode,'pending':'Actual commit and trial-json publication; no phase2 integration.'};write(O/'IDENTITIES.json',json.dumps(v,indent=2).encode());print(json.dumps(v,indent=2));print(cp.stdout.decode())
