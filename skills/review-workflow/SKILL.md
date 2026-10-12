---
name: review-workflow
description: Review code or a diff without edits, directly or with explicitly permitted independent reviewers.
---

# Review workflow

Honor the supplied target, team and validation limits. With no target, assume the current staged/unstaged and relevant untracked changes and state that assumption. For a branch or PR establish the comparison base; for a file target inspect it even without a Git diff. If nothing is available to review, report that rather than inventing findings.

Read the applicable repo guidance, complete assigned target and necessary nearby code. Inspect actual code independently of implementation summaries. Review-only means no edits, reverts, tooling installation, report-file creation or published comments.

Review directly unless independent workers are requested, useful and permitted. A correctness reviewer covers behavior, criteria and maintainability. Add a risk reviewer only for a distinct relevant risk. Resolve actual worker settings through [model routing](../../agents/model-routing.md). Delegated reviewers apply their assignment and return findings; they never dispatch more agents. Disclose unavailable required independence.

If the user requests the legacy menu, A means current diff plus one reviewer, B adds a risk reviewer, and C specifies a custom target. Do not show that menu for ordinary requests.

Task reviewers receive complete assigned criteria, binding decisions, target/base and relevant evidence. Final integration review receives all criteria and relevant decisions across the task and participating repos. Partial reviews do not replace that whole-task check. If the target changes during review, identify the mismatch and inspect the affected new state before carrying findings forward.

For Spec-driven assignments, use the exact approved baseline and approval reference. Review every assigned criterion and return implementation/evidence gaps; final review covers every approved criterion under the [coverage gate](../task-orchestrator/references/spec-driven.md#mandatory-spec-coverage-and-completion-gate). A clean diff review alone does not establish spec coverage.

Return actionable findings first: severity, file/line, realistic trigger, consequence and concrete correction. Deduplicate overlap and separate uncertain questions from confirmed bugs. Include the reviewed state, actual checks and meaningful limits. State when no actionable findings were found.

Return findings to the coordinator for authorized fixes. Read-only workers return concise evidence and existing artifact references; the coordinator may persist reports at an authorized path if needed. Re-review affected corrections when assigned using [recovery](../task-orchestrator/references/recovery.md). Review completion does not approve or implement the target.
