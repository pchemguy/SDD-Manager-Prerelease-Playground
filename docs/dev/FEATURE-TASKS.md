# Named-file ranges executable feature hierarchy

## Governing sources and preparation stop

This active feature list owns only the F-001–F-004 delta. Accepted [FEATURE-SPEC](FEATURE-SPEC.md)/[SPEC QC](FEATURE-SPEC-REVIEW-REPORT.md) at `b0f93cf170addc80a92541acc4151058e57b6e64` were accepted by decision `ca0eded9d6e8a7f40ba4e3c9ed4d8370b884db6d`. Accepted [FEATURE-PLAN](FEATURE-PLAN.md)/[PLAN QC](FEATURE-PLAN-REVIEW-REPORT.md) at `91d8a5a124004a7ca5b9c5217f4d5d99d825aade` were accepted by decision `515c3ea3464e4d67c359fa7bb949fe6945816f2b`. Reuse main [design](ARCHITECTURE.md), [components](DECOMPOSITION.md), [SPEC](SPEC.md), [layout](layout.md) and [TASKS](TASKS.md); unchanged contracts stay with those owners.

Project IDs T-001–T-017 remain singly owned in main TASKS. New T-018–T-024 are singly owned here, all unchecked. Main default has Phase 1 complete and pending Phase 2 tasks; the paused published phase checkpoint `e63b8946bbb99347b0f73f070f9c728945ee5925` separately proves T-010–T-012 complete. Treat that checkpoint's evidence as the JSON prerequisite rather than marking its copies in main complete. T-013–T-017 remain outside feature execution, pending. Existing task/phase reports and foreign hosted material remain preserved.

Preparation stops before execution. A later separately authorized handoff must satisfy published default preparation integration, a compatible verified/published JSON checkpoint on the feature branch, established paused-phase target, current QC and verified added-work projection. sdd-implement selects the actual bounded range and owns execution/completion. The adjacent [TASKS QC](FEATURE-TASKS-REVIEW-REPORT.md) and concrete delegated acceptance are separate gates; neither a checklist nor Ready authorizes implementation.

## Phase 2 — JSON and stdin

- [ ] Phase 2 — JSON and stdin
    - [ ] Milestone 2.4 — Named-file ranges
        - [x] T-018 — Implement pure normalized logical-line selection
            Outcome: internal C-010 selection using existing C-003 traversal; preserve selected contents/terminators, inclusive endpoints and available subsets without any BOM normalization or source dependency.
            Scope: `textstats/core.py`, `tests/unit/test_core.py` and internal selection/counting docstrings; public exports/signatures unchanged.
            Depends on: T-012's verified published milestone 2.1 completion/closure and the FEATURE-PLAN compatible baseline/projection prerequisites; existing pure core from T-001.
            Evidence: F-002/F-004 empty/final/blank/mixed CRLF/CR/LF, Unicode separators, EOF subset/empty, huge endpoints and exposed interior BOM. Verify normalized counting consumes selected content without a second normalization, plus whole-input core/API regression checks. This pure prerequisite leads directly to the real CLI path in T-019 within the same milestone.
        - [ ] T-019 — Integrate range validation and named-file text or JSON CLI
            Outcome: complete F-001/F-002/F-003 named-file path, both range spellings, all option orders and existing output/error/API behavior; minimal runnable range help/README demonstration.
            Scope: `textstats/cli.py`, cooperating `textstats/io.py` acquisition seam if needed, `tests/unit/test_cli.py`, `tests/unit/test_io.py`, `tests/integration/test_cli.py`, `tests/integration/test_api.py` and focused README/module documentation.
            Depends on: T-018 and retained completed JSON T-010–T-012 checkpoint; no stdin implementation dependency.
            Evidence: full invalid-range matrix including missing/repeated/mixed forms, ASCII positivity/order, >4,300-digit valid endpoints and many leading zeros without interpreter guard failure. Controlled seam and missing-file subprocess show usage rejection before acquisition. Decode complete bytes before selection, failing bad bytes after END; preserve owned-handle cleanup and unchanged file bytes. Run real text/JSON examples for every F-004 anchor, all range/BOM/JSON permutations, both spellings, INPUT placement and `--` dash-file support. Verify no-range API/CLI/JSON/signature/export/silence/error regressions; literal `-` remains a file. Run nonempty suites and execute the minimal README examples.
        - [ ] T-020 — Review, test and report milestone 2.4
            Scope: integrated parser, complete acquisition, normalized shared selection/counting and named-file text/JSON path; retained core/API/CLI failures and resource ownership.
            Depends on: T-018 and T-019.
            Evidence: code review and actual focused/full relevant tests, actual nonzero discovery counts, all F matrices, complete-decode/BOM/huge-endpoint regression evidence, repairs for every blocker and 2.4 human demonstration evidence. Report findings/TODO dispositions and limits; tests alone cannot complete this review.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.4.md`.
    - [ ] Milestone 2.5 — Range documentation and distribution
        - [ ] T-021 — Complete public and runnable named-file range documentation
            Outcome: accurate full range grammar/semantics/errors/composition/delivery boundary, with public API explicitly whole-input and stdin acquisition still deferred.
            Scope: `README.md`, `docs/public-api.md`, relevant core/I/O/CLI module/function docstrings and truthful owned root `AGENTS.md` navigation; preserve manual instructions and protected resources.
            Depends on: T-020 and reviewed/closed milestone 2.4.
            Evidence: execute documented named-file text/JSON examples in both BOM policies, selected blank/mixed/EOF/interior-BOM and invalid/decode cases; compare docs/help to delivered F contracts and retained public signatures/exports/exception/handle/status contracts. Review future stdin wording for source independence without asserting delivered acquisition. Run relevant nonempty product regressions.
        - [ ] T-022 — Verify range behavior from isolated extracted source
            Outcome: R-013 feature exits execute the real extracted module for named-file text/JSON range behavior and failures with truthful import provenance.
            Scope: `tools/check_distribution.py`, cooperating `tools/package_source.py` allowlist only if needed, `tests/integration/test_distribution.py` and distribution usage documentation.
            Depends on: T-021.
            Evidence: rebuild/extract source, isolate subprocess cwd/import environment and verify imported package belongs to extraction. Invoke its actual `python -m textstats` entry for F-004 success anchors, option/BOM/JSON composition, huge decimal/leading-zero endpoints, invalid/missing/repeated ranges and bad bytes after END; statuses/stdout/stderr retain contracts. Confirm archive docs and unchanged API, named-file/no-range/JSON/usage/error regressions and no coordinator resources/secrets. Use the selected supported Python executable with bytecode disabled in all child processes. Run independently nonempty unit/integration suites and extraction checks; archive listing/import alone is insufficient.
        - [ ] T-023 — Review, test and report milestone 2.5
            Scope: complete delivered range documentation, help/usability, isolated distribution and retained product behavior.
            Depends on: T-021 and T-022.
            Evidence: code review plus actual docs examples, nonempty discovery and extraction provenance/real module checks, all relevant regressions and repairs for every blocker. Record usability demonstration, actual evidence/limits and TODO dispositions before milestone closure.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.5.md`.
    - [ ] Milestone 2.6 — Range feature review
        - [ ] T-024 — Review, test and report the Phase 2 range feature extent
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
