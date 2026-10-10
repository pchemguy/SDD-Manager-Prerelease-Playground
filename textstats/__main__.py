"""Run the named-file or binary-stdin TextStats command via python -m textstats."""

from .cli import main

if __name__ == '__main__':
    raise SystemExit(main())
