# Codex manifest and presentation revision

- Campaign: `016_4d51bb4`.
- Baseline: `4d51bb4fa5f627809e6b449e28f89791b7b52f4d`.
- Working branch: `revision/016_4d51bb4-codex-manifest`.
- Target: `feature/architecture-revision`.
- Accepted scope: examine installed Superpowers packaging; expand and move SDD Manager's manifest to `.codex-plugin/plugin.json`, with suitable presentation metadata and assets.

V-001 moves the manifest to the Codex format, removes the portable root schema/extension wrapper, adds truthful publisher/repository/keyword/listing metadata and default prompts, explicitly declares `skills` and empty `hooks`, and supplies light/dark SVG composer icons and PNG listing logos. Keep the SVG as editable source; increment the package to `0.14.3`. Update current package documentation and TextStats package pinning, including binary assets and both supported manifest layouts for historical runs.

Verify JSON fields, contained paths, all 15 skill entries, artwork dimensions/rendering, short-description/prompt limits, local documentation links, support tests, case catalog, and whitespace. Commit/push the coherent revision, explicitly merge and verify the prospective result, publish the established target and retain evidence under the [scoped authorization policy (historical reference)](https://github.com/pchemguy/SDD-Manager/blob/5e2624e625e33410245cb3b51b1b31120ad18747/skills/sdd-manage/references/revision-authorization.md).

Do not copy Superpowers author identity, email or license. No repository-wide license or plugin legal policy is established, so those fields remain absent. No Node/Pi runtime is required; do not add `package.json`. Installed-page icon resolution remains a separate client check.
