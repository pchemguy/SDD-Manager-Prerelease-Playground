# Requested tracking fidelity review

## Campaign and conclusion

- Campaign: `038_d6218f1`; [scope and supplied result](README.md); [revision plan](REVISION-PLAN.md).
- Starting baseline: `d6218f1458b3805ecd27f6be6942162ec4a815ed`; exact current product source equivalent to `a6c42dd754843abf9bafca7dee2aee9e733b046a`, version `0.15.0`.
- Working branch: `revision/038_d6218f1-tracking-fidelity`; parent/target: suspended `revision/037_a6c42dd-prerelease-review`. Opening checkpoint `739b7ec1fae754de65cbf2bd728bce546a3e64ab` was pushed and exact remote readback matched before this assessment checkpoint.
- Reviewer: coordinating assistant, 2026-10-10 UTC; evidence mode: current source/composition inspection and human-supplied conversation excerpt. No independent consumer execution or external corroboration.
- Baseline state: Focused review complete; two instruction-fidelity improvement findings and one evidence gap were Open, with a Proposed plan. The later human execution instruction and actual dispositions are recorded in [REVISION-REPORT.md](REVISION-REPORT.md); baseline observations below are retained.

**The requirement already exists.** An explicit request to enable and maintain tracking confirms the decision; eligible phase projection and readback precede its first task. The supplied request is sufficient and needs no repeated user reminder or more emphatic prompt. If the reported chronology is accurate and the tested source contained these instructions, beginning tasks without that projection or an actual human override breached the existing workflow.

The actionable weakness is how that requirement reaches the executing agent: it is distributed across references, appears less prominently than local preparation/QC/push rules, and uses “active” for both selected tracking and already-created hosted state. Unqualified outage exceptions can then be read too broadly. Improve the explicit decision → observed projection → execution handoff, rather than adding another optional feature or a repeated-approval gate. These are grounded wording recommendations; the agent's retrospective explanation does not prove their causal role or that a rewrite will prevent the failure.

## Coverage

| Unit / criteria | Current source assessed | Outcome and boundary |
| --- | --- | --- |
| U-001 / C-001–C-006 | sdd-manage SKILL.md; tracking-decision, phase-activation, coordination, workflows, branch-management and examples; sdd-implement SKILL.md, startup-and-continuation and completion-and-checkpoints; sdd-forge SKILL.md and github-projection; shared backend-object-lifecycle. | Compared both sides of entry, preparation, activation, execution, completion, outage and next-phase handoffs. The mandatory invariant is present; R-001/R-002 identify fidelity weaknesses and R-003 limits attribution/verification. |

Read current root AGENTS.md and campaign identity/report conventions for this review. The local repository source is the reviewed authority; the installed sdd-manage copy is older in unrelated Markdown/prerelease/publication details and is not substituted for the pinned source. No closed campaign contents, demo repository, credential value, hosted inventory or consumer tool trace was loaded. The imported credential is excluded from retained evidence.

| Finding | Type | Priority | Disposition |
| --- | --- | --- | --- |
| R-001 | Instruction-fidelity improvement | P2 | Open; proposed |
| R-002 | Instruction-fidelity improvement | P2 | Open; proposed |
| R-003 | Evidence gap | P2 | Open; attribution and behavioral verification unresolved |

## R-001 — Put the requested-tracking gate at the execution entry

| Field | Assessment |
| --- | --- |
| Baseline evidence | `skills/sdd-manage/references/tracking-decision.md`, opening table begins with token/no-choice and merges confirmation with already-active state in its second row; explicit request equals confirmation appears in the following paragraph. `phase-activation.md`, step 3 says “When tracking is active” before projection. Manager SKILL.md step 3 dispatches responsible skills while step 4 establishes tracking; phase activation is a routing-table reference rather than a named pre-execution step. Executor SKILL.md step 4 explicitly loads document QC but omits an equivalent direct tracking/activation prerequisite; its startup reference supplies that gate later. |
| Existing correct safeguards | tracking-decision already says the explicit request is confirmation and inactive PLAN prose is no user decline. Phase activation and shared backend lifecycle already demand complete readback before the first task. Forge projection already covers all eligible phase objects, review units and associations. There is no missing general obligation to invent. |
| Reader consequence / confidence | An agent following the short executable protocol can prioritize preparation/QC/local task work and treat an unprojected requested tracker as “not active,” never reaching its enabling procedure. High confidence in the distribution/prominence observation; only a hypothesis about this consumer's cause. |
| Proposed correction | Make explicit request the first decision-table branch: choice confirmed/requested, projection pending until observed. Distinguish optional selection from required fulfillment after selection. Add concise linked mandatory loading/gate cues at manager dispatch and executor readiness, including direct calls/resume; use requested/confirmed scope rather than object existence as the trigger. Keep detailed provider procedure in forge and phase policy in its existing owner. |
| Objective recheck | Fresh consumers given the original broad project/tracking request and ordinary accepted-state handoff must carry the request without another activation question, complete/read back the eligible label/all milestones/all task issues and initial associations before task edits or task test execution, and project no future phases. Also exercise token-only, explicit decline and selection/preparation-only controls. Text presence alone cannot mark fidelity Verified. |
| Disposition / dependency | Open; proposed V-001. No source edit or human acceptance. |

## R-002 — Bound local continuation to previously satisfied activation

| Field | Assessment |
| --- | --- |
| Baseline evidence | `skills/sdd-implement/references/startup-and-continuation.md`, startup tracking paragraph says not to “block independent local work solely because hosting remains unavailable.” `completion-and-checkpoints.md`, Complete and commit steps 3/7 permit local commit/completion with unresolved references/closure when hosting is unavailable. Their local clauses do not explicitly constrain the initial projection gate. In contrast, `phase-activation.md` step 3 blocks partial/unavailable projection absent human override; backend-object-lifecycle explicitly limits independent execution to an already activated phase and requires added work projected before execution. |
| Reader consequence / confidence | A separately loaded execution/completion reference can overgeneralize an outage exception into “do local work and synchronize later,” including a phase never activated or a newly added task never projected. Canonical full-source policy resolves this; the local excerpt's boundary is insufficiently prominent. High confidence in the unqualified wording, moderate confidence that it increases bypass risk; no observed API outage is established by the supplied result. |
| Proposed correction | Qualify the existing allowances at their points of use: preserve/commit/push already verified work; independent further execution is allowed only inside an already verified activated phase, for projected tasks with satisfied dependencies. Required initial/added-work projection, dependent review/closure and next-phase transitions stay blocked when their evidence is missing/unknown. No silent local-only downgrade; an actual explicit human override records its scope. Add omission recovery distinct from late user confirmation: retain work, reconcile the missed gate before further affected implementation, do not replay tasks or claim earlier compliance. |
| Objective recheck | Compare initial partial/failed/unknown projection with outage after full activation. First case stops affected task edits/tests; second may retain local results and continue only eligible independent projected work, with closures pending. Unprojected added work and dependent next phase stay blocked. Resume reuses exact objects and retained commits, reads uncertain effects before retry, and does not fabricate earlier tracking or repeated user consent. |
| Disposition / dependency | Open; proposed V-002 after V-001. No requirement to halt every inspection/preparation action during a provider outage. |

## R-003 — The reported explanation is not a verified root cause

| Field | Assessment |
| --- | --- |
| Baseline evidence | Supplied conversation names two reference paths and admits omission, but supplies no tested package SHA/version, exact loaded-source record, command sequence or provider observation. It reports Phase 1–3 delivery and tracking omission; neither is independently inspected here. Current examples emphasize token-only choice, late confirmation and closure outages; acceptance A-003 explicitly asks the consumer to maintain tracking as a separate selected operation rather than proving that a broad seed request survives preparation into implementation. |
| Consequence / confidence | Current source permits a grounded usability review, but not attribution of the original failure to this exact version, a tooling blocker or a particular sentence. No reliable numerical fidelity improvement can be claimed. Confirmed evidence absence in this review; no claim that existing acceptance materials are useless or that the consumer had not loaded the references. |
| Proposed investigation | Preserve sanitized input and first attempt. If available, obtain exact tested source/loaded entries and actual task/provider chronology in a separately scoped inspection. For proposed wording, execute a behavioral comparison with isolated consumers/assessors and equivalent valid inputs; include the broad initial request as a handoff-retention scenario. Do not feed expected routing or this report to consumers. |
| Objective recheck | Retain source/package/runtime/handoff identities, first task/edit/test and projection/readback order, missing/partial/unknown cases, user decisions, first outcomes and interventions. Compare applicable current and revised source independently. Record unavailable facilities and failed attempts; passing local support or keyword checks is not fidelity acceptance. |
| Disposition / dependency | Open; V-003 verification design can be prepared, but live consumer/dedicated hosted target execution requires its own authorized facilities/scope. |

## Concrete proposed wording

These passages are review proposals for the owning files, not applied source changes or new mandatory artifact formats. Preserve the existing canonical invariants and replace weaker local phrasing instead of copying the complete policy into every skill.

For tracking-decision, before the token-only case:

> An explicit request to enable and maintain labels, milestones and task issues confirms tracking for the named repository and scope immediately. Carry that decision even when no hosted objects exist yet. Record the decision as requested/confirmed and projection as pending until verified; do not ask for the same activation approval again. Tracking is optional to select. Once selected, fulfill its activation and lifecycle requirements before dependent execution.

For manager dispatch and the executor's readiness step:

> Before handing off or starting phase task execution, load and apply tracking-decision and phase-activation. When tracking was requested or confirmed for this scope, require verified eligible-phase projection before task implementation edits or task test execution: its phase label, every milestone including review milestones, and every task issue including review tasks, with initial associations. Missing, partial or unknown projection blocks affected execution; return the concrete missing evidence to the manager. A local TASKS checklist, an implementation branch or an “inactive” note does not satisfy this gate. Publish retained verified commits first; preserve unfinished work while resolving the missed prerequisite.

For execution/completion outage clauses:

> Hosting unavailability does not erase verified local results. Preserve and publish already verified work and report pending hosted closure. Further independent task execution is permitted only in an already verified activated phase, for tasks whose required projection and dependencies are satisfied. This allowance does not waive initial or added-work projection, dependent review/closure or next-phase gates. Local-only continuation across an unmet tracking gate requires an actual explicit human override for that scope.

For an ordinary existing handoff, a compact example using actual discovered facts:

```text
Tracking decision: requested by the human for the named repository and lifecycle scope.
Phase projection: pending; no verified hosted inventory yet.
Next permitted action: forge projection/readback after accepted preparation; task execution blocked.
```

After successful projection, replace pending with verified object identities/associations or links and the eligible task scope. Use existing project/handoff evidence; no new tracking file, journal, checklist task, schema or second registry. Do not require fresh full readback for every task when still-applicable confirmed evidence suffices; recheck affected state on material change or uncertainty.

## Scenarios, verification and stopping

Source assessment confirms the stated policy and wording weaknesses; all behavioral scenarios above are **Not run** in this campaign. No API fault, successful hosted projection or consumer recovery is simulated as an observed outcome. Static source/link/diff checks verify the report's targets and scope only. No source code or package changed, so the 113-test support suite was not rerun for this report-only checkpoint.

The proposed plan preserves human review of newly created documents, preparation integration, optional tracking choice, credential protection, exact issue identity, eligible-phase-only projection, task/phase closure ordering, per-commit publication and scope limits. Git publication and API capability remain separate. The initial broad project request is not treated as acceptance of all preparation documents or permission to execute every phase.

Publish this report and proposed plan, then stop before source changes. Campaign 037 remains suspended with its original candidate/findings. Any accepted product wording revision creates a changed candidate requiring affected prerelease reassessment when 037 resumes; this focused source review neither clears its blockers nor claims runtime acceptance.

## Subsequent authorized execution

The human accepted execution on 2026-10-10. All three source/scenario-preparation actions are delivered with local checks; see [REVISION-REPORT.md](REVISION-REPORT.md) for evidence and integration scope. R-001/R-002 are Revised with behavioral rechecks pending; R-003 stays Open. This changes the initial review stopping boundary for the accepted source revision, without clearing the suspended prerelease assessment or authorizing live demo operations/release.
