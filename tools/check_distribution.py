"""Verify isolated source imports and real named-file module-entry contracts.

The checker builds/extracts the source ZIP, clears inherited Python import-path
settings, disables user-site packages and uses the extraction as process cwd.
It never substitutes a checkout import for extracted module execution.
"""

import os
import json
import itertools
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

try:
    from .package_source import build_archive, FILES
except ImportError:  # Direct script execution puts tools/ on sys.path.
    from package_source import build_archive, FILES


def verify_archive(archive: Path) -> int:
    """Check an approved ZIP in a temporary extraction; return CLI case count.

    Raises AssertionError/RuntimeError on bad contents, import provenance or
    process results. Every sample is checked for unchanged bytes. Temporary
    source/input files are removed on success and failure.
    """
    with tempfile.TemporaryDirectory() as directory:
        destination = Path(directory)
        with zipfile.ZipFile(archive) as bundle:
            expected = {'textstats-source/' + name for name in FILES}
            if set(bundle.namelist()) != expected or len(bundle.namelist()) != len(expected):
                raise RuntimeError('Archive does not match the approved source allowlist')
            bundle.extractall(destination)
        root = destination / 'textstats-source'
        environment = {key: value for key, value in os.environ.items()
                       if key not in {'PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP'}}
        environment['PYTHONNOUSERSITE'] = '1'
        environment['PYTHONDONTWRITEBYTECODE'] = '1'

        def invoke(arguments):
            return subprocess.run([sys.executable, '-B', '-s', *arguments], cwd=root,
                                  env=environment, capture_output=True, text=True)

        imported = invoke(['-c', 'import textstats; print(textstats.__file__)'])
        assert imported.returncode == 0 and imported.stderr == '', imported
        location = Path(imported.stdout.strip()).resolve()
        assert location == (root / 'textstats' / '__init__.py').resolve(), location
        print(f'extracted import: {location}')

        count = 0
        samples = [('', (0, 0), (0, 0)), ('alpha beta', (1, 2), (1, 2)),
                   ('alpha\n', (1, 1), (1, 1)), ('\n', (1, 0), (1, 0)),
                   ('α\r\n猫\rβ γ\n', (3, 4), (3, 4)), ('alpha\n\n', (2, 1), (2, 1)),
                   (' \t', (1, 0), (1, 0)), ('alpha\u2028beta', (1, 2), (1, 2)),
                   ('\ufeff', (0, 0), (1, 1)), ('\ufeff\ufeff', (1, 1), (1, 1)),
                   ('\ufeffalpha beta', (1, 2), (1, 2)), ('a\ufeffb', (1, 1), (1, 1)),
                   ('\r\n', (1, 0), (1, 0)), ('\r', (1, 0), (1, 0))]
        sample = root / 'sample.txt'
        for text, default, retained in samples:
            raw = text.encode('utf-8')
            sample.write_bytes(raw)
            for options, expected in [([], default), (['--keep-bom'], retained)]:
                result = invoke(['-m', 'textstats', *options, 'sample.txt'])
                assert (result.returncode, result.stdout, result.stderr) == (
                    0, f'lines={expected[0]} words={expected[1]}\n', ''), result
                assert sample.read_bytes() == raw
                count += 1
                for json_args in [['--json', *options, 'sample.txt'], ['sample.txt', *options, '--json']]:
                    result = invoke(['-m', 'textstats', *json_args])
                    assert result.returncode == 0 and result.stderr == '', result
                    assert result.stdout.endswith('\n') and result.stdout.count('\n') == 1, result
                    payload = json.loads(result.stdout)
                    assert payload == {'lines': expected[0], 'words': expected[1]}, result
                    assert all(type(value) is int for value in payload.values()), result
                    assert sample.read_bytes() == raw
                    count += 1
        dash = root / '-sample'
        dash.write_bytes(b'alpha beta\n')
        result = invoke(['-m', 'textstats', '--', '-sample'])
        assert (result.returncode, result.stdout, result.stderr) == (0, 'lines=1 words=2\n', ''), result
        assert dash.read_bytes() == b'alpha beta\n'
        count += 1
        result = invoke(['-m', 'textstats', '--json', '--', '-sample'])
        assert result.returncode == 0 and result.stderr == '', result
        assert json.loads(result.stdout) == {'lines': 1, 'words': 2}, result
        count += 1
        bad = root / 'bad.txt'
        bad.write_bytes(b'valid prefix\n\xff')
        for args, input_name, cause in [(['missing.txt'], 'missing.txt', 'No such file'),
                                        (['bad.txt'], 'bad.txt', 'utf-8')]:
            for format_option in [[], ['--json']]:
                result = invoke(['-m', 'textstats', *format_option, *args])
                assert result.returncode == 1 and result.stdout == '', result
                assert input_name in result.stderr and cause in result.stderr and 'Traceback' not in result.stderr, result
                count += 1
        assert bad.read_bytes() == b'valid prefix\n\xff'
        for args in [[], ['sample.txt', 'extra.txt'], ['--unknown', 'missing.txt'], ['--keep', 'missing.txt'],
                     ['--json'], ['--json', 'sample.txt', 'extra.txt'], ['--json', '--unknown', 'missing.txt'], ['--j', 'missing.txt']]:
            result = invoke(['-m', 'textstats', *args])
            assert result.returncode == 2 and result.stdout == '', result
            assert 'usage:' in result.stderr and 'error:' in result.stderr and 'Traceback' not in result.stderr, result
            count += 1
        result = invoke(['-m', 'textstats', '--help'])
        assert result.returncode == 0 and result.stderr == '' and 'INPUT' in result.stdout and '--keep-bom' in result.stdout and '--json' in result.stdout and '--lines' in result.stdout, result
        count += 1
        # Literal contract anchors are independent of checkout counting helpers.
        anchors = [
            ('alpha beta\nbeta\nlast two', '2:3', (2, 3), (2, 3)),
            ('alpha beta\nbeta\nlast two', '2:99', (2, 3), (2, 3)),
            ('alpha beta\nbeta\nlast two', '1:1', (1, 2), (1, 2)),
            ('alpha beta\nbeta\nlast two', '0001:0001', (1, 2), (1, 2)),
            ('alpha beta\nbeta\nlast two', '4:99', (0, 0), (0, 0)),
            ('a\n\n', '2:9', (1, 0), (1, 0)),
            ('a\r\nb c\rd\n', '2:3', (2, 3), (2, 3)),
            ('a\n\ufeff', '2:2', (1, 1), (1, 1)),
            ('', '1:99', (0, 0), (0, 0)),
            ('\ufeff', '1:1', (0, 0), (1, 1)),
            ('\ufeff\ufeff', '1:1', (1, 1), (1, 1)),
            ('alpha\u2028beta', '1:1', (1, 2), (1, 2)),
            ('\n', '1:1', (1, 0), (1, 0)),
        ]

        def check_range(arguments, expected, json_mode=False):
            nonlocal count
            result = invoke(['-m', 'textstats', *arguments])
            assert result.returncode == 0 and result.stderr == '', result
            assert result.stdout.endswith('\n') and result.stdout.count('\n') == 1, result
            if json_mode:
                payload = json.loads(result.stdout)
                assert payload == dict(zip(('lines', 'words'), expected)), result
                assert all(type(value) is int for value in payload.values()), result
            else:
                assert result.stdout == f'lines={expected[0]} words={expected[1]}\n', result
            count += 1

        for text, endpoint, default, retained in anchors:
            raw = text.encode('utf-8')
            sample.write_bytes(raw)
            for keep, expected in [(False, default), (True, retained)]:
                for json_mode in [False, True]:
                    flags = (['--keep-bom'] if keep else []) + (['--json'] if json_mode else [])
                    check_range([*flags, '--lines', endpoint, 'sample.txt'], expected, json_mode)
                    assert sample.read_bytes() == raw

        sample.write_bytes(b'alpha beta\nbeta\nlast two')
        for range_group in [('--lines', '2:3'), ('--lines=2:3',)]:
            for groups in itertools.permutations([range_group, ('--keep-bom',), ('--json',)]):
                for position in range(4):
                    ordered = list(groups)
                    ordered.insert(position, ('sample.txt',))
                    check_range([arg for group in ordered for arg in group], (2, 3), True)
                    assert sample.read_bytes() == b'alpha beta\nbeta\nlast two'
        huge = '9' * 5001
        for endpoint, expected in [('2:' + huge, (2, 3)), (huge + ':' + huge, (0, 0)),
                                   ('0' * 5000 + '2:' + '0' * 5000 + '3', (2, 3))]:
            for keep in [False, True]:
                for json_mode in [False, True]:
                    flags = (['--keep-bom'] if keep else []) + (['--json'] if json_mode else [])
                    check_range([*flags, '--lines=' + endpoint, 'sample.txt'], expected, json_mode)
                    assert sample.read_bytes() == b'alpha beta\nbeta\nlast two'

        invalid = ['0:1', '1:0', '3:2', '-1:2', '+1:2', '1:-2', '1:+2',
                   ' 1:2', '1:2 ', '1 :2', '1:\t2', '١:٢', '１:２',
                   ':2', '1:', ':', '1:2:3', '1', '']
        invalid_groups = [['--lines=' + value] for value in invalid] + [
            ['--lines'], ['--lines', '--json'],
            ['--lines', '1:2', '--lines', '1:2'],
            ['--lines=1:2', '--lines=1:2'],
            ['--lines=1:2', '--lines', '2:3'],
        ]
        for group in invalid_groups:
            for keep in [False, True]:
                for json_mode in [False, True]:
                    flags = (['--keep-bom'] if keep else []) + (['--json'] if json_mode else [])
                    # Missing file distinguishes usage validation from acquisition.
                    result = invoke(['-m', 'textstats', *flags, 'missing.txt', *group])
                    assert result.returncode == 2 and result.stdout == '', result
                    assert 'usage:' in result.stderr and 'error:' in result.stderr and 'Traceback' not in result.stderr, result
                    count += 1
        for keep in [False, True]:
            for json_mode in [False, True]:
                flags = (['--keep-bom'] if keep else []) + (['--json'] if json_mode else [])
                result = invoke(['-m', 'textstats', *flags, '--lines', '1:1', 'bad.txt'])
                assert result.returncode == 1 and result.stdout == '', result
                assert 'bad.txt' in result.stderr and 'utf-8' in result.stderr and 'Traceback' not in result.stderr, result
                assert bad.read_bytes() == b'valid prefix\n\xff'
                count += 1
        for name in ['-sample', '-']:
            path = root / name
            path.write_bytes(b'alpha beta\nbeta')
            for json_mode in [False, True]:
                check_range([*(['--json'] if json_mode else []), '--lines=2:2', '--', name], (1, 1), json_mode)
                assert path.read_bytes() == b'alpha beta\nbeta'

        sample.write_bytes(b'a b\nc')
        api = invoke(['-c', 'import inspect; import textstats; '
                      'from textstats import TextStats, count_text, count_file; '
                      'assert set(textstats.__all__) == {"TextStats", "count_text", "count_file"}; '
                      'assert count_text("a b\\nc") == TextStats(2, 3); '
                      'assert count_file("sample.txt") == TextStats(2, 3); '
                      'assert count_text("\\ufeff", strip_bom=False) == TextStats(1, 1); '
                      'assert list(inspect.signature(count_text).parameters) == ["text", "strip_bom"]; '
                      'assert list(inspect.signature(count_file).parameters) == ["path", "strip_bom"]; '
                      'assert all(inspect.signature(f).parameters["strip_bom"].kind == inspect.Parameter.KEYWORD_ONLY '
                      'and inspect.signature(f).parameters["strip_bom"].default is True for f in (count_text, count_file))'])
        assert (api.returncode, api.stdout, api.stderr) == (0, '', ''), api
        assert sample.read_bytes() == b'a b\nc'
        print(f'{count} extracted module cases passed')
        return count


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    verify_archive(build_archive(root, root / 'dist' / 'textstats-source.zip'))
