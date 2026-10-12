# Working with other agents

Use a worker for a separable change, specific question or required independent review, subject to runtime permission. Roles are optional, not pipeline stages. Honor explicit single-agent/team choices. Legacy `Direct multi-agent` means implementation plus independent review; `Manual` selects a team. Explicit Herdr loads [Herdr](herdr.md).

Resolve settings through [routing](../../../agents/model-routing.md). Give each worker pack/role paths, repo/worktree, outcome, full assigned criteria, write boundaries, binding decisions, prerequisite results and allowed checks. Load only its role. Prefer fresh/minimal history; disclose unsupported settings or history isolation. Workers inspect source and return results; they never delegate further.

One writer per checkout. Parallel writers need separate workspaces and non-conflicting ports, databases and generated artifacts. Start dependent work only after prerequisites are available. Track identities/ownership in chat; inspect liveness before relaunching after timeout or interruption.

Role instructions do not enforce permissions. Verify actual runtime controls when a task requires a sandbox or disabled tools; report unavailable protection before dispatch. For Codex, use the [permission limits](../../../docs/controls.md#permission-limits), including a separate read-only session when enforced review isolation is required.

Final integration review receives every criterion and relevant decision across repos. Required unavailable independence is a gap. Read-only workers return findings and existing references without writing reports. Writers save logs only within authorized paths. Reuse valid context and evidence; recheck affected results after integration or fixes.
