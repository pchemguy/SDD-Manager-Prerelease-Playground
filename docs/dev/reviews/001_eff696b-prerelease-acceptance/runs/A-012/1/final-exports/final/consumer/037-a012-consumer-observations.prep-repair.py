from pathlib import Path
import json,hashlib,shutil,re
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
first=Path(str(base)+'.first-preparation');assert not first.exists();first.mkdir()
manifest=Path(str(base)+'.preparation-identities.json')
entries=json.loads(manifest.read_text())
shutil.copyfile(manifest,first/'identities.json')
for name,item in entries.items():
 p=Path(name);assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
 target=first/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
p=Path('docs/dev/PLAN.md');p.write_text(p.read_text().replace('with alternate output, named-file ranges and byte-based stdin','with named-file ranges and byte-based stdin'))
p=Path('docs/dev/SPEC.md');p.write_text(p.read_text().replace('CLI text agree where delivered.','CLI text agrees with the whole-input API for whole input.'))
def digest(name):return hashlib.sha256(Path('docs/dev',name+'.md').read_bytes()).hexdigest()
for name,n,sources,summary in [('SPEC',5,['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC'],'R-001–R-008, R-011–R-013 and F-001–F-004 retain their complete text/count/BOM/range/error/resource/API/extraction obligations; R-009 is withdrawn and R-010 remains pending. No focused children.'),('PLAN',7,['SPEC','SPEC-REVIEW-REPORT','PROJECT','ARCHITECTURE','DECOMPOSITION','PLAN','layout'],'Phase 1 retains two cohesive delivery milestones; Phase 2 has three active delivery milestones 2.2/2.4/2.5. Historical 2.1 is retired, dedicated reviews 1.3/2.3/2.6 excluded. All retained contracts have routes; stdin/final work remains pending.'),('TASKS',4,['SPEC','SPEC-REVIEW-REPORT','PLAN','PLAN-REVIEW-REPORT','PROJECT','ARCHITECTURE','DECOMPOSITION','layout','TASKS'],'TASKS alone owns 24 stable task identities: 21 active checklist tasks, 16 checked, five unchecked T-013–T-017; retired historical T-010–T-012 have no current checkbox or new completion. Delivery counts 1.1=3,1.2=3,2.2=3,2.4=2,2.5=2; dedicated reviews excluded; small range groups remain cohesive. Affected current completion claims await runtime reassessment.')]:
 p=Path(f'docs/dev/{name}-REVIEW-REPORT.md');s=p.read_text();start=s.index('## Current gate');end=s.index('\n## Initial',start)
 old=s[start:end].replace('## Current gate','## Historical gate before JSON-removal correction',1)
 gate=f'''## Current gate\n\nState: **Ready for scoped JSON-removal preparation conformance**, Revision {n}; delegated candidate acceptance pending.\n\n{summary}\n\n| Current reviewed/governing source | SHA-256 |\n| --- | --- |\n'''+''.join(f'| `{x}.md` | `{digest(x)}` |\n' for x in sources)+'''\nOwner review and focused local-link/hierarchy/diff checks found no unresolved scoped preparation issue. The material JSON reduction invalidated older source identities; this gate and the latest revision apply to the corrected candidate. Ready does not conclude runtime verification, delegated acceptance, or full Phase 2 completion. Historical records and original findings below remain preserved.\n'''
 s=s[:start]+gate+'\n'+old+s[end:]
 a,b=s.rsplit(f'## Revision {n}',1)
 for x in ['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC','PLAN','layout','TASKS']:
  b=re.sub(r'(\| `'+x+r'\.md` \| `)[a-f0-9]+(` \|)',lambda m:m[1]+digest(x)+m[2],b)
 b+='\nDelegated review found stale Current gate hashes and obsolete alternate-output/agreement wording in this first candidate. Finding '+name+'-JSON-002: corrected the current gate to the actual reviewed source hashes and retirement counts; prior gate retained as historical above and exact first candidate preserved externally. Rechecked current source identities, dependencies, retained matrices, local links and pending task boundary. Resolved; no production consumption occurred before correction.\n'
 p.write_text(a+f'## Revision {n}'+b)
print('Preserved exact first eleven candidates before correction; updated three current gates and removed obsolete PLAN/SPEC claims.')
