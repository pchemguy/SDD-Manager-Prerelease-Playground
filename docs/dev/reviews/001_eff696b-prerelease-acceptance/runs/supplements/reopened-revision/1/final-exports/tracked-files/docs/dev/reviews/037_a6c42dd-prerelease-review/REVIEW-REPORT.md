# Comprehensive prerelease review report

## Campaign, candidate and evidence

- Campaign: `037_a6c42dd`; [review plan](REVIEW-PLAN.md), [complete source inventory](SOURCE-INVENTORY.md).
- Exact reviewed source: `a6c42dd754843abf9bafca7dee2aee9e733b046a`; version `0.15.0`. Reviewer: coordinating assistant, 2026-10-09 UTC; no independent/fresh reviewer is claimed.
- Exact locally built package: `sdd-manager.zip`, 132 regular files, 298720 bytes; SHA-256 `52a828f85e7ff619a0ebe028b446650ba999d89b2445efe573714ba96a012b2d`.
- Branch: `revision/037_a6c42dd-prerelease-review`; main is unchanged. Review authority covers artifacts/publication and scoped checks, not repairs or product release.
- State: Resumed by the human on 2026-10-10 for the campaigns 038–041 supplemental assessment at `b246f8f92f35a8d2077bce467102f63270d64f2b`. U-001–U-007 below retain the original candidate assessment; U-008 below is complete at source/package level; independent live behavioral acceptance remains unexecuted. Original four Open defects (one P1, three P2) and one Open P2 evidence gap remain; revision execution not started.
- Findings remain Open unless an actual human disposition is recorded. No deferral or risk acceptance has been supplied.

## Original candidate: unit coverage and checkpoints

| Unit / criterion | Outcome and evidence | Findings | Persistence |
| --- | --- | --- | --- |
| U-001 / C-001 | Root documentation/manifest/prompt/notices and all nine convention references inspected; supported owners, scope and frozen-history rules coherent. | None | `a7a3da2ea7ea384edd4525bbc2858b196176bdcc`; push/readback matched. |
| U-002 / C-002 | All five preparation/incorporation skill entries and thirteen focused references inspected; scope, ownership, QC and human checkpoints align. | None | `2fc398a3113d3a218989d952153d4c532c749233`; push/readback matched. |
| U-003 / C-003 | All manager/orientation/execution/steering entries and references assessed; owned effects, continuation and stopping gates are explicit. | None | `a5758ed0401b15cc2d5eb443a882fd124f92a49b`; push/readback matched. |
| U-004 / C-004 | All docs/report sources and current root/capability navigation assessed; two located documentation defects; four diagrams semantically inspected, rendering unavailable. | R-001, R-002 | `d0500161e92aad53a69f3ed2f95c6aa68df5b319`; push/readback matched. |
| U-005 / C-005 | All eight forge references and actual release CI assessed; curated-note transfer and publication recovery/verification are missing from CI. | R-003, R-004 | `983393b224e00e76f400fee7fff98aa4851e78ae`; push/readback matched. |
| U-006 / C-006 | Both entries/all nine TDD/verify references assessed; harness implementation and case assets inspected; 113 support tests and 27-case static catalog pass. | None | `3fccd6b8e042369dc1880f57891cb4933532162d`; push/readback matched. |
| U-007 / C-007 | Actual 132-file ZIP matches pinned source byte-for-byte; archive/resource checks pass except R-001 root links; presentation rendered; strict portable-format limits retained. | None | This unit report checkpoint; commit/push readback established in Git before the next unit. |

## Assessment detail

### U-001 — Product scope, authority and conventions

Inspected root README/AGENTS.md, canonical/legacy manifest contract, greenfield prompt, usage/disclosure assets and root notices/license, ignore rules, and every sdd-conventions entry/reference. S-001–S-003 source-assessed: README explicitly distinguishes source checkout from installed package, local support from live acceptance and lack of universal format conformance; root AGENTS routes current owners without reproducing the workflow chain. Direct calls retain the same conventions and authority constraints; explicit user/project instructions control. Shared hierarchy, phase lifecycle, QC, modularity, identity and closed-record criteria are mutually consistent. The 3–5 decomposition preference is explicitly a heuristic with exceptions, not padding or a quota. No confirmed finding in this unit. Package portability/resource resolution and diagram implications are reserved for U-004/U-007 rather than inferred passed here.

### U-002 — Preparation and feature incorporation

S-004–S-007 source-assessed across sdd-design, sdd-specify, sdd-plan, sdd-tasks and sdd-integrate-feature. Main roots retain complete intended end-state contracts; logical design, behavior, delivery, physical placement and task status have separate owners. Feature overlays are conditional, stable task IDs are project-wide and transfer requires both lists in scope. SPEC-only incorporation preserves unselected active sources and reports their invalidation rather than expanding edits. Archive procedure keeps eligible sources/reports together, updates active links and freezes history only after closure. New PLAN strategy and layout have separate human/QC checkpoints; existing adequate layout is reusable. Missing upstream readiness triggers focused review; downstream owners cannot rewrite requirements/strategy to fit their outputs. Code-review/testing/report tasks are derived from PLAN rather than inserted during execution. No confirmed defect found at instruction-source level; actual consumer execution remains unverified.

### U-003 — Coordination, execution and recovery

S-008–S-012 source-assessed. Compared manager coordination/branch/QC/human/tracking/activation/bootstrap/credentials/Git/campaign/profile/examples/workflow sources with orient inspection and implement/steer execution references. Partial main-phase ranges pause without merge; complete phases integrate only after review/exit/hosted closure gates. Clean-tree continuation resolves outstanding publication first. Every owned commit, including ancillary report/status and merge commits, must be pushed/read back before independent or dependent work; uncertainty permits inspection/recovery only. Existing merge/publication is finished rather than duplicated; unrelated staging/dirty work is preserved. Steering updates existing owners, targets the paused branch, reconciles changed acceptance and stops without resuming implementation. Preparation, review, tracking activation, human acceptance and permission capability remain distinct. The new prerelease reminder is advisory and explicit review is candidate-scoped/report-only unless separately authorized. No confirmed instruction defect in this unit; these branch paths were assessed, not executed in a fresh product consumer.

### U-004 — Documentation, reporting and diagrams

S-013–S-015 assessed: all four README diagrams preserve owner handoffs, repair loops, authorization and stop branches; preparation prose explicitly preserves separate human checkpoints despite grouped design/PLAN-layout nodes. No semantic diagram defect confirmed. No Mermaid CLI/module is installed, so syntax/rendered legibility are not certified. Documentation/report owners consistently separate drafting from effects, verified results from intended outcomes, adjacent QC reports from implementation/campaign records and findings from accepted deferrals. Broad static discovery checked 166 current Markdown documents and 488 local link occurrences without loading closed record contents; candidate hits were manually classified. Fence-first headings, template-relative example links and inline bootstrap copy examples are legitimate template content, not confirmed broken source links/style defects. Actual package root navigation and current capability map misalignment produced R-001/R-002. Professional-module/API documentation is also assessed with executable tooling in U-006.

### U-005 — Hosted tracking, highlights and releases

S-016–S-019 source-assessed across projection, exact issue/milestone identity and lifecycle, permissions, retry/readback, highlights, package, workflow and release ownership. A disposable real Git fixture executed the documented highlights collection recipe: previous stable first-parent baseline selected, merged feature commit and full multiline body retained, and the pending tag rejected as its own baseline. This does not exercise editorial curation or incremental-watermark agent behavior. Actual tag-only release.yml checks metadata, runs support tests, archives members and calls unconditional gh release create with generated notes. Compared with its current canonical requirements, it lacks the shared curated-note transfer (R-003), serialized/reconciled publication and actual archive/remote verification (R-004). Current primary actions repositories advertise checkout/setup-python v7; these are not invalid action references. Primary CLI/provider references consulted: https://cli.github.com/manual/gh_release_create, https://github.com/actions/checkout, https://github.com/actions/setup-python and https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases (2026-10-09). No live tracking write, CI run, release, installed download or latest-state mutation was performed. One initial U-005 read occurred after U-004 push acknowledgement but before remote readback completed; no mutation/commit intervened, and matching containment was confirmed before continuation.

### U-006 — Verification, TDD and acceptance support

S-020–S-022 assessed. Inspected core configuration/schema validation, committed/dirty package pinning, repository identity, actual Git/remote containment, recovery exports, task parsing/ownership and deterministic assessment, all auxiliary command/fault/probe/merge/coverage helpers, capture and catalog renderer, support test modules, schemas, coordinator instructions, all consumer requests and 27 independent guides. Catalog/contracts/fixture consistency were additionally exercised by the actual suite. Tests include wrong channels/status/type, duplicate owners, invalid/escaping/symlink paths, absent/ambiguous prerequisites, false scripted grades, failed/partial provenance, protected output, staged/unstaged/deleted/binary/conflict reconstruction, public-API regression sensitivity and shallow ancestry uncertainty. Expectations are independently literal and helper success explicitly remains non-agent evidence. Test fixture lstrip is a deliberately narrow two-vector probe fixture, not the product implementation or an assertion of full BOM semantics. Actual command: PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v; exit 0, 113 tests in 17.188s, OK, no skips reported; Python 3.12.14, Git 2.51.1. catalog_tools.py validate exited 0 with 27 cases and live_acceptance false. Python 3.11 and other environments were not executed. No dedicated live test repository is selected by this review; source/harness inspection and disposable local tests do not run the TextStats consumer campaign, install a client or certify fresh-context recovery. No confirmed additional defect in this unit; remaining runtime acceptance evidence is R-005.

### U-007 — Exact package, presentation and consolidation

S-023–S-025 assessed. Verified ZIP CRC, exact and case-fold duplicate absence, root prefix, traversal/absolute/backslash/symlink safety, complete expected source inventory, per-member Git-object bytes, byte size and SHA-256, and development/acceptance/Git/cache/credential-path exclusions. Canonical and legacy manifest bytes match; version and declared skill root agree. Parsed all 15 openai.yaml files, checked prompt names/description lengths and all 34 icon/logo references (17 distinct SVGs); parsed SVG XML, rendered all 17 with existing Inkscape and visually inspected the contact sheet: no clipping, missing glyph or illegible mark found at 100px. This is artwork evidence, not an installed-client UI result. Resolved 296 skill Markdown resource occurrences inside the whole extracted package; three future-output/bootstrap inline examples were manually classified rather than treated as links at the source reference location. An initial simplistic regex probe falsely flagged those examples and angle-bracket Markdown; corrected classification produced no missing skill resource. Root links to excluded source-only members remain R-001. Offline Agent Skills validator: sdd-conventions passes, other 14 fail on 31 cross-skill resource-root constraints. Agent Plugins 1.0 validator exits 1 with 35 errors: missing standard $schema, three client-specific manifest fields and the same 31 cross-skill escapes. Whole-package resolution succeeds, but standalone portability and strict standard conformance are not certified; current README already disclaims universal conformance, so this is not invented as a newly required migration defect. Source-only support is intentionally excluded. No installed-client discovery/activation or hosted asset/download was exercised. No further confirmed defect.

## Canonical findings

| Finding | Type | Priority | Disposition |
| --- | --- | --- | --- |
| R-001 | Defect | P2 | Open; proposed, no human acceptance/deferral recorded. |
| R-002 | Defect | P2 | Open; proposed, no human acceptance/deferral recorded. |
| R-003 | Defect | P1 | Open; proposed, no human acceptance/deferral recorded. |
| R-004 | Defect | P2 | Open; proposed, no human acceptance/deferral recorded. |
| R-005 | Evidence gap | P2 | Open; expanded for the supplemental candidate below; no human acceptance/deferral recorded. |
| R-006 | Improvement recommendation | P3 | Open; supplemental implementation-diagram proposal; optional, not a demonstrated workflow defect. |

### R-001 — Packaged root navigation points at excluded source-only paths

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Defect; P2; high confidence from actual ZIP inventory and extracted-path resolution. |
| Baseline location / evidence | README.md, Plugin package and Testing with TextStats/current evidence links; AGENTS.md, Source and instructions. The pinned archive has 13 root link occurrences targeting absent acceptance/ or docs/ members (11 README, two AGENTS), including acceptance/textstats/README.md, acceptance/textstats/AGENTS.md, docs/dev/CAPABILITY-MAP.md and docs/dev/reviews/README.md. |
| Observation / consequence | Repository links exist, but those same relative targets cannot resolve in the delivered package. Explicitly saying source-only material is excluded does not provide a working destination for an installed reader/agent. Package orientation and evidence navigation are incomplete. This is a defect in current root documentation, not historical-record compatibility. |
| Bounded correction / owner | sdd-docs with sdd-manage package orientation: point source-only references in current packaged root files to explicit source-repository URLs (prefer pinned/version-associated provenance where appropriate), while keeping shipped resource references local. Preserve all closed records and the existing package exclusion contract. |
| Objective recheck | Extract the candidate archive and verify every root local link resolves within it; inspect source-only external targets at the chosen source provenance. Recheck README/AGENTS audience, scope and packaged-resource links. |
| Decision / dependencies | Open; proposed bounded root-document repair. No decision to expand the archive or claim live installation support is implied. |

### R-002 — Current capability map trails the supported workflow contract

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Documentation misalignment; P2; high confidence from current document/source comparison. |
| Baseline location / evidence | docs/dev/CAPABILITY-MAP.md, Core development workflows says feature retention under docs/dev/features/<campaign>, while workflow-identity.md requires matching <campaign>-<slug>. Its sdd-forge capability row describes tracking only, omitting the shipped highlights/package/workflow/release references; the map also omits the design-docs/default preparation baseline, per-commit publication and human created-document checkpoints present in current owners. |
| Observation / consequence | This current document claims to describe intended capabilities and present ownership/status, but sends readers to an incomplete capability model and a stale generic feature path. It can obscure release support and the required preparation/publication/human gates. It is not a closed campaign artifact. |
| Bounded correction / owner | sdd-docs/current map owner: reconcile the concise map with current supported capabilities and branch/artifact paths; link canonical release, preparation, publication, human review and optional prerelease policies rather than reproduce their detailed procedures. |
| Objective recheck | Compare every capability row and workflow/path rule with current entries and canonical owners; resolve current local links and check that gate summaries distinguish human acceptance, technical QC and publication. |
| Decision / dependencies | Open; map-only repair proposal. Does not authorize editing frozen history or redesigning the workflow. |

### R-003 — Configured release workflow cannot receive shared curated highlights

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Defect; P1; high confidence from complete workflow and canonical release-source comparison. |
| Baseline location / evidence | .github/workflows/release.yml, Publish GitHub release uses only --generate-notes. skills/sdd-forge/references/github-release-workflows.md and github-releases.md require a prepared transfer of shared curated highlights before a tag-triggered publisher; the ignored local highlights file is absent from checkout and no input/artifact/file transfer is configured. |
| Observation / consequence | The configured automated publisher cannot deliver the required curated human release body. The supported release path therefore fails its own required contract even when source metadata and support tests pass. |
| Bounded correction / owner | sdd-forge workflow owner: define and implement one exact-candidate curated-note transfer and consume it in the existing publisher; retain human editorial sections and reject missing/mismatched transfer. Keep prerelease comprehensive review advisory. |
| Objective recheck | Exercise the chosen transfer on a disposable authorized release target: exact candidate/body, missing and mismatched notes, and generated-note exclusion; read back the published body against the approved curated content. |
| Decision / dependencies | Open; blocks readiness of the configured tag-triggered publishing path. A different authorized compliant route would require its own verified evidence. |

### R-004 — Actual release CI omits required reconciliation and verification

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Defect; P2; high confidence from actual workflow; no claim that a corrupted hosted asset was observed. |
| Baseline location / evidence | .github/workflows/release.yml has no concurrency policy, existing-release lookup/reconciliation, inspection of the actual ZIP contents, or remote source/body/assets/checksum/latest-state readback. It ends with unconditional gh release create. Current github-release-workflows.md, github-packaging.md and github-releases.md require these boundaries. |
| Observation / consequence | A rerun or uncertain publication has no explicit recovery path, overlapping publishers are not serialized, and successful CLI exit is treated as completion without evidence of the required delivered inventory/body. Metadata checks and a checksum calculation do not establish the inspected artifact or remote result. |
| Bounded correction / owner | sdd-forge workflow owner: reconcile an existing matching release and serialize the publisher; inspect the built archive before publication and read back required source, notes, asset inventory/checksum and selected latest/prerelease state. Stop safely on mismatch without clobbering unrelated content. |
| Objective recheck | Run first publication, rerun, partial/uncertain write and competing-run cases in an authorized disposable target; inject a wrong/missing archive member and mismatched existing source/body/asset. Verify safe stops, recovery and final remote evidence. |
| Decision / dependencies | Open; requires affected publishing-path recheck with R-003. No actual human acceptance of this verification/recovery gap is recorded. |

### R-005 — Current candidate lacks fresh-consumer and installed-client acceptance evidence in this review

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Evidence gap; P2; confirmed absence in this campaign, not a claim that the plugin fails at runtime. |
| Baseline location / evidence | README.md Testing with TextStats and acceptance/textstats/OBJECTIVES.md, EXECUTION.md and DIAGNOSTICS.md distinguish support/static tests from independently assessed consumer behavior. U-001–U-006 scenarios were source-assessed; the actual 113-test suite exercises harness/local fixtures, not current candidate agent routing, human gates, installation, live tracking or fresh continuation. |
| Observation / consequence | This report cannot certify those consequential supported workflow handoffs or installed discovery. Structural coherence and passing support tests leave current runtime behavior unestablished; unavailable evidence does not establish a product defect or retroactively erase retained historical results. |
| Bounded correction / owner | sdd-manage/acceptance coordinator: separately authorize a dedicated consumer acceptance destination and facilities, pin the repaired candidate, execute applicable required cases with separate consumers/assessors, and explicitly retain client/live/native limits. Prioritize publication barriers, human checkpoints, preparation QC and the optional-review distinction while covering current supported workflows. |
| Objective recheck | Publish independently assessed real case attempts with exact source/package/runtime, handoffs, first results/interventions, actual Git/provider effects and required/optional totals; distinguish explicit-source loading from installed client discovery. Reassess readiness for that exact candidate. |
| Decision / dependencies | Open; proposed follow-up acceptance scope. No human waiver/deferral has been recorded. It limits runtime acceptance claims; it is not a fabricated failure or a newly mandatory prerelease campaign gate. |

## Executed checks and limits

| Executed check | Observed result / exact boundary |
| --- | --- |
| Declared support suite | Python 3.12.14 / Git 2.51.1; `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`; exit 0; 113 tests in 17.188s, OK, no skips reported. Product/support source bytes equal the pinned candidate; only campaign artifacts differed on the review branch. |
| Catalog | `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`; exit 0, 27 cases, static validation, live acceptance false. |
| Highlights recipe | Disposable real Git repository with stable baseline, merged multiline feature message and pending tag; baseline/message inclusion and pending-self-baseline rejection passed. Editorial/incremental agent behavior was not executed. |
| Documentation discovery | 166 current Markdown files / 488 local-link occurrences; candidate hits manually classified. Closed campaign contents were neither loaded nor checked. R-001 identified from actual archive paths; R-002 from current owner comparison. |
| Candidate archive | Exact unchanged workflow `git archive` selection at pinned SHA; 132 regular files, 298720 bytes, SHA-256 `52a828f85e7ff619a0ebe028b446650ba999d89b2445efe573714ba96a012b2d`; CRC, names/safety, exclusions and every member byte checked against Git objects. |
| Packaged skills/presentation | All 15 presentation YAML files, 34 referenced artwork paths / 17 SVGs, and 296 local skill-resource occurrences checked; examples classified manually. Inkscape rendered 17 assets; visual inspection at 100px found no defect. |
| Strict offline validators | Agent Skills: one passes, fourteen fail on 31 cross-skill escapes; Agent Plugins 1.0: exit 1 / 35 errors (four manifest constraints plus 31 resource escapes). These are actual limited-format failures, not all-green results or installed-client evidence. |
| Release CI source | Tag trigger, metadata/support/build/publisher inspected; YAML parsed. Actual publisher misses required notes transfer and reconciliation/verification. Official action repositories confirm current v7 references; no live CI run occurred. |

Unavailable/not executed: Mermaid syntax/rendered legibility (no local Mermaid renderer); fresh consumer/independent-assessor runtime acceptance; native interruption/recovery; installed-client discovery and activation; live hosted projection/release/CI/download/latest-state checks; Python 3.11 and other platform/runtime compatibility. No online mutation was performed beyond the authorized campaign Git publication. Four README diagrams received semantic source assessment, which does not certify rendering. Existing artwork rendering required no new installation. Broad style/link discovery and source assessment do not prove every possible Markdown parser or instruction execution.

Check probes preserve unsuccessful/limited outcomes: an initial package-link regex assertion produced false positives for documented future-output/inline examples and angle-bracket Markdown; manual classification plus corrected resource resolution followed. CairoSVG was unavailable; existing Inkscape successfully rendered artwork. Neither probe modified product files. U-005 records the one publication-readback ordering deviation and containment confirmation.

## Readiness and revision handoff

The pinned candidate is **not ready for its configured tag-triggered publishing path**: R-003 is a demonstrated P1 failure of the required curated-note transfer. R-004 leaves prescribed recovery/archive/remote verification incomplete. Local support and source/package structural checks passed within their boundaries; they do not cure these publishing failures or establish runtime acceptance. R-001 is a delivered-package navigation defect; R-002 is current documentation misalignment. No data corruption, live provider failure or rendered diagram defect was observed.

| Proposed next scope | Findings / completion boundary |
| --- | --- |
| Release publisher correction | R-003/R-004: one exact-candidate notes transfer, serialized/reconciled publisher, actual archive inspection and final readback; authorized disposable first/retry/failure checks. Treat as a required publishing-path correction, not an optional review reminder gate. |
| Current documentation correction | R-001/R-002: root source-only navigation and concise current capability map; package/source link and owner-alignment rechecks. No closed-record edits. |
| Separate consumer acceptance | R-005: obtain an explicitly authorized dedicated test destination/facilities; execute independently assessed candidate-specific consumer cases and retain client/live/native limits. |

All five findings remain **Open**. There are no accepted repairs, rejected findings, human-accepted deferrals or waived checks. R-002 may be proposed for deferral if the human decides its consequence is acceptable; no such decision is recorded. R-005 limits runtime claims and is not a newly mandatory comprehensive prerelease-review gate. Strict portable-standard migration is not selected; record the demonstrated compatibility boundary rather than imply universal support. Diagram rendering and unrepresented platforms remain unavailable evidence, with no invented pass or deferral.

This readiness assessment applies only to source `a6c42dd754843abf9bafca7dee2aee9e733b046a` and the pinned package hash. Repairs or any new candidate require a new pin and affected unit/handoff/regression rechecks; retain original findings and evidence. Publish this review report and stop. A separately accepted revision plan/execution scope, main integration and product release publication remain outside the completed review authority. Main and all product source/closed records remain unchanged; campaign 037 stays available for revision planning.

## Suspension checkpoint

The human suspended prerelease campaign 037 on 2026-10-10 to open a separate focused tracking-fidelity review/revision campaign from this branch. Preserve the completed assessment, original candidate identity and all five Open findings. This suspension neither accepts proposed repairs nor clears the release blocker. The focused campaign will retain its own findings/proposals; no product change is authorized by that review alone. Resume 037 only when directed, inspect its actual branch state and re-pin/recheck affected coverage if product source or package changed. Main remains unchanged.

## Resumed comprehensive assessment: campaigns 038–041

### Candidate, authority and coverage

The human resumed 037 on 2026-10-10 and selected assessment of the four integrated campaigns, then explicitly authorized pushing this campaign's updated review plan and report to `pchemguy/SDD-Manager`. Resume plan checkpoint: `dd33132f71860e0eb7169dec68eab49c31024f74`; push and exact remote branch readback confirmed before this unit. Two earlier publication attempts were rejected by host automatic review; after explicit authorization, missing shell credentials were recovered from the existing ignored repository credential. No secret values are retained here.

- Supplemental reviewed product source: `b246f8f92f35a8d2077bce467102f63270d64f2b`, version `0.15.0`. Review date: 2026-10-10; coordinating assistant, not an independent fresh consumer.
- Workflow-shaped local package: 133 regular files, 317420 bytes; SHA-256 `7a4d5893c1413246d7553f8577202eecd3123e79efa20d31a3cc0da630c5614a`. Built with the unchanged workflow's exact `git archive` selection at this SHA; not a hosted release or installed-client package result.
- U-008 / C-001–C-007: all 33 changed current product/support paths inspected, plus relevant unchanged lifecycle, preparation, release and recovery authorities. The appended [source inventory](SOURCE-INVENTORY.md#supplemental-candidate-inventory) records exact changed blobs and unit effects.
- Selected child report/merge consultation establishes delivered scope and historical evidence only. Campaigns 038–041 remain closed and unmodified. Earlier child source walkthroughs, hypothetical assessments and support results are not relabeled as newly executed or independent live acceptance.
- Scope stops at this published assessment. No source repair, revision execution, child reopening, main merge, tag/release, hosted tracking write, publisher dispatch or full TextStats acceptance ran.

### Campaign subassessments and cross-unit effects

| Campaign / integration | Assessed current sources and affected units | Assessment / findings |
| --- | --- | --- |
| 038 / `8bb3b3d` | Manager dispatch, tracking-decision/phase-activation, executor direct/resume/completion, forge entry, shared lifecycle, workflow examples and source-only fidelity follow-ups; U-001/U-003/U-005/U-006. | Requested/confirmed tracking is separate from pending/verified projection. Initial, partial, unknown and added-work projection block affected edits/tests; an outage permits only independent already-projected work with satisfied dependencies. Omission recovery preserves results/history and differs from genuine late confirmation. No new confirmed source defect. Consumer comparison remains unexecuted: consolidate under R-005, preserving child R-001/R-002 Revised and R-003 Open rather than importing them as parent Verified findings. |
| 039 / `7f06904`, `f64e7eb`, `a0685b5` | Root greenfield prompt, current tracking/activation, human-review and authorization authorities; U-001/U-003/U-004/U-007. | Description-last order, persistent scoped repository authority, optional-token guidance and named activation/readback/stop are mutually consistent. Token availability is not API operation support or a tracking decision. Human document checkpoints and later scope changes are preserved. No new confirmed source defect; ordering/wording does not prove improved agent retention (R-005). |
| 040 / `e24f30c`, `ca99ca1` | Revision-modes, branch/identity/frozen-record owners, review lifecycle, Git integration, report summaries, forge highlights, release notes/checks, root overview/examples; U-001–U-005/U-007. | New nested identity defaults to immediate parent source/return target; integration/return does not resume the parent. Reopening needs human authority and the latest qualifying first-parent published closure; original opening and branch-off remain distinct. Summary producer/consumer handoffs preserve cumulative context, new delta, direct/revert/resolution coverage, ancestry, deduplication and analyzed watermark. Phase delivery and accepted design-docs preparation remain distinct. Ten current recipe fixtures pass; semantic curation and consumer compliance remain R-005. Current capability-map omissions expand R-002. |
| 041 / `b246f8f` | Manager/orientation entries, task execution/completion/continuation, report subjects, Git integration audits and root AGENTS; U-001/U-003/U-004/U-007. | One executable task closes per commit with result/current evidence/initial owning checkbox; exact leading single ID and staged/committed composition inspections are explicit. Authorized partial checkpoints, later repairs and eligible parent-only follow-ups do not permit detached initial task completion. Audit/recovery preserves published violations and requires scoped disposition; non-task campaigns/preparation/merges invent no task IDs. No new confirmed source defect; actual task-execution compliance remains R-005. Diagram discoverability is optional R-006. |

The detailed rules retain canonical owners and link callers rather than creating another registry or journal. Some invariants are restated at consequential entries to make direct invocation enforceable; no competing detailed authority was confirmed. Reporting drafts remain separate from execution authority, and recovery does not imply history rewriting. Both sides of the changed handoffs were compared.

### Supplemental source scenarios

These are coordinating-reviewer source applications, not independent agent executions. The outcome means current instructions support the stated boundary, not that an agent or provider actually followed it.

| Scenario | Located supported outcome |
| --- | --- |
| Broad explicit tracking request, no objects yet | tracking-decision and manager dispatch retain confirmation; phase-activation requires eligible objects/readback before edits/tests. |
| Direct executor/resume with missing or partial projection | implementation entry/startup retain work and return a concrete blocker; no manager bypass or automatic local-only downgrade. |
| Backend outage after verified activation | lifecycle/startup/completion allow only independent projected work; required closure, added-work and next-phase gates remain. |
| Original request omitted versus genuinely late choice | tracking-decision distinguishes both; omission recovery retains history/results and reconciles before further affected execution. |
| Token supplied without choice, or after explicit decline | decision table requires an actual scope choice and preserves decline; token guidance distinguishes transport/API support. |
| Broad prompt repository authority | prompt preserves required human document reviews and execution boundaries; description order changes no authority. |
| Nested child while parent is already suspended | revision-modes treats incomplete suspended parent as active; explicit integration/return retains suspension. |
| Related reopening after ordinary commits versus an intervening merge | latest first-parent closure test retains intervening ordinary work and rejects convenient older-campaign fallback. |
| Dirty worktree, unpublished checkpoint or unknown closure | branch/Git/revision-mode owners preserve index/work/history; safe worktree and publication/identity gates precede dependent work. |
| Latest cumulative summary, deleted refs and nested delivery | summary/highlights owners require reachable parent/identity coverage, adequate enclosing context and targeted gaps, not branch-tip proof or duplicate bullets. |
| Direct revert or incomplete summary in an increment | full identity inventory and targeted net changes precede watermark advance; preserve prior baseline and human cuts. |
| Phase versus document-preparation summary | report/highlights distinguish delivered phase exits from accepted preparation/readiness; use canonical design-docs naming. |
| One task result and first completion transition | completion contract inspects staged and committed result/evidence/status with the exact owning leading ID. |
| Bundled result or detached checkbox with a valid subject | composition audit rejects it despite subject shape; explicit recovery/exception needed, no automatic published rewrite. |
| Authorized partial checkpoint and final closure | unchecked partial state and real prior authority remain; closing tree/evidence/check identifies retained checkpoints without duplicating unchanged code. |
| Review task, parent-only follow-up and taskless campaign | substantive review evidence closes its task atomically; parent exception cannot split initial closure; taskless work invents no ID. |

### Original finding reassessment and new recommendation

| Finding | Supplemental evidence / current disposition |
| --- | --- |
| R-001 | Actual package inspection still finds the same 13 root-link occurrences to excluded source-only paths (11 README, two AGENTS). Changed overview/orientation material does not repair them. Open P2 defect. |
| R-002 | CAPABILITY-MAP.md is byte-identical to the original pin. Its original omissions persist; it additionally does not expose requested-tracking readiness, nested/reopened revision modes, cumulative integration/highlights support or the strict atomic task persistence/audit contract. Extend its existing concise owner-alignment correction/recheck to these capabilities; do not duplicate their detailed rules. Open P2 documentation defect. |
| R-003 | Actual release.yml is byte-identical and still uses generated notes with no curated exact-source transfer. New summary/highlights guidance does not implement the publisher handoff. Open P1 publishing-path blocker. |
| R-004 | The unchanged workflow still lacks the prescribed serialized/reconciled publisher, actual archive inspection and remote source/body/asset/latest readback. Local archive verification in this review does not repair CI. Open P2 defect. |
| R-005 | Expand the existing P2 evidence gap to the new tracking retention/entry/outage behavior, prompt fidelity, nested/reopened routing/return, cumulative editorial coverage/deduplication and task composition/audit/recovery. Source walkthroughs, recipe tests and child hypothetical applications establish neither actual task/provider chronology nor installed discovery. Open; no numerical fidelity claim, waiver or accepted deferral. |
| R-006 | Optional P3 implementation-diagram clarity improvement, defined below. No new release blocker or mandatory workflow gate. |

R-005's proposed acceptance scope and objective recheck now include the applicable separately selected tracking-fidelity follow-ups, actual single-task result/checklist/evidence commits, resumed violation handling, nested/amended return behavior and editorial incremental coverage. Retain real first attempts/interventions, exact source/package/runtime/loading mode and Git/provider observations; keep assessor material out of consumers. Missing native/installed/fault facilities remain unavailable checks, not simulated passes. This expands the existing gap rather than allocating duplicate evidence-gap findings for each child campaign.

### R-006 — Make activation and task-persistence gates visible in the implementation diagram

| Field | Evidence / proposal |
| --- | --- |
| Type / priority / confidence | Improvement recommendation; P3; high confidence from source comparison, optional rather than a demonstrated execution defect. |
| Candidate location / evidence | README.md, Implementation and continuation: diagram proceeds from executor resume/select via “task ready” to the development cycle; it shows hosted tracking as a post-commit completion branch. Surrounding prose explicitly places phase/task associations before the first task. New manager/executor owners require requested-tracking projection/readback and persistence audits. |
| Observation / consequence | The prose and linked authorities preserve the gates, so the diagram is not evidence of a contrary policy. Its prominent flow leaves the activation blocker and resume/integration audit implicit; a reader using the visual alone sees those obligations less clearly than current direct-entry instructions. |
| Bounded proposed correction / owner | sdd-docs with sdd-manage/implement: make pre-execution readiness explicit in the implementation diagram or its immediately adjacent key, including requested projection/readback, blocked execution and claimed task-boundary audit; make atomic result/evidence/initial-status closure and applicable integration audit discoverable without copying the full contract. Preserve local-only and already-activated outage behavior and keep the diagram readable. |
| Objective recheck | Compare graph/prose with current phase-activation, startup/completion and Git integration; source-assess requested pending/verified/declined states and violated closing boundary. Render with an available Mermaid renderer and inspect readability. Do not claim consumer compliance from rendering. |
| Decision / dependencies | Open recommendation; no human acceptance or deferral supplied. Separate from R-002's capability-map repair and R-005's behavioral evidence. Not a release blocker. |

All four README diagrams received affected semantic reassessment. Preparation and steering flows retain their established boundaries; the formal review/revision graph remains a general flow with nested/reopened target/return details supplied by current overview and canonical links. No additional semantic diagram defect was confirmed. Mermaid rendering was not executed: no local mmdc was available. Do not turn every omitted detail of an overview into a mandatory diagram requirement.

### Fresh local checks and evidence reuse

| Check | Actual outcome / limit |
| --- | --- |
| Support suite | PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v: 113 tests passed in 16.187s, exit 0; Python 3.12.14, Git 2.51.1. Current product/support bytes equal the supplemental pin; only active campaign artifacts differ. |
| Catalog | PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate: exit 0; 27 cases, static asset validation, live_acceptance false. Supplementary fidelity scenarios do not change default grades/totals. |
| Actual shipped highlights recipe | PYTHONDONTWRITEBYTECODE=1 python docs/dev/reviews/040_a0685b5-revision-campaign-modes/evidence/check_merge_highlights.py: ten disposable real-Git fixture tests passed in 1.094s, exit 0. Extracts/executes current shipped recipe; covers cumulative increment, direct gap/revert, nested/deleted refs, phase/preparation, baseline/pending tags, ambiguity and shallow/invalid ancestry. Mechanical collection, not semantic curation. |
| Package | Exact expected Git archive file set, CRC, duplicate/case-fold duplicate absence, safe names and every regular member's Git-blob bytes passed. 133 files / 317420 bytes and hash above. One new packaged reference is revision-modes.md; source-only follow-ups remain excluded intentionally. Manifest copies identical, version unchanged. |
| Resource/navigation check | 255 nonliteral relative link occurrences in all 33 changed product/support Markdown paths resolve in the source checkout. Packaged skill links resolve after classifying two unchanged bootstrap future-output examples; 13 missing root-source links remain R-001. No new broken skill resource confirmed. |
| Unchanged authorities/assets | Git confirms byte-identical release workflow, capability map, manifests, assets and support test modules against the original pin. Original artwork inspection is retained only for those unchanged bytes; no installed UI claim. Original strict-validator counts remain historical, not a fresh pass for this candidate's new cross-skill references. |

The original comprehensive U-001–U-007 assessment remains evidence for its own pin. U-008 reuses unchanged concerns only where byte identity and the changed handoffs were assessed; it does not falsely report a new line-by-line full-product review. The inventory covers the delta and preserved baseline, with source-only test helpers and changed assessor/consumer guides accounted for. No new dependency, manifest/version, platform or artwork change was introduced by these children. Full standards validators, Mermaid rendering, Python 3.11/unrepresented platforms, fresh consumers/native recovery, installed discovery and live tracking/release/CI remain unexecuted in this continuation.

### Current readiness and stopping point

At `b246f8f92f35a8d2077bce467102f63270d64f2b` and package hash `7a4d5893c1413246d7553f8577202eecd3123e79efa20d31a3cc0da630c5614a`, the configured tag-triggered publication path remains **not ready** because of R-003; R-004's required recovery/readback gaps also remain. Four defects, one expanded evidence gap and one optional improvement recommendation are Open. No original defect was repaired or silently closed by integrating the child campaigns. There are no newly accepted repairs, rejected findings or human-accepted deferrals.

Proposed revision queue remains release publisher R-003/R-004, current documentation R-001/R-002, then separately authorized candidate-specific acceptance R-005; optional R-006 can accompany a selected documentation scope. Priority is consequence-based, not authority to execute. This assessment completes the requested report update and publication, not campaign repair execution or closure/main integration. Campaign 037 is resumed and available for revision planning; version remains 0.15.0. Subsequent source/package changes require affected rechecks against a new exact pin. Final report commit/publication is established by Git and remote readback, not by this precommit prose.

## Revision planning continuation

On 2026-10-10 the human requested pulling origin and resuming 037. The published branch is current at `b2cc1d4`; U-001–U-008 review coverage is complete, so no review unit is repeated. The next artifact is the [proposed correction plan](REVISION-PLAN.md), covering the four defects, recommended optional R-006 documentation scope and separately selected R-005/live-provider evidence. All six findings remain Open; no source repair, finding acceptance/deferral, main integration or release effect is inferred from this planning continuation. Execution selection remains pending.

## Detailed all-target planning instruction

The human requested a detailed plan including all targets and optional targets, an execution-time test repository and clear intermediate commit checkpoints on 2026-10-10. The [revision plan](REVISION-PLAN.md) now includes R-001–R-006, 25 source-campaign checkpoints, full 27-case/32-required-variant TextStats scope, both optional catalog variants and named fidelity/native/client/platform/presentation follow-ups. Actual effects and facilities remain execution inputs; inclusion is not an observed pass, finding closure or source-execution authority.

Initial planning commit `80bc300` is retained locally. Host automatic approval review rejected its publication, stating that pulling/resuming did not authorize publishing new artifacts and the destination was not verified as trusted. Read-only verification confirms the established origin and remote tip `b2cc1d4`; no transport/account workaround or repeated denied push is performed. The expanded plan/report remain pending publication, and no product source changed.

### R-001 correction decision

On 2026-10-10 the human specified absolute `https://github.com/pchemguy/SDD-Manager/blob/main/<repository-path>` URLs for packaged README/AGENTS links to excluded docs, exemplified by the capability-map URL. The plan's CP-008 now applies this exact rule to all affected root occurrences; shipped-resource links remain relative. R-001 remains Open pending actual source repair and extracted-package/path verification. This records the selected correction method, not an implementation pass.

## Authorized planning publication

The human explicitly instructed: “publish campaign 037’s updated plan, report, and index to pchemguy/SDD-Manager”, 2026-10-10. Published the retained initial planning commit `80bc30018f205ce88e96cbbc10a6cc4d132ffe69`; exact remote branch readback matched before this next checkpoint. The earlier denial and pending-draft statements above describe their historical state, not the current publication result. This checkpoint contains the complete all-target plan, 25 intermediate commit checkpoints and explicit absolute blob/main root-link decision, plus its report/index navigation. Final commit/publication/readback is established by Git; source execution, test repository selection, finding closure, main integration and release effects remain outside this publication instruction.

## Execution source recheck — CP-011

The human authorized execution with the dedicated playground on 2026-10-10. [Revision evidence](REVISION-REPORT.md) retains separate CP-001–CP-011 actions and observations; earlier pending-planning statements above are historical. Current product recheck is `629d4cb7d6494fd49b9ac3c83a578ce4a9997409`, archive SHA-256 `b96c01003182d1e7e6f91a45b90e610b0c55525fd8a37e7da413481186a3defd`.

| Finding | Current disposition at this source pin |
| --- | --- |
| R-001 | Corrected: all 13 excluded-doc occurrences use accepted absolute current-main URLs; actual extracted-root targets and committed member bytes verified. |
| R-002 | Corrected: all 15 skills, canonical owner links and current preparation/tracking/revision/task/release boundaries reconciled; feature/campaign paths corrected. |
| R-003 | Locally corrected, Open for actual CI/provider recheck: strict source-associated curated notes and single manual publisher implemented; local contracts pass. |
| R-004 | Locally corrected, Open for actual CI/provider recheck: archive inspection, serialized reconciled draft/assets/publication and downloaded-byte/source/body/state/latest readback implemented. |
| R-005 | Open: full independent candidate-specific acceptance and supplementary facilities remain pending. |
| R-006 | Corrected: entry tracking/persistence, atomic task closure and integration audit appear in graph/key; all four diagrams actually rendered and visually inspected. |

Fresh publisher tests: 22 Passed. Fresh support suite: 113 Passed. Source-only checks do not establish live CI/release, consumer fidelity or installed-client acceptance. Production release readiness remains unestablished; no version bump or product release occurred.

## CP-013 provider observations and acceptance checkpoint

Source repairs remain at immutable plugin pin `ea515f5`; source report-only advancement does not change that tested package. Actual playground first run failed after creating an empty draft at immediate inventory readback. A later GET-only workflow-token probe finds the draft by list/exact ID, while tag lookup returns 404; its backend cause remains unresolved. Matching-draft recovery and a complete rerun Passed without recreating the release. Actual curated fixture body, tag source, published/prerelease/non-latest state, downloaded ZIP/checksum and all 133 member bytes were verified. Repeat release/asset IDs and timestamps are unchanged. Preserve the original Failed result and external restoration/diagnosis assistance; do not recast it as a clean first-pass release.

R-003 has actual fixture-body transfer/readback evidence, and R-004 has actual successful reconciliation, archive/readback and repeated-identity evidence. Both remain Open for the remaining selected provider fault/serialization observations and final source reconciliation. The retained fixture section is coordinator supplied; it does not certify real human-authored highlights preservation or editorial coverage. Full consumer R-005 remains Open: A-001 reaches published PROJECT/bootstrap with independent durable-state checks but waits for actual human review before ARCHITECTURE. Native transcript/isolation and installed/platform limits remain distinct. R-001/R-002/R-006 retain their CP-011 corrected source dispositions. See [revision report](REVISION-REPORT.md) for exact run, source, asset, publication and intervention evidence. No production release/readiness is claimed.

## CP-014 and delegated acceptance continuation

The user explicitly delegates all intermediate test-artifact assessment/acceptance to the coordinator. Exact separate preparation decisions through layout are published; TASKS/QC and full A-001 remain in progress, without direct-human review claims. Actual provider partial acknowledged-upload recovery, same-tag serialization, source/body/inventory refusals and preserved owned assets have been assessed. The fresh-create inventory-readback defect occurred twice and remains Open under R-004 pending repair and a clean first-run proof; provider internal cause is unknown. Original failures and assisted recoveries remain retained. See the [revision report](REVISION-REPORT.md) for exact identities and interventions. R-005/full consumer and supplementary acceptance remain Open.

## CP-014 repaired publisher disposition

Fresh first publication and complete rerun both Passed under separately pinned acknowledged-ID repair, with independent exact downloaded archive/checksum/member, body/tag/state/latest and repeated-identity checks. Original first-create failures and assisted recoveries remain Failed/assisted for their original tooling. R-003 and R-004 are corrected at current source publisher tooling; internal provider inventory visibility remains unexplained and is no longer a first-create dependency. R-005 remains Open for the full required campaign and selected supplements. Full A-001 preparation independently Passed under explicit coordinator delegation; main remains unmerged and no implementation/tracking is claimed. Exact identities/evidence are in the [revision report](REVISION-REPORT.md).

## CP-015 consumer acceptance recheck

Full preparation, selection-only and initial/repeated eligible-phase tracking independently Passed at unchanged prepared product `1e3305c8` with immutable package `ea515f5`. Actual preservation fixtures, hosted identities/associations and exact unmanaged material are verified in [revision evidence](REVISION-REPORT.md#cp-015--preparation-selection-and-hosted-activation-acceptance) and [published independent results](https://github.com/pchemguy/SDD-Manager-Prerelease-Playground/tree/65b6f802f16a66ff58e6d251c5cf77d24cda1f9e/docs/dev/reviews/001_eff696b-prerelease-acceptance). Original failures, coordinator recovery and platform-approval interventions remain retained. R-005 stays Open: five required variants Passed, remaining 27 required variants and selected supplemental/optional/native/installed/platform targets incomplete. No product implementation or readiness is inferred from P1 completion. R-001/R-002/R-006 retain corrected-source dispositions; R-003/R-004 retain corrected-publisher dispositions for their separately tested pins.

## R-007 — First-task assessor contract conflicts with required preparation integration

| Field | Evidence / disposition |
| --- | --- |
| Type / priority / confidence | Acceptance harness contract defect; P2; high confidence from actual fresh consumer and independent assessment. |
| Location | acceptance/textstats/cases/assessor/A-004.md and A-004.json require unchanged integration. Pinned startup-and-continuation.md requires accepted preparation merged/published before implementation branch creation. |
| Actual evidence | Main advanced only through document-only preparation merge `88a5c4b`; first task `9dc8075` stays on unmerged phase branch. Fifteen tests and independent probes Passed; literal original case Failed, consumer workflow Passed. |
| Bounded correction | State the allowed prerequisite preparation merge explicitly; retain incomplete-phase integration prohibition and exact before/after refs. Source guide and JSON changed together; immutable tested harness stays unchanged. |
| Recheck | Required support suite, guide/JSON alignment and separate newly pinned independent reassessment of actual retained lifecycle/source applicability. Original Failed result remains at its original pin. |
| Decision | Corrected at published assessor pin fc193b0; independently rechecked using eligible unchanged actual lifecycle evidence. Original assessor-pin Failed stays exact; reassessment-only corrected result Passed. Full readiness remains Open. |

## R-008 — Milestone assessor prematurely requires later failure-handling exits

| Field | Evidence / disposition |
| --- | --- |
| Type / priority / confidence | Acceptance harness scope defect; P2; high confidence from SCENARIO, accepted PLAN/TASKS and independent captures. |
| Location | A-005.json compares full baseline CLI including no-traceback file/decode failures at milestone1.1. SCENARIO assigns failure handling to milestone1.2; accepted PLAN maps R-008 there and T-003 explicitly defers complete diagnostics to T-005. |
| Actual result | API and success CLI captures Passed; missing/decode observations fail original premature criteria. Actual original captures and deterministic Failed retained; milestone code/review/hosted lifecycle independently assessed separately. |
| Bounded correction | Guide/JSON require accepted milestone scope, compare four fixed observed baseline success rows, retain complete captures/provenance and independent help/lifecycle checks. Full Phase1 failure requirements stay unchanged at A-006. |
| Recheck | Support suite, source alignment and separately pinned reassessment of exact actual retained evidence; original failed pin never relabeled. |
| Decision | Corrected at published assessor355e3d3; separate independent reassessment Passed with unchanged plugin/evidence applicability and explicit native historical RED/transcript/isolation limits. Original failedpin/result retained. Full readiness remains Open. |

## Current required acceptance disposition

Published original-pin totals are 23 Passed, 2 Failed and 7 unresolved. A019 controlled integration recovery independently Passed and published d2f8ebc with explicit local-delivery/intervention limits. Original A004/A005 failures and corrected rechecks remain distinct. A010 final feature reports are accepted; final lifecycle/reconciliation/archive/paused integration and independent grade remain pending. A021 sole accepted recovery checkpoint independently Passed; exact objects and assessment published ea9ab9d, with local-delivery limits retained. Stale-QC supplement Passed outside required totals; remaining follow-ups and strict-format/client/runtime limits are separately recorded. A014 new live refs remain automatically rejected without retry/bypass. Full readiness R-005 remains Open.
