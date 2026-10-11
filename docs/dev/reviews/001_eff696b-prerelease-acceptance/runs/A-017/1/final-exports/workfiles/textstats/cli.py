"""Named-file CLI validation, input-failure diagnostics and text presentation."""

import argparse
import sys
from .io import count_file


def main(argv: list[str] | None = None) -> int:
    """Parse one named file and emit its completed counts.

    Args:
        argv: Invocation arguments excluding the executable; None uses sys.argv.

    Returns:
        Zero on success/help, one on input failure, or two on invalid usage.

    Help and usage validate without acquiring input. Before stdin delivery a
    literal '-' remains a named filename. Expected file/decode failures identify
    the input and cause on stderr without a traceback or partial stdout result.
    Public API exception behavior remains unchanged.
    """
    parser = argparse.ArgumentParser(allow_abbrev=False, prog='python -m textstats', description='Count CRLF/CR/LF lines and Unicode whitespace words in a UTF-8 file.')
    parser.add_argument('--keep-bom', action='store_true', help='retain a leading Unicode BOM as ordinary content')
    parser.add_argument('input', metavar='INPUT', help='named UTF-8 file (use -- before dash-prefixed names)')
    try:
        args = parser.parse_args(argv)
    except SystemExit as exit_request:
        return int(exit_request.code)
    try:
        stats = count_file(args.input, strip_bom=not args.keep_bom)
    except (OSError, UnicodeDecodeError) as error:
        print(f'{parser.prog}: {args.input}: {error}', file=sys.stderr)
        return 1
    print(f'lines={stats.lines} words={stats.words}')
    return 0
