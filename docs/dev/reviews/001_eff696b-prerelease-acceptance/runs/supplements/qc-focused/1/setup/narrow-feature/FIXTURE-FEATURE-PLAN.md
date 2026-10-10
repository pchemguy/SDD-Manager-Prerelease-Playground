# Named-file ranges delivery plan

## Unaccepted proposal and retained accepted inputs

The [feature specification](FEATURE-SPEC.md) and [SPEC QC](FEATURE-SPEC-REVIEW-REPORT.md) at `b0f93cf170addc80a92541acc4151058e57b6e64` were accepted by delegated coordinator decision `ca0eded9d6e8a7f40ba4e3c9ed4d8370b884db6d`. Reuse main [architecture](ARCHITECTURE.md), [decomposition](DECOMPOSITION.md), [PLAN](PLAN.md) and [layout](layout.md). This delta activates deferred F-001–F-004 with an early meaningful named-file range path, then complete documented/extracted-source exits. It does not change main stdin delivery or claim full Phase 2 completion.

This modified draft is an unaccepted caller proposal derived from actual accepted preparation `8036adbd71ffc1f04b98e689cc131781bc20cd1f`. Historical acceptance and adjacent QC describe original objects only. No task, milestone, projection or implementation result is claimed.

## Phase and milestone strategy

Reuse the exact existing parent identity **Phase 2 — JSON and stdin**, with a feature-only extent and new noncolliding milestone IDs. Existing 2.1/2.2/2.3 retain their meanings, tasks and ownership in main TASKS. Feature completion/checks cover only added milestones; whole Phase 2 remains incomplete until its independent stdin/final obligations are met. A feature extent's final review does not replace the main phase review.

| Parent / proposed milestone | Useful outcome, prerequisites and objective exits |
| --- | --- |
| Phase 2 / 2.4 — Named-file ranges | One useful documented and distributable named-file capability: complete F-001–F-004 parser/selection/acquisition/text/JSON behavior, full public docs and runnable examples, nonempty unit/integration suites and real isolated extracted-module import provenance/exits. Depends on actual reviewed/published JSON 2.1 and compatible baseline/projection prerequisites below. Four bounded delivery tasks implement pure selection, integrate the real CLI, complete public documentation and independently verify extracted-source delivery. Dedicated T-020 performs complete code review, required checks, blocker repair, usefulness demonstration and milestone report after all four deliverables. |
| Phase 2 / 2.6 — Range feature review | Mandatory final single-task feature review T-024 after complete 2.4 delivery/review/closure. Review all F contracts and affected R obligations, component/docs/extraction coherence and accumulated findings/TODOs. Exclude its own still-open review milestone; preserve pending main 2.2/2.3 and T-013–T-017. |

The single delivery milestone provides one cohesive complete named-file capability. The earlier source split demonstrated CLI delivery from documentation/distribution; this proposal keeps internal progress and early runnable examples in four bounded tasks while treating accurate public explanation and independently portable source delivery as part of the same usable outcome. A separate public-docs phase would add handoff cost while withholding complete usability. Retain consequential human feedback after the first integrated path and extracted demonstration. Assess milestone size semantically, without padding to a count target. Mandatory delivery and final feature reviews are excluded from delivery counts.

Historical milestone 2.5 and task T-023 retain original identities in baseline `8036adbd71ffc1f04b98e689cc131781bc20cd1f`. They are reserved and outside this proposal's executable range: documentation and extraction move to 2.4 and review responsibilities to T-020. They are not completed, closed, deleted as done, renumbered, projected or archived. A later accepted change requires explicit ownership/hosted-history reconciliation. Accompanying caller evidence retains their original complete source text.

At T-019 demonstrate real middle/beyond-EOF/blank/mixed-terminator selections and exposed BOMs through text/JSON. At T-021/T-022 demonstrate complete public usage and the extracted package with unchanged API. These support actual continue/amend/simplify/stop choices without automatically changing scope or bypassing review.

## Baseline and integration dependencies

Preparation starts at default `main` `e7cae5b2216ff7dd311b6f7296d829d1927a6a8a` on the package's design-docs branch. Observed separately published JSON milestone 2.1 is `e63b8946bbb99347b0f73f070f9c728945ee5925` on paused `phase/2-json-and-stdin`; its T-010–T-012 are complete while T-013–T-017 remain pending. Main currently lacks JSON. No feature task may execute against the text-only default baseline while claiming text/JSON completion.

For a later separately authorized implementation, first merge/verify/publish accepted preparation into the actual refreshed default branch; only then create the feature implementation branch from that baseline. Establish `phase/2-json-and-stdin` as the intended implementation integration target and incorporate its verified published completed JSON checkpoint into the feature branch through an explicit verified/published compatible merge before feature execution. Preserve pending stdin/final work and original completed evidence. If histories, ownership or JSON state changed, the coordinator resolves that compatibility before execution; never reset/replay completed work or merge the incomplete phase into default by implication.

After authorized feature implementation, incorporate only the accepted feature targets needed for coherence through sdd-integrate-feature, including explicit task ownership/reconciliation scope. Preserve main pending obligations while updating their affected range composition/documentation dependencies. Archive only eligible incorporated feature sources; feature reports remain under the package prefix. Final explicit verified/published feature merge targets the paused phase, not default as a false complete Phase 2. Those are later execution/integration obligations, not actions in this preparation.

## Coverage and verification strategy

| Contract group | Delivery route and required evidence |
| --- | --- |
| F-001 | 2.4 parser validation and acquisition-order checks: signs/whitespace/Unicode/zero/reversal/open/extra-colon/missing/repeated, both spellings, huge ASCII decimals and leading zeros. No arbitrary conversion limit. |
| F-002 | 2.4 pure/shared logical-line traversal and once-only normalization; complete strict decode before selection including bytes after END, EOF subsets, blank/mixed/final lines and exposed interior BOM. |
| F-003 | 2.4 real text/JSON named-file composition and unchanged silent whole-input public API, output/error categories, dash paths and help; 2.4 complete user documentation and extraction. |
| F-004 and R-011–R-013 | All stated semantic examples and invalid matrix in 2.4; complete docs, nonempty independent product discovery and isolated extracted module exits in 2.4; cross-boundary feature review in 2.6. |
| Retained R-001–R-009 | Regressions at every delivery/review boundary for immutable results, exports/signatures, whole-input/BOM/newlines/Unicode, file ownership/input preservation, text/JSON and failures. R-010 remains deferred acquisition, with source-independent selection checked structurally. |

Detailed tests and concrete edit scopes belong to FEATURE-TASKS and existing layout. Reuse core for pure selection beside shared traversal, I/O for complete strict acquisition, CLI for validation/control/rendering, existing unit/integration suites and distribution tools. Main layout expressly allows pure selection in core for a separately accepted feature; no new source owner, directory or layout proposal is needed. PLAN QC includes this reuse assessment.

Main risks are integer conversion guards, duplicate argparse options silently overriding, normalized counting accidentally re-stripping an exposed BOM, early decode termination, changing API exports and extraction importing the checkout. Objective exits directly cover each. Complete in-memory decoding remains the accepted tradeoff; no performance target or release is introduced.

## Tracking and preparation boundary

Maintained tracking is already confirmed for eligible selected work. Phase 2 is already active; added accepted feature milestones/tasks require idempotent projection/readback of the existing exact phase label and new associations before execution. Read complete owning hierarchies for IDs; preserve all foreign issues/labels/comments/milestone prose and prior closed objects. Feature review cannot close a whole-project milestone with pending main-owned work. Projection waits for accepted FEATURE-TASKS/current QC; preparation does not create task issues or run task tests.

This preparation stops after concrete PLAN/QC and TASKS/QC acceptance and per-commit publication on design-docs, before implementation, default merge, feature branch creation, phase closure or release. No material contract choice remains unresolved; runtime-baseline integration and added-work projection are explicit future execution prerequisites. The adjacent [PLAN QC](FEATURE-PLAN-REVIEW-REPORT.md) separates technical readiness from delegated acceptance.
