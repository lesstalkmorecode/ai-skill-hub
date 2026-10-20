---
name: review-workflow
description: Review code or a diff directly without edits and return prioritized, evidence-backed findings. An independent worker is optional when authorized and useful.
---

# Read-only review

Review directly in the main session by default. Honor the supplied target and validation limits.
Without a target, state the assumption that staged, unstaged and relevant untracked changes are
in scope. Establish the base for a branch/PR; inspect a supplied file even without a diff. If no
review target is available, say so rather than inventing findings.

Read applicable repo guidance, the complete assigned target and necessary nearby code. Inspect
actual code independently of implementation summaries. Assess correctness, architecture, security,
concurrency, data integrity, performance or test coverage as relevant to the assignment. Use
[risk and evidence](../task-orchestrator/references/risk.md) for consequential failure modes;
load [Spring Boot](../spring-boot/SKILL.md) topics only for that stack. Do not turn every concern
into a separate worker. Independent review requires both authority and concrete benefit under
the linked delegation criteria; disclose unavailable required independence.

Review-only means no edits, reverts, tooling installation, report-file creation or published
comments. Run only permitted checks that respect those boundaries. Instructions do not enforce
access: see [permission limits](../../docs/controls.md#permission-limits) when enforced read-only
is required. A role name alone provides no sandbox.

For spec assignments use [spec-workflow coverage](../spec-workflow/SKILL.md#coverage-and-completion)
with the exact approved baseline and every assigned criterion. Partial reviews do not replace a
whole-task integration review. If the target changes, identify the mismatch and re-review affected
new changes before carrying conclusions forward. A clean diff alone does not prove criteria.

Return actionable findings first: severity, file/line, realistic trigger, consequence and suggested
correction, supported by source or a concrete check. Deduplicate overlap; distinguish confirmed
bugs from open questions. Include the reviewed revision/working state, actual checks and limits.
State when no actionable findings were found. Return to the requester or main agent for any
separately authorized fixes; review completion does not implement or approve the target.
