import pathlib,json,subprocess,os,sys,re,hashlib,urllib.request,zipfile,io,contextlib
from unittest.mock import patch
r=pathlib.Path('/workspace/scratch/46b31bb4dff6');p=r/'037-textstats-product';a=r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/cases/assessor';d=r/'037-a006-assessor-runtime';d.mkdir(exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest();out={'schema_version':1,'commands':[],'runtime':sys.version,'failures':[]}
env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','PYTHONSTARTUP')};env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1')
def run(args,cwd=p,expect=0):
 x=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True);out['commands'].append({'argv':args,'cwd':str(cwd),'returncode':x.returncode,'stdout':x.stdout,'stderr':x.stderr});assert expect is None or x.returncode==expect,(args,x.returncode,x.stderr);return x
try:
 out['start_status']=run(['git','status','--porcelain']).stdout
 head=run(['git','rev-parse','HEAD']).stdout.strip();phase=run(['git','rev-parse','phase/1-named-file-utility']).stdout.strip();parents=run(['git','show','-s','--format=%P','HEAD']).stdout.split();assert head=='e7cae5b2216ff7dd311b6f7296d829d1927a6a8a' and parents==['88a5c4b4424f4bba76940e40b1d6523b1f6fe191',phase];assert run(['git','branch','--show-current']).stdout.strip()=='main';assert run(['git','diff','HEAD','phase/1-named-file-utility','--exit-code']).returncode==0
 out['checkpoint_refs']={'product_branch':'main','product_commit':head,'integration_branch':'main','integration_commit':head,'merge_parents':parents,'phase_branch':'phase/1-named-file-utility','phase_commit':phase}
 run(['git','merge-base','--is-ancestor',phase,head]);run(['git','diff','--check','7d003c1..HEAD'])
 start=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-006/1/START.json'));out['preserved_hashes']={}
 for f,h in start['tracked_file_sha256'].items():
  if f.startswith(('textstats-run-resources/','.github/','docs/testing/')) or f in ('AI_DISCLOSURE.md','SDD-MANAGER.md') or f.startswith('docs/dev/') and f!='docs/dev/TASKS.md':
   assert sha((p/f).read_bytes())==h,f;out['preserved_hashes'][f]=h
 oldignore=run(['git','show',start['head']+':.gitignore']).stdout;assert (p/'.gitignore').read_text().startswith(oldignore)
 commits=run(['git','rev-list','--reverse',start['head']+'..'+phase]).stdout.split();assert len(commits)==5;out['task_commits']=[]
 for n,c in zip(range(5,10),commits):
  sub=run(['git','show','-s','--format=%s',c]).stdout.strip();assert sub.startswith('[T-%03d]'%n) and len(re.findall(r'\[T-\d+\]',sub))==1
  diff=run(['git','diff',c+'^',c,'--','docs/dev/TASKS.md']).stdout;initial=re.findall(r'^\+\s*- \[x\] (T-\d+)',diff,re.M);assert initial==['T-%03d'%n]
  assert '## T-%03d completion evidence'%n in diff
  paths=run(['git','diff-tree','--no-commit-id','--name-only','-r',c]).stdout.split();out['task_commits'].append({'task':'T-%03d'%n,'commit':c,'subject':sub,'initial_closures':initial,'paths':paths})
 text=(p/'docs/dev/TASKS.md').read_text();assert re.findall(r'^\s*- \[x\] (T-\d+)',text,re.M)==['T-%03d'%n for n in range(1,10)];assert '- [ ] Phase 2' in text and not (p/'docs/dev/reports/phases/2').exists() and not (p/'docs/dev/reports/IMPLEMENTATION-REPORT.md').exists()
 assert '--json' not in (p/'textstats/cli.py').read_text()
 run([sys.executable,'-B','tools/check_tests.py'])
 for suite in ('api','baseline'):
  run([sys.executable,'-B',str(a/'capture.py'),'--product-root',str(p),'--suite',suite,'--output',str(r/f'037-a006-{suite}-literals.json'),'--provenance',str(r/f'037-a006-{suite}-provenance.json'),'--python',sys.executable],r)
 sys.path.insert(0,str(p));from tools.package_source import build_archive,FILES
 archive=build_archive(p,d/'actual-source.zip');out['distribution_build']={'call':'tools.package_source.build_archive(actual_product_root, independent_output)','product_root':str(p),'archive':str(archive),'sha256':sha(archive.read_bytes()),'source_commit':head}
 with zipfile.ZipFile(archive) as z:
  assert set(z.namelist())=={'textstats-source/'+n for n in FILES};z.extractall(d/'extracted');out['archive_members']=z.namelist()
 extraction=d/'extracted/textstats-source'
 for name in FILES:assert (extraction/name).read_bytes()==(p/name).read_bytes()
 out['extracted_content_sha256']={name:sha((extraction/name).read_bytes()) for name in FILES}
 run([sys.executable,'-B',str(a/'capture.py'),'--product-root',str(extraction),'--suite','distribution','--output',str(r/'037-a006-distribution-literals.json'),'--provenance',str(r/'037-a006-distribution-provenance.json'),'--python',sys.executable],r)
 run([sys.executable,'-B','tools/check_distribution.py'],extraction)
 from textstats import count_file,TextStats
 captured=io.StringIO()
 with contextlib.redirect_stdout(captured),contextlib.redirect_stderr(captured):
  for raw,expected in ((b'a\r\nb\rc\n',TextStats(3,3)),(b'\xef\xbb\xbf',TextStats(0,0))):
   s=io.BytesIO(raw)
   with patch('textstats.io.open',return_value=s,create=True):assert count_file('independent')==expected
   assert s.closed
  s=io.BytesIO(b'valid\n\xff')
  with patch('textstats.io.open',return_value=s,create=True):
   try:count_file('independent')
   except UnicodeDecodeError:pass
   else:raise AssertionError('decode accepted')
  assert s.closed
  class Broken(io.BytesIO):
   def read(self,*a):raise OSError('independent read failure')
  s=Broken()
  with patch('textstats.io.open',return_value=s,create=True):
   try:count_file('independent')
   except OSError:pass
   else:raise AssertionError('read accepted')
  assert s.closed
  error=PermissionError('independent unreadable')
  with patch('textstats.io.open',side_effect=error,create=True):
   try:count_file('independent')
   except PermissionError as got:assert got is error
   else:raise AssertionError('unreadable accepted')
 assert captured.getvalue()=='';out['independent_lifetime_silence']={'passed':True,'controlled_seams':True}
 # Execute all actual user-document fences on an exact tracked snapshot, keeping product untouched.
 snapshot=d/'exact-final-snapshot';snapshot.mkdir();names=run(['git','ls-files']).stdout.splitlines()
 for f in names:
  target=snapshot/f;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((p/f).read_bytes())
 out['docs_fences']=[]
 for document in ('README.md','docs/public-api.md'):
  for i,(lang,code) in enumerate(re.findall(r'```(bash|python)\n(.*?)```',(snapshot/document).read_text(),re.S),1):
   args=['bash','-e','-c',code] if lang=='bash' else [sys.executable,'-B','-c',code]
   x=run(args,snapshot);out['docs_fences'].append({'document':document,'fence':i,'language':lang,'returncode':x.returncode})
  for link in re.findall(r'\]\(([^)]+)\)',(snapshot/document).read_text()):
   if '://' not in link:assert ((snapshot/document).parent/link.split('#')[0]).exists(),link
 auth=r/'SDD-Manager-Prerelease-Playground';assert subprocess.run(['git','check-ignore','-q','--','gh.tkn'],cwd=auth).returncode==0;assert subprocess.check_output(['git','ls-files','--','gh.tkn'],cwd=auth)==b'';token=(auth/'gh.tkn').read_text().strip();out['authentication']={'ignored':True,'untracked':True}
 def get(path):
  req=urllib.request.Request('https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground'+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
  with urllib.request.urlopen(req,timeout=40) as x:
   data=json.load(x);assert 'rel="next"' not in x.headers.get('Link','');out.setdefault('provider_operations',[]).append({'method':'GET','path':path,'status':x.status});return data
 out['remote_refs']={b:get('/git/ref/heads/'+b)['object']['sha'] for b in ('main','phase/1-named-file-utility','design-docs/main')};assert out['remote_refs']['main']==head and out['remote_refs']['phase/1-named-file-utility']==phase
 issues=get('/issues?state=all&per_page=100');milestones=get('/milestones?state=all&per_page=100');assert len(issues)==10 and len(milestones)==3;assert {x['number'] for x in issues}==set(range(1,11));assert all(x['state']=='closed' and x['state_reason']=='completed' for x in issues if x['number']>=2);assert all(x['state']=='closed' for x in milestones)
 obs=json.load(open(r/'037-a006-consumer-observations.json'));initial=next(x['tracking_snapshot'] for x in obs['events'] if 'tracking_snapshot' in x);out['issues']=[];out['milestones']=[]
 for x in issues:
  old=next(v for v in initial['issues'] if v['number']==x['number']);assert x['body']==old['body'] and [v['name'] for v in x['labels']]==old['labels'];assert (x['milestone']['number'] if x['milestone'] else None)==old['milestone'];out['issues'].append({'number':x['number'],'id':x['id'],'state':x['state'],'closed_at':x['closed_at'],'body_sha256':sha(x['body'].encode()),'labels':[v['name'] for v in x['labels']]})
  if x['number']==1:assert x['state']=='open'
 for x in milestones:
  old=next(v for v in initial['milestones'] if v['number']==x['number']);assert x['description']==old['description'];out['milestones'].append({'number':x['number'],'id':x['id'],'state':x['state'],'closed_at':x['closed_at'],'description_sha256':sha(x['description'].encode())})
 assert all(next(i for i in issues if i['number']==n)['closed_at']<next(m for m in milestones if m['number']==2)['closed_at'] for n in range(6,10));assert next(i for i in issues if i['number']==10)['closed_at']<next(m for m in milestones if m['number']==3)['closed_at']
 fixture=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-003/1/SECOND-PRESERVATION-FIXTURE.json'));out['comments']=[]
 for num in (2,6,7,8,9,10):
  comments=get('/issues/'+str(num)+'/comments?per_page=100')
  if num==2:assert sha(next(x for x in comments if x['id']==fixture['comment']['id'])['body'].encode())==fixture['comment']['body_sha256']
  else:assert any(commits[num-6] in x['body'] or commits[num-6][:7] in x['body'] for x in comments)
  out['comments'] += [{'issue':num,'id':x['id'],'body_sha256':sha(x['body'].encode())} for x in comments]
 out['final_status']=run(['git','status','--porcelain']).stdout;assert out['final_status']==out['start_status'];out['result']='Passed'
except BaseException as e:
 out['result']='Failed';out['failures'].append({'type':type(e).__name__,'message':str(e)})
finally:
 (r/'037-a006-independent-check-evidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':out.get('result'),'failures':out['failures'],'commands':len(out['commands'])}));
