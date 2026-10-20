# Workflow guide

The [README](../README.md) describes installation and entrypoints. The main Codex agent normally
handles the whole coding task using native planning, tools and context management. The conceptual
loop is understand → explore → decide → act → verify → recover; it is not six mandatory stages.
No pipeline, task-state schema, plan file or team is required.

## Choose proportionate guidance

| Situation | Useful decision |
| --- | --- |
| Known local fix | Inspect the path, edit and run a focused check. |
| Unknown bug | Reproduce or gather distinguishing evidence before patching. |
| Architectural change | Compare meaningful alternatives and shared boundaries before dependent changes. |
| Consequential change | Verify concrete denied paths, retries, isolation, compatibility or recovery as relevant. |
| Failed check | Revise the diagnosis with new evidence before retrying. |
| Unresolved product decision | Ask the user; continue independent authorized work. |

[Risk and evidence](../skills/task-orchestrator/references/risk.md) owns the consequence, reach,
reversibility and uncertainty criteria, evidence model, recovery decisions and completion limits.
[task-orchestrator](../skills/task-orchestrator/SKILL.md) remains only as an optional entrypoint for
these decisions; it does not route every task. Load domain references only for affected behavior.
For example, Spring persistence guidance helps with database invariants but is irrelevant to a
small Python fix. File counts are weak risk proxies. High risk increases verification depth,
not automatic team size.

## Scope and completion

Investigation and review requests return evidence without implementation. Fix/implementation
requests authorize scoped changes under applicable project rules. Preserve existing user edits
and explicit constraints. Ordinary coding introduces no new spec or final-acceptance gate.

Before completion, inspect the integrated diff and relevant untracked files. Match material claims
to current evidence and disclose limits. Passing unit mocks do not establish database isolation
or deployed behavior. Essential verification gaps and unresolved material findings prevent a
verified-completion claim. Recheck results affected by subsequent edits.

## Optional delegation

The [delegation criteria](../skills/task-orchestrator/references/risk.md#decide-whether-to-delegate)
require authorization and concrete value. A bounded independent implementation or focused review
can qualify; a coupled refactor or tiny fix normally stays local. Use only
[implementer or reviewer](../agents/README.md) and native runtime defaults, honoring explicit
supported user settings. Planning, design, test selection and risk analysis remain normal main-agent
capabilities. [Assignment and integration](../skills/task-orchestrator/references/execution.md)
loads only for actual dispatch. Workers are leaf assignments, not a required chain.

Independent review is distinct from self-review. If required independence is unavailable, say so.
Role instructions do not enforce read-only access; see [controls](controls.md#permission-limits).

## Optional spec work

[spec-workflow](../skills/spec-workflow/SKILL.md) is the only spec lifecycle, approval, storage and
coverage authority. It follows the target project's conventions, defaults to chat drafts without
a configured file workflow, and keeps explore/propose/apply/sync/archive distinct. Use its approval
and criterion-coverage rules when requested or required; ordinary tasks need no spec.

## Outside the coding loop

[Session transfer](session-transfer.md) is a short optional chat note, not another skill.
[Learning](learning.md) is only for supplied applicable guidance or requested lesson storage.
Neither adds startup scans, automatic persistent writes or a final acceptance ceremony.

The architecture aims for fewer concepts and relevant guidance; only observed development tasks
can establish behavioral quality, token savings or productivity changes. See the
[evaluation cases](../evals/decision-cases.md) for expectations and unverified areas.
