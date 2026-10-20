# Optional worker roles

The main agent normally performs planning, architectural reasoning, implementation and test design.
Only two reusable leaf contracts are supplied:

| Contract | Assignment |
| --- | --- |
| [implementer](implementer.md) | Bounded implementation with explicit ownership and actual verification. |
| [reviewer](reviewer.md) | Independent read-only assessment of a concrete engineering question or diff. |

Use [risk and evidence](../skills/task-orchestrator/references/risk.md#decide-whether-to-delegate)
to decide whether authorized delegation adds value, then
[assignment and integration](../skills/task-orchestrator/references/execution.md) for the actual
assignment. Roles are optional capabilities, not pipeline stages. Native runtime defaults apply.
Workers return evidence and limits; the main agent owns integration and the final claim.
