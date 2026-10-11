from pathlib import Path
path=Path('tests/unit/test_cli.py')
text=path.read_text().replace('import io\n', 'import io\nimport json\n',1)
insert='''    def test_json_success_composes_with_bom_and_option_order(self):
        for args, policy in [(["--json", "named"], True),
                             (["named", "--json"], True),
                             (["--json", "--keep-bom", "named"], False),
                             (["--keep-bom", "named", "--json"], False),
                             (["named", "--json", "--keep-bom"], False)]:
            with self.subTest(args=args):
                out, err = io.StringIO(), io.StringIO()
                with patch("textstats.cli.count_file", return_value=TextStats(3, 4)) as counter:
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main(args)
                self.assertEqual((status, err.getvalue()), (0, ""))
                self.assertEqual(out.getvalue().count("\\n"), 1)
                self.assertTrue(out.getvalue().endswith("\\n"))
                value = json.loads(out.getvalue())
                self.assertEqual(value, {"lines": 3, "words": 4})
                self.assertTrue(all(type(count) is int for count in value.values()))
                counter.assert_called_once_with("named", strip_bom=policy)

    def test_json_input_failures_retain_empty_stdout_and_status(self):
        for failure in [PermissionError("controlled unreadable"), OSError("controlled read failure"),
                        UnicodeDecodeError("utf-8", b"\\xff", 0, 1, "invalid start byte")]:
            with self.subTest(failure=type(failure).__name__):
                out, err = io.StringIO(), io.StringIO()
                with patch("textstats.cli.count_file", side_effect=failure):
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main(["--json", "affected.txt"])
                self.assertEqual((status, out.getvalue()), (1, ""))
                self.assertIn("affected.txt", err.getvalue())
                self.assertIn(str(failure), err.getvalue())
                self.assertNotIn("Traceback", err.getvalue())

    def test_json_usage_validates_before_acquisition(self):
        for args in [["--json"], ["--json", "one", "two"],
                     ["--json", "--unknown", "missing"], ["--j", "missing"]]:
            with self.subTest(args=args):
                out, err = io.StringIO(), io.StringIO()
                with patch("textstats.cli.count_file") as counter:
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main(args)
                counter.assert_not_called()
                self.assertEqual((status, out.getvalue()), (2, ""))
                self.assertIn("usage:", err.getvalue())
                self.assertIn("error:", err.getvalue())

'''
text=text.replace('class CliTests(unittest.TestCase):\n', 'class CliTests(unittest.TestCase):\n'+insert,1)
text=text.replace("self.assertIn('--keep-bom', out.getvalue())", "self.assertIn('--keep-bom', out.getvalue())\n            self.assertIn('--json', out.getvalue())",1)
path.write_text(text)
path=Path('tests/integration/test_cli.py')
text=path.read_text().replace('import os\n','import os\nimport json\n',1)
insert='''    def test_json_semantic_matrix_and_option_composition(self):
        cases = [("", (0, 0), (0, 0)), ("alpha beta", (1, 2), (1, 2)),
                 ("alpha\\n", (1, 1), (1, 1)), ("\\n", (1, 0), (1, 0)),
                 ("α\\r\\n猫\\rβ γ\\n", (3, 4), (3, 4)), ("alpha\\n\\n", (2, 1), (2, 1)),
                 (" \\t", (1, 0), (1, 0)), ("alpha\\u2028beta", (1, 2), (1, 2)),
                 ("\\ufeff", (0, 0), (1, 1)), ("\\ufeff\\ufeff", (1, 1), (1, 1)),
                 ("\\ufeffalpha beta", (1, 2), (1, 2)), ("a\\ufeffb", (1, 1), (1, 1)),
                 ("\\r\\n", (1, 0), (1, 0)), ("\\r", (1, 0), (1, 0))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            for text, default, retained in cases:
                raw = text.encode("utf-8")
                path.write_bytes(raw)
                choices = [(["--json", str(path)], True, default),
                           ([str(path), "--json"], True, default),
                           (["--json", "--keep-bom", str(path)], False, retained),
                           (["--keep-bom", str(path), "--json"], False, retained),
                           ([str(path), "--json", "--keep-bom"], False, retained)]
                for args, policy, expected in choices:
                    with self.subTest(text=text, args=args):
                        result = self.invoke(*args)
                        self.assertEqual((result.returncode, result.stderr), (0, ""))
                        self.assertEqual(result.stdout.count("\\n"), 1)
                        self.assertTrue(result.stdout.endswith("\\n"))
                        value = json.loads(result.stdout)
                        self.assertEqual(set(value), {"lines", "words"})
                        self.assertTrue(all(type(count) is int for count in value.values()))
                        self.assertEqual((value["lines"], value["words"]), expected)
                        self.assertEqual(count_file(path, strip_bom=policy), TextStats(*expected))
                        text_result = self.invoke(*([] if policy else ["--keep-bom"]), str(path))
                        self.assertEqual((text_result.returncode, text_result.stdout, text_result.stderr),
                                         (0, f"lines={expected[0]} words={expected[1]}\\n", ""))
                        self.assertEqual(path.read_bytes(), raw)

    def test_json_errors_retain_status_streams_and_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "bad.txt"
            bad.write_bytes(b"valid prefix\\n\\xff")
            for path, cause in [(bad, "utf-8"), (bad.with_name("absent.txt"), "No such file")]:
                for options in [["--json"], ["--keep-bom", "--json"]]:
                    with self.subTest(path=path, options=options):
                        result = self.invoke(*options, str(path))
                        self.assertEqual((result.returncode, result.stdout), (1, ""))
                        self.assertIn(str(path), result.stderr)
                        self.assertIn(cause, result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(bad.read_bytes(), b"valid prefix\\n\\xff")
        for args in [["--json"], ["--json", "one", "two"],
                     ["--json", "--unknown", "missing"], ["--j", "missing"]]:
            result = self.invoke(*args)
            self.assertEqual((result.returncode, result.stdout), (2, ""))
            self.assertIn("usage:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_json_option_like_filename_after_double_dash(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "--json"
            path.write_bytes(b"alpha beta\\n")
            result = self.invoke("--json", "--", "--json", cwd=directory)
            self.assertEqual((result.returncode, result.stderr), (0, ""))
            self.assertEqual(json.loads(result.stdout), {"lines": 1, "words": 2})
            text_result = self.invoke("--", "--json", cwd=directory)
            self.assertEqual((text_result.returncode, text_result.stdout, text_result.stderr),
                             (0, "lines=1 words=2\\n", ""))
            self.assertEqual(path.read_bytes(), b"alpha beta\\n")

'''
text=text.replace('class ModuleCliTests(unittest.TestCase):\n','class ModuleCliTests(unittest.TestCase):\n'+insert,1)
text=text.replace("self.assertIn('--keep-bom', result.stdout)", "self.assertIn('--keep-bom', result.stdout)\n            self.assertIn('--json', result.stdout)",1)
path.write_text(text)
