# Setup cursor correction

Coordinator supplied evidence_paths as a mapping, but the strict v1 schema requires an array. Preserved the original published cursor and corrected its shape without changing source/run identity or any consumer result. The optional jsonschema package was unavailable; the pinned standard-library validator independently checked the corrected INPUTS and RUN-STATE. No consumer attempt preceded this intervention.
