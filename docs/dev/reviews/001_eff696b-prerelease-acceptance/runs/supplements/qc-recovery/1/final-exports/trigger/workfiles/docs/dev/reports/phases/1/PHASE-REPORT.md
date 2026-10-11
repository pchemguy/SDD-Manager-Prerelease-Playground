# Phase 1 review — Named-file utility

## Identity and outcome

Owning task: T-009; Phase 1 milestone 1.3. Source reviewed on `phase/1-named-file-utility` at `7b9f570aa4452d2ca9d6105479640528cb113f0e`. Starting integration baseline is accepted-preparation main `88a5c4b4424f4bba76940e40b1d6523b1f6fe191`. The complete-phase request authorizes T-005 through T-009, full-phase integration/publication and then stopping before Phase 2. Maintained Phase 1 tracking is active. Native delivery milestones #1 (1.1) and #2 (1.2) and constituent issues #2–#9 were confirmed closed before this phase review. T-009 maps uniquely to #10, review milestone #3.

Phase 1 delivers an immutable silent whole-text/named-file API and useful real module CLI, with strict UTF-8, shared logical-line/word/BOM semantics, input preservation, robust expected failures, public documentation and isolated extracted-source distribution. Milestone reports [1.1](1.1.md) and [1.2](1.2.md) establish their respective reviews/exits. M1.2-001 is resolved; neither milestone carries a deferred TODO.

## Independent phase code review

Reviewed complete core, acquisition, public facade, parser/controller/rendering/module entry, product-test runner, packaging/extraction tools, product suites and README/public guide. Compared their cross-component behavior against SPEC R-001 through R-008/R-011 through R-013 and PLAN Phase 1 exits, separately from check execution.

| Interaction / exit | Code review conclusion and verification |
| --- | --- |
| Text/file/CLI equivalence | File and CLI reuse whole-text counting; binary strict decoding preserves terminators, one complete-input BOM is removed at the counting boundary. Semantic matrix/API/file and actual CLI checks establish equivalence without separate algorithms. |
| Value/API boundary | Three direct exports and keyword-only policy; immutable validated fields, equality and silent imports/calls covered. No stdin/range parameter or new public export. |
| Failure/resource boundary | Complete acquisition/decode precedes result/rendering. Owned context closes on all paths. APIs retain OSError subclasses/UnicodeDecodeError; CLI translates only those expected errors with identifying cause/input, empty failure stdout and no traceback. Usage validation precedes acquisition; unsupported abbreviations now rejected. |
| Usability and source distribution | User docs align with signatures/status/count/ownership contracts. Builder's literal allowlist supplies modules/docs/notices/tools and excludes credentials/caches/development/coordinator/tests. Checker validates extraction import provenance with sanitized environment and actually invokes module entry. Corrupted-extraction sensitivity prevents false success from the healthy checkout. |
| Test collection and retained delivery | Independently discovered nonempty unit/integration suites exercise observable contracts; workflow fixtures excluded. Count runner rejects either empty suite and propagates failures. Normal options/help/dash-file behavior retained across robustness/distribution delivery. |
| Extension seams and boundary | Normalized counting and preserved logical traversal remain internal collaborators. JSON, byte stdin and range remain unimplemented and unprojected; Phase 2 depends on separately authorized activation after this integration. |

No new bug, critical issue, SPEC/PLAN violation or missing required phase evidence was identified. No additional production repair was needed for T-009.

## Actual verification

Fresh checks from repository root against the published T-008 state on Python 3.12.14:

- `python tools/check_tests.py`: 23 unit and 18 integration tests passed, no skips/warnings, independently nonempty.
- `python tools/check_distribution.py`: exact extracted import confirmed; 36 real module cases passed with expected statuses/stdout/stderr and unchanged bytes. Fourteen semantic inputs under both BOM policies, dash-file, missing/bad-byte failure, four usage cases including unknown abbreviation, and help were exercised.
- Executed every runnable Bash/Python fence in README/public guide verbatim: setup/sample/API assertions/BOM/dash/help, runner and explicit unittest discover, source build/check and separate extracted sample. All commands succeeded, sample output was exact three lines/five words, BOM-only policies produced zero/zero versus one/one and dash-file one/two. Temporary inputs cleaned.
- Local user-guide links resolved and changed diff whitespace passed. Source-scope inspection confirms coordinator resources, pinned plugin, existing publisher fixture and unrelated material unchanged.
- Bounded task audit of each T-001 through T-008 parent diff confirmed exact single owning task subjects, task result/evidence and one initial executable checkbox together. T-004/T-008 close only their own review tasks with eligible parent status. T-009 receives the same composition before integration; no aggregate or split closing result is permitted.

Prior behavioral RED evidence is preserved in TASKS: T-005 four errors/four failures from twelve focused tests; T-007 three errors/one failure from four tests against valid unimplemented declarations; T-008 two abbreviation regressions. Documentation/review-only scope does not fabricate additional RED history.

## Findings, TODO and limits

Resolved finding: M1.2-001, parser accepted unsupported `--keep`, repaired/tested in T-008 at `7b9f570aa4452d2ca9d6105479640528cb113f0e`, with original RED and current extracted regression. No deferred milestone finding or new phase finding remains.

TODO: None.

Evidence covers local Python 3.12.14 in this environment, not a full supported-version/platform matrix, unrestricted real permission failures beyond controlled seams, external notice-link availability, installed packaging, JSON/stdin/ranges or release publication. The source archive is generated/ignored; reproducible builder source is tracked. This phase result does not claim completion of the entire two-phase project; no final IMPLEMENTATION-REPORT is produced before the full task list completes.

## Completion and integration boundary

Full Phase 1 acceptance/exits are verified. Report, evidence, initial T-009 checkbox and eligible milestone 1.3/Phase 1 parent status close together; publish and read back before issue #10 closure and native review milestone #3 closure/readback. Then audit all nine closing commits, refresh actual main, inspect complete branch delta and explicitly merge the pinned phase tip with two parents. Verify merged-state product/distribution/docs checks and record the actual parent tips/outcomes in the integration commit body, then push main and confirm exact remote containment. This report precedes that integration; it does not claim a future push succeeded. Retain phase branch and stop before Phase 2 activation/work and any release.
