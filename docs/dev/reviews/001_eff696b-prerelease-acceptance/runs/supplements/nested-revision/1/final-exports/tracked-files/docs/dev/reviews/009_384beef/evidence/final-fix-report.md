# Final bounded fixwave report

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

Base: `f6fd96f`. Scoped commit: `584cfe07ea6fe540c6cb81c8413e53fe45d53d17` (`Fix caller-relative TextStats recovery export paths`) on `revision/009_384beef-textstats-test-project`.

## Findings addressed

- WB-R1: `export_recovery()` now makes its caller-relative destination absolute without resolving its lexical target. Python artifact writes and Git bundle creation/verification use that same location. Missing output parents are created with `mkdir(parents=True)` while the export directory remains exclusive (`exist_ok` is still false). Existing and dangling-symlink recovery destinations explicitly block. The main CLI's existing lexical output occupancy check remains intact.
- Actual subprocess CLI regressions cover caller cwd different from consumer cwd, both direct and nested relative outputs, and an absolute output with missing nested parents. They verify the requested observation and adjacent manifest, manifest and artifact hashes, absolute export location, complete bundle verification/fetch in a fresh clone, and unchanged consumer HEAD/refs/status/raw index/workfile bytes/mode/path inventory. Refusal subcases retain existing files, directories, live symlinks and dangling symlinks for both JSON and recovery paths.
- WB-R2: updated only the plan's stale State bullet and final implementation-status sentence. Tasks 1–3 are implemented/reviewed, fresh directory-only bootstrap is verified, and live acceptance remains explicitly unexecuted/pending its dedicated repository input. No Task 4 checkbox changed.

## Exact committed paths

1. `acceptance/textstats/scripts/core.py`
2. `acceptance/textstats/tests/test_recovery.py`
3. `acceptance/textstats/scripts/HELPER-INTERFACES.md`
4. `docs/dev/reviews/009_384beef/REVISION-PLAN.md`

## Retained verification

All commands ran from `/workspace/scratch/6420baa7afea`; outputs were redirected to the exact retained logs below. RED ran after adding tests and before production changes.

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v acceptance.textstats.tests.test_recovery.RecoveryTests.test_caller_relative_cli_exports_verified_bundle_outside_consumer acceptance.textstats.tests.test_recovery.RecoveryTests.test_absolute_cli_output_creates_missing_parent acceptance.textstats.tests.test_recovery.RecoveryTests.test_cli_refuses_occupied_and_dangling_output_and_recovery_paths > /workspace/scratch/textstats-revision-009/final-fix-red.log 2>&1
```

RED: exit 1; **3 tests, 4 failing subcases, zero errors**. Direct caller-relative output reported `git_operation_unavailable`; relative and absolute missing-parent outputs reported `support_operation_failed`; dangling recovery symlink returned a generic failure rather than the explicit occupied-evidence classification. Other occupied/symlink refusal subcases passed. The original reviewed reproduction log was retained unchanged; no old failure artifacts were removed or retried.

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v acceptance.textstats.tests.test_recovery > /workspace/scratch/textstats-revision-009/final-fix-green.log 2>&1
```

Focused GREEN: exit 0; **20 tests passed**, zero failures/errors, 3.903 seconds.

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v > /workspace/scratch/textstats-revision-009/final-fix-full-green.log 2>&1
```

Single final full suite: exit 0; **67 tests passed**, zero failures/errors, 11.405 seconds. This is the documented complete support suite; previous 64 tests plus 3 new regression test methods. Subcases are not counted as additional test methods.

`git diff --check`, `git diff --cached --check`, and post-commit `git diff --check f6fd96f HEAD` passed. Post-commit `git diff f6fd96f HEAD --name-only` lists exactly the four paths above.

## Limits and ownership

Tests use only disposable local fixtures/bare remotes and fresh local clones. Their ordinary temporary-fixture cleanup does not remove retained campaign failure evidence. No source push, hosted provider operation, credential/token inspection, live consumer dispatch, plugin-package mutation, or subagent delegation occurred. No unrelated source change was made. Root-owned source REVISION-REPORT/bootstrap evidence and pre-existing unrelated local state were neither staged nor edited; the latter two untracked paths remain present after the scoped commit. This proves the bounded helper path correction and support-suite behavior, not live TextStats acceptance, installed-client routing, provider semantics, real worker isolation/interruption, or absence of plugin defects. Independent reviewer recheck of this fix diff remains required.
