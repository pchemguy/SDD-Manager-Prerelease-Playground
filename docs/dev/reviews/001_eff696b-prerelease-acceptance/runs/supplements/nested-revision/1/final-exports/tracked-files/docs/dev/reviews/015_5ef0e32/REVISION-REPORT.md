# SVG icon and listing metadata revision report

## Scope and result

- Campaign: `015_5ef0e32`; [plan](REVISION-PLAN.md).
- Baseline: `5ef0e32844ed7a70b820a505e4434d85fa0ddddf`.
- Working branch: `revision/015_5ef0e32-svg-presentation`.
- Integration target: `feature/architecture-revision`.
- Changes: `assets/icon.svg` replaces the PNG; both `composerIcon` and `logo` reference it. The listing category is `Developer Tools` and capabilities are `Interactive`, `Read`, `Write`. The version is `0.14.2`; package identity, display name and website are retained.
- State: repository revision verified, explicitly integrated and published; installed UI outcome unverified.

## Diagnosis and evidence boundary

The supplied screenshot shows a folder fallback. The installed `0.14.1` package contains `assets/icon.png`, and its portable manifest and generated compatibility manifest both reference that file. Its compatibility metadata also contains category `Other` and empty capabilities. Missing installed artwork is therefore not supported as the cause. Client/catalog rendering or import behavior remains unverified.

The replacement SVG uses the same navy document/checkmark motif, with numeric 128 × 128 dimensions and viewBox, simple paths, no embedded bitmap, fonts, script or external resources. It is authored directly as requested vector artwork.

## Verification and publication

XML parsing confirmed numeric square dimensions/viewBox and only SVG/rect/path elements. The self-contained file is below the 5 MiB limit. Sharp rendered it successfully at 32, 64 and 128 pixels; inspected previews retain the document/checkmark motif. Exact manifest values and both included asset paths passed; three campaign/index documents and 40 local links passed, as did whitespace checks.

Revision `5cbf2e59d7284333582b339e414e99ebe4729087` was pushed; exact working-branch remote readback matched. Explicit merge `12e88d8498f3eb15946ecaf8d4c976e29db2c7d7` has parents `5ef0e32844ed7a70b820a505e4434d85fa0ddddf` and that revision tip. The complete six-file difference is limited to the asset replacement, manifest and campaign records/index. Prospective merged SVG, metadata, links, whitespace and conflict checks passed. Target publication succeeded and exact remote readback matched the merge. `main` was not advanced by this campaign.

This revision changes repository packaging, not the installed account release. A fresh installed-page check remains necessary before claiming the reported UI defect resolved.
