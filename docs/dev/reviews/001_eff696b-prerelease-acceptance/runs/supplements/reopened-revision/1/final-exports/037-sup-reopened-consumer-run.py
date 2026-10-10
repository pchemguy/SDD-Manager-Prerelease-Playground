import subprocess,sys,json,os,hashlib,pathlib
root='/workspace/scratch/46b31bb4dff6/037-sup-reopened-revision'
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
cmd=sys.argv[1]
r=subprocess.run(cmd,shell=True,cwd=root,env=env,text=True,capture_output=True)
entry={'command':cmd,'stdout':r.stdout,'stderr':r.stderr,'exit':r.returncode}
with open('/workspace/scratch/46b31bb4dff6/037-sup-reopened-consumer-log.jsonl','a') as f:f.write(json.dumps(entry)+'\n')
print(r.stdout,end='');print(r.stderr,end='',file=sys.stderr);sys.exit(r.returncode)
