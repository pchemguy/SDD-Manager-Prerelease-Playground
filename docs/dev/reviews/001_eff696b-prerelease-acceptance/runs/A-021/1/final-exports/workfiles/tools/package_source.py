"""Build the explicit TextStats source allowlist without external dependencies."""

from pathlib import Path
import zipfile

FILES = (
    'README.md', 'docs/public-api.md', 'AI_DISCLOSURE.md', 'SDD-MANAGER.md',
    'textstats/__init__.py', 'textstats/__main__.py', 'textstats/core.py',
    'textstats/io.py', 'textstats/cli.py', 'tools/package_source.py',
    'tools/check_distribution.py',
)


def build_archive(root: Path, output: Path) -> Path:
    """Write approved files under textstats-source/ and return the ZIP path.

    Explicit file names exclude caches, credentials, tests, development records
    and coordinator resources. Missing files fail rather than silently producing
    an incomplete package. Symlink inputs are rejected to retain source ownership.
    """
    root, output = Path(root), Path(output)
    for name in FILES:
        source = root / name
        if not source.is_file() or source.is_symlink():
            raise ValueError(f'Required regular source file missing: {name}')
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(root / name, 'textstats-source/' + name)
    return output


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    print(build_archive(root, root / 'dist' / 'textstats-source.zip'))
