# Task 3 — Case contracts and isolated handoffs

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

Implemented and scoped-committed at **909e7fce443618cde907327c7fab695e29270a3c** (base 08b700b), on revision/009_384beef-textstats-test-project.

## Scope

- Catalog version 1 preserves all A-001–A-027 original intents, actual predecessor dependencies, operating modes, unique request/contract/guide paths, runtime checkpoint bindings and focused dependency-inflation/retired-task probes.
- cases/consumer/preparation.md supplies the chosen product requirements (including tests/unit, tests/integration and future stdin compatibility), without implementation/governing/task history or routing answers. Selected requests and separate fresh/uncontrolled continuation requests exclude assessor/coordinator fault setup.
- Every case has a nonempty finalized-DSL contract and separate independent lifecycle criteria. Actual literal capture observes API/default/JSON/ranges/range JSON/removal/stdin/extracted package outputs, recording actual import origin, args/status/raw channels and fixture hashes. Expected constants are independent assessor assets and never loaded by capture.py.
- Assessor procedures define actual trigger/fresh continuation for staged task work, unpushed commit, genuine failed required check, rejected push, conflict plus prospective failure, partial transfer, uncertain hosted effects/access classification. Separate native uncontrolled kill/recovery procedure covers file/stage/check/commit/push/API/checkpoint boundaries and fresh retained-state-only handoff.
- Assessor-side catalog validator detects actual ID/order/dependency-cycle/prerequisite/path/empty-DSL/protocol/separation defects. Renderer fails absent/ambiguous/missing refs, unassessed predecessor, unavailable exact destination readback, unretained/unpublished actual objects or mismatched published assessment; renders selected product input/current-state only.
- Narrow EXECUTION/DIAGNOSTICS refinements document concrete assets, capture, start-vs-reached checkpoint binding, focused causality and coverage limits.

## Interfaces

Finalized scripts/HELPER-INTERFACES.md/core.py DSL used without changes. Variable expected values use schema-allowed checkpoint_refs; arbitrary task IDs/paths are resolved from actual current-state observations and never invented as extra strict-schema keys. A-002/A-011 no-action expectations use independently observed starting refs; final commit/parents use independently observed reached refs. A-001 operates after P0's bounded initial operating/harness baseline without completed product prerequisites. A-027 reports blocked/failed campaigns without a successful product predecessor.

Resolved rendering input/checkpoint/publication shape is documented in cases/assessor/COMMON.md. It references an independently graded assessment and reads exact product/evidence destination containment plus published assessment bytes. It is still not an acceptance grader. Consumers receive rendered text and pinned product skills/current-state, never checkpoint proof/oracles/guides. Missing isolation/runtime injection/provider facilities block affected cases.

## Verification

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v`: **58 tests passed** (41 existing + 17 new), nonempty suite.
- New tests: valid all27 catalog; duplicate/missing/invalid IDs; genuine cycle/unknown prerequisite; missing/duplicate/escaping assets; empty/unknown/ref-invalid DSL; routing leakage; missing trigger; historical identity exclusion; isolated selected rendering; missing/ambiguous/unassessed predecessor; actual unpushed ref and mismatched published evidence rejection; placeholder resolution; empty-product/failure-report handoffs; raw command status/channels; derived error/fixture facts; every literal suite altered-actual sensitivity; all27 contracts consumed by actual finalized helper DSL; unavailable product import rejection.
- `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`: 27 resolved cases, static validation, live_acceptance false.
- `git diff --check` and scoped `git diff --cached --check`: passed.
- Scratch logs: task-3-tests.log and task-3-catalog-tests.log retain actual verification output.

## Limits and follow-up

No live consumer, provider writes/readback, token reads, source push, branch switch, finished TextStats implementation or tested-plugin edits occurred. Disposable local Git fixtures exercise harness behavior, not real workflow acceptance. Literal expected-evidence sensitivity/DSL-consumability fixtures are explicitly synthetic and never represented as product output. Runtime interruption, protected credential, unreadability/handle lifetime, stdin lifetime/read-error and complete distribution/docs checks also require independent actual execution per guides; deterministic samples alone do not certify them. If trigger/state/control facilities are missing, retain Blocked/Not run instead of scripted pass.

- [ ] **Live acceptance on a dedicated test repository.** Await an explicitly identified authorized destination, then execute bounded/full scope with fresh consumer/assessor contexts and real Git/GitHub facilities. No destination is silently inherited.

Root-owned revision report/README changes and unrelated .codex state remain outside this commit. Only our generated core bytecode was removed; original source history and parent evidence/ledger retained.

## Scoped review fixwave 1 — T3-R1

Review requested changes at original Task 3 commit 909e7fc: failed import/origin/timeout/launch or later capture error discarded already captured command provenance. Scoped correction committed at **5bb917dd84c3c624735d8604d9edcfc60130c6e9**, affecting only capture.py, COMMON.md and test_catalog.py; original implementation/review/failure evidence remain retained.

`invoke` now records safe attempted command/cwd/environment before execution, records actual return code on completion or null with explicit Not started/Timed out status, and preserves safely exportable observed/partial raw stdout/stderr. Capture exposes accumulated provenance through failure, retains rejected origin observations and all prior completed commands, and main writes a new status Failed provenance artifact on incomplete capture while leaving literal evidence absent. Content guards validate both channels before retaining either; protected channels are explicitly withheld, safe metadata survives. Existing attempt paths are not replaced. Provenance-write failure is reported as failed_provenance_retained false. Captured describes observation completion only, never acceptance.

Behavioral RED log **task-3-fixwave1-red.log**: 2 tests failed against original code (real CLI product import prints distinct stdout/stderr then raises, no provenance; TimeoutExpired with partial bytes leaves journal empty). GREEN log **task-3-fixwave1-green.log**: all 6 focused tests pass, adding actual CLI launch failure/occupied-attempt preservation, CLI later-suite timeout retaining actual prior import observation and partial channels, protected-partial-output withholding and outside-origin rejection retention. Timeout is a bounded injected subprocess exception, not live consumer or provider behavior; actual import/launch tests use disposable local modules/interpreters only.

Final **task-3-fixwave1-tests.log**: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v` **64 tests passed**. Exact27 catalog validator and staged/unstaged diff checks pass. No live acceptance, token/provider work, source push, branch switch or unrelated root-owned change occurred. T3-R1 is fixed in support tooling; independent review recheck remains the root coordinator's next gate. Explicit dedicated-repository live acceptance todo remains open.
