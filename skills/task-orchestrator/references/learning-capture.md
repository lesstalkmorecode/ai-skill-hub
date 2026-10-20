# Propose and save lessons

Load only after the user explicitly accepts the final result under the
[review gate](../SKILL.md#review-before-learning). Learning is optional.

## Capture only evidence-backed candidates

Inspect the final diff and the user's words. Propose only a clear, reusable rule supported by a
test, check or concrete review evidence. Include the rule, evidence, general or project scope,
applicability limits and resolved save path. General scope needs evidence beyond this project.
Ask separately for approval to save that proposal; code acceptance alone grants none.

## Personal storage

Resolve the source checkout, destination and project ID using the [retrieval rules](learning.md).
If the source path is unknown, resolve it before proposing a save. Create files only to save an
approved lesson. Writing lessons into the target application repository requires an explicit
request. Migrating lessons from an old ID or storage location requires separate approval; do not
move or delete them implicitly.

After explicit save approval, preserve unrelated entries and update duplicates rather than adding
conflicting rules. A local lesson never edits the shared skill. Report unavailable access without
falling back to the application repository. Keep lessons short: rule, evidence, scope and limits;
exclude credentials, raw machine paths, logs and transcripts.

Spring Boot supplies technical interpretation; task-orchestrator owns approval and storage.
Lessons are persistent guidance, not model training or a background process.
