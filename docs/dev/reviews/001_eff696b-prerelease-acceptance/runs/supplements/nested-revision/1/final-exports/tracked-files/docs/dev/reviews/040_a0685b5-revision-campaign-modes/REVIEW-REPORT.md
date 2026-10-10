# Revision campaign modes review report

## Campaign and assessment

- Campaign: `040_a0685b5`; exact starting/reviewed source: `a0685b578045637f9f503aef39ab3a5bf0930456`.
- Working branch: `revision/040_a0685b5-revision-campaign-modes`; proposed revision integration target: `revision/037_a6c42dd-prerelease-review`. Parent 037 remains suspended; its reviewed candidate/findings are unchanged.
- Human request: open another revision campaign to define (1) a new revision campaign that suspends an active campaign and defaults to branching from/merging into its branch; (2) an explicitly requested reopening/amendment of the last closed revision campaign, eligible only when the active branch’s latest merge is that campaign’s final merge. An agent may suggest the second mode when relevant context is readily available.
- Evidence: focused current-source inspection and Git branch/merge identity inspection on 2026-10-10. No independent external research or live consumer assessment. This review uses the prompt-defined unit/criteria rather than a separate comprehensive review plan.
- State: focused review complete; two improvement findings Open. [REVISION-PLAN.md](REVISION-PLAN.md) is Proposed; no plugin-source revisions are executed at this checkpoint.

## Coverage and findings

| Unit / criteria | Inspected owners | Outcome |
| --- | --- | --- |
| U-001 / C-001–C-005 | sdd-manage review-and-revision, branch-management, workflows, coordination, Git workflows and SKILL.md; sdd-conventions review-campaigns/workflow-identity; sdd-report campaign-artifacts; root README/AGENTS orientation | Compared entry/routing, target selection, suspension/return, identity, closure/reuse and evidence retention. Existing explicit merge/publication and recovery rules remain suitable. Missing mode defaults and closure exception are R-001/R-002. |

Criteria: C-001 explicit mode selection/authority; C-002 branch/target and safe pending-work preservation; C-003 objective last-merge eligibility; C-004 stable identity/history and narrow reopening exception; C-005 verification, publication and parent return/stopping.

| Finding | Type | Priority | Baseline disposition |
| --- | --- | --- | --- |
| R-001 | Workflow-definition improvement | P2 | Open; proposed nested revision mode |
| R-002 | Workflow-definition/consistency improvement | P2 | Open; proposed reopened amendment mode and closure exception |

## R-001 — Define nested revision campaign targeting and suspension

- Location: review-and-revision entry and lifecycle; branch-management “Establish context and identity” step 2 and “Create or reuse”; workflow-identity naming/context; workflows revision scope/operation catalog.
- Observation: revisions can target an active phase or established branch, and steering explicitly returns to a paused implementation branch. There is no formal default for a new campaign nested within another active campaign, no explicit parent suspension/return contract, and no concise routing cue for it. Branch prefixes alone are correctly insufficient to establish ownership.
- Consequence: an agent can choose a generic main/default target, mistake child completion for parent completion, or resume parent work without a new continuation decision. This is a gap against the requested definition, not proof of an observed runtime failure.
- Correction: call it **nested revision campaign**, a revision mode rather than another core development workflow. Reserve a new identity; record parent campaign/branch, published source checkpoint, pending-work ownership and return boundary. Suspend parent execution, branch from the established parent checkpoint and target that same branch by default. Preserve explicit human target overrides and existing project-preparation gates. Verify/publish the child merge and return with the parent still suspended unless continuation is already explicitly authorized.
- Objective recheck: positive nested revision/feature parent scenarios resolve the immediate established parent target; review-only stops at report publication; dirty/unpublished/ambiguous states preserve valid work and do not reset, evade push gates, or silently target main. Child completion does not close/resume the parent.

## R-002 — Define narrowly eligible reopened campaign amendments

- Location: review-and-revision closure and blocked continuation; branch-management reuse/continuation; review-campaigns “Closed campaign records”; manager SKILL.md/root AGENTS frozen-record cues; report campaign-artifacts identity/stage/disposition rules.
- Observation: reuse supports the same scope and target, but does not establish closed-campaign reopening, latest-merge eligibility or proactive proposal versus authorization. Closed campaign instructions categorically freeze records after closure. This must gain an explicit exception for the human-selected reopened campaign, while retaining the general historical boundary.
- Consequence: agents may reject an authorized amendment, silently amend older closed campaigns, allocate duplicate identity for a related extension, or overwrite earlier completion evidence. A merge subject or directory number alone does not prove qualifying closure.
- Correction: call it **reopened campaign amendment** (short form: **campaign amendment**). Require close logical relation to the last closed revision campaign and verify its published final explicit merge is the active worktree branch’s most recent first-parent merge. Verify campaign/target/source/closure from retained evidence and Git parents/containment. Keep the original campaign ID, baseline, directory and branch; record a distinct reopening checkpoint and append stable new action IDs/results. Bring the branch forward to current target without replay/reset; execute only accepted amendment scope, explicitly merge again, verify/publish and close the amended campaign. Only the selected reopened records become editable.
- Objective recheck: explicit human reopening proceeds after eligibility/authority is established. Readily available related context may justify a concise suggestion, but does not authorize automatic reopening. Wrong latest merge, wrong target, unknown closure, unrelated scope or uncertain ownership cannot silently reopen an older campaign. Recommend a new campaign or resolve the missing fact; preserve historical observations, prior merge/check evidence and all other closed packages.

## Git evidence and interpretation

At the reviewed baseline, `git log --first-parent --merges -1 --format='%H%n%P%n%s'` returns merge `a0685b578045637f9f503aef39ab3a5bf0930456`, with target parent `f64e7eb3e6286f9d7ed74d74401e45ee24d3a6f1` and campaign 039 source parent `b15d9f60978e8fd13880d4b4f854fed4c7845965`. This anchors the mode discussion; it does not reopen 039 in campaign 040 or independently validate its historical contents. Prior package contents are outside this review.

“Latest merge” means the most recent merge on the active branch’s first-parent history, not the latest merge found anywhere in ancestry. Non-merge commits after that merge are possible under the human’s stated condition; preserve/include the current target checkpoint and inspect their effects on amendment scope rather than pretending they are absent. Another later merge fails the default eligibility test even if an older revision campaign merge remains an ancestor.

## Revision handoff and limits

The proposed plan establishes two explicit modes using existing manager, Git and reporting owners. Keep lightweight steering distinct; do not add a new skill, registry, workflow counter or transaction protocol. Source-defined scenario checks and support tests can verify wording/package integration; improved agent fidelity requires separate behavioral evidence. Publish this report/plan, then stop before product-source revision. No main merge, release, prerelease resumption or amendment of campaign 039 is selected.

## Subsequent accepted revision

The human authorized execution with “Execute campaign” and clarified that both modes must switch the worktree back to the interrupted campaign branch after closure. All three source actions are delivered; [REVISION-REPORT.md](REVISION-REPORT.md) records actual checks. R-001/R-002 are Verified for the accepted source definitions/source scenario rechecks, with no claim of live agent fidelity. Baseline observations and the original Proposed-stage assessment above remain retained. Final integration is into suspended campaign 037 only.

## Accepted amendment findings: integration summaries

Reopening assessment source: `e24f30c6d6da128b5c59e95cd3a782d6a7215335`. The human accepted the full suggestions for campaign integration summaries and summary-first highlights as an amendment to this campaign. Earlier baseline observations/results remain retained.

- R-003, P2 reporting improvement, Accepted: sdd-report object-drafts “Merge commit” requires branches, checkpoints, parents, checks/conflicts/limits but does not explicitly require campaign title, objective, reviewed scope and delivered outcomes as a self-contained release-ready summary. Define the contract for ordinary/nested/reopened revisions and feature/steering integrations; derive title from final scope and distinguish new amendment delta from previous delivery. Recheck producer entry/lifecycle and actual final merge message against those fields.
- R-004, P2 release-evidence improvement, Accepted: forge release-highlights range step 5/recipe and incremental instructions require all full messages; reporting/verify/forge entry repeat that expectation. Branch enumeration/tips cannot replace integrated history: refs can disappear/advance and ordinary tip commits need not summarize closure. Define summary-first editorial consumption over complete reachable range identities/parents, nested integration and direct-change coverage, outcome/amendment consolidation and targeted fallback. Recheck actual Git collection mechanics and source curation/coverage policy; mechanical success is not semantic acceptance.

Both findings are executed under V-004 in the amended [revision plan](REVISION-PLAN.md), with results in [REVISION-REPORT.md](REVISION-REPORT.md). No earlier campaign records are reviewed or repaired.

V-004 incorporates the human’s subsequent cumulative-summary/original-opening/per-opening-scope clarifications. R-003/R-004 are Verified for the source contract and collection mechanics documented in REVISION-REPORT; no independent semantic curation or live acceptance is claimed. The latest adequate cumulative summary is sufficient without routine earlier merge-body traversal; full identity/parent coverage and targeted fallback remain required.
