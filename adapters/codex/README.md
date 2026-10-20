# Codex setup

Use the skills directly from source as described in the [README](../../README.md#use-from-source),
or distribute the package through your chosen Codex marketplace using the root `plugin.json`.
See the [official plugin guide](https://developers.openai.com/plugins/build/plugins).

## Distribution

Distribute a clean checkout without local lessons, credentials, or machine configuration. Keep
personal `learning/` files in your working checkout rather than the copy used for distribution.
The manifest describes plugin metadata; it does not filter private files from a directory.

When updating a distributed plugin, refresh or reinstall it through the client's marketplace
controls and test in a new chat. Existing chats can retain instructions already read. See the
[official marketplace behavior](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work).

## Register named agents

Named agents are optional and configured separately from plugins. Copy selected TOMLs from
`adapters/codex/agents/` in the hub checkout to one of these locations:

| Scope | Destination |
| --- | --- |
| One target repository | `<target-repository>/.codex/agents/` |
| Your personal Codex setup | `~/.codex/agents/` |

Each TOML defines an agent's `name`, `description`, and `developer_instructions`. The `name`
identifies the agent. The following examples register `reviewer` for an application; replace the
paths with your own and preserve existing same-name files.

**Windows PowerShell**

```powershell
$hubSource = "C:\Projects\ai-skill-hub"
$targetRepo = "C:\Projects\my-app"
$agentDirectory = Join-Path $targetRepo ".codex/agents"
$agentFile = Join-Path $agentDirectory "reviewer.toml"
if (Test-Path -LiteralPath $agentFile) { throw "reviewer.toml already exists; review it before replacing." }
New-Item -ItemType Directory -Force -Path $agentDirectory | Out-Null
Copy-Item -LiteralPath (Join-Path $hubSource "adapters/codex/agents/reviewer.toml") -Destination $agentFile
```

**macOS / Linux**

```bash
hub_source="/path/to/ai-skill-hub"
target_repo="/path/to/my-app"
mkdir -p "$target_repo/.codex/agents"
cp -i "$hub_source/adapters/codex/agents/reviewer.toml" "$target_repo/.codex/agents/reviewer.toml"
```

For personal registration, use `$HOME/.codex/agents` as the destination directory. Copy only the
selected TOMLs. Keep sandbox, approval, network, and agent-session settings in your local Codex
configuration. Start a new session in the trusted target repository with custom agents supported
and delegation permitted.

Provide the absolute hub checkout path when requesting work:

```text
Use the reviewer agent to review the current uncommitted changes without editing files.
Pack root: C:/Projects/ai-skill-hub.
Target repository: the current workspace.
Pass this pack root and review scope to the reviewer and return its findings.
```

The reviewer reads `agents/reviewer.md` from that root. Keep the checkout accessible: the TOML
contains loader instructions, not an embedded copy of the role contract. Check agent availability
before claiming a named worker performed the task. See the [official custom agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Native execution

For delegated work, load only [Codex execution](execution.md) for runtime capabilities, context
inheritance and permission limits. Task assignments and integration are owned by the portable
[Execution reference](../../skills/task-orchestrator/references/execution.md).

## Maintaining definitions

Canonical adapters in `adapters/codex/agents/` have matching regular-file copies under `.codex/agents/` for work
in this checkout. Update both sets together and keep their contents identical. Copies installed in
another project or your personal configuration require separate maintenance. Changes to central
Markdown contracts affect future reads from the supplied pack root.

The only supplied roles are `implementer` and `reviewer`. Models and effort inherit native runtime defaults; explicit supported user settings are handled in the [delegation guidance](../../skills/task-orchestrator/references/execution.md). No model-selection stage or global configuration changes are implied.
