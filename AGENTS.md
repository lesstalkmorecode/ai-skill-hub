# Working on AI Skill Hub

This repository contains a Codex plugin with reusable Markdown skills and role contracts. Keep it
understandable as a package that can be installed into Codex; use the target project's existing
tools for development and verification.

- The root `plugin.json` is the portable plugin manifest. Distribution uses the client's marketplace configuration.
- Skills live in `skills/`; reusable worker contracts live in `agents/`.
- `skills/task-orchestrator/SKILL.md` is an optional coordination entrypoint. Skills can be used directly; domain guidance loads only when needed. Use Codex's native lifecycle rather than recreating it.
- `skills/task-orchestrator/references/risk.md` owns risk/evidence and delegation decision criteria. Keep other workflows linked to it rather than duplicating matrices. Workers inherit runtime model/effort defaults unless explicitly overridden.
- `skills/spring-boot/SKILL.md` is domain guidance, not the task lifecycle owner.
- Lessons default to the local `learning/` directory in the AI Skill Hub source checkout, with separate general and project scopes. Keep lessons out of Git and plugin packages; an installed plugin must resolve the source checkout separately from its cache. Write lessons into a target application repository only when explicitly requested. Propose them only after explicit final review acceptance and save them only after separate user approval.
- Keep all project content in English, including prompts, comments and examples.
- Keep runtime-specific behavior in adapters or conditional references.
- Preserve explicit user choices, existing edits, honest check results and read-only review boundaries.
- Plugin packaging must not silently copy or rewrite project-local guidance.
- Load guidance when relevant; do not introduce mandatory planning, delegation or task-state infrastructure for ordinary work.
- When editing a workflow, inspect its role contracts, adapters and entrypoint docs for conflicting instructions. Preserve the explicit draft approval gate of optional Spec-driven mode.
- Validate JSON/TOML syntax, skill frontmatter, Markdown links, and matching agent definitions after changes. Run `git diff --check` when Git metadata is available. Use the target project's existing tools for application verification.
- Keep local handover notes, credentials, logs and machine preferences out of Git unless explicitly intended as project documentation. Distribute a clean checkout without local lessons or machine data.
- Judge workflow improvements on real development tasks. Do not claim token savings or productivity gains without observed evidence.
