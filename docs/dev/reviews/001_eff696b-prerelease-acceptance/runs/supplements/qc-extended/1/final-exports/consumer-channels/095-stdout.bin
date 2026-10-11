# Named-file ranges delivery plan

## Accepted inputs and bounded objective

The [feature specification](FEATURE-SPEC.md) and [SPEC QC](FEATURE-SPEC-REVIEW-REPORT.md) at `b0f93cf170addc80a92541acc4151058e57b6e64` were accepted by delegated coordinator decision `ca0eded9d6e8a7f40ba4e3c9ed4d8370b884db6d`. Reuse main [architecture](ARCHITECTURE.md), [decomposition](DECOMPOSITION.md), [PLAN](PLAN.md) and [layout](layout.md). This delta activates deferred F-001–F-004 with an early meaningful named-file range path, then complete documented/extracted-source exits. It does not change main stdin delivery or claim full Phase 2 completion.

## Phase and milestone strategy

Reuse the exact existing parent identity **Phase 2 — JSON and stdin**, with a feature-only extent and new noncolliding milestone IDs. Existing 2.1/2.2/2.3 retain their meanings, tasks and ownership in main TASKS. Feature completion/checks cover only added milestones; whole Phase 2 remains incomplete until its independent stdin/final obligations are met. A feature extent's final review does not replace the main phase review.

| Parent / new milestone | Useful outcome, prerequisites and objective exits |
| --- | --- |
| Phase 2 / 2.4 — Named-file ranges | Earliest usable changed path: both range spellings, ASCII/unbounded validation before access, pure selection, complete file decoding, once-only BOM, default text and JSON. Prerequisite: completed published JSON milestone 2.1 and compatible execution baseline. Keep internal normalization/selection/counting independently checkable while integrating promptly with real named-file CLI. Exit: complete F-001–F-004 core/CLI matrices, controlled acquisition and real module checks, nonempty suites, runnable minimal help/usage and retained API/whole-input/JSON regressions; dedicated milestone code review/testing/report. |
| Phase 2 / 2.5 — Range documentation and distribution | Complete public/module and runnable README explanation plus isolated extracted-source text/JSON range exits. Prerequisite: reviewed/closed feature milestone 2.4. Exit: accurate named-file/deferred-stdin docs, executed documented examples, real extracted module with provenance isolation across valid/invalid/huge/BOM/decode cases, nonempty regressions and dedicated milestone code review/testing/report. |
| Phase 2 / 2.6 — Range feature review | Dedicated final single-task review of this feature extent after 2.4 and 2.5 complete/close. Review cross-milestone interactions, all F contracts and affected R contracts; run full relevant product/docs/distribution checks, repair blockers and aggregate TODOs in feature reports. This closes the feature's extent only; main 2.2/2.3 and T-013–T-017 remain pending. |

There are two delivery milestones plus one excluded feature-extent review milestone. A larger phase split would pad this narrow capability or force unrelated stdin. Milestone 2.4's semantic parser/selection/acquisition integration is one user-visible outcome; 2.5 independently proves usable source-package delivery. Each delivery milestone includes its own final review outcome. No mock-only infrastructure milestone delays useful behavior.

At 2.4 demonstrate selecting middle/beyond-EOF/blank/mixed-terminator lines and exposed BOMs in real text/JSON invocations. The evidence informs a human continue/amend/simplify/stop decision about semantics and CLI usability. At 2.5 demonstrate documented usage from the extracted package and compare API compatibility. These are consequential feedback checkpoints for a later authorized implementation, without automatically authorizing steering or extra tasks.

## Baseline and integration dependencies

Preparation starts at default `main` `e7cae5b2216ff7dd311b6f7296d829d1927a6a8a` on the package's design-docs branch. Observed separately published JSON milestone 2.1 is `e63b8946bbb99347b0f73f070f9c728945ee5925` on paused `phase/2-json-and-stdin`; its T-010–T-012 are complete while T-013–T-017 remain pending. Main currently lacks JSON. No feature task may execute against the text-only default baseline while claiming text/JSON completion.

For a later separately authorized implementation, first merge/verify/publish accepted preparation into the actual refreshed default branch; only then create the feature implementation branch from that baseline. Establish `phase/2-json-and-stdin` as the intended implementation integration target and incorporate its verified published completed JSON checkpoint into the feature branch through an explicit verified/published compatible merge before feature execution. Preserve pending stdin/final work and original completed evidence. If histories, ownership or JSON state changed, the coordinator resolves that compatibility before execution; never reset/replay completed work or merge the incomplete phase into default by implication.

After authorized feature implementation, incorporate only the accepted feature targets needed for coherence through sdd-integrate-feature, including explicit task ownership/reconciliation scope. Preserve main pending obligations while updating their affected range composition/documentation dependencies. Archive only eligible incorporated feature sources; feature reports remain under the package prefix. Final explicit verified/published feature merge targets the paused phase, not default as a false complete Phase 2. Those are later execution/integration obligations, not actions in this preparation.

## Coverage and verification strategy

| Contract group | Delivery route and required evidence |
| --- | --- |
| F-001 | 2.4 parser validation and acquisition-order checks: signs/whitespace/Unicode/zero/reversal/open/extra-colon/missing/repeated, both spellings, huge ASCII decimals and leading zeros. No arbitrary conversion limit. |
| F-002 | 2.4 pure/shared logical-line traversal and once-only normalization; complete strict decode before selection including bytes after END, EOF subsets, blank/mixed/final lines and exposed interior BOM. |
| F-003 | 2.4 real text/JSON named-file composition and unchanged silent whole-input public API, output/error categories, dash paths and help; 2.5 user documentation and extraction. |
| F-004 and R-011–R-013 | All stated semantic examples and invalid matrix in 2.4; complete docs, nonempty independent product discovery and isolated extracted module exits in 2.5; cross-boundary feature review in 2.6. |
| Retained R-001–R-009 | Regressions at every delivery/review boundary for immutable results, exports/signatures, whole-input/BOM/newlines/Unicode, file ownership/input preservation, text/JSON and failures. R-010 remains deferred acquisition, with source-independent selection checked structurally. |

Detailed tests and concrete edit scopes belong to FEATURE-TASKS and existing layout. Reuse core for pure selection beside shared traversal, I/O for complete strict acquisition, CLI for validation/control/rendering, existing unit/integration suites and distribution tools. Main layout expressly allows pure selection in core for a separately accepted feature; no new source owner, directory or layout proposal is needed. PLAN QC includes this reuse assessment.

Main risks are integer conversion guards, duplicate argparse options silently overriding, normalized counting accidentally re-stripping an exposed BOM, early decode termination, changing API exports and extraction importing the checkout. Objective exits directly cover each. Complete in-memory decoding remains the accepted tradeoff; no performance target or release is introduced.

## Tracking and preparation boundary

Maintained tracking is already confirmed for eligible selected work. Phase 2 is already active; added accepted feature milestones/tasks require idempotent projection/readback of the existing exact phase label and new associations before execution. Read complete owning hierarchies for IDs; preserve all foreign issues/labels/comments/milestone prose and prior closed objects. Feature review cannot close a whole-project milestone with pending main-owned work. Projection waits for accepted FEATURE-TASKS/current QC; preparation does not create task issues or run task tests.

This preparation stops after concrete PLAN/QC and TASKS/QC acceptance and per-commit publication on design-docs, before implementation, default merge, feature branch creation, phase closure or release. No material contract choice remains unresolved; runtime-baseline integration and added-work projection are explicit future execution prerequisites. The adjacent [PLAN QC](FEATURE-PLAN-REVIEW-REPORT.md) separates technical readiness from delegated acceptance.
