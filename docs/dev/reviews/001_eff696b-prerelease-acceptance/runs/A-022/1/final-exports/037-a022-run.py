import subprocess,json,pathlib,sys,time,os
p=pathlib.Path('/workspace/scratch/46b31bb4dff6/037-a022-consumer-observations.json')
cmd=sys.argv[1]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run(cmd,shell=True,cwd='/workspace/scratch/46b31bb4dff6/037-a022-acceptance-change',env=env,text=True,capture_output=True)
d=json.loads(p.read_text());d['records'].append(dict(command=cmd,cwd='/workspace/scratch/46b31bb4dff6/037-a022-acceptance-change',stdout=r.stdout,stderr=r.stderr,exit_code=r.returncode,timestamp=time.time()));p.write_text(json.dumps(d,indent=2));print(r.stdout,end='');print(r.stderr,end='',file=sys.stderr);print('EXIT_STATUS='+str(r.returncode));sys.exit(r.returncode)
