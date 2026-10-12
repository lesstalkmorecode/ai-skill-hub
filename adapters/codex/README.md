# Optional Codex adapters

These TOMLs configure named roles in clients supporting custom agents. They are optional: normal orchestration assigns the [Markdown role contracts](../../agents/README.md) through available worker tools.

Before installing selected TOMLs, check your client's supported location and settings, and preserve existing same-name files. The [global loader](../../README.md#one-time-user-setup) does not install or apply adapters.

The TOML examples inherit runtime model/effort defaults. The coordinator resolves worker settings from explicit task choices, user-selected saved preferences, or automatic routing (manual selection when requested); see [model routing](../../agents/model-routing.md). Adapter defaults alone do not establish a user preference. Apply resolved concrete settings through supported dispatch overrides. If an adapter prevents an automatic override, disclose the fallback to runtime defaults; an explicit choice or constraint requires a compatible alternative before dispatch. Only implementer defaults to workspace-write. Other roles default to read-only with no escalation prompts and report inaccessible required context as blocked. Runtime permissions govern access.

Every delegation supplies the absolute pack root and target repository. Adapters explicitly read central contracts; TOML does not automatically include Markdown files. Central updates affect future contract reads, while copied adapter settings need separate maintenance. All workers remain leaf assignments.
