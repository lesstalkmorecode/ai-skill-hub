# Worker roles

Load only the assigned contract. [task-orchestrator](../skills/task-orchestrator/SKILL.md) coordinates work when requested; these roles are optional helpers, not a mandatory pipeline.

| Contract | Responsibility |
| --- | --- |
| [implementer](implementer.md) | Make scoped changes and check them |
| [reviewer](reviewer.md) | Independently review correctness |
| [risk-reviewer](risk-reviewer.md) | Examine relevant failure paths and regressions |
| [planner](planner.md) | Clarify requirements and dependencies |
| [architect](architect.md) | Answer consequential design questions |
| [test-planner](test-planner.md) | Propose useful acceptance checks |

The coordinator follows [Execution](../skills/task-orchestrator/references/execution.md) for assignment inputs, ownership, permissions and integration, and [worker settings](model-routing.md) only for explicit overrides or compatibility problems. Runtime defaults are otherwise inherited. These are coordinator references, not extra documents every worker must load.

Workers inspect relevant source and return results, actual checks and unresolved issues. Only implementer writes within assigned scope; other roles stay read-only. Workers never delegate or approve the overall task. The coordinator handles questions and the [final verification gate](../skills/task-orchestrator/SKILL.md#final-verification-gate); no task-state schema is required.
