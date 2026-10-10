from pathlib import Path
import re,ast
p=Path('tests/unit/test_cli.py');s=p.read_text().replace('import json\n','')
a=s.index('    def test_json_renders');b=s.index('    def test_success_renders',a)
s=s[:a]+'''    def test_removed_json_forms_reject_before_all_acquisition(self):
        for option in ['--json', '--json=true', '--j']:
            for args in [[option, 'named'], ['named', option],
                         ['--keep-bom', option, 'named'],
                         ['--lines=1:1', 'named', option]]:
                with self.subTest(args=args):
                    out, err = io.StringIO(), io.StringIO()
                    with patch('textstats.io.open', create=True) as acquire, patch('textstats.cli.count_file') as counter:
                        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                            status = main(args)
                    self.assertEqual((status, out.getvalue()), (2, ''))
                    self.assertIn('usage:', err.getvalue())
                    self.assertIn('error:', err.getvalue())
                    self.assertNotIn('Traceback', err.getvalue())
                    acquire.assert_not_called()
                    counter.assert_not_called()

    def test_literal_json_filename_after_termination(self):
        out, err = io.StringIO(), io.StringIO()
        with patch('textstats.cli.count_file', return_value=TextStats(1, 2)) as counter:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                status = main(['--', '--json'])
        self.assertEqual((status, out.getvalue(), err.getvalue()), (0, 'lines=1 words=2\\n', ''))
        counter.assert_called_once_with('--json', strip_bom=True)

'''+s[b:]
s=s.replace("for options in [[], ['--keep-bom'], ['--json'], ['--json', '--keep-bom']]:","for options in [[], ['--keep-bom']]:")
s=re.sub(r"            if '--json' in options:\n.*?            acquire.assert_called", "            self.assertEqual(out, 'lines=1 words=1\\\\n')\n            acquire.assert_called",s,flags=re.S)
s=s.replace("['--lines', '1:1', '--json', 'named']","['--lines', '1:1', 'named']")
p.write_text(s)
p=Path('tests/integration/test_cli.py');s=p.read_text().replace('import json\n','');a=s.index('    def test_json_matrix');b=s.index('    def invoke(',a)
s=s[:a]+'''    def test_removed_json_usage_even_on_missing_or_undecodable_file(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / 'bad.txt'
            bad.write_bytes(b'valid\\n\\xff')
            for path in [bad, Path(directory) / 'missing.txt']:
                for option in ['--json', '--json=true', '--j']:
                    for args in [[option, str(path)], [str(path), option],
                                 ['--keep-bom', '--lines=1:1', str(path), option]]:
                        result = self.invoke(*args)
                        self.assertEqual((result.returncode, result.stdout), (2, ''))
                        self.assertIn('usage:', result.stderr)
                        self.assertIn('error:', result.stderr)
                        self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(bad.read_bytes(), b'valid\\n\\xff')
        help_result = self.invoke('--help')
        self.assertEqual((help_result.returncode, help_result.stderr), (0, ''))
        self.assertNotIn('--json', help_result.stdout)
        for flag in ['--keep-bom', '--lines', 'INPUT']:
            self.assertIn(flag, help_result.stdout)

    def test_literal_json_filename_in_whole_and_range_modes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '--json'
            raw = b'alpha beta\\nbeta'
            path.write_bytes(raw)
            for args, expected in [(['--', '--json'], (2, 3)),
                                   (['--lines', '2:2', '--', '--json'], (1, 1)),
                                   (['--keep-bom', '--lines=1:1', '--', '--json'], (1, 2))]:
                result = self.invoke(*args, cwd=directory)
                self.assertEqual((result.returncode, result.stdout, result.stderr),
                                 (0, f'lines={expected[0]} words={expected[1]}\\n', ''))
                self.assertEqual(path.read_bytes(), raw)

'''+s[b:]
s=s.replace("('a\\n\\n', (2, 1), (2, 1))]","('a\\n\\n', (2, 1), (2, 1)), ('a\\ufeffb', (1, 1), (1, 1))]")
# Specialize only range test methods to the retained text contract.
a=s.index('class RangeModuleTests');prefix=s[:a];tail=s[a:]
class TextOnly(ast.NodeTransformer):
 def visit_For(self,node):
  if isinstance(node.target,ast.Name) and node.target.id=='json_mode':
   return [self.visit(x) for x in node.body]
  return self.generic_visit(node)
 def visit_Name(self,node):
  return ast.copy_location(ast.Constant(False),node) if isinstance(node.ctx,ast.Load) and node.id=='json_mode' else node
 def visit_If(self,node):
  node=self.generic_visit(node)
  if isinstance(node.test,ast.Constant):return node.body if node.test.value else node.orelse
  return node
 def visit_IfExp(self,node):
  node=self.generic_visit(node)
  if isinstance(node.test,ast.Constant):return node.body if node.test.value else node.orelse
  return node
ast_tail=TextOnly().visit(ast.parse(tail));ast.fix_missing_locations(ast_tail)
tail=ast.unparse(ast_tail)+'\n';tail=tail.replace('def assert_counts(self, result, expected, json_mode):','def assert_counts(self, result, expected):').replace(', False)', ')').replace(', json_mode=False', '').replace('text_json_and_bom','text_and_bom')
tail=tail.replace("[[], ['--json'], ['--keep-bom'], ['--keep-bom', '--json']]","[[], ['--keep-bom']]").replace("['-sample', '--lines', '-']","['-sample', '--lines', '--json', '-']")
p.write_text(prefix+tail)
p=Path('tests/integration/test_distribution.py');s=p.read_text();a=s.index('    def test_checker_rejects_json_wrong_types');b=s.index('    def test_checker_rejects_ignored_range',a);s=s[:a]+'''    def test_checker_rejects_silently_accepted_removed_json_option(self):
        self._assert_range_mutation_rejected(
            b"    parser.add_argument('--keep-bom'",
            b"    parser.add_argument('--json', action='store_true')\\n    parser.add_argument('--keep-bom'")

'''+s[b:];p.write_text(s)
print('Removal tests and retained text/range/lifetime coverage prepared; production unchanged.')
