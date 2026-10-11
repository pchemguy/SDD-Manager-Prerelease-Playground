# Plugin presentation metadata revision

## Scope and identity

- Campaign: `013_86ce4eb`.
- Starting baseline: `86ce4ebcbfaf3dfc535f5a448d4e044aa2fb4a81`.
- Working branch: `revision/013_86ce4eb-plugin-metadata`.
- Integration target: `feature/architecture-revision`.
- Accepted request: set the plugin website to `https://github.com/pchemguy/Skill-SDD-Manager` and display name to `SDD Manager`.
- Authorization: the requested repository revision and the coordinator's [scoped authorization policy (historical reference)](https://github.com/pchemguy/SDD-Manager/blob/5e2624e625e33410245cb3b51b1b31120ad18747/skills/sdd-manage/references/revision-authorization.md) cover routine scoped commit, push and verified integration.

## Action and acceptance

V-001 adds portable `homepage` and OpenAI presentation metadata at `extensions.com.openai.interface` in root `plugin.json`. Verify the applicable published portable-schema constraints, the exact requested strings, retained package identity/version, whitespace, and campaign links. Commit and publish the coherent revision; explicitly merge, verify the merged result, and publish the established target.

The [OpenAI package documentation](https://developers.openai.com/plugins/build/plugins) defines this inline extension; the [submission field reference](https://developers.openai.com/plugins/deploy/submission) distinguishes `homepage` from listing `websiteURL`. The [portable schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) permits object-valued extension namespaces.

Stop after this metadata revision. Installed listing refresh and public-directory submission are separate operations.
