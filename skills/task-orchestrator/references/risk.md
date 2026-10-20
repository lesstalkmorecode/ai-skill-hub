# Risk and evidence

Use consequence, reach, reversibility and uncertainty to choose evidence. File count and task
labels are weak proxies. A one-line authorization change can be high risk; a broad mechanical
rename can have predictable impact. Classify only as far as it helps choose the next check;
no numeric score, separate risk report or approval ceremony is required.

## Choose verification

| Observed conditions | Evidence to seek | Coordination |
| --- | --- | --- |
| Local, understood, reversible; no shared contract or sensitive state | Inspect the final diff and closest consumers; run a focused existing check or static validation suited to the change. Documentation-only work may need link/configuration checks rather than application tests. | Main agent; no separate plan or review worker needed. |
| Shared API, several consumers, unfamiliar path or external boundary | Trace affected callers; check success and relevant failure cases at the boundary. Use contract/integration evidence when mocks cannot expose the failure. Characterize uncovered behavior before a refactor when useful. | Keep coupled work local. A bounded investigation or independent review can help if it resolves a named uncertainty. |
| Authorization, sensitive data, irreversible migration, money, concurrent writes, broad rollout or difficult rollback | Identify the concrete failure (e.g. cross-tenant access, duplicate charge, data loss). Exercise denied/adversarial paths, retry/interleaving behavior or migration/compatibility checks as appropriate in an authorized environment. Inspect recovery/rollback feasibility. | Consider an independent reviewer for the specific failure mode when permitted; risk alone never mandates a team. Honor any user/project requirement for independence. |

Use the most consequential applicable row, then select only checks relevant to that failure.
Existing tests are evidence only for the paths they exercise. Source inspection can establish
structure, but cannot prove database isolation, token validation or a deployed interaction.
Do not add tests that merely restate implementation or mandate the whole suite for every edit.

Keep the evidence trail concise: **claim → source or check → observed result → limit**. For example:
"Retries create one order: concurrent requests with the same key returned one persisted ID in
the integration fixture; payment-provider retries were not exercised." For substantial work,
record criteria and checks in chat; use durable artifacts only when needed or requested.

## Decide whether to delegate

Dispatch only if delegation is authorized by the user/project and runtime, and all apply:

- There is a bounded question or outcome whose value exceeds dispatch and integration cost.
- Inputs are available; the worker can proceed without an unresolved main-session decision.
- Ownership and validation can be defined, and the returned evidence can be integrated.

Useful examples: independently inspect a tenant-isolation change, investigate a separate failing
consumer, or implement a stable independent module in a separate workspace. Keep a small local
fix, a tightly coupled refactor, or a bug still missing its reproduction in the main session.
Do not dispatch planners, architects or test planners just because those roles exist.

Select one role for the missing capability; add a second only for a distinct question. For an
actual dispatch, load [Execution](execution.md). Inherit runtime model/effort defaults unless
explicit constraints require otherwise. A larger model or more workers is not verification.

## Reassess and finish

Increase verification when evidence reveals additional consumers, irreversible effects, a weak
reproduction, surprising failures or a broader trust boundary. Reduce speculative process when
inspection establishes a local, covered change. After an edit or integration, rerun affected
checks; old passing output does not verify new behavior.

Before reporting completion, inspect the integrated final diff (including relevant untracked
files) and match material claims to current evidence. Missing optional checks are disclosed
limits; missing essential evidence or unresolved material findings prevent verified completion.
If required independent review is unavailable, name that gap. Otherwise use direct review and
available checks, without claiming independence. Never perform a live destructive experiment
or change permissions merely to fill an evidence gap.
