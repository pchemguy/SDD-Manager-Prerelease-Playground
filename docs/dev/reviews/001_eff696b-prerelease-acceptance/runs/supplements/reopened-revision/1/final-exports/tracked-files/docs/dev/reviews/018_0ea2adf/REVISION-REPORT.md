# Repository disclosure revision report

## Campaign and result

Campaign: `018_0ea2adf`; [accepted plan](REVISION-PLAN.md).
Baseline: `0ea2adfde7855465cc8d04e58ba98180c42e54a4`.
Working branch: `revision/018_0ea2adf-repository-disclosure`.
Target: `feature/architecture-revision`.

V-001 is implemented, verified, explicitly integrated and published. Initial target-repository adoption includes the packaged disclosure and a discoverable SDD Manager usage notice with the first authorized SDD result. This is an agent workflow instruction, not an installed-client hook. Integration/publication evidence is recorded below.

## Changes and ownership

- `assets/AI_DISCLOSURE.md` is byte-identical to the existing root disclosure. `assets/SDD-MANAGER.md` supplies the named upstream URL, truthful workflow scope and disclosure link.
- The canonical sdd-manage repository-bootstrap reference defines root placement, same-first-commit persistence, README links, existing-content reconciliation, explicit scope conflicts, push-first ordering, interruption/resume and idempotent reuse. Older repositories receive a next-commit adoption backfill without history rewriting.
- Coordinator persistence and direct implementation/steering commit paths apply the policy. sdd-report checks commit evidence without writing; read-only sdd-orient reports adoption state. Focused entries explicitly identify the bundled coordinator reference dependency.
- This source repository receives root `SDD-MANAGER.md` and README links as adoption backfill; its existing root disclosure is retained unchanged. Earlier commits are not represented as bootstrapped.
- Capability documentation and TextStats setup/execution prescribe independent committed-object checks. The harness vendors the assets but leaves root bootstrap to the consumer.

## Verification and evidence boundary

| Check | Observed result |
| --- | --- |
| Byte equality | Root/asset disclosure and source-root/asset usage notice are identical. |
| Changed prose reference links | Existing relative targets resolve; the literal target-README example is checked in its intended root context. |
| Skill structure | All 15 skills pass `agent-package-author/scripts/validate_skill.py`. |
| Manifest / package inventory | Codex manifest JSON parses. Generic Agent Plugins inspector reports `UNKNOWN: no root SKILL.md or plugin.json`; this is the established Codex layout, not a portable manifest claim. |
| TextStats support | `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 79 tests pass, 14.534 seconds. |
| Actual asset carriage | Disposable local-only `prepare` with `source_mode: dirty` copied both current assets byte for byte into the pinned vendor snapshot; target-root copies remained absent. Fixture remotes were local only. |
| Diff / ownership | Working-tree check passed before staging new assets. The complete staged check then flagged two pre-existing quoted blank lines copied verbatim from the disclosure (`> `). Preserve the requested exact copy; the branch diff check excluding only `assets/AI_DISCLOSURE.md` passes. Unrelated pending content is preserved and excluded from staging. |

Source scenario inspection covered initial preparation/review records, direct task and steering persistence, existing disclosure retention, read-only no-write, selected-path conflicts, nested project/root scope, pending copies/index and committed-but-unpushed continuation. These are protocol inspections, not fresh-agent runtime outcomes. The canonical load paths and ordinary commit owners are explicit; no hidden client hook is assumed.

During verification, an initial unittest command omitted the documented `-t acceptance/textstats` and produced a catalog relative-import error; the documented full command above passes. An initial link scan counted an inline README-template example as a source reference; prose-only scanning resolves the actual links. Strict skill validation rejected new cross-skill Markdown entry links; entries now explicitly declare the bundled dependency path, consistent with existing cross-skill workflow dependencies. No runtime-code change was required.

## Persistence

Plan checkpoint `1c15a1d5500ecd3b463ab25cd4ee455becde17c5` was pushed and verified by remote readback before source execution. Source/report commit and explicit target integration are recorded by Git and the publication supplement below.

## Remaining TODOs and limits

Campaign 011 QC implementation and live/client acceptance remain pending a separate later review. The live follow-up now includes first-consumer-commit bootstrap, existing-content preservation, selected-path limits and interruption/resumption checks described in TextStats SETUP. No dedicated acceptance repository run, plugin reinstall, release/version change, or installed-client activation is claimed here.

## Verified integration and publication

Source commit `b346210` and evidence correction `a4902e3fac387c5892ccb03edd635ced62f60153` were pushed; remote readback returned the pinned revision tip. The prospective merged index tree exactly matched the verified source tree, so the 79-test result remains applicable without another runtime change. Merged root asset equality and README links were checked again; the full merge diff check excluding only the byte-preserved disclosure passed.

Explicit merge: `3883680c9e555d23f982f29aafcd7268b0a9a93b`.
Parents: `0ea2adfde7855465cc8d04e58ba98180c42e54a4` and `a4902e3fac387c5892ccb03edd635ced62f60153`.
Target push succeeded and remote readback returned that exact merge SHA. The source branch is retained. This publication supplement is a target report checkpoint after verified integration; Git records its own subsequent commit identity. No other branch was integrated or published.
