from pathlib import Path
import importlib.util,json,hashlib,subprocess,collections,zipfile,datetime
root=Path(__file__).resolve().parent.parent
repo=root/'037-test-evidence'; b=repo/'docs/dev/reviews/001_eff696b-prerelease-acceptance'; out=Path(__file__).parent
cp=b/'resources/acceptance/textstats/scripts/core.py'
s=importlib.util.spec_from_file_location('core',cp);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
def sha(x):return hashlib.sha256(x).hexdigest()
def git(r,*a):return subprocess.check_output(['git','-C',str(r),*a])
head=git(repo,'rev-parse','HEAD').decode().strip()
pre=json.loads((b/'runs/A-027/1/pre-reconciliation/037-a027-independent-pre-reconciliation.json').read_bytes());records=[]
for r in pre['assessment_records']+[a for s in pre['supplements'] for a in s['assessments']]:
 p=r['assessment_path'];raw=(repo/p).read_bytes();g='Not JSON'
 try:parsed=json.loads(raw)
 except (ValueError,UnicodeDecodeError):pass
 else:
  try:c.no_secret(parsed);g='Passed'
  except c.Stop:g='Rejected'
 records.append({'path':p,'sha256':sha(raw),'recorded_sha_match':sha(raw)==r['sha256'],'published_byte_equal':raw==git(repo,'show',f'{head}:{p}'),'clean_bytes':c.clean_bytes(raw)==raw,'generic_json_guard':g})
ledgers={};optional=['A-023.live-response-loss','A-024.native-recovery']
for fn in ['VARIANT-RESULTS.json','VARIANT-RESULTS.corrected-rechecks.json']:
 raw=(b/fn).read_bytes();d=json.loads(raw);links=[]
 for k,v in d.items():
  p=v.get('assessment_path','')
  if not p:continue
  existing=next((x for x in [repo/p,b/p,b/'runs/A-027/1/final-independent'/p] if x.is_file()),None)
  links.append({'variant':k,'path':p,'exists':existing is not None,'sha256':sha(existing.read_bytes()) if existing else None})
 ledgers[fn]={'sha256':sha(raw),'entries':len(d),'case_ids':len({k.split('.')[0] for k in d}),'required_counts':dict(collections.Counter(v['status'] for k,v in d.items() if k not in optional)),'optional_counts':dict(collections.Counter(d[k]['status'] for k in optional)),'published_byte_equal':raw==git(repo,'show',f'{head}:{b.relative_to(repo)}/{fn}'),'resolved_paths':links}
source=root/'SDD-Manager';pin='ea515f5624c8a34cc4572731a2590223a5eb27f4'
zpath=b/'runs/A-027/1/final-source-verification/package/sdd-manager.zip';meta=json.loads((zpath.parent/'SOURCE-ARCHIVE.json').read_bytes());members=[]
with zipfile.ZipFile(zpath) as z:
 for m in meta['members']:
  raw=z.read('sdd-manager/'+m['path'])
  members.append({'path':m['path'],'sha256':sha(raw),'meta_equal':sha(raw)==m['sha256'],'pin_byte_equal':raw==git(source,'show',f'{pin}:{m["path"]}'),'archive_declared_source_byte_equal':raw==git(source,'show',f'{meta["source_commit"]}:{m["path"]}'),'current_source_byte_equal':raw==git(source,'show',f'HEAD:{m["path"]}')})
frozen=['docs/dev/reviews/'+x for x in ['038_d6218f1-tracking-fidelity','039_8bb3b3d-greenfield-prompt-order','040_a0685b5-revision-campaign-modes','041_ca99ca1-task-commit-contract']]
objects=git(source,'ls-tree','-r','HEAD','--',*frozen);previous=git(source,'ls-tree','-r','b246f8f','--',*frozen)
app=json.loads((b/'runs/A-027/1/final-source-verification/publisher-applicability/SOURCE-PUBLISHER-APPLICABILITY.json').read_bytes())
script=git(source,'show',meta['source_commit']+':.github/scripts/release.py');fixture=git(repo,'show',app['actual_tooling_fixture_commit']+':.github/scripts/release.py')
result={'schema_version':1,'case_id':'A-027','scope':'Independent published-record audit; final report/integration Pending','observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_head':head,'guard_sha256':sha(cp.read_bytes()),'ledgers':ledgers,'historical_assessment_records':records,'supplement_scopes':len(pre['supplements']),'prior_preparatory_attempts':pre['preparatory_attempts'],'own_preparatory_failures':['Attempt1: JSONDecodeError on nonJSON assessment before output write','Attempt2: zip member prefix omitted before output write','Attempt3: original abbreviated b246 ambiguous; explicit b246f8f commit selected before final audit'],'inherited_NUL_guard_gap':{'path':pre['a014_inherited_publication_gap']['original_path'],'sha256':pre['a014_inherited_publication_gap']['original_sha256'],'rejected_records':[x['path'] for x in records if x['generic_json_guard']=='Rejected']},'source_integrity':{'source_head':git(source,'rev-parse','HEAD').decode().strip(),'pin':pin,'zip_sha256':sha(zpath.read_bytes()),'member_count':len(members),'members':members,'pngs':[m for m in members if m['path'].endswith('.png')],'publisher_sha256':sha(script),'fixture_publisher_bytes_equal':script==fixture,'publisher_recorded_sha_equal':sha(script)==app['current_publisher_script_sha256'],'frozen_object_count':len(objects.splitlines()),'frozen_inventory_sha256':sha(objects),'frozen_b246_inventory_equal':objects==previous,'frozen_contents_read':False},'limits':['No final A027 workflow grade before exact report/tree and actual main publication','Historical A004/A005 Failed unchanged; separately corrected rechecks','Prior prepared grades/ledger errors immutable','Shared filesystem isolation, Python3.12.14 Unix, missing native/original channels and independent providerGET gaps remain','Strict creator Failed39 and historical NUL-only genericJSON rejection retained']}
raw=(json.dumps(result,indent=2)+'\n').encode();c.clean_bytes(raw);c.no_secret(json.loads(raw));(out/'CURRENT-LEDGER-SOURCE-AUDIT.json').write_bytes(raw)
for p in out.iterdir():
 if p.is_file():
  raw=p.read_bytes();c.clean_bytes(raw)
  try:d=json.loads(raw)
  except (ValueError,UnicodeDecodeError):pass
  else:c.no_secret(d)
result['source_integrity']['archive_declared_source']=meta['source_commit']
result['own_preparatory_failures'].append('Attempt4: current source main is preintegration a6c42dd and lacks archive revision-modes asset; comparison corrected to archive declared fb2a source, with current-source applicability pending separate actual integration assessment')
raw=(json.dumps(result,indent=2)+'\n').encode();c.clean_bytes(raw);c.no_secret(json.loads(raw));(out/'CURRENT-LEDGER-SOURCE-AUDIT.json').write_bytes(raw)
print(json.dumps({'path':str(out/'CURRENT-LEDGER-SOURCE-AUDIT.json'),'sha256':sha(raw),'historical_records':len(records),'hash_errors':[x['path'] for x in records if not x['recorded_sha_match'] or not x['published_byte_equal']],'unresolved_links':[(k,x['variant']) for k,v in ledgers.items() for x in v['resolved_paths'] if not x['exists']],'source_member_count':len(members),'source_differences':[x['path'] for x in members if not all(x[k] for k in ['meta_equal','pin_byte_equal','archive_declared_source_byte_equal'])],'png_count':len(result['source_integrity']['pngs']),'frozen_count':len(objects.splitlines()),'frozen_equal':objects==previous,'publisher_equal':script==fixture},indent=2))
