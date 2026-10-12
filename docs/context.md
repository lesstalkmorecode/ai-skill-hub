# Context size

- Load the entrypoint when invoked.
- Read other files only for their listed triggers.
- Reuse unchanged guidance already in the conversation.
- Do not recursively read every linked file.
- Workers receive their role and task facts, not README or the whole router.
- API and database rules come from the target project.

- Counts include Markdown and frontmatter.
- They use whitespace-separated words, like `wc -w <file>`.
- Recount after editing a listed file.
- These are instruction sizes, not measured model usage.

| File | Words | Load when |
| --- | ---: | --- |
| [Entry](../skills/task-orchestrator/SKILL.md) | 191 | Once when the shared workflow is invoked |
| [Delivery](../skills/task-orchestrator/references/delivery.md) | 136 | Substantial implementation |
| [Investigation](../skills/task-orchestrator/references/investigation.md) | 91 | Unexplained failure or diagnosis |
| [Execution](../skills/task-orchestrator/references/execution.md) | 176 | Actual delegation |
| [Worker routing](../agents/model-routing.md) | 149 | Coordinator resolving worker settings |
| [Implementer](../agents/implementer.md) | 149 | Assigned implementation worker; not all roles |
| [Context](../skills/task-orchestrator/references/context.md) | 133 | Missing information or substantial resume |
| [Multi-repo](../skills/task-orchestrator/references/multi-repo.md) | 304 | Cross-repo behavior |
| [Review](../skills/review-workflow/SKILL.md) | 367 | Requested/required review |
| [Recovery](../skills/task-orchestrator/references/recovery.md) | 198 | Failed check, material finding or repeated repair |
| [Preferences](../skills/task-orchestrator/references/preferences.md) | 201 | Manual or user-selected saved settings |
| [Spec-driven](../skills/task-orchestrator/references/spec-driven.md) | 1161 | Explicit Spec-driven mode; draft approval required |
| [Herdr](../skills/task-orchestrator/references/herdr.md) | 452 | Explicit visible-pane runtime |
| [Handover](../skills/ai-handover/SKILL.md) | 204 | Requested continuation/transfer note |

## Example reading paths

- Each example counts each listed file once.
- These are possible reading paths, not mandatory startup bundles.
- The delegated example spans coordinator and one worker.
- Repeated reads and billed inputs are not included in these totals.

| Situation | Words | Included files |
| --- | ---: | --- |
| Small direct change | 191 | Entry |
| Substantial direct implementation | 327 | Entry + delivery |
| Unexplained bug, then substantive fix | 418 | Entry + investigation + delivery |
| One delegated assignment with missing-context guidance | 934 | Implementation path + execution + routing + context + implementer |

## Words are not tokens

- Words and tokens are different units.
- Tokenization depends on the model and input, including code and Markdown.
- Exact counts need the model's tokenizer and complete input.
- These word counts do not prove token savings.

The tables exclude:

- Loader, runtime instructions and discovery metadata.
- Project rules, source code and task assignments.
- Conversation history and tool output.
- Repeated context across workers, reviews and retries.

Previously read text remains in the conversation. Avoiding rereads does not make later requests free. Measure total coordinator and worker usage when the runtime exposes it.

## What earns its place in context

- Shared rules cover scope, ownership, diagnosis and integration.
- Project facts define the actual contract, compatibility and allowed checks.
- Keep project facts in the task and project guidance.
- Do not duplicate them across every role.

- Workers need all assigned criteria, binding decisions and prerequisite results.
- Final review needs the whole task's criteria and relevant decisions.
- Never remove essential facts just to shorten a prompt.
- Evaluate scope mistakes, repair attempts, user corrections and verified outcomes.
- Smaller files alone do not prove better results.

