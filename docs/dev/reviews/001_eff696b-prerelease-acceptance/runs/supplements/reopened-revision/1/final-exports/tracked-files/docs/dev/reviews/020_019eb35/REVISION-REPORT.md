# Workflow publication revision report

Campaign: 020_019eb35. Baseline: 019eb354cf0921ebd6056e6579763ac33d0baec2. Branch: revision/020_019eb35-workflow-publication. Target: feature/architecture-revision. Status: implemented, verified, integrated and published.

## Incident and attribution

Live acceptance A-004 prepared local T-001 commit 9b24dbd8bacbfcfa8e09c38e131baaecc3ba8f76. Independent local tests passed, but a worker's normal Git push was rejected by platform automatic approval review. The coordinator then asked for publication approval despite the existing designated repository/GO/resume authorization. After the user rejected that redundant framing and directed resumption, normal parent Git publication succeeded for the task and evidence commit e77973c. A subsequent completion-evidence comment was separately rejected by the platform; readback confirmed issue #1 remained open with zero comments.

The root's redundant approval question is a confirmed coordination failure against the established scope. The plugin's authorization/reference routing encouraged supplying context to platform review and did not explicitly separate review completion from workflow publication; this ambiguity is directly corrected by the user-defined policy. No distinct callable platform review skill was observed: the reported rejections came from platform automatic approval enforcement, which the plugin cannot disable. Parent push success does not establish that the source amendment can prevent platform rejection. Original blocked results and later effects remain retained in the acceptance report.

## Changes

V-001: define report-commit end of review; publication belongs to the coordinating/execution workflow. Carry authorized effects through full workflows, including active maintained hosting. Prohibit invoking review skills or adding permission-review stages for pushes. Reuse actual human authority; report platform execution denial separately; retain no-bypass, current-state readback and explicit scope limits. Align coordinator, Git/review references, implementation checkpoint, reporting templates and README.

V-002: package version is 0.14.4. The tested acceptance package remains immutable at the baseline.

## Verification and limitations

All 79 support tests pass with the documented package-root discovery command; all 27 catalog cases validate. Changed live references, 15 skill frontmatter records, JSON/asset paths and whitespace checks pass. Independent assessment of five workflow requests found no material contradiction. Initial discovery omitted the required -t package root, causing a relative-import error; corrected invocation passed without source changes. Logs and summary are retained in verification/. Independent source provenance is retained in independent/. No claim that plugin instructions change platform enforcement or that the installed package has refreshed. Source publication and integration will be recorded from actual refs.

## Publication and integration evidence

Normal execution-owner Git publication (no review skill for push) published revision commit 55655e9a0ae2ddd2add42318e084e3846367b18b. Explicit merge eb42efeaf346b6876c014e24f2b6e38e8a65f947 has parents 019eb354cf0921ebd6056e6579763ac33d0baec2 and 55655e9a0ae2ddd2add42318e084e3846367b18b. Prospective merged state passed all 79 support tests, 27-case catalog validation and staged whitespace checks; its package/skill/README tree exactly matches the verified revision. Exact Git remote readback confirmed both revision and feature/architecture-revision tips. Main was not changed. Original source checkout's unrelated untracked files were preserved.

The source package is 0.14.4. Installed-client reload/update is not exposed here and is not claimed. The tested 0.14.3 acceptance snapshot remains unchanged.

The host subsequently rejected an even narrower same-repository completion comment containing only already-published commit/TASKS links, stating explicit payload/destination disclosure authorization was absent. Independent GET still shows issue #1 open. No further retry, alternate channel or closure was attempted. This demonstrates the platform limitation remains; the source change removes plugin-level routing and redundant approval behavior, not host enforcement.
