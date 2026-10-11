# Plugin presentation metadata revision report

## Result and context

- Campaign: `013_86ce4eb`; [accepted plan](REVISION-PLAN.md).
- Starting baseline: `86ce4ebcbfaf3dfc535f5a448d4e044aa2fb4a81`.
- Working branch: `revision/013_86ce4eb-plugin-metadata`.
- Integration target: `feature/architecture-revision`.
- V-001: root `plugin.json` now supplies `homepage`, `extensions.com.openai.interface.displayName` (`SDD Manager`) and `websiteURL` (the requested repository URL). Package identifier `sdd-manager` and version `0.14.1` are retained.
- State: revision verified, explicitly integrated and published.

## Verification

Direct Python checks passed all applicable constraints from the published portable manifest schema and exact requested presentation values, including display-name length. Current official OpenAI documentation confirms the inline extension and separate listing website field. An attempted generic JSON Schema check could not run because the local Python lacks `jsonschema`; no dependency was installed. The direct checks cover every portable-schema constraint applicable to this manifest; they do not validate client rendering.

Whitespace and local campaign-link checks are required before publication and again on the prospective merged result. No skill behavior changed, so runtime acceptance tests are outside this metadata revision.

## Publication and limits

Revision commit `84d18d0681525788f1a23d30700b5de10ac5e9da` was pushed to the working branch; `git ls-remote` returned that exact SHA. Whitespace passed; three campaign/index documents and 36 local links passed. The GitHub plugin's Git-object write endpoint returned `403: Resource not accessible by integration`; ordinary Git publication with existing shell authentication succeeded. This was a connector access limitation, not a platform approval rejection.

The retained working tip is `10d3e7452edc6ff3944e4c38f777f7ddb2966096`. Explicit merge `a4c2c1c24e1a81cbafabbdfdf6a461469c73b13f` has parents `86ce4ebcbfaf3dfc535f5a448d4e044aa2fb4a81` and that working tip. The complete branch difference comprised only the manifest and this campaign's plan, report and index entry. The prospective merge passed the metadata/schema constraints, three documents / 36 local links, staged and unstaged whitespace checks, and had no conflicts. The target push succeeded; remote readback confirmed the exact merge SHA.

The repository change does not update an already installed plugin or establish that its listing has refreshed. Public submission requirements are outside this request. The established integration target was used; `main` was not advanced by this campaign.
