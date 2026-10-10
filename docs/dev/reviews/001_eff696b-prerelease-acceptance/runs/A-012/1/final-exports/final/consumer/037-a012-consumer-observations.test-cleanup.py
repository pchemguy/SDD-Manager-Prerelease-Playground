from pathlib import Path
p=Path('tests/integration/test_cli.py');s=p.read_text().replace(' + []','');p.write_text(s)
print('Removed empty list remnants from retired JSON branches; retained scenarios unchanged.')
