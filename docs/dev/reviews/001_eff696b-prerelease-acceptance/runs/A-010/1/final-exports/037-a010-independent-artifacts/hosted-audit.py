from pathlib import Path
import json,hashlib
b=Path('/workspace/scratch/46b31bb4dff6');o=Path(__file__).parent;old=json.loads((b/'037-a009-hosted-readback.json').read_text());new=json.loads((b/'037-a010-final-hosted-readback.json').read_text());p=json.loads((b/'037-a010-provider-evidence.json').read_text());checks=[]
def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
issue={i['number']:i for i in new['issues']};mile={i['number']:i for i in new['milestones']};labels={i['name']:i for i in new['labels']}
for i in old['issues']:
 n=i['number'];fields=['number','id','title','state','state_reason','labels','milestone'];check('existing-issue-'+str(n),all(issue[n][k]==i[k] for k in fields),{'body_preserved':issue[n]['body_sha256']==i['body_sha256'],'body_update_authorized':n in [15,16,18]})
 if n not in [15,16,18]:check('existing-body-'+str(n),issue[n]['body_sha256']==i['body_sha256'])
for i in old['milestones']:
 n=i['number'];fields=['number','id','title','state'];check('existing-milestone-'+str(n),all(mile[n][k]==i[k] for k in fields) and mile[n]['body_sha256']==i['description_sha256'])
for i in old['labels']:
 x=labels[i['name']];check('existing-label-'+i['name'],x['name']==i['name'] and x['color']==i['color'] and x['description_sha256']==hashlib.sha256((i['description'] or '').encode()).hexdigest())
for tid,n in p['projection_verified']['tasks'].items():
 found=issue[n];expected_m=7 if tid<='T-020' else 8 if tid<='T-023' else 9
 check('range-issue-'+tid,found['title'].startswith('['+tid+'] ') and found['state']=='closed' and found['state_reason']=='completed' and found['milestone']==expected_m and found['labels']==['sdd-phase-2-JSON-and-stdin'])
for n in [7,8,9]:check('range-milestone-'+str(n),mile[n]['state']=='closed' and mile[n]['open_issues']==0)
for n in [5,6]:check('pending-milestone-'+str(n),mile[n]['state']=='open')
for row in [x for x in p['operations'] if x['operation']=='managed-source-link-reconciliation']:
 n=row['issue'];check('source-link-update-'+str(n),issue[n]['id']==row['id'] and issue[n]['body_sha256']==row['after_body_sha256'] and issue[n]['state']==row['state'] and issue[n]['state_reason']==row['state_reason'] and issue[n]['milestone']==row['milestone'] and [[z['id'],z['body_sha256']] for z in new['comments'].get(str(n),[])]==row['comments'] and row['exact_readback'])
for f in old['foreign_comment']:check('foreign-comment-'+str(f['id']),f in new['comments']['2'])
check('get-only-operations',all(x.get('method')=='GET' and x.get('status')==200 for x in new['operations']))
result={'metadata_checks':checks,'failed':[x for x in checks if not x['passed']],'inventory':{'issues':len(new['issues']),'milestones':len(new['milestones']),'labels':len(new['labels'])},'source':'Fresh GET-only metadata from coordinator; independent literal metadata comparison, no credentials/provider writes.','limit':'Bodies withheld; generated-section/outside-section fidelity supported by consumer recorded hashes and exact readbacks, not independently reconstructed raw bodies. Final snapshot cannot prove absence of transient unseen effects.'};(o/'hosted-audit.json').write_text(json.dumps(result,indent=2)+'\n');print({'checks':len(checks),'failed':result['failed']})
