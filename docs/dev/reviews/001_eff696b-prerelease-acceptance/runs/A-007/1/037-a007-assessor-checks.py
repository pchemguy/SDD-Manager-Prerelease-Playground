import pathlib,json,subprocess,os,sys,re,hashlib,urllib.request,zipfile
r=pathlib.Path('/workspace/scratch/46b31bb4dff6');p=r/'037-textstats-product';a=r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/resources/acceptance/textstats/cases/assessor'
d=r/'037-a007-assessor-runtime';d.mkdir(exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest()
out={'schema_version':1,'commands':[],'runtime':sys.version,'failures':[]}
env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','PYTHONSTARTUP')};env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1',GIT_ASKPASS=str(r/'playground-askpass.sh'),GIT_TERMINAL_PROMPT='0')
def run(args,cwd=p,expect=0):
 x=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True);out['commands'].append({'argv':args,'cwd':str(cwd),'returncode':x.returncode,'stdout':x.stdout,'stderr':x.stderr});assert expect is None or x.returncode==expect,(args,x.returncode,x.stderr);return x
try:
 out['start_status']=run(['git','status','--porcelain']).stdout
 assert out['start_status']==''
 head=run(['git','rev-parse','HEAD']).stdout.strip();branch=run(['git','branch','--show-current']).stdout.strip();main=run(['git','rev-parse','main']).stdout.strip()
 assert main=='e7cae5b2216ff7dd311b6f7296d829d1927a6a8a' and branch.startswith('phase/2-') and head!=main
 out['checkpoint_refs']={'product_branch':branch,'product_commit':head,'integration_branch':'main','integration_commit':main}
 run(['git','merge-base','--is-ancestor',main,head]);run(['git','diff','--check',main+'..'+head])
 start=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-007/1/START.json'));out['preserved_hashes']={}
 for f,h in start['tracked_file_sha256'].items():
  if f.startswith(('textstats-run-resources/','.github/','docs/testing/','docs/dev/')) and f!='docs/dev/TASKS.md' or f in ('AI_DISCLOSURE.md','SDD-MANAGER.md','textstats/core.py','textstats/io.py','textstats/__init__.py'):
   assert sha((p/f).read_bytes())==h,f;out['preserved_hashes'][f]=h
 assert (p/'.gitignore').read_text().startswith(run(['git','show',main+':.gitignore']).stdout)
 commits=run(['git','rev-list','--reverse',main+'..'+head]).stdout.split();out['task_commits']=[];assert len(commits)==3
 for n,c in zip(range(10,13),commits):
  sub=run(['git','show','-s','--format=%s',c]).stdout.strip();assert sub.startswith('[T-%03d]'%n) and len(re.findall(r'\[T-\d+\]',sub))==1
  diff=run(['git','diff',c+'^',c,'--','docs/dev/TASKS.md']).stdout;initial=re.findall(r'^\+\s*- \[x\] (T-\d+)',diff,re.M);assert initial==['T-%03d'%n]
  assert '## T-%03d completion evidence'%n in diff
  paths=run(['git','diff-tree','--no-commit-id','--name-only','-r',c]).stdout.split();out['task_commits'].append({'task':'T-%03d'%n,'commit':c,'subject':sub,'initial_closures':initial,'paths':paths})
 text=(p/'docs/dev/TASKS.md').read_text();assert re.findall(r'^\s*- \[x\] (T-\d+)',text,re.M)==['T-%03d'%n for n in range(1,13)];assert '- [ ] Phase 2' in text
 assert not (p/'docs/dev/reports/phases/2/PHASE-REPORT.md').exists() and not (p/'docs/dev/reports/IMPLEMENTATION-REPORT.md').exists()
 assert '--json' in (p/'textstats/cli.py').read_text() and 'sys.stdin' not in (p/'textstats/cli.py').read_text()
 for suite in ('baseline','json'):
  run([sys.executable,'-B',str(a/'capture.py'),'--product-root',str(p),'--suite',suite,'--output',str(r/f'037-a007-{suite}-literals.json'),'--provenance',str(r/f'037-a007-{suite}-provenance.json'),'--python',sys.executable],r)
 snapshot=d/'exact-final-snapshot';snapshot.mkdir();names=run(['git','ls-files']).stdout.splitlines()
 for f in names:
  target=snapshot/f;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((p/f).read_bytes())
 out['snapshot']={'root':str(snapshot),'source_commit':head,'tracked_hashes':{f:sha((snapshot/f).read_bytes()) for f in names}}
 run([sys.executable,'-B','tools/check_tests.py'],snapshot)
 sys.path.insert(0,str(snapshot));from tools.package_source import build_archive,FILES
 archive=build_archive(snapshot,d/'actual-source.zip');out['distribution_build']={'call':'tools.package_source.build_archive(exact_tracked_snapshot, independent_output)','import_origin':str(sys.modules['tools.package_source'].__file__),'product_root':str(snapshot),'archive':str(archive),'sha256':sha(archive.read_bytes()),'source_commit':head}
 with zipfile.ZipFile(archive) as z:
  assert set(z.namelist())=={'textstats-source/'+n for n in FILES};z.extractall(d/'extracted');out['archive_members']=z.namelist()
 extraction=d/'extracted/textstats-source'
 for name in FILES:assert (extraction/name).read_bytes()==(p/name).read_bytes()
 out['extracted_content_sha256']={name:sha((extraction/name).read_bytes()) for name in FILES}
 run([sys.executable,'-B',str(a/'capture.py'),'--product-root',str(extraction),'--suite','json','--output',str(r/'037-a007-extracted-json-literals.json'),'--provenance',str(r/'037-a007-extracted-json-provenance.json'),'--python',sys.executable],r)
 run([sys.executable,'-B','tools/check_distribution.py'],extraction)
 out['docs_fences']=[]
 for document in ('README.md','docs/public-api.md'):
  for i,(lang,code) in enumerate(re.findall(r'```(bash|python)\n(.*?)```',(snapshot/document).read_text(),re.S),1):
   args=['bash','-e','-c',code] if lang=='bash' else [sys.executable,'-B','-c',code]
   x=run(args,snapshot);out['docs_fences'].append({'document':document,'fence':i,'language':lang,'returncode':x.returncode})
  for link in re.findall(r'\]\(([^)]+)\)',(snapshot/document).read_text()):
   if '://' not in link:assert ((snapshot/document).parent/link.split('#')[0]).exists(),link
 # Exact authorized hosted identity, only read-only provider requests; retain sanitized fields/hashes.
 remote=run(['git','remote','get-url','origin']).stdout.strip();assert remote=='https://github.com/pchemguy/SDD-Manager-Prerelease-Playground.git';out['remote']=remote
 auth=r/'SDD-Manager-Prerelease-Playground';assert subprocess.run(['git','check-ignore','-q','--','gh.tkn'],cwd=auth).returncode==0;assert subprocess.check_output(['git','ls-files','--','gh.tkn'],cwd=auth)==b'';token=(auth/'gh.tkn').read_text().strip();out['authentication']={'ignored':True,'untracked':True,'transient_memory_only':True}
 def get(path):
  req=urllib.request.Request('https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground'+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
  with urllib.request.urlopen(req,timeout=40) as x:
   data=json.load(x);assert 'rel="next"' not in x.headers.get('Link','');out.setdefault('provider_operations',[]).append({'method':'GET','path':path,'status':x.status});return data
 out['remote_refs']={b:get('/git/ref/heads/'+b)['object']['sha'] for b in ('main',branch,'design-docs/main')};assert out['remote_refs']['main']==main and out['remote_refs'][branch]==head
 issues=get('/issues?state=all&per_page=100');milestones=get('/milestones?state=all&per_page=100');labels=get('/labels?per_page=100');assert len(issues)==18 and len(milestones)==6
 old=json.load(open(r/'037-a006-consumer-observations.json'));initial=[x['tracking_snapshot'] for x in old['events'] if 'tracking_snapshot' in x][-1];out['issues']=[];out['milestones']=[];out['labels']=[{'name':v['name'],'color':v['color'],'description':v['description']} for v in labels]
 added_labels=set(v['name'] for v in labels)-set(initial['labels']);assert len(added_labels)==1 and next(iter(added_labels)).startswith('sdd-phase-2-');assert set(initial['labels']).issubset(v['name'] for v in labels)
 for x in issues:
  if x['number']<=10:
   before=next(v for v in initial['issues'] if v['number']==x['number']);assert x['body']==before['body'] and [v['name'] for v in x['labels']]==before['labels'];assert x['state']==before['state'];assert (x['milestone']['number'] if x['milestone'] else None)==before['milestone']
  out['issues'].append({'number':x['number'],'id':x['id'],'title':x['title'],'state':x['state'],'state_reason':x['state_reason'],'created_at':x['created_at'],'closed_at':x['closed_at'],'body_sha256':sha(x['body'].encode()),'labels':[v['name'] for v in x['labels']],'milestone':x['milestone']['number'] if x['milestone'] else None})
 for x in milestones:
  if x['number']<=3:
   before=next(v for v in initial['milestones'] if v['number']==x['number']);assert x['description']==before['description'] and x['state']==before['state']
  out['milestones'].append({'number':x['number'],'id':x['id'],'title':x['title'],'state':x['state'],'created_at':x['created_at'],'closed_at':x['closed_at'],'description_sha256':sha(x['description'].encode())})
 assert {x['number'] for x in issues}==set(range(1,19))
 for n in range(11,19):
  issue=next(x for x in issues if x['number']==n);assert issue['state']==('closed' if n<=13 else 'open');assert issue['state_reason']==('completed' if n<=13 else None)
  assert 'T-%03d'%(n-1) in issue['title'];assert set(v['name'] for v in issue['labels'])==added_labels;assert issue['milestone']['number']==(4 if n<=13 else 5 if n<=17 else 6)
  assert issue['created_at']>max(m['closed_at'] for m in milestones if m['number']<=3)
 assert next(x for x in milestones if x['number']==4)['state']=='closed' and all(x['state']=='open' for x in milestones if x['number']>=5)
 out['comments']=[]
 fixture=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-003/1/SECOND-PRESERVATION-FIXTURE.json'))
 for num in (2,11,12,13):
  comments=get('/issues/'+str(num)+'/comments?per_page=100')
  if num==2:assert sha(next(x for x in comments if x['id']==fixture['comment']['id'])['body'].encode())==fixture['comment']['body_sha256']
  else:assert any(commits[num-11] in x['body'] or commits[num-11][:7] in x['body'] for x in comments)
  out['comments'] += [{'issue':num,'id':x['id'],'created_at':x['created_at'],'body_sha256':sha(x['body'].encode())} for x in comments]
 assert all(next(i for i in issues if i['number']==n)['closed_at']<next(m for m in milestones if m['number']==4)['closed_at'] for n in (11,12,13))
 out['final_status']=run(['git','status','--porcelain']).stdout;assert out['final_status']==out['start_status'];out['result']='Passed'
except BaseException as e:
 out['result']='Failed';out['failures'].append({'type':type(e).__name__,'message':str(e)})
finally:
 (r/'037-a007-independent-check-evidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':out.get('result'),'failures':out['failures'],'commands':len(out['commands'])}))
