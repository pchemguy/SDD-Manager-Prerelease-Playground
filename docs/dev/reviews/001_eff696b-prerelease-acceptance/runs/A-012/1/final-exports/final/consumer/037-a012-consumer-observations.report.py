from pathlib import Path
import re,hashlib,json,subprocess
p=Path('docs/dev/TASKS.md');s=p.read_text().replace('affected completion claims require amendment verification before conclusion.','affected retained completion claims are reassessed by current amendment verification; concrete conclusion acceptance remains pending.')
s+='''\n## JSON-removal amendment evidence\n\n[Steering report](reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md)\nrecords the accepted reduction, source, current checks and remaining boundary.\nR-009 and completed historical T-010–T-012/2.1 delivery scope are withdrawn; no\nID is reused or newly completed. Historical results/reports remain unchanged.\nRetained T-006/T-007 and T-018–T-024 text/count/BOM/range, API, documentation,\nresource/error and extraction acceptance passes current verification: 31 unit/\n28 integration tests and 241 real isolated extracted-module cases on Python\n3.12.14, plus ten runnable document fences with inspected exact count/error/API\noutputs. Controlled complete-decode-after-END/read-failure/owned-close coverage\nis converted to text. Core/I/O/API/entry/builder interfaces are unchanged.\n\nT-013–T-017, milestones 2.2/2.3 and whole Phase 2 remain unchecked and paused.\nTheir retained text/BOM/range stdin composition stays required. Managed hosted\nbriefs and retirement metadata require reconciliation after verified publication;\noriginal historical completion reasons stay preserved. This is steering evidence,\nnot a new task result or initial checkbox closure.\n''';p.write_text(s)
# Refresh affected current source identities without rewriting original review history.
def digest(name):return hashlib.sha256(Path('docs/dev',name).read_bytes()).hexdigest()
for name,n in [('SPEC',5),('PLAN',7),('TASKS',4)]:
 p=Path(f'docs/dev/{name}-REVIEW-REPORT.md');s=p.read_text();gate,rest=s.split('## Historical gate',1)
 for file,h in re.findall(r'\| `([^`]+)` \| `([a-f0-9]{64})`',gate):gate=gate.replace(h,digest(file))
 gate=gate.replace('delegated candidate acceptance pending.','preparation accepted at coordinator `3b7e7abef970ca6132aa4fe34f075d550f0ab0ba`; implementation conclusion remains pending.')
 gate=gate.replace('Affected current completion claims await runtime reassessment.','Retained affected completion acceptance passes current runtime/docs/extraction checks; implementation conclusion remains pending.')
 s=gate+'## Historical gate'+rest
 a,b=s.rsplit(f'## Revision {n}',1)
 # The preparation table is explicitly historical evidence after runtime status updates.
 b=b.replace('| Current source | SHA-256 |','| Preparation source at this review | SHA-256 |')
 if name=='TASKS':
  b+='''\nRuntime/status recheck: current TASKS root records 31 unit/28 integration tests, 241 isolated module cases and ten verified document fences. T-006/T-007 and T-018–T-024 retain verified text/count/BOM/range/docs/extraction acceptance; original JSON delivery claims remain retired. Only completion/evidence wording changes after accepted preparation: retained contracts, task structure, dependencies and the five pending checkboxes are equivalent to that reviewed preparation. Current root identity is recorded in the Current gate. Historical initial results remain unchanged.\n'''
 p.write_text(a+f'## Revision {n}'+b)
p=Path('docs/dev/reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md');s=p.read_text();s=s.replace('T-019–T-024 retained text/range completion awaits current verification.','T-019–T-024 retained text/range completion passes the current checks below, without replaying task execution.')
a=s.index('## Review and implementation status');b=s.index('## TODO',a)
s=s[:a]+'''## Review and implemented result

First candidate acceptance was withheld for stale current QC hashes and obsolete alternate-output/agreement wording. Exact first eleven artifact bytes were preserved externally; the correction retains historical gate prose separately. Corrected preparation was accepted through coordinator `3b7e7abef970ca6132aa4fe34f075d550f0ab0ba`, committed as campaign opening `636b46d8daf1455c940c98f4d535c9936c0f1733`, immediately pushed to the authorized revision branch and exactly read back before production consumption.

Production removes only the JSON import, option registration and serialization branch from `textstats/cli.py`, retaining the shared exact text renderer. The parser still validates before acquisition; core/I/O/API/entry/builder interfaces are unchanged. README/public guide/help and maintained root orientation agree with the reduced scope. Existing JSON callers receive a breaking usage error; there is no alias or alternate JSON path.

Separate coherent code review inspected parser/controller, complete acquisition and decode, pure normalize/select/count boundaries, public facade, resource/error translation, mixed tests, documentation and isolated distribution checker against retained contracts. No unresolved code/contract blocker was found. Mixed JSON tests preserve complete-decode/read-failure/owned-close evidence in text. Range matrices retain both spellings, both BOM policies, all retained option permutations/INPUT placements, huge/leading-zero endpoints, EOF/blank/mixed/Unicode/exposed-BOM and byte-preservation anchors. Extraction retains allowlist/import provenance and the silent unchanged API/signature probe. Checker mutations reject broken text, ignored ranges, second BOM normalization and silently accepted removed options.

## Actual verification

All commands use `PYTHONDONTWRITEBYTECODE=1 python -B` from the product root, with inherited child bytecode suppression, on Python 3.12.14.

| Check | Observed result |
| --- | --- |
| Two focused removal tests before production | Initial run: two assertion failures and three mock-serialization errors. Corrected realistic doubles, then same two tests: five intended behavioral failures, no errors. JSON remained accepted/acquired input. |
| `python -B -m unittest tests.unit.test_cli tests.integration.test_cli -v` | 28 tests pass after removal. |
| `python -B tools/check_tests.py` | Independent nonempty 31 unit / 28 integration tests pass, no skips/warnings. |
| `python -B -m unittest tests.integration.test_cli.RangeModuleTests -v` | Five tests pass after removing empty-list refactor remnants. |
| `python -B tools/package_source.py` and `python -B tools/check_distribution.py` | Allowlisted archive builds; 241 real isolated extracted module cases pass, plus silent API/signature probe. |
| All README/public guide runnable fences in temporary checkout | Ten fences execute; exact count/help/error/test/extraction/API outputs inspected. Invalid range examples intentionally produce four usage diagnostics and final strict-decode status 1; no unexpected failure. |
| Scoped current documents/links/task structure/hashes and full delta | Twenty current QC source hashes match before execution; whitespace/local links/16 checked active/five pending/three retired identities pass; protected resources, closed packages, core/I/O/API/entry/builder/bootstrap paths unchanged. |

Retained T-006/T-007 and T-018–T-024 acceptance is verified at this amended checkpoint; original historical reports/results remain preserved. T-010–T-012/2.1 are retired historical work, with no newly verified JSON completion. All five pending stdin/final tasks and whole Phase 2 remain paused. Broader supported runtimes/platforms are unverified; no performance/streaming/release claim is made.

## Publication, hosted disposition and integration boundary

Implementation/report candidate awaits concrete delegated conclusion review before its verified non-task commit/publication and eligible explicit two-parent paused-phase integration. Hosted read-only discovery resolved every exact stable task marker and parent association. A concrete managed-field reconciliation plan covers retired JSON and affected live briefs, phase-label/milestone scope; it preserves historical closed/completed reasons and pending open tasks. No issue is reopened solely because JSON was removed and no task is closed solely because its checkbox was retired. Writes/readbacks follow implementation publication. Unrelated issue2 body/label/comments and milestone1 content remain protected.

Raw actual commands, separate stdout/stderr/status, first candidate bytes, acceptance provenance, original failures and hosted original operations/readbacks are retained in the externally required `037-a012-consumer-observations` seal and sidecars. Initial orientation tool captures predate the separate-stream runner and some were truncated; they are not represented as complete raw separate-channel captures. One wrong manifest key and one shell quote parse failure were corrected and remain original failures. No `/pyenv` or coordinator resource change occurs.

'''+s[b:];p.write_text(s)
paths=subprocess.check_output(['git','diff','--name-only','795f3a3542c9981f8d43c8e182876f3efa5b5f16'],text=True).splitlines()
manifest={str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'blob':subprocess.check_output(['git','hash-object',str(p)],text=True).strip()} for p in map(Path,paths)}
out=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations.implementation-identities.json');assert not out.exists();out.write_text(json.dumps(manifest,indent=2)+'\n');print('Verified implementation/report candidate:',len(manifest),'paths; exact hash/blob manifest saved.')
