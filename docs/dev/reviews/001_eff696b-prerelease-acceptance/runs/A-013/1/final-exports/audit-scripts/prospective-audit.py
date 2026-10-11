import json,pathlib,hashlib,subprocess,zipfile,shutil,importlib.util
base=pathlib.Path('/workspace/scratch/46b31bb4dff6'); out=base/'037-a013-final-artifacts/prospective-integration';product=base/'037-textstats-product'
h=lambda b:hashlib.sha256(b).hexdigest()
corepath=base/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/scripts/core.py'
assert h(corepath.read_bytes())=='f3a25204cd110d934f42261dda28a30708f22baae03bbaf921fa098e6c883ee0'
spec=importlib.util.spec_from_file_location('a013core',corepath);core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
for src,dst in [('037-a013-consumer-integration-candidate.json','candidate.json'),('037-a013-consumer-phase2-merge.txt','merge-message.txt')]:shutil.copyfile(base/src,out/dst)
c=json.loads((out/'candidate.json').read_text());assert h((out/'candidate.json').read_bytes())=='e218a8a0cd3ec37fbd97457d32abef3a3c1893e00cdeb1a9da81d569f943f587';assert h((out/'merge-message.txt').read_bytes())=='eb51fa5b0e635b530fe212cc2adfcc2029adb6fe2db10244a973ad3d367e1157'
commands=[]
def git(*args):
 r=subprocess.run(['git',*args],cwd=product,capture_output=True);d={'argv':['git',*args],'status':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()};commands.append(d);assert r.returncode==0;return d['stdout'].strip()
assert git('rev-parse','HEAD')==c['parents'][0];assert git('rev-parse','MERGE_HEAD')==c['parents'][1];assert not git('diff','--name-only');assert not git('ls-files','-u');assert not git('diff','--cached',c['parents'][1],'--name-status')
obs=json.loads((base/'037-a013-consumer-observations.json').read_text());merged=[]
for r in obs['commands']:
 if 1791660743<=r.get('time',0)<=1791660870 and any(x in r.get('argv',[]) for x in ['tools/check_tests.py','tools/check_distribution.py']):merged.append(r)
assert len(merged)==2 and all(x['status']==0 for x in merged)
assert '478' in str(merged) and '37' in str(merged) and '34' in str(merged)
records=[]
for p in sorted((base/'037-a013-consumer-command-records').glob('*.json')):
 b=p.read_bytes();d=json.loads(b);r=d.get('record',{})
 if d.get('section')=='children' and 1791660743<=r.get('time',0)<=1791660870:
  assert '-B' in r['argv'] and r['environment']['PYTHONDONTWRITEBYTECODE']=='1';records.append({'path':p.name,'sha256':h(b),'time':r['time']})
assert len(records)==1628
shutil.copyfile(product/'dist/textstats-source.zip',out/'actual-prospective-source.zip'); archive=out/'actual-prospective-source.zip';assert h(archive.read_bytes())==c['archive_sha256']
members=[]
with zipfile.ZipFile(archive) as z:
 assert len(z.namelist())==11
 for i in z.infolist():
  rel='/'.join(i.filename.split('/')[1:]);b=z.read(i);assert b==(product/rel).read_bytes();members.append({'path':rel,'sha256':h(b),'bytes':len(b)})
audit={'commands':commands,'actual_merged_commands':merged,'immutable_child_records':records,'archive_members':members,'generic_JSON_guard':True,'independent_provider_GET':False}
(out/'independent-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
grade={'schema_version':1,'case_id':'A-013','status':'Passed','agent_behavior_assessed':True,'scope':'Independent prospective Phase2 integration gate only; actual merge commit/publication and final case seal remain pending','candidate_tree':c['tree'],'ordered_parents':c['parents'],'candidate_sha256':h((out/'candidate.json').read_bytes()),'merge_message_sha256':h((out/'merge-message.txt').read_bytes()),'findings':[],'assessment':['Actual readonly pending main observations establish exact ordered HEAD/MERGE_HEAD, conflict-free index and exact published phase tree; protected/history deltas from resume baseline were independently empty.','Inspected actual raw merged runner and checker commands: both status0 with37unit/34integration and478extracted cases/API probes. Independently enumerated1628 immutable fresh child records; all explicit-B/env1. Exact actual ZIP SHA and all11 member bytes match current sources. Timestamp-only archive difference and prior12document-fence reuse are correctly labeled.','Concrete merge body records substantive cumulative named ranges/removal/stdin/API and distinct milestone/final implementation review gates, resolved findings/TODO provenance, original logging/argv/cleanup limits, actual own issue18/reviewmilestone6 closure before integration, bounded hosted preservation and immediate target-publication boundary.','Prior own original literal API/baseline/ranges/removal/stdin/distribution and12fences apply to unchanged committed product/docs bytes; no tests executed on positive checkout.'],'evidence':['before-commit-observations.json','independent-audit.json','candidate.json','merge-message.txt','actual-prospective-source.zip'],'limits':['Consumer provider raw GET/PATCH records were inspected; independent provider GET is not claimed. Root additional four-resource late GET hash guard has its separate stated boundary.','No hard filesystem isolation exists. Shared filesystem access and first logger lost channels prevent universal complete read chronology or inaccessible-sibling certification.','This approves the concrete prospective integration only; completed actual merge/push/readback/seal and original DSL final reached-ref evaluation remain required.']}
(out/'ASSESSMENT.json').write_text(json.dumps(grade,indent=2)+'\n')
guarded=[]
for p in out.iterdir():
 if p.is_file():
  b=p.read_bytes();core.clean_bytes(b)
  try:d=json.loads(b)
  except (ValueError,UnicodeDecodeError):pass
  else:core.no_secret(d)
  guarded.append({'path':p.name,'sha256':h(b),'bytes':len(b)})
(out/'SCREENING.json').write_text(json.dumps({'pinned_core_sha256':h(corepath.read_bytes()),'whole_files':guarded,'JSON_sniff_regardless_extension':True},indent=2)+'\n');b=(out/'SCREENING.json').read_bytes();core.clean_bytes(b);core.no_secret(json.loads(b))
print(str(out/'ASSESSMENT.json'));print('Passed',len(records),len(members))
