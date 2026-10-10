# Task commit contract review

## Campaign and assessment

- Campaign: `041_ca99ca1`; starting and reviewed source: `ca99ca1750a1521c0045a220edaa2017fdab235f`.
- Working branch: `revision/041_ca99ca1-task-commit-contract`.
- Source and return target: suspended `revision/037_a6c42dd-prerelease-review`; parent remains suspended.
- Request: open a new revision campaign from test-run commit examples and reflection, with a strict leading task identity and stronger commit composition and workflow enforcement.
- Evidence: current-source inspection plus human-supplied observations. Test-run repository, exact tested plugin version, diffs and original execution baseline were not supplied; the quoted agent reflection is an assessment, not authoritative policy or independently verified Git history.
- State: focused review complete; proposed revisions in [revision plan](REVISION-PLAN.md). Source repairs and integration are not yet authorized by opening this campaign.

## Findings

### R-001 — Task identity position is unconstrained

`skills/sdd-report/references/object-drafts.md`, Git commit, requires inclusion of the owning task ID but permits its position anywhere. Its example uses `Clarify filesystem utility ownership (T-041)`. Consequently `docs(review): [T-031] Complete Phase 2 review` satisfies the current identity placement rule. Leading `[T-031]` is a new stricter requirement, not an existing requirement established by the quoted reflection.

Correction: require exactly one owning task marker at the beginning of every task-associated subject, followed by a space and concise imperative description. No conventional-commit prefix before the marker, trailing-only ID or multi-task marker. Apply equally to production, documentation, tests and explicit milestone/phase review/report tasks. Recheck canonical drafts and representative valid/invalid subjects. Confidence: high; disposition: proposed revision.

### R-002 — Per-task persistence needs an explicit non-bundling contract

`skills/sdd-implement/SKILL.md`, steps 4–5, requires one-task-at-a-time execution and durable result/status/push before advancing. `references/completion-and-checkpoints.md`, Complete and commit each task, step 5, explicitly requires result and completion status together; integration states task persistence remains per task. Bundled task completion and detached checkbox-only closing commits conflict with these instructions. However the source does not literally say “cumulative multi-task commits are explicitly forbidden” as the reflection claims.

Correction: explicitly prohibit closing more than one executable task in a commit and prohibit detaching its first completion checkbox from the task result. Verify actual task-owned staged content, evidence and checklist delta before commit, then the committed contents before push/advancement. Recheck shared files, unrelated staging and review tasks. Confidence: high; disposition: proposed revision.

### R-003 — Higher-level coordination and integration lack a specific task persistence audit

The manager routes commit composition to sdd-report; Git integration checks coherent scope and acceptance. Neither entry instruction defines an explicit task-by-task audit of subjects and atomic result/status persistence. Relying only on conditionally loaded completion instructions leaves this failure easier to repeat or overlook.

Correction: expose the invariant at coordinator and implementation entry, with a canonical detailed owner rather than duplicated procedures; include bounded persistence checks in continuation and pre-integration review. An invalid existing history needs an accurate blocker/recovery decision, not automatic rebase, force-push or silent replay. Confidence: high; disposition: proposed revision.

### R-004 — Exceptions and recovery must remain distinguishable from task closure

`completion-and-checkpoints.md`, Parent completion and stopping, permits parent-status follow-ups. `task-execution.md` permits explicitly authorized partial checkpoints. The reporting owner permits multiple issue references; this does not establish multiple task ownership. A blanket “each task has exactly one commit ever” would contradict these legitimate cases and obscure correction of existing violations.

Correction: define one task per closing commit while retaining clearly identified authorized partial checkpoints, task-specific repairs and parent-only follow-ups; none can detach or batch initial task closure. Preparation, campaign actions and merge commits without an executable task must not invent task IDs. Existing published violations are reported and reconciled through explicitly authorized recovery; cosmetic subject changes alone do not repair composition. Confidence: high; disposition: proposed revision.

## Limits and stopping boundary

The quoted combined feature commit and separate multi-task checkbox commit illustrate a reported composition failure; subjects alone cannot prove actual diffs or completion evidence. No demo Git history is rewritten, no hosted tracking is reconstructed, no plugin source is changed and no live consumer test is claimed. This campaign stops after publishing its review and proposed plan for human consideration.

## Execution dispositions

The human authorized execution on 2026-10-10. R-001–R-004 were revised through V-001–V-003 and rechecked under V-004; the baseline observations above remain unchanged. Current source walkthroughs, seven subject examples, independent hypothetical application and support/package checks are recorded in [revision evidence](REVISION-REPORT.md). Verification applies to the instruction contracts and named checks, not live agent compliance or the supplied demo history.
