from pathlib import Path
import json,re
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
x=json.loads(Path(str(base)+'.hosted-before.json').read_text());s=Path('docs/dev/TASKS.md').read_text().split('## T-001 completion evidence')[0];ops=[]
for n in range(10,25):
 tid=f'T-{n:03}'
 matches=[i for i in x['issues'] if i['title'].startswith('['+tid+'] ') and f'sdd-forge:task-id={tid} -->' in (i['body'] or '') and 'pull_request' not in i]
 assert len(matches)==1,(tid,matches)
 issue=matches[0];match=re.search(r'^        - (?:\[[x ]\] )?'+tid+r' — (.*)\n(.*?)(?=^        - |^    - |^## |\Z)',s,re.M|re.S);assert match,tid
 title,details=match.groups();details='\n\n'.join(l.strip() for l in details.splitlines() if l.strip())
 marker=f'sdd-forge:task-id={tid}'
 managed=f'## Task brief <!-- {marker} -->\n\n**Context:** Accepted JSON withdrawal; preserve exact text/count/BOM/ranges and five pending stdin/final tasks. Historical original delivery and issue completion remain historical; no new completion is claimed.\n\n'+details+'\n\n**Sources:** `docs/dev/TASKS.md`, `docs/dev/PLAN.md`, `docs/dev/SPEC.md`, `docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md`.\n<!-- /'+marker+' -->'
 pattern=r'## Task brief <!-- '+re.escape(marker)+r' -->.*?<!-- /'+re.escape(marker)+r' -->'
 assert len(re.findall(pattern,issue['body'],re.S))==1
 body=re.sub(pattern,lambda m:managed,issue['body'],flags=re.S)
 ops.append(dict(endpoint=f'issues/{issue["number"]}',method='PATCH',payload={'title':'['+tid+'] '+title,'body':body},task=tid,preserved_state=issue['state'],preserved_state_reason=issue['state_reason'],preserved_milestone=issue['milestone']['number']))
old='sdd-phase-2-JSON-and-stdin';assert sum(l['name']==old for l in x['labels'])==1
ops.append(dict(endpoint='labels/'+old,method='PATCH',payload={'new_name':'sdd-phase-2-Ranges-and-stdin','description':'Named-file ranges and pending strict UTF-8 stdin; exact text output.'}))
for m in x['milestones']:
 if m['number']==1:continue
 desc=m['description'] or '';new=desc.replace('text/JSON','text').replace('format/BOM','text/BOM').replace('JSON','text')
 payload={}
 if m['number']==4:payload={'title':'sdd-2.1-Withdrawn-historical-JSON-increment','description':'Historical completed JSON delivery/review is withdrawn by accepted steering 003_795f3a3-remove-json. Stable 2.1/T-010–T-012 identities and original completion history retained; no remaining delivery work or new completion. Exact text/count/BOM/range contracts are verified in the steering report.'}
 elif new!=desc:payload={'description':new}
 if payload:ops.append(dict(endpoint=f'milestones/{m["number"]}',method='PATCH',payload=payload,preserved_state=m['state']))
p=Path(str(base)+'.hosted-plan.json');assert not p.exists();p.write_text(json.dumps(ops,indent=2)+'\n')
print('Prepared',len(ops),'managed-field operations; no issue or milestone state changes; no issue2/milestone1 writes; unrelated outside-marker material/labels/comments preserved.')
