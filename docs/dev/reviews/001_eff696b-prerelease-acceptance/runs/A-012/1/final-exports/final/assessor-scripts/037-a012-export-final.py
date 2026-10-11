import pathlib,subprocess,json,hashlib,tarfile,io,shutil,stat,sys,base64
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');root=base/'037-textstats-product';out=base/'037-a012-final-artifacts/final';out.mkdir()
def git(*args):
 r=subprocess.run(['git','--no-optional-locks','-C',str(root),*args],capture_output=True);commands.append({'cmd':r.args,'returncode':r.returncode,'stdout_hex':r.stdout.hex(),'stderr_hex':r.stderr.hex()});r.check_returncode();return r.stdout
commands=[]
for name,args in {'head':['rev-parse','HEAD'],'parents':['show','-s','--format=%P','HEAD'],'branch':['branch','--show-current'],'refs':['show-ref'],'status':['status','--porcelain=v1'],'index':['ls-files','--stage'],'log':['log','-40','--format=%H %P %s'],'remotes':['remote','-v'],'diff':['diff','--binary','795f3a3542c9981f8d43c8e182876f3efa5b5f16','HEAD']}.items():(out/(name+'.txt')).write_bytes(git(*args))
raw=git('archive','--format=tar','HEAD');(out/'product-head.tar').write_bytes(raw)
with tarfile.open(fileobj=io.BytesIO(raw)) as t:t.extractall(out/'product-export',filter='data')
manifest={}
for p in (out/'product-export').rglob('*'):
 if p.is_file():manifest[str(p.relative_to(out/'product-export'))]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mode':oct(p.stat().st_mode&0o777)}
(out/'tree-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
work=out/'actual-workfiles'; work.mkdir();workmanifest={}
paths=git('ls-files','-z').split(b'\0')+git('ls-files','--others','--exclude-standard','-z').split(b'\0')
for bpath in sorted(set(paths)):
 if not bpath:continue
 path=bpath.decode();p=root/path;dest=work/path
 if not p.exists():workmanifest[path]={'exists':False};continue
 if p.is_symlink():workmanifest[path]={'symlink':str(p.readlink())};continue
 if p.is_file():dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);workmanifest[path]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mode':oct(p.stat().st_mode&0o777)}
(out/'workfile-manifest.json').write_text(json.dumps(workmanifest,indent=2)+'\n')
roots=[git('rev-parse','HEAD').decode().strip(),'795f3a3542c9981f8d43c8e182876f3efa5b5f16','fbe8bedf4c6cba1ab29d53d2da05e614603d76d1']
objects={};objdir=out/'git-object-originals';objdir.mkdir()
for row in git('rev-list','--objects',*roots).decode().splitlines():
 oid=row.split()[0];typ=git('cat-file','-t',oid).decode().strip();payload=git('cat-file',typ,oid);(objdir/oid).write_bytes(payload);objects[oid]={'type':typ,'size':len(payload),'sha256':hashlib.sha256(payload).hexdigest(),'object_hash_valid':hashlib.sha1((typ+' '+str(len(payload))+'\0').encode()+payload).hexdigest()==oid}
(out/'git-object-manifest.json').write_text(json.dumps({'retained_roots':roots,'objects':objects},indent=2)+'\n')
(out/'export-commands.json').write_text(json.dumps(commands,indent=2)+'\n')
print(json.dumps({'head':roots[0],'files':len(manifest),'objects':len(objects),'object_hashes_valid':all(v['object_hash_valid'] for v in objects.values())}))
