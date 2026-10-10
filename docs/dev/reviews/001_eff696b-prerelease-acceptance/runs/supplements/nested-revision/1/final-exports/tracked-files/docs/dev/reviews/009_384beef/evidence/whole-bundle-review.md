# Whole-bundle independent review

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

Reviewed immutable tip `f6fd96f` against implementation start `78d51c4`, the whole-bundle brief/diff, campaign 009 requirements/report and retained Task 1–3 implementation/review evidence. This is a cross-task infrastructure readiness review. Live acceptance remains a separately documented follow-up requiring an explicitly identified dedicated repository.

## Specification verdict: changes required

The complete reusable architecture substantially satisfies Tasks 1–3 and preserves the original 27 diagnostic intents. One reproducible interface defect, WB-R1, prevents the documented caller-relative observation command from exporting the recovery evidence required by the execution/recovery procedures. Correct it before accepting the portable bundle. No newly confirmed SDD Manager plugin defect is inferred from this harness defect.

## Quality verdict: changes required

The separation of product consumers, coordinator evidence and independent assessment is coherent; deterministic success cannot become case acceptance. The retained 64-test result is green, but its absolute-output fixtures miss a common CLI boundary. WB-R1 needs a focused path regression and bounded correction. WB-R2 is minor reporting cleanup. No other actionable cross-task defect was confirmed in this review.

## Prioritized findings

### WB-R1 — P2: caller-relative observer output is resolved against two different directories

**Locations:** `acceptance/textstats/scripts/core.py:369–371,421–429`; the caller-relative promise in `scripts/HELPER-INTERFACES.md` opening paragraph; observation/recovery integration in EXECUTION and RECOVERY.

`export_recovery()` keeps `destination` relative to the caller and creates its directory/blobs there with Python. It then passes the same relative bundle path to `git(root, 'bundle', ...)`, whose `git -C <consumer checkout>` makes Git resolve the path against the consumer instead. A coordinator running the helper from another directory with the documented `--output NEW.json` interface therefore receives `Blocked/git_operation_unavailable`, even with valid local repositories and all objects available. Its requested observation and recovery manifest are absent; a partial export remains at the caller location. Retrying the same name then encounters occupied recovery evidence. The diagnostic points at repository/access prerequisites although the repository is healthy.

**Bounded reproduction:** a disposable consumer repository with one published commit and a disposable bare remote; invoke the real CLI from the fixture parent with relative inputs/state and `--output relative-observation.json`. Exit is 2, output is absent, adjacent `.recovery/` exists without manifest, and consumer status is unchanged. Repeating with a distinct absolute output succeeds with exit 0 and complete manifest. Exact observed results and reproduction recipe are retained in `whole-bundle-review-repro.log`.

**Required correction:** use one caller-resolved export location for both filesystem operations and Git bundle create/verify while preserving occupied-output/symlink refusal. Add a CLI regression whose working directory differs from the consumer checkout, verifying observation, adjacent manifest, artifact hashes and usable bundle, with no unintended consumer output or consumer Git/index/workfile changes. Preserve failed attempts and avoid broad cleanup/reset.

**Related path consistency:** a distinct absolute output under a missing parent directory also exits 2 (`support_operation_failed`) because export uses `destination.mkdir()` before the normal output writer can create parents. The reproduction is retained. Either make observation create its authorized output parents consistently with `write_new`, or explicitly document/check the parent prerequisite. Include this in the same bounded output-path correction; it is not a separate finding.

### WB-R2 — P3: campaign plan still describes already completed infrastructure as unimplemented

**Location:** `docs/dev/reviews/009_384beef/REVISION-PLAN.md:8,193` at reviewed tip.

The state line says portable helpers/case contracts follow Task 1, and the final sentence says the bundle has not yet been implemented. Tasks 1–3 are checked complete and the report records their commits/review results. Update those two status statements during final reporting to distinguish implemented/reviewed infrastructure from pending live acceptance. Do not mark the live campaign complete. The root coordinator has acknowledged this reporting cleanup.

## Cross-task assessment

- **Entry and setup:** root README points to the bundle. AGENTS identifies the coordinator, ordered reading, exact missing-repository question before writes, explicit destination/authentication boundaries and fresh/resume distinction. No old repository/token is a default. Current report and bundle README each retain the required unchecked live-acceptance TODO and copyable agent prompt. The root separately reports a fresh directory-only bootstrap with unchanged source state; that is root evidence, not an independently executed consumer campaign by this reviewer.
- **Dependency and placement integrity:** all inspected bundle Markdown relative file targets resolve; source references explicitly identify pinned-package originals. There is no essential old scratch/chat/AgentPlayground input or superpowers runtime dependency in the shipped bundle. Run instructions consistently place coordinator artifacts under `docs/dev/reviews/<campaign>/` and use a distinct stable evidence branch.
- **Source and setup helpers:** schemas/configuration are strict and non-secret; output evidence is exclusive. Preparation is bounded to a new workspace, preserves existing source checkout instructions/index/workfiles, refuses resume/occupied lexical targets, and creates no completed product. Committed Git-object pinning is default; explicit dirty snapshots retain mode-sensitive fingerprints and reject unsafe package parents/symlinks. The 97 `plugin.json`/`skills/**` files are byte-identical between reviewed base and tip; diff paths contain no shipped package mutation.
- **Consumer/assessor boundary:** consumer requests contain ordinary product requirements, selected scope and current state. They do not carry catalog/AGENTS/assessor routes, expected outputs, historical success or fault setup. Renderer checks retained predecessor object/publication and matching independent assessment publication. Docs require actual access isolation or disclose the inability to certify isolation. Deterministic checks retain `agent_behavior_assessed:false`; independent lifecycle assessment remains necessary.
- **All original intents:** A-001–A-013 cover preparation/selection/tracking, incremental named-file/JSON/range delivery, selected incorporation/sole ownership, assessment-only subtraction, commanded retirement and explicit stdin continuation. A-014–A-026 preserve cross-phase scope, staged/unpublished recovery, required failure, rejected push, conflict plus prospective failure, unrelated staging, dirty transfer, reassessment, uncertain hosted effects, credential classification/effective ignore and verification collection/baseline intent. A-027 can report failed/blocked campaigns without a successful product predecessor.
- **Actual prerequisites and interruption:** cases bind runtime identities from assessed/published real checkpoints. Guides require actual observed partial consumer work and separate fresh continuation; no completed or interrupted work is manufactured as a successful fixture. Conflict/prospective failure has two genuine stops. Controlled adapter effects remain distinguishable from live readback. Uncontrolled termination is separately specified without planned-stop coaching. Missing trigger/runtime/provider facilities remain Blocked/Not run.
- **Recovery/publication:** exact pending repository/ref governs reconciliation; shallow/missing/error ancestry remains unknown and retry is never automatically safe. Exports retain staged/unstaged files, binary/mode/symlink/deletion intent, conflict stages, merge metadata and otherwise unreferenced parents. Retained tests actually restore these in fresh local clones. Protected/unsupported/missing state limits are explicit; exported evidence remains local-only until independently verified publication. WB-R1 is the confirmed mismatch between this intended recovery procedure and the CLI path interface.
- **Literal oracles and failed attempts:** capture observes product commands independently from expected constants and retains raw channels/status/provenance. Parsed all 27 contracts and verified all 22 shipped literal checks equal their separate expected assets across eight suites. Failed import/launch/timeout/later capture paths now retain safe first-attempt provenance, with explicit withholding when needed and no invented successful literals. Additional lifetime/unreadability/locale/distribution behavior is explicitly independent live assessment, not claimed from sample capture alone.
- **Diagnosis:** required final report explicitly states demonstrated behavior, issues, actions and proposed plugin changes (or supported no-confirmed-defect/no-change conclusion), with first/eventual outcomes, interventions, confidence and unresolved investigations. Historical TST-001–004 are lessons, not prefilled results. Green infrastructure checks are never represented as 27 new consumer outcomes.

## Exact checks and limits

1. Read the complete review brief, source plan/report, entry/setup/execution/recovery/scenario/diagnostics, schemas/helper interface, actual shared helper and CLI entry code, catalog/renderer/capture/common/interruption assets, consumer handoffs, contract criteria and retained per-task review/fix evidence; inspected support test construction and original 008 case intents. Whole diff inventory was reviewed against actual final assets.
2. `git diff --check 78d51c4 f6fd96f` passed. Compared all 97 package-file bytes between base and tip: zero differences. Bundle Markdown relative-target inspection: zero missing file targets. Parsed all 27 contracts and eight independent literal suites; all 22 literal checks matched their separate expected asset.
3. Reviewed retained `task-3-fixwave1-tests.log`: 64 tests ran and passed with zero failures/errors. Did not repeat the routine full suite; this retained result does not cover WB-R1.
4. Ran only the focused disposable-local real-CLI WB-R1 reproduction, one absolute-path positive control and the related absent-parent boundary. Fixtures were cleaned afterward. Fixture commits/pushes involved only temporary local repositories/remotes; no hosted operation occurred.
5. No implementation/source edits, branch switches, source commits/pushes, provider calls, credential/token inspection, live consumer dispatch or subagent delegation occurred. Only requested scratch review/reproduction evidence was authored. Root-owned later reporting/bootstrap files are outside the immutable implementation verdict.

These verdicts apply to the reusable infrastructure at `f6fd96f`. They do not certify installed-client routing, live GitHub/API behavior, real consumer isolation/interruption recovery, new TextStats acceptance outcomes or absence of SDD Manager defects. After the bounded WB-R1 correction, re-review its fix diff and focused evidence; complete the reporting cleanup separately. Live acceptance remains the explicit dedicated-repository follow-up.


## Final bounded fixwave recheck — `584cfe07ea6fe540c6cb81c8413e53fe45d53d17`

**Final specification verdict: accepted for reusable infrastructure readiness.**

**Final quality verdict: accepted.**

WB-R1 and WB-R2 are addressed. The initial review, failed reproduction and findings above remain retained. No new breakage was identified in the four-path correction diff from `f6fd96f` to `584cfe0`. This is the single final fixwave recheck; it does not reopen unrelated implementation scope or certify live acceptance.

### Finding dispositions

- **WB-R1 — addressed:** recovery destination is now made absolute relative to the caller without resolving away the lexical target. Python artifact writes and Git bundle creation/verification therefore use the same location. Explicit `exists`/`is_symlink` guards preserve occupied and dangling-symlink refusal; the CLI's existing output guard remains. `mkdir(parents=True)` creates authorized missing parents while retaining exclusive leaf creation. No consumer mutation or cleanup/reset was added. The helper interface now explicitly states caller location, parent creation, absolute recorded export and occupied-path refusal.
- **WB-R2 — addressed:** only the two stale plan-status statements changed. They correctly distinguish completed/reviewed reusable infrastructure and the separately verified directory bootstrap from unexecuted live acceptance. Task 4 checkboxes remain unchecked, and the dedicated-repository follow-up remains explicit.

### Independent recheck and retained verification

Read the complete four-path fix diff, actual corrected helper/tests/interface/plan, final-fix report and retained RED/GREEN logs. Confirmed actual HEAD is the reviewed full SHA and `git diff --check f6fd96f 584cfe0` succeeds.

The three new tests use actual CLI subprocesses with caller and consumer working directories distinct. They cover direct/nested relative outputs, an absolute output with missing nested parents, and file/directory/live-symlink/dangling-symlink refusal for both observation and recovery paths. Successful cases validate absolute export location, manifest and artifact hashes, bundle verification/fetch in a fresh clone and unchanged consumer HEAD/refs/status/raw index/workfile bytes/mode/path inventory. Refusal cases verify retained evidence/link targets and absence of unintended writes. These assertions directly exercise the original defect instead of merely inspecting the implementation.

Retained RED has 3 test methods and 4 expected failing subcases, zero errors. Focused recovery GREEN has 20 passing tests. The single full support GREEN has 67 passing tests, zero failures/errors. These are retained implementer results; this reviewer did not repeat the routine full suite.

Independently reran the original disposable-local relative-output reproduction and its absent-parent variant against the corrected real CLI. Both now exit 0 with requested observation, absolute adjacent recovery location, complete manifest, matching artifact hashes and a valid Git bundle. Consumer refs, raw index and workfile bytes remain unchanged. Exact results are retained in `final-fix-review-repro.log`; original failure evidence is unchanged. Fixture resources were cleaned normally afterward.

No source edits, branch changes, source commits/pushes, provider calls, credential/token inspection, live consumer execution or subagent delegation occurred. Only this requested review addendum and focused reproduction log were authored. The fix touches no shipped plugin files. Root's pending report/evidence bookkeeping is outside this implementation fix verdict.

The accepted result is a reusable diagnostic bundle with reviewed infrastructure and honest coverage limits. Actual dedicated-repository Git/GitHub lifecycle, consumer/assessor isolation, controlled and unexpected interruption acceptance, installed-client behavior and the final live diagnostic report remain the documented follow-up; no new 27-case campaign success or no-plugin-defect conclusion is implied.
