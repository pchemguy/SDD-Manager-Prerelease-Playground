from pathlib import Path
import hashlib,re,json
root=Path.cwd()
def change(name,fn):
 p=root/name;s=p.read_text();p.write_text(fn(s))
def modes(s):
 for a,b in [('text/JSON','text'),('JSON/stdin','stdin'),('stdin/text/JSON','stdin/text'),('range/BOM/JSON','range/BOM'),('BOM/JSON','BOM'),('whole-input/JSON','whole-input'),('CLI/JSON/','CLI/'),('default text and JSON','text'),('text and JSON','text'),('text or JSON','text'),('JSON/BOM','BOM'),('all text/BOM policies','both BOM policies')]:s=s.replace(a,b)
 return s
change('docs/dev/PROJECT.md',lambda s:modes(s.replace('| Phase 2, milestone 2.1 | `--json` emits one object plus newline, with integer `lines` and `words` fields only and identical counts. Text remains the default; JSON key order and spacing are unrestricted. |','| Phase 2, milestone 2.1 | Historical JSON increment withdrawn. Current output is exact text; `--json` is an unknown-option usage error before acquisition. A literal `--json` filename works after `--`. |')))
change('docs/dev/ARCHITECTURE.md',lambda s:modes(s.replace('select BOM/output policies','select BOM policy').replace('required text output or the later JSON object','required text output').replace('The CLI selects text output by default; JSON is a later output policy over the same statistics.','The CLI emits only the exact text output. Removed JSON options fail during parsing before acquisition.')))
change('docs/dev/DECOMPOSITION.md',lambda s:s.replace('BOM/output policy','BOM policy').replace('specified text string or later JSON object plus newline','specified text string plus newline').replace('Controller chooses format and emits result.','Controller emits the result.').replace('exact text output, JSON field/type constraints,','exact text output, removed-option rejection,'))
def spec(s):
 s=modes(s)
 s=re.sub(r'### R-009 JSON output\n\n.*?(?=\n### R-010)', '''### R-009 Withdrawn JSON output\n\nJSON output is withdrawn by the commanded checkpoint amendment; this stable ID is retained and never reused. `--json`, `--json=value` and abbreviated forms such as `--j` are unknown options: status 2, empty stdout, useful usage/error stderr and no traceback before input acquisition. After `--`, a literal `--json` filename remains valid for whole-input and range counting. R-007 exact text is the sole success format.\n''',s,flags=re.S)
 s=s.replace(' and `--json`','').replace('text counts are equal under R-007/R-009','text counts follow R-007').replace('with equal counts, status 0','with status 0').replace('CLI text and JSON agree where delivered.','CLI text agrees with the API for whole input.').replace('text/integer-only JSON','text').replace('R-007/R-008/R-009','R-007/R-008').replace('`--lines --json INPUT`','`--lines --keep-bom INPUT`')
 return s
change('docs/dev/SPEC.md',spec)
def plan(s):
 s=modes(s).replace('bounded JSON, named-file range and stdin increments','bounded named-file range and stdin increments').replace('JSON, stdin and range behavior are deferred.','Stdin and range behavior follow in Phase 2.').replace('Phase 2: JSON and stdin','Phase 2: Ranges and stdin')
 s=re.sub(r'### Milestone 2.1: JSON output\n\n.*?(?=\n### Milestone 2.2)', '''### Milestone 2.1: Withdrawn historical JSON increment\n\nStable milestone 2.1 and T-010–T-012 retain their historical identities and publication evidence; their JSON delivery scope is retired and allocates no remaining work. Current text/count/BOM/error/distribution behavior is protected by Phase 1 and range acceptance plus the steering amendment's verification. The withdrawal must reject removed options before acquisition and preserve literal option-like filenames after `--`. No empty new delivery milestone or replacement task is introduced.\n''',s,flags=re.S)
 s=s.replace('Depends on completed/reviewed 2.1.','Depends on completed Phase 1 and the reviewed text-only/range checkpoint.').replace('completed published JSON milestone 2.1 and compatible execution baseline','completed published Phase 1 and compatible text/range execution baseline').replace('| R-009 | 2.1 alternate named-file output, then composition with stdin in 2.2. |','| R-009 | Withdrawn; retained stable identity, no remaining delivery allocation. Removed-option rejection is R-008 regression acceptance. |').replace('repeated/extended for 2.1 JSON and 2.2 final stdin behavior','retained for range delivery and extended for 2.2 final stdin behavior')
 s=re.sub(r'Compatible execution requires accepted preparation merged.*?Phase 2\.', 'The named-file range checkpoint is already integrated into paused `phase/2-json-and-stdin`. JSON prerequisite delivery is withdrawn; Phase 1 and retained range review evidence establish the current compatible baseline. Preserve pending 2.2/2.3 and T-013–T-017; neither range review nor steering completes Phase 2.',s,flags=re.S)
 s=s.replace('four delivery milestones','three active delivery milestones').replace('four Phase 2 delivery milestones','three active Phase 2 delivery milestones').replace('four delivery milestones, with','three active delivery milestones, with')
 return s
change('docs/dev/PLAN.md',plan)
change('docs/dev/layout.md',lambda s:modes(s))
def tasks(s):
 current,history=s.split('## T-001 completion evidence',1)
 current=modes(current).replace('completed JSON evidence was incorporated through the compatible published merge.','historical JSON evidence remains preserved, while its delivery scope is withdrawn.').replace('Phase 2 — JSON and stdin','Phase 2 — Ranges and stdin')
 start=current.index('    - [x] Milestone 2.1')
 end=current.index('    - [ ] Milestone 2.2',start)
 current=current[:start]+'''    - Milestone 2.1 — Withdrawn historical JSON increment (no current delivery work)
        - T-010 — Retired JSON CLI delivery; historically completed, capability withdrawn.
            Original result and publication evidence below remain historical. No replacement task, current JSON acceptance or new completion is claimed.
        - T-011 — Retired JSON extraction delivery; historically completed, capability withdrawn.
            Original result and publication evidence below remain historical. Retained extraction acceptance belongs to T-007/T-022 and this amendment.
        - T-012 — Historical milestone 2.1 review; retained, no current executable work.
            Original review/publication remains historical; current retained contracts are reassessed by the steering report.
''' + current[end:]
 current=current.replace('T-012 and milestone 2.1 completion/closure','T-009 and the verified text-only/range amendment checkpoint').replace('through R-007/R-009 policies','through R-007 policy').replace("T-012's verified published milestone 2.1 completion/closure and the FEATURE-PLAN compatible baseline/projection prerequisites; existing pure core from T-001",'T-001 and completed Phase 1; accepted named-file range baseline/projection prerequisites').replace('T-018 and retained completed JSON T-010–T-012 checkpoint','T-018 and completed Phase 1 text/error checkpoint').replace('T-012, T-016','T-016').replace('milestones 2.1, 2.2, 2.4 and 2.5','milestones 2.2, 2.4 and 2.5')
 current=current.replace('boundary ends after concrete reconciliation/QC/archive acceptance and verified/\npublished explicit feature integration','boundary ends after concrete JSON-removal acceptance and verified/\npublished explicit steering integration').replace('No full\nPhase 2 merge into default or release follows this feature.','No full\nPhase 2 merge into default or release follows this amendment.')
 current=current.replace('Their verified status/evidence is transferred here unchanged.','Retained range acceptance is text/count/BOM/ranges; affected completion claims require amendment verification before conclusion. Historical results below are preserved unchanged.')
 return current+'## T-001 completion evidence'+history
change('docs/dev/TASKS.md',tasks)
report=Path('docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md');report.parent.mkdir(parents=True)
report.write_text('''# JSON-removal checkpoint amendment

## Objective and scope

Remove JSON output while retaining exact text, counting, BOM policy, complete strict decoding, resource ownership, unchanged API and named-file ranges. Removed options fail before acquisition; a literal `--json` filename works after `--`. Stdin/final T-013–T-017 remain paused; no default integration or release.

Campaign: 003_795f3a3-remove-json. Full baseline: `795f3a3542c9981f8d43c8e182876f3efa5b5f16`. Working branch: `revision/003_795f3a3-remove-json`; paused target: `phase/2-json-and-stdin`, origin `pchemguy/SDD-Manager-Prerelease-Playground`. Main remains `fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`. Pinned plugin: `ea515f5624c8a34cc4572731a2590223a5eb27f4`. Accepted external assessment: `037-a011-fresh-consumer-observations.json`.

## Preparation and affected ownership

PROJECT/design/SPEC/PLAN/layout/TASKS describe text-only current scope. R-009, milestone 2.1 and T-010–T-012 retain retired historical identities without replacement or new checked completion. Future stdin/final dependencies use the retained Phase 1/range checkpoint. T-018 pure semantics remain valid; T-019–T-024 retained text/range completion awaits current verification. Adjacent affected owner QC is appended, preserving original evidence. Closed feature and phase reports stay unchanged.

## Review and implementation status

Concrete preparation candidate awaits delegated coordinator review before production consumption. Implementation, verification, hosted reconciliation, publication and integration are not yet concluded.

## TODO

None outside the selected amendment. Pending stdin/final tasks remain outside its execution scope.
''')
# Current owner QC, preserve all original report evidence.
for name,n,owner,coverage in [('SPEC',5,'sdd-specify','R-001–R-008 retained; R-009 withdrawn; R-010 pending; R-011–R-013 and F-001–F-004 retain text/count/BOM/range, lifetime and extraction matrices.'),('PLAN',7,'sdd-plan','Phase 1: two delivery milestones (small cohesive useful path plus robustness/distribution); Phase 2: three active delivery milestones 2.2/2.4/2.5. Historical 2.1 is explicitly retired, not an empty delivery group. Dedicated reviews 1.3/2.3/2.6 excluded. Dependencies no longer require JSON.'),('TASKS',4,'sdd-tasks','Stable T-001–T-024 identities preserved: 21 active checklist tasks, 16 checked and five unchecked T-013–T-017; three retired historical identities have no current checkbox. Delivery counts: 1.1 three, 1.2 three, 2.2 three, 2.4 two, 2.5 two; exclude dedicated reviews. Two-task range groups retain cohesive pure-to-CLI and docs-to-extraction handoffs. No ID reuse, new completion, stdin execution or parent closure.')]:
 p=Path(f'docs/dev/{name}-REVIEW-REPORT.md');s=p.read_text();s=re.sub(r'State: .*',f'State: **Ready for scoped JSON-removal preparation conformance**, Revision {n}; delegated candidate acceptance pending.',s,count=1)
 sources=['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC','PLAN','layout','TASKS']
 identities='\n'.join(f'| `{x}.md` | `{hashlib.sha256(Path("docs/dev",x+".md").read_bytes()).hexdigest()}` |' for x in sources)
 s+=f'''\n## Revision {n}\n\nThe {owner} owner assessed the complete current {name} and affected upstream inputs under the commanded JSON reduction. Finding {name}-JSON-001: current JSON delivery/acceptance conflicted with the accepted removal. Steering corrected the affected clauses and rechecked retained contracts, stable IDs, dependencies, ownership and scoped count/conformance rules. Original findings/results remain preserved above.\n\n{coverage}\n\n| Current source | SHA-256 |\n| --- | --- |\n{identities}\n\nNo confirmed scoped preparation issue remains. Technical Ready applies to this amendment's inputs only; runtime completion and delegated review remain pending. Design/layout ownership and dependency directions suffice unchanged. Historical package/report contents are excluded from current validation.\n'''
 p.write_text(s)
manifest={str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [Path('docs/dev',x+'.md') for x in ['PROJECT','ARCHITECTURE','DECOMPOSITION','SPEC','PLAN','layout','TASKS','SPEC-REVIEW-REPORT','PLAN-REVIEW-REPORT','TASKS-REVIEW-REPORT']]+[report]}
Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.preparation-identities.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
