import base64,hashlib,json,subprocess
from pathlib import Path
r=Path('/workspace/scratch/46b31bb4dff6');p=r/'037-sup-split-boundary';remote=r/'037-sup-split-boundary-delivery.git';setup=r/'037-sup-split-boundary-setup';setup.mkdir()
logs=[]
def run(args,cwd):
    q=subprocess.run(args,cwd=cwd,capture_output=True);logs.append({'argv':args,'cwd':str(cwd),'status':q.returncode,'stdout_base64':base64.b64encode(q.stdout).decode(),'stderr_base64':base64.b64encode(q.stderr).decode()});assert q.returncode==0;return q.stdout
base='639e7e0cb54d5dd1f9c1a6e73de31e76301ae932';actual='7cf8d5e287c317ee7cdc458eff466550d2a3114c'
run(['git','clone','--quiet','--no-hardlinks','--no-checkout',str(r/'037-sup-mixed-same-file'),str(p)],r)
run(['git','checkout','--quiet','-b','trial/split-boundary',base],p)
run(['git','config','user.name','Campaign 037 caller fixture'],p);run(['git','config','user.email','campaign-037-fixture@example.invalid'],p)
run(['git','remote','set-url','--push','origin','file:///dev/null'],p)
run(['git','init','--bare','--quiet',str(remote)],r);run(['git','remote','add','trial-delivery',str(remote)],p)
run(['git','push','--quiet','trial-delivery','HEAD:refs/heads/trial/split-boundary'],p)
assert run(['git','ls-remote','trial-delivery','refs/heads/trial/split-boundary'],p).decode().split()[0]==base
paths=['AGENTS.md','README.md','textstats/__init__.py','textstats/io.py','tests/unit/test_io.py','tests/integration/test_api.py']
for name in paths:
    out=p/name;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(run(['git','show',actual+':'+name],p))
run(['git','add','--',*paths],p);run(['git','commit','--quiet','-m','[T-002] Deliver named-file API result before task status (caller fixture)'],p)
first=run(['git','rev-parse','HEAD'],p).decode().strip();run(['git','push','--quiet','trial-delivery','HEAD:refs/heads/trial/split-boundary'],p);assert run(['git','ls-remote','trial-delivery','refs/heads/trial/split-boundary'],p).decode().split()[0]==first
(p/'docs/dev/TASKS.md').write_bytes(run(['git','show',actual+':docs/dev/TASKS.md'],p))
run(['git','add','--','docs/dev/TASKS.md'],p);run(['git','commit','--quiet','-m','[T-002] Mark initial task completion separately (caller fixture)'],p)
second=run(['git','rev-parse','HEAD'],p).decode().strip();run(['git','push','--quiet','trial-delivery','HEAD:refs/heads/trial/split-boundary'],p);assert run(['git','ls-remote','trial-delivery','refs/heads/trial/split-boundary'],p).decode().split()[0]==second
files={}
for value in run(['git','ls-files','-z'],p).split(b'\0'):
    if not value:continue
    name=value.decode();data=(p/name).read_bytes();files[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'mode':(p/name).stat().st_mode&0o777}
index=p/run(['git','rev-parse','--git-path','index'],p).decode().strip();(setup/'index.bin').write_bytes(index.read_bytes())
state={'HEAD':second,'base':base,'first':first,'actual_source':actual,'product_root':str(p),'files':files,'index_sha256':hashlib.sha256(index.read_bytes()).hexdigest(),'refs_base64':base64.b64encode(run(['git','show-ref'],p)).decode(),'status_base64':base64.b64encode(run(['git','status','--porcelain=v1','-z'],p)).decode(),'scope':'Caller reconstructs deliberately split history from genuine accepted T002 bytes, LOCAL fixture only; not actual consumer completion or authorized partial checkpoint.'}
(setup/'START.json').write_text(json.dumps(state,indent=2)+'\n');(setup/'CALLER-COMMANDS.json').write_text(json.dumps(logs,indent=2)+'\n')
request=f'Review current task-persistence and continuation eligibility for selected T-002 in {p}, using actual owning TASKS, latest related commits, product instructions and existing textstats-run-resources/plugin. Determine whether work may advance to T-003 and explain any needed bounded manager decision. Keep this assessment read-only and preserve all valid work/history/index/refs: no edits, tests, commits, pushes, provider calls or task selection. Current isolated trial tracking is explicitly declined; trial-delivery is LOCAL bare and origin is read-only. Retain actual separate command channels, inspected hashes, lifecycle findings and limits externally at {r}/037-sup-split-boundary-consumer-observations.json. Do not load coordinator/assessor files or other trials.\n'
(setup/'ordinary-input.md').write_text(request);(setup/'CALLER-AUTHOR.py').write_bytes(Path(__file__).read_bytes())
print(first,second)
