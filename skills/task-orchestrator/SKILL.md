---
name: task-orchestrator
description: Guide coding changes that need explicit evidence and risk decisions, including uncertain bugs and changes across shared boundaries. Use a domain or review skill directly when sufficient.
---

# Task orchestrator

Resolve links here; pack root: two levels above unless supplied. Report inaccessible guidance.

Start with one agent. Add structure only to resolve a concrete uncertainty, failure mode or coordination need. Honor scope and existing edits; investigation, proposals and reviews do not authorize implementation. No routine planning, team or model-selection menus.

Before editing, locate the affected path, callers, tests and repository conventions. Implement understood local changes directly; use the references below when uncertainty or consequence warrants more structure. Planning and delegation are optional; reassess when evidence changes scope or risk.

Before changing behavior, identify what could fail, its consequence and the evidence needed to detect it. For consequential or uncertain changes, use [Risk and evidence](references/risk.md); routine local changes need only a proportionate check. Risk changes verification depth, not permission to delegate. Load only matching references:

| Trigger | Read |
| --- | --- |
| Spring Boot implementation, debugging or review | [Spring Boot](../spring-boot/SKILL.md) |
| Bug diagnosis, unfamiliar execution path or uncertain impact | [Investigation](references/investigation.md) |
| Substantial implementation, refactoring, architecture or security-sensitive change | [Delivery](references/delivery.md) |
| Coordinating permitted delegation | [Execution](references/execution.md) |
| Missing task context or resuming incomplete work | [Context](references/context.md) |
| Failed checks or interrupted work requiring repair | [Recovery](references/recovery.md) |
| Applicable saved lessons supplied by user/project guidance | [Learning](references/learning.md), retrieval only |
| Work spanning multiple repositories | [Coordination](references/multi-repo.md) |
| Requested or required code review | [Review](../review-workflow/SKILL.md) |
| Spec-driven requested or required by project instructions | [Spec](references/spec-driven.md); await draft approval |
| Explicit Herdr | [Herdr](references/herdr.md) |

Select domain skills only for the affected stack or boundary. Reuse unchanged guidance; never preload links, README or roles. Use Codex's native planning, context management and delegation when helpful; this pack adds decision guidance, not a replacement agent loop or task-state system.

## Final verification gate

Inspect final changes against criteria; report actual checks, gaps and consequential decisions.
Self-review is not independent review. Essential gaps prevent verified completion.

## Optional learning after acceptance

Report the result without requiring a final user-acceptance ceremony. If the user explicitly accepts it, that permits loading
[lesson proposal and storage](references/learning.md#capture-only-evidence-backed-candidates); silence, passing checks and earlier
code approval do not count. Propose a lesson only when useful; saving it requires separate approval.
