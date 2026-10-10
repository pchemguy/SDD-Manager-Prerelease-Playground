# Product repository orientation

This dedicated repository uses the SDD Manager package pinned in `textstats-run-resources/plugin/`. Read its `skills/sdd-manage/SKILL.md` and the relevant references for the requested product workflow. Product documents and implementation are consumer-owned; no TextStats implementation has been supplied by setup.

Preserve `textstats-run-resources/`, existing ignore rules and the separate publisher fixture under `.github/` and `docs/testing/publisher-037/`. Those are coordinator-owned resources, outside ordinary product edits. Credentials remain protected and outside reports or handoffs.

## Product orientation

The [TextStats project brief](docs/dev/PROJECT.md) has scoped delegated coordinator acceptance for this test. The [architecture](docs/dev/ARCHITECTURE.md) has scoped delegated coordinator acceptance. The [decomposition](docs/dev/DECOMPOSITION.md) has scoped delegated coordinator acceptance. The [SPEC](docs/dev/SPEC.md) and [owner review](docs/dev/SPEC-REVIEW-REPORT.md) have scoped delegated coordinator acceptance. The [PLAN strategy](docs/dev/PLAN.md) has scoped delegated coordinator acceptance. The [layout](docs/dev/layout.md) and combined [PLAN review](docs/dev/PLAN-REVIEW-REPORT.md) have scoped delegated coordinator acceptance. The canonical [TASKS](docs/dev/TASKS.md) and [owner review](docs/dev/TASKS-REVIEW-REPORT.md) have scoped delegated coordinator acceptance; sdd-implement owns range selection/execution and completion. The current complete-Phase-1 request supersedes historical preparation and milestone stops within Phase 1. Accepted preparation is integrated and published on `main`; T-001 supplies the pure core and text facade with nonempty unit/integration suites on `phase/1-named-file-utility`. The current request completes Phase 1 (T-005 through T-009), including reviews, hosted closures and full-phase integration/publication, then stops before Phase 2; retain the phase branch. Do not treat coordinator resources as product implementation.

Development uses the pinned [SDD Manager](SDD-MANAGER.md) package identified above. Read applicable nested instructions for selected paths. Keep each newly created document's human review boundary and the current request's selected task boundary. Follow the pinned [publication procedure](textstats-run-resources/plugin/skills/sdd-manage/references/git-workflows.md): push and verify each workflow-owned commit before advancing or creating another commit. Task execution uses the pinned [task commit contract](textstats-run-resources/plugin/skills/sdd-implement/references/completion-and-checkpoints.md#task-commit-contract).

Python 3.12.14 was verified for T-001. From the repository root, run `python -m unittest discover -s tests/unit -t . -v` and `python -m unittest discover -s tests/integration -t . -v`; both now collect actual product tests. `textstats/core.py` owns pure semantics; `textstats/__init__.py` now exports `TextStats`, `count_text` and `count_file`. Strict file acquisition and the baseline named-file CLI are delivered. Run `python tools/check_tests.py` for independently discovered nonempty unit/integration suites. Complete CLI failure handling is delivered. See the [public API/module reference](docs/public-api.md) and runnable [README](README.md). Run `python tools/package_source.py` for the allowlisted source ZIP and `python tools/check_distribution.py` for isolated extracted-import and real module-entry checks. Product tests require a checkout; the archive includes only package/docs/notices and the builder/checker. See [T-001 evidence](docs/dev/TASKS.md#t-001-completion-evidence) for the published baseline and bounded checks.

## Phase 1 delivery checkpoint

The [Phase 1 review](docs/dev/reports/phases/1/PHASE-REPORT.md) records completed named-file/API/error/documentation/distribution exits and the integration protocol. All nine Phase 1 task results are tracked in canonical TASKS; Phase 2 remains pending and outside the current request. Use the current Git/remote state for actual integration/publication identity rather than treating this navigation as a branch snapshot. The current verified product suites contain 23 unit and 18 integration tests; extracted distribution checks exercise 36 real module cases on Python 3.12.14. Broader runtime/platform coverage is unverified.

## Named-file range conclusion and paused-phase integration

The current request authorizes complete named-file range delivery T-018–T-024,
required governing/task incorporation, concrete delegated artifact review, maintained
hosted reconciliation, eligible archive and explicit integration into paused
`phase/2-json-and-stdin`. T-018–T-024 are accepted, published through
`bf1b784b2f7ad394e8aba206c8ba2214f0b6d7fa`, with unique issues #19–#25 closed/completed
and native #7/#8/#9 closed after full associations/readback. Stop after verified/
published reconciled feature integration; retain pending T-013–T-017 and do not release.
Historical preparation/Phase 1 stops above do not limit this selected request.

Main [SPEC](docs/dev/SPEC.md), [PLAN](docs/dev/PLAN.md) and [TASKS](docs/dev/TASKS.md)
with current adjacent QC supply complete requirements/strategy and sole T-001–T-024
executable ownership. [Package](docs/dev/features/002_e7cae5b-named-file-ranges/README.md)
retains archived feature sources/QC and implementation reports; archived checklists
are historical, not executable owners. Preserve unchecked main Phase 2/2.2/2.3 and
stdin/final tasks, stable dependencies, report prefixes, original failures and evidence.
Existing design/layout seams suffice unchanged. Current root product checks collect
31 unit/28 integration tests; distribution executes 315 isolated actual whole-input/
range module cases plus silent unchanged API/signature probe, on Python 3.12.14.
Other supported runtimes/platforms remain unverified.

Accepted preparation was explicitly merged/published into default at
`fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`, then feature branch created and compatible
JSON prerequisite merged/published at `806e989567aef425ddd933f33fbd8f9af5edae2a`.
Default stays preparation-only without JSON. Concrete acceptance/publication of the
current reconciliation/QC/archive checkpoint and final paused-phase merge are pending;
no unseen acceptance or integration is inferred. Follow immediate per-commit push/
exact readback and owning task/result/evidence/initial-checkbox contracts above.
Use `PYTHONDONTWRITEBYTECODE=1 python -B` including children. Preserve protected
coordinator resources/foreign material/manual controls and pending main work.
No complete Phase 2/default merge or release follows this feature.

## Published JSON prerequisite

The separately published completed JSON milestone checkpoint `e63b8946bbb99347b0f73f070f9c728945ee5925` supplies T-010–T-012 and [milestone 2.1 review](docs/dev/reports/phases/2/2.1.md). Named-file `--json` composes with BOM policy and text remains default; stdin remains pending. Historical JSON-only verification recorded 25 unit/21 integration tests and 99 isolated extracted-module cases on Python 3.12.14. This compatible merge retains those results and pending T-013–T-017 without completing/integrating Phase 2 into default. Current range delivery authority and stop above govern this continuation.
