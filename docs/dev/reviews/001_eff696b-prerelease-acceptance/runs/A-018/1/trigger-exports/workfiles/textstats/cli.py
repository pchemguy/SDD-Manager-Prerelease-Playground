"""Named-file CLI parsing and exact text presentation.

Invocation validation rejects abbreviated options before acquisition. Expected
file/read/decode failures produce identifying stderr and status 1 without partial
stdout or traceback.
"""

import argparse
import sys
from .io import count_file


def main(argv: list[str] | None = None) -> int:
    """Parse one named file and emit its completed counts.

    Args:
        argv: Invocation arguments excluding the executable; None uses sys.argv.

    Returns:
        Zero on success/help, one on file/read/decode failure, or two for usage.

    Help and usage validate without acquiring input. Before stdin delivery a
    literal '-' remains a named filename. Expected OSError and UnicodeDecodeError
    are translated only here; the silent file API retains its exceptions.
    """
    parser = argparse.ArgumentParser(prog='python -m textstats', allow_abbrev=False, description='Count CRLF/CR/LF lines and Unicode whitespace words in a UTF-8 file.')
    parser.add_argument('--keep-bom', action='store_true', help='retain a leading Unicode BOM as ordinary content')
    parser.add_argument('input', metavar='INPUT', help='named UTF-8 file (use -- before dash-prefixed names)')
    try:
        args = parser.parse_args(argv)
    except SystemExit as exit_request:
        return int(exit_request.code)
    try:
        stats = count_file(args.input, strip_bom=not args.keep_bom)
    except (OSError, UnicodeDecodeError) as failure:
        print(f'{parser.prog}: {args.input!r}: {failure}', file=sys.stderr)
        return 1
    print(f'lines={stats.lines} words={stats.words}')
    return 0
