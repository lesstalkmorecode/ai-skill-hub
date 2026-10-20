---
name: task-execution
description: Choose proportionate investigation, failure-mode evidence, and authorized delegation for uncertain or consequential coding changes. Ordinary fixes and direct skills need no task-execution guidance.
---

# Task execution

This is optional decision guidance, not a replacement for Codex's native loop. Keep normal work
in the main agent. Understand → explore → decide → act → verify → recover describes adaptive
behavior, not six mandatory stages, documents or approval gates.

Use [risk and evidence](references/risk.md) to decide what uncertainty to resolve and what check
could expose a consequential failure. An understood local fix can proceed directly; an unknown
bug needs distinguishing evidence before a patch. Reassess when observations contradict assumptions.

Load additional guidance only when it changes a concrete decision:

- Actual authorized delegation: [assignment and integration](references/execution.md).
- Requested code review: [review-workflow](../review-workflow/SKILL.md), directly in the main session by default.
- Requested or project-required spec work: [spec-workflow](../spec-workflow/SKILL.md), the sole spec lifecycle, approval and coverage authority.
- Spring Boot behavior: [spring-boot](../spring-boot/SKILL.md), only the affected domain topics.

Use native planning, tools and context management. Do not preload linked guidance, create task
state files, select a team by default or add an acceptance ceremony to ordinary coding.
Repository instructions and current authorization determine scope; an investigation or review
request remains read-only. Report final-state evidence and meaningful limits; missing essential
evidence prevents a verified-completion claim.
