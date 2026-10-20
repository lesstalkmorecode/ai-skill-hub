# Learning from approved work

Use this reference to retrieve saved guidance at task start and, after final acceptance, consider
reusable corrections, preferences or project decisions. Learning is optional; do not preload domain
documentation to look for lessons.

## Capture only evidence-backed candidates

Present the completed result and explicitly ask for review before proposing lessons. Complete
requested revisions, rerun relevant checks and ask for review again. Only explicit final acceptance
permits a proposal; silence, passing checks and earlier code approval do not establish acceptance.

After acceptance, inspect the final diff and the user's words. Propose only a clear, reusable rule
supported by a test, check or concrete review evidence. Include the rule, evidence, general or
project scope, applicability limits and resolved save path. General scope needs evidence beyond
this project. Ask separately for approval to save that proposal; code acceptance alone grants none.

## Personal storage and retrieval

Default to `<hub-source-root>/learning/` in the AI Skill Hub source checkout, outside Git and plugin
packages. General Spring Boot guidance uses `spring-boot.md`; project lessons use
`projects/<project-id>.md`. Create files only to save an approved lesson. Writing lessons into the
target application repository requires an explicit request.

Resolve `hub-source-root` from a supplied path or existing user-selected local setting; a verified
source checkout's pack root is valid. An installed/cached plugin root is not the source checkout.
Never assume the application directory is the hub source or search unrelated folders. If unknown,
continue without lessons and resolve the source path before proposing a save. Keep machine paths
in chat or authorized local preferences, not shared plugin files.

Before relevant work, read existing general guidance and the matching project file only. Do not
create files to read them. Task instructions and current project rules take precedence; flag stale
or conflicting lessons rather than applying them blindly.

Use the full SHA-256 hex digest of the canonical absolute Git common-directory path as `project-id`
(worktrees share it); for non-Git projects hash the canonical absolute root. Store a display name
for readability, not lookup. Moves and separate clones produce new IDs. Migrating lessons from an
old ID or storage location requires separate approval; do not move or delete them implicitly.

After explicit save approval, preserve unrelated entries and update duplicates rather than adding
conflicting rules. A local lesson never edits the shared skill. Report unavailable access without
falling back to the application repository. Keep lessons short: rule, evidence, scope and limits;
exclude credentials, raw machine paths, logs and transcripts.

Spring Boot supplies technical interpretation; task-orchestrator owns approval and storage.
Lessons are persistent guidance, not model training or a background process.
