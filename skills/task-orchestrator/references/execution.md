# Delegation and integration

Load only for an actual assignment after the [delegation decision](risk.md#decide-whether-to-delegate).
Use the native runtime; [Codex execution](../../../adapters/codex/execution.md) describes runtime limits.
Only two optional contracts exist: [implementer](../../../agents/implementer.md) and
[reviewer](../../../agents/reviewer.md). The main agent handles planning, design and test selection.
A reviewer can assess any named engineering concern; do not create a specialist role pipeline.

Give a worker the absolute pack and target paths, current revision/working state, one bounded
outcome or question, complete assigned criteria, owned paths/exclusions, binding decisions,
prerequisites and allowed checks. Pass the approved baseline and approval reference for spec work.
Load only the assigned contract and relevant domain guidance. Prefer minimal necessary context
where supported; do not claim isolated history when the runtime inherits it.

Inherit native model/effort defaults unless the user explicitly requests supported settings.
Honor those preferences; resolve unsupported explicit requirements before dispatch. Do not invent
model IDs, prices or effective settings, edit global configuration, or automatically upgrade after
failure. Model choice and worker count are not verification.

Parallel writers need separate workspaces and independent shared resources; keep one writer per
checkout. Sequence dependencies until interfaces are stable. Track ownership in chat. A timeout
is not proof a writer stopped: inspect liveness and changes before retrying or transferring ownership.
Workers do not delegate further, expand scope or publish; they return changes/findings, actual
checks and limits to the main agent.

Inspect returned evidence and diffs against source, resolve conflicts and verify the integrated
state in dependency order. For multiple repositories, verify producer/consumer compatibility and
the combined behavior at the intended revisions; separately passing tests may miss that boundary.
Partial reviews do not cover the whole task. Recheck evidence affected by integration or repairs.
If required independent review is unavailable, report that gap rather than calling self-review
independent. Continue locally when optional delegation adds no value or is unavailable.
