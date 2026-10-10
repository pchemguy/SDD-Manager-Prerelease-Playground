# Task 3 independent review

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

Reviewed commit `909e7fce443618cde907327c7fab695e29270a3c` against base `08b700b`, the Task 3 brief/interface ruling/review boundary, finalized helper contract/code, chosen scenario and the original A-001–A-027 table in `docs/dev/reviews/008_98a5562/REVISION-PLAN.md`.

## Specification verdict: changes requested

The case bundle substantially satisfies Task 3: exactly 27 distinct stable IDs, coherent dependency/order and real predecessor bindings, separate product requests/assessor guides, executable independent literal constants and actual API/CLI capture, all intended controlled trigger/fresh-continuation protocols, a separate uncontrolled-loss procedure, and honest live-acceptance limits. One explicit first-attempt diagnostic evidence requirement is unmet: failed capture can erase actual nested command output/provenance. Resolve finding T3-R1 before acceptance.

## Quality verdict: changes requested

The validator/renderer use the finalized helper DSL; successful capture records actual status/channels, literals preserve bool/integer distinctions, and lifecycle decisions remain independently assessed. Reviewed support-test logs are green (58 total, including 17 catalog tests), and no live acceptance is claimed. However, tests do not exercise durable failure provenance; the current unavailable-product test merely expects rejection. T3-R1 is a concrete failure-path regression in the diagnostic tool, rather than a speculative live-consumer defect.

## Prioritized finding

### T3-R1 — P1: failed capture discards diagnostic first-attempt command evidence

**Location:** `acceptance/textstats/cases/assessor/capture.py:43–46, 65–75, 100–111`.

`invoke()` adds a journal entry only after `subprocess.run()` returns and output safety checks pass. Thus launch errors/timeouts retain neither the attempted command nor `TimeoutExpired`'s available partial stdout/stderr. `capture()` owns a private journal and returns it only after the entire suite succeeds. Import failure/origin rejection and later capture errors discard even completed entries. `main()` catches those errors and emits only `actual capture unavailable; retain failed command/session evidence separately`, without writing provenance or exposing the sanitized nested diagnostics. An outer session transcript cannot recover bytes already captured inside the failed subprocess.

**Concrete observed reproduction:** a disposable product module printed unique non-secret stdout/stderr markers, then raised during import. The real capture CLI exited 2; outer stderr was empty, outer stdout contained only generic error JSON, both requested output files were absent, and neither marker survived. A bounded injected `TimeoutExpired` carrying known partial stdout/stderr left `invoke()`'s journal empty, and the CLI handler likewise produced no provenance file. Exact observations are retained in `task-3-review-repro.log` beside this review. No live provider/consumer/token read was involved.

This is a truthful unavailable/blocked capture, **not** an invented passing result. Nevertheless, it violates the explicit capture review boundary and first-attempt retention requirement, prevents cause attribution, and makes a retry appear to be the first diagnosable attempt.

**Required bounded correction:** retain an attempted-command entry before execution; retain safely exportable status/cause/observed or partial channels, import-origin observations and all completed prior entries on failure. Persist failure provenance through an explicit failure path without inventing literal success, replacing original evidence, or publishing protected content. When channel content cannot safely be exported, retain non-secret command metadata and an explicit withheld-content reason instead. Add focused checks covering import/launch/timeout and later-suite failure, asserting command identity/prior observations survive and failed capture never produces passing literal evidence. Clarify the failure artifact procedure in the capture protocol.

## Evidence supporting the remainder of the specification

- Catalog preserves every original intent, with source-relative reusable assets and no fixed historical repository/task/provider/SHA identities. P0 preparation and final failed/blocked campaign reporting do not require successful fabricated product checkpoints. Negative forks derive from actual assessed/published checkpoints; scope and unavailable-trigger rules are explicit.
- Consumer preparation supplies named-file/API/CLI/test-layout requirements, JSON/range/removal/stdin contracts and future stdin compatibility. Requests/continuations carry ordinary product work and authorization; expected routing and fault setup stay with coordinator/assessor assets. A-008 and A-012/A-013 focused probes inspect derivation/retirement/selection without supplying route answers. The renderer supplies selected request/current state only, while docs explicitly require fresh worker access isolation and block isolation certification when broad access exposes assessor assets.
- Independent guides preserve all original lifecycle/scope/ownership/publication criteria: selection-only/no edits, per-task evidence, paused phase boundaries, two-parent/target integration, selected incorporation/sole ownership/source retention/archive, subtractive steering/retired work, reassessment, unrelated index intent, credential classification and nonempty verification/baseline evidence. Deterministic contracts cannot confer case Passed.
- Controlled interruption guides require actual consumer-visible work/trigger, actual suspension, retained refs/files/index/parents/pending identities, separate fresh continuation, restoration only of bounded facilities and separate grading of attempts. Conflict/prospective failure requires two real stops. Hosted adapters require actual delivery plus consumer response and exact live readback, otherwise Blocked. Uncontrolled loss is separate, native, applicable during actual file/stage/check/commit/push/API/checkpoint operations, and resumes only from retained product state; missing exports are an exact recovery gap.
- Every shipped literal check was parsed and compared with its independent expected asset. Capture imports product code solely to observe actual behavior; it does not import expected constants or derive expected counts from production. Actual raw stdout/stderr/status and fixture facts survive on the successful path. Bool/int JSON distinctions survive capture and `core.exact`; bounded reproduction confirmed `true` cannot equal expected integer `1`.
- Documentation/report clearly state static/catalog/DSL/synthetic sensitivity evidence is harness verification only. Full installed-client/provider/interruption/product acceptance, unreadability/handle lifetime, stdin lifetime/read-error, full docs/distribution checks and Python-version limits remain actual independent work. No live acceptance or full-coverage result is inferred from the green support suite.

## Exact performed checks and limits

1. Read Task 3 briefs/interface/report, supplied review diff and actual catalog/consumer requests/preparation/continuations, all 27 contracts/guides, COMMON/INTERRUPTIONS, capture/validator/renderer, catalog tests, narrowed EXECUTION/DIAGNOSTICS changes, source scenario, original 27-case table and finalized helper documentation/assessment/type-comparison code. Parsed all literal assets/contracts and verified every contract literal matches its separate expected asset.
2. Inspected commit/stat and worktree status. Root-owned uncommitted README/report follow-up additions and unrelated `.codex` state were excluded from this Task 3 verdict. No source file was edited, committed or pushed.
3. Reviewed `task-3-tests.log` (58 passed) and `task-3-catalog-tests.log` (17 passed); did not routinely rerun the complete suite.
4. Ran bounded disposable-local reproduction of an actual import failure and bounded injected timeout plus a bool/int capture comparison; saved observed output in `task-3-review-repro.log`.
5. Ran `git diff --check 08b700b 909e7fc`: exit 0.

No live consumer dispatch, provider read/write, credentials/token inspection, finished TextStats fixture, source switch, source mutation or subagent delegation occurred. This is a reusable-bundle review; it does not establish any of the 27 live acceptance outcomes.

## Scoped fixwave 1 recheck — 5bb917dd84c3c624735d8604d9edcfc60130c6e9

**Final specification verdict: approved for Task 3's reusable-bundle scope.** **Final quality verdict: approved.** T3-R1 is resolved; the initial verdict, concrete failed reproduction and original verification evidence above remain retained. No additional blocker was identified in the scoped correction. These verdicts do not certify live consumer/provider/interruption acceptance.

Reviewed the complete scoped fix diff (capture.py, COMMON.md, six new failure-provenance checks), actual fixed code, appended implementation report, retained two-test behavioral RED, six-test focused GREEN and full 64-test GREEN logs. The RED records contain the real assertion failures described in T3-R1, rather than setup/import errors. Did not routinely rerun the full suite.

The correction records safe command/cwd/environment before launch; records actual completed status/return code or explicit timeout/not-started with null return code; retains safe partial channels and earlier completed commands; marks rejected import-origin observations; and exposes the accumulated journal to the CLI failure path. Failed capture writes a new `status: Failed` provenance artifact and no literal evidence. Protected channels are checked before either is retained, with explicit withholding metadata and no raw/base64 leak. Occupied attempt paths remain exclusive. Documentation distinguishes Captured observation completion from acceptance and explicitly reports unavailable failed-provenance retention.

Independent bounded recheck reran the original actual disposable import-failure scenario: exit 2, failed provenance present, both unique nested stdout/stderr markers and actual return code 1 retained, origin_accepted false, and literal output absent. Retrying the same requested attempt left the original provenance bytes unchanged. A bounded timeout exception with known partial bytes retained the attempted command, Timed out status, null return code and both partial channels. Exact observations are in `task-3-fix-review-repro.log`. `git diff --check 909e7fc 5bb917d` exited 0. Worktree status still contained only the explicitly excluded root-owned README/report additions and unrelated `.codex` state.

All work was review-only apart from the explicitly requested scratch review/reproduction logs. No source edits, provider/consumer execution, token reads, commits/pushes or delegation occurred. Dedicated-repository live acceptance remains the documented follow-up, with no outcome prefilled by this approval.
