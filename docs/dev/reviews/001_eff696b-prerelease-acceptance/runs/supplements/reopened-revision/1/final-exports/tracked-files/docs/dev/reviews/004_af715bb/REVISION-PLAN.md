# Design boundaries and incremental delivery revision plan

## Campaign and decisions

- **Campaign:** `004_af715bb`.
- **Starting and reviewed baseline:** `af715bbdc8bc4e5baea8058c7021b34a404e4a36`.
- **Current planning baseline:** `59486ec9dc1c8e30d4814f1396c4624a5621f9de`; the reviewed skill sources remain unchanged.
- **Date:** 2026-10-02.
- **Review:** [REVIEW-REPORT.md](REVIEW-REPORT.md).
- **Revision evidence:** [REVISION-REPORT.md](REVISION-REPORT.md).
- **Disposition:** R-001–R-005 included in the proposed revision scope; none deferred or rejected. All five findings are Verified for source articulation and instruction interpretation; original baseline observations remain retained in the review.
- **Authorization and state:** Subsequent user instruction authorized execution. V-001–V-005 completed, verified within recorded evidence limits, explicitly merged, and target publication verified; see the revision report. Consumer product implementation remains outside scope.

The intended result is a concise document ownership model and an explicit delivery strategy: reach the simplest practical meaningful end-to-end MVP early, establish rigorous relevant verification, and grow through small meaningful capability increments. Phase and milestone boundaries provide evidence for human decisions about usefulness, usability, risk, and continued investment.

## Authoritative project updates

| Owner / document | Intended change | Findings | Required before |
| --- | --- | --- | --- |
| sdd-design: architecture.md, decomposition.md, entry where needed | Explain structural granularity and design-level interfaces together; cross-link canonical definitions. | R-001, R-002 | Specification and planning alignment |
| sdd-specify: system-specification.md, review.md, entry where needed | Make behavioral contract ownership, structural traceability, and conflict feedback explicit. | R-002 | Delivery strategy derived from accepted contracts |
| sdd-plan: delivery-plan.md, review.md, entry where needed | Establish meaningful MVP-first delivery, bounded functional growth, verification dependencies, and consequential decision gates. | R-003–R-005 | Task derivation and coordinator alignment |
| sdd-tasks: task-derivation.md, entry where needed; sdd-conventions: task-hierarchy.md | Derive bounded executable work within capability increments; clarify hierarchy decision value without transferring implementation/completion ownership. | R-004, R-005 | Composed workflow validation |
| sdd-manage: workflows.md and affected preparation handoffs; README and docs/dev/CAPABILITY-MAP.md where descriptions need alignment | Carry the strategy into preparation and bounded execution, retaining human decisions and existing stops. | R-003–R-005 | Final campaign verification |

This repository has no governing PROJECT/ARCHITECTURE/DECOMPOSITION/SPEC/PLAN set to amend for these plugin instructions. Update the existing skill owners and navigation; do not create a synthetic consumer project document set. In future consumer projects, accepted requirements, design decisions, and delivery strategy belong in their respective governing documents, while this campaign retains the revision rationale and evidence.

## Ownership contract

| Artifact | Canonical responsibility |
| --- | --- |
| ARCHITECTURE | Major blocks, system-wide relationships and dependency direction, consequential rationale and invariants, and structural support for required qualities. |
| DECOMPOSITION | Logical components/subcomponents, responsibility boundaries, collaboration, provided/required design-level interfaces, state ownership, and extension/verification seams. |
| SPEC | Observable success/failure behavior, data and lifecycle contracts, cross-component guarantees, required nonfunctional constraints, and objective acceptance. |
| PLAN | Practical staged realization: initial meaningful capability, subsequent increments, dependencies, integration, verification, and decision gates. |
| layout.md | Physical allocation of source, tests, and documentation consistent with logical responsibilities. |
| TASKS / FEATURE-TASKS | Stable identities and bounded executable work realizing the owning plan's milestones. |

Architecture and decomposition describe structure at different granularity; SPEC makes its observable obligations precise. Relevant contracts link responsible owners and consumers. Conflicts feed back to the affected requirement/design owner rather than being silently resolved by duplication or unilateral redesign. No mandatory one-spec-per-component mapping or separate traceability artifact is introduced.

Extensibility, scalability, modularity, decoupling, and testability serve accepted requirements and credible variation/load needs. PLAN chooses when to realize the accepted structure; it does not redefine contracts or require speculative infrastructure before the MVP. Main design and SPEC continue to describe the complete intended system.

## Ordered revisions

### V-001 — Clarify architecture and decomposition

- **Findings:** R-001; establish the structural side of R-002.
- **Targets:** sdd-design entry and architecture/decomposition references.
- **Change:** Place a compact comparison at the shared entry or appropriate reference, then use short focused ownership statements and cross-links. Distinguish major blocks and system rationale from logical component collaboration; distinguish design-level interface shape from exact behavioral contracts and physical placement.
- **Acceptance:** A reader can route a system topology decision, a component responsibility split, a behavior guarantee, and a file allocation to their canonical owners. Existing separation from delivery order and task checklists remains explicit; no repeated normative contract is introduced.
- **Dependency:** None.

### V-002 — Articulate SPEC's relationship to design

- **Finding:** R-002.
- **Targets:** sdd-specify system-specification and review references; affected decomposition wording.
- **Change:** Require relevant structural owner/consumer links for behavioral contracts and cross-component guarantees. Explain bidirectional feedback and handling of unresolved design/contract conflicts through accepted decisions. Retain cohesive behavioral specification children rather than a document per component or implementation stage.
- **Acceptance:** A component-owned contract and a cross-component guarantee have clear canonical behavior and structural links. An incompatible contract produces an identified decision gap rather than an invented requirement, silent design amendment, or copied contract.
- **Dependency:** V-001.

### V-003 — Make MVP-first delivery and small growth the default

- **Findings:** R-003, R-004.
- **Targets:** sdd-plan delivery-plan, plan review, and entry where needed.
- **Change:** Define the earliest practical milestone around a minimal meaningful end-to-end capability. State included/deferred scope, relevant contracts, minimum necessary dependencies, demonstration/acceptance, and the reason for each prerequisite delaying it. For an existing project, preserve the useful baseline and identify the earliest meaningful changed path.
- **Growth:** Plan the smallest meaningful capability increments that can be integrated and robustly checked. Establish relevant end-to-end, regression, failure, and integration coverage early; preserve the working path and fix required failures before dependent growth. Keep detailed test strategy with sdd-tdd, checks with sdd-verify, and repair/task execution with sdd-implement.
- **Exceptions:** Permit justified infrastructure, characterization, compatibility/migration, or risk-probe prerequisites. Record their necessity and the route to meaningful integrated behavior. A technical skeleton or mocked-only demonstration does not by itself establish a useful MVP.
- **Acceptance:** A candidate plan identifies a usable initial slice, deliberate deferrals, applicable acceptance, justified prerequisites, and bounded later functional changes. It covers the full intended system without changing SPEC to describe only the MVP, scheduling all subsystems before integration, or promising optimal speed or guaranteed correctness.
- **Dependency:** V-002.

### V-004 — Align hierarchy, tasks, and human decision gates

- **Findings:** R-004, R-005.
- **Targets:** sdd-tasks task derivation; sdd-conventions task hierarchy; sdd-plan milestone/review criteria; sdd-manage workflow handoffs.
- **Change:** Phases express major delivery/risk outcomes; milestones expose meaningful integrated capabilities and suitable evidence; tasks supply bounded work within them. Module scope remains a useful task-sizing criterion but does not substitute for bounded behavioral increments. Not every task must independently yield user-visible functionality.
- **Decisions:** At appropriate early and subsequent milestones, identify what can be demonstrated, how functionality/usability and consequential risks will be assessed, and the human decision informed: continue, amend, simplify, or stop. No mandatory usability trial per task, automatic steering, automatic stop, or additional approval for already authorized routine work.
- **Acceptance:** The first meaningful slice and later consequential gates have explicit decision evidence. Task decomposition reaches integration and verification within the relevant increment rather than a distant final phase. Existing stable IDs, parent relationships, feature/main ownership, hosted mapping, task completion ownership, push-first execution, and bounded workflow stops remain intact.
- **Dependency:** V-003.

### V-005 — Verify composition and publish the revision boundary

- **Findings:** R-001–R-005.
- **Targets:** Affected source/navigation, README/CAPABILITY-MAP where needed, and retained campaign evidence.
- **Change:** Consolidate concise wording, remove contradictions and duplicated authority, and update relevant project descriptions. Record finding dispositions against original IDs, with actual checks and limits, in REVISION-REPORT.md.
- **Acceptance:** Execute the scenarios below; check changed entry/reference links, headings including fenced templates, package metadata, affected skill/package validation using available repository tooling, and the full boundary diff. Report unavailable checks precisely. After successful working-branch verification, perform explicit integration, verify the merged state, push the established target, and confirm remote containment.
- **Dependency:** V-001–V-004.

## Verification scenarios

These are planned checks, not observed results. Use compact disposable consumer documents or fresh consumer evaluations, without adding permanent test frameworks solely for wording changes. Record inputs, routing/plan outcome, evidence method, and limitations.

| Scenario | Expected result | Actions |
| --- | --- | --- |
| SC-001: Structural routing | Major system decision routes to ARCHITECTURE; component split to DECOMPOSITION; exact errors to SPEC; paths to layout; sequencing to PLAN. | V-001, V-002 |
| SC-002: Contract feedback | Component and cross-component contracts link structural owners/consumers; an incompatible design/behavior obligation remains a surfaced decision, not silent redesign. | V-002 |
| SC-003: Greenfield usable slice | Initial milestone delivers a small meaningful real end-to-end path, with scope/deferrals and relevant checks; a subsystem-first or mocked-only proposal is identified as insufficient without justification. | V-003 |
| SC-004: Existing-system prerequisite | Necessary characterization, compatibility, migration, or risk work is justified; preserved behavior and the first changed usable path are explicit. | V-003 |
| SC-005: Increment and task sizing | Two small module tasks that accumulate a large late behavioral jump are detected; bounded capability growth includes timely integration/regression evidence without demanding user-visible output from every task. | V-003, V-004 |
| SC-006: Functional/usability decision | A suitable milestone names demonstration, feedback, and a human continue/amend/simplify/stop decision; no automatic steer or task-list continuation occurs. | V-004 |
| SC-007: Composition regressions | Full intended design/contracts remain authoritative; feature hierarchy, hosted identities, completion owners, and established branch/push/merge boundaries remain consistent. | V-005 |

## Execution and persistence

1. On a subsequent instruction to implement, orient the current repository, publish any outstanding authorized commits, and establish a scoped revision branch targeting `feature/architecture-revision`. Record actual branch, target, checkpoint, and any changed baseline; do not assume this planning commit began execution.
2. Execute V-001–V-005 in dependency order. After each completed action, update REVISION-REPORT.md with source changes, observed checks, finding dispositions, and limits; commit and push source/evidence together and verify remote containment before dependent work.
3. Preserve this plan and the baseline review. Add disposition/evidence links to the review without rewriting historical observations. Planned or revised findings are not Verified until their objective rechecks pass.
4. Integrate once at the completed verified campaign boundary using an explicit merge commit (`--no-ff`), verify the merged result, push the target, and record merge/publication evidence. Do not merge every action separately or fabricate a merge for already integrated work.
5. Keep all campaign artifacts in `docs/dev/reviews/004_af715bb/`; update campaign navigation to actual stage/state and existing companion links. Return publication links, completed finding IDs, and material limits.

## Limits and stopping

This revision changes documentation instructions and their composition; it does not implement a consumer system or establish empirical delivery speed, bug-localization improvement, correctness, scalability, or usability. Structural validation and consumer interpretation evidence must be reported separately from installed-client/runtime behavior. No external research, new hosting scheme, transaction protocol, recovery skill, mandatory traceability store, or testing policy rewrite is planned.

If a prerequisite decision, conflicting authority, failed check, or publication access blocks an action, preserve valid work and report the exact unmet condition. Continue independent authorized work only where its dependencies allow. Planning stops after this document and navigation are committed, pushed, and remotely verified; source revision requires a subsequent implementation instruction.
