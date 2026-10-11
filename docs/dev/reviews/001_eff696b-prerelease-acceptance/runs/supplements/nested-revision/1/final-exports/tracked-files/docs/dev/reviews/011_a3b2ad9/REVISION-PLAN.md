# Development document QC revision plan

Campaign: `011_a3b2ad9`. Full starting baseline: `a3b2ad9bdbe68d42c32cdcdf0bd80fc2a598dad9`.
Working branch: `revision/011_a3b2ad9-dev-docs-qc`; target: `feature/architecture-revision`.
Inputs: [proposed policy](QC-POLICY.md), [baseline assessment](REVIEW-REPORT.md) and the human's document-QC requirements.
State: policy/review/preparation complete; shipped source revision not started. This request defines the policy and review workflow; implementing the proposed plugin changes is a subsequent revision boundary.

## Ordered source revisions

| Action | Findings | Owner / intended change | Recheck |
| --- | --- | --- | --- |
| V-001 | R-001–R-003 | sdd-conventions: canonical development-document QC reference, discovery entry and links; exclude implementation review units from shape counts. | One invariant owner; 3–5 guidance, 1–2 / 10+ triggers, justified exceptions and semantic scope checks explicit. |
| V-002 | R-001 | sdd-specify: complete-authoring QC gate against PROJECT/ARCHITECTURE/DECOMPOSITION, correction/recheck and report handoff. | Omitted or contradictory design obligation blocks PLAN; corrections go to correct design/contract owner. |
| V-003 | R-001, R-002 | sdd-plan: required SPEC conformance review before task derivation; phase/milestone count and semantic decomposition assessment; layout support. | Minimal meaningful increment retained; no invented features, unexplained coverage gaps, padded groups or quota-driven split. |
| V-004 | R-001, R-002 | sdd-tasks: dedicated post-generation conformance/decomposition review reference and route, separate from progress review; authorized bounded corrections. | TASKS preserves PLAN boundaries; 1–2 / 10+ delivery task groups assessed; review task counts excluded from heuristic but retained in execution selection. |
| V-005 | R-003 | sdd-report: adjacent root report format, current source/governing identities, stable findings, counts, Ready/Blocked and appended revision/recheck sections. | No overwritten baseline findings; current corrected evidence precedes Ready; no per-child report or duplicate traceability database requirement. |
| V-006 | R-001, R-003 | sdd-manage plus feature/steering/orientation/implementation handoffs: run gates during preparation, block dependents, reuse current evidence and reassess affected inputs; retain archive/report ownership. Clarify that active document QC report adjacency is distinct from lifecycle implementation-report prefixes. Align README/capability map. | Review-only remains read-only; authoring corrections cannot silently change upstream contracts; preparation QC adds no administrative implementation task chain. |
| V-007 | R-001–R-003 | Update affected TextStats preparation/conformance assessor criteria and dependency readiness; local catalog/support checks and fresh ordinary consumer assessments. | Small justified phase, 10+ overloaded groups, in-range oversized work, omission/drift, correction cycle, stale report and scoped feature/archive cases assessed. |
| V-008 | R-001–R-003 | Composed source review, verification/evidence, publication and integration under the established Git protocol after implementation authorization. | Complete source handoffs and required checks; live assertions require pinned-source consumer execution and real prerequisites. |

## Verification examples

- A narrowly bounded phase with one delivery milestone plus its mandatory review milestone can pass with rationale; do not create filler milestones.
- A phase with ten delivery milestones requires explicit scope/dependency/drift assessment, while three delivery milestones with enormous contracts can still fail semantic scope review.
- A milestone with four delivery tasks plus a dedicated review task has delivery count four; a ten-task milestone requires explicit overload assessment.
- A missing SPEC contract in PLAN blocks TASKS generation; task-list work redefining PLAN boundaries returns a plan amendment/recheck.
- SPEC/design conflict is resolved by the actual governing decision owner, not by silently rewriting the downstream document.
- Corrected artifacts retain original review findings and append a revision/recheck section; Ready identifies the actual revised state and current governing sources.
- Pure review, partial feature incorporation and interruption do not implicitly authorize unrelated edits or implementation; scoped archive retains report/source adjacency and current main-document readiness stays distinct.

## Persistence and scope

Use the current campaign/branch for the accepted source revision; maintain actual results in REVISION-REPORT.md when revision begins. Preserve the initial review findings and historical source paths. Do not fabricate a completed revision report during policy preparation.

An accepted revision implementation command includes routine commits, established-destination pushes and verified integration/publication under the coordinator's explicit authorization policy. Persist coherent source/report checkpoints, verify the complete boundary and stop at its authorized completion or actual blocker. Existing user limits and enforced permissions remain binding.

No new skill is proposed. Review responsibility stays with the artifact owner; the coordinator enforces progression, report composes evidence, and upstream owners settle necessary decisions. Live acceptance prerequisites remain a dedicated repository and appropriate runtime/provider facilities where execution claims require them; historical support tests cannot prove new QC workflows ran.

## Source implementation follow-up — campaign 019

The human requested a new revision implementing this policy. [Campaign 019 implementation report](../019_609d084/REVISION-REPORT.md) records the source changes, verification and publication. R-001–R-003 are resolved in that source revision; this campaign's original proposal, baseline findings and preparation-only history remain retained. Dedicated live/client acceptance remains separate and pending.
