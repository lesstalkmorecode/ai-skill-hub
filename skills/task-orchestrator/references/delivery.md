# Delivery

For substantial implementation, turn the requested behavior into observable acceptance conditions using actual source and project conventions. Keep boundaries and intended checks in the conversation; no mandatory spec file or new approval gate. Explicit [Spec-driven](spec-driven.md) retains draft approval.

For refactors, identify behavior that must remain unchanged. Make coherent changes with focused checks early enough to expose wrong assumptions. Avoid unrelated cleanup. Follow the target project's guidance for affected contracts and migrations.

Before closing, inspect the final diff and relevant untracked files. Match each criterion to actual final-state verification, or mark it unfinished/unverified. State what checks leave untested; recheck affected results after later edits. Explain consequential tradeoffs through the changed code. Required independent review and combined multi-repo checks remain required; a passing test does not prove all criteria. Commit, push and publication require task authorization.
