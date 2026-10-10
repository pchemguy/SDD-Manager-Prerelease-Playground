# Phase 2 — Named-file range feature extent review

T-024 reviews the named-file feature extent at published source
`4eeee9e9505b29b4a616292434561aab569dac7f`, after dedicated delivery reviews and
hosted closure of milestone 2.4/native #7 and 2.5/native #8. This report assesses
only added milestones 2.4–2.6, preserving the exact existing Phase 2 identity.
It does not assess completion of main stdin 2.2, final whole-phase review 2.3 or
pending T-013–T-017.

## Coherent implementation review

Read current main SPEC R/F contracts, accepted architecture/decomposition,
feature PLAN/task exits, both delivery reports and the collaborating current
implementation/documentation/test/distribution path. Rechecked the complete
feature delta against the compatible JSON baseline; product/test/public-guide
bytes are unchanged since the concretely accepted T-022 source, with T-023
adding only its reviewed report and owning task evidence.

| Interaction | Code review conclusion and supporting boundary |
| --- | --- |
| Validation to acquisition | CLI parsing rejects malformed/repeated/missing ranges before the shared file seam. Manual ASCII endpoint accumulation keeps arbitrarily large valid values valid; no global conversion guard is disabled. Huge endpoints remain comparisons over available logical lines. |
| Acquisition to normalization | Complete binary read/strict UTF-8 decode occurs under owned handle cleanup before any selection, including invalid bytes after END. No partial count or altered bytes; API retains original exceptions/silence. |
| Normalization to selection/count | Exactly one leading complete-input BOM is removed by policy before numbering. Preserved shared CRLF/CR/LF segments feed pure selection and normalized counting without stripping an exposed interior BOM. Unicode separators remain content; Unicode whitespace words and blank/final/EOF semantics are shared. |
| API and rendering compatibility | TextStats remains immutable and validated; exactly three public exports and keyword-only whole-input APIs retain contracts. No-range CLI remains whole-input; JSON has only integer lines/words equal to default text counts, newline and empty success stderr. Error statuses/output remain stable under flags. |
| Future source composition | Selection accepts normalized text and validated endpoints, with no filesystem/stdin/process dependency. Future complete borrowed-stdin acquisition can feed the same normalize/select/count path. Literal minus remains a named file now; actual stdin acquisition/ownership/locale exits require T-013–T-017 and are not claimed delivered. |
| Documentation and extraction | Full guide/help contracts match delivered source. Eleven-file allowlist and exact import provenance prevent checkout/foreign substitution; real extracted range/error/JSON cases and range-specific mutants protect the highest-risk interactions. Current docs explicitly defer stdin and preserve public API/resource contracts. |

No bug, critical quality issue or SPEC/PLAN violation was found. No final code or
document repair was needed. Code review is distinct from the actual checks below.
Existing component seams suffice; no design/layout change or new public boundary
is required.

## Actual feature-wide verification and usefulness

Fresh repository-root `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py`
passed independently discovered 31 unit/28 integration tests, both OK/process 0,
no skips/warnings, on Python 3.12.14. This covers complete pure/CLI range matrices,
controlled validation-before-open and read/decode cleanup, whole-input/API/JSON/
error regressions, unchanged bytes, huge/leading-zero endpoints and extraction
mutations. Fresh root extraction and API checks are recorded separately below.

Fresh execution of 27 selected runnable README/public-guide commands in a current
temporary checkout copy passed all named-file/setup/help/BOM/JSON/range/API/error
and Bash extraction examples, with an actual temporary source build. Documented
check fences are supported by the fresh root full runner/current extraction and
by T-023's complete 32-command all-fence execution of identical product/docs bytes;
they were not redundantly rerun inside this shorter demonstration. Logs distinguish
those scopes. The demonstrations select useful middle/EOF subsets (2/3), blank
segments (1/0), mixed available range (3/3), exposed interior BOM (1/1) and empty
beyond-EOF (0/0), retaining bytes and clear statuses/streams. No direct human
continue/amend decision or unrequested steering is inferred.

Fresh root `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_distribution.py`
passed 315 actual extracted module cases and the silent unchanged API/export/
keyword-only-signature probe. Actual import location belongs to the temporary
extraction. Every sample preserves bytes; inherited import paths are removed,
user-site and bytecode disabled. Fresh rebuilt ZIP has exactly eleven approved
members and each source/doc byte matches current published product; protected/
foreign material is excluded.

Actual evidence: ordinary logs `037-a010-T024-full.log`,
`037-a010-T024-examples.log`, `037-a010-T024-extraction.log`; previous complete
milestone examples and genuine task RED/GREEN remain retained. Selected local
links/whitespace and actual-parent task persistence audit are included at the
final checkpoint. Runtime/platform breadth and performance are unverified; no
streaming, installed entry point, stdin delivery or release claim is made.

## Milestone findings and TODO aggregation

| Provenance | Findings / disposition |
| --- | --- |
| [2.4 implementation review](2.4.md) | No unresolved bug, critical issue or contract violation; TODO None. Detailed docs/extraction were explicit next-milestone obligations and are now delivered/reviewed in 2.5. Historical 99-case extraction count remains truthful to that checkpoint. |
| [2.5 documentation/distribution review](2.5.md) | No unresolved product defect or eligible deferred item; TODO None. Both range-specific mutation RED runs and subsequent GREEN are preserved. |
| Feature extent | No additional blocker or admissible code deferral. Pending main stdin/final work is outside this feature, with accepted dependencies retained; it is not a waived feature defect. |
| EVID-A010-001, T-021 verification provenance | Earlier redirected runner returned 0 with incomplete log; incidental ps exited 1. Fresh complete captured 31/26 check and subsequent 31/28 checks resolve verification uncertainty. Original ambiguous evidence is retained, not counted as proof; no product repair. |
| EVID-A010-002, T-023 hosted closure helper | Original native8 helper exited 1 before mutation because it required literal heading `## TODO` instead of accepted `## Findings and TODO disposition`/`TODO: None`. Pinned reports require the empty TODO value, not that heading. Helper-only assertion corrected; full associated-issue validation, closure and exact readback then passed. Accepted product report bytes unchanged. Diagnostic rg on a guessed nonexistent forge reference returned 2; actual report rules were read. |

TODO: None. No unresolved required check, bug, critical issue or contract
violation is deferred. Resolved evidence/tool interventions retain provenance and
chosen resolution; no follow-up code owner or alternative is needed for an empty
deferred set. Main pending work keeps its existing owners/tasks.

## Extent conclusion and next boundary

All F-001–F-004 and affected delivered R-001–R-009/R-011–R-013 exits are
technically satisfied for named-file text/JSON ranges. R-010 acquisition is
explicitly pending; only source-independent compatibility is established.
Concrete delegated review of this and the package IMPLEMENTATION-REPORT is
pending. Once accepted, T-024 result/reports/current evidence/initial checkbox and
eligible feature 2.6/extent parents close together, immediately publish/read back,
close/read back issue #25, validate all associated issues and close/read back
native #9. Feature completion cannot check the main Phase 2 parent.

Then explicitly reconcile sole main TASKS ownership/evidence, current QC and
eligible archive/navigation, obtain concrete changed-artifact review, publish and
verify, and explicitly merge/publish the accepted reconciled feature into paused
`phase/2-json-and-stdin`. Whole Phase 2/default integration/release remain outside
this boundary. Neither later archive nor integration is claimed complete here.
