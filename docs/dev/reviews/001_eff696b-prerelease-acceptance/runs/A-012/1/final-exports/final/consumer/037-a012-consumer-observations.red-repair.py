from pathlib import Path
p=Path('tests/unit/test_cli.py');s=p.read_text().replace("with patch('textstats.io.open', create=True) as acquire, patch('textstats.cli.count_file') as counter:","with patch('textstats.io.open', return_value=io.BytesIO(b'a'), create=True) as acquire, patch('textstats.cli.count_file', return_value=TextStats(1, 1)) as counter:");p.write_text(s)
