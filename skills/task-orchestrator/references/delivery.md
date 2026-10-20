# Delivery

## Select an approach

Start with one agent and add structure for a concrete uncertainty or risk. Use [investigation](investigation.md) for bugs, unfamiliar behavior or uncertain impact; understood paths need no separate investigation. A small diff can affect a critical boundary; a broad mechanical change can remain straightforward.

| Task | Useful approach and evidence |
| --- | --- |
| Bug fix | Follow [bug diagnosis](investigation.md), then check the correction for recurrence and nearby behavior. |
| Feature | Find the closest existing behavior and extension point; define observable success and failure cases. Implement a narrow end-to-end slice, then extend it while preserving existing consumers. |
| Refactor | Identify invariant behavior and affected callers first. Use existing tests or targeted characterization for uncovered behavior; make small structural steps and keep intentional behavior changes separately reviewable. |
| Architectural change | Compare the smallest viable options at the affected boundaries. Resolve dependency direction, interface ownership, migration and compatibility questions in a short plan before dependent edits. Use an architect only if its focused answer adds value. |
| Security-sensitive change | Trace untrusted inputs, trust boundaries, authorization and sensitive outputs. Verify denied as well as allowed paths and relevant abuse cases without exposing secrets or exercising unauthorized systems. Seek independent review when consequence or uncertainty warrants it. |

Combine approaches when needed. A complex-task plan identifies unresolved questions, implementation slices, dependency order and checks. Plan in the main session unless a focused assignment adds value; revisit affected decisions as evidence changes.

Independent review is most useful for consequential security boundaries, data loss, concurrency, shared contracts, difficult migrations or weak verification. Select a reviewer for the actual risk; add another only for a distinct question. Routine well-understood changes normally need self-review and focused checks. Honor required review; disclose unavailable independence and its effect on completion rather than relabeling self-review.

## Implement and verify

State observable acceptance conditions, boundaries and intended checks in the conversation, grounded in source and project conventions. No spec file or new approval gate is required; explicit [Spec-driven](spec-driven.md) retains draft approval.

Make the smallest coherent diff that satisfies the behavior. Preserve public contracts, existing behavior and user edits unless the task explicitly changes them. Reuse established abstractions and dependencies; avoid unrelated cleanup, speculative generalization and documentation without a maintenance or user need. Follow the target project's conventions for errors, resource cleanup and generated artifacts. Check relevant invalid inputs, partial failures and edge cases; do not hide failures to make a check pass.

Implement incrementally and run focused checks early. Establish a relevant pre-change baseline when practical; distinguish existing failures from regressions. Use project migration conventions for changed contracts or data.

Choose verification by what could fail: a local logic change may need a focused unit check; changed interfaces need consumer checks; persistence, authentication, concurrency or user-interface behavior may need integration or manual evidence. Tests should assert observable behavior, not mirror implementation. Use the project's existing tools and broaden checks when impact or failures justify it. Respect offline, cost and execution limits; report unavailable checks instead of silently weakening coverage.

For the [final verification gate](../SKILL.md#final-verification-gate), inspect the final diff and relevant untracked files. Match each criterion to final-state evidence or mark it unfinished/unverified; name untested behavior and recheck affected results after later edits. Explain consequential tradeoffs. Required independent review and [combined multi-repo checks](multi-repo.md#verify-together) remain required. Commit, push and publication require task authorization.
