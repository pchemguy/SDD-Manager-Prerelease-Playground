"""Run the documented collection recipe in disposable real Git fixtures.

Mechanical coverage only: this script does not assess semantic curation,
agent compliance, public release publication, or historical campaign records.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[5]
RECIPE = re.search(r"```python\n(.*?)\n```", (ROOT / "skills/sdd-forge/references/release-highlights.md").read_text(), re.S).group(1)


class CollectionChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="sdd040-highlights-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.base = self.change("base", "Initial fixture")
        self.git("tag", "-a", "v1.0.0", "-m", "Baseline")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.repo, text=True, stderr=subprocess.DEVNULL).strip()

    def change(self, name, message):
        (self.repo / name).write_text(message)
        self.git("add", name)
        self.git("commit", "-m", message)
        return self.git("rev-parse", "HEAD")

    def collect(self, **values):
        env = {k: v for k, v in os.environ.items() if not k.startswith("RELEASE_")}
        env.update(values)
        result = subprocess.run([sys.executable, "-c", RECIPE], cwd=self.repo, env=env, text=True, capture_output=True)
        return result, json.loads(result.stdout) if result.returncode == 0 else None

    def valid(self, **values):
        result, data = self.collect(**values)
        self.assertEqual(result.returncode, 0, result.stderr)
        selected = self.git("rev-list", "--reverse", "--topo-order", (data["range_start_commit"] + ".." if data["range_start_commit"] else "") + data["analyzed_through_commit"]).splitlines()
        self.assertEqual([r["commit"] for r in data["commits"]], selected)
        for record in data["commits"]:
            self.assertEqual(record["parents"], self.git("show", "-s", "--format=%P", record["commit"]).split())
            self.assertEqual("message" in record or record.get("message_deferred", False), len(record["parents"]) > 1)
            if "message" in record:
                self.assertEqual(record["message"].strip(), self.git("show", "-s", "--format=%B", record["commit"]))
        return data

    def test_direct_gap_and_full_message_fallback(self):
        oid = self.change("direct", "Direct compatibility change\n\nMeaningful body beyond the subject")
        data = self.valid()
        self.assertEqual(data["release_commit"], self.base)
        self.assertEqual(data["commits"][0]["commit"], oid)
        self.assertNotIn("message", data["commits"][0])
        self.assertIn("Meaningful body", self.git("show", "-s", "--format=%B", oid))

    def test_nested_merges_survive_deleted_and_moved_branch_tips(self):
        self.git("switch", "-c", "revision/outer")
        outer = self.change("outer", "Outer change")
        self.git("switch", "-c", "revision/child")
        self.change("child", "Nested outcome")
        self.git("switch", "revision/outer")
        self.git("merge", "--no-ff", "revision/child", "-m", "Merge nested revision\n\nDelivered: nested outcome")
        nested = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "revision/outer", "-m", "Merge enclosing revision\n\nDelivered: outer and nested outcomes")
        enclosing = self.git("rev-parse", "HEAD")
        self.git("branch", "-D", "revision/child")
        self.git("branch", "-f", "revision/outer", self.base)
        data = self.valid()
        self.assertEqual({r["commit"] for r in data["commits"] if "message" in r}, {nested, enclosing})
        self.assertIn(outer, {r["commit"] for r in data["commits"]})
        self.assertNotIn(nested, self.git("rev-list", "--first-parent", "HEAD").splitlines())

    def test_cumulative_amendment_increment_keeps_baseline(self):
        self.git("switch", "-c", "revision/amend")
        self.change("original", "Original outcome")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "revision/amend", "-m", "Merge revision 040_aabbccd Original campaign\n\nDelivered: original outcome")
        analyzed = self.git("rev-parse", "HEAD")
        self.git("switch", "revision/amend")
        self.git("merge", "--ff-only", "main")
        delta = self.change("amendment", "New amendment delta")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "revision/amend", "-m", "Merge revision 040_aabbccd Campaign amendment\n\nRetained: original outcome\nDelta: new amendment")
        full = self.valid()
        old_merge = next(r for r in full["commits"] if r["commit"] == analyzed)
        self.assertTrue(old_merge["message_deferred"])
        self.assertNotIn("message", old_merge)
        self.assertIn("Retained: original", full["commits"][-1]["message"])
        data = self.valid(RELEASE_ANALYZED_COMMIT=analyzed)
        self.assertEqual(data["release_commit"], self.base)
        self.assertEqual(data["range_start_commit"], analyzed)
        self.assertEqual(len(data["commits"]), 2)
        self.assertEqual(data["commits"][0]["commit"], delta)
        self.assertIn("Retained: original", data["commits"][1]["message"])

    def test_pending_tag_empty_initial_and_lightweight_baselines(self):
        data = self.valid()
        self.assertEqual(data["commits"], [])
        oid = self.change("next", "Next outcome")
        self.git("tag", "v1.1.0")
        data = self.valid(RELEASE_PENDING_TAG="v1.1.0")
        self.assertEqual(data["release_commit"], self.base)
        self.assertEqual(len(data["commits"]), 1)
        self.assertEqual(self.valid()["release_commit"], oid)
        self.git("tag", "-d", "v1.0.0", "v1.1.0")
        initial = self.valid()
        self.assertIsNone(initial["release_commit"])
        self.assertEqual(len(initial["commits"]), 2)

    def test_pending_tag_cannot_be_explicit_baseline(self):
        result, _ = self.collect(RELEASE_PENDING_TAG="v1.0.0", RELEASE_BASE_TAG="v1.0.0")
        self.assertNotEqual(result.returncode, 0)

    def test_direct_revert_is_in_increment_inventory(self):
        original = self.change("original", "Original public change")
        self.git("revert", "--no-edit", original)
        data = self.valid(RELEASE_ANALYZED_COMMIT=original)
        self.assertEqual(len(data["commits"]), 1)
        self.assertIn("Revert", data["commits"][0]["subject"])
        self.assertNotIn("message", data["commits"][0])

    def test_wrong_increment_ancestry_and_shallow_history_fail(self):
        self.git("switch", "--orphan", "unrelated")
        unrelated = self.change("unrelated", "Unrelated root")
        self.git("switch", "main")
        self.assertNotEqual(self.collect(RELEASE_ANALYZED_COMMIT=unrelated)[0].returncode, 0)
        shallow = Path(self.tmp.name) / "shallow"
        subprocess.run(["git", "clone", "--depth=1", "--branch", "main", self.repo.as_uri(), str(shallow)], check=True, capture_output=True)
        old = self.repo
        self.repo = shallow
        try:
            self.assertNotEqual(self.collect()[0].returncode, 0)
        finally:
            self.repo = old

    def test_ambiguous_campaign_subject_keeps_full_message(self):
        self.git("switch", "-c", "revision/ambiguous")
        self.change("change", "Ambiguous change")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "revision/ambiguous", "-m", "Merge campaign 040 plus campaign 041\n\nReview: ambiguous subject")
        data = self.valid()
        self.assertIsNone(data["commits"][-1]["campaign_hint"])
        self.assertIn("message", data["commits"][-1])

    def test_phase_and_document_preparation_integrations(self):
        expected = set()
        for branch in ["design-docs/main", "design-docs/040-docs", "phase/1-delivery"]:
            self.git("switch", "-c", branch)
            self.change(branch.replace("/", "-"), "Scope for " + branch)
            self.git("switch", "main")
            self.git("merge", "--no-ff", branch, "-m", "Merge " + branch + "\n\nScope: accepted preparation or verified phase")
            expected.add(self.git("rev-parse", "HEAD"))
            self.git("branch", "-D", branch)
        data = self.valid()
        self.assertEqual({r["commit"] for r in data["commits"] if "message" in r}, expected)

    def test_side_history_release_tag_requires_policy(self):
        self.git("switch", "-c", "feature/tag")
        self.change("side", "Side change")
        self.git("tag", "v1.2.0")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "feature/tag", "-m", "Merge side release")
        self.assertNotEqual(self.collect()[0].returncode, 0)
        self.assertEqual(self.valid(RELEASE_BASE_TAG="v1.0.0")["release_commit"], self.base)


if __name__ == "__main__":
    unittest.main(verbosity=2)
