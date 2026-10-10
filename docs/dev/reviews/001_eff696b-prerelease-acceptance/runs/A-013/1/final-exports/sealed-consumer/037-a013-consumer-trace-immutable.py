import subprocess,os,json,hashlib,sys,runpy,time
from pathlib import Path
original=subprocess.run
obs=Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-observations.json")

def append(section, entry):
 import uuid
 directory=Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-command-records")
 directory.mkdir(exist_ok=True)
 target=directory/(str(time.time_ns())+"-"+str(os.getpid())+"-"+uuid.uuid4().hex+".json")
 with target.open("x") as record:
  record.write(json.dumps({"section":section,"record":entry},indent=2)+"\n")

def traced(*args,**kwargs):
 argv=kwargs.get("args",args[0] if args else None);cwd=str(kwargs.get("cwd") or os.getcwd()); inp=kwargs.get("input"); fixtures={}
 for p in Path(cwd).glob("*"):
  if p.is_file() and (p.suffix==".txt" or p.name.startswith("-")):
   fixtures[str(p)]={"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size}
 try:
  r=original(*args,**kwargs);entry={"argv":argv,"cwd":cwd,"stdout":r.stdout.decode("utf-8","replace") if isinstance(r.stdout,bytes) else r.stdout,"stderr":r.stderr.decode("utf-8","replace") if isinstance(r.stderr,bytes) else r.stderr,"status":r.returncode}
 except Exception as e:
  entry={"argv":argv,"cwd":cwd,"exception":type(e).__name__+": "+str(e)};raise
 finally:
  entry.update({"time":time.time(),"environment":{k:v for k,v in (kwargs.get("env") or os.environ).items() if k in {"PYTHONDONTWRITEBYTECODE","PYTHONUTF8","PYTHONCOERCECLOCALE","LC_ALL","LANG","PYTHONNOUSERSITE","PYTHONPATH"}},"fixtures":fixtures,"input_hex":inp.hex() if isinstance(inp,bytes) else None,"input_text":inp if isinstance(inp,str) else None,"input_sha256":hashlib.sha256(inp if isinstance(inp,bytes) else inp.encode()).hexdigest() if inp is not None else None});append("children",entry)
 return r
subprocess.run=traced
if sys.argv[1]=="-m":
 sys.path.insert(0,os.getcwd());module=sys.argv[2];sys.argv=sys.argv[2:];runpy.run_module(module,run_name="__main__",alter_sys=True)
else:
 path=sys.argv[1];sys.argv=sys.argv[1:];sys.path.insert(0,str(Path(path).resolve().parent));runpy.run_path(path,run_name="__main__")
