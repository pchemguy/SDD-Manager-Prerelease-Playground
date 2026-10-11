#!/usr/bin/env python3
"""Independent readonly post-seal snapshots. Never invokes a write adapter operation."""
import argparse, datetime, hashlib, json, pathlib, subprocess, sys
p=argparse.ArgumentParser(); p.add_argument('--product',required=True); p.add_argument('--facility',required=True); p.add_argument('--output',required=True); p.add_argument('--seal',required=True);a=p.parse_args()
f=pathlib.Path(a.facility); sys.path.insert(0,str(f)); import core
seal=pathlib.Path(a.seal); raw=seal.read_bytes(); screen={'path':str(seal),'sha256':hashlib.sha256(raw).hexdigest()}
try:
 core.clean_bytes(raw); core.no_secret(json.loads(raw)); screen['publication_safe']=True
except Exception as e:screen.update(publication_safe=False,withheld_reason=type(e).__name__)
def git(*args):
 r=subprocess.run(['git','-C',a.product,*args],capture_output=True); core.clean_bytes(r.stdout);core.clean_bytes(r.stderr)
 return {'argv':['git','-C',a.product,*args],'returncode':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()}
r={'schema_version':1,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'seal':screen,'product':a.product,'facility':a.facility,'commands':{},'tracked_worktree':{},'facility_files':{}}
for key,args in [('head',('rev-parse','HEAD')),('refs',('show-ref',)),('index',('ls-files','--stage')),('status',('status','--porcelain=v1')),('parents',('show','-s','--format=%P','HEAD')),('tracked',('ls-files','-z'))]:r['commands'][key]=git(*args)
for path in r['commands']['tracked']['stdout'].split('\0'):
 if path:
  file=pathlib.Path(a.product)/path
  r['tracked_worktree'][path]={'exists':file.exists(),'sha256':hashlib.sha256(file.read_bytes()).hexdigest() if file.is_file() else None}
r['commands']['tracked']['stdout']=r['commands']['tracked']['stdout'].split('\0')[:-1]
for file in sorted(f.rglob('*')):
 if file.is_file() and '__pycache__' not in file.parts:
  b=file.read_bytes(); entry={'sha256':hashlib.sha256(b).hexdigest(),'size':len(b)}
  if file.suffix=='.json':
   try: core.clean_bytes(b); obj=json.loads(b);core.no_secret(obj); entry['json']=obj
   except Exception as e:entry['withheld_reason']=type(e).__name__
  r['facility_files'][str(file.relative_to(f))]=entry
core.no_secret(r);b=(json.dumps(r,indent=2)+'\n').encode();core.clean_bytes(b)
with pathlib.Path(a.output).open('xb') as out:out.write(b)
print(json.dumps({'output':a.output,'sha256':hashlib.sha256(b).hexdigest(),'seal_publication_safe':screen['publication_safe']}))
