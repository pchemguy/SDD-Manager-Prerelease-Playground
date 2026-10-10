import pathlib,json,hashlib,subprocess,importlib.util,os
b=pathlib.Path('/workspace/scratch/46b31bb4dff6');product=b/'037-textstats-product';out=b/'037-a013-final-artifacts/final-reached/current-recovery';out.mkdir();cp=b/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';sp=importlib.util.spec_from_file_location('core',cp);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c);commands=[];objects=[];files=[];h=lambda x:hashlib.sha256(x).hexdigest()
def run(args,binary=False):
 argv=['git',*args];r=subprocess.run(argv,cwd=product,capture_output=True);d={'argv':argv,'cwd':str(product),'status':r.returncode,'stdout':None if binary else r.stdout.decode(),'stdout_sha256':h(r.stdout),'stdout_bytes':len(r.stdout),'stderr':r.stderr.decode()};commands.append(d);assert r.returncode==0;return r.stdout
raw=run(['ls-files','--stage','-z'],True);entries=[]
for row in raw.split(b'\0'):
 if not row:continue
 fields,name=row.decode().split('\t');mode,oid,stage=fields.split();assert stage=='0';entries.append({'path':name,'mode':mode,'oid':oid,'stage':stage})
for e in entries:
 raw=run(['cat-file','blob',e['oid']],True);c.clean_bytes(raw)
 try:d=json.loads(raw)
 except (ValueError,UnicodeDecodeError):pass
 else:c.no_secret(d)
 dest=out/'objects'/e['oid'];dest.parent.mkdir(exist_ok=True);dest.write_bytes(raw);objects.append({'oid':e['oid'],'type':'blob','sha256':h(raw),'bytes':len(raw),'source_path':e['path']})
 p=product/e['path'];assert p.is_file();data=p.read_bytes();assert data==raw;dst=out/'files'/e['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data);files.append({'path':e['path'],'mode':oct(p.stat().st_mode&0o777),'sha256':h(data),'bytes':len(data)})
roots=['77e7106e3134cc7053a2b1a045cf1a76cf0361ea','2d96774221165ac04096c8d57ddcefe85b2305e0','dbf50d7b6d83c7ddf53f287d82b199db3e83fd89','ca24007134141265a1937c77e2fda504bb0d6129','b49a26b36d68dc9bab8cf83633f5b7a2aae81eea','c05b65958e2a386cf2ae8782dca3e749ed9b60ff','549a25f4f1bc7702afa0b729fc0894918ec9d16d','fbe8bedf4c6cba1ab29d53d2da05e614603d76d1']
for oid in roots:
 raw=run(['cat-file','commit',oid],True);c.clean_bytes(raw);dest=out/'objects'/oid;dest.write_bytes(raw);objects.append({'oid':oid,'type':'commit','sha256':h(raw),'bytes':len(raw)})
 tree=run(['rev-parse',oid+'^{tree}']).decode().strip();raw=run(['cat-file','tree',tree],True);c.clean_bytes(raw);(out/'objects'/tree).write_bytes(raw);objects.append({'oid':tree,'type':'tree','sha256':h(raw),'bytes':len(raw)})
index=product/'.git/index';data=index.read_bytes();c.clean_bytes(data);(out/'index.original').write_bytes(data)
for label,args in [('staged',['diff','--cached','--binary']),('unstaged',['diff','--binary'])]:
 raw=run(args,True);c.clean_bytes(raw);(out/(label+'.patch')).write_bytes(raw)
refs=run(['show-ref']);(out/'refs.original').write_bytes(refs)
manifest={'scope':'Complete actual clean current tracked file/index/blob state; explicit reached case commits and root trees. Original helper whole reachable history export rejected sensitive bytes; no complete-history bundle asserted.','head':roots[-2],'index':entries,'index_sha256':h(data),'objects':objects,'files':files,'history_bundle':None,'complete_current_tracked_state':True,'complete_reachable_history':False,'original_recovery_failure':'Pinned observe helper sensitive_content_not_exportable, exact original commands/outcome retained separately'}
for name,d in [('manifest.json',manifest),('commands.json',commands)]:
 raw=(json.dumps(d,indent=2)+'\n').encode();c.clean_bytes(raw);c.no_secret(json.loads(raw));(out/name).write_bytes(raw)
print(len(entries),'current files',len(objects),'objects')
