# Phase 1 review — T-009

## Reviewed state and scope

Reviewed the complete named-file utility at starting commit `7b9f570aa4452d2ca9d6105479640528cb113f0e`, including T-001 through T-008, and the bounded runtime adjustment described below. Accepted preparation is integrated at `88a5c4b4424f4bba76940e40b1d6523b1f6fe191`. SPEC, PLAN, layout and adjacent QC retain their accepted semantic content; TASKS changes since preparation are completion/evidence annotations. The selected T-009 through T-010 range supersedes historical Phase-1-only stops.

The current fork explicitly disables hosted tracking. Historical issue/milestone identities in copied records are protected foreign objects; no hosted object write or closure is performed. Publication is restricted to the three explicitly authorized trial refs. The established local main target publishes only to `refs/heads/trial/037-a014-cross-main`, never the actual default remote branch.

## Implementation code review

Inspection covered every package module, all product tests, all three tools, README and public API guide, separately from test execution.

| Boundary | Assessment |
| --- | --- |
| Statistics/core/facade | Immutable nonnegative integer fields exclude bool. Three direct exports and whole-input signatures remain unchanged and silent. Shared traversal recognizes only CRLF/CR/LF, preserves segments and handles final/blank lines. Unicode words use split semantics. BOM normalization removes exactly one complete-input prefix. |
| Acquisition/lifetime | Complete binary read and strict UTF-8 decoding precede counting. Owned context-manager handles close for successful reads and decode/read errors; OSError subclasses and UnicodeDecodeError propagate silently. No input write or partial count path. |
| CLI/data flow | Argument validation precedes acquisition; abbreviation is disabled. Exactly one named file, option order, help and double-dash handling retain R-007/R-008. Controller translates only expected input/decode failures, identifies input/cause and emits completed exact text counts. Core/io do not depend on CLI. |
| Tests/distribution | Independent nonempty discovery, portable read/open/lifetime seams, real subprocess behavior and immutable/silent API checks cover Phase 1. Eleven literal source paths exclude credentials, caches, tests, development records and coordinator material. Extraction validates exact membership, sanitizes import paths, verifies imported location, invokes the extracted module and checks unchanged bytes. Sensitivity cases reject empty/failing suites and deliberately faulty extracted CLI. |
| Documentation/design seams | User documentation agrees with delivered signatures/counts/encoding/ownership/statuses and source-only distribution. Every runnable fence executes. Shared normalized counting and logical traversal remain suitable for separately requested range work; JSON/stdin/ranges are not yet delivered. |

No remaining Phase 1 bug, critical issue or contract violation was identified.

## Findings, corrections and retained failures

| ID | Observation | Correction / disposition |
| --- | --- | --- |
| P1-001 | Existing Python child command templates omitted explicit `-B`. Initial tests passed with inherited PYTHONDONTWRITEBYTECODE=1, but the current coordinator runtime instruction requires both that environment setting and explicit `-B`, including children. | With scoped coordinator runtime assistance, add only `"-B"` to existing child argv in four test modules and the distribution checker, retaining all existing flags. No behavior/governing change. Complete suites, archive and documentation reruns pass. |
| P1-002 | The consumer's first P1-001 edit incorrectly quoted the flag as bare `-B`, causing NameError: unit discovery ran 23 tests with 4 errors; integration discovery ran 18 tests with 31 errors. This is an edit defect, not a product-contract RED test. | Corrected to the string flag. Original raw failure retained in external command evidence; all affected checks rerun successfully. |

The milestone reports [1.1](1.1.md) and [1.2](1.2.md) have TODO None. M1.2-001 (long-option abbreviation) remains resolved and its regression is retained. No unresolved milestone finding is lost or deferred here.

## Actual checks and QC

Checks ran from the repository root on Python 3.12.14, with `python -B` and PYTHONDONTWRITEBYTECODE=1; final Python child argv also includes `-B`.

- `python -B tools/check_tests.py`: 23 unit and 18 integration tests pass independently, no skips. Covers semantic/BOM/Unicode matrix, direct API/signatures/silence, owned-handle/error seams, actual CLI success/help/failure/usage/dash-file processes and distribution sensitivity.
- `python -B tools/check_distribution.py`: isolated extracted import and 36 real module cases pass, with exact text/status/streams and unchanged sample bytes.
- Every runnable Bash/Python fence in README and public API guide executed with the same runtime flags. The README's runner plus separate unit/integration discovery commands each pass with 23/18 counts; builder/checker and independent extraction example pass. Demonstrations produce three lines/five words, BOM-only zero/zero versus one/one, and dash-file one/two. Temporary example ownership is checked before cleanup.
- User-guide and root-orientation local links resolve; current Markdown headings/lists/fences and changed diff whitespace pass. External URL refresh is not claimed.
- Bounded persistence audit inspected every T-001 through T-008 closing commit against its parent: exactly one leading owning ID, initial owning checkbox and substantive result/evidence together. No bundled or detached initial closure was found. Preparation-to-phase difference is solely product delivery and its evidence; pinned resources, publisher fixture and prior milestone report objects remain unchanged.

Current package module SHA-256 identities: cli `43e7e042edb7693ea2ba828726b691e2372feecb7954d7d05734c82a7b6319c1`; core `98b3374375eb7e6d4a301cabff99eb5e09ccccecbd9a808954e9c5cae084609f`; io `a45b0a1f320109f43d92e1b01507c2c2da941af51af09ede378724038db32b9f`; facade `b9b70e346fbf1cf4fe76e3b86d4ff626a5421c790e9d110c4508682357c00dc0`; module entry `b1829c14838dd795f5b054249a95ff42bc3550ac7e0446c91e0ea222b7cfa590`. Adjusted distribution checker SHA-256 is `4132a9a688ee8ce0a385c39b471ea9a29b4c6f4ba03c18e9f095cb10e9691d5f`. Concrete report/checklist/prospective tree identities are supplied for coordinator acceptance before commit/integration; this draft does not claim acceptance of itself.

## Exit assessment and integration boundary

Phase 1 R-001 through R-008 and applicable R-011/R-012/R-013 exits are verified. Milestones 1.1/1.2 and their review reports complete the delivery prerequisites; T-009 owns this final review and eligible milestone/phase parent status. Report, scoped runtime correction, evidence and initial T-009 checkbox close together only after concrete coordinator acceptance. Publish/read back that task commit before integration.

Then explicitly merge the pinned completed phase tip into local main using a two-parent boundary, verify merged-state product/distribution checks, and publish/read back only the authorized trial main destination. Those are prospective operations, not completed claims in this report. T-010 may start only after that verified published integration and authorized Phase 2 activation; no Phase 2 main integration is selected.

Coverage is local Python 3.12.14 on this environment. Other supported runtimes/platforms, external links, installed packaging, stdin/JSON/ranges and releases are outside this Phase 1 assessment. Shared filesystem access prevents certifying isolation. Reappearing untracked README sample files were observed after owned cleanup and are preserved pending ownership reconciliation; they are excluded from task staging and source archive.

## TODO

None. P1-001/P1-002 and milestone M1.2-001 are resolved. T-010 is the separately authorized next task after published Phase 1 integration; T-011 and later work remain unselected.
