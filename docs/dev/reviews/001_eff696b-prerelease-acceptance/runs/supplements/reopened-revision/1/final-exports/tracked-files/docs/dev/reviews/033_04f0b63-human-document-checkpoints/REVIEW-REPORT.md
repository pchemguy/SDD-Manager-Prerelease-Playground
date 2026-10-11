# Human review checkpoints — baseline review

## Campaign and assessment

- Campaign: `033_04f0b63`; directory: `033_04f0b63-human-document-checkpoints`.
- Starting and reviewed source: `04f0b63ed923ff97860a3205cf369b3421d41665`, SDD Manager **0.15.0**.
- Working branch: `revision/033_04f0b63-human-document-checkpoints`; eventual integration target: `main`.
- Date/reviewer: 2026-10-09, coordinating inline agent.
- Request: open a revision campaign and first review how mandatory checkpoints are currently articulated. The user explicitly clarified that these are **human review checkpoints** after creation of each PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, layout and TASKS.
- Current stage: baseline review complete; source revisions not started. Findings are relative to the clarified requested policy, not an assertion that an earlier human-checkpoint policy was violated.
- Evidence: current-source inspection and source-level handoff walkthroughs. No live agent/client behavior was executed; no independent reviewer or external research was used.

**Conclusion:** the source has agent-owned QC, accepted-input language and Git persistence/integration gates, but does not explicitly require a human review pause after creation of any of these seven roots. Generic authorization language permits already-authorized transitions to continue, so human acceptance cannot safely be inferred from the existing QC gates.

## Scope and criteria

The focused review is one unit, U-001, covering design owners, downstream authoring owners, manager transitions, readiness/reporting, startup observation and consumer instructions. No separate review plan is required for this prompt-defined scope.

| Criterion | Expected articulation | Result |
| --- | --- | --- |
| C-001 | Explicit human checkpoint after creation of each named root, before dependent creation/use. | Missing; R-001. |
| C-002 | Agent QC/Ready and human acceptance are distinct conditions. | No explicit preparation acceptance distinction; R-001/R-003. |
| C-003 | Broad project/repository-operation authorization does not silently satisfy a future document review. | Generic continuation language is unreconciled with the requested mandatory pause; R-002. |
| C-004 | Presentation, decision scope and continuation are tied to the actual document reviewed. | No common human-checkpoint handoff/resumption contract; R-003. |
| C-005 | Direct calls, existing accepted inputs and applicable feature deltas preserve equivalent checkpoint behavior. | Existing QC reuse/scope rules are useful, but no human-checkpoint coverage is defined; R-001/R-003. |

Prior closed campaigns were not read or edited. Identity allocation inspected paths/ref names and the current navigation index only; local and live remote discovery showed highest allocated numbered campaign 032 and matching main baseline. This is a source-policy review, not a TextStats campaign, client acceptance, code review or release operation.

## Document boundary coverage

The table follows the existing dependency order; the user's enumeration does not itself change SPEC-before-PLAN ownership. PLAN and layout are separate named human checkpoints even when coordinated by one skill. Focused children are part of their root's presented scope, not an implied checkpoint after every child file.

| Root / owner | Current articulated review/readiness | Mandatory human pause after creation |
| --- | --- | --- |
| PROJECT / sdd-design | Architecture reference defines the brief. Exploration distinguishes user decisions, assumptions and silence; its handoff concerns readiness for architecture. | Not specified for the created PROJECT document. |
| ARCHITECTURE / sdd-design | Architecture Review checks responsibilities, dependencies, constraints, unknowns and root/child navigation; stops when only architecture was requested. | No universal human review/acceptance step before decomposition. |
| DECOMPOSITION / sdd-design | Decomposition Review checks responsibilities, dependencies, seams and readiness for SPEC; unresolved design decisions are surfaced. | No human acceptance step before SPEC. |
| SPEC / sdd-specify | Mandatory SPEC/design QC, bounded correction/recheck and adjacent SPEC-REVIEW-REPORT; unresolved issues block PLAN. | Ready means owner QC, not a required human decision. |
| PLAN / sdd-plan | Mandatory PLAN/SPEC QC and adjacent PLAN-REVIEW-REPORT, including relevant layout; unresolved issues block TASKS. | No pause to review the created PLAN separately. |
| layout / sdd-plan | Material layout changes enter affected PLAN QC. Focused layout requests preserve selected-path/report authorization limits. | No distinct human review point; it can be bundled into PLAN/layout preparation. |
| TASKS / sdd-tasks | Mandatory TASKS/PLAN QC and adjacent TASKS-REVIEW-REPORT before implementation or hosted projection. | No required human acceptance after creation before those dependents. |

## Findings index

| Finding | Type / priority | Disposition |
| --- | --- | --- |
| R-001 | Requested-policy gap / High | Open; seven mandatory human boundaries need explicit coverage. |
| R-002 | Coordination ambiguity / High | Open; automatic continuation must respect mandatory human checkpoints. |
| R-003 | Decision/evidence gap / Medium | Open; human review handoff, accepted scope and resumption need a common contract. |

### R-001 — Document reviews do not establish mandatory human pauses

**Baseline evidence:** [skills/sdd-design/SKILL.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-design/SKILL.md); [skills/sdd-design/references/exploration.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-design/references/exploration.md#handoff); [skills/sdd-design/references/architecture.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-design/references/architecture.md#review); [skills/sdd-design/references/decomposition.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-design/references/decomposition.md#review); [skills/sdd-conventions/references/development-document-qc.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-conventions/references/development-document-qc.md#preparation-gates); [skills/sdd-manage/references/document-qc-gates.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/references/document-qc-gates.md#stage-handoff); [skills/sdd-plan/references/physical-layout.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-plan/references/physical-layout.md#layout-and-preparation-qc).

**Observation:** accepted decisions and design review checks do not prescribe returning each completed design root to the human. Canonical preparation gate tables explicitly cover SPEC, PLAN with relevant layout, and TASKS using owner QC and Ready/Blocked reports. They do not require human acceptance. Grouped architecture/decomposition and PLAN/layout routing can pass over separate document boundaries. The source's read-only/selected-stage stop rules apply to narrow requests; they do not guarantee pauses during an authorized multi-stage request.

**Consequence:** an agent may create multiple dependent documents, or progress from Ready TASKS to implementation/projection, without giving the human the requested review opportunity after each root. This is a source-level permission/omission analysis, not an observed live failure.

**Bounded correction:** add a mandatory human-checkpoint contract with all seven roots and their owners. Present the completed selected root and relevant children, obtain the human's decision, and block dependent progression until acceptance of that presented scope. Wire the contract into both manager routing and direct owner calls. Preserve existing automated QC and Git gates. Keep PLAN and layout as separate checkpoints; a joint owner does not erase either boundary.

**Objective recheck:** walk the full preparation path and each direct owner call. After each created root, the next dependent authoring/use step must remain pending without a human decision; passing QC alone must not clear that human checkpoint. Sufficient previously accepted inputs can be reused without inventing absent stages.

**Confidence:** high; controlling preparation/owner sources inspected. **Disposition:** Open; no source correction performed.

### R-002 — Standing authorization and continuation need an explicit checkpoint boundary

**Baseline evidence:** [skills/sdd-manage/SKILL.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/SKILL.md); [skills/sdd-manage/references/workflows.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/references/workflows.md); [skills/sdd-manage/references/examples.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/references/examples.md); [Greenfield Project Prompt Template](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/Greenfield%20Project%20Prompt%20Template.md).

**Observation:** workflows says not to require fresh approval for a transition already covered by a combined request. The manager reuses session authorization and acts routinely without repeated confirmation. The example for preparing through TASKS runs preparation through its final stop. The prompt template preserves checkpoints that SDD Manager requires, but those human document checkpoints are not defined. These rules are useful for repository operations; their relationship to mandatory document acceptance is unspecified.

**Consequence:** a broad instruction such as developing the full project or preparing through TASKS can be read as permission to bypass the future per-document human review. Conversely, an indiscriminate repair could reintroduce repeated approval for every commit or push. Neither reading implements the clarified requirement reliably.

**Bounded correction:** distinguish repository/workflow-operation authority from acceptance of the actual presented document. Mandatory human document pauses still apply to broadly authorized work unless the human explicitly changes that checkpoint requirement. Existing authority continues to cover permitted persistence operations at the checkpoint; acceptance does not require a second permission question to push the same authorized result. Reconcile the workflow examples, consumer explanation and owner handoffs with that distinction.

**Objective recheck:** a broad project authorization and valid token must still stop for human review of each newly created root. A human acceptance response must clear only its identified presented scope; the next routine commit/push must not request duplicate repository authorization. The phrase “prepare through TASKS” must not imply acceptance of unseen documents.

**Confidence:** high; wording and routing are explicit, actual runtime interpretation untested. **Disposition:** Open.

### R-003 — Human review lacks a shared presentation, decision and resume contract

**Baseline evidence:** [skills/sdd-conventions/references/development-document-qc.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-conventions/references/development-document-qc.md#review-reports-and-correction-records); [skills/sdd-report/references/document-qc-reports.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-report/references/document-qc-reports.md); [skills/sdd-manage/references/coordination.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/references/coordination.md#establish-scope-and-prerequisites); [skills/sdd-orient/SKILL.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-orient/SKILL.md); [skills/sdd-design/references/exploration.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-design/references/exploration.md#decision-state); [README.md](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/README.md#project-preparation).

**Observation:** QC reports retain exact reviewed/governing states and Ready/Blocked outcomes; orientation observes readiness and Git evidence. Exploration explicitly says silence is not acceptance, but no common created-document human checkpoint defines what to present, what decision clears it, which version/scope was accepted, or how interruption resumes at an awaiting-human boundary. README's preparation flow shows QC gates, not seven human decisions.

**Consequence:** an agent can mistake comments, a QC report, a prior high-level decision, or an old “accepted” response for current document acceptance. A resumed agent cannot reliably distinguish ready-to-present, awaiting-human, accepted, and revision-requested states from the defined preparation protocol alone.

**Bounded correction:** specify a concise handoff containing the document/root and children, current content identity or existing Git checkpoint, relevant decisions/assumptions, QC outcome/limits, and exact next dependent operation being held. Record the actual human decision and its scope in existing handoff/campaign/preparation evidence; require no new transaction journal or standalone database. Acceptance, revision request and unresolved discussion must remain distinguishable. Material edits after acceptance need explicit treatment in the proposed policy, with unaffected accepted scope reusable.

**Objective recheck:** silence and review comments alone cannot clear acceptance; a revision request keeps the dependent stage pending; an interrupted workflow resumes from the actual awaiting-human state without regenerating valid documents. An acceptance applies to the presented state/scope. Source/report/consumer wording must not equate agent Ready, commit/push or Git integration with human acceptance.

**Confidence:** high for the missing common contract; human-response interpretation and material-change details remain policy work, not executed evidence. **Disposition:** Open.

## Source-level scenarios and limits

| Scenario | Baseline source assessment |
| --- | --- |
| Full project preparation authorized; PROJECT created | No explicit mandatory PROJECT review pause before architecture. |
| Architecture created during a combined design request | Owner review is defined; human pause before decomposition is not. |
| SPEC QC report Ready; planning already requested | QC gate can permit PLAN without a separate required human acceptance step. |
| PLAN/layout requested together | A grouped authoring/QC path is defined; separate human checkpoints are not. |
| TASKS Ready; implementation already within request | QC and preparation integration are required; human TASKS acceptance is not separately mandatory. |
| User says nothing after presented draft | Exploration rejects silence as acceptance, but no universal per-document continuation rule connects that safeguard to all owners. |
| Human already accepted the unchanged current input | Accepted-input reuse is useful existing behavior and should be preserved. |

These are inspections of written control paths, not live runs or measured failure rates. No finding concerns historical campaign compatibility, token permissions, release packaging or product implementation. Existing code-review milestones and human-directed implementation steering are distinct from the requested preparation checkpoints.

## Artifact verification

Scoped validation checked all seven boundary rows, three stable finding records, 17 pinned-source links and anchors, heading spacing, source/version and closed-package preservation, an exact index-entry-only edit, and `git diff --check`. All passed. No support suite or live acceptance was run for this report-only checkpoint.

## Handoff and stopping point

The prompt supplies the required direction: seven mandatory **human** reviews after document creation. The proposed repair queue is R-001 → R-002 → R-003 with coordinated owner/consumer updates and source-level scenario verification. Detailed source edits and their verification belong to the subsequent revision execution. This review ends at its report checkpoint, then the coordinating workflow publishes it on the campaign branch. The campaign remains open; no default-branch merge or source-policy implementation is claimed.

## Subsequent human clarification — 2026-10-09

The human clarified applicability after the baseline review and initial proposed plan. Greenfield creation walks the human through the document chain. Existing documents at entry, including interrupted explicitly staged work, receive an initial agent assessment through orientation and the appropriate owner checks; acceptable results normally allow continuation to the next eligible stage without interactive review.

An explicit request to review existing artifacts means interactive review and must be the first work step. It presents concise substantive analysis to the human, including consequential choices, consistency/coverage, important issues and a reasoned recommendation. If startup assessment finds important document issues, the agent can raise concerns and proactively offer this review before advancing. The offer does not itself activate interactive mode or remove a real readiness blocker.

This clarification scopes R-001–R-003 and supersedes the initial plan's broader proposed rule that every material change to an existing accepted document automatically requires interactive reacceptance. Preserve the original baseline observations; the repair should add missing created-document checkpoints and selected interactive-review behavior without retroactive acceptance ceremonies or automatic interactive mode for acceptable existing inputs. The current [revision plan](REVISION-PLAN.md) incorporates these requirements; no source edits have been executed.

## Feature campaign extension — 2026-10-09

The human additionally requires a similar HIL approach for feature campaigns. Current feature routing at the reviewed baseline uses necessary scoped design/specification/plan deltas and accepted main inputs, but the baseline's missing explicit human document checkpoints also affects newly prepared feature proposals. See [feature sequencing](https://github.com/pchemguy/SDD-Manager/blob/04f0b63ed923ff97860a3205cf369b3421d41665/skills/sdd-manage/references/workflows.md#feature-sequencing); architecture/decomposition references explicitly keep their feature overlays optional.

The active plan extends R-001–R-003 repair coverage to feature HIL: orient to existing main/feature progress, establish the feature scope, then interactively develop and review only necessary new deltas before dependent use. Existing acceptable inputs normally permit continuation; explicit interactive-review requests take priority and important initial issues can prompt a concern/offer. Preserve separate new PLAN/layout proposal checkpoints, existing technical integration gates and operation authority. Create no obligatory FEATURE-PROJECT/FEATURE-LAYOUT artifact or full-project document replay. This is clarified revision scope and proposed articulation, not implemented source or live acceptance evidence.
