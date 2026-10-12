# Learning from approved work

Use this reference when a completed task contains a correction, explicit preference, or project
decision that may help with future work. Learning is optional and lightweight; do not preload
domain documentation just to look for lessons.

## Capture only evidence-backed candidates

Do not propose learning at the first task-completion message. Present the result and explicitly ask
the user to review it. If changes are requested, complete them, rerun relevant checks and ask for
review again. Silence, passing checks or earlier code approval do not establish final acceptance.
After the user explicitly accepts the final result, inspect
the final diff and the user's words. Create a lesson candidate only when the behavior or preference
is clear, supported by a test, check, or concrete review evidence, and more reusable than the exact
code change.

Code approval alone is not lesson approval. Do not infer permission from “looks good”, a passing
test, or silence. Ask separately whether the lesson should be saved.

## Personal storage and retrieval

Default to `<hub-source-root>/learning/` in the AI Skill Hub source checkout. Keep this directory
out of Git and plugin packages. Use `spring-boot.md` for approved general Spring Boot guidance and
`projects/<project-id>.md` for project-specific lessons. Create files only when saving an approved
lesson. Writing into the target application repository still requires an explicit request.

Resolve `hub-source-root` from the user's supplied path or an existing user-selected local setting.
When using skills directly from a verified source checkout, use that pack root. Installed plugins
must resolve the source checkout separately: their pack root is an installed or cached copy, not
the lesson destination. Never assume the current application directory is the hub source. If the
source path is unknown, continue without saved lessons and resolve it before proposing a save;
do not search unrelated folders or silently fall back to another location. Keep machine paths in
the conversation or explicitly authorized local preferences, not in shared plugin files.

Before relevant work, read existing general guidance and the matching project file. Do not scan
other projects' lessons or create files just to read them. Task instructions and current project
rules take precedence; flag stale or conflicting lessons rather than applying them blindly.

Derive `project-id` as the full SHA-256 hex digest of the canonical absolute Git common-directory
path, so worktrees share lessons and same-name repositories do not collide. For a non-Git project,
hash its canonical absolute root path. Store the project display name with the ID for readability,
not as the lookup key. A moved repository or separate clone gets a new ID; ask before migrating
old lessons. Do not store remote credentials or raw machine paths in lesson content.

Existing lessons in a previous storage location require explicit migration approval; changing
the default does not authorize moving or deleting them.

After final acceptance, propose the rule, evidence, general or project scope, and resolved save
path. Save only after explicit approval of that proposal. General scope requires a reason it
applies beyond the current project; do not promote project conventions automatically. A local
lesson never edits the shared skill. Preserve unrelated entries and update duplicates rather than
appending contradictory rules. If access is unavailable, report it; do not fall back to writing in
the application repository.

Keep each lesson short: rule, evidence, scope, and applicability limits. Exclude credentials, logs
and raw transcripts. The Spring Boot skill supplies technical interpretation; task-orchestrator
owns approval and storage. This is persistent guidance read by the agent, not model training or a
background process.
