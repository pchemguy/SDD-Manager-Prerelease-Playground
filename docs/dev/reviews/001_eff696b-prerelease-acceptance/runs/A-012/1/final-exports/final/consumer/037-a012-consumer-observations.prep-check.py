from pathlib import Path
import re,hashlib,json,subprocess
p=Path('docs/dev/PLAN.md');s=p.read_text().replace('phase 2 delivery milestones 2.1 and 2.2','phase 2 active delivery milestones 2.2, 2.4 and 2.5, with historical 2.1 retired').replace('(2.1, 2.2, 2.4 and 2.5)','(2.2, 2.4 and 2.5)').replace('then 2.1 relevant update and 2.2 final exits','then range documentation and 2.2 final exits');p.write_text(s)
p=Path('docs/dev/TASKS.md');s=p.read_text();a,b=s.split('## T-001 completion evidence',1);a=a.replace('named-file/no-range/JSON/usage','named-file/no-range/usage');p.write_text(a+'## T-001 completion evidence'+b)
for name,n in [('SPEC',5),('PLAN',7),('TASKS',4)]:
 p=Path(f'docs/dev/{name}-REVIEW-REPORT.md');s=p.read_text();a,b=s.rsplit(f'## Revision {n}',1)
 for x in ['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC','PLAN','layout','TASKS']:
  b=re.sub(r'(\| `'+x+r'\.md` \| `)[a-f0-9]+(` \|)',lambda m:m[1]+hashlib.sha256(Path('docs/dev',x+'.md').read_bytes()).hexdigest()+m[2],b)
 p.write_text(a+f'## Revision {n}'+b)
files=[Path('docs/dev',x+'.md') for x in ['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC','PLAN','layout','TASKS','SPEC-REVIEW-REPORT','PLAN-REVIEW-REPORT','TASKS-REVIEW-REPORT']]+[Path('docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md')]
manifest={str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'blob':subprocess.check_output(['git','hash-object',str(p)],text=True).strip()} for p in files}
for p in files:
 s=p.read_text()
 for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)',s):
  if '://' not in target: assert (p.parent/target).exists(),(p,target)
 for line in re.findall(r'^([ \t]*)- \[[x ]\] T-(\d+)',s,re.M):assert len(line[0])==8,line
s=Path('docs/dev/TASKS.md').read_text().split('## T-001 completion evidence')[0]
assert re.findall(r'^        - \[ \] (T-\d+)',s,re.M)==['T-013','T-014','T-015','T-016','T-017']
assert len(re.findall(r'^        - \[x\] T-',s,re.M))==16
Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.preparation-identities.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Scoped local links, task indentation, 16 active checked / five pending / three retired stable identities passed.')
print(json.dumps(manifest,indent=2))
