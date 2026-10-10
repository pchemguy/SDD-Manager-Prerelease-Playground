"""Named-file CLI parsing and exact text presentation.

Milestone 1.1 delivers success, BOM policy, option termination and help.
Complete input-failure diagnostics belong to the following milestone.
"""

import argparse
from .io import count_file


def main(argv: list[str] | None = None) -> int:
    """Parse one named file and emit its completed counts.

    Args:
        argv: Invocation arguments excluding the executable; None uses sys.argv.

    Returns:
        Zero on success/help or argparse's usage status on invalid invocation.

    Help and usage validate without acquiring input. Before stdin delivery a
    literal '-' remains a named filename. Expected file/decode exceptions still
    propagate here until the failure-handling task is delivered.
    """
    parser = argparse.ArgumentParser(prog='python -m textstats', description='Count CRLF/CR/LF lines and Unicode whitespace words in a UTF-8 file.')
    parser.add_argument('--keep-bom', action='store_true', help='retain a leading Unicode BOM as ordinary content')
    parser.add_argument('input', metavar='INPUT', help='named UTF-8 file (use -- before dash-prefixed names)')
    try:
        args = parser.parse_args(argv)
    except SystemExit as exit_request:
        return int(exit_request.code)
    stats = count_file(args.input, strip_bom=not args.keep_bom)
    print(f'lines={stats.lines} words={stats.words}')
    return 0
