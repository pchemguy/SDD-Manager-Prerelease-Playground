"""Verify isolated source imports and real named-file module-entry contracts.

The checker builds/extracts the source ZIP, clears inherited Python import-path
settings, disables user-site packages and uses the extraction as process cwd.
It never substitutes a checkout import for extracted module execution.
"""

import os
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

        def invoke(arguments):
            return subprocess.run([sys.executable, "-B", '-s', *arguments], cwd=root,
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
        dash = root / '-sample'
        dash.write_bytes(b'alpha beta\n')
        result = invoke(['-m', 'textstats', '--', '-sample'])
        assert (result.returncode, result.stdout, result.stderr) == (0, 'lines=1 words=2\n', ''), result
        assert dash.read_bytes() == b'alpha beta\n'
        count += 1
        bad = root / 'bad.txt'
        bad.write_bytes(b'valid prefix\n\xff')
        for args, input_name, cause in [(['missing.txt'], 'missing.txt', 'No such file'),
                                        (['bad.txt'], 'bad.txt', 'utf-8')]:
            result = invoke(['-m', 'textstats', *args])
            assert result.returncode == 1 and result.stdout == '', result
            assert input_name in result.stderr and cause in result.stderr and 'Traceback' not in result.stderr, result
            count += 1
        assert bad.read_bytes() == b'valid prefix\n\xff'
        for args in [[], ['sample.txt', 'extra.txt'], ['--unknown', 'missing.txt'], ['--keep', 'missing.txt']]:
            result = invoke(['-m', 'textstats', *args])
            assert result.returncode == 2 and result.stdout == '', result
            assert 'usage:' in result.stderr and 'error:' in result.stderr and 'Traceback' not in result.stderr, result
            count += 1
        result = invoke(['-m', 'textstats', '--help'])
        assert result.returncode == 0 and result.stderr == '' and 'INPUT' in result.stdout and '--keep-bom' in result.stdout, result
        count += 1
        print(f'{count} extracted module cases passed')
        return count


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    verify_archive(build_archive(root, root / 'dist' / 'textstats-source.zip'))
