import tempfile
import unittest
from pathlib import Path

from evals.validate import ROOT, frontmatter, link_errors, maintained_files, package_errors, validate


class PackageValidationTests(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual([], validate(ROOT))

    def test_frontmatter_rejects_duplicate_missing_and_nonstring_values(self):
        for value in (
            "no frontmatter",
            "---\nname: demo\n---",
            "---\nname: demo\nname: second\ndescription: A task\n---",
            "---\nname: demo\ndescription: null\n---",
            "---\nname: demo\ndescription: [nested]\n---",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                frontmatter(value)

    def test_frontmatter_accepts_current_profile(self):
        self.assertEqual("demo", frontmatter("---\nname: demo\ndescription: Do a task.\n---")["name"])

    def test_broken_and_escaping_links_are_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.md"
            (root / "target.md").write_text("# Known heading\n", encoding="utf-8")
            source.write_text(
                "[valid](target.md#known-heading)\n[bad](target.md#missing)\n"
                "[absent](absent.md)\n[escape](../elsewhere.md)\n"
                "[external](https://example.invalid/)\n```text\n[example](not-real.md)\n```\n",
                encoding="utf-8",
            )
            errors = link_errors(root, source)
            self.assertEqual(3, len(errors), errors)

    def test_distribution_rejects_private_data(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("learning/lesson.md", ".codex/auth.json", ".env", "evals/results/run.json"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("synthetic", encoding="utf-8")
            (root / "plugin.json").write_text("{}", encoding="utf-8")
            errors = package_errors(root)
            for name in ("lesson.md", "auth.json", ".env", "run.json"):
                self.assertTrue(any(name in error for error in errors), name)

    def test_adapter_drift_and_broken_role_are_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for source in maintained_files(ROOT):
                target = root / source.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
            adapter = root / ".codex/agents/reviewer.toml"
            adapter.write_text(adapter.read_text(encoding="utf-8") + "\n# Drift\n", encoding="utf-8")
            (root / "agents/reviewer.md").unlink()
            errors = validate(root)
            self.assertTrue(any("definitions differ" in error for error in errors), errors)
            self.assertTrue(any("missing or mismatched role" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
