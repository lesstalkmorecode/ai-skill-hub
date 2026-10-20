# Permissions and verification

The [workflow guide](workflow.md) describes task behavior. Runtime access is controlled by your
local Codex configuration and applicable managed policies.

## Verification

When editing this package, validate `plugin.json`, skill frontmatter, and relative Markdown links.
Keep canonical agent definitions in `adapters/codex/agents/` identical to the matching `.codex/agents/`
regular-file copies. Review changes against the affected role contracts and approval boundaries.

Choose verification using [Risk and evidence](../skills/task-orchestrator/references/risk.md),
which owns the shared matrix and completion limits. Use the target application's own tests to verify application changes. Report checks actually
performed and meaningful limits. Evaluate workflow changes through real tasks and observed results.

## Permission limits

Sandbox, approval, network, and agent-session settings are local choices. Configure them in your
personal `~/.codex/config.toml` or an untracked `.codex/config.toml` for this checkout. The repository
ignores the project configuration file and does not ship session defaults. Confirm the actual
session permissions when they matter; managed requirements and session overrides still apply.

Codex workers inherit the parent session's sandbox and approval policy. A role named `reviewer`
or an instruction to avoid edits does not create a separate read-only sandbox. The supplied
adapters omit per-agent session settings that cannot enforce such a restriction, and do not
claim to disable nested-agent tools. See the [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

When enforced read-only review is required, use a separate restricted CLI session:

```bash
codex -C /absolute/target --sandbox read-only --ask-for-approval never
```

Supply the review scope and role contract and confirm the permissions before review. If the
required isolation is unavailable, report the gap instead of claiming a worker provides it.
Shell/filesystem restrictions do not control hosted search or connectors, which have their own
permissions. A workspace boundary also does not isolate writers from each other within a checkout.

Static validation cannot prove runtime enforcement or application correctness. Report check results
and remaining limits accurately; claim security, productivity, or usage improvements only when
supported by observed evidence.

## Repeatable package checks and live evaluations

Use the [evaluation guide](../evals/README.md) for offline validation and the optional
container runner. Offline tests verify package structure and evidence-checking logic.
Live scenarios assess specified observable behavior with independent fixture checks.
Neither a schema-valid report nor an unchanged final diff proves all actions were
authorized. The runner does not add per-role permission profiles to the plugin;
its sandbox settings apply to separate evaluation sessions.
