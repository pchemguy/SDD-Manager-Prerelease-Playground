# TextStats executable task hierarchy

## Governing inputs and execution boundary

This complete two-phase hierarchy derives from [PROJECT](PROJECT.md),
[ARCHITECTURE](ARCHITECTURE.md), [DECOMPOSITION](DECOMPOSITION.md), [SPEC](SPEC.md),
[PLAN](PLAN.md) and [layout](layout.md), with current adjacent SPEC/PLAN/TASKS QC.
TASKS is the sole executable owner of T-001–T-024. Phase 1 is complete on default;
historical JSON evidence remains preserved, while its delivery scope is withdrawn.
Named-file range T-018–T-024 and added milestones 2.4–2.6 are reviewed, published
and hosted-closed. Retained range acceptance is text/count/BOM/ranges. The accepted
text-only amendment is integrated and published at `77e7106e3134cc7053a2b1a045cf1a76cf0361ea`,
with final delegated publication acceptance `963d058`. Historical results below remain unchanged.
[Archived feature sources](features/002_e7cae5b-named-file-ranges/README.md) are
historical snapshots, not additional executable owners.

Task details identify bounded outcomes, scopes, prerequisites and objective
checks. Each owns relevant tests/docs without padding; parent identities match
PLAN. Current task status below tracks authorized stdin/final T-013–T-017.
Their source-independent range composition/dependencies remain
required. A feature extent parent does not establish whole-project completion.

Execution selection/completion belongs to sdd-implement. The explicit resume
instruction authorizes T-013–T-017, all final Phase 2 exits, managed hosted closures
and verified two-parent integration/publication into established `main`.
Startup preparation/hosted-association and bounded closure-plan acceptance is
`fb98e7b984134755845fc46390381d9933aa397e`. Historical amendment-only stops do not
limit this resume. Stop after published Phase 2 integration; no next phase,
version bump or release is authorized.

## Phase 1 — Named-file utility

- [x] Phase 1 — Named-file utility
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
            Evidence: real subprocess named-file/BOM/mixed-terminator/empty/help/dash-filename invocations with prescribed status/stdout/stderr, API equivalence and unchanged input. The standard-library test runner discovers unit/integration independently, reports counts, rejects zero collection in either suite and propagates test failure; workflow fixtures are excluded. Demonstrate a real file through API and CLI for milestone feedback. Complete CLI failure diagnostics/status robustness follows in T-005; stdin/range remain deferred.
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
            Evidence: document all three exports/signatures, constructor invariants, count/BOM/strict UTF-8/exception/lifetime/silence contracts, setup/check commands, exact text/help/status usage and planned distribution boundary. Execute every runnable named-file/API/help example against delivered code and current suites; documentation advertises neither stdin nor range as delivered.
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
    - [x] Milestone 1.3 — Phase 1 review
        - [x] T-009 — Review, test and report phase 1
            Scope: cross-milestone/API/CLI/resource/docs/distribution code review and all phase 1 exits.
            Depends on: T-004 and T-008, and completed/closed delivery milestones 1.1 and 1.2; excludes its own still-open review milestone.
            Evidence: full phase code review plus applicable product/docs/extracted-source checks, actual nonzero suite counts, blocker repairs and phase report carrying unresolved milestone findings/TODOs. Commit/push report and task completion, reconcile eligible hosted closures, then full phase integration/merged-state verification/publication under the manager gate. No partial-range merge or phase 2 activation before these exits.
            Report: [phase 1 review](reports/phases/1/PHASE-REPORT.md).

## Phase 2 — Ranges and stdin

- [ ] Phase 2 — Ranges and stdin
    - Milestone 2.1 — Withdrawn historical JSON increment (no current delivery work)
        - T-010 — Retired JSON CLI delivery; historically completed, capability withdrawn.
            Original result and publication evidence below remain historical. No replacement task, current JSON acceptance or new completion is claimed.
        - T-011 — Retired JSON extraction delivery; historically completed, capability withdrawn.
            Original result and publication evidence below remain historical. Retained extraction acceptance belongs to T-007/T-022 and this amendment.
        - T-012 — Historical milestone 2.1 review; retained, no current executable work.
            Original review/publication remains historical; current retained contracts are reassessed by the steering report.
    - [ ] Milestone 2.2 — UTF-8 stdin and final delivery
        - [x] T-013 — Add borrowed binary stdin acquisition
            Outcome: R-010 internal byte reader reaching EOF, strict locale-independent UTF-8 and retained stream ownership; no new public API export.
            Scope: `textstats/io.py`, `tests/unit/test_io.py` and input ownership/decode docstrings.
            Depends on: T-009 and the verified text-only/range amendment checkpoint.
            Evidence: borrowed byte-stream empty/Unicode/mixed-terminator/BOM inputs, EOF, invalid bytes and controlled read errors; never close borrowed stream on success/failure; no partial decoded result. Verify named-file acquisition/API regressions. CLI consumer follows in T-014 within the same milestone.
        - [x] T-014 — Integrate stdin across text CLI
            Outcome: R-010 input `-` through R-007 policy with R-008 error categories and unchanged named-file/public API behavior.
            Scope: `textstats/cli.py`, `tests/unit/test_cli.py`, `tests/integration/test_cli.py`, help/README stdin usage and error documentation.
            Depends on: T-013 and reviewed range feature T-024.
            Evidence: real byte-fed subprocess stdin in text modes with both BOM policies, Unicode/mixed terminators/empty data; invalid bytes and controlled read errors identify stdin, return 1, leave stdout empty and avoid traceback. Check under differing locale, preserved borrowed-stream ownership at controlled seams, named-file `./-`, option/usage regressions and no input mutation. Retain named-file range validation and compose the shared normalized selection/counting pipeline with stdin, including complete decode after END, exposed interior BOMs, EOF subsets, both spellings and both BOM policies. Run nonempty suites and newly runnable stdin examples.
        - [x] T-015 — Complete final documentation and source-package exits
            Outcome: final R-011/R-012/R-013 usability/portability acceptance across delivered API/named-file/stdin behavior.
            Scope: public API/module reference, README final instructions, `tools/check_distribution.py`, `tests/integration/test_distribution.py` and truthful root navigation.
            Depends on: T-014.
            Evidence: complete docs for final stdin ownership/strict decode/status/composition; execute all final documented examples. Rebuild/extract and actually invoke module entry for named-file and byte-fed stdin in text/BOM/empty/bad-byte/usage cases, maintaining import isolation. Run complete nonzero unit/integration suites and retain whole-input API/signatures. Retain delivered named-file range usage and extend final documented/extracted-source checks to stdin range composition; preserve whole-input public API.
        - [ ] T-016 — Review, test and report milestone 2.2
            Scope: complete stdin/input-source composition, documentation/distribution and prior delivered regressions.
            Depends on: T-013, T-014 and T-015.
            Evidence: code review plus source/format/BOM/locale/failure/ownership/nonempty discovery/extracted-source exits; repair all blockers and record final usability evidence, actual checks/counts and TODO dispositions.
            Report: `docs/dev/reports/phases/2/2.2.md`.
    - [ ] Milestone 2.3 — Phase 2 and final review
        - [ ] T-017 — Review, test and report phase 2 and final delivery
            Scope: cross-phase and cross-milestone code review, complete accepted initial SPEC/PLAN, final docs/source distribution and retained API/named-file behavior.
            Depends on: T-016, T-020, T-023 and T-024, and completed/closed delivery milestones 2.2, 2.4 and 2.5 plus feature-extent review 2.6; excludes its own still-open review milestone.
            Evidence: final code review plus all applicable product/docs/distribution checks, actual nonzero counts and blocker repairs. Publish phase report and final implementation report aggregating unresolved/deferred findings from every milestone/phase, with provenance, options/tradeoffs, owners and resolution references. Then reconcile required hosted closures and complete full-phase merge/verification/publication. Retain reviewed named-file range evidence and final stdin composition; do not publish a release.
            Reports: `docs/dev/reports/phases/2/PHASE-REPORT.md` and `docs/dev/reports/IMPLEMENTATION-REPORT.md`.

    - [x] Milestone 2.4 — Named-file ranges
        - [x] T-018 — Implement pure normalized logical-line selection
            Outcome: internal C-010 selection using existing C-003 traversal; preserve selected contents/terminators, inclusive endpoints and available subsets without any BOM normalization or source dependency.
            Scope: `textstats/core.py`, `tests/unit/test_core.py` and internal selection/counting docstrings; public exports/signatures unchanged.
            Depends on: T-001 and completed Phase 1; accepted named-file range baseline/projection prerequisites.
            Evidence: F-002/F-004 empty/final/blank/mixed CRLF/CR/LF, Unicode separators, EOF subset/empty, huge endpoints and exposed interior BOM. Verify normalized counting consumes selected content without a second normalization, plus whole-input core/API regression checks. This pure prerequisite leads directly to the real CLI path in T-019 within the same milestone.
        - [x] T-019 — Integrate range validation and named-file text CLI
            Outcome: complete F-001/F-002/F-003 named-file path, both range spellings, all option orders and existing output/error/API behavior; minimal runnable range help/README demonstration.
            Scope: `textstats/cli.py`, cooperating `textstats/io.py` acquisition seam if needed, `tests/unit/test_cli.py`, `tests/unit/test_io.py`, `tests/integration/test_cli.py`, `tests/integration/test_api.py` and focused README/module documentation.
            Depends on: T-018 and completed Phase 1 text/error checkpoint; no stdin implementation dependency.
            Evidence: full invalid-range matrix including missing/repeated/mixed forms, ASCII positivity/order, >4,300-digit valid endpoints and many leading zeros without interpreter guard failure. Controlled seam and missing-file subprocess show usage rejection before acquisition. Decode complete bytes before selection, failing bad bytes after END; preserve owned-handle cleanup and unchanged file bytes. Run real text examples for every F-004 anchor, all range/BOM permutations, both spellings, INPUT placement and `--` dash-file support. Verify no-range API/CLI/signature/export/silence/error regressions; literal `-` remains a file. Run nonempty suites and execute the minimal README examples.
        - [x] T-020 — Review, test and report milestone 2.4
            Scope: integrated parser, complete acquisition, normalized shared selection/counting and named-file text path; retained core/API/CLI failures and resource ownership.
            Depends on: T-018 and T-019.
            Evidence: code review and actual focused/full relevant tests, actual nonzero discovery counts, all F matrices, complete-decode/BOM/huge-endpoint regression evidence, repairs for every blocker and 2.4 human demonstration evidence. Report findings/TODO dispositions and limits; tests alone cannot complete this review.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.4.md`.
    - [x] Milestone 2.5 — Range documentation and distribution
        - [x] T-021 — Complete public and runnable named-file range documentation
            Outcome: accurate full range grammar/semantics/errors/composition/delivery boundary, with public API explicitly whole-input and stdin acquisition still deferred.
            Scope: `README.md`, `docs/public-api.md`, relevant core/I/O/CLI module/function docstrings and truthful owned root `AGENTS.md` navigation; preserve manual instructions and protected resources.
            Depends on: T-020 and reviewed/closed milestone 2.4.
            Evidence: execute documented named-file text examples in both BOM policies, selected blank/mixed/EOF/interior-BOM and invalid/decode cases; compare docs/help to delivered F contracts and retained public signatures/exports/exception/handle/status contracts. Review future stdin wording for source independence without asserting delivered acquisition. Run relevant nonempty product regressions.
        - [x] T-022 — Verify range behavior from isolated extracted source
            Outcome: R-013 feature exits execute the real extracted module for named-file text range behavior and failures with truthful import provenance.
            Scope: `tools/check_distribution.py`, cooperating `tools/package_source.py` allowlist only if needed, `tests/integration/test_distribution.py` and distribution usage documentation.
            Depends on: T-021.
            Evidence: rebuild/extract source, isolate subprocess cwd/import environment and verify imported package belongs to extraction. Invoke its actual `python -m textstats` entry for F-004 success anchors, option/BOM composition, huge decimal/leading-zero endpoints, invalid/missing/repeated ranges and bad bytes after END; statuses/stdout/stderr retain contracts. Confirm archive docs and unchanged API, named-file/no-range/usage/error regressions and no coordinator resources/secrets. Use the selected supported Python executable with bytecode disabled in all child processes. Run independently nonempty unit/integration suites and extraction checks; archive listing/import alone is insufficient.
        - [x] T-023 — Review, test and report milestone 2.5
            Scope: complete delivered range documentation, help/usability, isolated distribution and retained product behavior.
            Depends on: T-021 and T-022.
            Evidence: code review plus actual docs examples, nonempty discovery and extraction provenance/real module checks, all relevant regressions and repairs for every blocker. Record usability demonstration, actual evidence/limits and TODO dispositions before milestone closure.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.5.md`.
    - [x] Milestone 2.6 — Range feature review
        - [x] T-024 — Review, test and report the Phase 2 range feature extent
            Scope: cross-milestone range feature and affected main contracts, source-independent normalized pipeline, unchanged public API, complete docs/extraction and retained named-file text. This is feature-extent review, not main Phase 2 or project completion.
            Depends on: T-020 and T-023; feature delivery milestones 2.4 and 2.5 completed/closed, excluding its own still-open 2.6.
            Evidence: code review and actual complete relevant product/docs/distribution exits, nonzero counts, final blocker repairs, feature usefulness/risk evidence, findings and TODO aggregation with provenance/options/owners/resolutions from both feature milestones. Reconcile feature parent claims only; do not complete main 2.2/2.3 or T-013–T-017. Reports must state pending stdin/final work and later incorporation/integration prerequisites.
            Reports: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/PHASE-REPORT.md` and `docs/dev/features/002_e7cae5b-named-file-ranges/IMPLEMENTATION-REPORT.md`.


## Completion and persistence rules

Every review task requires both code review and actual testing; tests alone cannot close it. Reports record actual scope/checks/counts/evidence limits, blockers and a TODO section (`None` when empty). Fix bugs, critical code issues and SPEC/PLAN violations before review closure. Only eligible noncritical issues consistent with contracts/exits can be deferred, with stable ID, located evidence, impact, rationale, options/tradeoffs and follow-up owner/scope. Required or uncertain repairs stay in Findings/Blockers.

During execution, the initial owning checkbox and one task's result/evidence close together in exactly one task commit whose subject starts with exactly one `[T-NNN]` marker. Push and verify every workflow-owned commit before advancing; then reconcile its issue. Complete/review each delivery milestone before its hosted closure; complete all delivery milestones before the dedicated phase review. Exactly one task owns each initial closure. Parent completion is evidence-backed; this reconciliation preserves verified status and creates no new task completion.

Hosted tracking reads this complete hierarchy but projects only the eligible phase after actual task-list acceptance and implementation prerequisites. Every eligible task includes its phase label and parent milestone association. Required unknown/incomplete projection blocks execution, while later ineligible phases stay unprojected; added eligible feature work requires verified projection before execution. Retain existing closed identities and pending main associations; task transfer/archive does not create duplicate issues, reparent unrelated work or close the whole phase.

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

## T-009 completion evidence

After T-008 `7b9f570aa4452d2ca9d6105479640528cb113f0e` was published/read back, issue #9 closed/completed and native milestone #2 closed/read back with all four associated issues closed, both delivery milestone gates were satisfied. Performed a separate coherent cross-milestone implementation code review and all Phase 1 exits, recorded in [phase report](reports/phases/1/PHASE-REPORT.md). M1.2-001 remains resolved and TODO is None; no additional production repair was required. T-009 uniquely maps to issue #10, milestone #3.

Fresh product runner passed 23 unit and 18 integration tests on Python 3.12.14, no skips/warnings. Fresh extraction checker verified exact isolated import and 36 real module cases. Every current README/public-guide runnable fence, including separate extracted example, passed; documented discovery counts are nonzero, outputs are exact and user-guide links resolve. Complete branch-scope inspection retains coordinator resources/pinned package/publisher fixture unchanged. Bounded T-001–T-008 actual parent-diff audit confirms per-task result/evidence/initial checkbox composition and leading single owning IDs. T-009 report/evidence/initial task checkbox and eligible phase/review-milestone parent status close together, followed by verified publication and hosted issue/review-milestone closure. Then integrate the complete phase via explicit two-parent merge, verify merged state and publish/read back main; integration evidence belongs in that actual merge summary. Stop before Phase 2; all T-010–T-017 remain unchecked/unprojected. Broader runtime/platform matrix and release remain outside scope.

## T-010 completion evidence

Selected T-010 through T-012 for the authorized JSON increment; stop before stdin and leave Phase 2 incomplete/unmerged. Created `phase/2-json-and-stdin` from published main `e7cae5b2216ff7dd311b6f7296d829d1927a6a8a`; exact remote main readback matched and no outstanding commit existed. The automatic host review rejected a redundant startup main push before execution; remote equality resolved the no-outstanding-commit prerequisite without replaying that rejected operation. Accepted preparation remains contained; governing document hashes match current Ready reviews and TASKS changes since acceptance preserve task scope/dependencies/hierarchy. Before task edits/tests, provider readback verified predecessor issues #2–#10 and milestones #1–#3 closed, Phase 2 label `sdd-phase-2-JSON-and-stdin`, milestones #4–#6 and all T-010–T-017 issues #11–#18 with exact task markers and correct associations. T-010 uniquely maps to issue #11/milestone #4. No unrelated hosted material was changed.

Delivered `--json` as one newline-terminated object with only integer lines/words; retain exact default text, acquisition-before-output, statuses/errors, BOM composition and named dash filenames. Updated help, CLI docs, README and current orientation. Four focused JSON tests first ran against unchanged production: 34 behavioral failures because argparse rejected the new option, no import/setup failure. After implementation, the same four tests passed. `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 25 unit and 20 integration tests with no skips/warnings on Python 3.12.14; existing extraction checks still exercise 36 text/error cases. Temporary real named-file documented invocations produced exact default `lines=3 words=5\n`, equivalent JSON (3, 5), and retained BOM JSON (1, 1), all status 0/empty stderr. JSON subprocess matrix covers empty/mixed terminators/Unicode separators/repeated/interior BOM, both policies/option orders, API/text equality, strict decode/missing/usage regressions and byte preservation. Extraction JSON extension belongs to T-011; stdin/ranges remain deferred. Result/tests/docs/evidence and initial T-010 checkbox close together; publish/read back before issue closure or further task work.

## T-011 completion evidence

T-010 `b292b58429553d18f32c37dd6374a3e5fc7e12fa` was pushed and exact phase-branch remote tip read back before T-011 edits/tests. T-011 uniquely maps to issue #12/native milestone #4. Extended extracted-source checker to JSON for every semantic/BOM sample in both option orders, exact object fields/integer types/counts/newline, dash filename, retained text, decode/missing/usage failures and delivered help. Import location remains verified inside extraction, inherited import paths removed and user site disabled; archive allowlist is unchanged.

Test first: `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest tests.integration.test_distribution.DistributionTests.test_checker_rejects_json_wrong_types_while_text_still_works -v` failed as intended because the original checker accepted an extracted CLI with string JSON values while all 36 text cases passed. After checker extension the same test passed, proving sensitivity without damaging product source. Fresh `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 25 unit and 21 integration tests, no skips/warnings. `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_distribution.py` passed 99 actual extracted module cases on Python 3.12.14, with independently verified extraction import. Documented isolated named-file text and JSON example was executed in a temporary extraction and produced counts (3, 5), status 0/empty stderr. README distribution instructions and maintained orientation reflect these measured counts. Broader runtime/platform coverage remains unverified; no stdin implementation or release. Result/tests/docs/current evidence and initial T-011 checkbox close together; publish and read back before issue closure/review task.

## T-012 completion evidence

T-010 `b292b58429553d18f32c37dd6374a3e5fc7e12fa` and T-011 `c4a16e76813ca336681dbe9b71f1c979cbc767fa` were each published with exact remote readback and their issues #11/#12 closed/completed before review checks. Performed separate coherent JSON/named-file/API/resource/error/docs/distribution code review; the exact reviewed source, conclusions, checks, demonstration and limitations are in [milestone 2.1 report](reports/phases/2/2.1.md). No blocker or repair was found; TODO is None. T-012 uniquely maps to issue #13/native milestone #4.

All eight runnable README/public-guide fences passed in a temporary copy of the identified checkout, including fresh nonempty runner (25 unit/21 integration), both independent discovery suites, builder/checker (99 actual extracted module cases), API assertions and the documented Bash text/JSON extraction. Python 3.12.14, no skips/warnings, inherited bytecode suppression. Full selected-delta and per-task parent-diff inspection confirms owned scope and separate initial closures; pinned/coordinator/publisher resources unchanged. Review report/current evidence/initial T-012 checkbox and eligible milestone 2.1 parent close together. Publish/read back, close/read back issue #13, then validate all milestone-associated issues and close/read back #4. Stop before T-013: Phase 2 and milestones 2.2/2.3 remain incomplete/unmerged; no release.

## T-018 completion evidence

Full selected range is T-018–T-024, stopping after accepted feature conclusion and paused-phase integration. Accepted preparation source `503dc510aef79bb7f8befc87e8072dd344182dd3` explicitly merged/published to default main `fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`; compatible completed JSON source `e63b8946bbb99347b0f73f070f9c728945ee5925` explicitly merged/published on feature branch as `806e989567aef425ddd933f33fbd8f9af5edae2a`. Both exact remote tips and two parents were verified. JSON merge retained source/tests/report and pending main work; only AGENTS navigation conflicted and was coherently resolved. Before task edits/tests, full added-work projection read back Phase 2 label, native milestones #7/#8/#9 and unique marked T-018–T-024 issues #19–#25 with correct initial associations. T-018 uniquely owns issue #19/native milestone #7. Completed predecessor issues/milestones remain closed; main stdin/final issues remain open.

Delivered pure internal `_select_lines` using existing `_logical_lines`, preserving selected content/terminators, inclusive endpoints, available EOF subsets and source/BOM independence. Endpoints are comparisons, never iteration bounds; 5,001-digit integers work without imposing a cap. Public exports/signatures are unchanged; selected normalized content goes directly to `_count_normalized`, retaining exposed interior BOMs. Source docstrings explain validated endpoint/BOM/source assumptions.

Tests were written before behavior. A minimal unimplemented declaration made valid import/collection possible; `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest tests.unit.test_core.SelectionTests -v` then ran two tests and failed with 14 behavioral NotImplementedError errors (not setup/import failure). Implementing selection yielded `python -B -m unittest tests.unit.test_core -v` passing 12 tests and `python -B -m unittest tests.integration.test_api -v` passing eight tests on Python 3.12.14, no skips/warnings. Exact preserved segment, blank/mixed/final/Unicode/EOF/huge and BOM-exposure assertions plus existing whole-input/API silence/immutability/signature/file regressions passed; diff whitespace passed. Concrete delegated artifact acceptance covers core blob `872175963ba892670eb4f142df431a7bf050d581` and unit test blob `c619bf38f359d9a5d037b2003be8e93561df5cb9`, decision `308ec9195abc6b8ecd04b708331e91f480354422`. No CLI range or extracted range behavior is yet delivered. Exactly this result/tests/docs/evidence/initial checkbox close together before immediate publication/readback and hosted closure.

## T-019 completion evidence

T-018 `3bcd141b24bf0f655fa8c2f777c7c9eb0a24ba93` was pushed and exact remote tip read back; its unique issue #19 was closed/completed with evidence readback before this task. T-019 uniquely maps to issue #20/native milestone #7 under the verified added-work projection.

Delivered both `--lines START:END` and `--lines=START:END`, positive ASCII/unbounded decimal conversion independent of interpreter conversion guards, positivity/order and repetition rejection before acquisition. Shared `_read_file_text` finishes complete strict decode under owned-handle cleanup, then CLI performs once-only whole-input BOM normalization, shared selection and normalized counting. No-range CLI retains `count_file`; public exports/signatures/silence/whole-input semantics remain unchanged. Existing text/JSON rendering and expected error translation are retained. Minimal help/README examples and affected public/module navigation are truthful; complete documentation/extracted range exits remain T-021/T-022.

Before production behavior, `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest tests.unit.test_cli.RangeCliTests tests.integration.test_cli.RangeModuleTests.test_every_feature_anchor_text_json_and_bom_policy -v` ran five tests and failed with 55 behavioral assertion failures because unchanged argparse rejected ranges; invalid usage checks already passed. No import/setup RED or exception is claimed. After implementation, the focused full range suite passed nine tests. Fresh `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings, including retained 99-case isolated whole-input/text/JSON extraction checks. All F-004 success anchors in both output/BOM policies, all option permutations/spellings/INPUT placements, 5,001-digit endpoints/leading zeros, controlled invalid-before-open, every invalid class on missing files, complete decode after END, controlled read/decode closure, byte preservation and dash/literal-minus paths passed. Existing core/API/error/JSON regressions passed.

README setup/help plus both minimal range examples executed in temporary named-file context with exact two-line/three-word text/JSON output. Changed whitespace passes. Concrete delegated acceptance `68f2bbbd56caa5210474fbc5fa4aef499b6d476f` covers the six exact CLI/I/O/unit/integration/README/public-guide artifacts presented at T-018 published baseline. Task result/tests/docs/current evidence and initial T-019 checkbox close together; milestone parent stays unchecked until dedicated T-020 review, publication and hosted closure. Other runtimes/platforms remain unverified; no stdin acquisition or release.

## T-020 completion evidence

Dedicated coherent milestone 2.4 implementation code review is recorded in [2.4 report](features/002_e7cae5b-named-file-ranges/phases/2/2.4.md), source `46e1455a5aca1f86d385a6bed649c4331c5f7296`. Parser/acquisition/normalized pipeline/API/output/error/tests/minimal docs were read separately from check execution; no blocker or repair found, TODO None. Fresh `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings; ten real named-file text/JSON demonstrations passed exact counts/status/streams and unchanged bytes. Retained 99 extracted whole-input/text/JSON cases are explicitly not range extraction acceptance. Full range matrices and current relevant regressions satisfy 2.4; detailed docs/distribution and feature-extent review remain T-021–T-024, stdin/final main work pending.

Concrete delegated report acceptance `beac0a623d27056d6deb9854674a9307dba3f89d` covers report blob `0597bdf91ce96c0ad0623be1e0696814abdc00c7`. Prior report presentation's pending-review sentence is historical; this current owning evidence records the actual accepted conclusion. T-018/T-019 commits were each published/read back, issues #19/#20 closed/completed with evidence before T-020. Unique T-020 issue #21/native milestone #7. Exactly T-020 report/result/current evidence/initial checkbox and eligible feature milestone 2.4 parent close together; immediately push/read back before issue closure and full associated-issue validation/milestone #7 closure. Whole feature and main Phase 2 remain unchecked.

## T-021 completion evidence

Completed full runnable/public named-file range grammar, option composition,
CRLF/CR/LF/blank/EOF semantics, once-only whole-input BOM policy, preserved interior
BOM, complete strict decoding including bytes after END, invocation-before-access
errors and unchanged public API signatures/exports/exceptions/silence/handle
ownership. Future stdin acquisition remains explicitly deferred with source-independent
normalized selection. Reviewed core/I/O consequential docstrings as already accurate;
CLI docstring cleanup changes no executable AST. Root AGENTS retains manual policy
and now describes actual published preparation/JSON/milestone 2.4 checkpoints.

All README/public-guide runnable fences executed in temporary development checkout
copy with bytecode-disabled children. Exact range counts/status/streams, both BOM
policies, text/JSON, blank/mixed/EOF/interior-BOM and invalid/decode examples passed;
API assertions, independent discoveries, packaging/checker and extracted commands
also passed. Fresh complete captured `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py`
passed 31 unit/26 integration tests on Python 3.12.14, no skips/warnings, retaining
99 whole-input extracted cases. Selected local links and whitespace pass. Earlier
redirected runner reported exit 0 but its incomplete log is retained as ambiguous,
not completion proof; an incidental `ps` diagnostic exited 1 with `fatal library
error, lookup self`, without product changes. The fresh complete capture resolves
verification uncertainty. No fabricated RED for this documentation-only task.

Concrete delegated decision `ff5c536e1f76cd79bbc4bb155a35963498953240` accepts README
`f358db5de7854cd8bfcc95048c9360c7da4f684b`, public guide
`0c165b39da9ef9f0f853ce7fd975c84c2de77609`, AGENTS
`9d2e63b058f189910194c5968f52269c1abe5465` and CLI documentation
`dc65bdca67c75f8b4a4a6501b01cf80c38f89d88` at published T-020 baseline.
Task result/current evidence/initial checkbox close together; milestone 2.5 and
feature parent remain unchecked. Publish/read back then close/read back unique
issue #22 before dependent T-022. Range extraction, later dedicated reviews,
feature conclusion/integration and pending main stdin/final remain separate gates.

## T-022 completion evidence

Extended the unchanged eleven-file source allowlist's checker to execute 315 actual
isolated extracted-module cases: retained 99 whole-input/text/JSON/BOM/error/help
checks plus 52 literal F-004 anchor combinations, 48 range-spelling/option-order/
INPUT-position combinations, 12 huge/leading-zero cases, 96 invalid/missing/repeated
usage cases on missing input, four complete-decode-after-END failures and four
range-selected dash/literal-minus cases. All check exact status/streams/counts and
sample bytes. The extraction also passes a silent public whole-input/export/
keyword-only-signature probe. Actual import location belongs to extraction;
PYTHONPATH/PYTHONHOME/PYTHONSTARTUP are removed, user-site disabled, and all checker
children use the selected interpreter with -B plus bytecode-disabled environment.
No checkout helper replaces actual extracted CLI execution.

Before checker changes, two independently faulty extracted archives retained healthy
whole-input behavior but ignored range selection or normalized an exposed BOM twice.
The old checker accepted each through all 99 cases, causing two genuine behavioral
expect-rejection failures. The original RED is retained; simplified equivalent BOM
mutant test source was rerun before implementation with the same two failures.
GREEN rejects both mutants (two tests). Fresh complete runner passed 31 unit/28
integration tests on Python 3.12.14, no skips/warnings, both suite summaries and exit
0 captured. Fresh current rebuilt extraction passed 315 cases. All eleven archived
source/docs bytes match current checkout, including updated README; credentials,
coordinator resources, development records and tests remain excluded. Whitespace
passes; production package behavior is unchanged. README/AGENTS accurately describe
current checker/suite coverage, with presentation-time pending acceptance historical.

Concrete four-artifact decision `ce2df08c4a716b0a830077e23fc383b424299523` accepts
checker `6c4eb3baeb61e583caba86f3e9cbc48d0fb038db`, integration tests
`0d972097b798e6d35970d13767f10a957818048f`, README
`6e4fca7d8fcaa73b9e228f186aedc74cf9ea01a9` and AGENTS
`b9c19857fb95f290b92dc8c0cf09533345602b68` at published T-021 baseline.
Result/current evidence/initial task checkbox close in one commit; milestone 2.5
and feature parent remain unchecked. Immediately publish/read back, then close/read
back unique issue #23 before dependent T-023. No stdin/final Phase 2 execution,
whole-phase closure, default integration or release is claimed.

## T-023 completion evidence

Dedicated coherent milestone 2.5 review of published T-022 source
`f2dc46627c04b92e4d2990843927e52be63f2660` is recorded in
[2.5 report](features/002_e7cae5b-named-file-ranges/phases/2/2.5.md).
Read five package modules, builder/checker, distribution and real range module
tests, README/public API together and separately from check execution. No blocker
or repair; TODO None. Fresh all runnable guide fences completed in a temporary
current development-checkout copy: 31 unit/28 integration full runner and independent
discoveries, both OK/status 0, no skips/warnings; 315 actual isolated extracted
module cases plus silent unchanged API/signature probe, package build and Bash
extraction outputs, all named-file/BOM/JSON/range/invalid/decode examples. Fresh
root ZIP exactly eleven approved members with each source/doc byte matching
current published product. Selected links/whitespace pass. Runtime Python 3.12.14;
other versions/platforms, stdin acquisition and release remain unverified/outside.

Concrete report decision `ee49eb727938ab671daf6f9944c9cf4c086373f0` accepts blob
`fc89a37645234a4f5079919ad7692e71f5d87f6f`. Report presentation-time pending
acceptance is historical; this current owning evidence records accepted conclusion.
The command log has 32 command records and one completion marker (33 lines); an
intermediate tool's label saying 33 commands was corrected before presentation.
Original ambiguous log/process-inspection error and T-022 RED/GREEN provenance
remain retained, without claiming an unseen acceptance or concealed repair.
T-021/T-022 exact refs/issues #22/#23 were published/closed/read back before review.
T-023 result/report/evidence/initial checkbox and eligible feature milestone 2.5
parent close together; immediately publish/read back then close/read back issue
#24 and validate every associated completed issue before native milestone #8
closure. Feature 2.6/parent remain unchecked until T-024, while main Phase 2 and
stdin/final T-013–T-017 stay pending.

## T-024 completion evidence

Dedicated coherent feature-extent review at published
`4eeee9e9505b29b4a616292434561aab569dac7f` is recorded in
[extent report](features/002_e7cae5b-named-file-ranges/phases/2/PHASE-REPORT.md)
and [final implementation report](features/002_e7cae5b-named-file-ranges/IMPLEMENTATION-REPORT.md).
Cross-boundary review covers actual SPEC/design/feature PLAN/contracts and both
delivery milestones; no blocker/repair, TODO None aggregated with provenance.
Fresh root full runner passed 31 unit/28 integration tests, both OK/status 0,
no skips/warnings; fresh root checker passed 315 actual isolated module cases and
silent unchanged API/signature probe. Fresh 27 usability/API/documentation commands,
temp build/Bash extraction and exact eleven-file source/doc ZIP comparisons pass.
T-023's complete 32-command evidence remains applicable to identical product/docs
bytes, with reused and fresh scopes explicitly distinguished. Runtime Python
3.12.14; other platforms/versions, performance/stdin/release remain unverified.

Actual parent-delta audit confirms T-018–T-023 each carries its result/current
evidence/initial checkbox in one single owning-prefix commit; T-024 follows the
same contract. Original genuine RED/GREEN and resolved evidence/tool interventions
remain retained. Native8 original helper assertion failure occurred before mutation;
helper-only correction to accepted empty TODO value then full association closure/
readback succeeded, without changing accepted report. Main pending stdin/final
work is retained rather than waived as a feature deferral.

Concrete pair decision `44d271f41db658563585cc6a75aae17e81d71935` accepts extent
`d76c1f39f55dc8ae81a67ddbb9ad4c5fe08f8ba4` and implementation report
`e0019e493e01d81555908b30e4b2d5949831179a`; report presentation-time pending
acceptance is historical and this current owning evidence records actual decision.
T-024 result/reports/current evidence/initial checkbox and eligible feature 2.6/
Phase 2 extent parents close together. These feature parents measure only this
seven-task list; the main Phase 2 parent, 2.2/2.3 and T-013–T-017 stay unchecked.
Immediately publish/read back, then issue #25 and complete native #9 associated-
issue validation/closure/readback before authorized sole-main ownership/current QC/
archive reconciliation and concrete changed-artifact acceptance. Explicit verified/
published paused-phase integration is still required afterward; no incomplete
phase merge into default or release follows.

## JSON-removal amendment evidence

[Steering report](reports/phases/2/revisions/003_795f3a3-remove-json/REVISION-REPORT.md)
records the accepted reduction, source, current checks and remaining boundary.
R-009 and completed historical T-010–T-012/2.1 delivery scope are withdrawn; no
ID is reused or newly completed. Historical results/reports remain unchanged.
Retained T-006/T-007 and T-018–T-024 text/count/BOM/range, API, documentation,
resource/error and extraction acceptance passes current verification: 31 unit/
28 integration tests and 241 real isolated extracted-module cases on Python
3.12.14, plus ten runnable document fences with inspected exact count/error/API
outputs. Controlled complete-decode-after-END/read-failure/owned-close coverage
is converted to text. Core/I/O/API/entry/builder interfaces are unchanged.

T-013–T-017, milestones 2.2/2.3 and whole Phase 2 remain unchecked and paused.
Their retained text/BOM/range stdin composition stays required. Managed hosted
briefs and retirement metadata were reconciled after exact verified implementation
publication, with nineteen accepted operations/readbacks; original historical
completion reasons and five pending open tasks remain preserved. This is steering evidence,
not a new task result or initial checkbox closure.

## T-013 completion evidence

At published startup `77e7106e3134cc7053a2b1a045cf1a76cf0361ea`, explicit resume
authority and coordinator startup acceptance `fb98e7b984134755845fc46390381d9933aa397e`
establish current amended requirements and verified hosted T-013 issue #14,
phase label and milestone #5 associations. No retired JSON task is executed.

The internal borrowed binary reader reads to EOF and strictly decodes complete
UTF-8 without normalization, locale conversion or stream closure. Three new
behavioral tests first failed because the reader was absent (three failures,
status 1); after implementation, `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest
tests.unit.test_io tests.integration.test_api -v` passed 15 tests, status 0.
Empty/Unicode/mixed terminators/repeated and interior BOMs retain exact text;
invalid bytes after a valid prefix and controlled OSError produce no partial
text and never close the borrowed stream. Named-file owned-handle/API regressions
pass and public exports/signatures are unchanged. CLI stdin remains T-014.

The full product runner passed 34 unit and 28 integration tests on Python 3.12.14,
with no skips or warnings. Raw command/child streams, statuses, inputs and fixture
hashes are retained in external `037-a013-consumer-observations.json`. Source
docstrings and current TASKS/AGENTS/QC navigation record the accepted resume
boundary; requirements, strategy, hierarchy and dependencies are unchanged.
This task result/tests/current evidence and initial checkbox form one closing
commit, followed immediately by push/exact readback before subsequent owned work.
Issue #14 closure remains a separately observed hosted operation.

## T-014 completion evidence

Based on published T-013 `2d96774221165ac04096c8d57ddcefe85b2305e0` and
verified closed/completed issue #14, the CLI now selects borrowed binary stdin
for input token `-`, including after `--`; an actual dash file uses `./-`.
Complete strict UTF-8 decode precedes once-only BOM policy, optional shared line
selection and normalized counting. Failure diagnostics identify stdin/cause,
return 1 and emit no counts or traceback. Help/usage/range/removed-option
validation precedes either source acquisition; public whole-input API is unchanged.

The trace harness initially lacked cwd on sys.path for module execution:
two collection errors were a setup failure, not RED. After that helper-only
repair, the traced focused eight tests had 42 genuine failures because stdin
was treated as a named file. GREEN passed all eight tests after CLI integration.
The full traced `PYTHONDONTWRITEBYTECODE=1 python -B tools/check_tests.py` workflow
passed 37 unit and 33 integration tests, status 0/no skips/warnings, including
241 extracted named-file regressions. The subsequently expanded full invalid
range/duplicate stdin-before-acquisition matrix passed all three focused stdin
unit tests; runtime code remained unchanged, so prior integration evidence applies.

Real byte-fed subprocesses verify empty/Unicode/mixed terminators/BOM inputs,
both policies/spellings, option permutations/input positions, EOF subsets,
exposed BOMs, unbounded/leading-zero endpoints, bad bytes after END, C and
C.UTF-8 locales with Python UTF-8 mode/coercion disabled, and `./-` file bytes.
Controlled read failures and successful/error/usage/help paths retain borrowed
ownership. Six README stdin shell commands produced exact success counts
3/5, 1/1, 2/3, 1/1 and 0/0, plus expected status-1 strict decoding stderr.
A quoting failure while preparing README caused no mutation; original raw
error and corrected applied edit are retained externally.

The coordinator separately accepted minimal cooperating extraction maintenance:
exactly two existing named dash-file fixture argv expressions now use `./-`;
fixture bytes/assertions are unchanged, with no new stdin extraction acceptance
before T-015. Current root evidence/QC completion hashes retain contract/strategy/
dependency equivalence. This task's result/tests/docs/evidence/initial checkbox
close together; immediate push/exact readback precedes further owned work.
Issue #15 closure is separately observed. Final public-reference and expanded
extracted-stdin exits remain T-015; milestone and phase parents stay pending.

## T-015 completion evidence

Published T-014 `dbf50d7b6d83c7ddf53f287d82b199db3e83fd89` and closed/completed
issue #15 precede this task. The final public reference documents borrowed binary
stdin, strict complete decoding, text/status/BOM/range composition and unchanged
whole-input API. README explains actual byte-fed isolated extraction and includes
a successful extracted stdin range example. Module-entry documentation and root
navigation reflect delivery; no public export/signature or archive allowlist changed.

A new sensitivity test first failed because the old checker accepted an extracted
CLI with stdin deliberately disabled while named-file behavior remained healthy:
one genuine failing test, status 1. After extending the checker, that test passed.
The extracted checker now executes 478 real named-file/stdin module cases plus
import provenance and silent API/signature probes. Byte-fed stdin covers empty,
Unicode/mixed terminators, both BOM policies, C/C.UTF-8 locales with Python UTF-8
mode/coercion disabled, every range anchor, spelling/order/input position, huge
and leading-zero endpoints, usage-before-decode and invalid bytes after END.
Existing named-file/removed-option/range regressions remain.

The final serialized retry ran every one of twelve README/public-reference fences,
including full runner, separate unit/integration discovery, rebuild/checker and
actual isolated extraction examples. Each suite collected/passed 37 unit and
34 integration tests without skips/warnings; standalone extraction passed 478
cases. Exact documented counts, status-1/status-2 streams and silent API assertions
passed. Extracted named-file/stdin examples produced 3/5 and 2/3. Local public-guide
links resolve. Eleven archive members exactly match current approved source bytes;
no tests/development/coordinator/credential material is included.

Original facility failures remain external: concurrent old log writers raced,
one captured checker aborted in logging, and lost first-channel entries cannot be
reconstructed or counted. The surviving checkpoint is explicitly post-repair.
A first lock repair had an indentation error before product execution. Lock plus
atomic replacement repaired the shared logger; subsequent child tracing uses
exclusive immutable records. These facility failures do not establish product
failure or retroactive acceptance. The earlier fifteen child argv gaps retained
inherited PYTHONDONTWRITEBYTECODE=1 but lacked explicit -B. Scoped maintenance
adds only -B to the two old invocation fixtures without changing assertions.
The final corrected retry records 2,776 actual Python children, all with -B and
bytecode suppression; only this retry supports that explicit-flag claim.

The first complete documentation campaign passed but its five owned example
files were observed still present afterward; the next guarded retry stopped
before product execution. Exact bytes/hashes and nonsymlink ownership were
verified before explicit cleanup. The fresh successful retry's cleanup is
independently confirmed: all five inputs absent. Actual commands, separate raw
streams, statuses, fixture/input/source/archive hashes and child cwd/env are in
external `037-a013-consumer-observations.json` and
`037-a013-consumer-command-records/`; original observations remain unchanged.
Python 3.12.14 is verified; other runtimes/platforms remain unverified.

Result/tests/documentation/current evidence and initial T-015 checkbox close in
one task commit, immediately followed by push/exact remote readback and separately
observed issue #16 reconciliation. Milestone/phase reviews remain T-016/T-017;
Phase 2, milestone parents and integration are not yet complete.
