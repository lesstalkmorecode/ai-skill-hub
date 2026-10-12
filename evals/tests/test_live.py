import contextlib
import io
import json
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

from evals.live import codex_command, docker_command, inside, main, preflight, sandbox_probe


class RunnerSafetyTests(unittest.TestCase):
    def test_default_does_not_start_docker_or_codex(self):
        with patch("sys.argv", ["live"]), patch("evals.live.subprocess.run") as run:
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(0, main())
            run.assert_not_called()
            self.assertEqual("SKIPPED", json.loads(output.getvalue())["status"])

    def test_preflight_skips_without_docker(self):
        with patch("evals.live.shutil.which", return_value=None):
            self.assertEqual("Docker is unavailable", preflight("unused"))

    def test_fixture_execution_refuses_host(self):
        with patch.dict("os.environ", {}, clear=True), patch("evals.live.subprocess.run") as run:
            self.assertEqual("SKIPPED", inside("bug-fix", "test-model", 10)["status"])
            run.assert_not_called()

    def test_docker_has_no_host_mounts_or_privilege_escalation(self):
        args = docker_command("test-image", "generated-name", "bug-fix", "test-model", 30)
        self.assertIn("--read-only", args)
        self.assertIn("--cap-drop=ALL", args)
        self.assertIn("--security-opt=no-new-privileges", args)
        self.assertIn("CODEX_API_KEY", args)
        for forbidden in ("--privileged", "--mount", "-v", "--volume", "--network=host"):
            self.assertNotIn(forbidden, args)

    def test_runtime_permissions_differ_by_scenario(self):
        for scenario, sandbox in (("bug-fix", "workspace-write"), ("read-only-review", "read-only"), ("unapproved-spec", "workspace-write")):
            with self.subTest(scenario=scenario):
                args = codex_command(Path("/workspace/task"), Path("/tmp/schema"), Path("/tmp/report"), "test-model", scenario)
                self.assertEqual(sandbox, args[args.index("--sandbox") + 1])
                self.assertIn('approval_policy="never"', args)
                self.assertIn("agents.enabled=false", args)
                self.assertIn("--strict-config", args)
                self.assertIn("--ignore-user-config", args)
                self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", args)

    def test_smoke_has_no_credentials_or_network(self):
        args = docker_command("test-image", "generated-name", "bug-fix", None, 30, smoke=True)
        self.assertIn("--network=none", args)
        self.assertIn("--smoke", args)
        self.assertNotIn("CODEX_API_KEY", args)
        self.assertNotIn("--model", args)

    def test_unsupported_native_sandbox_stops_preflight(self):
        failure = subprocess.CompletedProcess([], 1, "", "Namespace unavailable")
        with patch("evals.live.command", return_value=failure) as run:
            result = sandbox_probe(Path("/workspace/fixture"))
            self.assertEqual("read-only", result["mode"])
            self.assertEqual(1, run.call_count)

    def test_writable_read_only_probe_is_rejected(self):
        allowed = subprocess.CompletedProcess([], 0, "ALLOWED\n", "")
        with patch("evals.live.command", return_value=allowed):
            self.assertIsNotNone(sandbox_probe(Path("/workspace/fixture")))

    def test_both_native_permission_profiles_are_probed(self):
        results = [
            subprocess.CompletedProcess([], 0, "DENIED\n", ""),
            subprocess.CompletedProcess([], 0, "ALLOWED\n", ""),
        ]
        with patch("evals.live.command", side_effect=results) as run:
            self.assertIsNone(sandbox_probe(Path("/workspace/fixture")))
            self.assertIn(":read-only", run.call_args_list[0].args[0])
            self.assertIn(":workspace", run.call_args_list[1].args[0])


if __name__ == "__main__":
    unittest.main()
