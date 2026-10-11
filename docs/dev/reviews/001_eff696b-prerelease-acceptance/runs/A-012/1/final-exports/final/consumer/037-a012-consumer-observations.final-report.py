from pathlib import Path
import json,hashlib,re,subprocess
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations')
results=json.loads(Path(str(base)+'.hosted-results.json').read_text());assert len(results)==19
assert json.loads(Path(str(base)+'.foreign-preservation-after.json').read_text())['preserved']
report=Path('docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md')
s=report.read_text();start=s.index('Implementation/report candidate awaits');end=s.index('\n\nRaw actual commands',start)
s=s[:start]+"""The exact nineteen-artifact implementation/report candidate and corrected nineteen-operation hosted plan were accepted by delegated coordinator review `0cea6338b3ca4e33374c05437e577a2664922522`. The reviewer independently checked full code/tests/docs/QC/tasks/report, 31 unit / 28 integration tests, 241 extracted cases, four pinned captures and 33 additional retained-semantics probes. Accepted implementation `1dc6851aef7fdcc9581b00aaffc8c4661ff67d3f` was immediately pushed to `revision/003_795f3a3-remove-json` and exactly read back before hosted writes; committed bytes match the accepted manifest.

Hosted reconciliation completed all nineteen exact accepted operations with read-before-write and independent GET readbacks: fifteen bounded task titles/brief markers, one existing phase label rename and three managed milestone descriptions/titles. Historical closed/completed reasons, milestone associations and all five pending open task states remain unchanged. Retired JSON task bodies explicitly retain historical context; pending stdin briefs retain their actionable text/BOM/range scope. Unrelated issue #2 body/labels/comments and milestone #1 content compare exactly to their original reads.

The original generated hosted plan had incorrect unbounded task-title extraction and empty owning content; delegated review rejected it before any write. Its exact bytes remain preserved. Corrected bounded plan SHA-256 is `ad27d570ed50892b2e1d3926e3e64d58b8b8fce0d3edb5d50260b5756151dcdc`. After issue #15's successful PATCH, its first GET failed with proxy tunnel 403; execution stopped. Authorized same-endpoint GET-only recovery independently verified the exact accepted payload and preserved fields before continuing the remaining operations, without replaying that PATCH. Original transport failure and all successful operations/readbacks remain recorded.

This verified publication/hosted conclusion checkpoint awaits concrete delegated final report/QC review before its non-task checkpoint publication and explicit two-parent integration into the paused Phase 2 target. No stdin task, default integration, whole-phase completion or release is authorized."""+s[end:];report.write_text(s)
p=Path('docs/dev/TASKS.md');s=p.read_text();s=s.replace('Managed hosted\nbriefs and retirement metadata require reconciliation after verified publication;\noriginal historical completion reasons stay preserved.','Managed hosted\nbriefs and retirement metadata were reconciled after exact verified implementation\npublication, with nineteen accepted operations/readbacks; original historical\ncompletion reasons and five pending open tasks remain preserved.');p.write_text(s)
for owner in ['SPEC','PLAN','TASKS']:
 p=Path(f'docs/dev/{owner}-REVIEW-REPORT.md');s=p.read_text();a,b=s.split('## Historical gate before JSON-removal correction',1)
 a=a.replace('Ready for scoped JSON-removal preparation conformance','Verified scoped JSON-removal conformance')
 a=a.replace('implementation conclusion remains pending.','implementation accepted at coordinator `0cea6338b3ca4e33374c05437e577a2664922522`, published/exactly read back as `1dc6851aef7fdcc9581b00aaffc8c4661ff67d3f`; nineteen hosted operations/readbacks verified; final integration checkpoint review pending.')
 a=a.replace('Owner review and focused local-link/hierarchy/diff checks found no unresolved scoped preparation issue. The material JSON reduction invalidated older source identities; this gate and the latest revision apply to the corrected candidate. Ready does not conclude runtime verification, delegated acceptance, or full Phase 2 completion. Historical records and original findings below remain preserved.','Owner review and focused local-link/hierarchy/diff checks found no unresolved scoped issue. Actual 31 unit / 28 integration tests, 241 isolated extracted cases and ten runnable document fences verify retained completion claims. Hosted retirement and affected briefs are reconciled with preserved history and pending work. The current source identities below govern this accepted implementation checkpoint; final report/integration acceptance remains pending. Full Phase 2 remains incomplete. Historical records and original findings below remain preserved.')
 def current(m):
  f=Path('docs/dev')/m[1];assert f.exists();return '| `'+m[1]+'` | `'+hashlib.sha256(f.read_bytes()).hexdigest()+'` |'
 a=re.sub(r'\| `([^`]+\.md)` \| `[a-f0-9]{64}` \|',current,a)
 p.write_text(a+'## Historical gate before JSON-removal correction'+b)
files=['docs/dev/SPEC-REVIEW-REPORT.md','docs/dev/PLAN-REVIEW-REPORT.md','docs/dev/TASKS-REVIEW-REPORT.md','docs/dev/TASKS.md',str(report)]
manifest={f:{'sha256':hashlib.sha256(Path(f).read_bytes()).hexdigest(),'blob':subprocess.check_output(['git','hash-object',f],text=True).strip()} for f in files}
p=Path(str(base)+'.conclusion-identities.json');assert not p.exists();p.write_text(json.dumps(manifest,indent=2)+'\n')
for owner in ['SPEC','PLAN','TASKS']:
 s=Path(f'docs/dev/{owner}-REVIEW-REPORT.md').read_text().split('## Historical gate')[0]
 for f,h in re.findall(r'\| `([^`]+\.md)` \| `([a-f0-9]{64})` \|',s):assert hashlib.sha256((Path('docs/dev')/f).read_bytes()).hexdigest()==h,f
print('Exact five conclusion artifacts prepared; all20 current QC source hashes match; historical sections unchanged.')
