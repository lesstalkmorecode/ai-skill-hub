# Worker settings

Keep the main chat's settings. Explicit task choices win, then user-selected preferences; otherwise the coordinator chooses supported runtime options. Load [preferences](../skills/task-orchestrator/references/preferences.md) only for manual or saved choices. Workers never reroute themselves.

Choose capacity and reasoning separately by uncertainty and consequence, not fixed role or file count. Mechanical work may use lighter settings; ambiguous debugging, security or cross-repo behavior may need more. Do not invent model IDs, prices or applied overrides. If reliable selection information is absent, disclose runtime defaults.

State requested settings, observable effective settings and a short reason. Apply only compatible dispatch arguments; unknown effective settings remain unknown. Automatic fallback must respect explicit constraints; resolve an unsupported explicit choice before dispatch. No global config edits.

Before upgrading, distinguish missing context, scope, tooling and incorrect assumptions from reasoning difficulty through [recovery](../skills/task-orchestrator/references/recovery.md). Budgets require observable runtime enforcement. Model changes grant no permissions, spec approval or review independence.
