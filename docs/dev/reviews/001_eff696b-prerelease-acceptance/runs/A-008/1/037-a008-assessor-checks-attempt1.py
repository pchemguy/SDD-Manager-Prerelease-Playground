import pathlib,json,subprocess,os,sys,re,hashlib,urllib.request
r=pathlib.Path('/workspace/scratch/46b31bb4dff6');p=r/'037-textstats-product';b=r/'037-test-evidence/docs/dev/reviews/001_eff696b-prerelease-acceptance';a=b/'resources/acceptance/textstats'
sys.path.insert(0,str(a/'scripts'));import core
sha=lambda v:hashlib.sha256(v).hexdigest()
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_ASKPASS=str(r/'playground-askpass.sh'),GIT_TERMINAL_PROMPT='0')
out={'schema_version':1,'commands':[],'checks':{},'runtime':sys.version,'provider_operations':[]}
def run(args,cwd=p):
 x=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True);v={'argv':args,'cwd':str(cwd),'returncode':x.returncode,'stdout':x.stdout,'stderr':x.stderr};core.no_secret(v);out['commands'].append(v);assert x.returncode==0;return x.stdout
obs=json.loads((r/'037-a008-consumer-observations.json').read_text());core.no_secret(obs);assert sha((r/'037-a008-consumer-observations.json').read_bytes())=='9ce26cec008d769a663e0c5a71cb5259eeb975fcf80a577b1c2f678857864279'
head=run(['git','rev-parse','HEAD']).strip();branch=run(['git','branch','--show-current']).strip();assert head=='8036adbd71ffc1f04b98e689cc131781bc20cd1f';assert branch=='design-docs/002_e7cae5b-named-file-ranges'
assert run(['git','status','--porcelain=v1'])=='';out['index']=run(['git','ls-files','--stage']);out['refs']=run(['git','show-ref']);out['parents']=run(['git','show','-s','--format=%P',head]).strip().split()
main=run(['git','rev-parse','main']).strip();phase=run(['git','rev-parse','phase/2-json-and-stdin']).strip();assert main=='e7cae5b2216ff7dd311b6f7296d829d1927a6a8a' and phase=='e63b8946bbb99347b0f73f070f9c728945ee5925';run(['git','merge-base','--is-ancestor',main,head]);assert 'refs/heads/feature/002_' not in out['refs'];run(['git','diff','--check',main,head])
paths=run(['git','diff','--name-only',main,head]).splitlines();expected=['AGENTS.md']+['docs/dev/FEATURE-'+x+'.md' for x in ['PLAN-REVIEW-REPORT','PLAN','SPEC-REVIEW-REPORT','SPEC','TASKS-REVIEW-REPORT','TASKS']]+['docs/dev/features/002_e7cae5b-named-file-ranges/README.md'];assert sorted(paths)==sorted(expected);out['checks']['bounded_delta']=paths
out['artifacts']={f:{'sha256':sha((p/f).read_bytes()),'blob':run(['git','rev-parse',head+':'+f]).strip()} for f in paths}
for f in paths:core.no_secret((p/f).read_text())
commits=run(['git','rev-list','--reverse',main+'..'+head]).split();assert commits==[v['sha'] for v in obs['commits']];out['commits']=[]
for c in commits:out['commits'].append({'sha':c,'subject':run(['git','show','-s','--format=%s',c]).strip(),'paths':run(['git','diff-tree','--no-commit-id','--name-only','-r',c]).splitlines()})
# First derivation bytes still exact at final tip.
for c,f in [('b0f93cf170addc80a92541acc4151058e57b6e64','SPEC'),('91d8a5a124004a7ca5b9c5217f4d5d99d825aade','PLAN'),('493d5e2d2251922041c235b1c8377f3fdf827bce','TASKS')]:
 for name in [f,f+'-REVIEW-REPORT']:
  z='docs/dev/FEATURE-'+name+'.md';assert run(['git','rev-parse',c+':'+z]).strip()==out['artifacts'][z]['blob']
text=(p/'docs/dev/FEATURE-TASKS.md').read_text();ids=re.findall(r'^        - \[ \] (T-\d+)',text,re.M);assert ids==['T-%03d'%i for i in range(18,25)];assert '- [x]' not in text
mainids=re.findall(r'- \[[ x]\] (T-\d+)',(p/'docs/dev/TASKS.md').read_text());assert len(mainids)==17 and not set(ids)&set(mainids);out['checks']['unique_unchecked_ownership']={'feature':ids,'main':mainids,'delivery_counts':{'2.4':2,'2.5':2},'excluded_reviews':['T-020','T-023','T-024']}
for x in ['T-020','T-023','T-024']:assert x in text
out['checks']['unchanged_default_and_paused_phase']=True
start=json.loads((b/'runs/A-008/1/START.json').read_text());out['pinned_preservation']={}
for f,v in start['tracked_file_sha256'].items():
 if f.startswith('textstats-run-resources/'):
  h=v if isinstance(v,str) else v['sha256'];assert sha((p/f).read_bytes())==h;out['pinned_preservation'][f]=h
# Read-only provider inspection, credential protection established before memory load.
auth=r/'SDD-Manager-Prerelease-Playground';assert subprocess.run(['git','check-ignore','-q','--','gh.tkn'],cwd=auth).returncode==0;assert subprocess.check_output(['git','ls-files','--','gh.tkn'],cwd=auth)==b'';value=(auth/'gh.tkn').read_text().strip();out['authentication']={'effective_ignore':True,'untracked':True,'transient_memory_only':True}
def get(path):
 req=urllib.request.Request('https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground'+path,headers={'Authorization':'Bearer '+value,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 with urllib.request.urlopen(req,timeout=40) as x:
  obj=json.load(x);assert 'rel="next"' not in x.headers.get('Link','');out['provider_operations'].append({'method':'GET','path':path,'status':x.status});return obj
out['remote_refs']={name:get('/git/ref/heads/'+name)['object']['sha'] for name in [branch,'main','phase/2-json-and-stdin']};assert out['remote_refs']=={branch:head,'main':main,'phase/2-json-and-stdin':phase}
old=json.loads((r/'037-a007-independent-check-evidence.json').read_text())
issues=get('/issues?state=all&per_page=100');milestones=get('/milestones?state=all&per_page=100');labels=get('/labels?per_page=100')
out['issues']=[{'number':x['number'],'id':x['id'],'title':x['title'],'state':x['state'],'state_reason':x['state_reason'],'created_at':x['created_at'],'closed_at':x['closed_at'],'body_sha256':sha((x['body'] or '').encode()),'labels':[v['name'] for v in x['labels']],'milestone':x['milestone']['number'] if x['milestone'] else None} for x in issues]
out['milestones']=[{'number':x['number'],'id':x['id'],'title':x['title'],'state':x['state'],'created_at':x['created_at'],'closed_at':x['closed_at'],'description_sha256':sha((x['description'] or '').encode())} for x in milestones]
out['labels']=[{'name':v['name'],'color':v['color'],'description':v['description']} for v in labels]
for key in ['issues','milestones','labels']:assert sorted(out[key],key=lambda x:json.dumps(x,sort_keys=True))==sorted(old[key],key=lambda x:json.dumps(x,sort_keys=True)),key
comments=get('/issues/2/comments?per_page=100');out['foreign_comment']=[{'id':x['id'],'body_sha256':sha(x['body'].encode())} for x in comments if x['id']==6097383663];assert out['foreign_comment']
fixture=json.loads((b/'runs/A-003/1/SECOND-PRESERVATION-FIXTURE.json').read_text());assert out['foreign_comment'][0]['body_sha256']==fixture['comment']['body_sha256'];out['checks']['provider_no_projection_or_foreign_change']=True
out['checkpoint_refs']={'product_branch':branch,'product_commit':head,'integration_branch':'main','integration_commit':main,'paused_phase_branch':'phase/2-json-and-stdin','paused_phase_commit':phase}
inputs=json.loads((b/'runs/A-008/1/INPUTS.json').read_text());state=json.loads((b/'runs/A-008/1/RUN-STATE.json').read_text());state['checkpoint_refs']=out['checkpoint_refs'];det,code=core.assessment(inputs,state,a/'cases/assessor/A-008.json',None);core.no_secret(det);assert code==0
(r/'037-a008-deterministic-assessment.json').write_text(json.dumps(det,indent=2)+'\n')
assert run(['git','status','--porcelain=v1'])=='';core.no_secret(out);out['result']='Checks passed';(r/'037-a008-independent-check-evidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':out['result'],'head':head,'deterministic':det['status'],'files':len(paths),'issues':len(issues),'milestones':len(milestones)}))
