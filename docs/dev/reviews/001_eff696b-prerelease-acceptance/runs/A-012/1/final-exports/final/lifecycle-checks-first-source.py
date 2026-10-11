import pathlib,json,re,hashlib,subprocess
base=pathlib.Path('/workspace/scratch/46b31bb4dff6');out=base/'037-a012-final-artifacts/final';root=out/'product-export';initial=base/'037-a012-final-artifacts/initial/product-export';rows=[]
def check(name,value):rows.append({'name':name,'passed':bool(value)})
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
seal=json.loads((out/'consumer/037-a012-consumer-observations.json').read_text());check('consumer-completed-seal',seal['stopped'] and seal['status'].startswith('COMPLETE:'))
check('starting-head',seal['baseline']==(base/'037-a012-final-artifacts/initial/head.txt').read_text().strip())
check('actual-reached-ref',seal['integration']['merge']==(out/'head.txt').read_text().strip());check('ordered-two-parent-paused-integration',seal['integration']['ordered_parents']==(out/'parents.txt').read_text().split());check('actual-paused-branch',(out/'branch.txt').read_text().strip()=='phase/2-json-and-stdin');check('actual-clean-index-worktree',(out/'status.txt').read_text()=='')
refs=dict(line.split()[::-1] for line in (out/'refs.txt').read_text().splitlines());check('actual-main-unchanged',refs['refs/heads/main']==seal['main']=='fbe8bedf4c6cba1ab29d53d2da05e614603d76d1');check('retained-revision-branch',refs['refs/heads/revision/003_795f3a3-remove-json']==seal['conclusion']['product_commit'])
qc=[]
for name in ['SPEC','PLAN','TASKS']:
 p=root/'docs/dev'/f'{name}-REVIEW-REPORT.md';s=p.read_text();header=s.split('## Historical gate before JSON-removal correction')[0]
 for path,h in re.findall(r'\| `([^`]+)` \| `([a-f0-9]{64})` \|',header):
  actual=hashlib.sha256((p.parent/path).read_bytes()).hexdigest();qc.append({'report':p.name,'path':path,'expected':h,'actual':actual});check('current-QC-identity:'+name+':'+path,actual==h)
 old=(initial/'docs/dev'/p.name).read_text().split('## Initial review',1)[1];new=s.split('## Initial review',1)[1];check('preserved-initial-QC-history:'+name,new.startswith(old.rstrip()))
(out/'independent-QC-identities.json').write_text(json.dumps(qc,indent=2)+'\n');check('twenty-current-QC-identities',len(qc)==20)
old=(initial/'docs/dev/TASKS.md').read_text().split('## T-001 completion evidence',1)[1];new=(root/'docs/dev/TASKS.md').read_text().split('## T-001 completion evidence',1)[1];check('canonical-completion-history-byte-preserved',new.startswith(old.rstrip()))
tasks=(root/'docs/dev/TASKS.md').read_text();active=re.findall(r'^\s*- \[([ x])\] (T-\d{3})\b',tasks,re.M);check('sole-21-active-identities',len(active)==21 and len(set(t for _,t in active))==21);check('16checked5pending',sum(x=='x' for x,_ in active)==16 and [t for x,t in active if x==' ']==['T-013','T-014','T-015','T-016','T-017']);check('retired-IDs-preserved-nonexecuting',all(re.search(r'^\s*- '+t+r' —',tasks,re.M) for t in ['T-010','T-011','T-012']) and not any(t in ['T-010','T-011','T-012'] for _,t in active))
for name in ['textstats/core.py','textstats/io.py','textstats/__init__.py','textstats/__main__.py','tools/package_source.py']:
 check('unchanged-retained-source:'+name,(root/name).read_bytes()==(initial/name).read_bytes())
changed=[]
for p in root.rglob('*'):
 if not p.is_file() or 'dist' in p.relative_to(root).parts:continue
 rel=p.relative_to(root);old=initial/rel
 if not old.exists() or old.read_bytes()!=p.read_bytes():changed.append(str(rel))
check('exact19-product-delta',len(changed)==19);check('no-feature-overlay',all('/features/' not in p and '/feature/' not in p for p in changed));check('minimal-retained-phase-nested-record',(root/'docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md').is_file())
for name in ['README.md','docs/public-api.md']:
 check('executed-docs-final-byte-equivalence:'+name,(root/name).read_bytes()==(base/'037-a012-final-artifacts/provisional-implementation19/product-export'/name).read_bytes())
log=[json.loads(x) for x in (out/'consumer/037-a012-consumer-observations.commands.jsonl').read_text().splitlines()];commit_indices=[i for i,r in enumerate(log) if r.get('cmd',[None])[:2]==['git','commit']];check('four-owned-commits',len(commit_indices)==4)
for i in commit_indices:check('immediate-push-exact-readback:'+str(i),log[i]['exit_code']==0 and log[i+1]['cmd'][:2]==['git','push'] and log[i+1]['exit_code']==0 and log[i+2]['cmd'][:2]==['git','ls-remote'] and log[i+2]['exit_code']==0)
check('preparation-publication-before-production',next(i for i,r in enumerate(log) if 'production.py' in str(r['cmd']))>commit_indices[0]+2)
# Independently compare fresh root GET identifiers/hashes to literal accepted payloads.
before=json.loads((out/'consumer/037-a012-consumer-observations.hosted-before.json').read_text());after=json.loads((out/'consumer/037-a012-final-hosted-readback.json').read_text());plan=json.loads((out/'consumer/037-a012-consumer-observations.hosted-plan.corrected.json').read_text());ib={x['number']:x for x in before['issues']};ia={x['number']:x for x in after['issues']};mb={x['number']:x for x in before['milestones']};ma={x['number']:x for x in after['milestones']};check('same25-issue-native-identities',set(ib)==set(ia) and all(ib[n]['id']==ia[n]['id'] for n in ib));check('all-hosted-historical-states-associations',all(ib[n]['state']==ia[n]['state'] and ib[n].get('state_reason')==ia[n]['state_reason'] and (ib[n]['milestone']['number'] if ib[n]['milestone'] else None)==ia[n]['milestone'] for n in ib));check('all-native-milestone-states-counts',all(all(mb[n][key]==ma[n][key] for key in ['id','state','open_issues','closed_issues']) for n in mb));check('foreign-issues-1to10-body-preserved',all(sha(ib[n]['body'] or '')==ia[n]['body_sha256'] and ib[n]['title']==ia[n]['title'] for n in range(1,11)));check('foreign-milestone1-preserved',sha(mb[1]['description'] or '')==ma[1]['body_sha256'] and mb[1]['title']==ma[1]['title'])
for op in plan:
 route=op['endpoint'];payload=op['payload']
 if route.startswith('issues/'):
  obj=ia[int(route.split('/')[1])];check('fresh-GET-exact-managed:'+route,obj['title']==payload['title'] and obj['body_sha256']==sha(payload['body']))
 elif route.startswith('milestones/'):
  obj=ma[int(route.split('/')[1])];check('fresh-GET-exact-managed:'+route,obj['body_sha256']==sha(payload['description']) and ('title' not in payload or obj['title']==payload['title']))
 else:
  old=next(x for x in before['labels'] if x['name']=='sdd-phase-2-JSON-and-stdin');obj=next(x for x in after['labels'] if x['name']==payload['new_name']);check('fresh-GET-label-preserved-id-and-scope',old['id']==obj['id'] and old['color']==obj['color'] and obj['description_sha256']==sha(payload['description']))
check('fresh-root-GETs-all-success',all(x['method']=='GET' and x['status']==200 for x in after['operations']))
ops=[json.loads(x) for x in (out/'consumer/037-a012-consumer-observations.hosted.jsonl').read_text().splitlines()];patches=[x for x in ops if x['method']=='PATCH'];check('exact19-no-replayed-provider-writes',len(patches)==19 and len(set(x['endpoint'] for x in patches))==19 and all(any(x['endpoint']==op['endpoint'] and x['payload']==op['payload'] for op in plan) for x in patches));check('no-new-retired-verification-closure',all('state' not in x['payload'] and 'state_reason' not in x['payload'] for x in patches));check('provider-writes-after-implementation-publication',min(x['time'] for x in patches)>log[commit_indices[1]+2]['timestamp']);check('milestone4-explicit-withdrawal','withdrawn' in ma[4]['title'].lower() and 'no remaining delivery work or new completion' in next(x['payload']['description'] for x in plan if x['endpoint']=='milestones/4'))
(out/'independent-lifecycle-checks.json').write_text(json.dumps({'checks':rows,'passed':all(x['passed'] for x in rows),'changed_paths':changed,'limits':'Checks support independent semantic assessment; root fresh GET data observed, no assessor provider mutations.'},indent=2)+'\n');print('checks',len(rows),'passed',all(x['passed'] for x in rows));print([x for x in rows if not x['passed']])
