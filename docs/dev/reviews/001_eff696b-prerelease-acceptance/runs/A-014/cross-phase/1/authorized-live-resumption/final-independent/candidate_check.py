import pathlib,subprocess,json,hashlib,importlib.util,datetime,shutil,os
R=pathlib.Path('/workspace/scratch/46b31bb4dff6');W=R/'037-a014-cross-phase';O=R/'037-a014-authorized-independent'/'t009-candidate';O.mkdir(exist_ok=True)
C=R/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';s=importlib.util.spec_from_file_location('core',C);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
def write(p,b):
 c.clean_bytes(b)
 try:v=json.loads(b)
 except (ValueError,UnicodeError):pass
 else:c.no_secret(v)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def git(*args):return subprocess.check_output(['git',*args],cwd=W)
shutil.copytree(R/'037-a014-authorized-independent/initial/files',O/'files',dirs_exist_ok=True)
paths=git('diff','--cached','--name-only').decode().splitlines(); hashes={}
for p in paths:
 b=git('show',':'+p);write(O/'files'/p,b);hashes[p]=hashlib.sha256(b).hexdigest()
for n,a in [('status',['status','--porcelain=v2']),('diff',['diff','--cached','--binary']),('index',['ls-files','--stage']),('head',['rev-parse','HEAD']),('tree',['rev-parse','93756800aafe8abb0d8719176a14eb81ba42b4e1^{tree}']),('main',['rev-parse','main'])]:write(O/(n+'.stdout'),git(*a))
ancestor=subprocess.run(['git','merge-base','--is-ancestor','main','HEAD'],cwd=W).returncode
summary={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_tree':'93756800aafe8abb0d8719176a14eb81ba42b4e1','staged_paths':paths,'sha256':hashes,'main_ancestor_of_current_phase_head':ancestor==0,'prospective_merge':'Main is ancestor of unchanged current phase; no target-only delta observed. Required two-parent merge and real merged-state checks/publication remain future gates.'}
write(O/'IDENTITIES.json',json.dumps(summary,indent=2).encode())
cp=subprocess.run(['python','-B','tools/check_tests.py'],cwd=O/'files',env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=subprocess.PIPE,stderr=subprocess.PIPE);write(O/'tests.stdout',cp.stdout);write(O/'tests.stderr',cp.stderr);write(O/'tests.json',json.dumps({'argv':['python','-B','tools/check_tests.py'],'cwd':str(O/'files'),'status':cp.returncode},indent=2).encode());print(json.dumps(summary,indent=2));print('independent candidate tests status',cp.returncode);print(cp.stdout.decode())
