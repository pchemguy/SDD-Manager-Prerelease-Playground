# Pre-release review report

Campaign **024_ed2d571**, source **ed2d571d20aa8ad6ee77f25ad89602e82e6a653b**, version **0.14.6**, 2026-10-06. See [review plan](REVIEW-PLAN.md).

**Current repair disposition:** user authorized R-001–R-004 and excluded live testing. All four are verified on 0.14.7 source e33949aded51c55013d2de6318e0564127a13d3d; see [revision report](REVISION-REPORT.md). R-005 remains an unexecuted evidence gap outside scope. The original 0.14.6 observations and readiness assessment below remain historical baseline evidence.

State: **comprehensive source/local pre-release review complete; hold an unqualified acceptance-certified release**. Four confirmed defects (one Important, three Minor) and one separate release-evidence gap are open as proposals. Fix R-001 before relying on required live failure-trial acceptance. No confirmed workflow-policy defect was found. Report-only branch `revision/024_ed2d571-pre-release-review`; source target `feature/architecture-revision`. Tracked source was clean at orientation; unrelated untracked work is preserved. Remote main and source target both named the reviewed baseline at orientation.

| Unit | State | Evidence |
| --- | --- | --- |
| U-001 Package | Assessed; no confirmed release blocker | [Package checks](package-checks.json), [navigation/presentation checks](navigation-checks.json); 15/15 skill validators pass; 16 SVGs parse; metadata copies match |
| U-002 Skills/workflows | Assessed; no confirmed workflow-policy defect | All 15 entrypoints and consequential handoffs inspected; scenario matrix below |
| U-003 Harness | Assessed; two confirmed defects | 107 support tests Passed; 27 static catalog cases validated; independent and coordinator reproductions |
| U-004 Documentation/consolidation | Assessed; two minor documentation defects and release evidence gap | Package navigation, campaign index, historical hashes, four diagrams and independently reconciled findings |

No source repair, new live campaign or installed-client activation has been performed.

## U-001 evidence and boundaries

Agent-package-author offline validators ran with Python 3.12.14. All 15 skill entries satisfy its structural rules; names/descriptions and matching directory identities pass. All 15 OpenAI presentation files name their skill in the default prompt and resolve both local icons. Root and nested SVGs parse as XML (16). Root MIT license and the third-party TDD notice/provenance are present. Root manifest and Codex manifest match byte-for-byte at version 0.14.6; PNG/SVG presentation paths exist.

The strict portable-plugin validator exits 1: canonical Agent Plugins schema is absent and skills/hooks/interface are nonportable root keys. This is an expected target distinction, not a repair request: the user requested an exact Codex metadata copy and README explicitly disclaims portable conformance. No portable/Gemini/Antigravity installation is certified.

Navigation scan inspects 149 current Markdown files and 293 local link tokens. Its two unresolved tokens in repository-bootstrap.md occur inside a literal target-README example; they are not links intended to resolve from the policy directory. No actual missing current source navigation link was found. Anchor rendering and installed-client UI are outside this mechanical check. The README Getting started sentence means no root *conforming Agent Plugins 1.0* manifest; the later section accurately describes the existing Codex copy. Wording can be clearer, but presence alone is not a contradictory conformance claim.

Checkpoint history is retained in Git on this review branch; coordinating publication uses ordinary pushes with exact remote ref readback. No source files were changed.

## U-002 cross-skill coverage

Evidence is instruction/source inspection, not a fresh consumer execution or a certification that agents will follow the instructions.

| Concern / skills | Positive path inspected | Negative / interrupted boundary inspected | Result |
| --- | --- | --- | --- |
| Orientation / manage / conventions | Eligible repository, accepted scope and current state handoff | No Git, ambiguous owner, pending merge or unrelated index work | Mutation prerequisites and preservation explicitly assigned |
| Design / specify / plan / tasks | Accepted design → SPEC QC → PLAN/layout QC → TASKS QC | Stale Ready, changed upstream, missing decision or forbidden adjacent report path | Dependent progression blocked; routine status alone does not invalidate equivalent review |
| Implement / tdd / docs / verify / report | Task acceptance, tests, documentation, read-only boundary review, coherent commit and push | Failing required check, completed work awaiting persistence, missing test-first history, unpushed commit | Repair/persistence remains with execution owner; valid existing work retained |
| Range / phase coordination | Precise next-N units, explicit review tasks, sequential completed phase integration | Cross-list next ambiguity, out-of-range prerequisite, partial phase or unclosed predecessor | No guessed expansion, skipped review task or partial main-phase merge permitted |
| Integrate-feature | Selected accepted delta; both lists for task transfer; archival of eligible sources and QC pairs | SPEC-only selection, duplicate owner, stale checked claim, interrupted archive or active references | Unique task ownership, scoped reassessment and source retention explicit |
| Steer | Commanded amendment, changed contracts/tests/docs, merge into paused target | Assessment-only request, scope reduction invalidates status, blocked merge/publication | Amendment owns persistence; always returns control without automatic task resumption |
| Forge / backend lifecycle | Eligible phase projected fully; task issue then milestone closure; independent code review/testing | Partial projection, unknown write, duplicate managed identity, foreign issue, rate limit | Readback/reconciliation required; optional hosting distinct from local implementation |
| Authorization / credentials | Existing human scope carried through prescribed normal publication | Missing scope versus host denial, access failure versus provider limit/policy | Mandatory authorization policy read; token is access capability; no bypass or duplicate plugin approval gate |

Shared policies and stage owners agree on concern ownership, the final single-task phase review milestone, per-task persistence, affected preparation reassessment and feature-versus-main parent completion. No concrete contradictory execution instruction was confirmed in these inspected handoffs. This outcome does not waive live consumer evidence or independent harness findings.

## U-003 harness execution and findings

Command: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`. Actual result: **107 tests passed in 41.863 seconds**, Python **3.12.14**. See [complete output](support-suite.txt). Independent reviewer separately observed 107 Passed in 47.534 seconds; tests ran concurrently, so duration is environment-specific. No 3.11 execution is claimed.

Static catalog command: `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`; [result](catalog-validation.json) confirms 27 cases and does not certify runtime acceptance. [Variant accounting](variant-accounting-check.json) retains missing grades as required Blocked or optional Not run and readiness false; this is a synthetic accounting check, not a current live campaign result.

Reviewed helper boundaries include committed/dirty package hashing, schema and checkpoint validation, local-only remote avoidance, deterministic-versus-agent assessment, unique task ownership, isolated consumer rendering, protected exports, held state drift, uncertainty retention, controlled ledger response loss and read-only evidence merge verification. Support tests exercise those local checks; they do not establish consumer decisions or native/live provider behavior. Source/support outcomes are distinct from legacy 20 Passed / seven Blocked.

### R-001 — Required count probe assesses the private implementation instead of the public API

- Type/severity/confidence/disposition: **Defect / Important (P2) / High / Open, proposed repair**.
- Location: `acceptance/textstats/scripts/contract_probe.py` lines 26–33 and implementation-specific injector at 61–67; public contract in SCENARIO.md Counting and API and cases/consumer/preparation.md; required use in cases/assessor/A-017.md and A-026.md.
- Observed: fresh isolated public-only package with correct literal counting and no core module returns Unavailable with zero tests/ImportError. A public count_text returning (99,99) plus correct private core.count_text returns Passed, two tests, no assertion failure. Both independent reviewer and coordinator reproduced this; see [observations](defect-reproductions.json).
- Consequence: valid consumer layouts can be blocked by harness setup, and broken required public exports can supply a false baseline. This obstructs reliable required A-017/A-026 trial setup. No new actual consumer case is labelled failed from these reproductions.
- Proposed correction: probe `textstats.count_text` through the contracted public package, verifying its actual import origin. Separate injection's supported layout from the public baseline check; permit explicitly documented equivalent isolated regression setup for other valid layouts. No production TextStats amendment is indicated.
- Objective recheck: package-only valid implementation passes; wrong public export fails despite correct private core; missing/wrong import remains setup Unavailable; disclosed injected count regression yields nonzero assertions with zero setup errors. Add boundary tests independent of production results, then run relevant/full support checks.

### R-002 — Receipt resolution defeats the symlink guard

- Type/severity/confidence/disposition: **Defect / Minor (P3) / High / Open, proposed repair**.
- Location: `acceptance/textstats/scripts/trial_control.py` lines 79–82, save at 93–98.
- Observed: Path(receipt).resolve() occurs before is_symlink(). A dangling receipt link into a different temporary directory runs a harmless manifest, returns Completed, creates the target JSON and preserves the lexical symlink. Independently reproduced twice; see defect-reproductions.json.
- Consequence: the stated path rejection does not hold and evidence can be created/updated at the referent. This caller-controlled helper reproduction does not demonstrate malicious exploitation or product corruption.
- Proposed correction: validate the original lexical receipt before canonicalization for fresh and resumed execution, retaining watched-file overlap and occupied-path checks; define/recheck parent symlink handling consistently with the supported path policy.
- Objective recheck: dangling and occupied receipt symlinks rejected without referent mutation; ordinary new receipt and held continuation work; existing drift/failed/unknown receipt non-replay tests still pass.

Fresh independent assessment is retained at [independent/REVIEW-REPORT.md](independent/REVIEW-REPORT.md). Independent-01 maps to R-001 and Independent-02 to R-002; these are two canonical defects, not duplicate findings.

## U-004 documentation and release evidence

The full current source scan found no actual missing local file navigation links (293 tokens across 149 Markdown files, excluding code blocks). Checking the *shipped snapshot* separately revealed R-003. [Package navigation](package-navigation.json) records all 45 root README local link occurrences: 32 resolve within the 114-file snapshot; 13 do not. Eleven missing occurrences concern acceptance/development material explicitly identified as source-only; those are a navigation improvement opportunity, not additional defects. The other two are the notices in R-003. Snapshot fingerprint **60840f4b62aa5566d1d25fe11f6e035ac9fd20c2e4a368ecf5868a024be459d1** matches campaign 023's retained package validation.

[Release evidence checks](release-evidence-checks.json) independently recomputed all nine imported campaign 021 file hashes; all match retained import provenance. Historical diagnostic grades remain **20 Passed / seven Blocked for 0.14.3**, not results for 0.14.6. Older campaign 008 explicitly records its own assisted-source evidence and limits; no historical pass is promoted to current acceptance. Four README Mermaid blocks were inspected for workflow semantics and source syntax. No rendered preview or installed UI validation is claimed.

TextStats README's full-run prompt and AGENTS reading/role/scope protocol agree: explicit dedicated destination, existing authentication first, fresh consumer and assessor isolation, preserved real interruption state, pinned-source immutability, separate assistance, required versus optional classification, and final evidence-only integration into test main unless an explicit earlier boundary applies. No automatic run on a previous repository is implied by this review.

### R-003 — Packaged README links to notices omitted from its snapshot

- Type/severity/confidence/disposition: **Defect / Minor (P3) / High / Open, proposed repair**.
- Location: README.md line 9 and package section lines 43–45; acceptance/textstats/scripts/core.py PACKAGE_PATHS at line 24.
- Observed: committed snapshot includes README and assets/SDD-MANAGER.md plus assets/AI_DISCLOSURE.md, but excludes the two root notices named by README's usage/disclosure links. Independent reviewer corroborated this against the baseline after coordinator observation.
- Consequence: two user-facing local links fail in the pinned package. Bootstrap templates remain available, so no bootstrap implementation blocker is demonstrated. Ordinary whole-repository checkout links work.
- Proposed correction: include the two existing root notices in the package selection, preserving byte/hash provenance, or redirect to the included assets after checking their relative links. Prefer including root notices to preserve existing source README navigation. Source-only links may separately use repository URLs; do not pull assessor material into consumer packages to repair navigation.
- Objective recheck: enumerate the real committed snapshot; resolve both README notice links and their own dependent local links within it; retain dirty/committed fingerprint tests and consumer assessor isolation.

### R-004 — Campaign navigation omits 020 and interrupts its table

- Type/severity/confidence/disposition: **Defect / Minor (P3) / High / Open, proposed repair**.
- Location: docs/dev/reviews/README.md lines 25–31.
- Observed: 020_019eb35/REVISION-REPORT.md exists but no 020 index row exists. Blank lines before 021, 022 and 023 terminate the preceding GFM table; these standalone rows lack a header/separator. Independent reviewer corroborated both facts. This is source inspection, not a claimed rendered preview.
- Consequence: a completed authorization/publication campaign is absent from sequential navigation, and newer rows render as pipe-delimited paragraphs. Original records and their direct links remain intact.
- Proposed correction: add the truthful 020 entry and keep the index rows contiguous. Add this campaign's navigation entry when integrating accepted documentation work; preserve existing identities and evidence.
- Objective recheck: GFM rendering yields a single campaign table; baseline campaigns 001–023 each appear once with resolving record links, followed by any subsequently accepted campaign entries.

### R-005 — Current release has no fresh live or installed-client acceptance evidence

- Type/severity/confidence/disposition: **Evidence gap / Important for an acceptance-certified release / High / Open, follow-up scope required**. This is not a confirmed plugin defect or a failed live case.
- Location: README.md Testing with TextStats and Package status; campaign 021/023 revision limits; source pin and results in imported diagnostic/provenance.
- Observed: local support checks and structural validation cover 0.14.6. Retained completed live diagnostic tested 0.14.3; campaign 021 changed authorization instructions and harness, and 023 changed discovery metadata/package contents. Installed-client discovery/routing/activation remains untested. No fresh consumer run was selected or performed here.
- Consequence: unconditional current-version live or installed-client readiness cannot be substantiated. The reviewed source can be distributed as a clearly qualified pre-release candidate, subject to known defects, but current support passes alone cannot certify the advertised agent behavior.
- Proposed follow-up: after R-001 correction and package repin, execute the supported required live scope on an explicitly identified dedicated repository using fresh consumers and independent assessors. Validate actual supported-client discovery, routing and presentation for any client advertised as tested. Preserve original attempts, interventions and literal/Git/hosted evidence; integrate final test evidence as prescribed. A full current scope contains **32 required variants across 27 cases**, not a retrospective split of historical case grades.
- Objective recheck: publish newly pinned current-source grades with independently assessed required coverage and exact publication/integration evidence, plus a separately identified installed-client observation if claiming client readiness. Optional A-023 live-response-loss and A-024 native-recovery remain separately Not run/non-blocking without their facilities; cooperative controls never become native evidence. Their absence alone does not gate ordinary required acceptance.

## Canonical findings and readiness

| ID | Type | Severity / priority | Disposition | Release consequence |
| --- | --- | --- | --- | --- |
| R-001 | Harness defect | Important / first repair | Open proposal | Required failure-trial baseline is unreliable |
| R-002 | Harness defect | Minor / subsequent repair | Open proposal | Receipt path rejection is ineffective |
| R-003 | Package documentation defect | Minor / subsequent repair | Open proposal | Two notice links fail in pinned package |
| R-004 | Source documentation defect | Minor / subsequent repair | Open proposal | Missing campaign navigation and broken table |
| R-005 | Evidence gap | Important for certified release / after repairs | Open follow-up | No new-source live or installed-client certification |

**Counts: four confirmed defects, one evidence gap; zero repairs implemented by this review.** No Critical finding and no confirmed contradiction in inspected workflow policies. All four planned review units are assessed; assessed does not mean findings resolved.

| Readiness boundary | Supported conclusion |
| --- | --- |
| Skill structure and local support checks | 15/15 validators, 16 XML SVGs, matching manifests and 107 support tests pass; 27 catalog cases validate |
| Harness for required acceptance | Hold reliance on A-017/A-026 baseline until R-001 is repaired/rechecked; support suite misses the reproduced public-API boundaries |
| Explicit-source agent behavior on 0.14.6 | Not certified by this review; fresh required consumer assessment remains pending |
| Installed ChatGPT/Codex discovery/routing/presentation | Not certified; need actual target-client observations |
| Generic Agent Plugins 1.0 / Gemini / Antigravity portability | Not a declared verified target; intentional Codex metadata copy is not portable conformance |
| Optional complex live/native recovery | Non-blocking omissions when unavailable; full execution needs isolated hosted post-send suppression/readback or protected native access/recovery facilities respectively |

## Proposed revision order and stopping point

1. Repair R-001's public API boundary and independent regression tests before starting a new acceptance campaign. Update injection/guide layout assumptions together.
2. Repair R-002's lexical path validation and regression checks. R-003 and R-004 documentation/package corrections can proceed independently; package changes require synchronized source provenance and appropriate checks.
3. Run focused regression then the full support suite on the accepted repairs; structurally validate and repin the resulting package. A separately accepted revision campaign should retain original findings and use its normal verified merge/publication boundary.
4. Close R-005 through explicitly selected current-source required live acceptance and target-client smoke evidence. Keep unavailable complex optional extensions non-blocking and disclose Python 3.11 and rendered Mermaid coverage separately if still unexecuted.

These are bounded proposals, not accepted source amendments or an executed REVISION-PLAN. Review-only evidence remains on revision/024_ed2d571-pre-release-review; no source merge or installed package update was performed. The coordinating workflow publishes the final report normally and verifies the exact remote ref after its commit.

## Published checkpoints and evidence limits

| Boundary | Commit | Publication evidence |
| --- | --- | --- |
| Plan | 82ad0ceb998f0aa5ce6d16b0278e15c368f524b4 | Normal push; exact remote review ref read back |
| U-001 | fbe66f0197f2dfc8d9091ca835dd91dabb7f68d3 | Normal push; exact remote review ref read back before dependent assessment |
| U-002 | af97b69ad348629cf25461fedac36f2bdd45df20 | Normal push; exact remote review ref read back |
| U-003 | c1c7d882af734bc4d6cc8c2baf3b2a4cfc6c83cc | Normal push; exact remote review ref read back |
| U-004 / final report | This report's final Git commit | Coordinator performs normal push and exact ref verification after the report commit; report does not embed its own SHA |

Source inspection, mechanical structure/navigation checks, actual local support execution and independently reproduced isolated faults are the achieved evidence classes. No fresh live campaign, installed-client activation, native kill, protected credential recovery, live response-loss or authorization-setting behavior was exercised. Python 3.12.14 was observed; no Python 3.11 execution. No Mermaid/GFM rendered preview was available. None of these limitations is silently relabelled as a source defect or consumer failure.

Primary standards consulted for format distinctions: [Agent Skills specification](https://agentskills.io/specification) and [Agent Plugins 1.0 specification](https://agent-plugins.org/specification), accessed 2026-10-06. Local validators enforce their own documented strict authoring policy. Their success/failure is structural evidence, not client installation evidence.

## Revision 1 — Accepted four-defect repair recheck

| Finding | Current disposition | Recheck |
| --- | --- | --- |
| R-001 | Verified on 0.14.7 | Public-only/broken-public/private-correct tests and genuine injected assertions; outside import rejected |
| R-002 | Verified on 0.14.7 | Lexical/parent symlink rejection before effects on fresh/resume; hold/resume/nonreplay retained |
| R-003 | Verified on 0.14.7 | Actual 116-file package notice navigation and dirty fingerprint changes |
| R-004 | Verified on 0.14.7 | One contiguous unique 001–024 campaign table and resolving links |
| R-005 | Open evidence gap; explicitly outside current scope | No live or installed-client test executed |

Full support suite: 112 Passed. Fresh independent repair review reports no remaining scoped issue. Original observations, four-defect baseline count and source identities are retained; no historical live grades are rewritten. Revision integration/publication state is recorded in the companion report.
