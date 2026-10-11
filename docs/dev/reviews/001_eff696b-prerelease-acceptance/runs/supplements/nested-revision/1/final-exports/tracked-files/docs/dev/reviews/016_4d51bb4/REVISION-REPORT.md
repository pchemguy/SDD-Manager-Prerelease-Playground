# Codex manifest and presentation revision report

## Context and result

- Campaign: `016_4d51bb4`; [plan](REVISION-PLAN.md).
- Baseline: `4d51bb4fa5f627809e6b449e28f89791b7b52f4d`.
- Working branch: `revision/016_4d51bb4-codex-manifest`.
- Target: `feature/architecture-revision`.
- State: source revision verified, explicitly integrated and published; installed UI rendering unverified.

## Superpowers comparison and changes

The inspected installed Superpowers `6.4.2` manifest is `.codex-plugin/plugin.json`. It uses top-level `interface`, `skills: ./skills/`, empty `hooks`, publisher/repository/license/keywords and detailed listing metadata. Its actual installed assets differ from the supplied source example: composer SVG, dark composer PNG, and both logo PNGs live under `.codex-plugin/assets/`; paths are relative to the package root. This observation is not proof that asset directory placement or format caused SDD Manager's installed-page fallback.

SDD Manager now uses only `.codex-plugin/plugin.json`, with a top-level `interface`, explicit skills discovery, empty hooks, author/developer `pchemguy`, repository/homepage, focused keywords, short/long descriptions, starter prompts, category/capabilities and brand colors. Its version is `0.14.3`. SVG composer paths and PNG logo paths are explicit for both themes. `assets/logo.png` is rendered from the retained `assets/icon.svg`; both assets remain at the package root's assets directory. README identifies this as Codex packaging rather than a root Agent Plugins 1.0 package.

No repository-wide license is present; only the bundled TDD component carries a license. No publisher email or plugin-specific privacy/terms policy is established. Those fields were not fabricated or copied from Superpowers. Its `package.json` serves separate Node/Pi integrations, not Codex manifest discovery; no such runtime was introduced.

TextStats package pinning now includes `.codex-plugin`, root assets and skills; historical root-manifest snapshots remain supported. Manifest availability is checked after dirty overlays as well. Documentation is updated, brittle fixed-file-count assertions are replaced by exact Git inventory comparisons, and a regression exercises Codex manifest pinning plus binary asset/untracked asset preservation in dirty preparation.

## Verification and limits

The full support suite passed: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v` (68 tests). The 27-case catalog validated. Direct checks passed manifest format/exact metadata, short-description and prompt limits, 15 skill entries, four contained icon references, 128-pixel SVG and decoded 512-pixel PNG, size limits, and four documents / 70 local links. Visual inspection confirmed the PNG retains the SVG artwork. Actual dirty-source snapshot checks captured 104 package files, including the moved manifest and exact binary logo bytes, with no root manifest. Whitespace checks passed.

Revision `217ffcb00fa78bacb4a54cfd16778053b01ccb69` was pushed to the retained working branch and exact remote readback matched. The complete 11-file branch difference contains only manifest/presentation, package documentation, TextStats snapshot compatibility and campaign records/index. Explicit merge `458716bcd4ae28829f74b00c70c53fdb912841b8` has parents `4d51bb4fa5f627809e6b449e28f89791b7b52f4d` and that revision tip. The prospective merged result passed all 68 support tests, the 27-case catalog, whitespace and conflict checks. Pinning the published revision captured 104 files; every snapshot file matched the prospective merge's bytes and all four icon paths resolved inside the snapshot. Target push and exact remote readback succeeded. This campaign did not advance `main`.

Changing manifest format is the requested compatibility experiment, not a verified repair of the installed plugin page. The repository revision does not update the installed account release. The archived root-manifest campaign records remain historical evidence.

## Publisher display-name correction

The human clarified that the publisher is stylized `PChemGuy`. The follow-up branch `revision/016_4d51bb4-publisher-styling` starts at `efe1a1900fd756fc50d905d5cc3ce33e331d53d6` and changes only `author.name` and `interface.developerName` to that exact spelling. GitHub URL values and package version remain unchanged. Direct comparison with the baseline confirms only these two manifest values change; JSON and whitespace checks pass. Revision `83a38f948c9510ec505f56d902789f0d110d9fb2` was pushed with exact remote readback. Explicit merge `d6a516da960039ac5914caf619ac0fe91cc0b1ce` has parents `efe1a1900fd756fc50d905d5cc3ce33e331d53d6` and that revision tip; merged metadata, conflict and whitespace checks passed. Target publication and exact remote readback succeeded.

## Terminology correction

The human corrected the listing subtitle to use “driven.” `interface.shortDescription` is now `Spec-driven development` (23 characters), preserving the 30-character listing limit. The follow-up branch `revision/016_4d51bb4-driven-subtitle` starts at `a1ae2542f824a2d2ed5d9c2f7ed069155f144c87`. JSON, exact wording and length checks pass; only this manifest value changes. Revision `e62f9bdc5d31023a63574146e7c79102c7208a40` was pushed with exact remote readback. Explicit merge `c6206de189c17433a04fb8fc51e0411de2d4edeb` has parents `a1ae2542f824a2d2ed5d9c2f7ed069155f144c87` and that revision tip. Prospective merged comparison confirmed only the requested subtitle changes; conflict and whitespace checks passed. Target push and exact remote readback succeeded.
