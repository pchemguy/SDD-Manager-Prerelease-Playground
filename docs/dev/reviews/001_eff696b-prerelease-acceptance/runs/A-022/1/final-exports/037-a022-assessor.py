import pathlib,subprocess,json,hashlib,os,sys,shutil,time
ROOT=pathlib.Path('/workspace/scratch/46b31bb4dff6/037-a022-acceptance-change')
OUT=pathlib.Path('/workspace/scratch/46b31bb4dff6/037-a022-final-artifacts');OUT.mkdir(exist_ok=True)
records=[]
def run(args,cwd=ROOT):
 p=subprocess.run(args,cwd=cwd,capture_output=True,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1'})
 n=len(records);base=OUT/(sys.argv[1]+'-command-'+str(n));base.with_suffix('.stdout').write_bytes(p.stdout);base.with_suffix('.stderr').write_bytes(p.stderr)
 records.append(dict(argv=args,cwd=str(cwd),exit_code=p.returncode,stdout_file=base.with_suffix('.stdout').name,stderr_file=base.with_suffix('.stderr').name,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr_sha256=hashlib.sha256(p.stderr).hexdigest()))
 return p.stdout
label=sys.argv[1]
snap={}
for name,args in [('head',['rev-parse','HEAD']),('parents',['show','-s','--format=%P','HEAD']),('branch',['branch','--show-current']),('refs',['for-each-ref','--format=%(objectname) %(refname)']),('status',['status','--porcelain=v2']),('index',['ls-files','--stage','-z']),('diff',['diff','--binary']),('cached_diff',['diff','--cached','--binary']),('objects',['rev-list','--objects','--all']),('local_delivery',['ls-remote','trial-delivery','refs/heads/phase/2-json-and-stdin'])]:
 snap[name]=run(['git','--no-optional-locks',*args]).decode()
paths=run(['git','--no-optional-locks','ls-files','-z']).decode().split('\0')
files={}
for name in paths:
 if not name:continue
 p=ROOT/name
 if p.is_file():
  data=p.read_bytes();target=OUT/label/'workfiles'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);target.chmod(p.stat().st_mode&0o777)
  files[name]={'sha256':hashlib.sha256(data).hexdigest(),'mode':oct(p.stat().st_mode&0o777)}
snap['files']=files
snap['index_file_sha256']=hashlib.sha256((ROOT/'.git/index').read_bytes()).hexdigest()
(OUT/(label+'-snapshot.json')).write_text(json.dumps(snap,indent=2))
(OUT/(label+'-commands.json')).write_text(json.dumps(records,indent=2))
print(json.dumps({'label':label,'head':snap['head'].strip(),'tracked_files':len(files),'status':snap['status']}))
