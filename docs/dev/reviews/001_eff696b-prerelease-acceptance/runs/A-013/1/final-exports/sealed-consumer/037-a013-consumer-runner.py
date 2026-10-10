import os,sys,json,subprocess,time,hashlib
from pathlib import Path
root="/workspace/scratch/46b31bb4dff6/037-textstats-product"
obs=Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-observations.json")

def append(section, entry):
 import fcntl,os
 with open(str(obs)+".lock","a") as lock:
  fcntl.flock(lock,fcntl.LOCK_EX)
  d=json.loads(obs.read_text()) if obs.exists() else {"commands":[],"notes":[]}
  d.setdefault(section,[]).append(entry)
  temp=Path(str(obs)+".tmp-"+str(os.getpid()))
  temp.write_text(json.dumps(d,indent=2)+"\n")
  os.replace(temp,obs)

def run(argv,cwd=root,input=None,env=None):
 e=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",GIT_ASKPASS="/workspace/scratch/46b31bb4dff6/playground-askpass.sh",GIT_TERMINAL_PROMPT="0");e.update(env or {})
 p=subprocess.run(argv,cwd=cwd,input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=e)
 ent={"argv":argv,"cwd":cwd,"stdout":p.stdout.decode("utf-8","replace"),"stderr":p.stderr.decode("utf-8","replace"),"status":p.returncode,"input_hex":input.hex() if input is not None else None,"input_sha256":hashlib.sha256(input).hexdigest() if input is not None else None,"time":time.time(),"environment":{k:v for k,v in e.items() if k in {"PYTHONDONTWRITEBYTECODE","PYTHONUTF8","PYTHONCOERCECLOCALE","LC_ALL","LANG","PYTHONNOUSERSITE","PYTHONPATH"}}}
 append("commands",ent)
 print(json.dumps(ent));return p
if __name__=="__main__":
 p=run(sys.argv[1:]);sys.exit(p.returncode)
