# Remove the standalone authorization policy

Campaign `028_5e2624e` starts at `5e2624e625e33410245cb3b51b1b31120ad18747`. Working branch: `revision/028_5e2624e-remove-authorization-policy`; target: `main`. The user requested a revision campaign to remove the redundant standalone policy. This directly accepted amendment includes execution, verification, normal checkpoint publication and explicit integration.

## Accepted scope

Delete `skills/sdd-manage/references/revision-authorization.md`, remove its active navigation/dependencies, and retain only concise practical guidance in existing owners: carry request scope through coordination, distinguish credentials from policy failures, retain blocked work and report actual effects through Git recovery. Do not rename the file, recreate an equivalent policy elsewhere, restore campaign 027, or change project-preparation/integration gates, optional tracking decisions, credential protection or host controls. Historical campaign observations and source inventories remain evidence of their recorded baselines.

| Action | Outcome | Verification |
| --- | --- | --- |
| V-001 | Remove the file and reconcile manager, forge, implementation, preparation, coordination, credentials, Git, review workflow, README and root AGENTS navigation. | No active reference to the removed file or separate authorization-policy prerequisite; practical recovery/handoff guidance has existing owners; actual Markdown links/anchors resolve; manifests remain identical; support suite passes. |

Publish this plan on the revision branch before source work. Implement the coherent action with its revision results, verify/commit/push, then explicitly merge the complete published tip into main, verify the merged result and push main. Record final merge/publication through Git and the completion response without adding an unmerged post-completion report commit. Stop after this campaign.
