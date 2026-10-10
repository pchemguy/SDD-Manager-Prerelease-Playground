# GitHub Release Workflow revision report

## Campaign and scope

- Campaign: `031_646af89`; [accepted plan](REVISION-PLAN.md).
- Starting source: `646af8924cd06aedcf8c7edb1937ba887e40eab6`.
- Published planning checkpoint: `31e8ea73b4ff5e527f64aaad292bdaf805d49167`.
- Working branch: `revision/031_646af89-github-release-workflow`; integration target: actual default `main`.
- The user commanded “Execute” after publishing the plan. Source implementation, checkpoint publication and the complete verified merge/publication are authorized. Product release/tag/dispatch writes are outside the requested execution boundary.
- State: V-001 through V-006 source implementation and verification complete; final explicit integration/publication proceeds after this complete report checkpoint. Final parent/check/push evidence is recorded in the merge commit, without a post-merge report-only commit.

## Implemented behavior

The GitHub backend now routes package assessment, interactive package/build-workflow preparation, workflow dispatch/monitoring, and release creation/recovery. Five focused references define packaging, workflow operations, release lifecycle, verification and reporting. Manager/forge entry points and current README/examples expose them without requiring TASKS or tracking activation for standalone release work.

Packages use version-free asset names and conventional suffixes for actual variants. Latest downloads require a complete advertised asset set. One publisher builds/uploads the verified source; direct release creation follows draft, complete uploads, verify, publish and readback, with bounded recovery for uncertain writes. Current token guidance adds Workflows read/write and distinguishes conditional Actions access and job GITHUB_TOKEN permissions. Both synchronized plugin manifests describe these capabilities and use source version `0.16.0`.

## Revision actions and actual evidence

| Action | Implemented result | Evidence and limits |
| --- | --- | --- |
| V-001 | Expanded forge/manager request triggers and operation handoffs; retained Git ownership and independent release/preparation boundaries. | Inspected both entry points, manager catalog and GitHub route table. No live consumer routing exercised. |
| V-002 | Added package contract, interactive continuation, safe archive assessment, source/output comparison, names/checksums and latest URLs. | Inspected github-packaging and workflow preparation guidance; the actual committed workflow package was built and checked below. |
| V-003 | Added workflow authoring/dispatch/monitoring and release identity/draft/upload/publish/recovery/readback procedures, with CLI/API recipes. | Checked operation semantics against current English GitHub/CLI documentation. No dispatch, tag or release API mutation performed. |
| V-004 | Added Workflows read/write in the backend profile; reconciled current README and acceptance SETUP; clarified conditional Actions and obsolete profile exclusions. | Current-source search and profile inspection agree. No existing PAT permissions were modified or asserted. |
| V-005 | Added release verification/reporting references, skill triggers and README/examples; synchronized metadata at 0.16.0. | Four skill validators pass; 126 current relative links/anchors pass; both manifests byte-identical; 113 support tests pass. |
| V-006 | Actual committed workflow package build, 16 source-scenario assessments and prior artifact preservation checked; complete report prepared before integration. | 128 package files match inventory and committed bytes; ZIP/checksum verified; 252 prior artifact path/object identities unchanged. Final merged checks/publication recorded in the explicit merge commit. |

## Local checks

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 113 tests, all passed. Test log retained temporarily at `/tmp/sdd031-support.log`; source was the pending implementation delta over planning commit `31e8ea7`.
- `quick_validate.py` for sdd-forge, sdd-manage, sdd-verify and sdd-report: all four valid.
- Current changed/new Markdown relative link and anchor inspection: 126 passed. Historical campaign targets were excluded; no historical contents loaded or validated.
- `git diff --check`: passed. Canonical/legacy manifest comparison: identical, version 0.16.0.

## Evidence boundaries

This is an instruction-source implementation. No executable product packaging/release code or test implementation changed; the existing support suite is a required boundary regression, not proof of release lifecycle behavior. The 16 source-scenario assessments below are distinct from actual package execution and do not certify consumer behavior. No fresh independent consumer, live CI, platform installer, credential-permission change, new tag/release or hosted asset download has been exercised. No release of SDD Manager itself is implied by updating source version metadata.

## Integration handoff

Publish coherent source/evidence on the campaign branch before dependent finalization. Verify the committed package and scenario coverage, finish current records/navigation, then explicitly merge the complete tip into refreshed main. Record exact parents, merged checks, target publication and remote containment in the merge commit; do not leave a final report commit outside integration. Prior closed campaign files remain untouched, checked by Git path/object identity only.

## Committed package execution

Source checkpoint `ef6bc94ce8deea8f9f61f8a3c11281cf46213c33` was committed and pushed to the campaign branch. The actual “Build package and checksum” run block from `.github/workflows/release.yml` was parsed and executed with Bash in a disposable local clone of that committed source. No publisher or hosted operation was executed.

The ZIP has 128 files. Every packaged file name and byte matches both the Git-object inventory selected by the acceptance helper's `PACKAGE_PATHS` and its committed contents. All five new package/workflow/release/verify/report references are included. ZIP integrity passes; the generated checksum matches the archive SHA-256 `4f084c72adc2471dd5c98bea6ca3d13caad7412479f3ed4c2194f0de4e424847`. No credential or campaign artifact is packaged. This verifies this source-package build, not target-platform installers, live CI or release uploads; no byte-reproducibility claim is made.

Git path/object comparison against the starting baseline preserves 252 prior review/feature/report artifacts unchanged, excluding the maintained global index. Their contents were neither loaded nor assessed for current compatibility.

## Source-scenario assessment

These are coordinator source assessments on `ef6bc94`, not isolated consumer runs, mock provider execution or live GitHub acceptance. No blocking source contradiction was found across the 16 planned cases.

| Planned case | Source behavior assessed | Evidence owner |
| --- | --- | --- |
| Simple source ZIP | Explicit inventory, source comparison, proportional workflow preparation. | github-packaging: Establish/Assess; github-release-workflows: Author. |
| Complex several-variant package | Material decisions resolved interactively and retained through continuation. | github-packaging: Establish; workflow matrix collection. |
| Credential/traversal/conflicting paths | Inspect before extraction, reject unsafe contents, never execute input scripts. | github-packaging: Assess. |
| Missing or generated member | Required/actual comparison and declared build origin; no tracked-only assumption. | github-packaging: Establish/Assess. |
| Versioned/colliding names | Version-free conventional suffixes and complete-set uniqueness. | github-packaging: Names and URLs. |
| Missing latest platform asset | No older-variant fallback or incomplete latest publication claim. | github-packaging: Names; github-releases: Read back. |
| Draft/prerelease | Explicit state, latest stable restriction, no fictitious alias. | github-releases: Draft/publish; package URLs. |
| Wrong tag/source/version | Exact SHA and peeled tag comparison; no implicit movement/default target. | github-releases: Resolve; workflow checkout. |
| Existing suitable workflow | Reuse/extend it, one publisher, actual trigger/input assessment. | github-release-workflows: Author. |
| GITHUB_TOKEN tag chain | Supported direct/dispatch path; no assumed downstream run. | github-release-workflows: token event rules. |
| Missing Workflows/Actions | Workflow editing and dispatch access are explicitly separate. | github.md: conventional profile and release/workflow access. |
| Partial build/upload | Collect all required outputs; retain matching draft, resume pending work. | github-release-workflows: matrix; github-releases: Draft/recovery. |
| Timeout after publication | Remote release lookup before replay, no duplicate creation. | github-releases: Recover. |
| Conflicting/published/immutable state | Preserve existing source/assets; bounded decision rather than clobber/delete/move. | github-releases: Resolve/Draft/Recover. |
| Workflow-only/local-only preparation | Preparation and publication are distinct; respect selected effects/stopping boundary. | manager Release operations; forge package/workflow entries. |
| Completed hosted release | Actual source/state/assets/latest/readback with metadata/download limits. | github-releases: Read back; release-checks; reporting releases. |

## Final boundary

All six accepted source actions are implemented. No runtime helper or product release workflow was changed, so no artificial implementation-mirroring tests were added. The required 113-test suite, four skill validators, current navigation checks, real source-package build and source-scenario assessment supply the stated evidence. Fresh consumer routing and actual hosted release/dispatch/download behavior remain unverified.

The complete report and current index are part of the campaign tip before the explicit merge. Refresh actual main, inspect divergence, merge that entire tip with two parents, verify the merged state and publish/read back main. Existing releases, tags, PAT permissions, repository settings and the minimal greenfield prompt remain outside this campaign's mutations. No further project feature or release execution follows this boundary.
