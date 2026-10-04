"""Stdlib tests for scripts/omnisync.py. Run: python -m unittest discover -s tests"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import omnisync as o  # noqa: E402


class Blocks(unittest.TestCase):
    def test_insert_after_h1_and_idempotent(self):
        text = "---\nid: x\n---\n# Title\n\nBody\n"
        once = o.upsert_block(text, "core", "hello")
        self.assertIn("<!-- omni:begin core", once)
        self.assertLess(once.index("# Title"), once.index("omni:begin"))
        self.assertEqual(once, o.upsert_block(once, "core", "hello"))

    def test_replace_existing_block_only(self):
        text = o.upsert_block("# T\n\nmine\n", "core", "old")
        new = o.upsert_block(text, "core", "new")
        self.assertIn("new", new)
        self.assertNotIn("\nold\n", new)
        self.assertIn("mine", new)


class Parsing(unittest.TestCase):
    def test_roadmap_table_and_checklist(self):
        md = ("| Ref | Item | Status | Owner |\n|---|---|---|---|\n| A-1 | Do it | todo | Human |\n"
              "| A-2 | Done | done | Computer |\n\n- [ ] idea one\n- [x] shipped\n")
        items = o.roadmap_items("demo", md)
        self.assertEqual([i["key"] for i in items[:2]], ["demo:A-1", "demo:A-2"])
        self.assertTrue(items[0]["open"])
        self.assertFalse(items[1]["open"])
        self.assertEqual(sum(1 for i in items if i["source"] == "checklist" and i["open"]), 1)

    def test_phase_table(self):
        items = o.roadmap_items("qc", "| Phase | Scope | Status |\n|---|---|---|\n| 7 | Validate | Next |\n")
        self.assertEqual(items[0]["key"], "qc:P7")

    def test_brain_facts(self):
        md = "# B\n## Facts learned\n- one\n- two\n## Other\n- no\n"
        self.assertEqual(o.brain_facts(md), ["one", "two"])


class Safety(unittest.TestCase):
    def test_secret_names_and_content(self):
        self.assertTrue(o.secret_like(".env.local"))
        self.assertTrue(o.secret_like("config/MASTER.env"))
        self.assertFalse(o.secret_like("BRAIN.md"))
        self.assertTrue(o.SECRET_CONTENT.search("token ghp_" + "a" * 30))

    def test_dollar_quote_cannot_break_out(self):
        s = "x $kb$ y"
        q = o.dq(s)
        self.assertTrue(q.startswith("$kbx$") and q.endswith("$kbx$"))


class EndToEnd(unittest.TestCase):
    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "demo").mkdir()
            (root / "demo" / "BRAIN.md").write_text("# Demo\n## Facts learned\n- a\n")
            reg = root / "reg.json"
            reg.write_text(json.dumps({"requiredDocs": ["BRAIN.md"], "projects": [
                {"slug": "demo", "name": "Demo", "repo": "x/demo"}]}))
            before = (root / "demo" / "BRAIN.md").read_text()
            o.main(["--registry", str(reg), "inject", "--repos", str(root)])
            self.assertEqual(before, (root / "demo" / "BRAIN.md").read_text())
            o.main(["--registry", str(reg), "inject", "--repos", str(root), "--apply"])
            self.assertIn("omni:begin core", (root / "demo" / "BRAIN.md").read_text())


if __name__ == "__main__":
    unittest.main()
