"""Validate the hub's maintained files without an LLM or third-party packages."""

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROLES = {"implementer", "reviewer"}
EXPECTED_SKILLS = {"task-orchestrator", "spec-workflow", "review-workflow", "spring-boot"}
CONTENT_DIRS = ("skills", "agents", "adapters", "docs", "evals", ".github")
PRIVATE_PARTS = {
    "learning", ".git", ".idea", ".aws", ".ai-skill-hub", "__pycache__",
    "node_modules", ".venv", "results", "sessions", "logs",
}
PRIVATE_NAMES = {"auth.json", "history.jsonl", "config.toml", "credentials"}


def private_path(path):
    parts = {part.lower() for part in Path(path).parts}
    name = Path(path).name.lower()
    return bool(parts & PRIVATE_PARTS) or name in PRIVATE_NAMES or (
        name.startswith(".env") and name not in {".env.example", ".env.sample", ".env.template"}
    ) or name.endswith((".log", ".tmp", ".bak", ".pyc"))


def package_errors(root):
    """Audit an already staged distribution; do not confuse gitignore with packaging."""
    errors = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if path.is_symlink() or getattr(path, "is_junction", lambda: False)():
            errors.append(f"{relative}: links are not allowed in a distribution")
        elif private_path(relative):
            errors.append(f"{relative}: private/local data in distribution")
    return errors


def maintained_files(root):
    files = [root / name for name in ("README.md", "AGENTS.md", "plugin.json")]
    for directory in CONTENT_DIRS + (".codex/agents",):
        files.extend(
            p for p in (root / directory).rglob("*")
            if p.is_file() and p.resolve().is_relative_to(root.resolve())
            and not private_path(p.relative_to(root))
        )
    return files


def frontmatter(text):
    """Parse the repository's deliberately small YAML profile: two plain scalars.

    Reject unsupported YAML instead of guessing at its meaning. A future switch to
    nested metadata should use a real YAML parser and extend this documented profile.
    """
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("unterminated frontmatter") from exc
    result = {}
    for line in lines[1:end]:
        match = re.fullmatch(r"(name|description): ([^\r\n]+)", line)
        if not match:
            raise ValueError("frontmatter supports only name and description plain scalars")
        key, value = match.groups()
        if key in result:
            raise ValueError(f"duplicate frontmatter key: {key}")
        if value[0] in "\"'[{&*!>|%@`" or ": " in value or " #" in value:
            raise ValueError(f"{key}: unsupported YAML scalar; use an unambiguous plain string")
        if value.lower() in {"null", "~", "true", "false", "yes", "no", "on", "off"} or re.fullmatch(r"[-+]?[0-9.]+", value):
            raise ValueError(f"{key}: must be a string scalar")
        result[key] = value.strip()
    if set(result) != {"name", "description"} or not all(result.values()):
        raise ValueError("name and description must be nonempty")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", result["name"]):
        raise ValueError("invalid skill name")
    return result


def prose(text):
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", text)


def anchors(text):
    found, counts = set(), {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", prose(text)):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(f"{slug}-{count}" if count else slug)
    return found


def link_errors(root, path):
    errors = []
    text = prose(path.read_text(encoding="utf-8"))
    # The maintained Markdown uses inline links. Reference definitions are also checked.
    links = re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text)
    links += re.findall(r"(?m)^\[[^\]\n]+\]:\s*(\S+)", text)
    for link in links:
        target = link.strip().split(' "', 1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not destination.is_relative_to(root.resolve()):
            errors.append(f"{path.relative_to(root)}: link escapes package: {target}")
        elif not destination.exists():
            errors.append(f"{path.relative_to(root)}: missing link: {target}")
        elif parsed.fragment and destination.suffix == ".md":
            if unquote(parsed.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                errors.append(f"{path.relative_to(root)}: missing anchor: {target}")
    return errors


def validate(root):
    errors = []
    files = maintained_files(root)
    # Inspect links before is_file() filtering so broken links cannot disappear from validation.
    for directory in CONTENT_DIRS + (".codex/agents",):
        for path in (root / directory).rglob("*"):
            if path.is_symlink() and not private_path(path.relative_to(root)):
                if not path.exists() or not path.resolve().is_relative_to(root.resolve()):
                    errors.append(f"{path.relative_to(root)}: broken or escaping symlink")
    skills = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    roles = {p.stem for p in (root / "agents").glob("*.md") if p.name != "README.md"}
    if skills != EXPECTED_SKILLS:
        errors.append(f"skill inventory differs: {sorted(skills)}")
    if roles != EXPECTED_ROLES:
        errors.append(f"role inventory differs: {sorted(roles)}")
    for path in files:
        try:
            if path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
            elif path.suffix == ".toml":
                tomllib.loads(path.read_text(encoding="utf-8"))
            elif path.suffix == ".md":
                errors.extend(link_errors(root, path))
                if path.name == "SKILL.md":
                    metadata = frontmatter(path.read_text(encoding="utf-8"))
                    if metadata["name"] != path.parent.name:
                        errors.append(f"{path.relative_to(root)}: name differs from directory")
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    try:
        manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
        for key in ("name", "version", "description"):
            if not isinstance(manifest.get(key), str) or not manifest[key].strip():
                errors.append(f"plugin.json: missing/non-string {key}")
    except (OSError, ValueError):
        pass  # Already reported above.
    canonical = {p.name: p for p in (root / "adapters/codex/agents").glob("*.toml")}
    copies = {p.name: p for p in (root / ".codex/agents").glob("*.toml")}
    if set(canonical) != {f"{role}.toml" for role in EXPECTED_ROLES} or canonical.keys() != copies.keys():
        errors.append("canonical and local agent inventories differ from the two-role catalog")
    for name, path in canonical.items():
        if name in copies and copies[name].is_symlink():
            errors.append(f"{name}: local agent definition must be a portable regular-file copy")
        try:
            if not path.resolve().is_relative_to(root.resolve()):
                continue  # Reported by the symlink audit; never read outside the pack.
            if name in copies:
                if not copies[name].resolve().is_relative_to(root.resolve()):
                    continue
                if path.read_bytes() != copies[name].read_bytes():
                    errors.append(f"{name}: canonical and local agent definitions differ")
            agent = tomllib.loads(path.read_text(encoding="utf-8"))
            for key in ("name", "description", "developer_instructions"):
                if not isinstance(agent.get(key), str) or not agent[key].strip():
                    errors.append(f"{name}: missing/non-string {key}")
            role = root / "agents" / f"{path.stem}.md"
            if agent.get("name") != path.stem or not role.is_file():
                errors.append(f"{name}: missing or mismatched role")
            if f"<pack-root>/agents/{path.stem}.md" not in agent.get("developer_instructions", ""):
                errors.append(f"{name}: canonical role loader reference missing")
            unsupported = set(agent) - {"name", "description", "developer_instructions"}
            if unsupported:
                errors.append(f"{name}: outside this adapter's instructions-only native-default profile: {sorted(unsupported)}")
        except OSError as exc:
            errors.append(f"{name}: unreadable agent definition: {exc}")
        except ValueError:
            pass  # Syntax errors were reported while parsing maintained files.
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--package-dir", type=Path, help="Also audit a staged distribution for local data.")
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if args.package_dir:
        if not args.package_dir.is_dir():
            errors.append("package directory does not exist")
        else:
            errors.extend(package_errors(args.package_dir))
    for error in errors:
        print(f"FAIL: {error}")
    print(f"{'FAIL' if errors else 'PASS'}: package validation ({len(errors)} errors)")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
