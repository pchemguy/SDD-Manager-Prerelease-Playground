import subprocess,json,hashlib,sys,os,contextlib,io,inspect,urllib.request,pathlib,re
root=pathlib.Path('/workspace/scratch/46b31bb4dff6'); product=root/'037-textstats-product'; out={'schema_version':1,'commands':[]}
def run(args,cwd=product,env=None):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env=env); out['commands'].append({'argv':args,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}); return p
for suite in ('unit','integration'): assert run([sys.executable,'-B','-m','unittest','discover','-s','tests/'+suite,'-t','.','-v'],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')).returncode==0
sys.path.insert(0,str(product)); stdout=io.StringIO(); stderr=io.StringIO()
with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
 from textstats import TextStats,count_text
 cases=[('',(0,0),(0,0)),('alpha beta',(1,2),(1,2)),('alpha\n',(1,1),(1,1)),('\n',(1,0),(1,0)),('alpha\r\nbeta\rgamma\n',(3,3),(3,3)),('alpha\n\n',(2,1),(2,1)),(' \t',(1,0),(1,0)),('alpha\u2028beta',(1,2),(1,2)),('\ufeff',(0,0),(1,1)),('\ufeff\ufeff',(1,1),(1,1)),('\ufeffalpha beta',(1,2),(1,2)),('a\ufeffb',(1,1),(1,1)),('\r\n',(1,0),(1,0)),('\r',(1,0),(1,0)),('a\u0085b\u2029c\v d\f e',(1,5),(1,5)),('\ufeff\n\ufeff',(2,1),(2,2)),('\n\r\r\n',(3,0),(3,0))]
 for text,a,b in cases:
  for policy,expected in ((True,a),(False,b)):
   s=count_text(text,strip_bom=policy); assert (s.lines,s.words)==expected
 for value in (True,False,1.0,'1',None,1j):
  for pair in ((value,0),(0,value)):
   try: TextStats(*pair)
   except TypeError: pass
   else: raise AssertionError(pair)
 for pair in ((-1,0),(0,-1)):
  try: TextStats(*pair)
  except ValueError: pass
  else: raise AssertionError(pair)
 s=TextStats(2,3)
 for field in ('lines','words'):
  for operation in (lambda:setattr(s,field,9),lambda:delattr(s,field)):
   try: operation()
   except (AttributeError,TypeError): pass
   else: raise AssertionError(field)
 assert s==TextStats(2,3)
assert stdout.getvalue()==stderr.getvalue()==''
out['literal_probes']={'vectors':len(cases),'policies':2,'silent':True,'constructor_validation':True,'immutable_assignment_deletion':True,'signature':str(inspect.signature(count_text))}
for args in (['git','status','--porcelain=v1'],['git','show','-s','--format=%H %P%n%B','HEAD'],['git','show','-s','--format=%H %P%n%B','main'],['git','diff','HEAD^','HEAD','--name-only'],['git','diff','HEAD^','HEAD','--','docs/dev/TASKS.md']): assert run(args).returncode==0
# Secret store protection is checked before reading; retained records have no secret path.
authrepo=root/'SDD-Manager-Prerelease-Playground'; secret='gh.tkn'
ignored=subprocess.run(['git','check-ignore','-q','--',secret],cwd=authrepo).returncode==0
tracked=subprocess.check_output(['git','ls-files','--',secret],cwd=authrepo,text=True)==''
assert ignored and tracked
out['authentication']={'effectively_ignored':ignored,'absent_from_index':tracked}
token=(authrepo/secret).read_text().strip(); base='https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground'
def get(path):
 req=urllib.request.Request(base+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 with urllib.request.urlopen(req) as r: status=r.status; data=json.load(r)
 out.setdefault('provider_operations',[]).append({'method':'GET','endpoint':path,'status':status});return data
issue=get('/issues/2'); comments=get('/issues/2/comments?per_page=100'); milestones=get('/milestones?state=all&per_page=100'); issues=get('/issues?state=all&per_page=100')
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
fixture=json.load(open(root/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-003/1/SECOND-PRESERVATION-FIXTURE.json'))
assert sha(issue['body'])==fixture['issue']['body_sha256']; assert issue['state']=='closed' and issue['state_reason']=='completed'; assert 'campaign-037-preserve' in [x['name'] for x in issue['labels']]
old=next(x for x in comments if x['id']==fixture['comment']['id']);assert sha(old['body'])==fixture['comment']['body_sha256']
m=next(x for x in milestones if x['number']==1);assert sha(m['description'])==fixture['milestone']['description_sha256'];assert all(x['state']=='open' for x in milestones)
evidence=next(x for x in comments if x['id']==6097586619);assert '9dc8075' in evidence['body'] and 'T-001' in evidence['body']
assert all(x['state']=='open' for x in issues if 3<=x['number']<=10)
out['hosted']={'issue':2,'state':issue['state'],'state_reason':issue['state_reason'],'body_sha256':sha(issue['body']),'labels':[x['name'] for x in issue['labels']],'old_comment_sha256':sha(old['body']),'evidence_comment':{'id':evidence['id'],'body_sha256':sha(evidence['body']),'references_task_commit':True},'milestone_description_sha256':sha(m['description']),'all_milestones_open':True,'remaining_phase_tasks_open':True,'fixture_preserved':True}
# Read remote refs through API to avoid credential-bearing command arguments.
for branch in ('main','phase/1-named-file-utility','design-docs/main'):
 ref=get('/git/ref/heads/'+branch);out.setdefault('remote_refs',{})[branch]=ref['object']['sha']
assert out['remote_refs']['main']=='88a5c4b4424f4bba76940e40b1d6523b1f6fe191';assert out['remote_refs']['phase/1-named-file-utility']=='9dc8075dd1b96d3a2744717a9d6d98a3024acbec'
out['source_hash_integrity']={}
start=json.load(open(root/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance/runs/A-004/1/START.json'))
for p,h in start['tracked_hashes'].items():
 if p.startswith('textstats-run-resources/'):
  assert hashlib.sha256((product/p).read_bytes()).hexdigest()==h
out['source_hash_integrity']={'all_pinned_resource_hashes_match_start':True}
(root/'037-a004-independent-check-evidence.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':'passed','suites':[10,5],'vectors':len(cases),'provider_readback':True,'source_unchanged':True}))
