# Dedicated scoped authorization policy revision

Campaign: `012_21cba43`. Full starting baseline: `21cba43132d2211d1a7e788bbc7d9cdb1fab2ae7`.
Repository: `pchemguy/Skill-SDD-Manager`, established remote `https://github.com/pchemguy/Skill-SDD-Manager.git`.
Working branch: `revision/012_21cba43-scoped-authorization`; target: `feature/architecture-revision`.
Objective: implement the human-requested dedicated sdd-manage authorization policy, authorizing scoped revision pushes and verified review-branch merging, and supplying authorization context after platform rejection rather than asserting an override.

## Changes and verification

- Added `skills/sdd-manage/references/revision-authorization.md`: authorized review-record/source-revision persistence and completed-branch integration, explicit human limits, rejection response and authorization evidence fields.
- Coordinator entry, review/revision coordination and Git workflows now route to that file. Replaced the earlier active override wording; campaign 010 policy links to the resulting authority, with historical revision evidence preserved.
- Review records and implementation repairs remain distinct scopes. Platform review is preserved, repeated unchanged denied requests and evasion are prohibited, and credential recovery is distinguished from approval rejection.
- Verification: focused source/Markdown local-link, coordinator YAML frontmatter, routing and whitespace checks. No runtime/provider lifecycle test or installed-client approval behavior is claimed from policy text.

## Persistence

Current result: revision branch and verified target integration published following the human command “Push and integrate.” The earlier rejected attempt and its context below are retained as history.

Source amendment committed as `67e1794bdbc217d05ebddfca7fda21cd49e2c64f`. The push request supplied the human objective, observed Git destination, exact commit/eight changed files, verification and review-branch/target context. Platform automatic approval review rejected publication, stating that the policy-creation request did not explicitly authorize publishing this new commit to GitHub and that the destination/content required explicit authorization. Read-only remote lookup confirmed that the new branch is absent. At that checkpoint, push and integration remained pending; the denied write was not repeated or bypassed. Existing unrelated workspace material is preserved.

### Scoped authorization retained from the rejected attempt

- Human request: add the dedicated sdd-manage authorization policy, authorizing revision pushes and verified review-branch integration, and supply scoped authorization after platform rejection.
- Policy: `skills/sdd-manage/references/revision-authorization.md`, applied with that actual request rather than as an exemption.
- Requested publication: current revision commits to `pchemguy/Skill-SDD-Manager`, branch `revision/012_21cba43-scoped-authorization`; established target `feature/architecture-revision` at baseline `21cba43132d2211d1a7e788bbc7d9cdb1fab2ae7`.
- Scope/evidence: the dedicated policy, three coordinator routing/protocol files, retained campaign 010 policy/plan links, campaign 012 report and campaign index; local links/frontmatter/whitespace checks passed.
- Platform requirement at that checkpoint: explicit authorization to publish this revision branch and complete verified target integration. The policy file alone did not establish platform approval; the source commit was preserved pending that specific authorization.

## Remaining work

This amendment does not implement campaign 011's planned document-QC workflow changes or run TextStats live acceptance. Those retain their existing state. No source issue is deferred within this focused authorization amendment.

## Verified integration — 2026-10-04

Revision branch tip `7ba1204ed5ca2c67f3bd2002ca153f0a3bb35d74` was pushed and exact remote readback matched. Explicit merge `09bb4dabfad7557580226a99bdfbf0d2be76be22` integrated it into `feature/architecture-revision`, with target parent `21cba43132d2211d1a7e788bbc7d9cdb1fab2ae7`. Prospective checks covered 14 documents and 70 local links, coordinator YAML frontmatter, exact merged policy/source equivalence and staged whitespace; no conflicts. Target push succeeded and exact remote readback matched the merge SHA. The successful operations followed the direct human publication/integration command; they do not prove that policy context alone changes platform approval behavior.
