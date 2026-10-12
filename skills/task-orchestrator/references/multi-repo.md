# Work across repositories

Read when the requested behavior spans repos. Use each repo's guidance and existing development tools. Identify the participating checkout paths and authorized write scope; access to a repo is not permission to change unrelated projects.

## Agree on the boundary

Locate the authoritative contract, producer, consumers and generated-file conventions. Establish the expected behavior and compatibility requirements before dependent implementation. Resolve consequential product decisions with the user; use explicit spec approval only when Spec-driven mode or project guidance requires it.

Describe the work as a short dependency order in the conversation. For example: agree on an API field, align backend and SDK, update the app, then verify the combined behavior. Separate repos may proceed in parallel once their shared contract is stable and delegation is permitted.

## Connect the intended states

Assign exact repo/path ownership. One writer per checkout; separate workspaces also need non-conflicting ports, databases and generated artifacts. Consumers must use the intended local dependency version or artifact, not an unspecified latest release.

If a contract changes after dependent work starts, tell the affected owners through the authorized runtime and recheck downstream code and results. Integrate changes in dependency order, preserving existing user edits.

## Verify together

Check producer behavior, consumer compatibility and the combined user-visible outcome. Passing each repo's tests separately is not enough when the task depends on their interaction. Report the participating revisions or working-tree changes and actual checks. Final review includes all criteria and binding decisions from the whole task.

If publication is requested, establish compatible rollout order and partial-failure recovery. Local verified completion does not imply deployment or publication; no cross-repo atomic merge is assumed.

For interrupted work use [handover](../../ai-handover/SKILL.md): include completed prerequisites, pending repos, shared decisions and active ownership. Resume by inspecting actual state and worker liveness, then recheck evidence affected by later edits.
