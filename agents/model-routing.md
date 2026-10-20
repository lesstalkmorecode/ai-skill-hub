# Optional worker settings

Inherit runtime model and effort defaults. Role names, risk levels and file counts do not select
models; no routing stage or model menu is required. Keep the main chat's settings.

Read this only for an explicit model/effort choice, an existing user-selected constraint or an
unsupported dispatch setting. Current user choices take precedence over saved preferences.
Load [preferences](../skills/task-orchestrator/references/preferences.md) only when those exist.

Apply overrides only through supported runtime arguments; never invent IDs, prices or effective
settings. If a requested setting cannot be honored, report that before dispatch and resolve the
conflict with the user. Missing optional overrides otherwise use runtime defaults. Unknown
effective settings stay unknown; no global configuration edits are implied.

Do not respond to a failed check by automatically upgrading a model. Use [recovery](../skills/task-orchestrator/references/recovery.md)
to inspect missing context, assumptions, scope and tooling first. Respect explicit attempt and
budget limits; claim enforcement only when observable. Workers do not reroute themselves.
