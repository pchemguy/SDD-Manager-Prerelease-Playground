# Exact-candidate release handoff

The repository publisher is `.github/workflows/release.yml`, triggered only by manual dispatch. Pushing a tag alone does not publish. Its selected workflow ref supplies tooling; the separate full source SHA supplies the candidate. The workflow must first exist on the default branch for GitHub to discover manual dispatch. Publication requires an existing tag peeled to that exact source and agreement with the canonical manifest version.

Prepare curated body-only Markdown through the shared [highlights owner](../skills/sdd-forge/references/release-highlights.md). Preserve human sections, pin their source and hash their UTF-8 bytes. Retain the local draft until actual published-body readback confirms consumption; a dispatch, build-only run or failed publisher does not consume it.

Dispatch one string input named `handoff`, containing this JSON object. Pass it using a structured API/CLI input file, never interpolate notes into shell code.

| Field | Contract |
| --- | --- |
| `source` | Full lowercase 40-character candidate commit SHA. |
| `tag` | `v` followed by that source’s manifest version. |
| `notes_source` | Same SHA as `source`; editorial coverage must actually reach it. |
| `notes` | Nonempty curated multiline Markdown body, without YAML front matter. |
| `notes_sha256` | SHA-256 of the exact UTF-8 `notes` bytes. |
| `publish` | Boolean; false performs build/checks only. |
| `prerelease` | Boolean, explicitly selected. |
| `make_latest` | Boolean; stable latest is opt-in, prohibited for prereleases. |
| `request_id` | Unique 1–80 character correlation marker: letters, digits, underscore or hyphen. |

The complete handoff is limited to 60,000 UTF-8 bytes. Unknown or missing fields are rejected. Oversized notes require an accepted alternative transport before dispatch; no automatic arbitrary URL retrieval is implemented.

The build job runs source support checks and tooling publisher contracts, builds the explicit shipped inventory and verifies every ZIP member against the committed source. The publishing job rebuilds the same candidate and compares its archive hash with the build job before any release call. Build-only performs no tag/release/latest writes. The tag is created separately on the verified candidate when that effect is authorized.

A single repository/tag concurrency group retains running work and queues pending runs within GitHub’s supported bound. Repeated invocations read the complete release/asset inventories. Matching drafts upload only verified missing assets; matching published releases require readback and perform no mutation. Field conflicts, foreign/duplicate/starter assets or differing bytes stop without deletion or clobber. An uncertain mutation exits; inspect actual provider effects before a new invocation. Completed assets remain in a draft until every required asset is verified.

Final verification reads actual tag source, body, state, asset downloads and latest identity. Stable/non-latest publication preserves the observed prior latest identity; a provider discrepancy is reported rather than silently corrected. The log and `build/release-observation.json` record source, workflow commit, run/request identifiers and hashes without credentials. Correlate the actual workflow run and retain its observation/logs as release evidence. Local contract success does not establish CI or hosted publication success.
