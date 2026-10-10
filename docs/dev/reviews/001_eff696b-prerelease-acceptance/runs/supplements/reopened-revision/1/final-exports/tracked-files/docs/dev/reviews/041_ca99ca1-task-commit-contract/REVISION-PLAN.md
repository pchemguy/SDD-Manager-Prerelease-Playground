# Task commit contract revision plan

## Campaign and scope

- Campaign: `041_ca99ca1`; full baseline: `ca99ca1750a1521c0045a220edaa2017fdab235f`.
- Working branch: `revision/041_ca99ca1-task-commit-contract`.
- Suspended parent and eventual return target: `revision/037_a6c42dd-prerelease-review`.
- Objective: make task subjects predictable and each task closure independently durable, with task result, verification evidence and owning checklist status committed together.
- Basis: [focused review](REVIEW-REPORT.md), R-001–R-004, and human-provided test-run examples.
- State: accepted and executed; V-001–V-004 complete with local/source verification. Final integration/publication and return are recorded in Git. Parent prerelease execution remains suspended.
- Exclusions: rewriting demo or plugin published history, automatic tracking reconstruction, release/version change, live test campaign, modification of earlier closed campaign packages and parent review resumption.

## Proposed contract

- Task-associated subjects use `[<owning-task-id>] <imperative description>`, for example `[T-028] Implement lock delay`, `[T-029] Implement SRS wall kicks` and `[T-031] Complete Phase 2 review`.
- The marker is the first subject content. There is exactly one owning task ID; no `feat(...)` or `docs(...)` prefix before it, trailing-only task ID, comma-separated IDs or task range. Preserve the owning list's project-wide identity and numbering convention. For numeric T IDs padded to at least three digits, the shape check is `^\[T-[0-9]{3,}\] [^\r\n]+$`; ownership, uniqueness and truthful content need separate checks.
- Complete one executable task at a time. Its closing commit contains that task's actual result, applicable tests/documentation, required verification evidence and its own first `[ ]` to `[x]` checklist transition. Do not batch closure of two tasks or use a later checkbox-only commit to finish ordinary initial closure.
- Review/report tasks obey the same contract; their substantive review/report and task completion status are their result. Parent checkboxes may accompany the final closing task when justified without counting as additional executable task closure.
- Authorized incomplete checkpoints retain an unchecked task and explicit partial state. Later scoped repairs and justified parent-only follow-ups identify the owning task/boundary and do not masquerade as initial closure or batch other task results. Multiple verified issue references do not authorize multiple executable tasks in one commit.
- Non-task preparation, maintenance, campaign action and merge commits keep their applicable formats; do not invent executable task IDs. Merge summaries may describe multiple tasks without becoming task-closing commits.
- Inspect subjects and actual staged/committed checklist/result/evidence composition before advancement. Preserve unrelated staging and shared-file changes. On discovered existing violations, report evidence and obtain any consequential history-repair decision; never automatically rebase/reset/force-push or replay implementation. Record authorized forward recovery accurately rather than claiming historical compliance.

## Ordered actions

| Action | Findings / owners | Intended outcome | Verification |
| --- | --- | --- | --- |
| V-001 | R-001, R-004; sdd-report drafts and entry | Canonical leading single-ID subject format, aligned valid/invalid examples and issue-reference distinction | Assess subject cases, exact ownership and non-task exceptions; remove contrary current examples within scope. |
| V-002 | R-002, R-004; sdd-implement entry, completion, execution and continuation | Explicit per-task closing commit composition, precommit/postcommit checks and retained partial/parent/recovery distinctions | Assess combined tasks, checkbox-only commits, review/report tasks, shared files, unrelated staging, interrupted completion and already published violations. |
| V-003 | R-003; sdd-manage entry, orientation handoff and Git integration owners | Visible coordinator invariant and bounded task-persistence audit before advancement/integration, linked to detailed owners | Trace direct/coordinated/resumed calls and phase/feature integration; a valid subject alone cannot pass an invalid composition. |
| V-004 | All; active campaign evidence and current navigation | Recheck coupled instructions, document observed verification/limits and finalize eligible child integration | Changed current links/Markdown, support suite, package inclusion, scoped Git diff and unchanged older closed records; explicit two-parent merge and publication only after execution authorization and successful checks. |

## Recheck scenarios

| Case | Required outcome |
| --- | --- |
| Single task result plus checklist and evidence | Accept truthful leading single-ID subject and atomic closure. |
| Conventional prefix or trailing-only ID | Reject task subject. |
| Multi-ID marker or task range | Reject task subject and multi-task closing composition. |
| Two task closures with a single valid leading ID | Reject composition despite valid subject shape. |
| Feature implementation then detached checkbox commit | Identify split closure; do not claim compliance from latest checkbox. |
| Milestone/phase review task | Commit substantive review/report and its task checkbox together. |
| Final task plus justified milestone/phase parent checks | Accept one executable task closure with eligible parent status. |
| Authorized partial task checkpoint | Retain unchecked state; no completion/issue closure claim. |
| Justified later parent-only status follow-up | Distinguish from initial task closure; no deferred task checkbox allowed by this exception. |
| Shared files or unrelated staged content | Inspect hunks and isolate ownership; block unsafe separation. |
| Several verified issues associated with one task | References allowed; no inferred multi-task ownership. |
| Campaign/preparation/merge without executable task | Retain applicable format; no fabricated task marker. |
| Existing published malformed or bundled history | Preserve history, report exact evidence and scoped recovery need; no automatic rewrite. |

## Persistence and stopping

Publish the campaign opening review/plan commit and verify containment before further work. Execution, if accepted, follows action-scoped source/evidence commits and publication; finish verification and integration into the suspended parent, then confirm return to that parent without resuming its prerelease review. Source/support checks establish instruction and tooling evidence, not live agent compliance. No new obligatory hook, state registry or external service is introduced by this plan.
