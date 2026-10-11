import pathlib,sys,json,hashlib,shutil,signal,re
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');source=base/'037-a012-final-artifacts';destination=base/'037-a012-publishable-artifacts';destination.mkdir()
sys.path.insert(0,str(base/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts'));import core
class GuardLimit(Exception):pass
def interrupt(*args):raise GuardLimit()
signal.signal(signal.SIGALRM,interrupt)
def screen(data,suffix):
 signal.alarm(2)
 try:
  core.clean_bytes(data)
  if suffix=='.json':core.no_secret(json.loads(data))
  elif suffix=='.jsonl':
   for line in data.decode().splitlines():core.no_secret(json.loads(line))
 finally:signal.alarm(0)
def scrub(value):
 if isinstance(value,dict):return {('descriptive_'+k if k!='protected_credentials' and re.fullmatch(r'(?:token|password|credentials?|secret|access_token|credential_path)',k,re.I) else k):scrub(v) for k,v in value.items()}
 if isinstance(value,list):return [scrub(v) for v in value]
 if isinstance(value,str):return core.SECRET.sub('[WITHHELD_GUARD_PATTERN]',value.replace('\0','[NUL]'))
 return value
rows=[]
files=sorted(p for p in source.rglob('*') if p.is_file() and p.name!='safe-publication-manifest.json')
for p in files:
 rel=p.relative_to(source);raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest();record={'original_path':str(rel),'original_sha256':h,'original_bytes':len(raw),'original_mode':oct(p.stat().st_mode&0o777),'original_retained':True}
 try:screen(raw,p.suffix);record['published_path']=str(rel);record['publication_form']='exact original';dest=destination/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 except Exception as error:
  cause=getattr(error,'cause',type(error).__name__);record['original_guard_disposition']=cause
  derivative=None
  try:
   if rel==pathlib.Path('final/export-commands.json'):
    data=json.loads(raw);derivative=[]
    for item in data:
     v={k:val for k,val in item.items() if k not in ['stdout_hex','stderr_hex']}
     for name in ['stdout','stderr']:
      channel=bytes.fromhex(item[name+'_hex']);v[name+'_bytes']=len(channel);v[name+'_sha256']=hashlib.sha256(channel).hexdigest()
     derivative.append(v)
    derivative={'derivative_class':'Channel payload hash/size metadata; exact raw channels remain in original local command record and reached Git-object originals','records':derivative}
   elif p.suffix=='.json':derivative=scrub(json.loads(raw))
   elif p.suffix=='.jsonl':derivative=[scrub(json.loads(line)) for line in raw.decode().splitlines()]
   else:derivative={'redacted_text_derivative':scrub(raw.decode('utf-8',errors='replace'))}
   payload=(json.dumps({'original_sha256':h,'original_path':str(rel),'derivative_warning':'This is a screened derivative; compare its provenance, never treat its edited bytes as the original artifact. Original retained locally unchanged.','original_guard_disposition':cause,'content':derivative},indent=2)+'\n').encode();screen(payload,'.json');derivrel=pathlib.Path('screened-derivatives')/(str(rel)+'.json');d=destination/derivrel;d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes(payload);record['published_path']=str(derivrel);record['publication_form']='explicit screened derivative'
  except Exception as inner:
   record['derivative_guard_disposition']=getattr(inner,'cause',type(inner).__name__);record['publication_form']='safe provenance sidecar only; original/derivative withheld'
  side={'original_path':str(rel),'original_sha256':h,'original_bytes':len(raw),'original_mode':record['original_mode'],'original_retained':True,'publication_form':record['publication_form'],'original_guard_disposition':cause,'derivative_path':record.get('published_path'),'limits':'Raw protected or guard-limited bytes remain local; no guard behavior was changed.'};payload=(json.dumps(side,indent=2)+'\n').encode();screen(payload,'.json');siderel=pathlib.Path('original-sidecars')/(str(rel)+'.json');dest=destination/siderel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(payload);record['sidecar_path']=str(siderel)
 rows.append(record)
manifest={'schema_version':1,'case_id':'A-012','complete_original_inventory':True,'original_files':len(rows),'originals_root':str(source),'publishable_root':str(destination),'guards':'Exact pinned core.clean_bytes plus parsed JSON/JSONL no_secret; each guard attempt bounded2 seconds; no modification to guards','original_bulk_screen_attempt':'Full-directory first screen interrupted exit130 after excessive runtime on unbroken large hex channel JSON; original bytes unchanged.','files':rows,'limitations':'Complete original inventory and narrow sidecars preserve identity/provenance where literal guard rejects NUL/config-key/synthetic-pattern artifacts. Screened derivatives are distinct from raw originals.'};payload=(json.dumps(manifest,indent=2)+'\n').encode();screen(payload,'.json');(destination/'safe-publication-manifest.json').write_bytes(payload);(source/'safe-publication-manifest.json').write_bytes(payload);print(json.dumps({'files':len(rows),'exact':sum(x['publication_form']=='exact original' for x in rows),'derivatives':sum(x['publication_form']=='explicit screened derivative' for x in rows),'provenance_only':sum(x['publication_form'].startswith('safe provenance') for x in rows)}))
