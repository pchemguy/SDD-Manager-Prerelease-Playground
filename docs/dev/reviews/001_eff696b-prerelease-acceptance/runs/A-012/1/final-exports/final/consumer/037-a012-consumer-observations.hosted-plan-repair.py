from pathlib import Path
import json,re,hashlib,shutil
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
old=Path(str(base)+'.hosted-plan.json');copy=Path(str(base)+'.first-hosted-plan.json');assert not copy.exists();shutil.copyfile(old,copy)
x=json.loads(Path(str(base)+'.hosted-before.json').read_text());s=Path('docs/dev/TASKS.md').read_text().split('## T-001 completion evidence')[0];ops=json.loads(old.read_text());summary=[]
for op in ops:
 if not op['endpoint'].startswith('issues/'):continue
 tid=op['task'];matches=[i for i in x['issues'] if i['title'].startswith('['+tid+'] ') and f'sdd-forge:task-id={tid} -->' in (i['body'] or '') and 'pull_request' not in i];assert len(matches)==1
 issue=matches[0]
 match=re.search(r'^        - (?:\[[x ]\] )?'+tid+r' — ([^\n]+)\n(.*?)(?=^        - |^    - |^## |\Z)',s,re.M|re.S);assert match,tid
 title,raw=match.groups();details='\n\n'.join(l.strip() for l in raw.splitlines() if l.strip())
 assert '\n' not in title and len(title)<160
 assert not re.search(r'^        - (?:\[[x ]\] )?T-',raw,re.M)
 assert '## Completion and persistence rules' not in details
 if tid not in ['T-010','T-011','T-012']:
  assert ('Outcome:' in details or 'Scope:' in details) and 'Depends on:' in details and 'Evidence:' in details,tid
 else:assert 'historical' in details.lower(),tid
 marker='sdd-forge:task-id='+tid
 context='Retired historical JSON delivery/review; no current executable work, ID reuse or new completion. Original published completion history is preserved.' if tid in ['T-010','T-011','T-012'] else 'Current text/count/BOM/range acceptance; T-013–T-017 remain pending and paused. Historical task results remain preserved; this amendment does not execute new main-list tasks.'
 managed=f'## Task brief <!-- {marker} -->\n\n**Context:** {context}\n\n'+details+'\n\n**Sources:** `docs/dev/TASKS.md`, `docs/dev/PLAN.md`, `docs/dev/SPEC.md`, `docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md`.\n<!-- /'+marker+' -->'
 pattern=r'## Task brief <!-- '+re.escape(marker)+r' -->.*?<!-- /'+re.escape(marker)+r' -->'
 assert len(re.findall(pattern,issue['body'],re.S))==1
 body=re.sub(pattern,lambda m:managed,issue['body'],flags=re.S)
 assert re.sub(pattern,'',body,flags=re.S)==re.sub(pattern,'',issue['body'],flags=re.S)
 op['payload']={'title':'['+tid+'] '+title,'body':body}
 summary.append({'task':tid,'endpoint':op['endpoint'],'title':op['payload']['title'],'bounded_task_block':raw.strip(),'body_sha256':hashlib.sha256(body.encode()).hexdigest()})
p=Path(str(base)+'.hosted-plan.corrected.json');assert not p.exists();p.write_text(json.dumps(ops,indent=2)+'\n')
p=Path(str(base)+'.hosted-blocks.corrected.json');assert not p.exists();p.write_text(json.dumps(summary,indent=2)+'\n')
print('Corrected bounded15 exact single-line task titles/nonempty retired-or-live blocks;19 planned managed operations; first invalid plan preserved unchanged.')
print('plan SHA256',hashlib.sha256(Path(str(base)+'.hosted-plan.corrected.json').read_bytes()).hexdigest())
print('blocks SHA256',hashlib.sha256(Path(str(base)+'.hosted-blocks.corrected.json').read_bytes()).hexdigest())
for row in summary:print(row['task'],row['title'],len(row['bounded_task_block']))
p=Path(str(base)+'.hosted-apply.py');p.write_text(p.read_text().replace("'.hosted-plan.json'","'.hosted-plan.corrected.json'"))
