# Personal choices

Read only for an explicit or supplied saved choice. Honor the current request before saved preferences. The main chat keeps its selected model; workers inherit runtime defaults unless overridden. See [worker settings](../../../agents/model-routing.md) only when applying overrides.

Existing project or user-selected preferences can specify one agent, a reviewed team, allowed models, effort or concurrency. Read only a preference file explicitly supplied by the user or project guidance. Do not search unrelated personal folders or introduce a profile schema.

Save a preference only when requested, at a user-chosen authorized path, using the existing format or a short Markdown note. Preserve unrelated contents and keep personal machine settings out of Git. A saved preference grants no permissions, spec approval or publishing authorization.

Ask for model or effort only when the user explicitly requires choosing it before dispatch; unspecified settings otherwise inherit runtime defaults. A preselection, silence or timeout does not approve a required choice. Continue independent preparation while waiting; do not bypass an explicit choice constraint by taking over that assignment.

Apply concrete settings only through supported runtime arguments. Disclose automatic fallback to runtime defaults. If that fallback conflicts with an explicit model or limit, resolve it before dispatch. Report effective settings as unknown when unobservable; do not claim a token or monetary limit is enforced without runtime support.
