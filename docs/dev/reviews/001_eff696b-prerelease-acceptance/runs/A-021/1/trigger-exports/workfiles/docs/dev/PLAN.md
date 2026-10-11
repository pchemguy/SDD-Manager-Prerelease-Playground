# TextStats delivery plan

## Objective and governing inputs

Deliver the accepted [SPEC](SPEC.md) through an early useful named-file API/CLI and then two bounded JSON/stdin increments. The [architecture](ARCHITECTURE.md), [decomposition](DECOMPOSITION.md) and current [SPEC QC](SPEC-REVIEW-REPORT.md) establish the structural and behavioral baseline. This document is strategy only: no implementation, executable task list or physical layout is supplied here.

Preserve the user's phase and milestone identities: phase 1 delivery milestones 1.1 and 1.2; phase 2 delivery milestones 2.1 and 2.2. Each phase also has a final dedicated review milestone. Accepted named-file ranges extend Phase 2 with milestones 2.4/2.5 and extent review 2.6. Existing 2.1/2.2/2.3 identities remain; whole Phase 2 requires both main and feature exits.

## Phase 1: Named-file utility

The outcome is a useful documented named-file utility with complete expected failure behavior and a verified source distribution. It begins from accepted preparation integrated and published to the actual default branch under the manager's gate, followed by eligible phase activation when confirmed tracking applies. There is no technical-skeleton milestone before useful counting.

### Milestone 1.1: Named-file counting

Scope: R-001 through R-007's API, whole-input semantics, strict UTF-8 file acquisition, BOM option, module entry, one named input, dash-prefixed filenames through `--`, successful exact text output and help. Establish nonempty discoverable unit/integration product suites (R-012) alongside implementation. The minimum integrated slice is a real named-file CLI call through the same semantics used by the silent public API, not a mocked-only path.

Dependencies are the small immutable result, pure semantics and strict acquisition boundaries required by this path. Localized implementation units can build those collaborators and integrate the CLI within this milestone. Deliver API exceptions and owned-handle closure with the file API; CLI failure diagnostics/status robustness, runnable public documentation and distribution exits follow in 1.2. JSON, stdin and range behavior are deferred.

Exit evidence: whole-input sample matrix, direct API exports/signatures/immutability/silence, string/file equivalence, strict decode/lifetime checks and subprocess named-file/BOM/help/dash-filename success. Record actual nonzero test counts for both product suites. Its final dedicated milestone review performs code review of the complete path, applicable tests/regressions, blocker repair and a committed/pushed milestone report.

Demonstrate a real UTF-8 file with mixed terminators and BOM policy through API and module CLI. This gives the human concrete usefulness/clarity evidence for continue, amend, simplify or stop at an authorized checkpoint. It does not authorize automatic steering or broaden a selected execution range.

### Milestone 1.2: Failure handling and distribution

Depends on completed/reviewed 1.1. Scope: R-008 CLI input/read/decode status 1 and usage status 2, identifying useful stderr, empty failure stdout, no traceback and validation before acquisition; R-011 public API/module docs and runnable README; R-013 extracted-source distribution; complete phase 1 R-012 acceptance and regression coverage. Preserve the useful counting/API/CLI path and unchanged input bytes.

Exit evidence: named-file failure/usage subprocess matrix and controlled read/unreadability/resource seams, successful-path regressions, documentation examples executed against delivered code, nonzero unit/integration counts and extracted-source module-entry invocation independent of the original checkout. Include successful named-file output and expected input/decode failures in distribution evidence. Its final milestone review performs code review, required tests/checks, repairs every contract/exit blocker and publishes a milestone report.

Demonstrate useful error handling and the README's runnable invocation after extraction. This checkpoint informs confidence in usability/distribution and a human continue/amend/stop decision before phase 2, within the separately authorized execution scope.

### Milestone 1.3: Phase 1 review

This dedicated review milestone contains exactly one phase code review/testing/report task, derived later in TASKS. It depends on both delivery milestones completing and, when tracking is active, closing with all constituent issues and reports. It has no separate milestone review task.

Review API/CLI/acquisition/documentation/distribution interactions, run all applicable phase 1 checks and inspect complete code/contract conformance. Resolve bugs, critical code issues and SPEC/PLAN violations; publish the phase report and establish full phase exits. Then reconcile hosted review closure if active and explicitly merge, verify and publish the complete phase into the established main integration branch before phase 2 activation. A partial milestone/task range pauses on its phase branch rather than merging by implication.

## Phase 2: JSON and stdin

The outcome extends the documented utility with alternate output and byte-based stdin while retaining the phase 1 contracts. Phase 2 begins only after phase 1 reviews, exits, required hosted closure and target integration/publication, and only within authorized execution scope. Activate/project phase 2 immediately before execution, not during preparation.

### Milestone 2.1: JSON output

Depends on phase 1 completion/integration. Scope: R-009 named-file `--json` with exactly integer `lines`/`words` fields and one final newline; `--keep-bom` composition, unchanged text default and R-008 errors. Update relevant CLI help/documentation with the delivered option and extend nonempty product tests/distribution regressions. Stdin and range remain deferred.

Exit evidence: semantic equality of text/API/JSON for representative whole-input and BOM examples, JSON shape/types, option composition, failure output/status regressions, documented named-file JSON usage and extracted-source JSON/module execution. The final milestone review performs code review, focused/regression tests, blocker repair and publishes its milestone report.

Demonstrate switching a real named-file invocation between text and JSON. Use the output contract and README clarity to inform a consequential continue/amend/simplify/stop checkpoint when selected by the human.

### Milestone 2.2: UTF-8 stdin and final delivery

Depends on completed/reviewed 2.1. Scope: R-010 stdin bytes to EOF, strict locale-independent UTF-8, retained stdin ownership, empty input and identifying read/decode failures. Compose with text/JSON/BOM policies while preserving named-file/API behavior. Complete R-011/R-012/R-013 final documentation, regression and extracted-source exits for the delivered phase. Public API stays whole-input. Retain source-independent range composition when delivering stdin; acquisition remains main-owned.

Exit evidence: subprocess byte-fed stdin in text/JSON modes with Unicode, mixed terminators, both BOM policies and empty input; invalid bytes/read errors, no partial output and no traceback; controlled borrowed-stream ownership/locale independence checks; named-file/API retained behavior. Run updated README examples, nonzero unit/integration suites and extracted-source named-file plus stdin/text/JSON module-entry checks. Its final milestone review performs whole-capability code review, tests, blocker repair and publishes a report.

Demonstrate a UTF-8 byte stream under a differing process locale and its documented output/failure behavior. This supplies final usability and portability evidence for a human accept/amend/stop decision within the separately authorized execution scope.

### Milestone 2.3: Phase 2 and final review

This dedicated review milestone contains exactly one phase code review/testing/report task. It depends on all phase 2 delivery milestones completing/closing; it has no extra milestone review task. Review cross-milestone and cross-phase interactions, all final SPEC obligations and complete distribution/documentation behavior. Run final product and distribution checks, resolve blockers and publish the phase report plus final implementation report.

Every milestone/phase report includes a TODO section (`None` when empty). Only noncritical code issues consistent with SPEC/PLAN can be deferred, with stable identity, location/evidence, impact, rationale, options/tradeoffs and owner/scope. Phase reports carry unresolved milestone findings; the final report aggregates all unresolved/deferred findings with provenance and resolution references. Contract violations and missing required evidence remain blockers.

Once full exits/reports and applicable hosted closure are verified, explicitly integrate, verify and publish the complete phase to the main target. Partial execution cannot claim project completion. Full final review includes incorporated range exits and feature report provenance after 2.4/2.5/2.6, while retaining pending stdin obligations. No release is authorized.

## Named-file range delivery extent

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

Detailed tests and concrete edit scopes belong to canonical TASKS after selected transfer and existing layout. Reuse core for pure selection beside shared traversal, I/O for complete strict acquisition, CLI for validation/control/rendering, existing unit/integration suites and distribution tools. Main layout expressly allows pure selection in core for a separately accepted feature; no new source owner, directory or layout proposal is needed. PLAN QC includes this reuse assessment.

Main risks are integer conversion guards, duplicate argparse options silently overriding, normalized counting accidentally re-stripping an exposed BOM, early decode termination, changing API exports and extraction importing the checkout. Objective exits directly cover each. Complete in-memory decoding remains the accepted tradeoff; no performance target or release is introduced.


## Coverage, dependencies and verification strategy

| SPEC obligation | Delivery route |
| --- | --- |
| R-001/R-002/R-003/R-004/R-005/R-006/R-007 | 1.1 integrated API/named-file success and associated semantic/lifetime tests; retained through every later exit. |
| R-008 | 1.2 complete CLI failure/usage handling; retained in JSON/stdin and extracted-source checks. |
| R-009 | 2.1 alternate named-file output, then composition with stdin in 2.2. |
| R-010 | 2.2 bytes/locale/lifetime/failures; public whole-input API remains unchanged. |
| R-011 | 1.2 complete public docs/README, then 2.1 relevant update and 2.2 final exits. |
| R-012 | Nonempty unit/integration suites established in 1.1, grown with each delivery capability and regressions at every review. Workflow fixtures stay separate. |
| R-013 | 1.2 first complete extracted-source exit, repeated/extended for 2.1 JSON and 2.2 final stdin behavior. |
| F-001 through F-004 | 2.4 named-file text/JSON selection and validation; 2.5 documented extracted delivery; 2.6 feature-extent review. Main stdin/final work remains pending. |

The pure core precedes its consumers within a bounded milestone; acquisition preserves raw terminators and complete strict decoding; controllers publish completed results. Check failures at component seams where portable subprocess reproduction is unreliable, but retain real module-entry integration for observable process contracts. No platform permission trick alone establishes unreadability coverage. Source extraction checks must isolate imports from the checkout and installed copies.

There is no benchmark, bounded-memory target, third-party build requirement or release publication in scope. In-memory decode is the accepted design tradeoff. Main risks are mistaken Unicode line splitting, newline translation, repeated BOM removal, silently empty discovery, environment-dependent unreadability tests and accidentally importing the checkout during distribution verification; the exits above address each with objective evidence.

## Integration and review evidence

TASKS will provide stable executable identities and bounded edit scopes from the accepted strategy and later layout. Each delivery milestone ends in a dedicated milestone code review/testing/report task; each final phase review milestone has exactly one task. Review reports follow the pinned lifecycle locations: `docs/dev/reports/phases/1/1.1.md`, `1.2.md`, `PHASE-REPORT.md`, corresponding phase 2 paths, and `docs/dev/reports/IMPLEMENTATION-REPORT.md` at final delivery. These fixed external report conventions do not allocate source files.

User-authorized GitHub tracking is confirmed for the scoped workflow, but preparation does not activate a phase. Eligible phase labels, all its milestones and task issues must be projected and verified through sdd-forge before its first task; later phases stay unprojected until eligible. Completion commits/pushes precede issue closure, milestone reviews precede milestone closure, and full phase review/closure plus integration/publication precede next-phase activation. Exact hosted objects and task mappings will be derived from accepted TASKS rather than guessed here.

## Strategy checkpoint

The adjacent [PLAN review report](PLAN-REVIEW-REPORT.md) assesses strategy conformance and the two delivery milestones per phase. The separate [layout](layout.md) has scoped delegated coordinator acceptance at `b3ba0338d71c167aaec8ca85317d09002557ea2d`, with exact evidence recorded in its checkpoint and the combined QC report. Strategy acceptance enabled that proposal, not automatic TASKS derivation or implementation. The coordinator accepted PLAN and its strategy-only report at commit `928c319ed84a919c6424adfa4522918e054a1d43`, PLAN blob `8fe5bccad16fcfda6bf554f1b82dc324a4c8f048` and report blob `70408868785610c4521266b839777a96db734126`, under delegated test-artifact review authority; published decision evidence is `af5a37a`. The scoped decision enables the separate layout proposal and combined QC, without accepting unseen TASKS or implementation.
