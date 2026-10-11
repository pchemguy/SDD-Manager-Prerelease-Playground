# Specification

S1: Given one UTF-8 file path, print `lines=N` followed by newline and exit 0. S2: Count a final unterminated line once; empty files count as zero. S3: Reject unreadable input or decoding failure with a clear stderr message and exit 1; usage errors exit 2. Close the file on success and failure. No JSON, stdin, networking or archives. Acceptance covers success, empty/final line, file/decoding errors, usage status and resource release.
