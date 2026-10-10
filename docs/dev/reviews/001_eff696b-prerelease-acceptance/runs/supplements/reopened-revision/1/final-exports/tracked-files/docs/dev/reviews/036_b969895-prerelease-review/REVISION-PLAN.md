# Revision plan

## Campaign and accepted decisions

- Campaign: `036_b969895`; starting and current source baseline: `b9698951df514f09e01021bfb59a459d4c0bdb12`.
- Working branch: `revision/036_b969895-prerelease-review`; eventual integration target: `main` in `pchemguy/SDD-Manager`.
- Objective: define an explicitly selectable comprehensive prerelease review campaign and make release workflows produce an advisory reminder about it.
- Accepted input: the human's prerelease review proposal and follow-up instruction to open a revision campaign, with the review optional for now. This is a directly accepted amendment, not a defect finding from a performed review.
- State: Execution authorized by the subsequent human “Execute” instruction. The initial planning request stopped after publication; observed results are in [REVISION-REPORT.md](REVISION-REPORT.md).
- Execution evidence: [REVISION-REPORT.md](REVISION-REPORT.md). No preceding review report is required or implied.
- Product source version remains `0.15.0`; planning does not authorize a version change, tag, product release, workflow dispatch or hosted tracking change.

## Resulting workflow contract

The prerelease profile will use the existing manager review/revision campaign procedure and focused skill owners. Add a conditionally loaded, provider-independent reference at `skills/sdd-manage/references/prerelease-review.md`; do not introduce another skill or a parallel review framework. Selecting the review establishes its own campaign scope, pinned candidate and report boundary. Review alone does not authorize repairs, revision execution or release publication.

At release entry, briefly recommend comprehensive prerelease review and identify how to select it. The reminder applies to coordinated release publication and direct release-owner calls, including an established release workflow. It must not automatically activate review, require a confirmation or waiver, delay authorized release work, or introduce a mandatory review gate. Reuse a known decision or applicable candidate-specific review instead of repeatedly prompting. Ordinary required package/source/publication checks continue to apply; an optional review report does not substitute for them. Preparing highlights alone does not trigger a publication reminder.

Pin the candidate source commit and relevant package identity, version and evidence. Inventory the complete CURRENT supported product, with the release diff used to prioritize attention rather than restrict coverage. Define review units, dependencies, criteria, representative success/failure/boundary scenarios, exclusions, unavailable checks and report checkpoints before comprehensive assessment. After source/package changes, reassess affected coverage and tie readiness to the actually assessed candidate.

## Coverage to incorporate

| Concern | Required assessment |
| --- | --- |
| Coherence and completeness | Duplication, inconsistent terminology or behavior, misalignment, stale current material, missing contracts, scope violations, defects and bounded improvement opportunities. |
| Traceability and claims | Requirements, design, implementation, tests and documentation agree; supported, planned, deferred and untested capabilities are explicit; claims have appropriate evidence. |
| Workflow and instruction behavior | Prerequisites, ownership, handoffs, human decisions, stopping/recovery paths, permissions, ambiguous instructions, unsupported mandates and possible gate bypasses. |
| README and AGENTS.md | README positioning, capabilities, installation, quickstart, examples, limits, navigation and release downloads; concise current AGENTS.md orientation, authorities, commands and ownership without duplicating workflows. |
| Diagrams | Semantic alignment with actors, transitions, branches, gates, failures and stopping points; rendered readability as well as source syntax, with rendering limits reported. |
| Maintainability | Competing authorities, coupling, unnecessary duplication, progressive disclosure and context consumption. |
| Verification | Meaningful success, failure, boundary and recovery evidence; distinguish structural support checks from live consumer/client acceptance and identify missing evidence. |
| Distribution and operation | Actual package contents/exclusions, metadata/version, entry points, dependencies, notices, checksums, installation/startup, supported interfaces/platforms and compatibility where relevant. |
| Access and sensitive material | Credential handling, unintended sensitive content, applicable dependency risks and supported access assumptions without speculative compliance requirements. |
| Agent plugin specifics | Activation descriptions, direct invocation, bundled-reference resolution, instruction handoffs and source-to-shipped-package consistency. Apply these criteria when reviewing an agent plugin, not indiscriminately to every project. |

Closed campaign and archived feature/steering records remain frozen and outside routine review or validation. Consult selected history only for a specific evidence question; do not create historical compatibility repairs or findings. Review depth follows the product's actual supported scope; record justified not-applicable criteria rather than inventing requirements.

## Source owners and ordered revisions

| Action | Owner and intended outcome | Dependencies | Objective recheck |
| --- | --- | --- | --- |
| V-001 | sdd-manage defines the focused prerelease review reference and routes explicit selection from its entry/workflow/review references. Reuse sdd-conventions campaign identity, sdd-report artifact formats, sdd-docs documentation assessment and sdd-verify evidence/release checks. | Accepted contract above. | Explicit selection yields a pinned comprehensive campaign, complete current inventory, owned units, stable findings and a report-only stopping boundary. |
| V-002 | sdd-manage release operations and sdd-forge release entry/lifecycle expose the shared advisory reminder, including direct release calls. Inspect release workflow dispatch guidance for a discoverable shared handoff. Keep reminder semantics in one authority and link callers. | V-001. | Coordinated/direct release scenarios show one relevant recommendation without automatic review, confirmation, waiver or blocked progression; existing release checks remain intact. |
| V-003 | Reconcile current README/navigation and relevant examples only as necessary; verify composition and record actual action/scenario evidence in the active revision report. | V-001 and V-002. | Changed links/style, source behavior scenarios, applicable support suite and actual package checks pass; claims remain limited to observed evidence. |

No root PROJECT, SPEC, PLAN or TASKS change is required for this plugin-source amendment. Campaign action IDs organize bounded maintenance and do not become invented executable task IDs. Changes outside the identified current owners require a demonstrated dependency within this accepted scope.

## Planned verification scenarios

| Scenario | Expected result |
| --- | --- |
| SC-001 | Explicit comprehensive prerelease review selection loads the profile through existing campaign routing. |
| SC-002 | Small release diff still produces an inventory of the complete current supported product. |
| SC-003 | Review plan orders units and records criteria, scenarios, exclusions and unavailable checks. |
| SC-004 | Duplication, stale current material, scope violations and gaps have actionable located evidence and objective rechecks. |
| SC-005 | README and AGENTS.md receive distinct audience/authority assessments. |
| SC-006 | A diagram with valid syntax but a missing failure/gate path is assessed for semantic alignment; rendering evidence is distinguished. |
| SC-007 | Readiness separates release blockers, accepted deferrals, improvements, unknowns and actual human decisions. |
| SC-008 | Changed candidate source/package causes affected rechecks; an old report is not current readiness evidence. |
| SC-009 | Review completion publishes its report and stops before repairs or product release absent independent authorization. |
| SC-010 | Coordinated release publication emits the optional reminder and proceeds under existing checks when review is not selected. |
| SC-011 | Direct sdd-forge release calls and established-workflow publication have the same reminder semantics. |
| SC-012 | Known applicable review or human decision is reused without repeated reminders or invented waiver records. |
| SC-013 | Highlights-only work does not activate a review or publication reminder; preparation alone does not publish a release. |
| SC-014 | Optional review never replaces mandatory package validation; unavailable live acceptance remains explicitly unverified. |
| SC-015 | Closed historical packages are excluded and unchanged; targeted historical consultation creates no repair duty. |
| SC-016 | Generic projects receive relevant comprehensive criteria; plugin-specific criteria apply only where pertinent. |

These scenarios are planned source/consumer assessments, not performed runtime tests. During execution, record actual commands, assessed source, evidence class, results and limitations. For coherent plugin integration, read acceptance/textstats/AGENTS.md and run the established support suite; inspect the actual built package using its existing contract. Do not claim live agent/client, rendered-diagram or hosted-release verification without performing it under applicable authority.

## Persistence and stopping

Commit this plan and its current campaign-index entry together, push the campaign branch and verify remote containment before further project work or another commit. Stop after published planning; leave main and product source unchanged.

A later execution instruction uses this branch and plan. After each action, update the active revision report, commit the scoped source/evidence, push and verify remote containment before the next action. Finish report/navigation and scoped checks before eligible explicit two-parent integration into main; verify and publish that boundary under existing Git workflow ownership. Preserve all prior closed packages. No release/tag or external live acceptance is included by implication.
