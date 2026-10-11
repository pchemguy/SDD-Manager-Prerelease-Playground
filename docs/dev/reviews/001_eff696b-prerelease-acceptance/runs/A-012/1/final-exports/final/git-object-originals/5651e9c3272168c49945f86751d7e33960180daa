# Named-file ranges executable feature hierarchy

## Governing sources and preparation stop

This active feature list owns only the F-001–F-004 delta. Accepted [FEATURE-SPEC](FEATURE-SPEC.md)/[SPEC QC](FEATURE-SPEC-REVIEW-REPORT.md) at `b0f93cf170addc80a92541acc4151058e57b6e64` were accepted by decision `ca0eded9d6e8a7f40ba4e3c9ed4d8370b884db6d`. Accepted [FEATURE-PLAN](FEATURE-PLAN.md)/[PLAN QC](FEATURE-PLAN-REVIEW-REPORT.md) at `91d8a5a124004a7ca5b9c5217f4d5d99d825aade` were accepted by decision `515c3ea3464e4d67c359fa7bb949fe6945816f2b`. Reuse main [design](ARCHITECTURE.md), [components](DECOMPOSITION.md), [SPEC](SPEC.md), [layout](layout.md) and [TASKS](TASKS.md); unchanged contracts stay with those owners.

Project IDs T-001–T-017 remain singly owned in main TASKS. New T-018–T-024 are singly owned here, all unchecked. Main default has Phase 1 complete and pending Phase 2 tasks; the paused published phase checkpoint `e63b8946bbb99347b0f73f070f9c728945ee5925` separately proves T-010–T-012 complete. Treat that checkpoint's evidence as the JSON prerequisite rather than marking its copies in main complete. T-013–T-017 remain outside feature execution, pending. Existing task/phase reports and foreign hosted material remain preserved.

Preparation stops before execution. A later separately authorized handoff must satisfy published default preparation integration, a compatible verified/published JSON checkpoint on the feature branch, established paused-phase target, current QC and verified added-work projection. sdd-implement selects the actual bounded range and owns execution/completion. The adjacent [TASKS QC](FEATURE-TASKS-REVIEW-REPORT.md) and concrete delegated acceptance are separate gates; neither a checklist nor Ready authorizes implementation.

## Phase 2 — JSON and stdin

- [x] Phase 2 — JSON and stdin
    - [x] Milestone 2.4 — Named-file ranges
        - [x] T-018 — Implement pure normalized logical-line selection
            Outcome: internal C-010 selection using existing C-003 traversal; preserve selected contents/terminators, inclusive endpoints and available subsets without any BOM normalization or source dependency.
            Scope: `textstats/core.py`, `tests/unit/test_core.py` and internal selection/counting docstrings; public exports/signatures unchanged.
            Depends on: T-012's verified published milestone 2.1 completion/closure and the FEATURE-PLAN compatible baseline/projection prerequisites; existing pure core from T-001.
            Evidence: F-002/F-004 empty/final/blank/mixed CRLF/CR/LF, Unicode separators, EOF subset/empty, huge endpoints and exposed interior BOM. Verify normalized counting consumes selected content without a second normalization, plus whole-input core/API regression checks. This pure prerequisite leads directly to the real CLI path in T-019 within the same milestone.
        - [x] T-019 — Integrate range validation and named-file text or JSON CLI
            Outcome: complete F-001/F-002/F-003 named-file path, both range spellings, all option orders and existing output/error/API behavior; minimal runnable range help/README demonstration.
            Scope: `textstats/cli.py`, cooperating `textstats/io.py` acquisition seam if needed, `tests/unit/test_cli.py`, `tests/unit/test_io.py`, `tests/integration/test_cli.py`, `tests/integration/test_api.py` and focused README/module documentation.
            Depends on: T-018 and retained completed JSON T-010–T-012 checkpoint; no stdin implementation dependency.
            Evidence: full invalid-range matrix including missing/repeated/mixed forms, ASCII positivity/order, >4,300-digit valid endpoints and many leading zeros without interpreter guard failure. Controlled seam and missing-file subprocess show usage rejection before acquisition. Decode complete bytes before selection, failing bad bytes after END; preserve owned-handle cleanup and unchanged file bytes. Run real text/JSON examples for every F-004 anchor, all range/BOM/JSON permutations, both spellings, INPUT placement and `--` dash-file support. Verify no-range API/CLI/JSON/signature/export/silence/error regressions; literal `-` remains a file. Run nonempty suites and execute the minimal README examples.
        - [x] T-020 — Review, test and report milestone 2.4
            Scope: integrated parser, complete acquisition, normalized shared selection/counting and named-file text/JSON path; retained core/API/CLI failures and resource ownership.
            Depends on: T-018 and T-019.
            Evidence: code review and actual focused/full relevant tests, actual nonzero discovery counts, all F matrices, complete-decode/BOM/huge-endpoint regression evidence, repairs for every blocker and 2.4 human demonstration evidence. Report findings/TODO dispositions and limits; tests alone cannot complete this review.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.4.md`.
    - [x] Milestone 2.5 — Range documentation and distribution
        - [x] T-021 — Complete public and runnable named-file range documentation
            Outcome: accurate full range grammar/semantics/errors/composition/delivery boundary, with public API explicitly whole-input and stdin acquisition still deferred.
            Scope: `README.md`, `docs/public-api.md`, relevant core/I/O/CLI module/function docstrings and truthful owned root `AGENTS.md` navigation; preserve manual instructions and protected resources.
            Depends on: T-020 and reviewed/closed milestone 2.4.
            Evidence: execute documented named-file text/JSON examples in both BOM policies, selected blank/mixed/EOF/interior-BOM and invalid/decode cases; compare docs/help to delivered F contracts and retained public signatures/exports/exception/handle/status contracts. Review future stdin wording for source independence without asserting delivered acquisition. Run relevant nonempty product regressions.
        - [x] T-022 — Verify range behavior from isolated extracted source
            Outcome: R-013 feature exits execute the real extracted module for named-file text/JSON range behavior and failures with truthful import provenance.
            Scope: `tools/check_distribution.py`, cooperating `tools/package_source.py` allowlist only if needed, `tests/integration/test_distribution.py` and distribution usage documentation.
            Depends on: T-021.
            Evidence: rebuild/extract source, isolate subprocess cwd/import environment and verify imported package belongs to extraction. Invoke its actual `python -m textstats` entry for F-004 success anchors, option/BOM/JSON composition, huge decimal/leading-zero endpoints, invalid/missing/repeated ranges and bad bytes after END; statuses/stdout/stderr retain contracts. Confirm archive docs and unchanged API, named-file/no-range/JSON/usage/error regressions and no coordinator resources/secrets. Use the selected supported Python executable with bytecode disabled in all child processes. Run independently nonempty unit/integration suites and extraction checks; archive listing/import alone is insufficient.
        - [x] T-023 — Review, test and report milestone 2.5
            Scope: complete delivered range documentation, help/usability, isolated distribution and retained product behavior.
            Depends on: T-021 and T-022.
            Evidence: code review plus actual docs examples, nonempty discovery and extraction provenance/real module checks, all relevant regressions and repairs for every blocker. Record usability demonstration, actual evidence/limits and TODO dispositions before milestone closure.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.5.md`.
    - [x] Milestone 2.6 — Range feature review
        - [x] T-024 — Review, test and report the Phase 2 range feature extent
            Scope: cross-milestone range feature and affected main contracts, source-independent normalized pipeline, unchanged public API, complete docs/extraction and retained named-file text/JSON. This is feature-extent review, not main Phase 2 or project completion.
            Depends on: T-020 and T-023; feature delivery milestones 2.4 and 2.5 completed/closed, excluding its own still-open 2.6.
            Evidence: code review and actual complete relevant product/docs/distribution exits, nonzero counts, final blocker repairs, feature usefulness/risk evidence, findings and TODO aggregation with provenance/options/owners/resolutions from both feature milestones. Reconcile feature parent claims only; do not complete main 2.2/2.3 or T-013–T-017. Reports must state pending stdin/final work and later incorporation/integration prerequisites.
            Reports: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/PHASE-REPORT.md` and `docs/dev/features/002_e7cae5b-named-file-ranges/IMPLEMENTATION-REPORT.md`.

## Execution, ownership and integration rules

Every feature checkbox measures this list's extent only. It cannot close the whole Phase 2 or main final review while independent main work remains. Existing main parents retain exact names/IDs; new milestone identities are the accepted plan's 2.4/2.5/2.6. Future added-work projection reuses the exact existing Phase 2 label and associates every new task with its one new parent milestone. Preserve foreign issues, labels, comments and milestone prose; uncertain ownership blocks writes/closure.

A task closes with its result/evidence and initial checkbox together in one commit whose subject starts with exactly one owning `[T-NNN]`; publish/read back every owned commit before further work, then reconcile the task issue. Each delivery milestone closes only after all its tasks including review and exit evidence; final feature review follows both delivery closures. Reviews require both code review and actual checks; bugs, critical issues and SPEC/PLAN violations block completion. Reports include TODO `None` or stable located eligible noncritical deferrals with impact/rationale/options/owner, retaining prior findings and resolutions.

After a later authorized complete feature boundary, sdd-integrate-feature coordinates accepted incorporation and explicit TASKS/FEATURE-TASKS ownership reconciliation, preserving stable task IDs/issues and updating affected pending main composition/docs/final review dependencies. Archive eligible sources only after ownership/evidence disposition; then verify the reconciled result and explicitly merge/publish to the paused phase target. No automatic default merge or whole-phase completion follows. This preparation performs none of those actions, executes no task, closes no issue/milestone and publishes no release.

## T-018 completion evidence

Full selected range is T-018–T-024, stopping after accepted feature conclusion and paused-phase integration. Accepted preparation source `503dc510aef79bb7f8befc87e8072dd344182dd3` explicitly merged/published to default main `fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`; compatible completed JSON source `e63b8946bbb99347b0f73f070f9c728945ee5925` explicitly merged/published on feature branch as `806e989567aef425ddd933f33fbd8f9af5edae2a`. Both exact remote tips and two parents were verified. JSON merge retained source/tests/report and pending main work; only AGENTS navigation conflicted and was coherently resolved. Before task edits/tests, full added-work projection read back Phase 2 label, native milestones #7/#8/#9 and unique marked T-018–T-024 issues #19–#25 with correct initial associations. T-018 uniquely owns issue #19/native milestone #7. Completed predecessor issues/milestones remain closed; main stdin/final issues remain open.

Delivered pure internal `_select_lines` using existing `_logical_lines`, preserving selected content/terminators, inclusive endpoints, available EOF subsets and source/BOM independence. Endpoints are comparisons, never iteration bounds; 5,001-digit integers work without imposing a cap. Public exports/signatures are unchanged; selected normalized content goes directly to `_count_normalized`, retaining exposed interior BOMs. Source docstrings explain validated endpoint/BOM/source assumptions.

Tests were written before behavior. A minimal unimplemented declaration made valid import/collection possible; `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest tests.unit.test_core.SelectionTests -v` then ran two tests and failed with 14 behavioral NotImplementedError errors (not setup/import failure). Implementing selection yielded `python -B -m unittest tests.unit.test_core -v` passing 12 tests and `python -B -m unittest tests.integration.test_api -v` passing eight tests on Python 3.12.14, no skips/warnings. Exact preserved segment, blank/mixed/final/Unicode/EOF/huge and BOM-exposure assertions plus existing whole-input/API silence/immutability/signature/file regressions passed; diff whitespace passed. Concrete delegated artifact acceptance covers core blob `872175963ba892670eb4f142df431a7bf050d581` and unit test blob `c619bf38f359d9a5d037b2003be8e93561df5cb9`, decision `308ec9195abc6b8ecd04b708331e91f480354422`. No CLI range or extracted range behavior is yet delivered. Exactly this result/tests/docs/evidence/initial checkbox close together before immediate publication/readback and hosted closure.

## T-019 completion evidence

T-018 `3bcd141b24bf0f655fa8c2f777c7c9eb0a24ba93` was pushed and exact remote tip read back; its unique issue #19 was closed/completed with evidence readback before this task. T-019 uniquely maps to issue #20/native milestone #7 under the verified added-work projection.

Delivered both `--lines START:END` and `--lines=START:END`, positive ASCII/unbounded decimal conversion independent of interpreter conversion guards, positivity/order and repetition rejection before acquisition. Shared `_read_file_text` finishes complete strict decode under owned-handle cleanup, then CLI performs once-only whole-input BOM normalization, shared selection and normalized counting. No-range CLI retains `count_file`; public exports/signatures/silence/whole-input semantics remain unchanged. Existing text/JSON rendering and expected error translation are retained. Minimal help/README examples and affected public/module navigation are truthful; complete documentation/extracted range exits remain T-021/T-022.

Before production behavior, `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest tests.unit.test_cli.RangeCliTests tests.integration.test_cli.RangeModuleTests.test_every_feature_anchor_text_json_and_bom_policy -v` ran five tests and failed with 55 behavioral assertion failures because unchanged argparse rejected ranges; invalid usage checks already passed. No import/setup RED or exception is claimed. After implementation, the focused full range suite passed nine tests. Fresh `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings, including retained 99-case isolated whole-input/text/JSON extraction checks. All F-004 success anchors in both output/BOM policies, all option permutations/spellings/INPUT placements, 5,001-digit endpoints/leading zeros, controlled invalid-before-open, every invalid class on missing files, complete decode after END, controlled read/decode closure, byte preservation and dash/literal-minus paths passed. Existing core/API/error/JSON regressions passed.

README setup/help plus both minimal range examples executed in temporary named-file context with exact two-line/three-word text/JSON output. Changed whitespace passes. Concrete delegated acceptance `68f2bbbd56caa5210474fbc5fa4aef499b6d476f` covers the six exact CLI/I/O/unit/integration/README/public-guide artifacts presented at T-018 published baseline. Task result/tests/docs/current evidence and initial T-019 checkbox close together; milestone parent stays unchecked until dedicated T-020 review, publication and hosted closure. Other runtimes/platforms remain unverified; no stdin acquisition or release.

## T-020 completion evidence

Dedicated coherent milestone 2.4 implementation code review is recorded in [2.4 report](features/002_e7cae5b-named-file-ranges/phases/2/2.4.md), source `46e1455a5aca1f86d385a6bed649c4331c5f7296`. Parser/acquisition/normalized pipeline/API/output/error/tests/minimal docs were read separately from check execution; no blocker or repair found, TODO None. Fresh `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings; ten real named-file text/JSON demonstrations passed exact counts/status/streams and unchanged bytes. Retained 99 extracted whole-input/text/JSON cases are explicitly not range extraction acceptance. Full range matrices and current relevant regressions satisfy 2.4; detailed docs/distribution and feature-extent review remain T-021–T-024, stdin/final main work pending.

Concrete delegated report acceptance `beac0a623d27056d6deb9854674a9307dba3f89d` covers report blob `0597bdf91ce96c0ad0623be1e0696814abdc00c7`. Prior report presentation's pending-review sentence is historical; this current owning evidence records the actual accepted conclusion. T-018/T-019 commits were each published/read back, issues #19/#20 closed/completed with evidence before T-020. Unique T-020 issue #21/native milestone #7. Exactly T-020 report/result/current evidence/initial checkbox and eligible feature milestone 2.4 parent close together; immediately push/read back before issue closure and full associated-issue validation/milestone #7 closure. Whole feature and main Phase 2 remain unchecked.

## T-021 completion evidence

Completed full runnable/public named-file range grammar, option composition,
CRLF/CR/LF/blank/EOF semantics, once-only whole-input BOM policy, preserved interior
BOM, complete strict decoding including bytes after END, invocation-before-access
errors and unchanged public API signatures/exports/exceptions/silence/handle
ownership. Future stdin acquisition remains explicitly deferred with source-independent
normalized selection. Reviewed core/I/O consequential docstrings as already accurate;
CLI docstring cleanup changes no executable AST. Root AGENTS retains manual policy
and now describes actual published preparation/JSON/milestone 2.4 checkpoints.

All README/public-guide runnable fences executed in temporary development checkout
copy with bytecode-disabled children. Exact range counts/status/streams, both BOM
policies, text/JSON, blank/mixed/EOF/interior-BOM and invalid/decode examples passed;
API assertions, independent discoveries, packaging/checker and extracted commands
also passed. Fresh complete captured `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py`
passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings, retaining
99 whole-input extracted cases. Selected local links and whitespace pass. Earlier
redirected runner reported exit 0 but its incomplete log is retained as ambiguous,
not completion proof; an incidental `ps` diagnostic exited 1 with `fatal library
error, lookup self`, without product changes. The fresh complete capture resolves
verification uncertainty. No fabricated RED for this documentation-only task.

Concrete delegated decision `ff5c536e1f76cd79bbc4bb155a35963498953240` accepts README
`f358db5de7854cd8bfcc95048c9360c7da4f684b`, public guide
`0c165b39da9ef9f0f853ce7fd975c84c2de77609`, AGENTS
`9d2e63b058f189910194c5968f52269c1abe5465` and CLI documentation
`dc65bdca67c75f8b4a4a6501b01cf80c38f89d88` at published T-020 baseline.
Task result/current evidence/initial checkbox close together; milestone 2.5 and
feature parent remain unchecked. Publish/read back then close/read back unique
issue #22 before dependent T-022. Range extraction, later dedicated reviews,
feature conclusion/integration and pending main stdin/final remain separate gates.

## T-022 completion evidence

Extended the unchanged eleven-file source allowlist's checker to execute 315 actual
isolated extracted-module cases: retained 99 whole-input/text/JSON/BOM/error/help
checks plus 52 literal F-004 anchor combinations, 48 range-spelling/option-order/
INPUT-position combinations, 12 huge/leading-zero cases, 96 invalid/missing/repeated
usage cases on missing input, four complete-decode-after-END failures and four
range-selected dash/literal-minus cases. All check exact status/streams/counts and
sample bytes. The extraction also passes a silent public whole-input/export/
keyword-only-signature probe. Actual import location belongs to extraction;
PYTHONPATH/PYTHONHOME/PYTHONSTARTUP are removed, user-site disabled, and all checker
children use the selected interpreter with -B plus bytecode-disabled environment.
No checkout helper replaces actual extracted CLI execution.

Before checker changes, two independently faulty extracted archives retained healthy
whole-input behavior but ignored range selection or normalized an exposed BOM twice.
The old checker accepted each through all 99 cases, causing two genuine behavioral
expect-rejection failures. The original RED is retained; simplified equivalent BOM
mutant test source was rerun before implementation with the same two failures.
GREEN rejects both mutants (two tests). Fresh complete runner passed 31 unit/28
integration tests on Python 3.12.14, no skips/warnings, both suite summaries and exit
0 captured. Fresh current rebuilt extraction passed 315 cases. All eleven archived
source/docs bytes match current checkout, including updated README; credentials,
coordinator resources, development records and tests remain excluded. Whitespace
passes; production package behavior is unchanged. README/AGENTS accurately describe
current checker/suite coverage, with presentation-time pending acceptance historical.

Concrete four-artifact decision `ce2df08c4a716b0a830077e23fc383b424299523` accepts
checker `6c4eb3baeb61e583caba86f3e9cbc48d0fb038db`, integration tests
`0d972097b798e6d35970d13767f10a957818048f`, README
`6e4fca7d8fcaa73b9e228f186aedc74cf9ea01a9` and AGENTS
`b9c19857fb95f290b92dc8c0cf09533345602b68` at published T-021 baseline.
Result/current evidence/initial task checkbox close in one commit; milestone 2.5
and feature parent remain unchecked. Immediately publish/read back, then close/read
back unique issue #23 before dependent T-023. No stdin/final Phase 2 execution,
whole-phase closure, default integration or release is claimed.

## T-023 completion evidence

Dedicated coherent milestone 2.5 review of published T-022 source
`f2dc46627c04b92e4d2990843927e52be63f2660` is recorded in
[2.5 report](features/002_e7cae5b-named-file-ranges/phases/2/2.5.md).
Read five package modules, builder/checker, distribution and real range module
tests, README/public API together and separately from check execution. No blocker
or repair; TODO None. Fresh all runnable guide fences completed in a temporary
current development-checkout copy: 31 unit/28 integration full runner and independent
discoveries, both OK/status 0, no skips/warnings; 315 actual isolated extracted
module cases plus silent unchanged API/signature probe, package build and Bash
extraction outputs, all named-file/BOM/JSON/range/invalid/decode examples. Fresh
root ZIP exactly eleven approved members with each source/doc byte matching
current published product. Selected links/whitespace pass. Runtime Python 3.12.14;
other versions/platforms, stdin acquisition and release remain unverified/outside.

Concrete report decision `ee49eb727938ab671daf6f9944c9cf4c086373f0` accepts blob
`fc89a37645234a4f5079919ad7692e71f5d87f6f`. Report presentation-time pending
acceptance is historical; this current owning evidence records accepted conclusion.
The command log has 32 command records and one completion marker (33 lines); an
intermediate tool's label saying 33 commands was corrected before presentation.
Original ambiguous log/process-inspection error and T-022 RED/GREEN provenance
remain retained, without claiming an unseen acceptance or concealed repair.
T-021/T-022 exact refs/issues #22/#23 were published/closed/read back before review.
T-023 result/report/evidence/initial checkbox and eligible feature milestone 2.5
parent close together; immediately publish/read back then close/read back issue
#24 and validate every associated completed issue before native milestone #8
closure. Feature 2.6/parent remain unchecked until T-024, while main Phase 2 and
stdin/final T-013–T-017 stay pending.

## T-024 completion evidence

Dedicated coherent feature-extent review at published
`4eeee9e9505b29b4a616292434561aab569dac7f` is recorded in
[extent report](features/002_e7cae5b-named-file-ranges/phases/2/PHASE-REPORT.md)
and [final implementation report](features/002_e7cae5b-named-file-ranges/IMPLEMENTATION-REPORT.md).
Cross-boundary review covers actual SPEC/design/feature PLAN/contracts and both
delivery milestones; no blocker/repair, TODO None aggregated with provenance.
Fresh root full runner passed 31 unit/28 integration tests, both OK/status 0,
no skips/warnings; fresh root checker passed 315 actual isolated module cases and
silent unchanged API/signature probe. Fresh 27 usability/API/documentation commands,
temp build/Bash extraction and exact eleven-file source/doc ZIP comparisons pass.
T-023's complete 32-command evidence remains applicable to identical product/docs
bytes, with reused and fresh scopes explicitly distinguished. Runtime Python
3.12.14; other platforms/versions, performance/stdin/release remain unverified.

Actual parent-delta audit confirms T-018–T-023 each carries its result/current
evidence/initial checkbox in one single owning-prefix commit; T-024 follows the
same contract. Original genuine RED/GREEN and resolved evidence/tool interventions
remain retained. Native8 original helper assertion failure occurred before mutation;
helper-only correction to accepted empty TODO value then full association closure/
readback succeeded, without changing accepted report. Main pending stdin/final
work is retained rather than waived as a feature deferral.

Concrete pair decision `44d271f41db658563585cc6a75aae17e81d71935` accepts extent
`d76c1f39f55dc8ae81a67ddbb9ad4c5fe08f8ba4` and implementation report
`e0019e493e01d81555908b30e4b2d5949831179a`; report presentation-time pending
acceptance is historical and this current owning evidence records actual decision.
T-024 result/reports/current evidence/initial checkbox and eligible feature 2.6/
Phase 2 extent parents close together. These feature parents measure only this
seven-task list; the main Phase 2 parent, 2.2/2.3 and T-013–T-017 stay unchecked.
Immediately publish/read back, then issue #25 and complete native #9 associated-
issue validation/closure/readback before authorized sole-main ownership/current QC/
archive reconciliation and concrete changed-artifact acceptance. Explicit verified/
published paused-phase integration is still required afterward; no incomplete
phase merge into default or release follows.
