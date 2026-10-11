# Tracking-fidelity revision report

## Campaign and execution

- Campaign: `038_d6218f1`; [accepted plan](REVISION-PLAN.md), [baseline review](REVIEW-REPORT.md).
- Human execution instruction: “Execute campaign”, 2026-10-10.
- Working branch: `revision/038_d6218f1-tracking-fidelity`; target: suspended `revision/037_a6c42dd-prerelease-review`. Main is outside this integration boundary.
- State: All three accepted source/scenario-preparation actions complete and locally verified. Integration is into the suspended parent branch only; the final two-parent merge and target publication are recorded in Git. Behavioral fidelity is not certified.

## Action evidence

| Action / findings | Changes and verification | Disposition / publication |
| --- | --- | --- |
| V-001 / R-001 | Explicit request is first in the tracking decision table; requested/confirmed choice is separate from projection. Manager dispatch, executor direct/resume readiness, coordination and workflow entry now explicitly load/apply the gate. Phase activation requires every eligible phase object and initial association before task edits/tests; pending/unknown projection blocks execution. Added broad-request example. Changed links and policy handoffs inspected; no repeated activation approval, no new registry and existing human/preparation gates preserved. | R-001 Revised; behavioral recheck pending. Commit `753e45a9852c4b822b6004315bf559287b4381c5`; pushed/readback matched before V-002. |
| V-002 / R-002 | Startup/completion allowances now require already verified phase/task projection and satisfied dependencies. Shared lifecycle, phase/workflow and forge entry preserve that boundary. Omission recovery distinguishes the original requested gate from genuinely late confirmation, retains files/index/commits and matched objects, and stops further affected execution until missing prerequisites are reconciled. Added initial-projection/outage/omission examples. Owner comparisons and changed-link inspection preserve closure, added-work, no-reset and no-future-phase gates. | R-002 Revised; behavioral recheck pending. Commit `36a5f8a651546a375e57e4edf1d38e2d86bb6ff5`; pushed/readback matched before V-003. |
| V-003 / R-001–R-003 | Added assessor-only TRACKING-FIDELITY.md and an ordinary broad consumer request template; linked from existing A-003/COMMON owners. Nine selected follow-ups define actual observations, direct entry, initial/partial/unknown projection, token-only/decline, activated outage, added work, genuine omission recovery and next phase. Stable 27-case/default-required coverage is unchanged. Scenario preparation is delivered; no dedicated destination, original test source/trace or isolated comparative run is supplied. | R-001/R-002 Revised; R-003 Open. Behavioral follow-ups Not run; no invented pass/deferral. |

## Executed checks and completion boundary

- Source checkpoint: V-001/V-002 at `36a5f8a651546a375e57e4edf1d38e2d86bb6ff5`, plus the V-003 scenario/report changes in this publication checkpoint. Commit identity is discoverable from Git; no self-referential commit SHA is claimed.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 113 tests passed in 15.903 seconds.
- `PYTHONDONTWRITEBYTECODE=1 python acceptance/textstats/cases/assessor/catalog_tools.py validate`: static assets valid, 27 catalog cases, live acceptance false.
- Changed Markdown/link and policy handoffs inspected, manifest copies identical, full campaign path diff confined to current source, selected acceptance documents, campaign 038 and the review index. Suspended 037 records and closed campaigns preserved.
- Completion covers accepted wording revision, scenario preparation and local integration checks. Comparative consumer/provider execution is Not run: no dedicated authorized destination or isolated execution facility has been established. This is an unavailable check, not an accepted human deferral or a Verified finding. R-001/R-002 remain Revised; R-003 remains Open.
- Prospective merged-state checks, both parent identities, final merge commit and remote publication/containment are retained in Git integration evidence. Parent campaign 037 stays suspended; its review candidate must be re-pinned and affected units reassessed when separately resumed.

## Evidence limits

No fresh consumer comparison, installed-client behavior or live provider mutation has occurred. R-003 remains an evidence gap: supplied test source/trace is unknown and no dedicated consumer target is selected. Source inspection is evidence of the wording change, not proof of improved LLM compliance. Preserve original review observations and suspended campaign 037 candidate/findings.
