import hashlib,json
from pathlib import Path
r=Path('/workspace/scratch/46b31bb4dff6');old=json.loads((r/'037-a010-final-hosted-readback.json').read_text());new=json.loads((r/'037-a012-final-hosted-readback.json').read_text());plan=json.loads((r/'037-a012-consumer-observations.hosted-plan.corrected.json').read_text())
oi={x['number']:x for x in old['issues']};ni={x['number']:x for x in new['issues']};om={x['number']:x for x in old['milestones']};nm={x['number']:x for x in new['milestones']}
checks={'same_issue_identities':set(oi)==set(ni) and all(oi[n]['id']==ni[n]['id'] for n in oi),'unaffected_issues_1_to_10':all(oi[n]==ni[n] for n in range(1,11)), 'comments_unchanged':old['comments']==new['comments'],'foreign_milestone1_unchanged':om[1]==nm[1],'all_historical_states_and_associations':all(all(oi[n][k]==ni[n][k] for k in ['id','state','state_reason','milestone']) for n in oi),'all_milestone_states_and_counts':all(all(om[n][k]==nm[n][k] for k in ['id','state','open_issues','closed_issues']) for n in om),'all_GET_success':all(x['status']==200 and x['method']=='GET' for x in new['operations'])}
for op in plan:
 route=op['endpoint'];payload=op['payload']
 if route.startswith('issues/'):
  number=int(route.split('/')[1]);checks[route+'_exact_title_body']=ni[number]['title']==payload['title'] and ni[number]['body_sha256']==hashlib.sha256(payload['body'].encode()).hexdigest()
 elif route.startswith('milestones/'):
  number=int(route.split('/')[1]);checks[route+'_exact_scope']=nm[number]['body_sha256']==hashlib.sha256(payload['description'].encode()).hexdigest() and ('title' not in payload or nm[number]['title']==payload['title'])
ol={x['id']:x for x in old['labels']};nl={x['id']:x for x in new['labels']};labelid=next(k for k,v in ol.items() if v['name']=='sdd-phase-2-JSON-and-stdin')
checks['phase_label_identity_and_scope']=set(ol)==set(nl) and nl[labelid]['name']=='sdd-phase-2-Ranges-and-stdin' and nl[labelid]['color']==ol[labelid]['color']
checks['unaffected_labels']=all(ol[k]==nl[k] for k in ol if k!=labelid)
checks['all_issue_label_sets']=all(sorted('sdd-phase-2-Ranges-and-stdin' if x=='sdd-phase-2-JSON-and-stdin' else x for x in oi[n]['labels'])==ni[n]['labels'] for n in oi)
assert all(checks.values()),[k for k,v in checks.items() if not v]
result={'status':'Checks passed','class':'Root independently fetched current hosted state after consumer19 exact managed operations','checks':checks,'limits':'Safe hashes, identifiers and states; full write chronology independently assessed separately. No token/response bodies emitted.'}
(r/'037-a012-root-hosted-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'root hosted checks passed')
