# Fresh orientation and recovery consumer exercise

Source read: `/workspace/scratch/6420baa7afea`, HEAD `719540de681cb3cfcf3e8a06dbeb7f4940cc755a` (observed with `git --no-optional-locks rev-parse HEAD`). No source files were edited. I read root AGENTS and the relevant sdd-orient, sdd-manage, sdd-docs, sdd-integrate-feature, sdd-implement recovery/browser, and sdd-verify skill/reference instructions. I did not read campaign025, findings, baseline or assessment material, use credentials/network services, or install a browser.

The exercise applies package instructions directly to disposable local fixtures. It establishes these consumer behaviors, not acceptance by all hosts or live production repositories. The fixtures have local Git baseline commits, no remote, and no publication. The explicit exercise scope stops at verified fixture files.

## Actual orientation fixtures and observations

Artifact root: `/workspace/scratch/revision025-fixtures`.

Construction/check runner: `/workspace/scratch/revision025-fixtures/exercise_orientation.py`.

Observed command: `python /workspace/scratch/revision025-fixtures/exercise_orientation.py` exited 0. Machine results: `/workspace/scratch/revision025-fixtures/orientation-results.json`. Local link audit: `/workspace/scratch/revision025-fixtures/all-markdown-link-check.json`.

| Case | Actual artifact | Outcome |
| --- | --- | --- |
| O1 | `o1-minimal-adoption/AGENTS.md` | Created absent root orientation using README purpose, actual source/tests, existing notices, declared checks, missing-task-owner statement, constraints and explicit-load instruction. Five local AGENTS links exist. |
| O2 | `o2-manual-maintenance/AGENTS.md` and `checks/AGENTS.md` | Authorized preparation moved tests to checks, changed declared discovery command and added active `docs/dev/FEATURE-TASKS.md`. Updated only bounded root maintained content; preserved manual prefix containing “Never change data fixtures without explicit permission.” The prior `tests/AGENTS.md` moved with its directory to `checks/AGENTS.md`, retaining exactly “Run tests from repository root” and all its bytes. Six root links exist. |
| O3 | `o2-manual-maintenance/AGENTS.md` | Repeated maintenance with identical facts made no write. Before/after bytes and nanosecond modification time matched. SHA-256 both times: `b75fdc0f6cba5c04be8dcddd2323b5a54c18dd843f0b11985be68f23f183fb89`. |
| O4 | `o4-owner-transfer/AGENTS.md`, `docs/dev/TASKS.md`, `docs/dev/features/counter-formatting/FEATURE-TASKS.md` | Transferred current ownership to main TASKS; removed root active FEATURE-TASKS. Selected original source preserved byte-for-byte in descriptive counter-formatting archive. `docs/dev/features/counter-formatting/README.md` records transfer and marks archived checkboxes historical, not executable. Root orientation links current and historical owners, contains zero checklist entries. |
| O5 | `o5-interrupted-resume/AGENTS.md` and `user-notes.txt` | Before resumption Git showed both files modified. Replaced only the owned interrupted maintained section after inspecting retained content; preserved root manual prefix and unrelated user bytes. After resumption both paths remain modified; no reset/staging/commit of user work. |

Commands were executed from each fixture repository root with `PYTHONDONTWRITEBYTECODE=1`:

- All four repositories: `python src/main.py 2 3` exited 0 and printed `5`.
- O1, O4, O5: `python -m unittest discover -s tests` exited 0, collected/passed 2 tests.
- O2: `python -m unittest discover -s checks` exited 0, collected/passed 2 tests.
- Git inspections used `git --no-optional-locks status --porcelain=v1 --untracked-files=all`; status outputs are retained in the JSON.
- Independent Python traversal verified all 43 local Markdown links across all fixtures, including README, main owner and archive-transfer record; every target exists. This is filesystem existence validation, not semantic review or external-link verification.

O5 unrelated file SHA-256 before and after: `23fc8ddee2e949a7361c056e906c1d88d12bbea145947388ae745f9467d09fe1`.

I explicitly loaded O5 root AGENTS using `cat AGENTS.md` and O2 root/nested files using `cat AGENTS.md` and `cat checks/AGENTS.md`. For a host requiring explicit loading, the handoff must actually supply/load root AGENTS and applicable nested files before scoped work; the root's sentence tells the consumer what to do but cannot itself ensure discovery. This exercise demonstrates readable files and explicit loading here, not automatic discovery on an untested host.

Read-only sdd-orient supplies the factual missing/stale guidance and Git state. Authorized sdd-manage adoption/maintenance with sdd-docs supplies the writes; source transfer belongs to sdd-integrate-feature. I did not interpret orientation alone as write authority. No task implementation or completion claim arises from O4's document ownership transfer.

## Hypothetical recovery decisions: no browser installation or runtime probes executed

These decisions apply the supplied scenario facts and package recovery guidance. They are proposed routing/probes; they are separate from the actual local fixture evidence above.

| Case | Decision and evidence boundary |
| --- | --- |
| R1: CLI dependency/runtime blocker; browser unrelated | Preserve work and capture exact CLI check, runtime/dependency versions and failure. Inspect declared supported setup; route technical diagnosis and supported alternatives through the affected implementation/steering workflow, coordinated by manager. Probe the required CLI import/launch and selected actual suite after any material environment change. Browser, fonts and Canvas add no relevant evidence or prerequisites. Do not claim resolved without attempts/outcomes. |
| R2: HTTP 200 HTML; approved compatible alternative; repeated contexts and visible Canvas/text required | HTTP success establishes transport success only; HTML is an invalid expected browser archive. Inspect response content/magic/archive members, source integrity, executable/platform compatibility and stated approval of the alternative. Investigate the compatible approved route within scope. Representative checks must reproduce successive contexts/pages, teardown and process behavior, exercise visible text glyph pixels/font configuration and Canvas pixel/shape output, and inspect relevant screenshots with contract-based tolerances. A single launch or DOM string assertion is insufficient. Record version, configuration, substitution, observed attempts and blocked checks. Here no install/probes were run, so compatibility remains a scenario claim and runtime/rendering readiness is unknown. |
| R3: DOM assertions pass, glyph pixels absent, second context crashes | DOM text presence is verified to the extent of the supplied assertion. Visible glyph rendering is not established; if the screenshot should contain text under the accepted contract, absent pixels are an observed rendering failure, with cause still unknown. Successive-context lifecycle is failed in the observed run; one earlier successful context cannot establish session stability. Preserve screenshots/logs/process outcomes; distinguish missing fonts/rendering/configuration, incompatible facility and product defect through investigation. Full visual/session acceptance is not verified. |
| R4: native focus unavailable headless; injected handler passes | Injected handler evidence verifies controlled handler behavior only. Native focus/visibility/input delivery remains unverified or facility-blocked, not proven by injection. Keep independent passing behavior evidence; report the native gap and require a suitable facility if native delivery is an accepted condition. Do not classify unavailable optional native capability as a product failure without evidence. |
| R5: fresh-cache reproducible provisioning accepted | Run declared provisioning in a new task-owned cache/configuration, record exact versions/route/configuration, validate resulting artifact and execute representative required checks. Preserve unrelated caches/toolchains; no broad cleanup. Existing warm-cache success cannot satisfy fresh-cache reproducibility. If approved facilities cannot exercise that check, keep it blocked rather than dropping the accepted condition. No fresh-cache provisioning was attempted here. |
| R6: genuine platform policy denial called tooling blocker | Classify as platform execution denial, separately from existing workflow authority; recovery alternatives are not an evasion route. Preserve exact denied operation/reason and local state, inspect actual destination state if effect may be uncertain. Do not repeat unchanged denial or switch tools/transports/accounts/credentials to bypass it. A demonstrable missing-context mismatch may use an available supported reconsideration channel with actual grant/ref/payload/verification; a genuine policy restriction remains blocked. Retry only when supported resolution/new conditions permit; identify explicit host confirmation requirements if present, rather than inventing plugin approval. |

The source references were sufficient to reach the above routing and evidence limits without inventing an installation recipe, retry quota, universal host loading hook, extra execution journal, or task checklist in AGENTS. No recovery outcome is reported as executed.
