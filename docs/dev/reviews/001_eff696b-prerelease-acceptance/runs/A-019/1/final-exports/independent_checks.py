from pathlib import Path
import subprocess,json,hashlib,tarfile,zipfile,os,re,shutil,sys
base=Path('/workspace/scratch/46b31bb4dff6');out=base/'037-a019-final-artifacts';repo=base/'037-a019-integration';evidence=base/'037-test-evidence';campaign='docs/dev/reviews/001_eff696b-prerelease-acceptance';case=campaign+'/runs/A-019/1';assessor=evidence/campaign/'resources/acceptance/textstats/cases/assessor';commands=[];facts={};failures=[]
env={k:v for k,v in os.environ.items() if k not in ['PYTHONPATH','PYTHONHOME','PYTHONSTARTUP']};env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1')
sha=lambda b:hashlib.sha256(b).hexdigest()
def run(args,cwd=repo,inp=None,binary=False,expected=0):
 r=subprocess.run(args,cwd=cwd,env=env,input=inp,capture_output=True);n=len(commands);rec={'argv':args,'cwd':str(cwd),'returncode':r.returncode,'stderr':r.stderr.decode(errors='replace')}
 if binary or b'\0' in r.stdout:
  p=out/f'COMMAND{n:03d}-STDOUT.bin';p.write_bytes(r.stdout);rec['stdout']={'sidecar':p.name,'sha256':sha(r.stdout),'bytes':len(r.stdout)}
 else:rec['stdout']=r.stdout.decode(errors='replace')
 commands.append(rec)
 assert expected is None or r.returncode==expected,(args,r.returncode,r.stderr.decode(errors='replace'))
 return r.stdout
try:
 head=run(['git','--no-optional-locks','rev-parse','HEAD']).decode().strip();assert head=='2bcbf7d3f4b64321e3ca014a8ea9f4f9fa442749';parents=run(['git','show','-s','--format=%P',head]).decode().split();assert parents==['3ebf358ae5851a797f7390c1e75889b2cb18673d','bbd5b80e588337f14d8ec3221fea2aded33f0239'];tree=run(['git','rev-parse',head+'^{tree}']).decode().strip();assert tree=='b57a3f4c8e1b90dc19e96546fb1f5317c6760ba2';assert run(['git','branch','--show-current']).decode().strip()=='a019/target';assert not run(['git','--no-optional-locks','status','--porcelain']);assert not run(['git','--no-optional-locks','ls-files','--unmerged']);assert not (repo/'.git/MERGE_HEAD').exists()
 remote=run(['git','ls-remote','trial-delivery','refs/heads/a019/target','refs/heads/a019/incoming']).decode();assert head+'\trefs/heads/a019/target' in remote and parents[1]+'\trefs/heads/a019/incoming' in remote;assert run(['git','rev-parse','a019/incoming']).decode().strip()==parents[1];run(['git','merge-base','--is-ancestor',parents[1],head]);run(['git','diff','--check',parents[0],head]);facts['checkpoint_refs']={'product_branch':'a019/target','product_commit':head,'integration_branch':'a019/target','integration_commit':head,'merge_parents':parents,'incoming_branch':'a019/incoming','incoming_commit':parents[1],'tree':tree};facts['local_remote_readback']=remote
 changed=run(['git','diff','--name-only',parents[1],head]).decode().splitlines();assert set(changed)=={'AGENTS.md','README.md','docs/dev/reports/phases/1/PHASE-REPORT.md','docs/public-api.md','tests/integration/test_prospective_contract.py','tests/unit/test_core.py','textstats/core.py','tools/check_distribution.py'};facts['changed_against_incoming']=changed
 assert run(['git','show',head+':tests/integration/test_prospective_contract.py'])==run(['git','show',parents[0]+':tests/integration/test_prospective_contract.py']);assert run(['git','show',head+':textstats/core.py'])==run(['git','show','5b17e4650c64c7c735991931b591bdabb8069215:textstats/core.py']);assert not run(['git','diff','--name-only',parents[1],head,'--','textstats-run-resources','.github','docs/testing','docs/dev/TASKS.md','AI_DISCLOSURE.md','SDD-MANAGER.md']);facts['preservation']='Original prospective tests byte-identical; core restored exactly to original complete phase; task owners and protected resources unchanged from incoming.'
 tasks=(repo/'docs/dev/TASKS.md').read_text();assert re.findall(r'^\s*- \[x\] (T-\d{3})\b',tasks,re.M)==[f'T-{n:03d}' for n in range(1,10)];assert re.findall(r'^\s*- \[ \] (T-\d{3})\b',tasks,re.M)==[f'T-{n:03d}' for n in range(10,18)];assert not (repo/'docs/dev/reports/phases/2').exists();assert not (repo/'docs/dev/reports/IMPLEMENTATION-REPORT.md').exists();assert '--json' not in (repo/'textstats/cli.py').read_text();facts['task_boundary']='T001-009 closed; T010-017 pending, no Phase2/final/release work.'
 # Retain exact original consumer seals, raw repair logs and published review identity.
 for p in [base/'037-a019-conflict-observations.json',base/'037-a019-prospective-observations.json',base/'037-a019-recovery-observations.json',base/'037-a019-recovery-input.md',*base.glob('037-a019-repair-*.json')]:shutil.copyfile(p,out/p.name)
 decisionraw=run(['git','show','88fd0eacd1edfea261eabad89b8a41c4a2a61823:'+case+'/REPAIR-DECISION.json'],evidence);decision=json.loads(decisionraw);assert decision['pending_tree']==tree and decision['parents']==parents
 for p,obj in decision['artifact_blobs'].items():assert run(['git','rev-parse',head+':'+p]).decode().strip()==obj
 for n,h in decision['log_sha256'].items():assert sha((base/n).read_bytes())==h
 (out/'REPAIR-DECISION.json').write_bytes(decisionraw);facts['accepted_review']={'commit':'88fd0eacd1edfea261eabad89b8a41c4a2a61823','tree':tree,'seven_artifact_blobs_exact':True,'raw_review_log_hashes_exact':True}
 # Revalidate durable publication against exact historical commits and compare original export bytes.
 publications=[('31ce4fa8b43ecb2ba599e4a3bde32613347a224c','setup-exports',base/'037-a019-setup-artifacts'),('75a14d4b60c72cf9a20ae377a7526086a67978a3','conflict-exports',base/'037-a019-conflict-artifacts'),('8e51a8c','prospective-exports',base/'037-a019-prospective-artifacts')];facts['historical_publications']=[]
 for rev,sub,directory in publications:
  full=run(['git','rev-parse',rev],evidence).decode().strip();manifest=json.loads((directory/'SHA256SUMS.json').read_text());checked=[]
  for n,h in manifest.items():
   assert sha((directory/n).read_bytes())==h
   if sub=='conflict-exports' and n=='COMMANDS.json':continue
   actual=run(['git','show',full+':'+case+'/'+sub+'/'+n],evidence,binary=True);assert sha(actual)==h,n;checked.append(n)
  facts['historical_publications'].append({'commit':full,'path':case+'/'+sub,'original_manifest_matches':True,'verified_published_files':checked})
 provenancepath=case+'/conflict-exports/PUBLICATION-PROVENANCE.json';provenance=run(['git','show','75a14d4:'+provenancepath],evidence);(out/'ORIGINAL-SCREENING-PROVENANCE.json').write_bytes(provenance);p=json.loads(provenance);original=(base/'037-a019-conflict-artifacts/COMMANDS.json').read_bytes();assert sha(original)==p['original_sha256'];derived=run(['git','show','75a14d4:'+case+'/conflict-exports/COMMANDS-screened.json'],evidence);raw=run(['git','show','75a14d4:'+case+'/conflict-exports/COMMAND12-STDOUT.bin'],evidence,binary=True);assert sha(raw)==p['binary_sha256'];o=json.loads(original);d=json.loads(derived);assert o[12]['stdout'].encode()==raw;o[12]['stdout']=d[12]['stdout'];assert o==d;facts['screening_derivative_exact']='Original locally exact; only command12 stdout scalar converted to published exact binary sidecar. Initial NUL JSON screening rejection retained.'
 # Export final Git/index/files before checks; tests run only in a separate restored exact snapshot.
 stages=run(['git','--no-optional-locks','ls-files','--stage']).decode();(out/'index-stages.txt').write_text(stages);shutil.copyfile(repo/'.git/index',out/'index.raw');paths=run(['git','--no-optional-locks','ls-files','-z']).decode().rstrip('\0').split('\0');files={}
 with tarfile.open(out/'workfiles.tar','w') as tf:
  for n in paths:
   p=repo/n;tf.add(p,arcname=n,recursive=False);files[n]={'sha256':sha(p.read_bytes()) if not p.is_symlink() else None,'mode':oct(p.lstat().st_mode),'symlink':os.readlink(p) if p.is_symlink() else None}
 (out/'workfile-manifest.json').write_text(json.dumps(files,indent=2)+'\n');run(['git','bundle','create',str(out/'objects.bundle'),'refs/heads/a019/target','refs/heads/a019/incoming','refs/a019/provenance']);run(['git','bundle','verify',str(out/'objects.bundle')]);snapshot=base/'037-a019-final-assessor-snapshot';run(['git','clone','--no-checkout','--branch','a019/target',str(out/'objects.bundle'),str(snapshot)],base);run(['git','config','--unset','branch.a019/target.remote'],snapshot);run(['git','config','--unset','branch.a019/target.merge'],snapshot)
 with tarfile.open(out/'workfiles.tar') as tf:tf.extractall(snapshot,filter='data')
 shutil.copyfile(out/'index.raw',snapshot/'.git/index');assert run(['git','--no-optional-locks','ls-files','--stage'],snapshot).decode()==stages;assert not run(['git','--no-optional-locks','status','--porcelain'],snapshot)
 for n,rec in files.items():
  if rec['sha256']:assert sha((snapshot/n).read_bytes())==rec['sha256']
 for obj in {x.split()[1] for x in stages.splitlines()}:run(['git','cat-file','-e',obj],snapshot)
 facts['restoration']={'exact_final_head':head,'exact_stages':True,'workfile_count':len(files),'bundle_complete':True,'snapshot':str(snapshot)}
 # Independent final behavioral checks and literal expected comparisons.
 runner=run([sys.executable,'-B','tools/check_tests.py'],snapshot).decode();assert 'unit: 23 tests' in runner and 'integration: 20 tests' in runner and '38 extracted module cases passed' in runner
 distribution=run([sys.executable,'-B','tools/check_distribution.py'],snapshot).decode();assert '38 extracted module cases passed' in distribution;run([sys.executable,'-B','-m','unittest','tests.integration.test_prospective_contract','-v'],snapshot);facts['product_checks']={'unit':23,'integration':20,'prospective_public_tests':2,'extracted_module_cases':38,'all_returncode':0}
 expected=json.loads((assessor/'expected.json').read_text())['literals'];facts['literal_suites']={}
 for suite in ['api','baseline']:
  run([sys.executable,'-B',str(assessor/'capture.py'),'--product-root',str(snapshot),'--suite',suite,'--output',str(out/f'{suite}-literals.json'),'--provenance',str(out/f'{suite}-provenance.json'),'--python',sys.executable],base)
  actual=json.loads((out/f'{suite}-literals.json').read_text())['literals']
  for k,v in actual.items():assert expected[k]==v,k
  facts['literal_suites'][suite]='All actual observed literals exactly match immutable assessor expected values.'
 archive=snapshot/'dist/textstats-source.zip';shutil.copyfile(archive,out/'actual-source.zip');extraction=base/'037-a019-final-assessor-extraction';extraction.mkdir()
 with zipfile.ZipFile(archive) as z:z.extractall(extraction);members=z.namelist()
 extracted=extraction/'textstats-source'
 for n in members:assert (extraction/n).read_bytes()==(snapshot/n.removeprefix('textstats-source/')).read_bytes()
 run([sys.executable,'-B',str(assessor/'capture.py'),'--product-root',str(extracted),'--suite','distribution','--output',str(out/'distribution-literals.json'),'--provenance',str(out/'distribution-provenance.json'),'--python',sys.executable],base)
 for k,v in json.loads((out/'distribution-literals.json').read_text())['literals'].items():assert expected[k]==v,k
 facts['literal_suites']['distribution']='Actual extracted origin and all observed literals exactly match immutable expected values.';facts['archive']={'sha256':sha(archive.read_bytes()),'members':members,'all_source_bytes_match':True}
 # Execute each runnable user document fence verbatim; -B/env preserved for child Python.
 facts['docs_fences']=[]
 for document in ['README.md','docs/public-api.md']:
  for i,(lang,code) in enumerate(re.findall(r'```(bash|python)\n(.*?)```',(snapshot/document).read_text(),re.S),1):
   args=['bash','-e','-c',code] if lang=='bash' else [sys.executable,'-B','-c',code];result=run(args,snapshot).decode();facts['docs_fences'].append({'document':document,'fence':i,'language':lang,'returncode':0,'code_sha256':sha(code.encode())})
  for link in re.findall(r'\]\(([^)]+)\)',(snapshot/document).read_text()):
   if '://' not in link:assert ((snapshot/document).parent/link.split('#')[0]).exists(),link
 assert len(facts['docs_fences'])==7
 # Original source/index still untouched, compare after independent snapshot checks.
 assert not run(['git','--no-optional-locks','status','--porcelain']);assert sha((repo/'.git/index').read_bytes())==sha((out/'index.raw').read_bytes());assert run(['git','rev-parse','HEAD']).decode().strip()==head;facts['original_trial_unchanged_by_assessment']=True;facts['runtime']=sys.version;facts['result']='Passed'
except BaseException as e:
 failures.append({'type':type(e).__name__,'message':str(e)});facts['result']='Failed'
finally:
 facts['failures']=failures;(out/'INDEPENDENT-CHECKS.json').write_text(json.dumps(facts,indent=2)+'\n');(out/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(json.dumps({'result':facts.get('result'),'failures':failures,'command_count':len(commands)},indent=2))
