"""Opt-in, container-contained Codex evaluations. Never invoked by offline tests."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

try:
    from .cases import REPORT_SCHEMA, SCENARIOS, grade, parse_events, prompt, seed, snapshot
except ImportError:
    from cases import REPORT_SCHEMA, SCENARIOS, grade, parse_events, prompt, seed, snapshot

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "ai-skill-hub-eval:0.144.5"
CLI_VERSION = "codex-cli 0.144.5"


def command(args, **kwargs):
    return subprocess.run(args, text=True, capture_output=True, timeout=30, **kwargs)


def preflight(image):
    if not shutil.which("docker"):
        return "Docker is unavailable"
    try:
        info = command(["docker", "info", "--format", "{{.OSType}}"])
        if info.returncode or info.stdout.strip() != "linux":
            return "A reachable Linux Docker engine is required"
        inspect = command(["docker", "image", "inspect", image])
        if inspect.returncode:
            return "Evaluation image is missing; build it explicitly using evals/Dockerfile"
        metadata = json.loads(inspect.stdout)[0]
        labels = metadata.get("Config", {}).get("Labels", {}) or {}
        if labels.get("ai-skill-hub.evals") != "1":
            return "Image does not declare the evaluation runner contract"
        return None
    except (OSError, subprocess.TimeoutExpired, ValueError, KeyError, IndexError) as exc:
        return f"Docker preflight unavailable: {type(exc).__name__}"


def docker_command(image, name, scenario, model, timeout, smoke=False):
    args = [
        "docker", "run", "--rm", "--pull=never", "--name", name,
        "--read-only", "--user", "1000:1000",
        "--cap-drop=ALL", "--security-opt=no-new-privileges",
        "--pids-limit=256", "--memory=2g", "--cpus=2",
        "--tmpfs", "/tmp:rw,nosuid,nodev,size=512m,mode=1777",
        "--tmpfs", "/workspace:rw,nosuid,nodev,size=256m,mode=1777",
        "--tmpfs", "/state:rw,nosuid,nodev,size=256m,mode=1777",
    ]
    args += ["--network=none"] if smoke else ["-e", "CODEX_API_KEY"]
    args += [
        image,
        "python3", "/opt/hub/evals/live.py", "--inside", "--scenario", scenario,
        "--timeout", str(timeout),
    ]
    if smoke:
        args += ["--smoke"]
    else:
        args += ["--model", model]
    return args


def codex_command(workspace, schema, report, model, scenario):
    return [
        "codex", "exec", "--strict-config", "--ignore-user-config", "--ignore-rules",
        "--ephemeral", "--json", "--color", "never",
        "--sandbox", "read-only" if scenario == "read-only-review" else "workspace-write",
        "-c", 'approval_policy="never"', "-c", "agents.enabled=false",
        "-c", 'web_search="disabled"',
        "-c", 'shell_environment_policy.filters.CODEX_API_KEY="exclude"',
        "-c", "sandbox_workspace_write.network_access=false",
        "-C", str(workspace), "--model", model, "--output-schema", str(schema),
        "--output-last-message", str(report), "-",
    ]


def sandbox_probe(workspace):
    """Probe native sandbox support before spending model tokens."""
    for mode, marker in (("read-only", "DENIED"), ("workspace-write", "ALLOWED")):
        program = (
            "from pathlib import Path\n"
            "p = Path('sandbox-probe.txt')\n"
            "try:\n"
            "    p.write_text('synthetic probe')\n"
            "except PermissionError:\n"
            "    print('DENIED')\n"
            "else:\n"
            "    p.unlink()\n"
            "    print('ALLOWED')\n"
        )
        result = command([
            "codex", "sandbox", "--permission-profile",
            ":read-only" if mode == "read-only" else ":workspace",
            "-c", 'approval_policy="never"', "-C", str(workspace),
            "--", "python3", "-c", program,
        ])
        if result.returncode or result.stdout.strip() != marker:
            return {"mode": mode, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    return None


def inside(scenario, model, timeout, smoke=False):
    # This guard prevents accidental execution of fixture code on the host.
    if not Path("/.dockerenv").is_file() or os.environ.get("AI_SKILL_HUB_EVAL_CONTAINER") != "1":
        return {"status": "SKIPPED", "reason": "Internal runner requires the evaluation container"}
    Path("/state/codex").mkdir(exist_ok=True)
    version = command(["codex", "--version"])
    if version.returncode or version.stdout.strip() != CLI_VERSION:
        return {"status": "SKIPPED", "reason": "Unsupported CLI version", "cli_version": version.stdout.strip()}
    with tempfile.TemporaryDirectory(prefix="hub-eval-", dir="/workspace") as directory:
        workspace = Path(directory)
        seed(workspace)
        try:
            probe = sandbox_probe(workspace)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {"status": "SKIPPED", "reason": f"Sandbox preflight unavailable: {type(exc).__name__}"}
        if probe:
            return {"status": "SKIPPED", "reason": "Native sandbox preflight failed; no model run started", "probe": probe}
        if smoke:
            oracle_args = ["python3", "-B", str(ROOT / "evals/oracle.py"), str(workspace / "calc.py")]
            broken = command(oracle_args)
            (workspace / "calc.py").write_text(
                "def total(items):\n    return sum(i['price'] * i['quantity'] for i in items)\n",
                encoding="utf-8",
            )
            fixed = command(oracle_args)
            passed = broken.returncode == 1 and fixed.returncode == 0
            return {
                "status": "READY" if passed else "FAIL",
                "reason": "Sandbox and oracle smoke checks passed; no model run performed" if passed else "Oracle smoke check failed",
                "cli_version": version.stdout.strip(),
                "oracle_broken": broken.stdout, "oracle_fixed": fixed.stdout,
            }
        for args in (
            ["git", "init", "-q", str(workspace)],
            ["git", "-C", str(workspace), "add", "."],
            ["git", "-C", str(workspace), "-c", "user.name=Evaluation",
             "-c", "user.email=evaluation@example.invalid", "commit", "-qm", "Fixture baseline"],
        ):
            result = command(args)
            if result.returncode:
                return {"status": "SKIPPED", "reason": "Fixture Git setup failed", "stderr": result.stderr}
        before = snapshot(workspace)
        with tempfile.TemporaryDirectory(prefix="hub-report-") as report_directory:
            schema = Path(report_directory) / "schema.json"
            report_file = Path(report_directory) / "report.json"
            schema.write_text(json.dumps(REPORT_SCHEMA), encoding="utf-8")
            args = codex_command(workspace, schema, report_file, model, scenario)
            started = time.monotonic()
            try:
                run = subprocess.run(
                    args, input=prompt(scenario, ROOT), text=True, capture_output=True,
                    timeout=timeout, cwd=workspace,
                )
            except subprocess.TimeoutExpired:
                return {"status": "INCONCLUSIVE", "reason": "Codex timeout", "duration_seconds": time.monotonic() - started}
            events, event_errors = parse_events(run.stdout)
            report = None
            if report_file.is_file():
                try:
                    report = json.loads(report_file.read_text(encoding="utf-8"))
                except ValueError:
                    pass
            after = snapshot(workspace)
            oracle = None
            if scenario == "bug-fix" and run.returncode == 0:
                env = {key: value for key, value in os.environ.items() if key != "CODEX_API_KEY"}
                try:
                    oracle = subprocess.run(
                        ["python3", "-B", str(ROOT / "evals/oracle.py"), str(workspace / "calc.py")],
                        text=True, capture_output=True, timeout=10, env=env, cwd="/tmp",
                    )
                except subprocess.TimeoutExpired:
                    return {"status": "INCONCLUSIVE", "reason": "Independent correctness check timed out", "events": events}
            result = grade(scenario, before, after, report, None if oracle is None else oracle.returncode == 0)
            # Missing/failed execution cannot earn a pass from a plausible final response.
            complete = any(e["type"] == "turn.completed" for e in events)
            failed = any(e["type"] in {"turn.failed", "error"} for e in events)
            if result["status"] != "FAIL" and (run.returncode or event_errors or not complete or failed):
                result.update(status="INCONCLUSIVE", reason="Runtime failure or incomplete event evidence")
            diff = command(["git", "-C", str(workspace), "diff", "--no-ext-diff", "--no-textconv", "HEAD"])
            result.update(
                scenario=scenario, model=model, cli_version=version.stdout.strip(),
                duration_seconds=round(time.monotonic() - started, 3),
                exit_code=run.returncode, agent_report=report, events=events,
                event_errors=event_errors, stderr=run.stderr,
                before=before, after=after, git_diff=diff.stdout,
                oracle=None if oracle is None else {
                    "exit_code": oracle.returncode, "stdout": oracle.stdout, "stderr": oracle.stderr,
                },
                usage=[e.get("usage") for e in events if e["type"] == "turn.completed"],
                limits=[
                    "Filesystem snapshots detect resulting changes, not attempted or reverted writes.",
                    "JSONL events are not a complete operating-system access audit.",
                    "Review uses a read-only sandbox; this does not prove voluntary non-editing.",
                    "PASS covers only the scenario's documented observable checks.",
                ],
            )
            return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=SCENARIOS, default="bug-fix")
    parser.add_argument("--model", help="Explicit model for a paid live run")
    parser.add_argument("--image", default=IMAGE)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--allow-live", action="store_true", help="Authorize model usage for this invocation")
    parser.add_argument("--preflight", action="store_true", help="Check Docker/image readiness without model usage")
    parser.add_argument("--smoke", action="store_true", help="Check container sandbox and oracle with no credentials or networking")
    parser.add_argument("--inside", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if not 10 <= args.timeout <= 600:
        parser.error("--timeout must be between 10 and 600 seconds")
    if args.inside:
        print(json.dumps(inside(args.scenario, args.model, args.timeout, args.smoke)))
        return 0
    if not args.allow_live and not args.preflight and not args.smoke:
        print(json.dumps({"status": "SKIPPED", "reason": "Live evaluation requires --allow-live"}))
        return 0
    reason = preflight(args.image)
    if reason or args.preflight:
        print(json.dumps({"status": "SKIPPED" if reason else "READY", "reason": reason or "Container image available; no model run performed"}))
        return 0
    if not args.model and not args.smoke:
        parser.error("--model is required for a live run")
    if not os.environ.get("CODEX_API_KEY") and not args.smoke:
        print(json.dumps({"status": "SKIPPED", "reason": "A dedicated evaluation CODEX_API_KEY is required"}))
        return 0
    # Resolve once so a mutable tag cannot select a different image after preflight.
    try:
        identity = command(["docker", "image", "inspect", args.image, "--format", "{{.Id}}"])
    except (OSError, subprocess.TimeoutExpired):
        print(json.dumps({"status": "SKIPPED", "reason": "Image identity lookup failed"}))
        return 0
    if identity.returncode or not identity.stdout.strip().startswith("sha256:"):
        print(json.dumps({"status": "SKIPPED", "reason": "Could not resolve the evaluation image ID"}))
        return 0
    image_id = identity.stdout.strip()
    name = "ai-skill-hub-eval-" + uuid.uuid4().hex
    result = {}
    try:
        run = subprocess.run(
            docker_command(image_id, name, args.scenario, args.model, args.timeout, args.smoke),
            text=True, capture_output=True, timeout=args.timeout + 60,
        )
        try:
            result = json.loads(run.stdout)
            statuses = {"PASS", "FAIL", "INCONCLUSIVE", "SKIPPED"} | ({"READY"} if args.smoke else set())
            if not isinstance(result, dict) or result.get("status") not in statuses:
                raise ValueError("invalid runner output")
            if run.returncode:
                result.update(status="INCONCLUSIVE", reason="Container returned a nonzero exit code")
        except ValueError:
            result = {"status": "INCONCLUSIVE", "reason": "Container failed to return a result", "stderr": run.stderr}
    except (OSError, subprocess.TimeoutExpired) as exc:
        result = {"status": "INCONCLUSIVE", "reason": f"Container execution failed: {type(exc).__name__}"}
    finally:
        # Only this invocation's generated container name can be removed.
        try:
            cleanup = command(["docker", "rm", "-f", name])
            if cleanup.returncode and "No such container" not in cleanup.stderr:
                result["cleanup_warning"] = "Could not confirm container removal; inspect " + name
        except (OSError, subprocess.TimeoutExpired):
            result["cleanup_warning"] = "Could not confirm container removal; inspect " + name
    result["image"] = args.image
    result["image_id"] = image_id
    result["scenario"] = args.scenario
    result["run_kind"] = "smoke" if args.smoke else "live"
    # Reports are private by default; never print traces or credentials to the terminal.
    encoded = json.dumps(result, indent=2)
    if os.environ.get("CODEX_API_KEY"):
        encoded = encoded.replace(os.environ["CODEX_API_KEY"], "[REDACTED]")
    output = ROOT / "evals/results"
    output.mkdir(exist_ok=True)
    path = output / f"{name}.json"
    with path.open("x", encoding="utf-8") as stream:
        stream.write(encoded + "\n")
    print(f"{result['status']}: {result.get('reason', '')}\nEvidence: {path}")
    return 1 if result["status"] in {"FAIL", "INCONCLUSIVE"} or "cleanup_warning" in result else 0


if __name__ == "__main__":
    sys.exit(main())
