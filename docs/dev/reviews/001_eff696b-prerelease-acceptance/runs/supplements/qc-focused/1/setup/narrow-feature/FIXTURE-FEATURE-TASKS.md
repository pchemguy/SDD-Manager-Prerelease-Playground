# Named-file ranges executable feature hierarchy

## Unaccepted proposal and retained original provenance

This active feature list owns only the F-001–F-004 delta. Accepted [FEATURE-SPEC](FEATURE-SPEC.md)/[SPEC QC](FEATURE-SPEC-REVIEW-REPORT.md) at `b0f93cf170addc80a92541acc4151058e57b6e64` were accepted by decision `ca0eded9d6e8a7f40ba4e3c9ed4d8370b884db6d`. Accepted [FEATURE-PLAN](FEATURE-PLAN.md)/[PLAN QC](FEATURE-PLAN-REVIEW-REPORT.md) at `91d8a5a124004a7ca5b9c5217f4d5d99d825aade` were accepted by decision `515c3ea3464e4d67c359fa7bb949fe6945816f2b`. Reuse main [design](ARCHITECTURE.md), [components](DECOMPOSITION.md), [SPEC](SPEC.md), [layout](layout.md) and [TASKS](TASKS.md); unchanged contracts stay with those owners.

Project IDs T-001–T-017 remain singly owned in main TASKS. New T-018–T-024 are singly owned here, all unchecked. Main default has Phase 1 complete and pending Phase 2 tasks; the paused published phase checkpoint `e63b8946bbb99347b0f73f070f9c728945ee5925` separately proves T-010–T-012 complete. Treat that checkpoint's evidence as the JSON prerequisite rather than marking its copies in main complete. T-013–T-017 remain outside feature execution, pending. Existing task/phase reports and foreign hosted material remain preserved.

Preparation stops before execution. A later separately authorized handoff must satisfy published default preparation integration, a compatible verified/published JSON checkpoint on the feature branch, established paused-phase target, current QC and verified added-work projection. sdd-implement selects the actual bounded range and owns execution/completion. The adjacent [TASKS QC](FEATURE-TASKS-REVIEW-REPORT.md) and concrete delegated acceptance are separate gates; neither a checklist nor Ready authorizes implementation.

This modified hierarchy is an unaccepted caller proposal. Original PLAN/TASKS acceptance and adjacent QC do not accept these draft bytes. No unchecked work is treated as completed.

## Phase 2 — JSON and stdin

- [ ] Phase 2 — JSON and stdin
    - [ ] Milestone 2.4 — Named-file ranges
        - [ ] T-018 — Implement pure normalized logical-line selection
            Outcome: internal C-010 selection using existing C-003 traversal; preserve selected contents/terminators, inclusive endpoints and available subsets without any BOM normalization or source dependency.
            Scope: `textstats/core.py`, `tests/unit/test_core.py` and internal selection/counting docstrings; public exports/signatures unchanged.
            Depends on: T-012's verified published milestone 2.1 completion/closure and the FEATURE-PLAN compatible baseline/projection prerequisites; existing pure core from T-001.
            Evidence: F-002/F-004 empty/final/blank/mixed CRLF/CR/LF, Unicode separators, EOF subset/empty, huge endpoints and exposed interior BOM. Verify normalized counting consumes selected content without a second normalization, plus whole-input core/API regression checks. This pure prerequisite leads directly to the real CLI path in T-019 within the same milestone.
        - [ ] T-019 — Integrate range validation and named-file text or JSON CLI
            Outcome: complete F-001/F-002/F-003 named-file path, both range spellings, all option orders and existing output/error/API behavior; minimal runnable range help/README demonstration.
            Scope: `textstats/cli.py`, cooperating `textstats/io.py` acquisition seam if needed, `tests/unit/test_cli.py`, `tests/unit/test_io.py`, `tests/integration/test_cli.py`, `tests/integration/test_api.py` and focused README/module documentation.
            Depends on: T-018 and retained completed JSON T-010–T-012 checkpoint; no stdin implementation dependency.
            Evidence: full invalid-range matrix including missing/repeated/mixed forms, ASCII positivity/order, >4,300-digit valid endpoints and many leading zeros without interpreter guard failure. Controlled seam and missing-file subprocess show usage rejection before acquisition. Decode complete bytes before selection, failing bad bytes after END; preserve owned-handle cleanup and unchanged file bytes. Run real text/JSON examples for every F-004 anchor, all range/BOM/JSON permutations, both spellings, INPUT placement and `--` dash-file support. Verify no-range API/CLI/JSON/signature/export/silence/error regressions; literal `-` remains a file. Run nonempty suites and execute the minimal README examples.
        - [ ] T-021 — Complete public and runnable named-file range documentation
            Outcome: accurate full range grammar/semantics/errors/composition/delivery boundary, with public API explicitly whole-input and stdin acquisition still deferred.
            Scope: `README.md`, `docs/public-api.md`, relevant core/I/O/CLI module/function docstrings and truthful owned root `AGENTS.md` navigation; preserve manual instructions and protected resources.
            Depends on: T-019; consolidated delivery review/closure follows all four delivery tasks.
            Evidence: execute documented named-file text/JSON examples in both BOM policies, selected blank/mixed/EOF/interior-BOM and invalid/decode cases; compare docs/help to delivered F contracts and retained public signatures/exports/exception/handle/status contracts. Review future stdin wording for source independence without asserting delivered acquisition. Run relevant nonempty product regressions.
        - [ ] T-022 — Verify range behavior from isolated extracted source
            Outcome: R-013 feature exits execute the real extracted module for named-file text/JSON range behavior and failures with truthful import provenance.
            Scope: `tools/check_distribution.py`, cooperating `tools/package_source.py` allowlist only if needed, `tests/integration/test_distribution.py` and distribution usage documentation.
            Depends on: T-021.
            Evidence: rebuild/extract source, isolate subprocess cwd/import environment and verify imported package belongs to extraction. Invoke its actual `python -m textstats` entry for F-004 success anchors, option/BOM/JSON composition, huge decimal/leading-zero endpoints, invalid/missing/repeated ranges and bad bytes after END; statuses/stdout/stderr retain contracts. Confirm archive docs and unchanged API, named-file/no-range/JSON/usage/error regressions and no coordinator resources/secrets. Use the selected supported Python executable with bytecode disabled in all child processes. Run independently nonempty unit/integration suites and extraction checks; archive listing/import alone is insufficient.
        - [ ] T-020 — Review, test and report complete milestone 2.4
            Scope: parser/selection/complete acquisition/named-file text/JSON, full public/runnable documentation, isolated extracted-source provenance and unchanged public API/core/file/resource/error behavior.
            Depends on: T-018, T-019, T-021 and T-022.
            Evidence: actual code review plus every F matrix, huge-endpoint/BOM/complete-decode/usage-before-acquisition regressions, nonempty unit/integration counts, all runnable public examples, independently imported extracted real module and retained signature/export/error/resource checks. Repair every blocker. Preserve usefulness demonstrations and original findings/TODOs with provenance/options/owners/limits; tests alone cannot complete review. Original T-020/T-023 review responsibilities consolidate here without claiming T-023 completed.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.4.md`.
    - [ ] Milestone 2.6 — Range feature review
        - [ ] T-024 — Review, test and report the Phase 2 range feature extent
            Scope: cross-milestone range feature and affected main contracts, source-independent normalized pipeline, unchanged public API, complete docs/extraction and retained named-file text/JSON. This is feature-extent review, not main Phase 2 or project completion.
            Depends on: T-020 and completed/closed consolidated milestone 2.4, excluding its own still-open 2.6.
            Evidence: code review and actual complete relevant product/docs/distribution exits, nonzero counts, final blocker repairs, feature usefulness/risk evidence, findings and TODO aggregation with provenance/options/owners/resolutions from all delivery tasks and their consolidated milestone review. Reconcile feature parent claims only; do not complete main 2.2/2.3 or T-013–T-017. Reports must state pending stdin/final work and later incorporation/integration prerequisites.
            Reports: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/PHASE-REPORT.md` and `docs/dev/features/002_e7cae5b-named-file-ranges/IMPLEMENTATION-REPORT.md`.

## Reserved historical identities

T-023 and former milestone 2.5 remain reserved, unchecked in original source objects and outside this proposed executable range. Their original names, dependencies, reports and responsibilities remain in baseline `8036adbd71ffc1f04b98e689cc131781bc20cd1f` and accompanying original caller source evidence. No closure, deletion-as-done, duplicate ownership, new issue or archive follows. T-020 proposes combined delivery review; T-024 remains final feature review.

## Execution, ownership and integration rules

Every feature checkbox measures this list's extent only. It cannot close the whole Phase 2 or main final review while independent main work remains. Existing main parents retain exact names/IDs; proposed active milestone identities are 2.4/2.6; original 2.5 is reserved and unexecuted. Future added-work projection reuses the exact existing Phase 2 label and associates every new task with its one new parent milestone. Preserve foreign issues, labels, comments and milestone prose; uncertain ownership blocks writes/closure.

A task closes with its result/evidence and initial checkbox together in one commit whose subject starts with exactly one owning `[T-NNN]`; publish/read back every owned commit before further work, then reconcile the task issue. Each delivery milestone closes only after all its tasks including review and exit evidence; final feature review follows the delivery closure. Reviews require both code review and actual checks; bugs, critical issues and SPEC/PLAN violations block completion. Reports include TODO `None` or stable located eligible noncritical deferrals with impact/rationale/options/owner, retaining prior findings and resolutions.

After a later authorized complete feature boundary, sdd-integrate-feature coordinates accepted incorporation and explicit TASKS/FEATURE-TASKS ownership reconciliation, preserving stable task IDs/issues and updating affected pending main composition/docs/final review dependencies. Archive eligible sources only after ownership/evidence disposition; then verify the reconciled result and explicitly merge/publish to the paused phase target. No automatic default merge or whole-phase completion follows. This preparation performs none of those actions, executes no task, closes no issue/milestone and publishes no release.
