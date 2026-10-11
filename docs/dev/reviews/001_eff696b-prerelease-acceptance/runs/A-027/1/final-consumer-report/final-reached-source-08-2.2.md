# Milestone 2.2 review — UTF-8 stdin and final delivery

## Identity and reviewed state

Owning review task: T-016. At this candidate checkpoint, applicable milestone exits are verified;
delegated report acceptance, owning persistence and hosted closure are pending.
This report does not complete Phase 2 or integrate into main.

Reviewed `phase/2-json-and-stdin` at published/exactly read back
`ca24007134141265a1937c77e2fda504bb0d6129`, after issue #16 was observed
closed/completed with its evidence comment and preserved native fields.
Delivery commits are T-013 `2d96774221165ac04096c8d57ddcefe85b2305e0`,
T-014 `dbf50d7b6d83c7ddf53f287d82b199db3e83fd89` and T-015
`ca24007134141265a1937c77e2fda504bb0d6129`.
[Current SPEC](../../../SPEC.md), [PLAN](../../../PLAN.md) milestone 2.2 and
[canonical TASKS](../../../TASKS.md) govern. Startup acceptance
`fb98e7b984134755845fc46390381d9933aa397e` authorizes this resumed range.
The accepted text-only amendment retains R-009 as withdrawn; retired JSON
identities are historical and were not replayed.

## Delivered capability

The module CLI reads token `-` from borrowed binary stdin through EOF and
strictly decodes UTF-8 independently of the text locale. It applies whole-input
BOM policy once, optional shared logical-line selection, then normalized counting.
Text output, named-file behavior, usage/input status categories and silent
whole-input public signatures remain stable. A token `-` after `--` still means
stdin; `./-` selects an actual named file. Empty input counts zero/zero.
Invalid bytes after a selected END still fail without partial counts.

Public instructions explain source ownership, decoding, composition, output and
failure behavior. The source ZIP contains the unchanged eleven-file allowlist and
runs the real module for named-file and byte-fed stdin whole-input/range cases
from isolated extraction. No new dependency, installed entry point, streaming
promise, version or release was introduced.

## Implementation code review

Source inspection was performed separately from test execution across all five
package modules, the runner/builder/checker, all three unit files, all three
integration files and the current README/public reference. The complete path,
not only the final diff, was reviewed against R-001–R-008/R-010–R-013 and retained
F-001–F-004 composition.

| Reviewed boundary | Inspection assessment |
| --- | --- |
| `textstats/io.py` byte acquisition | No locale text wrapper or newline translation. Named-file context management closes owned handles on all paths; borrowed reader reads complete bytes, strictly decodes, does not normalize and does not close. Expected failures produce no partial text. |
| `textstats/core.py` semantics | Pure immutable values and Unicode whitespace counting remain unchanged. CRLF/CR/LF traversal preserves selected segments and final/blank/EOF semantics. Whole-input normalization removes at most one leading BOM; selection/counting do not remove an exposed interior BOM. |
| `textstats/cli.py` parsing/control | Complete parse/validation precedes source access. Exact options, repetition, ASCII positivity/order and manual unbounded decimal conversion retain conversion-guard behavior. Named-file no-range API route is preserved; stdin/range use the same normalized pipeline. Only expected OSError/UnicodeDecodeError are translated; identifying stderr/status 1 and success rendering occur at the correct boundaries. |
| Facade/module adapter | Direct exports, keyword-only BOM policy, silent API exception contracts and process status adapter remain unchanged; stdin adds no public API. |
| Test runner and tests | Actual independent nonempty discovery, failure propagation and workflow exclusion are tested. Controlled borrowed/owned streams establish portable read/ownership behavior; real byte-fed processes independently cover CLI status/streams and differing locales. Literal expected counts and archive mutations avoid using checkout counters as extraction acceptance. |
| Builder and extraction checker | Explicit regular-file allowlist excludes development, fixtures, resources and credentials. Extraction cwd, sanitized inherited import paths, disabled user site and exact imported location prevent checkout substitution. Real byte-fed module invocations cover both BOM policies, all range anchors/options/endpoints, errors and API compatibility. |
| Public documentation | Delivered stdin and retained API/named-file/range behavior agree with inspected code. Complete-input memory use and verified-runtime limits are explicit; no deferred stdin wording remains in public instructions. |

No remaining bug, critical issue, contract violation or required evidence blocker
was located. No additional production repair was required by this review.

## Findings and dispositions

| Stable finding | Evidence, impact and disposition |
| --- | --- |
| M2.2-001 — extraction acceptance gap, resolved | Before T-015, `tools/check_distribution.py` accepted an extracted CLI with stdin disabled: the new sensitivity test failed while 241 named-file cases passed. This blocked final R-013 stdin acceptance, not named-file behavior. T-015 added actual byte-fed isolated cases and the same regression now rejects the faulty archive. Resolution: `ca24007134141265a1937c77e2fda504bb0d6129`; fresh T-016 sensitivity recheck passed. |
| M2.2-002 — explicit child flag gap, resolved | Two retained invocation fixtures in `tests/integration/test_api.py` and `tests/unit/test_cli.py` inherited bytecode suppression but omitted required explicit `-B`; fifteen prior captured argv gaps remain historical. Scoped T-015 maintenance adds only that flag, preserving assertions. The corrected final campaign recorded 2,776 actual Python children, all with `-B` and `PYTHONDONTWRITEBYTECODE=1`. Earlier runs do not support this explicit-flag claim. |

External evidence facility incidents remain visible in
[T-015 evidence](../../../TASKS.md#t-015-completion-evidence): raced old JSON writes,
captured logging/indentation failures, unknown lost first-channel entries and a
first successful documentation campaign whose owned fixtures were later observed
still present. No historical content or removal is reconstructed. Logger locking
with atomic replacement and fresh exclusive immutable child records, verified
fixture bytes before explicit cleanup, guarded retries and independently absent
final fixtures establish the corrected campaign. These incidents are evidence
limitations, not product bugs or deferred code TODOs. The later guessed plural
plugin-reference read failed without mutation; the actual linked
`boundary-review.md` was then read. That navigation failure changes no product
acceptance result.

## Tests and evidence

Environment: repository-root cwd, Python 3.12.14, standard library,
`PYTHONDONTWRITEBYTECODE=1`; every corrected Python invocation uses `-B`.
External runner/trace wrappers preserve actual argv/cwd, separate stdout/stderr,
statuses, byte inputs and fixture/source/archive hashes. The external prefix is
`/workspace/scratch/46b31bb4dff6/037-a013-consumer-`.

Fresh T-016 command, executed through the external runner:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B /workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py python -B /workspace/scratch/46b31bb4dff6/037-a013-consumer-trace-immutable.py -m unittest tests.unit.test_io.BorrowedAcquisitionTests tests.unit.test_cli.StdinCliTests tests.integration.test_cli.StdinModuleTests tests.integration.test_distribution.DistributionTests.test_checker_rejects_ignored_stdin_with_healthy_named_file_behavior -v
```

Observed status 0: 12 tests, no skips/warnings. This freshly checks borrowed EOF/
success/read/decode ownership, parsing before borrowed access, real source/locale/
BOM/range/error composition, dash-file distinction and faulty extraction rejection.

Prior T-015 final corrected evidence is reused explicitly: reviewed source/test/
public-document bytes are identical to the published T-015 state, and this review
changes none of them. Its serialized `037-a013-consumer-docs-retry.py` campaign
returned 0 and executed all twelve README/API fences. The actual product commands
were run through `037-a013-consumer-trace-immutable.py`: `tools/check_tests.py`,
separate `-m unittest discover -s tests/unit -t . -v` and
`-m unittest discover -s tests/integration -t . -v`, plus
`tools/check_distribution.py`. They passed 37 unit/34 integration tests and 478
isolated actual module cases, with no suite skips/warnings. Silent API/signature
checks, exact named-file bytes and removed-option errors remain covered.
The archive matched all eleven current allowlisted file bytes, with SHA-256
`4fcf4a60d08f4a8c2a69a0b2d567de70c5a554e2249eb0f101f18c5340b7349c`.
Public-guide local links resolved and staged whitespace/current QC hashes passed.

## Usability and portability demonstration

Executed README byte-stream examples visibly produced counts 3/5, 1/1, 2/3,
1/1 and 0/0 with status 0/empty stderr; malformed complete UTF-8 after END
produced status 1, empty stdout and an identifying stdin diagnostic. The actual
isolated extracted example produced named-file 3/5 and stdin-range 2/3.
Integration/extraction fed non-ASCII bytes under C and C.UTF-8 with Python UTF-8
mode and locale coercion disabled, establishing source decoding independence
for those exercised environments. Controlled read failures support portable
ownership/diagnostic evidence without relying on platform permission tricks.

## Exit assessment and limits

R-010 complete byte/strict UTF-8/EOF/empty/read/decode/borrowed ownership exits pass.
R-011 final delivered public docs and actual runnable examples pass. R-012
independently nonempty unit/integration discovery and retained regressions pass.
R-013 isolated real named-file/stdin module entry and final source/docs archive
pass. F-001–F-004 named-file behavior and stdin composition remain verified.

Python 3.11+ is the supported declaration; only Python 3.12.14 and the current
Unix environment were exercised. Other supported runtimes/platforms are
unverified, not an established defect or invented deferral. Complete in-memory
acquisition remains the accepted design; no performance/bounded-memory claim is
made. The unknown original observation loss remains unknown despite trustworthy
fresh acceptance.

## TODO

TODO: None.

## Next boundary

After concrete delegated acceptance, commit this T-016 report/result/current
evidence with its initial owning checkbox and eligible milestone 2.2 parent.
Immediately push/read back before further work; reconcile issue #17 with native
fields preserved, enumerate all milestone #5 associations, and only then close/
read back that native milestone. T-017 waits for the applicable closed delivery/
feature review milestones, performs separate cross-phase review and final checks,
and supplies the required Phase 2/final implementation report pair. Main remains
unchanged until completed-phase integration has its concrete delegated review.
Stop after published completed Phase 2; no next phase or release.
