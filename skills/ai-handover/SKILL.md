---
name: ai-handover
description: Prepare a short continuation note for unfinished work or a requested transfer between agents or sessions.
---

# AI handover

Return enough current information to continue without replaying the whole conversation. Use conversation output by default; save Markdown only when requested at an authorized path. Read-only reviews never write into the target repository.

Include the relevant parts:

- Requested outcome, boundaries and unresolved acceptance criteria.
- Repo/worktree paths, branches and changed files.
- Completed work and binding decisions, with source or evidence references.
- Checks actually run, results and skipped checks; identify results affected by later changes.
- Open findings, missing information, blockers and the next concrete step.
- Active worker/pane identities, ownership and unfinished assignments when relevant.
- Approved spec and approval reference when Spec-driven mode applies.

Link useful source and logs instead of copying transcripts. Preserve exact user decisions, uncertainty and authorization boundaries. Exclude credentials. A handover does not start a worker, message another chat or approve unfinished work.

The receiving agent inspects current Git/code state and applicable project guidance before acting. It verifies active worker liveness before restarting work and repeats checks affected by edits. Historical notes are context, not proof that the current result is verified.
