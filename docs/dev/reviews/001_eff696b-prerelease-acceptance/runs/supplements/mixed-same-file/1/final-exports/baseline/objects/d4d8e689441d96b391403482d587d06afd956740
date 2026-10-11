# Product repository orientation

## Current independent trial checkpoint

The current trial authorizes only T-001 on `phase/1-named-file-utility`, starting
from accepted preparation `1e3305c8659045945244c06861079fef879ca3c3` on `main`.
The trial explicitly declines hosted issue/milestone tracking. Publish each
checkpoint to local remote `delivery` and verify its exact ref before further
work. `origin` is read-only; no hosted writes are authorized. Stop after T-001
without T-002, parent completion, phase integration or later-phase activation.

T-001 supplies `textstats/core.py` and text exports in `textstats/__init__.py`.
Product tests live in `tests/unit/test_core.py` and
`tests/integration/test_api.py`. From the repository root, run
`python -B -m unittest discover -s tests/unit -t . -v` and
`python -B -m unittest discover -s tests/integration -t . -v`; both suites must
collect nonzero tests. `tools/check_tests.py` belongs to T-003 and distribution
tools to T-007, so those full-delivery commands below are unavailable at this
partial checkpoint. File exports and the module CLI remain undelivered.

The original preparation orientation below is retained as acceptance history;
its earlier preparation-only stopping instruction is superseded for this trial
by the current bounded implementation request. Product contracts and imported
acceptance/QC history remain unchanged.

## Original accepted preparation orientation

This dedicated repository uses the SDD Manager package pinned in `textstats-run-resources/plugin/`. Read its `skills/sdd-manage/SKILL.md` and the relevant references for the requested product workflow. Product documents and implementation are consumer-owned; no TextStats implementation has been supplied by setup.

Preserve `textstats-run-resources/`, existing ignore rules and the separate publisher fixture under `.github/` and `docs/testing/publisher-037/`. Those are coordinator-owned resources, outside ordinary product edits. Credentials remain protected and outside reports or handoffs.

## Product orientation

The [TextStats project brief](docs/dev/PROJECT.md) has scoped delegated coordinator acceptance for this test. The [architecture](docs/dev/ARCHITECTURE.md) has scoped delegated coordinator acceptance. The [decomposition](docs/dev/DECOMPOSITION.md) has scoped delegated coordinator acceptance. The [SPEC](docs/dev/SPEC.md) and [owner review](docs/dev/SPEC-REVIEW-REPORT.md) have scoped delegated coordinator acceptance. The [PLAN strategy](docs/dev/PLAN.md) has scoped delegated coordinator acceptance. The [layout](docs/dev/layout.md) and combined [PLAN review](docs/dev/PLAN-REVIEW-REPORT.md) have scoped delegated coordinator acceptance. The canonical [TASKS](docs/dev/TASKS.md) and [owner review](docs/dev/TASKS-REVIEW-REPORT.md) have scoped delegated coordinator acceptance; sdd-implement owns future range selection/execution and completion. Preparation is complete under the current request and stops before implementation, hosted projection and default-branch integration. No implementation task has started. Source and product tests do not exist yet. Do not treat coordinator resources as product implementation.

Preparation uses the pinned [SDD Manager](SDD-MANAGER.md) package identified above. Read applicable nested instructions for selected paths. Keep each newly created document's human review boundary, and stop before implementation under the current request. Follow the pinned [publication procedure](textstats-run-resources/plugin/skills/sdd-manage/references/git-workflows.md): push and verify each workflow-owned commit before advancing or creating another commit. Future task execution uses the pinned [task commit contract](textstats-run-resources/plugin/skills/sdd-implement/references/completion-and-checkpoints.md#task-commit-contract).

Python 3.12.14 is available in the preparation environment. The layout proposes `textstats/`, unit/integration product tests, `docs/public-api.md` and standard-library test/package/distribution check tools. Its commands are planned and have not been validated because implementation files do not exist. After delivery, run `python tools/check_tests.py` and `python tools/check_distribution.py` from the repository root; the test runner must reject empty product suites.
