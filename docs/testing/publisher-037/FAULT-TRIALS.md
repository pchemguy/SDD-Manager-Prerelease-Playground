# Controlled live-provider publisher faults

The playground-only wrapper invokes the unchanged publisher and injects a stop only for requests starting `037-cp014-partial-`, after the real provider has acknowledged the first uploaded asset. It prints sanitized effect identity, then raises. This is a controlled post-effect response suppression, not native network response loss or uncontrolled termination. The existing publisher remains the sole release writer. Normal requests pass through without injection.

A separate manifest-version fixture isolates the fault draft from the verified plugin prerelease. Both fixture manifests change together; candidate package metadata differs from the immutable plugin and is identified explicitly. First failed/partial attempts, real draft/assets and later read-before-retry are retained. Repeated original-package requests provide overlapping-run concurrency observations. Neither fixture extends optional consumer isolation/termination claims.
