# Codex execution

Read when coordinating delegated work in Codex. For installation and named-agent registration,
see the [setup guide](README.md); ordinary tasks need neither registration nor this reference.

Use the session's native search, editing, command, planning and subagent tools, and the target
project's build/test commands. No additional orchestration runtime, index or task-state service
is required.

Check the tools and named roles actually exposed before dispatch. Follow
[Execution](../../skills/task-execution/references/execution.md) for assignments, ownership,
liveness, recovery and integration. Check whether the dispatch API supports selective context or
inherits history; disclose inherited history rather than claiming isolated context.
Use supported status/wait and continuation controls. If optional delegation is unavailable,
continue in the main session; report any required independence as a gap.

Role loaders do not enforce tool or filesystem restrictions. Follow
[permission limits](../../docs/controls.md#permission-limits), including a separate restricted
session when enforced read-only review is required. Context separation, independent review and
OS-enforced isolation require separate evidence.

The supplied adapters inherit native runtime model/effort defaults. Explicit supported user settings
are handled in the linked delegation guidance; no separate routing layer is required.
