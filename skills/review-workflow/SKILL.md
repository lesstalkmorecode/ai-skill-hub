---
name: review-workflow
description: Review code or a diff without edits, directly or with explicitly permitted independent reviewers.
---

# Review workflow

Honor the supplied target, team and validation limits. With no target, assume the current staged/unstaged and relevant untracked changes and state that assumption. For a branch or PR establish the comparison base; for a file target inspect it even without a Git diff. If nothing is available to review, report that rather than inventing findings.

Read the applicable repo guidance, complete assigned target and necessary nearby code. Inspect actual code independently of implementation summaries. Review-only means no edits, reverts, tooling installation, report-file creation or published comments.

These boundaries are instructions, not a sandbox. When enforced read-only access is required, verify the session's actual permissions before reviewing; disclose unavailable enforcement. Codex workers inherit parent permissions; follow the [permission limits](../../docs/controls.md#permission-limits) for a separate restricted review session.

For Spring Boot targets, apply [Spring Boot](../spring-boot/SKILL.md) and only relevant references within these read-only boundaries.

Review directly by default. Use [risk and evidence](../task-orchestrator/references/risk.md) when consequences or uncertainty need deeper checks or a decision about permitted independent review. A correctness reviewer covers behavior, criteria and maintainability; add a risk reviewer only for a distinct question. Inherit runtime settings; read [worker settings](../../agents/model-routing.md) only for explicit overrides or compatibility problems. Delegated reviewers apply their assignment and return findings; they never dispatch more agents. Disclose unavailable required independence.

Task reviewers receive complete assigned criteria, binding decisions, target/base and relevant evidence. Final integration review receives all criteria and relevant decisions across the task and participating repos. Partial reviews do not replace that whole-task check. If the target changes during review, identify the mismatch and inspect the affected new state before carrying findings forward.

For Spec-driven assignments, follow the [coverage gate](../task-orchestrator/references/spec-driven.md#mandatory-spec-coverage-and-completion-gate) for the approved baseline, criterion coverage and evidence gaps. A clean diff review alone does not establish spec coverage.

Return actionable findings first: severity, file/line, realistic trigger, consequence and concrete correction. Deduplicate overlap and separate uncertain questions from confirmed bugs. Include the reviewed state, actual checks and meaningful limits. State when no actionable findings were found.

Return findings to the coordinator for authorized fixes. Read-only workers return concise evidence and existing artifact references; the coordinator may persist reports at an authorized path if needed. Re-review affected corrections when assigned using [recovery](../task-orchestrator/references/recovery.md). Review completion does not approve or implement the target.
