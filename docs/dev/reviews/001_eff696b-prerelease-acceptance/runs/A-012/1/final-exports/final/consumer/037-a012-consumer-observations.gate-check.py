from pathlib import Path
import re,hashlib
n=0
for root in ['SPEC','PLAN','TASKS']:
 s=Path('docs/dev',root+'-REVIEW-REPORT.md').read_text().split('## Historical gate')[0]
 for name,h in re.findall(r'\| `([^`]+)` \| `([a-f0-9]{64})`',s):
  assert hashlib.sha256(Path('docs/dev',name).read_bytes()).hexdigest()==h,(root,name)
  n+=1
print('All',n,'current QC root/upstream hashes match actual sources.')
