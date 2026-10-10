# TextStats actual status — provisional ordinary-consumer report

## Reached state and boundary

This read-only report concerns actual TextStats delivery and the published prerelease observations. It does not authorize implementation, commits, pushes, hosted changes or release. Product reporting and integration are still underway; finalization is held until actual final records become available.

The first captured checkout was clean on `phase/2-json-and-stdin` at `ca24007134141265a1937c77e2fda504bb0d6129` (T-015). Local `main` and its cached origin tracking ref both pointed to `fbe8bedf4c6cba1ab29d53d2da05e614603d76d1`. Those cached refs alone are not live publication proof. The recorded actual consumer `git ls-remote --heads origin refs/heads/phase/2-json-and-stdin` returned exactly `ca24007134141265a1937c77e2fda504bb0d6129`; its prior push succeeded. No completed Phase 2/default integration was observed in this initial snapshot.

Canonical TASKS contains 24 stable identities: 21 active tasks, 19 checked active owners, pending T-016/T-017, and retired historical T-010–T-012. Earlier JSON and range reports describe historical delivery; JSON is now withdrawn. Current SPEC/PLAN/TASKS and AGENTS supersede their earlier stopping boundaries.

## Completed and pending work

| Extent | Actual initial state | Evidence |
| --- | --- | --- |
| Phase 1 | Delivered named-file counting, silent API, strict UTF-8, error handling, documentation and extracted source distribution | Governing owners, Phase 1 results and chronological campaign report |
| Named-file ranges T-018–T-024 | Delivered and previously integrated into paused Phase 2 | Recorded feature tip `6f161448` and two-parent paused merge `795f3a3542c9981f8d43c8e182876f3efa5b5f16` |
| JSON removal | Accepted amendment integrated into paused Phase 2 | `77e7106e3134cc7053a2b1a045cf1a76cf0361ea`; JSON identities retained as retired history |
| T-013 | Borrowed binary stdin reader delivered | `2d96774221165ac04096c8d57ddcefe85b2305e0`; complete decode, no borrowed stream closure |
| T-014 | Stdin CLI/count/BOM/range composition delivered | `dbf50d7b6d83c7ddf53f287d82b199db3e83fd89`; `-` is stdin and `./-` a named file |
| T-015 | Final public instructions and extracted stdin exits delivered | `ca24007134141265a1937c77e2fda504bb0d6129`; exact current public documents/archive checks |
| T-016/T-017 | Pending milestone/final review and report owners | Initial canonical unchecked owners; final report acceptance and hosted completion not yet observed |
| Completed Phase 2 integration | Pending at first observation | Actual target verification/publication remains distinct from checked task or closed issue |
| Version/release/next phase | Outside authorized boundary | No release readiness or release publication claim |

Current capabilities are exact text line/word output, strict complete UTF-8 acquisition, once-only leading-BOM policy, inclusive logical-line ranges and binary stdin. Whole-input public exports/signatures remain unchanged. Removed JSON options are usage errors before acquisition; a literal `--json` filename remains usable after `--`.

## Actual checks and publication evidence

I inspected retained actual command/result records; I did not execute product checks, rebuild its archive, or make provider requests. That distinction avoids mutating a checkout under active delivery. Product-owned source claims were compared with recorded command outcomes rather than relying solely on checkboxes or helper exit codes.

Initial `037-a013-consumer-observations.json` contains 223 command records plus child/provider observations. Records 186, 187 and 192 show successful product runner and independently discovered suites: 37 unit and 34 integration tests, nonempty, on Python 3.12.14. Record 195 reports an isolated extracted package import and 478 actual extracted module cases passed. Record 198 retains a corrected documentation campaign: twelve README/API fences, actual extraction demonstrations, exact success and failure outputs. T-015 evidence reports eleven archive members matching approved source bytes, silent import/API probes and successful cleanup verification.

The recorded T-015 publication was an actual successful push followed by exact remote tip readback (record 208). Recorded closure helper output (209) reports issue #16 closed/completed with exact comment readback and preserved native fields; corresponding provider records are retained. T-013/T-014 publication and issues #14/#15 are recorded separately. Hosted closure does not itself establish behavior or full-phase integration.

The final explicit child-flag claim belongs only to the corrected retry: 2,776 recorded Python children with `-B` and bytecode suppression. Earlier fifteen child argv gaps and earlier logger failures remain separate. Runtime support is specified as Python 3.11+, but this product delivery verification covers Python 3.12.14; it does not establish all supported runtime/platform combinations.

## Chronological campaign outcomes

Published result tables are reporting observations, not a substitute for actual product acceptance. Across all 34 entries (32 required plus two optional), the original table contains 27 Passed, two Failed, one Running, one Blocked, one Pending and two Not run. The corrected-rechecks table contains 29 Passed with the same remaining Running/Blocked/Pending/Not run entries. These are table-entry counts, not numerical reliability estimates.

Original A-004 and A-005 failures remain preserved. Their later Passed dispositions are separately pinned assessor scope rechecks using retained earlier behavior, not fresh consumer executions or retroactive original passes. A-013 is Running; A-014.cross-phase is Blocked with a recorded live publication barrier; A-027 is Pending. Optional A-023.live-response-loss and A-024.native-recovery are Not run. Controlled reconciliation/denial/rate-limit/access cases retain their controlled evidence class; they do not establish live or native facility coverage.

The diagnostic narrative is chronological and its last appended subtotal predates newer table dispositions. I retain its older subtotals as historical instead of silently treating them as a current summary. Full prerelease readiness remains open in those records.

## First outcomes, recovery and limits

- T-014 first collection failed because the trace harness lacked its execution import path. Subsequent genuine behavioral failures preceded implementation; setup failures are not behavioral RED.
- Concurrent logger writes caused an actual logging abort/race. Exact lost first-channel entries/counts are unavailable. The surviving snapshot is post-repair; corrected serialized observations support eventual checks without reconstructing missing originals.
- The first logger lock repair had an indentation error before product execution. Later lock/atomic replacement and immutable child capture are facility recovery, not proof of earlier behavior.
- The first documentation campaign reported success while five owned example inputs were subsequently still present. A guarded retry stopped before product execution; exact owned bytes/nonsymlink identity were checked, explicit cleanup followed, and a fresh successful retry confirmed absence. Helper success alone did not establish cleanup.
- Earlier publisher first-create failures, assisted recovery, retained original failures and separately repaired clean-run outcomes remain distinct. No new publisher change or plugin-pin change is proposed here.
- Native exhaustive transcripts, installed client discovery, Windows/session/native recovery and all supported runtime/platform coverage remain unavailable or unverified. Shared unrestricted filesystem access is a disclosed isolation limit; chmod snapshots are cooperative preservation, not cryptographic immutability against another actor.
- Some recovered/controlled trials are local-only publication. They are not live provider delivery proofs. Strict standalone package validation reported portability/manifest and sibling-resource containment differences; resolving local plugin links does not establish universal client portability.

## Current supplemental and source-only evidence

The later published `pre-reconciliation/supplement-current` register (supplied publication `d80a28c`, exact bytes snapshotted separately) selects current scoped results without erasing earlier trigger/held records. Its required accounting remains 27 original Passed/two original Failed/one Running/one Blocked/one Pending; corrected reassessments yield 29 Passed. Optional Not run remains two. Supplements remain outside those totals.

Current same-cycle QC recovery is a scoped Passed published continuation of the same retained owned commit, with no new commit or QC cycle inferred. Split-boundary evidence distinguishes consumer required behavior Passed from caller reconstructed product-history contract Failed. Reopening and tracking controls are LOCAL or bounded fixture evidence. Strict creator validation remains Failed (39 errors: four manifest/schema differences plus 35 shared sibling-resource containment errors); it is not a new product runtime defect or installed-client portability pass.

The register records source verification of `083c50ee12874484e2ce25620601dbce5c2d1af4`, published in evidence `09d8cb9`: 113 source support tests, 133 package-byte checks with no differences, canonical manifest equivalence and preservation of 16 frozen Git path/object/mode entries. These are source integrity/support results, not product/native/client/Windows acceptance. Later publisher records published in `131ed69` retain an actual root-run `python -B -m unittest discover -s .github/tests -v` at source `083c50ee12874484e2ce25620601dbce5c2d1af4`: Python 3.12.14, exit 0, raw stderr `Ran 26 tests`/`OK`, empty stdout. I inspected those raw records; this is not my independent test run or live provider acceptance. Source tip `fb2a06bb3f3ed5beeba03c045019d6c1f461de09` finishes CP019–022 assessment/disposition records only. Its build-only package record, published in `c24a16b46c22d2f83c7bba013e3c71fe21dfb7c6`, records 133 members all byte-equal to tested pin `ea515f5624c8a34cc4572731a2590223a5eb27f4`, version 0.15.0 and SHA-256 `935ad686d34caa953979a6d7de85152621c923a7bd43337b8238ecb1aabece6b`. No provider operations were performed for that build. Final source integration has not been supplied or inferred.

## Confidence, actions and bounded proposals

High confidence: actual local initial branch/HEAD/clean status and canonical pending owners, from direct reads and Git commands. Moderate-to-high confidence within retained records: current command outcomes and exact phase remote readback, backed by raw observations but not newly reexecuted here. Historical reported independent grades remain attributed to their sources and evidence classes; missing facilities remain missing.

No confirmed consumer instruction defect is established by this reporting inspection. It does not waive historical failed outcomes, classify platform barriers as plugin defects, or certify whole-package readiness. No product repair is proposed without a demonstrated current contract defect.

Actions taken: read ordinary input, applicable product instructions/pinned reporting resources and current governing owners; captured read-only local Git status; snapshotted authorized sources and actual observation records with SHA-256 provenance; drafted this separate report. No product mutation, commit, push, provider write or release action was performed.

Bounded next action: refresh this draft from actual accepted T-016/T-017 reports, exact task/publication/hosted records and completed-phase target merge verification when reached. Retain this initial state and each first/eventual outcome. Stop at published complete Phase 2, with no version bump or release. If actual final integration is blocked, report its last trusted state and precise barrier instead of inferring completion.

## Intermediate reached update — finalization held

After the initial snapshot, the coordinator supplied actual T-016 candidate independent/delegated acceptance published in `9338f067a575511b6d818a6898a458957f4670a8` (`runs/A-013/1/T016-gate/`) and local T-016 commit `b49a26b36d68dc9bab8cf83633f5b7a2aae81eea`. Its immediate publication and native closure readbacks are still in progress; this report does not infer either from local HEAD. The separately published cursor `19c3d45f1b46f86c5ab04a9dc6052d8aefaa00d1` updates reporting navigation while preserving earlier RESUME history. T-017's final report pair and completed-phase integration remain pending. This supplied intermediate observation preserves the initial pending state above and does not finalize delivery.

## Provenance

Read-only snapshots and actual Git argv/stdout/stderr/status records are in `037-a027-consumer-artifacts/initial-provenance.json`, `initial-command-*.json`, `initial-source-*`, `initial-a013-observations.json` and its provenance file. Initial instruction/source cats preceded snapshot creation; later snapshots are separate actual reads and are not represented as original command captures. Source hashes identify the bytes actually read during this provisional pass. This report uses no assessor guides, contracts, fault setup or closed source campaigns.
