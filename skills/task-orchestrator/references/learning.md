# Retrieve saved guidance

At task start, read only existing guidance relevant to the task. Learning is optional; do not
preload domain documentation to look for lessons. Proposal and storage instructions are loaded
only after explicit final acceptance, through the [orchestrator](../SKILL.md#review-before-learning).

Default to `<hub-source-root>/learning/` in the AI Skill Hub source checkout, outside Git and plugin
packages. General Spring Boot guidance uses `spring-boot.md`; project lessons use
`projects/<project-id>.md`. Do not create files or directories during retrieval.

Resolve `hub-source-root` from a supplied path or existing user-selected local setting; a verified
source checkout's pack root is valid. An installed/cached plugin root is not the source checkout.
Never assume the application directory is the hub source or search unrelated folders. If unknown,
continue without lessons. Keep machine paths in chat or authorized local preferences, not shared
plugin files.

Before relevant work, read existing general guidance and the matching project file only. Task
instructions and current project rules take precedence; flag stale or conflicting lessons rather
than applying them blindly.

Use the full SHA-256 hex digest of the canonical absolute Git common-directory path as `project-id`
(worktrees share it); for non-Git projects hash the canonical absolute root. Store a display name
for readability, not lookup. Moves and separate clones produce new IDs; do not implicitly migrate,
move or delete lessons. Report unavailable access without falling back to the application repository.
