# Workflow guide

Use this guide to understand how the skills handle scope, delegation, specification approval,
and saved lessons. For installation and a first task, see the [README](../README.md).

## Task scope

The main Codex agent reads the target repository's instructions and relevant code before acting.
It follows your requested outcome, preserves existing edits, and uses the project's build and test
tools. For substantial implementation, it states the scope, acceptance criteria, and checks in
the conversation. Small tasks can proceed directly.

| Request | Expected behavior |
| --- | --- |
| Investigate or explain | Gather evidence and report the diagnosis without editing code. |
| Review | Return prioritized findings with file references and consequences, without applying fixes. |
| Fix or implement | Change the requested behavior within scope and run relevant, permitted checks. |
| Spec-driven implementation | Present a draft and wait for approval before implementation. |
| Handover | Summarize decisions, progress, checks, blockers, and next steps; save a file only when requested. |

The final response describes the result, actual verification, and remaining gaps. Passing checks
are evidence for the checked behavior; they do not establish user acceptance of the result.

## Spec-driven approval

Spec-driven mode applies when you request it or the target project's instructions require it.
Codex drafts the intended behavior, acceptance criteria, non-goals, open questions, and test plan.
It follows an existing specification process, or presents the draft in the conversation when no
file-based process is required.

You must explicitly approve the presented draft before implementation or implementation workers
start. Requested revisions produce a new draft for approval. A material change to approved scope
or behavior also requires renewed approval.

Final verification covers every approved acceptance criterion. The `Spec Coverage` report links
each criterion to implementation and check evidence, identifies unverified or partially satisfied
criteria, and reports remaining work. Syncing or archiving specifications requires the applicable
project workflow and task authorization. See the [full Spec-driven rules](../skills/task-orchestrator/references/spec-driven.md).

## Delegation

You can request `Keep this in the main session` or `Use sub-agents`. Your instructions and runtime
permissions govern delegation. Otherwise, the main agent may assign separable work when useful;
roles are selected for the assignment rather than run as a fixed sequence.

Each worker receives the absolute hub pack root, target repository or worktree, role contract,
expected outcome, assigned criteria, ownership, relevant decisions, and allowed checks. Workers
inspect relevant source and return results and verification limits to the main agent. They do not
delegate further or declare the overall task accepted.

Only implementation workers are instructed to edit their assigned files. Parallel writers need
separate workspaces and independent shared resources. The main agent integrates changes and
checks the final state; self-review is not independent review.

See [worker contracts](../agents/README.md), [model settings](../agents/model-routing.md), and
[optional Codex registration](../adapters/codex/README.md#register-named-agents). Role instructions are
behavioral rules; enforced access restrictions depend on [session permissions](controls.md#permission-limits).

## Learning

Learning stores approved guidance for future tasks. It starts after you explicitly accept the
final result: Codex may then propose a short lesson with its rule, evidence, scope, and destination.
Saving needs a separate approval; silence authorizes no write.

The default destination is `<hub-source-root>/learning/` in the source checkout. Provide that path
in the conversation or an existing user-selected local preference:

```text
AI Skill Hub source: /absolute/path/to/ai-skill-hub
```

General Spring Boot lessons use `learning/spring-boot.md`; application lessons use
`learning/projects/<project-id>.md`. The directory is created only when saving an approved lesson
and remains outside Git and plugin packages. An installed or cached plugin directory is not the
lesson destination. Without the source path, Codex continues without saved lessons and resolves
it before proposing a save.

Future relevant work reads existing general guidance and the matching application's lessons.
Project IDs distinguish separate repositories while allowing worktrees to share lessons. Moving
lessons or saving them in the target application requires explicit authorization. See the
[learning reference](../skills/task-orchestrator/references/learning.md) for identification,
retrieval, and migration rules.

## Loading guidance

Skills link to topic-specific references so Codex can read only what the task needs. For example,
Spring Boot persistence work uses the data reference; authentication work uses security guidance.
Workers receive the assigned contract and necessary task facts rather than every skill and role.
Reuse unchanged guidance, while preserving all acceptance criteria and binding decisions.

These loading rules aim to keep instructions relevant. File lengths and word counts do not
establish token savings or better outcomes; evaluate changes through real tasks and observed
verification, repairs, and user corrections.
