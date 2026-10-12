# AI Skill Hub

Shared skills for structured coding with AI agents. Use them across your local projects.

## Start

- Open the project you want to change.
- Replace `/absolute/pack` with this checkout's path.
- Send a task like this:

```text
Use /absolute/pack/skills/task-orchestrator/SKILL.md.
Fix duplicate orders when a request is retried.
Preserve the response contract and my existing edits.
Run the relevant project checks.
```

**Add your own skill:** create a folder inside this checkout.

```text
/absolute/pack/
└── skills/
    └── retry-review/
        └── SKILL.md
```

Example `SKILL.md`:

```markdown
---
name: retry-review
description: Review request retries for duplicate records.
---

Inspect retry handling and persistence. Check whether repeated requests
can create duplicate records. Report findings with file/line references.
Do not edit code.
```

Use it from any target project:

```text
Use /absolute/pack/skills/retry-review/SKILL.md.
Review the current diff.
```

## What happens

- The agent reads project rules and relevant code.
- For substantial work, it states behavior, boundaries and acceptance criteria.
- It investigates unknown causes before patching.
- It implements and verifies against the criteria.
- It reports changes, actual checks and remaining gaps.

Small tasks stay with one agent. Delegation depends on useful separable work and runtime permission. Important missing requirements come back to you. No routine workflow menu.

## Examples

Add the request after the skill path:

- **Investigate:** `Find the cause. Do not edit yet.`
- **Implement:** `Apply the fix. Keep the public API unchanged.`
- **Delegate:** `Use subagents for separable work. Independently review the combined result.`
- **Review:** `Review the current diff. Do not edit or publish comments.`
- **Multiple repos:** `Targets: backend=/path/backend, sdk=/path/sdk. Preserve older clients.`
- **Continue:** `Read this handover, inspect current state, and finish the remaining work.`
- **Spec-driven:** `Draft the feature spec. Wait for my approval before implementation.`

## Context

- Small direct change: **191 words** of shared instructions.
- Substantial implementation: **327 words**.
- Unexplained bug plus substantive fix: **418 words**.
- These exclude project code, chat history and runtime instructions.
- Words are not tokens. Read [file counts and loading rules](docs/context.md).

## One-time user setup

Keep the whole checkout together. Optional: create a loader in your client's supported skill directory. Preserve existing files.

<details>
<summary>Loader example</summary>

```markdown
---
name: task-orchestrator
description: Use my shared coding practices when requested.
---

Read /absolute/pack/skills/task-orchestrator/SKILL.md.
Pack root: /absolute/pack. Target: current workspace unless specified.
Resolve links from their containing document.
Pass the pack root and target to workers. Report inaccessible guidance.
```

</details>

[Worker roles](agents/README.md) · [Optional Codex adapters](adapters/codex/README.md)

Skills guide agent behavior; they do not enforce runtime safety or guarantee correctness.
