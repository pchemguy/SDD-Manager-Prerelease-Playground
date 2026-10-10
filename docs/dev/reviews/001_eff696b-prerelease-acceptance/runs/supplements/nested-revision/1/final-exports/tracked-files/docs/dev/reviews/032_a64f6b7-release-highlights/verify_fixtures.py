"""Exercise the shipped Git recipe and local file mechanics, without a publisher.

Run from the repository root with Python 3.11+. The file-mechanics checks are
explicit demonstrations of the instruction contract, not an agent acceptance
test or a shipped draft-management implementation. All repositories are local
and disposable; no token, hosted release or remote service is used.
"""

import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path("skills/sdd-forge/references/release-highlights.md")
RECIPE = re.search(r"```python\n(.*?)\n```", SOURCE.read_text(), re.S).group(1)


class GitRecipeCases(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="sdd032-fixture-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Local fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.root = self.commit("Initial product")

    def git(self, *args, repo=None, check=True):
        result = subprocess.run(["git", *args], cwd=repo or self.repo,
                                text=True, capture_output=True, check=check)
        return result.stdout.strip()

    def commit(self, message):
        self.git("commit", "--allow-empty", "-q", "-m", message)
        return self.git("rev-parse", "HEAD")

    def collect(self, repo=None, ok=True, **values):
        env = {k: v for k, v in os.environ.items() if not k.startswith("RELEASE_")}
        env.update(values)
        result = subprocess.run([sys.executable, "-B", "-c", RECIPE],
                                cwd=repo or self.repo, env=env, text=True,
                                capture_output=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(result.stdout, "Failure must not emit usable partial JSON")
        return result.stderr

    def test_annotated_and_lightweight_tags(self):
        self.git("tag", "-a", "v1.2.3", "-m", "Release", self.root)
        target = self.commit("Fix exports\n\nKeep a complete message body.")
        annotated = self.collect()
        self.git("tag", "-d", "v1.2.3")
        self.git("tag", "v1.2.3", self.root)
        self.assertEqual(self.collect(), annotated)
        self.assertEqual(annotated["release_commit"], self.root)
        self.assertEqual(annotated["analyzed_through_commit"], target)
        self.assertIn("Keep a complete message body.", annotated["commits"][0]["message"])

    def test_channel_and_unrelated_tags(self):
        self.git("tag", "v1.2.3", self.root)
        self.git("switch", "-q", "-c", "unrelated")
        unrelated = self.commit("Unreleased side line")
        self.git("tag", "v99.0.0", unrelated)
        self.git("switch", "-q", "main")
        target = self.commit("Current change")
        self.git("tag", "v2.0.0-rc.1", target)
        self.git("tag", "v1-spec-plan-implement", target)
        self.assertEqual(self.collect()["release_tag"], "v1.2.3")

    def test_nearest_ancestry_not_largest_version(self):
        self.git("tag", "v9.0.0", self.root)
        nearer = self.commit("Backport release line")
        self.git("tag", "v1.2.3", nearer)
        self.commit("New backport")
        self.assertEqual(self.collect()["release_commit"], nearer)

    def test_merged_messages_and_repeated_text(self):
        self.git("tag", "v1.2.3", self.root)
        self.git("switch", "-q", "-c", "feature")
        side = self.commit("Repeated subject\n\nMerged feature body.")
        self.git("switch", "-q", "main")
        direct = self.commit("Repeated subject")
        self.git("merge", "-q", "--no-ff", "feature", "-m", "Integrate feature")
        target = self.git("rev-parse", "HEAD")
        records = self.collect()["commits"]
        self.assertEqual({r["commit"] for r in records}, {side, direct, target})
        self.assertEqual(len(records), 3)
        self.assertEqual(records[-1]["commit"], target)
        self.assertTrue(any("Merged feature body." in r["message"] for r in records))

    def test_initial_release_and_nonrelease_tags(self):
        self.git("tag", "design-checkpoint", self.root)
        target = self.commit("First feature")
        evidence = self.collect()
        self.assertIsNone(evidence["release_tag"])
        self.assertIsNone(evidence["release_commit"])
        self.assertEqual({r["commit"] for r in evidence["commits"]}, {self.root, target})

    def test_shallow_history(self):
        self.commit("New feature")
        shallow = Path(self.tmp.name) / "shallow"
        self.git("clone", "-q", "--depth=1", self.repo.as_uri(), str(shallow))
        self.assertIn("Incomplete shallow history", self.collect(repo=shallow, ok=False))

    def test_missing_explicit_object(self):
        self.collect(ok=False, RELEASE_BASE_TAG="absent")

    def test_empty_range(self):
        self.git("tag", "v1.2.3", self.root)
        self.assertEqual(self.collect()["commits"], [])

    def test_pending_tag_cannot_be_previous_baseline(self):
        self.git("tag", "v1.2.3", self.root)
        target = self.commit("Next release feature")
        self.git("tag", "v1.2.4", target)
        evidence = self.collect(RELEASE_PENDING_TAG="v1.2.4")
        self.assertEqual(evidence["release_tag"], "v1.2.3")
        self.assertEqual(evidence["commits"][0]["commit"], target)
        self.collect(ok=False, RELEASE_PENDING_TAG="v1.2.4", RELEASE_BASE_TAG="v1.2.4")

    def test_side_history_requires_policy_then_explicit_baseline(self):
        self.git("switch", "-q", "-c", "side")
        side = self.commit("Side release")
        self.git("tag", "v1.2.3", side)
        self.git("switch", "-q", "main")
        self.commit("Main feature")
        self.git("merge", "-q", "--no-ff", "side", "-m", "Merge side")
        self.assertIn("Assess side-history", self.collect(ok=False))
        self.assertEqual(self.collect(RELEASE_BASE_TAG="v1.2.3")["release_commit"], side)

    def test_multiple_tags_require_selection(self):
        self.git("tag", "v1.2.3", self.root)
        self.git("tag", "1.2.3", self.root)
        self.assertIn("Select an explicit baseline", self.collect(ok=False))
        self.assertEqual(self.collect(RELEASE_BASE_TAG="v1.2.3")["release_commit"], self.root)

    def test_unrelated_explicit_baseline_rejected(self):
        self.git("switch", "-q", "-c", "side")
        side = self.commit("Side-only release")
        self.git("tag", "v1.2.3", side)
        self.git("switch", "-q", "main")
        self.commit("Independent main change")
        self.collect(ok=False, RELEASE_BASE_TAG="v1.2.3")

    def test_increment_records_revert_and_ancestry_guards(self):
        self.git("tag", "v1.2.3", self.root)
        analyzed = self.commit("Add optional export")
        target = self.commit('Revert "Add optional export"\n\nRemove the optional export.')
        ids = self.git("rev-list", "--reverse", "--topo-order", analyzed + ".." + target).splitlines()
        self.assertEqual(ids, [target])
        self.assertIn("Remove the optional export.", self.git("show", "-s", "--format=%B", target))
        self.assertEqual(self.git("rev-list", analyzed + ".." + analyzed), "")
        self.git("merge-base", "--is-ancestor", self.root, analyzed)
        self.git("merge-base", "--is-ancestor", analyzed, target)
        self.git("tag", "-f", "v1.2.3", target)
        self.assertNotEqual(self.git("rev-parse", "refs/tags/v1.2.3^{commit}"), self.root)
        self.git("switch", "-q", "-c", "diverged", self.root)
        diverged = self.commit("Other line")
        result = subprocess.run(["git", "merge-base", "--is-ancestor", analyzed, diverged], cwd=self.repo)
        self.assertEqual(result.returncode, 1)

    def test_ignored_draft_is_absent_from_fresh_clone(self):
        (self.repo / ".gitignore").write_text("/.release-highlights.md\n")
        self.git("add", ".gitignore")
        self.git("commit", "-q", "-m", "Ignore owned draft")
        draft = self.repo / ".release-highlights.md"
        draft.write_text("---\nrelease_tag: null\nrelease_commit: null\n---\nCurated notes\n")
        self.git("check-ignore", "-q", ".release-highlights.md")
        self.assertEqual(self.git("ls-files", "--", ".release-highlights.md"), "")
        clone = Path(self.tmp.name) / "consumer"
        self.git("clone", "-q", "--no-hardlinks", str(self.repo), str(clone))
        self.assertFalse((clone / draft.name).exists())


class FileMechanicsCases(unittest.TestCase):
    """Demonstrate atomic save/body transfer/retention with fixed edited prose.

    These cases do not implement or test a semantic agent, a YAML parser,
    source selection, or an actual provider. Fixed decisions are illustrative.
    """

    def test_atomic_save_interruption_and_curated_body(self):
        with tempfile.TemporaryDirectory(prefix="sdd032-draft-") as directory:
            draft = Path(directory) / ".release-highlights.md"
            original = '---\nrelease_tag: "v1.2.3"\nanalyzed_through_commit: "old"\n---\nHuman edit; minor bullet deliberately cut.\n'
            draft.write_text(original)
            candidate = Path(directory) / ".owned-candidate"
            candidate.write_text("Incomplete analysis")
            candidate.unlink()  # Simulated interruption: do not replace or advance.
            self.assertEqual(draft.read_text(), original)
            body = "Human edit; minor bullet deliberately cut.\nUpdated consequential fix.\n"
            complete = '---\nrelease_tag: "v1.2.3"\nanalyzed_through_commit: "new"\n---\n' + body
            candidate.write_text(complete)
            os.replace(candidate, draft)
            self.assertEqual(draft.read_text(), complete)
            final_body = draft.read_text().split("\n---\n", 1)[1]
            self.assertEqual(final_body, body)
            notes = "Installation: keep human guidance.\n\n" + final_body
            transfer = json.loads(json.dumps({"notes": notes}))
            self.assertEqual(transfer["notes"], notes)
            self.assertNotIn("analyzed_through_commit", notes)

    def test_retention_and_idempotent_owned_cleanup(self):
        with tempfile.TemporaryDirectory(prefix="sdd032-cleanup-") as directory:
            draft = Path(directory) / ".release-highlights.md"
            draft.write_text("Curated highlights\n")
            # Fixed decision matrix, not a provider integration test.
            for published, body_matches, owned, tracked, retain in [
                (False, True, True, False, False),  # Draft/preparation.
                (True, False, True, False, False),  # Missing/mismatched readback.
                (False, False, True, False, False),  # Failed/uncertain.
                (True, True, False, False, False),  # Foreign ownership.
                (True, True, True, True, False),    # Tracked file.
                (True, True, True, False, True),    # Explicit retention.
            ]:
                eligible = published and body_matches and owned and not tracked and not retain
                self.assertFalse(eligible)
                self.assertTrue(draft.exists())
            draft.unlink()  # All required conditions deliberately established locally.
            draft.unlink(missing_ok=True)
            self.assertFalse(draft.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
