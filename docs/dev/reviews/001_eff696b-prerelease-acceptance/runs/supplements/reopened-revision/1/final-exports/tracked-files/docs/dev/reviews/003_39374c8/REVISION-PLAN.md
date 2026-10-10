# SDD Manager revision plan

**Campaign:** `003_39374c8`. Current record: `docs/dev/reviews/003_39374c8/REVISION-PLAN.md`. Established finding IDs and baseline evidence are retained. The completion-time archive instruction below records the original executed procedure; new campaigns write directly into their stable review directory.

## Baseline and scope

- **Source baseline:** `39374c8ae60f92ce8dd874774ed69ab3cb15c459` (`39374c8`), plugin version `0.14.1`.
- **Independent input:** [critical review](REVIEW-REPORT.md), added at this baseline. Its observations are review hypotheses; it supplies no exact reviewed commit, attached validator output, or reproduced failure fixtures.
- **Prior verified revisions:** [systematic review and follow-up](../002_81011e7/REVIEW-REPORT.md). Preserve SDD-R-001 and SDD-R-002 corrections and their historical evidence.
- **Purpose:** Address useful failure-handling clarifications and adopt branch-based workflow boundaries with default, explicit merge commits.
- **Execution status:** SDD-V-001–007 implemented and validated; explicit campaign merge `37ea99359e9b34a202f7e922b0d1b1bc8e62cf3f` published to `feature/architecture-revision`. Actual evidence and limits: [revision report](REVISION-REPORT.md). This completed plan is archived.
- **Revision IDs:** `SDD-V-001` through `SDD-V-007`, stable within this plan and subsequent implementation reports. These are planned revisions, not newly verified defects.

## Accepted decisions

- Git commits remain checkpoints; no transaction journal, lock file, mandatory evidence JSON, or separate recovery skill.
- Preserve valid interrupted work and unrelated staged/unstaged changes. Dirty state alone never authorizes reset, cleanup, or rollback.
- Commit and push completed task work on its working branch. Merge at the verified workflow boundary, not after every task commit.
- Feature and steering workflows merge into their established targets by default after successful verification. Every successful integration requires an explicit merge commit; use `git merge --no-ff`, never a fast-forward or squash substitute.
- Main implementation uses a coherent selected range or milestone as its working-branch boundary. The authorized range, rather than an arbitrary number of commits, determines its finish.
- Feature document reconciliation occurs on the feature branch before final verification and merge when incorporation is within the requested workflow. Git integration and document integration remain distinct responsibilities.
- Steering merges into the paused implementation branch and then returns control to the human. It never resumes the main task list automatically.
- Hosted task closure continues to describe verified task work on its stated branch; it does not establish integration into a target or default branch.
- Ordinary filesystem and Git operations remain portable core behavior. Worktrees are optional isolation facilities; no host-specific hook or mandatory client API is introduced.

## Independent report disposition

| Report section | Disposition | Planned response |
| --- | --- | --- |
| 4.1 — Cross-skill rollback | Partial concern: interruption can leave document amendments incomplete. A new journal and automatic rollback are not accepted. | SDD-V-001 / SDD-V-004: isolate selected work on a branch and define scoped document continuation before publication. |
| 4.2 — Evidence fragmentation | Claim of guaranteed fragmentation is unsupported. Existing task evidence and sdd-report already provide a contract. | SDD-V-006: explicit fallback to the owning task entry or its existing linked evidence; retain project-defined locations. |
| 4.3 — Steering dead ends | Existing steering already repairs failures until verified or concretely blocked; human control is intentional. | SDD-V-003: explicit continuation of the same blocked amendment and merge only after verified resolution. |
| 4.4 — Provider failures | Useful missing specificity for rate limits, transient failures, offline states, and uncertain write results. | SDD-V-005: provider-specific failure classification and bounded retry/reconciliation. |
| 4.5 — TDD exception visibility | Exceptions and missing RED evidence are already reportable; mechanical proof of execution order is outside this instruction package. | SDD-V-006: persist applicable exceptions and evidence gaps without pretending that reporting proves strict TDD. |

## Responsibilities and branch contract

| Capability | Responsibility |
| --- | --- |
| sdd-manage | Establish branch/target identities and workflow boundary; coordinate branch creation/reuse, final Git integration, publication, and reporting. |
| sdd-orient | Observe branch, HEAD, relevant worktree state, task evidence, and unfinished workflow context without mutation; report ambiguity. |
| sdd-implement | Push outstanding commits before other execution work; implement the selected range; own task completion, commits, and pushes; request final integration at the boundary. |
| sdd-steer | Own the commanded amendment, its continuation, document/code/test changes, verification, commits, and pushes; coordinate integration into the paused branch and stop. |
| sdd-integrate-feature | Reconcile selected document owners on the working branch; preserve executable ownership and durable pending reassessment; do not equate document reconciliation with Git merge. |
| sdd-verify | Assess working-branch acceptance and the merged result; report failures and evidence without owning production repairs or Git integration. |
| sdd-report | Compose task, amendment, and merge messages and completion summaries, including branch identities and evidence limits. |
| sdd-forge / GitHub reference | Own hosted object reconciliation and provider-specific response handling; no implicit PR creation or merge capability. |

The ordinary handoff identifies workflow kind, authorized range or amendment, working branch, target branch, starting checkpoint, current HEADs, and pending work. Git and existing documents/evidence retain durable context; do not add a parallel state store. If the target cannot be recovered unambiguously in a fresh session, report the missing decision rather than defaulting to the repository's default branch. Branch naming follows project policy; define a concise fallback and collisions/reuse checks without treating a branch name alone as proof of ownership.

## Ordered revisions

### SDD-V-001 — Establish branch and merge lifecycle

- **Targets:** sdd-manage coordination/workflows and sdd-orient inspection/handoff; add a focused Git workflow reference where useful.
- **Procedure:** Establish eligible worktree, authorized scope, existing pending-work ownership, working branch, target, and checkpoint before mutations. Reuse a suitable branch on continuation; create a branch before new scoped changes. An optional separate worktree keeps the target available without relocating unrelated dirty work.
- **Startup:** Preserve implementation's push-first rule on the current established branch before branch creation or task execution. Creating a branch must not bypass unresolved outstanding commits, divergence, or destination ambiguity.
- **Integration:** Refresh target state, preserve unrelated work, and perform a non-fast-forward merge. A useful procedure is `git merge --no-ff --no-commit` followed by merged-state verification and an explicit merge commit. Account for Git's already-up-to-date case: do not fabricate a boundary commit or duplicate an already completed merge.
- **Failures:** Conflicts, failed checks, missing access, protected target policy, or ambiguous ownership block completion. Preserve and report merge state; repair only within the authorized scope. No force-push, automatic hard reset, implicit target substitution, or invented PR workflow.
- **Publication:** Push the verified merge commit to the established target remote and verify containment. A local merge or successful task-branch push alone is not published integration. A failed target push retains the merge commit and reports pending publication.
- **Acceptance:** Disposable Git fixtures cover fresh branch creation, continuation, dirty/staged preservation, fast-forwardable history that still produces two-parent merge commits, divergent target history, already integrated work, conflicts, failed merged checks, target push failure, and unavailable/protected destinations. Successful cases identify and verify both branch and merge commits on local bare remotes.

### SDD-V-002 — Integrate branch boundaries into task and feature implementation

- **Targets:** sdd-implement startup, selection, execution, and completion references; sdd-manage workflows; sdd-report object/completion drafts; GitHub issue lifecycle wording where needed.
- **Procedure:** Select one owning task list and bounded range. Execute and push each completed task on the working branch. Do not merge per task. At the completed range boundary, coordinate required document reconciliation, final acceptance, explicit merge, merged-state verification, and target push through SDD-V-001.
- **Feature scope:** Reuse the established feature branch through preparation and execution. Include selected feature-document incorporation before the final merge; do not silently broaden a one-task request into full feature incorporation or declare an unfinished feature complete. Report unmet integration prerequisites and retain needed feature sources.
- **Evidence:** Task commits retain stable IDs and verified issue associations. Merge messages identify the feature, milestone, or selected range and its aggregate verification. Report task completion, branch completion, target integration, and publication separately.
- **Acceptance:** Multi-task fixtures demonstrate multiple task pushes and exactly one successful boundary merge. Main and feature scopes retain unique executable task ownership, pending reassessment, historical evidence, and selected stop conditions. A narrow feature request does not merge or incorporate unrelated unfinished work.

### SDD-V-003 — Isolate steering and define blocked-amendment continuation

- **Targets:** sdd-steer objective/impact, amendment execution, verification/stop; coordinator routing and examples.
- **Procedure:** Start or reuse an amendment branch from the paused implementation checkpoint. Directly update existing documents, code, tests, and docs within the human-commanded amendment; create no new feature overlay. Commit and push the verified amendment, merge into the paused implementation branch with an explicit merge commit, verify and push the target, then stop.
- **Blocked continuation:** Repair amendment failures within scope until verified or concretely blocked. Report amendment/target branches, pending changes, failed conditions, existing evidence, and needed decision or facility. A later human command to continue the amendment resumes its branch and unfinished scope; it neither selects another main task nor starts a new amendment implicitly.
- **Checkpoint protection:** Before integration, the paused target remains at its established checkpoint. If integration itself is blocked, identify the exact merge/worktree state; do not claim it is a completed usable checkpoint or erase valid work automatically.
- **Acceptance:** Fresh-session fixtures cover successful reduction, failing verification repaired within scope, environment blockage followed by commanded continuation, ambiguous amendment ownership, and conflict during integration. No main-task continuation occurs after amendment merge.

### SDD-V-004 — Define interrupted document-integration continuation

- **Targets:** sdd-integrate-feature incorporation reference; sdd-orient and coordinator handoffs where necessary.
- **Procedure:** Inspect actual documents and diff against the established Git checkpoint and accepted feature sources. Identify which selected owners were amended and which remain inconsistent. Resume reconciliation on the existing working branch within the selected scope; do not rerun implementation, create duplicate executable tasks, or propagate unsupported parent completion.
- **Invariants:** Preserve stable IDs, one executable owner per task, historical evidence, pending completion reassessment, out-of-scope lists, and source documents still required by active work. Do not publish or merge incomplete document reconciliation as successful integration.
- **Limits:** Branch isolation protects the target from unpublished partial edits; it does not make working-branch edits transactional or automatically resolve ambiguity after a crash.
- **Acceptance:** Interrupt after SPEC amendment but before TASKS reconciliation, then resume in a fresh session with repository artifacts only. Also exercise SPEC-only scope, duplicate IDs, partially transferred task ownership, and retained source links. Verify coherent selected documents before merge; blocked cases remain reported and preserved.

### SDD-V-005 — Expand GitHub operational failure handling

- **Targets:** primarily sdd-forge/references/github.md; projection/lifecycle and shared coordinator protocol only where handoffs require alignment.
- **Classification:** Distinguish provider-indicated credential/permission failures, rate limits, transient service failures, connectivity/offline failures, invalid requests, and uncertain write results. Status 403 is not invariably a credential failure; honor the indicated cause. Preserve the established suitable-token request path through sdd-manage where applicable.
- **Retry:** Consult current official GitHub endpoint and rate-limit guidance during implementation. Use available retry/reset information, bounded retry attempts, and stop/report when progress is blocked. Do not replace credentials to treat a network outage or retry indefinitely.
- **Uncertain writes:** Re-read affected objects and stable identities before retrying creation, association changes, comments, or closure after an interrupted/ambiguous response. Preserve successful independent results and report remaining differences without duplicate hosted effects.
- **Local continuity:** Hosted unavailability does not erase verified local completion; report synchronization as pending and reconcile the maintained scope when access returns.
- **Acceptance:** Controlled provider fixtures cover permission403, rate-limit403/429, server failure, offline reads, timeout after successful creation or closure, and partial multi-object projection. Observe bounded attempts, sanitized reports, re-read-before-retry, no duplicate objects/comments, and correct unresolved-state handoff. Live hosting is separately scoped, not required for these tests.

### SDD-V-006 — Make evidence fallback and TDD exceptions explicit

- **Targets:** sdd-verify execution/evidence; sdd-tdd cycle; implementation/steering completion; sdd-report presentation references.
- **Fallback:** Honor project-designated evidence locations. Otherwise persist concise evidence beside the owning task or in its existing linked record. Taskless maintenance reports use the ordinary change/commit report. Introduce no mandatory evidence file or schema.
- **Facts:** Record applicable task/change identity, implementation state, check command, observed outcome, condition coverage, and material limitations. Preserve outputs where necessary to review consequential claims. Prior evidence stays identified as historical and must be applicable before reuse.
- **Exceptions:** Record the concrete test-first limitation, applicable policy or user authorization, what evidence was actually obtained, and remaining gaps. Missing historical RED is not a performed RED run; characterization and isolated sensitivity demonstrations are labeled accurately. Do not delete existing code to reconstruct history.
- **Acceptance:** Consumers locate task evidence without chat history in projects with and without designated records; sdd-report preserves the facts and gaps. Authorized exceptions and missing RED remain visible in durable task/change evidence and relevant reporting. No mechanical enforcement or proof-of-order claim is introduced.

### SDD-V-007 — Validate composition and document workflows

- **Targets:** README, CAPABILITY-MAP, workflow examples, all affected entry/reference links, and revision evidence.
- **Procedure:** Document main-range, feature, steering, interrupted integration, and provider-outage workflows. Align branch versus document integration terminology, default merge authorization, explicit merge commits, target publication, and human-controlled steering stops. Remove conflicting instructions that categorically prohibit necessary Git merges; keep PR operations outside the present backend scope.
- **Regression:** Recheck optional-write suppression, push-first execution, preserved staging, durable completion reassessment, taskless messages, feature/main ownership, older pending hosted issues, and default-branch versus feature-branch completion claims.
- **Validation:** Run changed-skill validators, plugin validator and inspector, heading/template spacing, local links, skill references, metadata/icon consistency, and credential-pattern checks. Exercise actual isolated branch/merge workflows with local bare remotes and fresh consumers where continuity is material.
- **Reporting:** Separate structural results, executed Git/provider fixtures, consumer dispositions, and untested installed-client/live-provider behavior. Record commands, observed outcomes, revision commits, blockers, and limitations; do not promote plan acceptance cases to observed results.

## Execution and persistence checkpoints

1. Execute SDD-V-001 through SDD-V-007 in order. Keep each revision bounded; adjust later targets only when findings demonstrate a dependency.
2. After each revision, update its stable-ID evidence record in a companion revision report, run appropriate checks, commit source and evidence together, push with the established saved credential, and verify remote containment before the next revision.
3. The future source revision campaign itself follows the accepted branch protocol: create/reuse a scoped working branch targeting the established development branch, push per-revision commits, and perform one verified explicit merge at campaign completion. This planning-only update does not initiate that source campaign.
4. A blocked step reports successful independent work, retained Git state, and the exact unmet condition. Continue independent authorized work only where the dependency permits it.
5. After the final validation and verified merge publication, move this completed plan and its companion revision report to `docs/dev/revision_plans/`, adjust links, and commit/push the archive checkpoint. Preserve the independent report and prior review archives as evidence.
6. Return direct GitHub links to the revised sources, plan/report, working branch, and merge commit, with actual push state and remaining limits.
