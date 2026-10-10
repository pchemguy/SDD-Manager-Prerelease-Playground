# Comprehensive review report

## Baseline and scope

Campaign `017_54d55ed`; reviewed source `54d55edebd8a7af6499d625bdbb357f864a4db1d`. Working branch `revision/017_54d55ed-comprehensive-review`; target `feature/architecture-revision`. [Review plan](REVIEW-PLAN.md).

State: review records verified, explicitly integrated and published; source repairs remain proposed. Evidence combines source inspection and actual local checks; no fresh-agent/live-client acceptance is claimed. No source repairs are authorized by this review.

| Unit | State | Evidence/findings |
| --- | --- | --- |
| U-001 Package and entry points | Complete | 15 entry points validate; assets resolve; installed subtitle is stale (E-001). |
| U-002 Authoring and QC | Complete | Full-intent/delta and ownership conventions coherent; campaign 011 QC remains pending (P-001). |
| U-003 Lifecycle and orchestration | Complete | Source transition traces coherent; live lifecycle remains E-002. |
| U-004 Acceptance helpers and composed checks | Complete | 68 support tests pass; catalog validates; R-001/R-002 reproduced, R-003 documentation gap. |

## U-001 — Package and entry points

All 15 shipped skill entry points pass the available skill validator. The 72 Markdown files and 147 local links in the package/README/capability-map audit have no confirmed missing shipped resource: the one raw missing link is a generated report-template placeholder. Manifest resource paths resolve; the Codex manifest names SDD Manager, PChemGuy, Developer Tools and the requested capabilities. Entry points distinguish read-only review, authoring and execution ownership, and route to focused references. No source repair finding is established by these checks.

Evidence: [structure](evidence/package-structure.json), [presentation and installed comparison](evidence/package-presentation.json), [baseline inventory](evidence/source-inventory.json). Byte differences in installed skill entries are CRLF conversion; normalized text matches all 15 source entries. Installed manifest still says `Specification-led development`, while reviewed source says `Spec-driven development`; both declare version 0.14.3.

**E-001 — Installed presentation acceptance remains open.** Installed metadata is observably stale; this does not establish a source manifest defect or the cause of the reported installed-icon behavior. Follow-up: refresh the distributed package with a distinguishable release identity and verify installed subtitle, icons and routing in the actual client against pinned source. Recheck: installed manifest matches selected source semantically and a recorded client session demonstrates presentation. No installation/cache modification was performed by this review.

## U-002 — Authoring and document QC

Inspected design exploration/architecture/decomposition, SPEC system/change/review, PLAN delivery/layout/review, TASKS derivation/progress, shared hierarchy/modularity/design heuristics, and documentation/TDD references. Full-system intent remains separate from feature deltas; physical ownership belongs to layout; PLAN defines meaningful integrated increments and TASKS derives bounded work. Both delivery milestone review tasks and the single-task phase review milestone are consistently required. Stable IDs, four-space checklist hierarchy, feature parent semantics and preservation of accepted existing hierarchies are explicit. No contradictory authoring handoff was established in these traces.

**P-001 — Accepted document QC preparation is not implemented.** Campaign [011 revision plan](../011_a3b2ad9/REVISION-PLAN.md) remains an eight-action pending source revision. Current PLAN review checks SPEC alignment and incremental delivery; TASKS derivation checks coverage/totals, but the package lacks the requested mandatory post-generation TASKS conformance review, adjacent SPEC/PLAN/TASKS review reports with appended rechecks, readiness gates and explicit 3–5 guidance/1–2 and 10+ fragmentation/overload triggers. This is a known outstanding policy revision, not newly implemented functionality or a duplicate source repair campaign. Consequence: agents can proceed under current instructions without completing the desired QC protocol. Recommended next action: execute campaign 011 with review-unit exclusion from implementation counts and corresponding TextStats cases; validate conformance failures and justified small phases, not just source wording.

Document-only preparation correctly stops before implementation and hosted projection. TDD distinguishes missing historical RED from actual observed chronology; documentation amendments to governing contracts return to the human. These checks are source analysis, not a fresh consumer execution.

## U-003 — Lifecycle, ownership and recovery

Inspected coordinator branch/Git/phase activation/credentials/authorization protocols, implementation selection/startup/task/completion, verification boundary/check/failure/evidence procedures, reporting formats, feature incorporation/archive/transfer, steering and GitHub projection/issue/milestone/failure procedures. Source traces produced the following consistent obligations:

| Trace | Required transition and observed source consistency |
| --- | --- |
| First phase / partial projection | No predecessor; all eligible phase objects/readback before first task; unknown or incomplete projection blocks activation. |
| Next-N within an incomplete phase | Review tasks count; per-task result/status commit, push/readback, then issue closure; pause without filling range or merging an unfinished phase. |
| Delivery milestone completion | Dedicated review includes code inspection and tests; bugs/contract violations repaired, report pushed, review issue closed, every owned issue checked, then milestone closure/readback. |
| Full phase / next phase | Delivery milestones close before sole phase-review task; review milestone closes after it; explicit verified/published phase merge before eligible next activation. |
| Backend outage / uncertain write | Preserve verified local work and pending closures; read exact identities/state/comments before replay; unknown outcome blocks dependent gates, not independent already-active work. |
| Feature subset / task transfer | Selected owners only; both lists required for transfer; stable task/issue IDs and evidence retained; scoped feature parent cannot close project-wide milestone; archive only after owner/link disposition. |
| Commanded steering | Existing affected contracts/code/task scope revised, invalidated acceptance reassessed, retirement distinguished from completion; merge into paused branch and stop without task continuation. |
| Merge/push interruption or platform rejection | Recover existing merge/parents and publication; no second merge, no destructive reset, no permission bypass; provide actual scoped authorization through supported review channel. |

No new contradictory transition or missing ownership assignment was confirmed in these source traces. Canonical shared lifecycle rules and focused owners agree on report-before-close ordering, retained TODO options/provenance, active-source preservation and read-only verification. Token recovery is repository scoped and distinct from platform rejection; backend PR operations are explicitly unsupported. The conventional token permission profile is a policy choice, not asserted endpoint minimum.

**E-002 — New lifecycle live acceptance is still pending.** Historical explicit-source consumer cases and local helper checks do not exercise current lifecycle additions against a live dedicated backend or prove installed routing. Follow-up: run the existing live-acceptance prompt in acceptance/textstats/README.md on an explicitly supplied dedicated test repository, using pinned current source and independent assessment; exercise projection/closure/reopening/readback plus controlled and uncontrolled interruptions. No test repository was supplied for this review, so no hosted task objects were created and no live acceptance pass is claimed.

## U-004 — TextStats support and composed checks

Reviewed the portable setup/execution/recovery/diagnostic contracts, preparation brief, catalog dependencies and independent criteria, helper implementation, actual-output capture and renderer, and support-test coverage. Setup asks for a dedicated repository before writes, preserves pinned source and separates product/evidence branches. Controlled and uncontrolled interruptions explicitly require observed partial actions, separate fresh continuation and exact Git/index/object restoration. Deterministic checks are correctly distinguished from independent behavior assessment. Both manifest layouts and binary/executable package state are supported; recovery tests reconstruct staged/unstaged work, deletions, conflicts and an unreferenced incoming merge commit. These are local support observations, not live plugin acceptance.

Actual commands on unchanged baseline helper source:

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: exit 0, **68 tests passed**, 12.484 seconds, no reported skips/failures. [Raw output](evidence/support-tests.txt).
- `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`: exit 0, **27 static cases valid**, live_acceptance false. [Output](evidence/catalog-validation.json).
- `PYTHONDONTWRITEBYTECODE=1 python docs/dev/reviews/017_54d55ed/evidence/ownership-probes.py`: exit 0; control detects duplicate T-001, three counterexamples contradict intended ownership semantics. [Reproduction](evidence/ownership-probes.py), [actual results](evidence/ownership-probes.json). This script reports observations; exit 0 does not mean the counterexamples meet the contract.

### R-001 — Custom task IDs can evade duplicate ownership checks

**Severity:** Medium. **Confidence:** Confirmed by reproduction. **Location:** acceptance/textstats/scripts/core.py, `ownership`, checkbox identifier regex; skills/sdd-tasks/references/task-derivation.md, stable ID convention.

The plugin allows project-specific stable IDs; the checker recognizes checkbox IDs only with prefix `T-`. A TASKS list containing T-001 and F-001 plus FEATURE-TASKS containing F-001 is accepted and returns only T-001. The valid control with T-001 duplicated is rejected. With only non-T IDs, valid work can instead be reported as an empty collection.

**Impact:** The deterministic task-ownership check can pass an actual duplicate executable owner or reject a permitted ID convention. Independent assessment remains required, but this does not repair an inaccurate deterministic result.

**Proposal:** Define an explicit supported task-ID parsing contract consistent with accepted project conventions, then parse every active task or fail closed on unsupported task syntax. Preserve parent/task distinction and exact IDs; do not simply treat all checkboxes as tasks. **Recheck:** Mixed/default/custom ID fixtures reject duplicates across both active lists, valid custom IDs are recognized, and unsupported entries cannot be silently omitted. Add genuine regression scenarios to test_checkers.py; retain this counterexample's original outcome.

### R-002 — Non-owning Markdown is interpreted as executable task ownership

**Severity:** Medium. **Confidence:** Confirmed by reproduction. **Location:** acceptance/textstats/scripts/core.py, `ownership` recursive link traversal and line parsing.

The helper follows every local Markdown link from an owning list and parses task-like rows/checkboxes without excluding fenced examples. TASKS containing T-001 and linking a report that summarizes T-001 is rejected as duplicate ownership, although that report is evidence. A fenced illustrative T-001 checklist in TASKS also causes rejection. The helper contract calls for linked child **lists**, not every linked specification/report/example.

**Impact:** Valid task/report navigation and documentation examples can block case assessment; attempts may be misdiagnosed as consumer ownership failures or prompt unnecessary product edits.

**Proposal:** Limit traversal to explicitly designated active task-list children and exclude fenced/non-executable examples using a deliberate Markdown ownership model. Keep reports/contracts as evidence rather than owners; preserve active-child duplicate detection and archive exclusions. **Recheck:** Both reproduced non-owner fixtures pass, linked active child tasks are included, actual duplicate owners still fail and historical snapshots remain excluded. Do not weaken duplicate detection merely to accept linked reports.

### R-003 — Consequential helper interfaces lack local API documentation

**Severity:** Low. **Confidence:** Confirmed source inspection. **Location:** acceptance/textstats/scripts/core.py and tests/support.py, test_checkers.py, test_preflight.py, test_recovery.py. [Module inventory](evidence/module-documentation.json).

The standalone HELPER-INTERFACES guide gives useful operational contracts, but 24 top-level core interfaces lack docstrings, including package, prepare, export_recovery, reconcile and assessment. Four support/test modules lack module responsibility docstrings. The plugin's own sdd-docs policy calls for module and consequential interface documentation.

**Impact:** Maintainers must inspect large function bodies and cross-reference a separate guide to establish mutation, failure and recovery guarantees. This is a documentation/maintenance gap, not a demonstrated functional failure.

**Proposal:** Add concise responsibility docstrings to the four modules and focused API contracts for consequential helpers, linking the canonical guide without duplicating it wholesale. An alternative is an explicit internal-interface documentation policy with equivalent discoverability. **Recheck:** A documentation review checks actual arguments/results, Stop/error behavior, side effects and invariants against callers/tests; existing support tests continue to pass. No module split is proposed solely on file size.

## Assessment and proposed correction queue

**Demonstrated:** Package/resource integrity and normalized installed skill equality, coherent source-level lifecycle/ownership traces, 68 local helper tests and static catalog validity. **Issues:** Two reproduced ownership-checker defects and one documentation gap; accepted document QC source implementation is pending; installed metadata and live acceptance remain open. **Actions taken:** Review records and reproducible evidence only. No SDD Manager skill, package metadata, acceptance implementation or product source was repaired. **Proposed changes:** R-001/R-002 checker repairs, R-003 documentation maintenance, and completion of the existing campaign 011 QC revision.

| Priority | Proposed next action | Ownership / acceptance boundary |
| --- | --- | --- |
| 1 | Correct R-001/R-002 together as one cohesive ownership-parser increment with independent regression fixtures. | TextStats harness implementation/testing; source repair requires a separately accepted revision. |
| 2 | Execute pending 011 QC actions, retaining its finding/action provenance and avoiding duplicate policy sources. | conventions, specify, plan, tasks, report and manage; TextStats criteria must exercise actual conformance failures and justified shapes. |
| 3 | Address R-003 within helper documentation scope. | Documentation owner; no speculative module fragmentation. |
| 4 | Refresh/version distributed presentation and verify installed source/UI (E-001); run dedicated live acceptance (E-002). | Package/client verification and TextStats coordinator; repository/client facilities required. |

There is no newly confirmed defect in the reviewed skill lifecycle instructions. The two functional findings are in acceptance support and therefore weaken diagnostic evidence rather than proving the product workflows fail. A source-level review cannot establish fresh-agent routing or live GitHub ordering. Python 3.12 was exercised in this environment; minimum Python 3.11, other operating systems, installed icon rendering, protected credential recovery and live provider interruptions were not newly exercised. Historical reports were used for pending-work/provenance context, not certified again as current runtime evidence. Consumer cases A-001–A-027 were not run anew.

No correction queue is marked accepted or implemented by this review. Finish publication and verified integration of these review records, then stop before repairs.

## Publication and integration evidence

Review checkpoints c1a08db, 676458f, 30212d5, 56f26aa and 3bb2bc5 were pushed on revision/017_54d55ed-comprehensive-review. Final working tip: `3bb2bc57e2272fbef79b4e5c65cc7ed1d6201151`. Refreshed target: `54d55edebd8a7af6499d625bdbb357f864a4db1d`.

Explicit merge `68748e872c8fb2dca8b94af269e05993f87b4db6` has exactly those two parents. The prospective merged state passed staged diff checks, baseline source SHA-256 equality, review-record link/JSON validation, review-only path-scope inspection and absence-of-conflicts checks. The full helper suite was not repeated because integration changed only review records and exact helper source hashes remained unchanged. No conflict resolution or source repair was needed.

The merge was pushed to origin/feature/architecture-revision; actual ls-remote readback confirms the target at that merge and the review branch at its final working tip. This follow-up records observed publication on the target; it makes no new source claim. Stop boundary: completed comprehensive review and proposed correction queue, before repair implementation. Working branch retained; main was not merged or pushed by this campaign.

## Planning disposition — 2026-10-04

The human requested an implementation plan and explicitly deferred campaign 011 QC implementation and live/client acceptance to a separate later review. [REVISION-PLAN.md](REVISION-PLAN.md) selects R-001/R-002 checker repairs and R-003 documentation maintenance for planning; source execution has not started. The original observations and proposed queue above are retained as review history. The current plan takes precedence for the next revision's scope: P-001 and E-001/E-002 are pending TODOs, outside its actions and exit requirements.

| Disposition | Work | Current state |
| --- | --- | --- |
| Planned revision | R-001, R-002, R-003 | Plan prepared; implementation not started. |
| TODO-017-001 | Campaign 011 QC implementation / P-001 | Pending; separate later review. |
| TODO-017-002 | Live/client acceptance / E-001/E-002 | Pending; separate later review. |

Both TODOs must remain visible in the future revision report and handoff; completing the selected repairs cannot establish their completion.

## Revision disposition — 2026-10-04

The human commanded the prepared revision. R-001/R-002 ownership behavior and R-003 helper documentation have been repaired and rechecked; actual action evidence and integration status are recorded in [REVISION-REPORT.md](REVISION-REPORT.md). Original baseline findings/probe outputs are retained. TODO-017-001 campaign 011 QC implementation and TODO-017-002 live/client acceptance remain pending for a separate later review, outside this revision.
