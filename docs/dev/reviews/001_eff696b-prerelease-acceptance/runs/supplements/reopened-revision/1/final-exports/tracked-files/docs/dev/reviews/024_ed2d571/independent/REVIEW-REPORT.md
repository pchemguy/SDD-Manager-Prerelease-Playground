# Independent pre-release assessment

Reviewer: fresh agent `/root/prerelease_independent`, supplied only bounded task/source context. Reviewed exact source ed2d571d20aa8ad6ee77f25ad89602e82e6a653b (0.14.6), 2026-10-06. This retained assessment is transcribed from the reviewer's returned assessment by the coordinator; no independent file-writing/commit claim is made.

## Findings

1. **Independent-01 / canonical R-001 — P2.** contract_probe.py lines 26–33 imports private textstats.core instead of required public textstats.count_text. A correct package-only implementation returns Unavailable; a broken public export with a correct private function returns Passed with two tests. A-017 requires baseline probe success before any alternative injection, and A-026 uses the same baseline fixture. Import the public package and validate its origin; separate implementation-specific injection selection from general API assessment. Recheck valid package-only layout, wrong public export with correct private implementation, and genuine injected assertion failure with zero setup errors.
2. **Independent-02 / canonical R-002 — P3.** trial_control.py lines 79–82 resolves receipt before is_symlink, making its guard ineffective. A dangling caller receipt link creates the referent and completes. Validate lexical receipt before resolution in fresh/resume paths; recheck dangling/occupied links, normal creation and held continuation. Caller-controlled helper; no independent exploitation or product corruption was shown.

Both findings high confidence and independently reproduced in disposable fixtures; no source repair was performed.

## Actual checks

Full support discovery: 107 tests passed in 47.534 seconds. Static catalog validator: 27 cases validated. No hosted writes, clones, /pyenv access or source changes. Package/source paths remain identical to baseline despite coordinator report-only commits.

## No-finding coverage

All 15 skill entries and consequential orientation/coordinator/QC/Git handoffs inspected. No confirmed contradiction in push-first startup, range counts, incomplete phase pause, completed phase integration, unrelated index preservation, feature ownership transfer/archive, reassessment, steering stop, reviewer versus coordinator publication or platform denial versus existing authority. GitHub projection/issue/milestone instructions distinguish local acceptance, publication, retirement, hosted closure, unknown writes and dependencies.

Harness configuration/pinning, Git observation, recovery export, deterministic assessment, capture, catalog rendering, coverage accounting, controlled fault adapter and evidence merge inspected. All 27 assessor guides, dependencies and classifications reviewed. Existing tests miss the two confirmed boundary scenarios.

## Limits

No fresh consumer workflow or live acceptance campaign, installed-client discovery/routing/activation, native termination, protected credential recovery or live GitHub verification. Historical 0.14.3 grades are not current-source evidence. Intentional Codex metadata exact-copy design is not counted as a portable-format defect.

## Independently corroborated documentation follow-up

After the coordinator supplied two located candidates, this reviewer independently checked them against the same baseline. Both are P3, high-confidence defects with limited release impact. These follow-up checks were candidate-directed, distinct from the fresh initial review.

- **Canonical R-003:** core.package returns 114 files but omits root notices named by README line 9, despite including their asset templates. Include root notices or redirect to included assets; bootstrap templates remain usable. Recheck committed snapshot local navigation and notice dependencies. Source-only acceptance/development URLs are optional improvement, not another required defect.
- **Canonical R-004:** docs/dev/reviews/README.md omits completed 020 and has blank lines before 021–023 that terminate its GFM table. Add truthful 020 row and remove row gaps; recheck one rendered campaign table and resolving links while retaining historical identities.
