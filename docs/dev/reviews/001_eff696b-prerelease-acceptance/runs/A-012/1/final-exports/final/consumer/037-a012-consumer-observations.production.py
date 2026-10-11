from pathlib import Path
import re
p=Path('textstats/cli.py');s=p.read_text().replace('Named-file range parsing and text or JSON presentation.','Named-file range parsing and exact text presentation.').replace('import json\n','');s=re.sub(r"    parser.add_argument\('--json'.*\n",'',s);s=re.sub(r'    if args.json:\n.*?    return 0',"    print(f'lines={stats.lines} words={stats.words}')\n    return 0",s,flags=re.S);p.write_text(s)
p=Path('tools/check_distribution.py');s=p.read_text().replace('import json\n','');a=s.index('                for json_args');b=s.index('        dash =',a);s=s[:a]+s[b:]
a=s.index("        result = invoke(['-m', 'textstats', '--json', '--', '-sample'])");b=s.index("        bad =",a);s=s[:a]+s[b:]
a=s.index('            for format_option');b=s.index('        assert bad.read_bytes()',a);s=s[:a]+'''            result = invoke(['-m', 'textstats', *args])
            assert result.returncode == 1 and result.stdout == '', result
            assert input_name in result.stderr and cause in result.stderr and 'Traceback' not in result.stderr, result
            count += 1
'''+s[b:]
s=s.replace("and '--json' in result.stdout","and '--json' not in result.stdout")
a=s.index('        def check_range');b=s.index('        invalid =',a)
s=s[:a]+'''        def check_range(arguments, expected):
            nonlocal count
            result = invoke(['-m', 'textstats', *arguments])
            assert (result.returncode, result.stdout, result.stderr) == (
                0, f'lines={expected[0]} words={expected[1]}\\n', ''), result
            count += 1

        for text, endpoint, default, retained in anchors:
            raw = text.encode('utf-8')
            sample.write_bytes(raw)
            for keep, expected in [(False, default), (True, retained)]:
                flags = ['--keep-bom'] if keep else []
                for spelling in [['--lines', endpoint], ['--lines=' + endpoint]]:
                    check_range([*flags, *spelling, 'sample.txt'], expected)
                    assert sample.read_bytes() == raw

        sample.write_bytes(b'alpha beta\\nbeta\\nlast two')
        for range_group in [('--lines', '2:3'), ('--lines=2:3',)]:
            for keep in [False, True]:
                option_groups = [range_group] + ([('--keep-bom',)] if keep else [])
                for groups in itertools.permutations(option_groups):
                    for position in range(len(groups) + 1):
                        ordered = list(groups)
                        ordered.insert(position, ('sample.txt',))
                        check_range([arg for group in ordered for arg in group], (2, 3))
                        assert sample.read_bytes() == b'alpha beta\\nbeta\\nlast two'
        huge = '9' * 5001
        for endpoint, expected in [('2:' + huge, (2, 3)), (huge + ':' + huge, (0, 0)),
                                   ('0' * 5000 + '2:' + '0' * 5000 + '3', (2, 3))]:
            for keep in [False, True]:
                flags = ['--keep-bom'] if keep else []
                for spelling in [['--lines', endpoint], ['--lines=' + endpoint]]:
                    check_range([*flags, *spelling, 'sample.txt'], expected)
                    assert sample.read_bytes() == b'alpha beta\\nbeta\\nlast two'

'''+s[b:]
s=s.replace("invalid_groups = [['--lines=' + value] for value in invalid] + [","invalid_groups = [['--lines=' + value] for value in invalid] + [['--lines', value] for value in invalid] + [").replace("['--lines', '--json']","['--lines', '--keep-bom']")
a=s.index('        for group in invalid_groups:');b=s.index("        sample.write_bytes(b'a b",a)
s=s[:a]+'''        for group in invalid_groups:
            for keep in [False, True]:
                flags = ['--keep-bom'] if keep else []
                # Missing input distinguishes usage validation from acquisition.
                result = invoke(['-m', 'textstats', *flags, 'missing.txt', *group])
                assert result.returncode == 2 and result.stdout == '', result
                assert 'usage:' in result.stderr and 'error:' in result.stderr and 'Traceback' not in result.stderr, result
                count += 1
        for keep in [False, True]:
            flags = ['--keep-bom'] if keep else []
            result = invoke(['-m', 'textstats', *flags, '--lines', '1:1', 'bad.txt'])
            assert result.returncode == 1 and result.stdout == '', result
            assert 'bad.txt' in result.stderr and 'utf-8' in result.stderr and 'Traceback' not in result.stderr, result
            assert bad.read_bytes() == b'valid prefix\\n\\xff'
            count += 1
        for name in ['-sample', '-', '--json']:
            path = root / name
            path.write_bytes(b'alpha beta\\nbeta')
            for arguments, expected in [(['--', name], (2, 3)),
                                        (['--lines=2:2', '--', name], (1, 1))]:
                check_range(arguments, expected)
                assert path.read_bytes() == b'alpha beta\\nbeta'
        for option in ['--json', '--json=true', '--j']:
            for name in ['sample.txt', 'missing.txt', 'bad.txt']:
                for arguments in [[option, name], [name, option],
                                  ['--keep-bom', '--lines=1:1', name, option]]:
                    result = invoke(['-m', 'textstats', *arguments])
                    assert (result.returncode, result.stdout) == (2, ''), result
                    assert 'usage:' in result.stderr and 'error:' in result.stderr and 'Traceback' not in result.stderr, result
                    count += 1

'''+s[b:];p.write_text(s)
print('Removed CLI option/import/renderer; extraction checks now preserve text/BOM/range permutations and reject removed forms.')
