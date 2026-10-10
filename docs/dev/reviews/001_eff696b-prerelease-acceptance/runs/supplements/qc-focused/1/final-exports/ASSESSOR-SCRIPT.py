from pathlib import Path
import json, hashlib, subprocess, base64, datetime
B=Path('/workspace/scratch/46b31bb4dff6'); S=B/'037-sup-qc-focused-setups'; O=B/'037-sup-qc-focused-final-artifacts'
calls=[]
def h(b): return hashlib.sha256(b).hexdigest()
def run(argv,cwd):
 r=subprocess.run(argv,cwd=cwd,capture_output=True)
 calls.append({'argv':argv,'cwd':str(cwd),'exit_code':r.returncode,'stdout_base64':base64.b64encode(r.stdout).decode(),'stderr_base64':base64.b64encode(r.stderr).decode(),'stdout_sha256':h(r.stdout),'stderr_sha256':h(r.stderr)})
 if r.returncode: raise RuntimeError(f'command failed {argv}: {r.returncode}')
 return r.stdout
def git(p,*args): return run(['git','--no-optional-locks',*args],p)
checks={}
for c in ['narrow-feature','missing-plan-contract']:
 start=json.loads((S/c/'START.json').read_text()); p=Path(start['worktree']); files={}
 for n in git(p,'ls-files','-z').decode().split('\0'):
  if n:
   f=p/n; files[n]={'sha256':h(f.read_bytes()),'mode':f.stat().st_mode & 0o777}
 idx=p/git(p,'rev-parse','--git-path','index').decode().strip()
 after={'head':git(p,'rev-parse','HEAD').decode().strip(),'status':git(p,'status','--porcelain=v1').decode(),'refs':git(p,'show-ref').decode(),'index_entries':git(p,'ls-files','--stage').decode(),'index_sha256':h(idx.read_bytes()),'tracked_files':files}
 diff=git(p,'diff','--binary','--',*start['owned_fixture_paths'])
 checks[c]={'tracked_count':len(files),'matches_start':{k:after[k]==start[k] for k in after},'diff_matches_setup':diff==(S/c/'FIXTURE.diff').read_bytes(),'untracked':git(p,'ls-files','--others','--exclude-standard','-z').decode().split('\0')[:-1]}
 (O/(c+'-AFTER.json')).write_text(json.dumps(after,indent=2)+'\n')
 (O/(c+'-AFTER.diff')).write_bytes(diff)
(O/'ASSESSOR-COMMANDS-BASE64.json').write_text(json.dumps({'schema_version':1,'commands':calls},indent=2)+'\n')
(O/'STATE-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
