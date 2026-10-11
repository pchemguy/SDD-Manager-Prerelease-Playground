import pathlib,json,hashlib,shutil,importlib.util,time
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');out=base/'037-a013-final-artifacts/sealed-consumer';out.mkdir();cp=base/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py';h=lambda b:hashlib.sha256(b).hexdigest();assert h(cp.read_bytes())=='f3a25204cd110d934f42261dda28a30708f22baae03bbaf921fa098e6c883ee0';sp=importlib.util.spec_from_file_location('coreguard',cp);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
seal=json.loads((base/'037-a013-consumer-blocked-seal.json').read_text());assert h((base/'037-a013-consumer-blocked-seal.json').read_bytes())=='b412f23d320d90ab77ab1c2368e9bd20f1ed7efa03222c91948e365e49e9bf0a';assert h((base/'037-a013-consumer-observations.json').read_bytes())==seal['original_observations']['sha256'];assert h((base/'037-a013-consumer-observations-surviving-race-checkpoint.json').read_bytes())==seal['surviving_race_checkpoint']['sha256'];files=[];reject=[];aggregate=hashlib.sha256();children=sorted((base/'037-a013-consumer-command-records').glob('*.json'));assert len(children)==7537
for p in children:aggregate.update(p.name.encode()+b'\0'+hashlib.sha256(p.read_bytes()).digest())
assert aggregate.hexdigest()==seal['immutable_children']['aggregate_sha256']
selected=[p for p in base.glob('037-a013-consumer-*') if p.is_file() and not p.name.endswith('.lock')]+children
for p in selected:
 rel=pathlib.Path('command-records')/p.name if p.parent.name=='037-a013-consumer-command-records' else pathlib.Path(p.name);raw=p.read_bytes()
 try:
  c.clean_bytes(raw)
  try:d=json.loads(raw)
  except (ValueError,UnicodeDecodeError):valid=False
  else:c.no_secret(d);valid=True
 except Exception as e:
  reject.append({'path':str(p),'sha256':h(raw),'cause':getattr(e,'cause',type(e).__name__)});continue
 dest=out/rel;dest.parent.mkdir(exist_ok=True);dest.write_bytes(raw);files.append({'path':str(rel),'original':str(p),'sha256':h(raw),'bytes':len(raw),'JSON_sniff_valid':valid,'whole_file_clean_bytes':True,'no_secret_if_validJSON':True})
manifest={'kind':'Exact sealed consumer originals exported with whole-file pinned guard and generic JSON sniff','core_sha256':h(cp.read_bytes()),'seal_sha256':h((base/'037-a013-consumer-blocked-seal.json').read_bytes()),'immutable_children_count':len(children),'immutable_children_aggregate':aggregate.hexdigest(),'files':files,'rejected':reject,'limitations':'Unknown overwritten first channels are unavailable; surviving checkpoint is later than race and is not a reconstructed pre-race backup'};raw=(json.dumps(manifest,indent=2)+'\n').encode();c.clean_bytes(raw);c.no_secret(json.loads(raw));(out/'MANIFEST.json').write_bytes(raw);print(len(files),'exact files;',len(reject),'rejected');assert not reject
