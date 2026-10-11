import json,sys,urllib.request,urllib.error,hashlib,time
from pathlib import Path
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

base="https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground"
def api(endpoint,method="GET",payload=None):
 token=Path("/workspace/scratch/46b31bb4dff6/SDD-Manager-Prerelease-Playground/gh.tkn").read_text().strip()
 data=json.dumps(payload).encode() if payload is not None else None
 req=urllib.request.Request(base+endpoint,data=data,method=method,headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","Content-Type":"application/json"})
 try:
  with urllib.request.urlopen(req) as r: raw=r.read();status=r.status;headers=dict(r.headers)
 except urllib.error.HTTPError as r: raw=r.read();status=r.code;headers=dict(r.headers)
 result=json.loads(raw);append("provider",{"method":method,"endpoint":base+endpoint,"request_payload":payload,"status":status,"response_sha256":hashlib.sha256(raw).hexdigest(),"response_bytes":len(raw),"headers":{k:v for k,v in headers.items() if k.lower() in {"link","x-github-request-id","x-ratelimit-remaining","x-ratelimit-reset"}},"response":result if not isinstance(result,list) else [{k:v for k,v in o.items() if k in {"number","title","state","state_reason","body","description","labels","milestone","html_url","id"}} if "sdd-forge:task-id=" in (o.get("body") or "") or str(o.get("title","")).startswith("sdd-") else {"id":o.get("id"),"number":o.get("number"),"state":o.get("state"),"sha256":hashlib.sha256(json.dumps(o,sort_keys=True).encode()).hexdigest()} for o in result]})
 if status>=400: raise RuntimeError(f"HTTP {status}: {result.get('message')}")
 return result
if __name__=="__main__":
 r=api(sys.argv[1]);print(json.dumps(r if isinstance(r,dict) else [{k:v for k,v in o.items() if k in {"number","title","state","state_reason","labels","milestone","description"}} for o in r],indent=2))
