import subprocess,json,hashlib,sys,os,pathlib,re,urllib.request,io,contextlib
from unittest.mock import patch
r=pathlib.Path('/workspace/scratch/46b31bb4dff6'); p=r/'037-textstats-product'; sha=lambda b:hashlib.sha256(b).hexdigest(); out={'schema_version':1,'commands':[]}
def run(a):
 x=subprocess.run(a,cwd=p,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'));out['commands'].append({'argv':a,'cwd':str(p),'returncode':x.returncode,'stdout':x.stdout,'stderr':x.stderr});return x
assert run([sys.executable,'-B','tools/check_tests.py']).returncode==0
head=run(['git','rev-parse','HEAD']).stdout.strip();assert head=='7d003c1cf31c994340d8644e95990ef2253754ed';assert run(['git','status','--porcelain']).stdout==''
main=run(['git','rev-parse','main']).stdout.strip();assert main=='88a5c4b4424f4bba76940e40b1d6523b1f6fe191';assert run(['git','merge-base','--is-ancestor',head,'main']).returncode==1
start=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-005/1/START.json'));out['preserved_start_hashes']={}
for f,h in start['tracked_file_sha256'].items():
 if f.startswith(('textstats-run-resources/','.github/','docs/testing/')) or f in ('.gitignore','AI_DISCLOSURE.md','SDD-MANAGER.md') or f.startswith('docs/dev/') and f!='docs/dev/TASKS.md':
  assert sha((p/f).read_bytes())==h;out['preserved_start_hashes'][f]=h
commits=run(['git','rev-list','--reverse',start['head']+'..HEAD']).stdout.split();assert len(commits)==3
out['task_commits']=[]
for n,c in zip((2,3,4),commits):
 subject=run(['git','show','-s','--format=%s',c]).stdout.strip();assert subject.startswith('[T-%03d]'%n) and len(re.findall(r'\[T-\d+\]',subject))==1
 diff=run(['git','diff',c+'^',c,'--','docs/dev/TASKS.md']).stdout
 initial=re.findall(r'^\+\s*- \[x\] (T-\d+)',diff,re.M);assert initial==['T-%03d'%n]
 paths=run(['git','diff-tree','--no-commit-id','--name-only','-r',c]).stdout.splitlines();out['task_commits'].append({'task':'T-%03d'%n,'commit':c,'subject':subject,'initial_closures':initial,'paths':paths})
text=(p/'docs/dev/TASKS.md').read_text();assert re.findall(r'^\s*- \[x\] (T-\d+)',text,re.M)==['T-001','T-002','T-003','T-004'];assert '- [ ] Phase 1' in text and '- [x] Milestone 1.1' in text
sys.path.insert(0,str(p));from textstats import count_file,TextStats
captured=io.StringIO()
with contextlib.redirect_stdout(captured),contextlib.redirect_stderr(captured):
 for raw,expect in ((b'a\r\nb\rc\n',TextStats(3,3)),(b'\xef\xbb\xbf',TextStats(0,0))):
  s=io.BytesIO(raw)
  with patch('textstats.io.open',return_value=s,create=True):assert count_file('independent')==expect
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
  else:raise AssertionError('read failure accepted')
 assert s.closed
 e=PermissionError('independent unreadable')
 with patch('textstats.io.open',side_effect=e,create=True):
  try:count_file('independent')
  except PermissionError as got:assert got is e
  else:raise AssertionError('unreadable accepted')
assert captured.getvalue()=='';out['independent_lifetime_unreadability']={'passed':True,'controlled_seams':True}
auth=r/'SDD-Manager-Prerelease-Playground';secret='gh.tkn';assert subprocess.run(['git','check-ignore','-q','--',secret],cwd=auth).returncode==0;assert subprocess.check_output(['git','ls-files','--',secret],cwd=auth)==b'';token=(auth/secret).read_text().strip();out['authentication']={'ignored':True,'untracked':True}
def get(path):
 req=urllib.request.Request('https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground'+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 with urllib.request.urlopen(req,timeout=40) as x:
  d=json.load(x);assert not isinstance(d,list) or 'rel="next"' not in x.headers.get('Link','');out.setdefault('provider_operations',[]).append({'method':'GET','path':path,'status':x.status});return d
out['remote_refs']={b:get('/git/ref/heads/'+b)['object']['sha'] for b in ('main','phase/1-named-file-utility','design-docs/main')};assert out['remote_refs']['main']==main and out['remote_refs']['phase/1-named-file-utility']==head
issues=get('/issues?state=all&per_page=100');milestones=get('/milestones?state=all&per_page=100');out['issues']=[]
obs=json.load(open(r/'037-a005-consumer-observations.json'));initial=next(e['objects'] for e in obs['events'] if 'issues?state=all' in e['endpoint'] and 'objects' in e)
for x in issues:
 original=next(v for v in initial if v['number']==x['number']);assert sha(x['body'].encode())==original['body_sha256'];assert [v['name'] for v in x['labels']]==original['labels'];assert x['state']==('closed' if 2<=x['number']<=5 else 'open')
 out['issues'].append({'number':x['number'],'id':x['id'],'state':x['state'],'closed_at':x['closed_at'],'body_sha256':sha(x['body'].encode()),'labels':[v['name'] for v in x['labels']]})
m=next(x for x in milestones if x['number']==1);assert m['state']=='closed';assert all(x['state']=='open' for x in milestones if x['number']!=1);initialm=next(e['objects'] for e in obs['events'] if 'milestones?' in e['endpoint'] and 'objects' in e)
for x in milestones:assert sha(x['description'].encode())==next(v for v in initialm if v['number']==x['number'])['description_sha256']
assert all(x['closed_at']<m['closed_at'] for x in issues if 2<=x['number']<=5)
out['milestone']={'number':1,'id':m['id'],'state':m['state'],'closed_at':m['closed_at'],'description_sha256':sha(m['description'].encode()),'task_closures_precede_milestone':True}
fixture=json.load(open(r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-003/1/SECOND-PRESERVATION-FIXTURE.json'));out['comments']=[]
for num in (2,3,4,5):
 comments=get('/issues/'+str(num)+'/comments?per_page=100')
 if num==2:assert sha(next(x for x in comments if x['id']==fixture['comment']['id'])['body'].encode())==fixture['comment']['body_sha256']
 commit='9dc8075' if num==2 else commits[num-3][:7]
 assert any(commit in x['body'] and ('T-%03d'%(num-1)) in x['body'] for x in comments)
 out['comments'] += [{'issue':num,'id':x['id'],'body_sha256':sha(x['body'].encode()),'has_commit_check_evidence':commit in x['body'] and ('test' in x['body'].lower() or 'check' in x['body'].lower())} for x in comments]
out['runtime']=sys.version;out['final_clean']=run(['git','status','--porcelain']).stdout==''
(r/'037-a005-independent-check-evidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'independent_checks':'passed','head':head,'provider_readback':True}))
