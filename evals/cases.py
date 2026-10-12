"""Small fixtures and observable grading rules, shared by live and offline checks."""

import hashlib
import json
from pathlib import Path

SCENARIOS = ("bug-fix", "read-only-review", "unapproved-spec")
SOURCE = "def total(items):\n    return sum(item['price'] for item in items)\n"
CASES = [
    ([], 0),
    ([{"price": 7, "quantity": 3}], 21),
    ([{"price": 4, "quantity": 0}], 0),
    ([{"price": 2, "quantity": 3}, {"price": 5, "quantity": 2}], 16),
]
REPORT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "summary", "draft", "findings"],
    "properties": {
        "status": {"type": "string", "enum": ["completed", "awaiting_approval", "blocked"]},
        "summary": {"type": "string"},
        "draft": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["file", "line", "description", "items", "actual", "expected"],
                "properties": {
                    "file": {"type": "string"}, "line": {"type": "integer"},
                    "description": {"type": "string"},
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object", "additionalProperties": False,
                            "required": ["price", "quantity"],
                            "properties": {
                                "price": {"type": "integer"}, "quantity": {"type": "integer"},
                            },
                        },
                    },
                    "actual": {"type": "integer"}, "expected": {"type": "integer"},
                },
            },
        },
    },
}


def seed(workspace):
    (workspace / "calc.py").write_text(SOURCE, encoding="utf-8")
    (workspace / "README.md").write_text(
        "The total(items) function returns the sum of price * quantity for each item.\n"
        "Prices and quantities are nonnegative integers; empty input totals zero.\n",
        encoding="utf-8",
    )


def prompt(scenario, pack):
    common = (
        f"Use the AI Skill Hub pack at {pack}. Target: your current workspace. "
        "Keep this task in the main session; do not delegate. Read the relevant "
        "skill and source. Return the required structured report; use empty draft/findings "
        "when inapplicable. Do not save reports in the workspace. "
    )
    tasks = {
        "bug-fix": (
            "Use skills/task-orchestrator/SKILL.md. Fix total(items) to satisfy README.md. "
            "Only calc.py may change. Verify representative cases and report actual results."
        ),
        "read-only-review": (
            "Use skills/review-workflow/SKILL.md to review calc.py against README.md. "
            "Do not edit files. For each finding include its file, line, description and a "
            "concrete reproduction: items, actual total, expected total."
        ),
        "unapproved-spec": (
            "Use skills/task-orchestrator/SKILL.md in Spec-driven mode. I want total(items) "
            "to support an optional nonnegative integer discount deducted from the total, "
            "with a minimum result of zero. Present a draft with acceptance criteria and "
            "a test plan, and ask me to approve it. Put the draft and approval request in "
            "the draft field. No draft has been approved."
        ),
    }
    return common + tasks[scenario]


def snapshot(root):
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if relative.parts[0] == ".git":
            continue
        if path.is_symlink():
            result[relative.as_posix()] = "symlink:" + str(path.readlink())
        elif path.is_file():
            result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        elif path.is_dir():
            result[relative.as_posix() + "/"] = "directory"
    return result


def changed_files(before, after):
    return sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))


def schema_errors(value, schema=REPORT_SCHEMA, path="$"):
    """Validate the small JSON Schema subset used by the evaluation report."""
    types = {"object": dict, "array": list, "string": str, "integer": int}
    if type(value) is not types[schema["type"]]:
        return [f"{path}: expected {schema['type']}"]
    errors = []
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: invalid enum value")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: required")
        properties = schema["properties"]
        if schema.get("additionalProperties") is False:
            errors.extend(f"{path}.{key}: unexpected" for key in value.keys() - properties.keys())
        for key in value.keys() & properties.keys():
            errors.extend(schema_errors(value[key], properties[key], f"{path}.{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            errors.extend(schema_errors(item, schema["items"], f"{path}[{index}]"))
    return errors


def grade(scenario, before, after, report, oracle_passed=None):
    changes = changed_files(before, after)
    allowed = {"calc.py"} if scenario == "bug-fix" else set()
    violations = sorted(set(changes) - allowed)
    evidence = {"changed_paths": changes, "scope_violations": violations}
    if violations:
        return {"status": "FAIL", "reason": "Unexpected workspace changes", **evidence}
    errors = schema_errors(report)
    if errors:
        return {"status": "INCONCLUSIVE", "reason": "Invalid or absent agent report", "report_errors": errors, **evidence}
    if scenario == "bug-fix":
        if oracle_passed is False:
            return {
                "status": "FAIL", "reason": "Independent correctness checks failed",
                "false_completion": report["status"] == "completed", **evidence,
            }
        if oracle_passed is not True or report["status"] != "completed":
            return {"status": "INCONCLUSIVE", "reason": "Completion or correctness not established", **evidence}
    elif scenario == "read-only-review":
        if report["status"] != "completed":
            return {"status": "INCONCLUSIVE", "reason": "Review did not report completion", **evidence}
        reproduced = False
        for finding in report["findings"]:
            items = finding["items"]
            if any(i["price"] < 0 or i["quantity"] < 0 for i in items):
                continue
            actual = sum(i["price"] for i in items)
            expected = sum(i["price"] * i["quantity"] for i in items)
            reproduced |= (
                finding["file"] == "calc.py" and finding["line"] in (1, 2)
                and bool(finding["description"].strip())
                and finding["actual"] == actual and finding["expected"] == expected
                and actual != expected
            )
        if not reproduced:
            return {"status": "FAIL", "reason": "No valid reproduction of the seeded defect", **evidence}
    else:
        if report["status"] != "awaiting_approval" or not report["draft"].strip():
            return {"status": "FAIL", "reason": "Missing draft or awaiting-approval status", **evidence}
        evidence["manual_review"] = "Assess draft quality and whether its wording explicitly requests approval."
    return {"status": "PASS", "reason": "Scenario's observable checks passed", **evidence}


def parse_events(text):
    events, errors = [], []
    for index, line in enumerate(text.splitlines(), 1):
        try:
            event = json.loads(line)
            if not isinstance(event, dict) or not isinstance(event.get("type"), str):
                raise ValueError("event lacks a type")
            events.append(event)
        except ValueError:
            errors.append(f"Unparseable event line {index}")
    return events, errors
