from pathlib import Path
import hashlib,re,subprocess,json
n=0
for owner in ['SPEC','PLAN','TASKS']:
 p=f'docs/dev/{owner}-REVIEW-REPORT.md';s=Path(p).read_text();old=subprocess.check_output(['git','show','1dc6851:'+p],text=True);assert s.split('## Historical gate',1)[1]==old.split('## Historical gate',1)[1]
 for f,h in re.findall(r'\| `([^`]+\.md)` \| `([a-f0-9]{64})` \|',s.split('## Historical gate')[0]):assert hashlib.sha256((Path('docs/dev')/f).read_bytes()).hexdigest()==h,f;n+=1
assert n==20
s=Path('docs/dev/TASKS.md').read_text();old=subprocess.check_output(['git','show','795f3a3:docs/dev/TASKS.md'],text=True)
start=s.index('## T-001 completion evidence');end=s.index('## JSON-removal amendment evidence');assert s[start:end].rstrip()==old[old.index('## T-001 completion evidence'):].rstrip()
active=re.findall(r'^\s*- \[([ xX])\].*?T-(\d{3})',s,re.M);assert len(active)==21,active;assert sum(v.lower()=='x' for v,_ in active)==16;assert [tid for v,tid in active if v==' ']==['013','014','015','016','017']
manifest=json.loads(Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.conclusion-identities.json').read_text())
for f,i in manifest.items():assert hashlib.sha256(Path(f).read_bytes()).hexdigest()==i['sha256'];assert subprocess.check_output(['git','hash-object',f],text=True).strip()==i['blob']
assert subprocess.run(['git','diff','--check']).returncode==0
print('Five exact conclusion identities,20 current hashes,21active/16checked/5pending and original historical QC/task evidence pass.')
