# TextStats executable task hierarchy

## Governing inputs and execution boundary

This complete initial two-phase hierarchy derives from accepted [PROJECT](PROJECT.md), [ARCHITECTURE](ARCHITECTURE.md), [DECOMPOSITION](DECOMPOSITION.md), [SPEC](SPEC.md), [PLAN](PLAN.md) and [layout](layout.md), with current [SPEC QC](SPEC-REVIEW-REPORT.md) and [combined PLAN QC](PLAN-REVIEW-REPORT.md). There is no pre-existing product task list or verified implementation; all checkboxes are unchecked. Monotonic project-wide IDs T-001 through T-017 are allocated here once and have exactly one executable owner.

Task details identify outcomes, likely edit scopes, prerequisite IDs and objective evidence. Each task includes its own relevant tests/docstrings/docs rather than separate padding work. The phase/milestone names match PLAN. Deferred SPEC F-001 through F-004/C-010 have no implementation task or hosted issue in this hierarchy; preserve their design seams while implementing accepted whole-input capabilities.

The user requested preparation through TASKS and stop before implementation. The coordinator accepted this concrete list and [owner QC](TASKS-REVIEW-REPORT.md) at commit `1510709f6e10d82d1b525b8c7cb221c5e1c5e20f`, TASKS blob `a4a5a4c645fd87c6d00cc057b662b1234b4adc26` and report blob `d6e9306e34157632bcf4cdea638427770edb4ad9`, under delegated test-artifact review authority; published decision evidence is `df4dfd5`. The full substantive assessment accepted this exact hierarchy/report without authorizing implementation or hosted projection. Execution selection/completion belongs to sdd-implement, not document authoring. A future implementation instruction must select its bounded range and satisfy accepted-preparation integration/publication plus eligible-phase verified tracking prerequisites. No production code or hosted projection occurs in this preparation checkpoint.

## Phase 1 — Named-file utility

- [ ] Phase 1 — Named-file utility
    - [x] Milestone 1.1 — Named-file counting
        - [x] T-001 — Implement immutable statistics and whole-text counting
            Outcome: cohesive pure core and silent public text API under R-001 through R-005, including strict integer/nonnegative constructor validation, shared terminator traversal and once-only BOM normalization.
            Scope: `textstats/core.py`, text/statistics exports in `textstats/__init__.py`, source docstrings, unittest package markers, `tests/unit/test_core.py` and public text cases in `tests/integration/test_api.py`. Do not publish undefined file exports before T-002 supplies them.
            Depends on: none within the list; execution prerequisites above apply.
            Evidence: all whole-input SPEC examples, Unicode separators/whitespace, repeated/interior BOMs, both policies, immutable value/equality and invalid constructor cases; direct imports/signatures and captured API silence. Discover focused unit and integration suites and record nonzero counts. Public file counting/module CLI remain later tasks within this same useful milestone.
        - [x] T-002 — Implement strict file acquisition and complete public API
            Outcome: R-006 byte-preserving strict UTF-8 file input and R-002 whole-file API, with required exceptions and owned-handle cleanup.
            Scope: `textstats/io.py`, complete exports in `textstats/__init__.py`, module/API docstrings, `tests/unit/test_io.py` and real-file public API cases in `tests/integration/test_api.py`.
            Depends on: T-001.
            Evidence: import all three required public names; string/file equality for the sample matrix using str and Path inputs; missing/unreadable/read-failure OSError subclasses, invalid-byte UnicodeDecodeError, no partial result, closure on every path, API silence and unchanged file bytes. Use controlled failure streams for portable cleanup/read/unreadability checks and real temporary files for decode/equivalence. Rerun core/API regressions.
        - [x] T-003 — Integrate named-file CLI and nonempty product checks
            Outcome: R-007 real module entry, exactly one input, `--keep-bom`, `--` dash-filename handling, exact text success and help; first useful end-to-end slice with R-012 collection evidence.
            Scope: `textstats/cli.py`, `textstats/__main__.py`, CLI docstrings, `tests/unit/test_cli.py`, `tests/integration/test_cli.py` and `tools/check_tests.py`.
            Depends on: T-002.
            Evidence: real subprocess named-file/BOM/mixed-terminator/empty/help/dash-filename invocations with prescribed status/stdout/stderr, API equivalence and unchanged input. The standard-library test runner discovers unit/integration independently, reports counts, rejects zero collection in either suite and propagates test failure; workflow fixtures are excluded. Demonstrate a real file through API and CLI for milestone feedback. Complete CLI failure diagnostics/status robustness follows in T-005; JSON/stdin/range remain deferred.
        - [x] T-004 — Review, test and report milestone 1.1
            Scope: complete core/acquisition/public API/CLI capability and relevant dependencies; no extra feature delivery.
            Depends on: T-001, T-002 and T-003.
            Evidence: sdd-verify code review plus applicable semantic/lifetime/API/subprocess/nonempty discovery checks; sdd-implement repairs every bug, critical issue or milestone SPEC/PLAN violation before closure. Record actual checks/counts, demonstration usefulness and evidence limits; publish milestone report with TODO section and dispositions.
            Report: [milestone 1.1 review](reports/phases/1/1.1.md).
    - [x] Milestone 1.2 — Failure handling and distribution
        - [x] T-005 — Complete named-file CLI failure and usage handling
            Outcome: R-008 complete expected error paths while preserving R-007 success/help and R-006 exceptions.
            Scope: `textstats/cli.py`, `tests/unit/test_cli.py`, `tests/integration/test_cli.py` and relevant source error documentation.
            Depends on: T-004 and milestone 1.1 completion/closure.
            Evidence: status 1 for missing/unreadable/read/decode failures with identifying cause/input stderr, empty stdout and no traceback; status 2 for missing/extra input/unknown options with useful stderr and empty stdout; validate invocation before acquisition. Exercise controlled read/unreadability seams and real subprocess missing/bad-byte inputs. Retain named-file/BOM/help/API behavior and byte preservation; run nonempty unit/integration suites.
        - [x] T-006 — Document public API and runnable named-file usage
            Outcome: R-011 public API/module reference and runnable README for delivered phase 1 behavior.
            Scope: `docs/public-api.md`, `README.md`, public module/function docstrings and discoverability links in `AGENTS.md` as needed.
            Depends on: T-005.
            Evidence: document all three exports/signatures, constructor invariants, count/BOM/strict UTF-8/exception/lifetime/silence contracts, setup/check commands, exact text/help/status usage and planned distribution boundary. Execute every runnable named-file/API/help example against delivered code and current suites; documentation advertises neither JSON/stdin nor range as delivered.
        - [x] T-007 — Build and verify isolated source distribution
            Outcome: R-013 allowlisted source archive and extracted-source module-entry acceptance, completing phase 1 distribution exits.
            Scope: `tools/package_source.py`, `tools/check_distribution.py`, `tests/integration/test_distribution.py`, distribution instructions in README and necessary generated-artifact ignore rules while preserving existing rules.
            Depends on: T-005 and T-006.
            Evidence: build `dist/textstats-source.zip` with approved top-level/package/docs/disclosure/tool contents; exclude credentials/caches/coordinator resources/workflow fixtures. Extract temporarily, sanitize checkout import paths, verify imported package belongs to extraction, and actually invoke its `python -m textstats` from extracted source cwd. Check text/BOM/named-file success and input/decode/usage failures, exact outputs/statuses and unchanged inputs. Run archive/check integration plus nonempty product suites and the documented extracted-source example. No third-party build dependency or release publication.
        - [x] T-008 — Review, test and report milestone 1.2
            Scope: complete named-file robustness, API/module docs, README and source distribution plus retained 1.1 behavior.
            Depends on: T-005, T-006 and T-007.
            Evidence: code review and complete milestone failure/regression/docs/nonempty discovery/extracted-source exits; repair every blocker before closure. Record usability/distribution demonstration, actual commands/counts and TODO section with allowed deferral evidence.
            Report: [milestone 1.2 review](reports/phases/1/1.2.md).
    - [ ] Milestone 1.3 — Phase 1 review
        - [ ] T-009 — Review, test and report phase 1
            Scope: cross-milestone/API/CLI/resource/docs/distribution code review and all phase 1 exits.
            Depends on: T-004 and T-008, and completed/closed delivery milestones 1.1 and 1.2; excludes its own still-open review milestone.
            Evidence: full phase code review plus applicable product/docs/extracted-source checks, actual nonzero suite counts, blocker repairs and phase report carrying unresolved milestone findings/TODOs. Commit/push report and task completion, reconcile eligible hosted closures, then full phase integration/merged-state verification/publication under the manager gate. No partial-range merge or phase 2 activation before these exits.
            Report: `docs/dev/reports/phases/1/PHASE-REPORT.md`.

## Phase 2 — JSON and stdin

- [ ] Phase 2 — JSON and stdin
    - [ ] Milestone 2.1 — JSON output
        - [ ] T-010 — Add JSON CLI output with retained text behavior
            Outcome: R-009 named-file JSON with only integer lines/words, one object plus newline and unchanged default text/errors.
            Scope: `textstats/cli.py`, unit rendering/parser checks, `tests/integration/test_cli.py`, delivered-option help, README and API/module CLI documentation.
            Depends on: T-009, completed phase 1 integration/publication and verified authorized phase 2 activation.
            Evidence: parse subprocess JSON and assert exact keys/integer types/count equality for semantic/BOM examples and option composition; assert text default remains exact and errors retain empty stdout/status/diagnostics. Run nonempty suites and documented JSON examples. Stdin and range remain deferred.
        - [ ] T-011 — Verify JSON from extracted source
            Outcome: extend R-013 distribution acceptance to the delivered alternate format and retained named-file behavior.
            Scope: `tools/check_distribution.py`, `tests/integration/test_distribution.py` and extracted-source JSON instructions in README.
            Depends on: T-010.
            Evidence: rebuild/extract allowlisted source and invoke extracted module for JSON/BOM plus text/error regressions; verify isolated import location, object keys/types/count equality and exact process statuses/streams. Run nonempty product suites and documented archive examples. This delivery check extends portability evidence, not a duplicated code-review/report task.
        - [ ] T-012 — Review, test and report milestone 2.1
            Scope: JSON integration and all affected named-file/text/error/docs/distribution contracts.
            Depends on: T-010 and T-011.
            Evidence: code review plus JSON/composition/default/failure and extracted-source checks, blocker repairs, actual counts and demonstration feedback; publish report with TODO dispositions.
            Report: `docs/dev/reports/phases/2/2.1.md`.
    - [ ] Milestone 2.2 — UTF-8 stdin and final delivery
        - [ ] T-013 — Add borrowed binary stdin acquisition
            Outcome: R-010 internal byte reader reaching EOF, strict locale-independent UTF-8 and retained stream ownership; no new public API export.
            Scope: `textstats/io.py`, `tests/unit/test_io.py` and input ownership/decode docstrings.
            Depends on: T-012 and milestone 2.1 completion/closure.
            Evidence: borrowed byte-stream empty/Unicode/mixed-terminator/BOM inputs, EOF, invalid bytes and controlled read errors; never close borrowed stream on success/failure; no partial decoded result. Verify named-file acquisition/API regressions. CLI consumer follows in T-014 within the same milestone.
        - [ ] T-014 — Integrate stdin across text and JSON CLI
            Outcome: R-010 input `-` through R-007/R-009 policies with R-008 error categories and unchanged named-file/public API behavior.
            Scope: `textstats/cli.py`, `tests/unit/test_cli.py`, `tests/integration/test_cli.py`, help/README stdin usage and error documentation.
            Depends on: T-013.
            Evidence: real byte-fed subprocess stdin in text/JSON modes with both BOM policies, Unicode/mixed terminators/empty data; invalid bytes and controlled read errors identify stdin, return 1, leave stdout empty and avoid traceback. Check under differing locale, preserved borrowed-stream ownership at controlled seams, named-file `./-`, option/usage regressions and no input mutation. Run nonempty suites and newly runnable stdin examples.
        - [ ] T-015 — Complete final documentation and source-package exits
            Outcome: final R-011/R-012/R-013 usability/portability acceptance across delivered API/named-file/JSON/stdin behavior.
            Scope: public API/module reference, README final instructions, `tools/check_distribution.py`, `tests/integration/test_distribution.py` and truthful root navigation.
            Depends on: T-014.
            Evidence: complete docs for final stdin ownership/strict decode/status/composition; execute all final documented examples. Rebuild/extract and actually invoke module entry for named-file and byte-fed stdin in text/JSON/BOM/empty/bad-byte/usage cases, maintaining import isolation. Run complete nonzero unit/integration suites and retain whole-input API/signatures. Range remains documented as future scope only, without runnable delivery claims.
        - [ ] T-016 — Review, test and report milestone 2.2
            Scope: complete stdin/input-source composition, documentation/distribution and prior delivered regressions.
            Depends on: T-013, T-014 and T-015.
            Evidence: code review plus source/format/BOM/locale/failure/ownership/nonempty discovery/extracted-source exits; repair all blockers and record final usability evidence, actual checks/counts and TODO dispositions.
            Report: `docs/dev/reports/phases/2/2.2.md`.
    - [ ] Milestone 2.3 — Phase 2 and final review
        - [ ] T-017 — Review, test and report phase 2 and final delivery
            Scope: cross-phase and cross-milestone code review, complete accepted initial SPEC/PLAN, final docs/source distribution and retained API/named-file behavior.
            Depends on: T-012 and T-016, and completed/closed delivery milestones 2.1 and 2.2; excludes its own still-open review milestone.
            Evidence: final code review plus all applicable product/docs/distribution checks, actual nonzero counts and blocker repairs. Publish phase report and final implementation report aggregating unresolved/deferred findings from every milestone/phase, with provenance, options/tradeoffs, owners and resolution references. Then reconcile required hosted closures and complete full-phase merge/verification/publication. Do not execute range feature or publish a release.
            Reports: `docs/dev/reports/phases/2/PHASE-REPORT.md` and `docs/dev/reports/IMPLEMENTATION-REPORT.md`.

## Completion and persistence rules

Every review task requires both code review and actual testing; tests alone cannot close it. Reports record actual scope/checks/counts/evidence limits, blockers and a TODO section (`None` when empty). Fix bugs, critical code issues and SPEC/PLAN violations before review closure. Only eligible noncritical issues consistent with contracts/exits can be deferred, with stable ID, located evidence, impact, rationale, options/tradeoffs and follow-up owner/scope. Required or uncertain repairs stay in Findings/Blockers.

During future execution, the initial owning checkbox and one task's result/evidence close together in exactly one task commit whose subject starts with exactly one `[T-NNN]` marker. Push and verify every workflow-owned commit before advancing; then reconcile its issue. Complete/review each delivery milestone before its hosted closure; complete all delivery milestones before the dedicated phase review. Exactly one task owns each initial closure. Parent completion is evidence-backed; no task is marked complete by this preparation.

Hosted tracking reads this complete hierarchy but projects only the eligible phase after actual task-list acceptance and implementation prerequisites. Every eligible task includes its phase label and parent milestone association. Required unknown/incomplete projection blocks execution, while later phases and the range feature stay unprojected. The final task-list checkpoint remains the current stopping boundary before any implementation or hosted projection.

## T-001 completion evidence

The current request supersedes the historical preparation-only stopping statements for exactly the first executable Phase 1 task. Selected T-001 in milestone 1.1, with no task dependency. Accepted preparation tip `1e3305c8659045945244c06861079fef879ca3c3` was explicitly merged into actual default `main`, parent `eff696b38f0b8a94bd6f91ca1c64d54fd714df46`, as `88a5c4b4424f4bba76940e40b1d6523b1f6fe191`; merged document hashes, local links, heading spacing and document-only scope were verified and that exact remote tip read back before creating `phase/1-named-file-utility` from it. The accepted disclosure's two pre-existing whitespace warnings were preserved.

Maintained Phase 1 tracking is confirmed by the current request. Before task edits/tests, provider readback verified `sdd-phase-1-Named-file-utility`, native milestones 1–3 (1.1, 1.2, 1.3), and unique marked T-001 through T-009 issues 2–10 with their phase label and correct milestone association. T-001 uniquely maps to `pchemguy/SDD-Manager-Prerelease-Playground#2`, milestone 1. Existing unrelated labels, issue text/comments and milestone content are preserved; later phases remain unprojected.

Delivered immutable, equal-by-value integer/nonnegative statistics excluding bool, shared CRLF/CR/LF segment traversal preserving terminators, exactly-once whole-input BOM normalization, normalized counting using Unicode `str.split`, and the silent direct text facade. Internal traversal/counting allow later selection without renormalizing interior BOMs. Module/class/function docstrings describe the delivered contracts. File exports, acquisition, CLI, tools and public API guide are not delivered by this task. Narrow product cache ignores preserve existing rules.

On Python 3.12.14 from the repository root, tests were written first. The initial unit discovery failed to import the absent package and is classified as setup failure, not behavioral RED. Minimal unimplemented declarations then enabled actual RED: unit discovery collected 10 tests and failed with 21 validation/equality/immutability failures and 43 missing-counting errors; integration discovery collected 5 tests and failed with two missing-counting errors. No test-first exception is claimed.

After implementing the contracts, `python -m unittest discover -s tests/unit -t . -v` passed all 10 tests and `python -m unittest discover -s tests/integration -t . -v` passed all 5 tests, without skips or warnings. Evidence covers every whole-input SPEC matrix row under both policies; Unicode separators/whitespace and non-ASCII words; mixed/consecutive/final terminators; repeated/interior BOMs; equality, invalid fields and assignment/deletion immutability; direct exports/signatures, keyword-only policy, repeated-call independence and import/call silence. Verification also inspects source/document contracts and preserved internal segment seams. Coverage is T-001 on this runtime, not full Python-version, file/API, CLI or distribution acceptance. The future check tools are absent because their owning tasks are unselected.

Exactly T-001's result, tests, documentation, current evidence and initial checkbox close together in its task commit. Publication and issue closure are subsequent observed operations reported in the workflow handoff. All parents and T-002 through T-017 remain unchecked. Stop after the verified push and hosted reconciliation of T-001; do not integrate the incomplete phase or start another task.

## T-002 completion evidence

The milestone 1.1 request selects T-002 through T-004 and supersedes historical first-task/preparation stops only within this boundary. Startup clean branch/remote tip was `9dc8075dd1b96d3a2744717a9d6d98a3024acbec`; its T-001 result/evidence/initial checkbox and single-ID subject were inspected and compliant. Accepted preparation remains published on main `88a5c4b4424f4bba76940e40b1d6523b1f6fe191`. Current SPEC/PLAN/layout and adjacent Ready owner reviews retain unchanged governing contracts; TASKS differs only in T-001 completion evidence/status, which does not invalidate hierarchy QC. Maintained phase tracking readback returned the phase label, milestones 1–3 and unique marked T-001–T-009 issues 2–10 with correct parent associations before task edits/tests. T-002 maps uniquely to issue #3, milestone #1; T-001 issue #2 is closed.

Delivered complete binary read followed by strict UTF-8 decoding, silent count_file with the prescribed keyword-only BOM policy and all three direct exports. The owned context manager closes on successful read, decode failure and read failure; OSError subclasses propagate unchanged, and input bytes/terminators are preserved. Module and function documentation describe the actual API and lifetime boundary.

Tests preceded production behavior. With an unimplemented count_file declaration (so import/collection was valid), `python -m unittest discover -s tests/unit -t . -v` collected 14 tests and failed with six behavioral NotImplementedError errors at the acquisition scenarios; the ten core tests stayed green. After production implementation, that command passed 14 tests and `python -m unittest discover -s tests/integration -t . -v` passed 8 tests on Python 3.12.14 without skips or warnings. Coverage includes controlled success/read/decode/open failures and closed handles, PermissionError/FileNotFoundError/IsADirectoryError propagation, real-file strict decode and missing path, all whole-input matrix rows under both policies using str and Path arguments, Unicode content, exact byte preservation, direct exports/signature and API silence. Source and docstring inspection confirms no CLI dependency or fallback decoding. No TDD exception; broader CLI/distribution and other runtimes remain unverified. Exactly this task's result/tests/documentation/evidence/initial checkbox close together before publication and issue reconciliation; remaining milestone tasks and all parents stay open.

## T-003 completion evidence

T-002 was closed durably at `f28f6e415b3e0c13353a61e82354c47b0d2cabb2`, pushed and read back as exact remote phase tip before T-003 work. Provider readback confirms its issue #3 closed/completed with the evidence comment; recovery after an overbroad Link-header guard independently read actual closed state and the existing comment without duplicating writes. T-003 uniquely maps to maintained issue #4, milestone #1.

Delivered module-entry CLI, exactly one named input, useful no-acquisition help, `--keep-bom` before/after the input, `--` option termination and exact completed text output. A literal `-` is still a named file. The CLI shares count_file; no independent semantics or new API exports. Source docstrings describe the current success/help and intentionally incomplete next-milestone input-failure diagnostics. README/orientation now identify delivered capabilities without advertising future docs/distribution.

Tests preceded behavior. `python -m unittest tests.unit.test_cli -v` collected seven tests and failed with four assertions and five NotImplementedError errors against unimplemented CLI and a runner that incorrectly returned success without discovery. These are observed behavioral RED failures, including both empty-suite rejection and propagation of a product failure. `python tools/check_tests.py` subsequently passed 21 unit and 12 integration tests on Python 3.12.14, without skips/warnings. The runner reports independent counts, rejects zero in either suite, executes both real product suites and propagates failure. Its subprocess fixtures exercise empty unit, empty integration, failure propagation, successful independent counts and exclusion of deliberately failing workflow fixtures.

Real module processes verify named UTF-8/mixed terminator/Unicode/BOM/empty input, exact status/stdout/stderr, before/after BOM option order, help without input, required single input and actual dash-prefixed names after `--`, including a file named `--keep-bom` and literal `-`. API equality and unchanged bytes are checked. Controlled CLI seams assert default/retaining policy and help without acquisition. Source/docstring/staged-scope review found no current contract violation. Complete R-008 diagnostics/status robustness, standalone public docs/distribution, JSON/stdin/range and other runtimes remain outside this task. The named-file useful demonstration and coherent milestone review follow in T-004; milestone/phase remain unchecked here.

## T-004 completion evidence

Completed the separate coherent milestone implementation code review, actual nonempty runner, API/module demonstration and exit assessment in [milestone 1.1 report](reports/phases/1/1.1.md), reviewed at published T-003 source `373203d6f41bee2229eed900b761de8669678e0b`. The runner passed 21 unit and 12 integration tests on Python 3.12.14, with no skips/warnings. Mixed-terminator/non-ASCII/BOM temporary-file API and real CLI returned three lines/four words with exact streams/status and unchanged bytes; BOM-only default versus retaining calls visibly produced zero/zero versus one/one. Source review found no milestone contract blocker and no required repair; TODO is None. Full runtime/platform matrix, complete CLI failure diagnostics, public guide/distribution and later phase capabilities remain unverified/planned in their owning tasks.

T-002/T-003 separate closing commits were inspected and published before this review; provider readback confirms issues #3/#4 closed/completed with evidence, and T-001 #2 remains closed. Unique T-004 issue is #5 in native milestone #1. The report/evidence, initial T-004 checkbox and eligible milestone 1.1 parent close together; phase and unselected tasks remain unchecked. Publish/read back this task commit before closing issue #5, then validate all milestone-associated task issues and close/read back milestone #1. Stop on the incomplete phase branch, with main unchanged and no release or T-005 work.

## T-005 completion evidence

The complete-phase request selects T-005 through T-009 and explicit full-phase integration, superseding the historical Phase 1 partial stops. Startup published phase tip `7d003c1cf31c994340d8644e95990ef2253754ed` and main `88a5c4b4424f4bba76940e40b1d6523b1f6fe191` were read back exactly; latest T-004 closing result/report/evidence/initial checkbox composition is compliant. Current SPEC/PLAN/layout hashes match the accepted Ready owner reports, and TASKS changes only completion/evidence, preserving reviewed hierarchy/contracts. Provider readback verified all nine uniquely marked Phase 1 task issues #2–#10 with phase label and milestones #1–#3, and T-001–T-004 issues plus milestone #1 closed. T-005 uniquely maps to #6 in milestone #2; unrelated hosted material is retained.

Tests preceded the production change. `python -m unittest tests.unit.test_cli.CliTests tests.integration.test_cli -v` ran 12 tests with four errors and four failures: expected controlled FileNotFoundError/PermissionError/read OSError/decode errors escaped, real module missing-file failures exposed tracebacks and bad-byte failures omitted the input identity. These are meaningful behavioral RED. Usage-before-acquisition cases already passed. The CLI now catches only expected OSError/UnicodeDecodeError, emits identifying input/cause stderr, returns 1 and leaves stdout empty. Parsing precedes acquisition and retains status 2, success/help/BOM/dash-file contracts and silent API exceptions.

`python tools/check_tests.py` passed 23 unit and 14 integration tests on Python 3.12.14, no skips/warnings; `git diff --check` passed. Controlled open/read/decode/owned-handle checks and CLI failures, real subprocess missing/bad-byte inputs under both BOM policies, invocation errors before acquisition, exact success/help streams, API semantics and unchanged bytes are covered. Source/docstring inspection found no scoped contract blocker. Broader runtime/platform coverage, public guide and distribution remain later selected tasks; Phase 2 stays unselected. Result/tests/source documentation/current evidence and initial T-005 checkbox close together before publication and issue #6 reconciliation.

## T-006 completion evidence

T-005 closing commit `809f045e3cd32445e7dca29d0174ea25aa5da7ea` was pushed and exact remote containment verified before documentation work; provider issue #6 is closed/completed with evidence. T-006 maps uniquely to #7, milestone #2. Delivered [public API/module reference](../public-api.md), runnable README setup/named-file/API/BOM/help/check examples, precise constructor/signature/counting/decode/exception/ownership/silence contracts and module responsibility navigation. Source docstrings were inspected against the guide and already satisfy the delivered boundaries. Root AGENTS retains controlling instructions and now reflects the authorized complete-phase stop and real public guide. Distribution is explicitly planned pending T-007; JSON/stdin/ranges are not advertised as delivered.

Every runnable bash/Python fence in README and the public guide was executed verbatim in repository context on Python 3.12.14. The sample produced exact `lines=3 words=5`, BOM default/retaining produced zero/zero and one/one, dash-file produced one/two, help succeeded, and silent API assertions passed. Runner and separate documented discover commands each passed 23 unit and 14 integration tests with no skips/warnings. Local user-guide links resolve; changed diff whitespace passed. Temporary example inputs were cleaned. This documentation-only task adds no behavioral code and requires no fabricated RED cycle; existing source coverage supports the inspected contracts. External notice links and other runtimes were not revalidated. Documentation/navigation/evidence/initial checkbox close together before publication and issue #7 reconciliation.

## T-007 completion evidence

T-006 `fde1537b5c4ba1bcef4f538dfb47276d564e4aaa` was published/read back exactly and issue #7 closed/completed before this task. T-007 uniquely maps to #8 in milestone #2. Added explicit eleven-file standard-library source builder at `tools/package_source.py`, extraction checker at `tools/check_distribution.py`, independent distribution integration checks, narrow tool-cache ignore and real distribution instructions/navigation. Existing ignore rules and coordinator resources remain intact. The ZIP has `textstats-source/` root and exactly five package modules, README, public API guide, two disclosure/usage notices and builder/checker. Credentials/caches/tests/development/coordinator/workflow material is excluded. Required missing/symlink source files fail, rather than silently producing an incomplete allowlist.

Tests preceded production functionality. With valid importable NotImplementedError declarations, `python -m unittest tests.integration.test_distribution -v` ran four tests and failed with three errors and one assertion failure, demonstrating absent packaging and checker behavior. Source review corrected the controlled faulty-archive test's CLI path before implementation; no false sensitivity claim is made for that earlier fixture. After implementation, the same four tests passed, including exact content/byte allowlist under harmless unrelated-file pollution, checkout-PYTHONPATH pollution and rejection of a deliberately wrong extracted CLI while the checkout remains healthy. No copied real credential enters a fixture.

`python tools/check_tests.py` passed 23 unit and 18 integration tests on Python 3.12.14, no skips/warnings. `python tools/check_distribution.py` verified exact extracted import path and 35 actual `python -s -m textstats` invocations from temporary extracted cwd with inherited PYTHONPATH/PYTHONHOME removed and user-site packages disabled: fourteen semantic/Unicode/terminator/BOM cases under both policies, dash-file success, missing/decode failures, three usage errors and help. Exact success/status/streams, input identity/cause/no traceback and unchanged sample/bad/dash bytes were verified; temporary extractions clean up on failure too. The checker builds an ignored archive and imports no checkout product code for acceptance.

Every updated README/public-guide runnable fence, including builder/checker and a separate Bash extraction/example, executed successfully. The extracted example returned exact three lines/five words; checkout-only test commands are explicitly distinguished from archive tools. Local user-guide links and diff whitespace passed. Other runtimes/platforms, locale-varied stdin, JSON/ranges, installed packaging and release publication remain unverified/outside Phase 1. Result/tests/docs/evidence/initial checkbox close together before publication and issue #8 reconciliation.

## T-008 completion evidence

Performed coherent milestone code review of the package/acquisition/API/CLI, tests/runner, docs and distribution, separately from test execution; scope, located finding M1.2-001, repair/RED/GREEN and exit assessment are in [milestone 1.2 report](reports/phases/1/1.2.md). Fixed argparse's unintended abbreviation acceptance after two targeted regression tests failed (input acquisition for `--keep` and status 1 rather than 2). `allow_abbrev=False` now rejects unsupported spelling before acquisition; extracted checker includes the additional regression and README truthfully reports 36 cases.

`python tools/check_tests.py` passed 23 unit and 18 integration tests on Python 3.12.14 without skips/warnings; `python tools/check_distribution.py` verified isolated extracted import and 36 actual module processes. Current source review found no remaining milestone blocker, docs/examples retain applicable executed evidence and TODO is None. T-005–T-007 commits were separately published/read back and issues #6–#8 closed before this review. T-008 uniquely maps to issue #9/milestone #2. Report, scoped repair/tests/docs, evidence, initial task checkbox and eligible milestone parent status close together; publish/read back before review issue closure and milestone #2 validation/closure. Phase review remains unchecked until that hosted gate succeeds.
