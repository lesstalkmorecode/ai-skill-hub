---
name: spec-workflow
description: Explore, propose, apply, sync, or archive requested spec changes using the target repository's configured spec lifecycle.
---

# Spec workflow

Use the action matching the user's request: explore, propose, apply, sync, or archive. A request for one action does not authorize the others. Ask only for missing action or change context when it cannot be inferred. When called by task-orchestrator, follow its task contract and return results to it; delegated workers remain leaf assignments.

Read the target repository's guidance and spec configuration. All paths below belong to that repository, not the central skill pack. This profile uses `spec/project.md`, `spec/current/`, `spec/changes/<change-name>/`, and `spec/archive/`. Use it only when configured; otherwise follow the target's lifecycle or return the context to task-orchestrator for [Spec-driven drafting](../task-orchestrator/references/spec-driven.md). That reference owns draft storage, explicit approval, coverage and final reporting. Do not initialize a framework or silently impose this layout.

## Explore

Read `spec/project.md`, current behavior in `spec/current/`, active changes in `spec/changes/`, and relevant recent history in `spec/archive/`. Summarize current behavior, proposed changes, differences, and open questions grounded in those files. Stay read-only; do not implement, sync, or archive.

## Propose

Read `spec/project.md` and the selected requirement source. For Jira input, use an available connector or user-provided issue details; consider title, description, acceptance criteria, comments, attachments, and linked issues where relevant and accessible. For text input, use the supplied requirements. Follow the user and repository decision about the source of record. Treat Jira and text as requirement inputs; record material conflicts under Open Questions rather than silently choosing one.

Create a narrow change under `spec/changes/<change-name>/` with:

- `proposal.md`: goal, constraints, explicit non-goals, assumptions, and open questions.
- `design.md`: implementation approach and relevant design decisions.
- `tasks.md`: small, testable implementation steps and applicable verification commands.
- `spec.md`: observable user-facing behavior, acceptance criteria, and scenarios.

Do not invent product requirements. Record reasonable assumptions or missing acceptance criteria explicitly. Keep traceability through issue links or concise source references when useful; avoid duplicating entire requirement sources. Do not implement application code, sync living specs, or archive the proposal.

Present the draft for explicit approval under the [Spec-driven approval gate](../task-orchestrator/references/spec-driven.md), then stop before implementation. When delegated, return it to task-orchestrator to present and obtain approval.

## Apply

Implement only an approved change from `spec/changes/<change-name>/`. Read `spec/project.md` and every file in that change. Honor acceptance criteria, constraints, and non-goals. Update or add relevant tests with code changes and run allowed checks within user and repository validation constraints. Report skipped or unavailable checks.

Apply does not authorize proposal creation, automatic sync, or automatic archive. Return implementation evidence for the orchestrator's review and final verification.

Return evidence under the [mandatory coverage gate](../task-orchestrator/references/spec-driven.md#mandatory-spec-coverage-and-completion-gate).

## Sync

For an authorized sync after behavior is complete, read the relevant change artifacts, current living specs, and completion evidence. Update only affected files in `spec/current/` so they reflect completed product behavior. Preserve unrelated current specs and all archived changes. Do not implement unfinished code or archive the change.

## Archive

For an authorized completed change, verify completion evidence and move `spec/changes/<change-name>/` to `spec/archive/<change-name>/` using target-repository conventions. Mark tasks complete only when supported by the actual final state. Preserve the artifacts and existing archived history; do not overwrite another archive. Archive does not authorize changes to living specs; perform a separately requested sync first when required.

## Output

Report the selected action, change name where applicable, behavior or artifacts inspected, files changed, actual verification, unresolved assumptions, and remaining work. A proposal is not an approved implementation; applying code does not imply specs were synced or archived.

In Spec-driven mode, use the final response requirements in the linked reference. Delegated workers return evidence to the coordinator rather than issuing the overall final response.

Use this skill directly when the spec action is sufficient, or let task-orchestrator load it for requested Spec-driven work. Ordinary coding does not require this workflow.
