# Architecture

CLI delegates text counting to a pure counter and owns file/error handling. Counter does not depend on CLI. All processing is synchronous and resource ownership stays in CLI.
