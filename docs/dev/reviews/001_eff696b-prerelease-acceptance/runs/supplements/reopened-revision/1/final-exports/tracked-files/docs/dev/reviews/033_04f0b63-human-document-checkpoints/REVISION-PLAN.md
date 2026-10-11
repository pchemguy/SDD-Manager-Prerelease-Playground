# Mandatory human document review — proposed revision plan

## Campaign and decisions

- Campaign: `033_04f0b63-human-document-checkpoints`.
- Starting/reviewed baseline: `04f0b63ed923ff97860a3205cf369b3421d41665`, version **0.15.0**.
- Working branch: `revision/033_04f0b63-human-document-checkpoints`; eventual integration target: `main`.
- Review: [REVIEW-REPORT.md](REVIEW-REPORT.md), committed and remotely verified as `f2f127c82f35760de5e08c601bde0bb89e2f6623` before this plan.
- Human-defined direction: walk the human through creation of the greenfield document chain with mandatory **human review checkpoints** after each PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, layout and TASKS.
- Subsequent human clarification: at repository entry, assess existing progress and normally continue to the next eligible stage without activating interactive review of existing documents. An explicit request for interactive review takes precedence; important startup issues may prompt a proactive offer.
- Additional human direction: articulate the same human-in-the-loop (HIL) approach for feature campaigns, preserving their scoped document deltas and reuse of existing main/feature inputs.
- Findings R-001–R-003 are proposed repair inputs. No finding is marked corrected or verified.
- State: Proposed; campaign opened and baseline review complete. Source revision execution has not started. Startup/interactive-mode rules below incorporate the user's clarification. Detailed presentation/evidence mechanics remain proposed; source implementation has not occurred.

## Entry and interactive review selection

`sdd-orient` establishes existing progress, document/Git state, governing instructions and current handoff/readiness evidence. Keep orientation read-only. Where substantive QC is needed, route it to the artifact owner through sdd-manage; orientation does not silently become an authoring or repair workflow.

| Entry condition | Required behavior |
| --- | --- |
| Greenfield chain needs a document to be created | Develop that document with the human and use its creation checkpoint before dependent progression. |
| Some documents already exist, including interrupted explicitly staged preparation | Assess actual progress, decisions, readiness and remaining work; reuse acceptable existing inputs and continue from the next eligible stage within the request. File presence does not prove readiness, and absence of a retrospective human-review record does not itself activate interactive mode. |
| Human explicitly requests review of existing artifacts | Begin with that interactive review before advancing the chain. Present concise, substantive agent analysis to the human, discuss identified decisions/issues and conclude the selected review before dependent continuation. |
| Initial agent assessment identifies important document issues | Raise the concrete concern, its consequence and affected next stage; proactively offer interactive review before advancing. An offer is not acceptance to enter interactive mode. Keep unresolved consequential issues subject to the normal readiness/decision gates. |
| Initial assessment is acceptable and no interactive review is requested/selected | Proceed to the next eligible workflow stage under existing scope without another acceptance ceremony for the existing artifacts. |

Interactive review means presenting substantive analysis for a human decision/discussion, rather than merely listing files, returning a Ready label or announcing that checks ran. Keep the analysis concise: intended purpose and coverage, consequential choices, consistency/gaps, important risks or assumptions, and a recommended disposition with reasons. Scope it to the selected artifacts and concerns.

Repository startup assessment and agent QC are routine readiness work. They do not automatically activate interactive review. Preserve actual human stopping instructions and unresolved requested reviews; do not infer a new human checkpoint solely because the repository contains an existing document or a paused process.

## Created-document checkpoint contract

1. Complete the selected document/root and relevant children, perform applicable owner QC, and persist the reviewable result through authorized Git operations.
2. Present that specific document scope to the human with links and concise substantive analysis: purpose/coverage, consequential choices and their rationale, consistency/gaps, assumptions/open questions and recommended disposition. Include applicable QC result/limits and the exact dependent operation being held.
3. Pause for the human's review decision. Passing agent QC, a Ready report, a commit/push, or general authorization to develop the project does not supply that decision.
4. Record the actual decision and its document/version/scope in existing preparation, handoff or campaign evidence. A request to revise returns to the current owner and holds the dependent stage. Silence or unresolved review discussion leaves acceptance pending.
5. Continue only after acceptance of the presented scope and within the previously authorized work. An explicit acceptance-and-proceed response can clear the presented checkpoint and authorize its stated next step; it cannot preaccept documents that have not been presented.

| Created document | Presenting owner | Dependent progression held |
| --- | --- | --- |
| PROJECT | sdd-design | ARCHITECTURE or other work relying on the created brief. |
| ARCHITECTURE | sdd-design | DECOMPOSITION or other work relying on the created architecture. |
| DECOMPOSITION | sdd-design | SPEC or other work relying on the created component model. |
| SPEC | sdd-specify | PLAN and dependent work relying on the created behavioral contracts. |
| PLAN | sdd-plan | Subsequent dependent layout/TASKS work relying on the created strategy. |
| layout | sdd-plan | TASKS and other work relying on the created physical ownership. |
| TASKS | sdd-tasks | Implementation and hosted task projection using the created list. |

Preserve the existing dependency order, with SPEC before PLAN. PLAN and layout receive distinct checkpoints during combined preparation. Present a root's relevant children together. At entry, use acceptable existing inputs without requiring retrospective human acceptance or replaying their creation. Newly created missing documents enter the interactive chain at their creation boundaries. Preserve optional stages and scoped feature workflows; do not invent documents solely to fill the chain.

Repository-operation authority remains usable for the authorized commit/push at a checkpoint. The human review concerns document acceptance; it does not add repeated permission questions for the same authorized repository operations. An explicit human change to checkpoint scope is retained as such; generic project authorization is not an implicit waiver.

Proposed revision/resumption rule: during an active interactive document review, requested revisions stay with that owner and the review concludes on the actual presented state before dependent progression. For existing documents assessed at startup, material issues invalidate affected technical readiness and require their owning assessment/correction or a consequential human decision as appropriate; this is not automatic activation of a full interactive review. Routine authorized maintenance and status/evidence edits do not create new interactive checkpoints by themselves. After interruption, orient to the actual document/Git state, relevant human decisions and remaining requested work; resume the existing workflow at its next eligible stage, preserving any actual unresolved human stopping instruction or requested review. Store state in existing evidence rather than a new journal or registry.

## Feature campaign HIL

Begin by orienting to the existing project, active feature package, relevant main/feature documents, accepted decisions and actual progress. Establish the feature objective, scope, non-goals and affected owners with the human. Follow the same startup selection rule: acceptable existing inputs allow normal advancement; an explicitly requested interactive artifact review begins first; important initial issues can prompt a concern and offer of interactive review before advancing.

Walk the human through development of the feature's necessary document deltas. Each newly prepared document/proposal receives concise substantive analysis and a human checkpoint before its dependent stage. Present changed behavior, architectural or delivery choices, affected main guarantees, compatibility/integration effects, scope/deferrals, uncertainties and a reasoned recommendation. Passing QC or broadly authorizing the feature does not preaccept these new proposals.

| Needed feature artifact/proposal | HIL checkpoint and dependent progression |
| --- | --- |
| Feature objective/brief | Establish the actual feature scope through exploration and existing package/handoff evidence. Reuse the main PROJECT brief; create/review PROJECT only when that artifact is genuinely selected. |
| FEATURE_ARCHITECTURE | Human review of the scoped structural proposal before dependent component/contract work. Create only when architecture needs a delta. |
| FEATURE_DECOMPOSITION | Human review of affected component/collaboration boundaries before dependent specification. Create only when this design level needs a delta. |
| FEATURE-SPEC | Human review of the new behavioral delta, affected contracts and acceptance before dependent planning/tasks. |
| FEATURE-PLAN | Human review of the scoped delivery strategy before dependent layout/tasks. Reuse sufficient existing strategy when a feature plan is unnecessary. |
| Feature layout proposal, when needed | Human review of the new physical-ownership decisions before dependent task derivation. Use the existing selected layout/feature-plan owners; prescribe no new FEATURE-LAYOUT filename. |
| FEATURE-TASKS | Human review of the new executable delta before implementation or hosted task projection. |

Keep feature PLAN and layout proposal checkpoints distinct when both are newly prepared. Reuse unchanged main design, SPEC, strategy and layout; omitted optional overlays do not create checkpoint placeholders. A feature campaign has its own scoped sequence rather than repeating seven project-wide documents or rewriting the complete main chain.

An interrupted feature campaign follows normal existing-progress assessment: reuse acceptable existing deltas and resume the next eligible stage without automatically replaying interactive review. Preserve an actual unresolved human instruction or selected review. Consequential newly proposed decisions enter their appropriate HIL checkpoint; routine status/evidence edits do not activate full interactive mode.

Human acceptance of feature proposals supplies the relevant document decisions. Existing preparation integration, bounded implementation, accepted feature incorporation and final verification/publication retain their own scope and technical gates. Authorized commits, pushes and merges use existing operation authority; this requirement adds no approval question for every implementation task or repository operation.

## Ordered revisions

| Action | Findings | Intended outcome and affected owners | Dependencies / objective recheck |
| --- | --- | --- | --- |
| V-001 | R-001, R-003 | Define one canonical human-review protocol through sdd-manage; distinguish greenfield and necessary feature-proposal checkpoints from normal existing-document startup assessment. Include seven root boundaries, explicit requested-review precedence, proactive concern/offer, presentation, decision scope and continuation. Retain current agent QC gates. | First action. Newly created roots and selected interactive reviews must hold dependent progression pending their human review decision. Acceptable existing startup inputs must permit normal continuation without automatically activating interactive mode. Canonical policy placement is resolved before duplicating owner text. |
| V-002 | R-001, R-003 | Wire sdd-design PROJECT/ARCHITECTURE/DECOMPOSITION, sdd-specify SPEC, sdd-plan PLAN/layout and sdd-tasks TASKS/FEATURE-TASKS authoring/direct calls to the canonical protocol. Include applicable FEATURE_ARCHITECTURE, FEATURE_DECOMPOSITION, FEATURE-SPEC, FEATURE-PLAN and scoped layout proposal handoffs. Reconcile shared readiness/reporting and orientation observation where affected. | V-001. Check direct and coordinated calls, combined PLAN/layout requests, acceptable existing inputs, interrupted staged processes, explicit requested reviews, proactive offers and optional feature-delta stages. Preserve selected-stage and read-only limits. Resolve QC scope at the PLAN checkpoint without authoring the future layout before human review; complete affected combined QC at the subsequent layout boundary. |
| V-003 | R-002, R-003 | Reconcile manager workflow/coordination language, examples, README main/feature preparation flows and the greenfield prompt with the distinction between operation authority, routine startup/QC assessment and selected interactive document review. | V-001–V-002. Broad “develop the project” or “prepare through TASKS” authorization must still pause per created root; accepted result persistence must not ask for duplicate operation permission. |
| V-004 | R-001–R-003 | Recheck all affected current sources and explicit positive/negative control paths. Record actual changes, outcomes, remaining decisions and evidence limits in the active campaign revision report. Finish eligible verified integration/publication only after execution is authorized and complete. | V-001–V-003. Verify the scenarios below, changed links and package inclusion as applicable; run the repository-required support suite for the coherent plugin source integration. Support tests remain distinct from live agent/client acceptance. |

No project TASKS owner exists in this repository; V-001–V-004 are campaign action IDs, not invented executable task IDs. Existing closed packages stay frozen. Retain source version **0.15.0** as requested; this plan adds no product release or version bump.

## Planned acceptance scenarios

| Scenario | Required result after revision |
| --- | --- |
| Greenfield combined initial preparation request | Walk the human through the created chain with seven human boundaries; the next dependent root/use remains pending at each one. |
| Direct creation request for any named root | Same human-review contract; no unrequested downstream creation/execution. |
| PLAN and layout requested together | Review PLAN before continuing to dependent layout, and review layout before TASKS; no single deferred end-of-bundle checkpoint. |
| Agent QC Ready and broad execution authorization | Human review still pending for the newly created root. |
| Human accepts the presented document and asks to continue | That scope clears; only the authorized next operation proceeds. |
| Silence, comments without acceptance, or request for revision | Pending state retained; dependent work held and requested revisions routed to the current owner. |
| Existing documents with acceptable startup assessment | Proceed to the next eligible workflow stage without interactive review or retrospective acceptance ceremony. |
| Interrupted explicitly staged preparation with some documents present | Orient to actual progress and decisions, reuse acceptable work and resume the next eligible stage; preserve actual explicit stopping instructions. |
| Explicit interactive review request for existing artifacts | Begin with that review, present concise substantive analysis and resolve its selected scope before advancing. |
| Important issues identified in initial assessment | Raise concern and offer interactive review before advancing; preserve real readiness blockers without treating the offer as accepted. |
| Proactive review offer accepted or declined | Enter the selected review only when accepted; a decline does not erase an unresolved consequential issue. Continue independent/eligible authorized work when readiness permits. |
| Existing inputs reused or optional stages absent | No invented document stage or compulsory interactive replay. |
| Material issue/change in an existing startup input | Affected technical readiness rechecked and consequential decisions routed; no automatic full interactive-mode activation. |
| Interrupted awaiting-human workflow | Actual document/decision state reused; no invented acceptance or duplicate generation. |
| Feature with a small behavioral delta and sufficient main design/strategy | Review the needed new feature proposals interactively; reuse adequate existing inputs without creating optional overlays or a complete main-document chain. |
| Feature needs architecture, decomposition, SPEC, PLAN, layout and TASKS deltas | Walk the human through each necessary proposal in dependency order with distinct PLAN/layout checkpoints. |
| Existing/interrupted feature package passes startup assessment | Continue its next eligible stage without automatic interactive replay. |
| Requested review or important issues in main/feature inputs | Requested interactive review comes first; important issues support a proactive concern/offer without silently entering interactive mode. |
| Accepted feature proposals and integration already authorized | Technical readiness, selected incorporation and publication gates still apply; no repeated approval per commit/merge/task. |
| Git/token authorization already established | Ordinary checkpoint persistence uses it; no duplicate repository-operation approval. |

These are planned checks, not executed acceptance results. Source-level review can establish articulation; runtime or installed-client acceptance needs separate observed evidence within its authorized scope.

## Current persistence and stopping point

The review report and this proposed plan are retained on the campaign revision branch with navigation in the current campaign index. Opening/assessment does not merge an unfinished campaign into main. Source-policy changes, support tests, product packaging and live acceptance have not been executed. The campaign remains open for subsequent revision execution; no REVISION-REPORT is fabricated before revisions begin.

## Execution disposition

The human instructed execution. V-001–V-004 are implemented and source-verified; see [REVISION-REPORT.md](REVISION-REPORT.md) for actual checks, scenario assessments and limits. Proposed baseline observations above are retained as planning evidence.
