# Task 2 portable support implementation

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

Implemented and committed as `fb5bbf1` (`test(textstats): add portable coordinator setup and recovery support`), based on `8afda4d`, on `revision/009_384beef-textstats-test-project`. No branch switch, push, live consumer campaign, real hosted write, credential-store inspection or package repair occurred. Owned paths are the four CLI entry points/shared stdlib core, helper interface guide, three support test modules/test utilities/discovery package markers, and one SETUP guide link. Source `.codex/` and revision report were not changed.

## Interfaces and behavior

The committed `scripts/HELPER-INTERFACES.md` specifies the exact version 1 JSON shapes and supported limits. All CLIs accept `--inputs/--output`; observe/assess also require `--run-state`; prepare requires a fresh explicit `--workspace`. Preflight/prepare optionally accept `--source-root`. Assess optionally accepts `--contract/--evidence` and supports literal, Git, file and task_ownership checks. Runtime Git identity binding uses schema-validated `expected_ref: checkpoint_refs.<field>`, mutually exclusive with `expected`. Recursive equality distinguishes JSON bool/integer. Empty collections, unknown fields, malformed evidence and absent runtime bindings fail. Deterministic results always retain `agent_behavior_assessed:false`; no registry/consumer Passed claim is accepted as agent assessment.

Missing or blank repository produces the exact required repository question on stdout, exit 2, before output/setup writes. Unknown/secret configuration errors are generic and do not echo values. Repository discovery verifies matching authorized remote identity and blocks ambiguity. Preflight only reads actual state and writes the caller's new observation file. Preparation exclusively creates an isolated absent-path clone, preserves original files/instructions/index, refuses resume setup, pins only committed package files (97 current files) from Git objects by default, and never copies source credentials or a product implementation fixture. Explicit dirty mode records working bytes, Git modes, changed paths and a mode-sensitive hash fingerprint; untracked additions are in the exact snapshot. Unborn dedicated local remotes receive only bounded operating instructions/ignore/vendor/provenance setup without author/branch/publication assumptions.

Observation reads actual HEAD/parents/refs/worktrees/index stages/workfiles/MERGE_HEAD and live read-only destination refs. Publication is published/unpublished/unknown; missing ancestry never produces a false unpublished finding. Uncertain push readback reconciles existing identity; uncertain API remains unknown. Helpers never retry a write or certify replay safety. Recovery exports include staged objects, separate binary-safe pending workfiles, deletions/modes/symlinks, merge metadata, tracked path baseline, checksums, patches and a verified bundle containing actual available merge/checkpoint/pending commit roots. Artifacts remain explicitly local-only pending external verified publication.

## Verification and retained failures

Final, post-commit complete repository test command:

`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v`

Result: **33 collected tests, 33 passed, zero failures/errors**. Full output: `/workspace/scratch/textstats-revision-009/task-2-final-green.log`. `git diff --check` also passed. Tests use disposable checkouts and bare local remotes only; fixture Git pushes target those temporary remotes, never hosted objects.

TDD progression is retained rather than conflated with a consumer campaign:

- `task-2-red.log`: 28 tests collected before CLI entry points existed. This is interface-not-implemented RED: expected success assertions failed and JSON consumers errored because scripts were missing. It is not claimed as proof of detailed behavioral sensitivity.
- `task-2-green-1.log`: initial implementation collected 28 and had 16 failures: legitimate schema vocabulary was over-rejected by the non-secret guard and an explicit local bare destination was misclassified as a checkout. Fixed without loosening version 1 schema validation. `task-2-green-2.log`: all 28 passed.
- `task-2-hardening-red.log`: 32 tests; expected behavioral failures exposed mode-insensitive dirty fingerprint and false unpublished inference for unavailable remote ancestry; missing merge_metadata/tracked_paths export fields produced two errors. `task-2-hardening-green.log`: all 32 passed after adding those required exports/mode facts.
- `task-2-path-red.log`: 33 tests; one expected failure showed an external workfile could be read through a replaced parent-directory symlink. Export now blocks that unsafe path before writing recovery output; final suite passes.
- `task-2-sensitivity.py` uses disposable copies, never mutates shipped source. Three retained fault-injection runs each fail the selected real behavior test: `task-2-sensitivity-bool-int.log` (bool/int equality fault), `task-2-sensitivity-conflict-stages.log` (index conflict stages flattened), and `task-2-sensitivity-unknown-publication.log` (unavailable remote falsely unpublished). These are expected sensitivity failures, not remaining test failures.

The test suite independently checks exact stdout/stderr/exit evidence mismatch, invalid and empty evidence, strict configuration/schema constraints, unknown nested fields, credential-bearing values, missing/ambiguous/mismatched repositories, occupied output/workspace/resume preservation, actual dirty-source pinning/modes, bounded unborn preparation, retained task ownership with review history excluded, staging/conflicts/local commit/publication uncertainty and protected-file exclusion.

Recovery usability is actually reconstructed in disposable fresh clones, not merely checked as metadata: staged versus unstaged file contents plus binary and symlink files restore exact index intent; staged and unstaged deletion restore and compare both diffs; conflict restoration imports all stages, verifies bundle, restores merge metadata and compares index/worktree diff/MERGE_HEAD. The conflict incoming commit is deleted from every named branch before merging by SHA, proving the bundle retains an otherwise unreferenced merge object. The original consumer index/workfiles stay untouched.

## Limits and concerns

No plugin consumer outcome, installed-client behavior, hosted issue/API write, real publication, fresh-agent isolation, interruption campaign or final plugin diagnosis is certified by helper self-tests. Capability fields conservatively remain false for unobserved agent/API/publication facilities. Source-loading/pinning is not an installed-plugin test. The assessor compares independently retained evidence but cannot certify the provenance of an arbitrary caller-created JSON value; independent actual command capture and agent behavior assessment remain mandatory.

Protected paths are omitted without reading them; recognizable token/credential URL content blocks evidence export. Unknown arbitrary secret bytes cannot be inferred perfectly, so the coordinator must keep protected information out of product/evidence artifacts. Historical protected paths, missing required objects and unsupported submodule state make recovery incomplete. Ignored noncredential workfiles, external machine state and credentials require separate retention if needed. All exports are local-only until the coordinator independently publishes and verifies them. Restoration is a documented coordinator procedure, verified in self-tests, not an automatic mutation helper. Package symlinks/submodules are unsupported and block pinning. Ambiguous remotes require resolution; helpers do not silently select origin or authenticate.

No SDD Manager skill/package change was made or proposed from these support self-tests. Any later independently demonstrated plugin defect requires its own diagnostic finding and accepted repair/new tested identity.

## Independent review corrections

Independent review of `fb5bbf1` reproduced actual support defects, retained in `/workspace/scratch/textstats-revision-009/task-2-review.md`. They were fixed in `24dc6095085d041efdaba8b4e9e18748ee0cf52b` (`fix(textstats): bind recovery effects and reject symlink destinations`):

- Pending push reconciliation previously borrowed current-branch publication despite an explicit different ref. It now gives the explicit ref precedence, verifies only that recorded target's equality/available ancestor containment, and retains unknown when ancestry is unavailable. A recorded pending repository different from the configured authorized destination remains unknown rather than claiming publication.
- Preparation previously resolved a dangling symlink workspace before checking occupancy, potentially creating its external destination. It now refuses an occupied lexical requested path before resolution; the destination remains absent.
- Dirty package pinning previously followed an ignored parent-directory symlink into external source bytes. It now rejects symlinked parents/escaping paths before reading package content.
- Credential URL filtering previously rejected standard username-only SSH transport. It now allows `ssh://git@host/path` while rejecting URL passwords, SSH query strings, HTTP(S) userinfo and credential query fields; no authentication or transport rewrite is attempted.

Added focused regression REDs before fixes. `task-2-review-red.log` contains four real assertion failures for dangling workspace, external dirty package, explicit different ref and unavailable target ancestry. `task-2-review-identity-red.log` contains two real assertion failures for SSH transport and pending repository mismatch. `task-2-review-relevant-green.log` records the 32-test relevant preflight/recovery suite passing after fixes. Original logs are preserved.

Added positive explicit-target ancestor coverage in `5fa622e` (`test(textstats): verify explicit push target ancestor containment`); it establishes the exact target's ancestor containment while current branch publication remains unpublished, proving reconciliation is target-specific. This is a coverage addition for implemented behavior, not claimed as a failing-first regression.

Final full-suite command after review corrections: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v` — **40 tests collected, 40 passed, zero errors/failures**. Output: `task-2-review-full-green.log`; `git diff --check` passed. No hosted writes, source credential reads, branch changes, plugin changes or report-root commits occurred. All previously documented limits remain.

## Scoped shallow-ancestry correction

The remaining T2-R1 recheck counterexample is corrected in `3b4049e3371bb32e3714235e01445ad80c7788df` (`fix(textstats): preserve unknown shallow ancestry effects`), based on `5fa622e31075c2dca62600e6861b7977b386e13e`. Only `scripts/core.py` and `tests/test_recovery.py` changed. The separately owned revision report and untracked evidence were preserved and excluded from the scoped commit.

Normal current-branch publication and exact pending-target reconciliation now share a conservative tri-state ancestry check. Exact equality and a successful positive ancestry proof still establish publication, including in shallow checkouts. A negative is accepted only when Git reports non-containment, the checkout is non-shallow, and traversal of both reachable commit histories succeeds. Missing endpoint objects, shallow negative results, traversal/ancestry errors and unavailable ancestry commands remain unknown. An actually absent target remains not observed; complete-history negatives keep their prior unpublished/not-observed behavior. Observation performs no fetch or consumer mutation.

The new regression uses a complete disposable source and bare local remote containing A→B→C, then a depth-2 clone containing both A and C whose shallow boundary at B hides that relationship. It independently proves ancestry in the full source and the negative ancestry result in the shallow clone, then exercises actual observation without recovery export. It requires unknown publication/containment/pending effect, preserves retry_safe:false, verifies refs/status/shallow metadata/object inventory are unchanged, and retains equality and visible B→C positive ancestry results in shallow history. Recovery bundle export/portability is explicitly outside this focused regression; existing export regressions remain covered by the complete suite.

Retained commands and outcomes (all logs under `/workspace/scratch/textstats-revision-009/`):

- RED: `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v acceptance.textstats.tests.test_recovery.RecoveryTests.test_shallow_checkout_with_both_endpoints_keeps_unproven_containment_unknown` — **1 collected test, 3 expected assertion subtest failures**, zero errors. `task-2-shallow-red.log` records the actual wrong unpublished/absent/not-observed results before production changes.
- Relevant GREEN: `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v acceptance.textstats.tests.test_recovery` — **17 tests collected, 17 passed**, zero failures/errors. Output: `task-2-shallow-green.log`.
- One final full-suite GREEN after the code/test changes: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v` — **41 tests collected, 41 passed**, zero failures/errors; exit 0. Output: `task-2-shallow-full-green.log`.
- `git diff --check` passed before committing; the scoped commit contains exactly the two owned paths.

Fixture publication/clone operations involved only temporary local repositories, cleaned by the test fixture. No hosted push, provider operation, consumer campaign, credential inspection, plugin/package change, branch switch or subagent delegation occurred. This corrects a support-tool defect, not a confirmed SDD Manager product defect; all previously documented campaign/installed-client/API/isolation limits remain.
