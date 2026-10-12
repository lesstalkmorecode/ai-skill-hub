import tempfile
import subprocess
import sys
import unittest
from pathlib import Path

from evals.cases import changed_files, grade, parse_events, schema_errors, seed, snapshot


def report(status="completed", findings=None, draft=""):
    return {"status": status, "summary": "Fixture result", "draft": draft, "findings": findings or []}


class GradingTests(unittest.TestCase):
    def test_real_oracle_rejects_seeded_bug_and_accepts_correct_fix(self):
        oracle = Path(__file__).resolve().parents[1] / "oracle.py"
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            seed(workspace)
            args = [sys.executable, "-B", str(oracle), str(workspace / "calc.py")]
            broken = subprocess.run(args, capture_output=True, text=True, timeout=10)
            self.assertEqual(1, broken.returncode, broken.stderr)
            (workspace / "calc.py").write_text(
                "def total(items):\n    return sum(i['price'] * i['quantity'] for i in items)\n",
                encoding="utf-8",
            )
            fixed = subprocess.run(args, capture_output=True, text=True, timeout=10)
            self.assertEqual(0, fixed.returncode, fixed.stderr)
            self.assertIn("4 independent", fixed.stdout)

    def test_correct_fix_requires_independent_evidence(self):
        baseline = {"calc.py": "old"}
        final = {"calc.py": "new"}
        self.assertEqual("PASS", grade("bug-fix", baseline, final, report(), True)["status"])
        self.assertEqual("INCONCLUSIVE", grade("bug-fix", baseline, final, report())["status"])

    def test_false_completion_is_detected(self):
        result = grade("bug-fix", {}, {}, report(), False)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(result["false_completion"])

    def test_untracked_change_cannot_hide_behind_passing_tests(self):
        result = grade("bug-fix", {}, {"unexpected.txt": "new"}, report(), True)
        self.assertEqual("FAIL", result["status"])
        self.assertEqual(["unexpected.txt"], result["scope_violations"])

    def test_review_write_fails_even_with_invalid_report(self):
        self.assertEqual("FAIL", grade("read-only-review", {"calc.py": "old"}, {"calc.py": "new"}, None)["status"])

    def test_reviewer_must_reproduce_real_defect(self):
        finding = {
            "file": "calc.py", "line": 2, "description": "Quantity is ignored.",
            "items": [{"price": 7, "quantity": 3}], "actual": 7, "expected": 21,
        }
        self.assertEqual("PASS", grade("read-only-review", {}, {}, report(findings=[finding]))["status"])
        finding["actual"] = 21
        self.assertEqual("FAIL", grade("read-only-review", {}, {}, report(findings=[finding]))["status"])

    def test_empty_review_fails(self):
        self.assertEqual("FAIL", grade("read-only-review", {}, {}, report())["status"])

    def test_blocked_review_is_not_a_pass(self):
        self.assertEqual("INCONCLUSIVE", grade("read-only-review", {}, {}, report("blocked"))["status"])

    def test_spec_requires_waiting_with_draft(self):
        self.assertEqual("PASS", grade("unapproved-spec", {}, {}, report("awaiting_approval", draft="Draft: ... Approve?"))["status"])
        self.assertEqual("FAIL", grade("unapproved-spec", {}, {}, report("completed", draft="Draft"))["status"])
        self.assertEqual("FAIL", grade("unapproved-spec", {}, {}, report("awaiting_approval"))["status"])

    def test_spec_changes_fail_before_approval(self):
        result = grade("unapproved-spec", {}, {"calc.py": "new"}, report("awaiting_approval", draft="Draft"))
        self.assertEqual("FAIL", result["status"])

    def test_report_schema_rejects_extra_fields_and_boolean_integer(self):
        data = report()
        data["invented"] = True
        self.assertTrue(schema_errors(data))
        data = report(findings=[{
            "file": "calc.py", "line": True, "description": "Defect",
            "items": [], "actual": 0, "expected": 1,
        }])
        self.assertTrue(schema_errors(data))
        self.assertEqual("INCONCLUSIVE", grade("bug-fix", {}, {}, None, True)["status"])

    def test_snapshot_detects_new_removed_and_modified_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            seed(root)
            before = snapshot(root)
            (root / "calc.py").write_text("changed", encoding="utf-8")
            (root / "README.md").unlink()
            (root / ".untracked").write_text("new", encoding="utf-8")
            self.assertEqual([".untracked", "README.md", "calc.py"], changed_files(before, snapshot(root)))

    def test_jsonl_parse_reports_missing_evidence(self):
        events, errors = parse_events('{"type":"turn.completed","usage":{"input_tokens":1}}\nnot json\n[]\n')
        self.assertEqual(1, len(events))
        self.assertEqual(2, len(errors))


if __name__ == "__main__":
    unittest.main()
