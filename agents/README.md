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

Every worker receives the absolute pack root, assigned role path, target repo/worktree, outcome, complete assigned criteria, ownership, applicable decisions, prerequisite results and allowed checks. Final integration reviewers receive the whole task's criteria and binding decisions. Settings are resolved by the coordinator through [model routing](model-routing.md); workers use the assignment's settings.

Give a complete, narrow assignment instead of the whole conversation or all role contracts. Workers read relevant source themselves, ask for specific missing facts and return results, actual checks and unresolved issues. Finishing an assignment does not approve the overall task.

Workers never delegate further. Only implementer writes within assigned scope; other roles stay read-only and return findings without creating report files. One writer per checkout; parallel writers need separate workspaces and resource ownership. The coordinator handles questions, integration and the [final verification gate](../skills/task-orchestrator/SKILL.md#final-verification-gate). Track active ownership in the conversation or a requested handover; no task-state schema is required.
