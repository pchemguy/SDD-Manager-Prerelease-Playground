import subprocess,json,sys,os,time
from pathlib import Path
base=Path("/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations")
cmd=sys.argv[1:]
stdin_source=sys.stdin.read() if cmd and cmd[-1]=="-" else None
e=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",GIT_ASKPASS="/workspace/scratch/46b31bb4dff6/playground-askpass.sh",GIT_TERMINAL_PROMPT="0",GIT_OPTIONAL_LOCKS="0")
r=subprocess.run(cmd,cwd="/workspace/scratch/46b31bb4dff6/037-textstats-product",env=e,text=True,capture_output=True,input=stdin_source)
with Path(str(base)+".commands.jsonl").open("a") as f:f.write(json.dumps(dict(command=cmd,stdin=stdin_source,cwd="/workspace/scratch/46b31bb4dff6/037-textstats-product",bytecode_disabled=True,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,timestamp=time.time()))+"\n")
print(r.stdout,end="");print(r.stderr,end="",file=sys.stderr);sys.exit(r.returncode)
