from pathlib import Path
import json,re,hashlib,shutil,subprocess
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
manifest=json.loads(Path(str(base)+'.implementation-identities.json').read_text())
copy=Path(str(base)+'.first-implementation');assert not copy.exists();copy.mkdir()
for name,item in manifest.items():
 p=Path(name);assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
 q=copy/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
shutil.copyfile(Path(str(base)+'.implementation-identities.json'),copy/'identities.json')
for name in manifest:
 p=Path(name)
 if p.suffix!='.md':continue
 for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)',p.read_text()):
  if '://' not in target:assert (p.parent/target).exists(),(p,target)
s=Path('docs/dev/TASKS.md').read_text().split('## T-001 completion evidence')[0]
assert re.findall(r'^        - \[ \] (T-\d+)',s,re.M)==['T-013','T-014','T-015','T-016','T-017']
assert len(re.findall(r'^        - \[x\] T-',s,re.M))==16
assert len(set(re.findall(r'^        - (?:\[[x ]\] )?(T-\d+)',s,re.M)))==24
prior=subprocess.check_output(['git','show','795f3a3:docs/dev/TASKS.md'],text=True)
assert prior.split('## T-001 completion evidence',1)[1]==Path('docs/dev/TASKS.md').read_text().split('## T-001 completion evidence',1)[1].split('\n## JSON-removal amendment evidence',1)[0]
print('Exact19 implementation candidate preserved; scoped current links,24 stable identities/21active16checked5pending and byte-identical original task evidence passed.')
