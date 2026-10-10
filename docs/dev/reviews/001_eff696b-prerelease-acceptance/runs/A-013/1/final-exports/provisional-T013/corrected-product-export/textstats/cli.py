"""Named-file range parsing and exact text presentation.

Expected acquisition/decode failures produce an identifying stderr diagnostic
and status 1; invocation errors produce status 2 before acquisition.
"""

import argparse
import sys
from .io import count_file, _read_file_text
from .core import _normalize_text, _select_lines, _count_normalized


def _decimal_endpoint(digits: str) -> int:
    """Convert validated ASCII digits without the interpreter string-int cap."""
    value = 0
    for digit in digits:
        value = value * 10 + (ord(digit) - ord('0'))
    return value


class _RangeAction(argparse.Action):
    """Reject repeated options and validate unbounded endpoints before access."""

    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(namespace, self.dest, None) is not None:
            raise argparse.ArgumentError(self, "--lines may be specified only once")
        parts = values.split(':')
        if len(parts) != 2 or any(not part or any(not '0' <= c <= '9' for c in part) for part in parts):
            raise argparse.ArgumentError(self, "expected positive ASCII decimal START:END")
        start, end = (_decimal_endpoint(part) for part in parts)
        if start == 0 or end == 0 or start > end:
            raise argparse.ArgumentError(self, "endpoints must be positive with START <= END")
        setattr(namespace, self.dest, (start, end))


def main(argv: list[str] | None = None) -> int:
    """Parse one named file and emit its completed counts.

    Args:
        argv: Invocation arguments excluding the executable; None uses sys.argv.

    Returns:
        Zero on success/help, one for input failures, or two for invalid usage.

    Range validation precedes acquisition; complete strict decode precedes
    once-only BOM normalization, preserved selection and normalized counting.
    The public API remains whole-input. Help never acquires input.
    Before stdin delivery a literal '-' remains a named filename. Expected
    file/decode failures are translated without a traceback; the public file
    API retains its exceptions.
    """
    parser = argparse.ArgumentParser(prog='python -m textstats', allow_abbrev=False, description='Count CRLF/CR/LF lines and Unicode whitespace words in a UTF-8 file.')
    parser.add_argument('--keep-bom', action='store_true', help='retain a leading Unicode BOM as ordinary content')
    parser.add_argument('--lines', action=_RangeAction, metavar='START:END', help='select inclusive positive ASCII decimal logical lines (one range only)')
    parser.add_argument('input', metavar='INPUT', help='named UTF-8 file (use -- before dash-prefixed names)')
    try:
        args = parser.parse_args(argv)
    except SystemExit as exit_request:
        return int(exit_request.code)
    try:
        if args.lines is None:
            stats = count_file(args.input, strip_bom=not args.keep_bom)
        else:
            text = _read_file_text(args.input)
            normalized = _normalize_text(text, not args.keep_bom)
            stats = _count_normalized(_select_lines(normalized, *args.lines))
    except (OSError, UnicodeDecodeError) as failure:
        print(f"textstats: {args.input!r}: {failure}", file=sys.stderr)
        return 1
    print(f'lines={stats.lines} words={stats.words}')
    return 0
