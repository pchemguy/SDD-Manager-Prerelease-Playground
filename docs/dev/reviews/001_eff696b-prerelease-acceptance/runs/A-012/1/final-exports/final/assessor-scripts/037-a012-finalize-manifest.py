import pathlib,json,hashlib,sys,shutil,signal
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');src=base/'037-a012-final-artifacts';pub=base/'037-a012-publishable-artifacts';sys.path.insert(0,str(base/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts'));import core
manifest=json.loads((src/'safe-publication-manifest.json').read_text());rows={r['original_path']:r for r in manifest['files']}
class GuardLimit(Exception):pass
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(GuardLimit()))
def screen(data,suffix):
 signal.alarm(10)
 try:
  core.clean_bytes(data)
  try:parsed=json.loads(data)
  except (ValueError,UnicodeDecodeError):parsed=None
  if parsed is not None:core.no_secret(parsed)
  if suffix=='.jsonl':
   for line in data.decode().splitlines():core.no_secret(json.loads(line))
 finally:signal.alarm(0)
for p in sorted(src.rglob('*')):
 if not p.is_file() or p.name=='safe-publication-manifest.json':continue
 rel=str(p.relative_to(src));raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest()
 if rel not in rows:
  screen(raw,p.suffix);dest=pub/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);rows[rel]={'original_path':rel,'original_sha256':h,'original_bytes':len(raw),'original_mode':oct(p.stat().st_mode&0o777),'original_retained':True,'published_path':rel,'publication_form':'exact original'}
 else:assert rows[rel]['original_sha256']==h,(rel,'original changed')
checks=[]
for p in sorted(pub.rglob('*')):
 if not p.is_file() or p.name=='safe-publication-manifest.json':continue
 raw=p.read_bytes();screen(raw,p.suffix);checks.append({'published_path':str(p.relative_to(pub)),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'mode':oct(p.stat().st_mode&0o777),'clean_bytes_passed':True,'no_secret_passed_for_every_valid_JSON_JSONL':True})
manifest.update(files=list(rows.values()),original_files=len(rows),complete_original_inventory=True,publishable_files=checks,all_published_files_rechecked_with_generic_JSON_sniff=True)
payload=(json.dumps(manifest,indent=2)+'\n').encode();screen(payload,'.json');(src/'safe-publication-manifest.json').write_bytes(payload);(pub/'safe-publication-manifest.json').write_bytes(payload);print(json.dumps({'original_files':len(rows),'published_files':len(checks)+1,'exact_originals':sum(r['publication_form']=='exact original' for r in rows.values()),'explicit_derivatives':sum(r['publication_form']=='explicit screened derivative' for r in rows.values()),'complete':True,'all_dual_guard_rechecked':True,'manifest_sha256':hashlib.sha256(payload).hexdigest()}))
