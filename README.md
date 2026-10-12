# AI Skill Hub

AI Skill Hub packages reusable coding instructions as a local Codex plugin. It helps Codex
investigate problems, implement changes, review code, work from approved specifications, and
hand over unfinished tasks. It also includes technical guidance for Spring Boot applications.

This personal project supports daily development and practice in designing agent workflows.
Codex performs the work using its available tools; the repository supplies Markdown skills,
optional worker definitions, and a portable plugin manifest.

## How it works

Start with `task-orchestrator` or invoke a skill directly. Codex reads the relevant project rules
and skill instructions, then uses the application's tools and tests. Each skill can load detailed
`references/` guidance for the topic at hand, such as transactions or authentication.

### Skills

| Skill | Purpose |
| --- | --- |
| [task-orchestrator](skills/task-orchestrator/SKILL.md) | Coordinate task scope, relevant guidance, permitted delegation, and final verification. |
| [spring-boot](skills/spring-boot/SKILL.md) | Guide implementation, debugging, and review using the application's versions and conventions. |
| [review-workflow](skills/review-workflow/SKILL.md) | Produce prioritized code review findings without applying fixes. |
| [spec-workflow](skills/spec-workflow/SKILL.md) | Explore, propose, implement, sync, or archive specifications under the project's conventions. |
| [ai-handover](skills/ai-handover/SKILL.md) | Prepare a continuation note with decisions, current state, checks, and remaining work. |

### Worker roles

The main Codex agent can perform a task itself or assign a scoped part to a worker when permitted.
These roles apply to application work and development of the plugin; they are optional assignments.

| Role | Assignment |
| --- | --- |
| `planner` | Clarify requirements, dependencies, and implementation steps. |
| `architect` | Assess design decisions and module boundaries. |
| `implementer` | Make changes within assigned ownership and verify them. |
| `reviewer` | Independently assess correctness and maintainability. |
| `risk-reviewer` | Examine security risks, failure paths, and regressions. |
| `test-planner` | Propose acceptance and regression checks without running them. |

Workers return results to the main agent for integration. Only `implementer` is instructed to edit
files. To use roles by name, follow [Optional: register named agents](#optional-register-named-agents).

## Use from source

Keep a local checkout of this repository. Open your application, the **target repository**, in
Codex and provide the skill path and pack root:

```text
Use /absolute/path/to/ai-skill-hub/skills/task-orchestrator/SKILL.md.
Pack root: /absolute/path/to/ai-skill-hub.
Target project: the current workspace.
Fix duplicate orders when a request is retried and run the relevant tests.
```

Codex reads the central instructions and works in the target repository using that project's tools.
After changing guidance, start a new chat or explicitly request a reread.

## Plugin packaging

The root `plugin.json` identifies the package. Skills are discovered under `skills/`; shared role
contracts and references remain alongside them. Plugin distribution uses the client's marketplace
configuration; follow the [official packaging guide](https://developers.openai.com/plugins/build/plugins).
Use a clean checkout for distribution, excluding local lessons, credentials, and machine settings.

### Optional: register named agents

To request a role by name, such as `reviewer`, copy its TOML definition from
`adapters/codex/agents/` to the target repository's `.codex/agents/` directory or your personal
`~/.codex/agents/` directory. Plugin installation does not perform this step. Follow the
[named agent registration instructions](adapters/codex/README.md#register-named-agents)
for copy commands, session setup, and an example request with the hub source path.

## Usage

Open the target repository in Codex and start a new chat:

```text
Use task-orchestrator to fix duplicate orders when a request is retried.
Preserve the existing API contract and run the relevant tests.
```

For a review, use `Use review-workflow to review the authentication changes.` Investigation and
review requests produce findings without code changes; a fix or implementation request authorizes
changes within scope.

For specification approval before coding, request `Use task-orchestrator in Spec-driven mode to
add order cancellation.` Codex presents a draft for approval, then verifies the implementation
against every approved acceptance criterion. See the [workflow guide](docs/workflow.md).

### Personal learning

After you accept a completed result, Codex may propose saving a reusable lesson. Saving requires
separate approval. Lessons stay in the hub checkout's gitignored `learning/` directory and must
be excluded from distribution. Provide the source path when using this feature; see [learning](docs/workflow.md#learning).

## Development

Edit the hub checkout to change the plugin. Follow the repository's `AGENTS.md`; skills belong in
`skills/`, worker contracts in `agents/`, and Codex definitions in `adapters/codex/agents/` with
matching `.codex/agents/` copies.

Validate the manifest, skill frontmatter, Markdown links, and matching agent definitions after
changes. Use the target repository's own checks for application behavior. See
[permissions and verification](docs/controls.md) for verification guidance and permission limits.

Run `python -m evals.validate` and `python -m unittest discover -s evals/tests -v`
with Python 3.11+ for offline package and checker verification. The
[evaluation guide](evals/README.md) documents deterministic CI, staged-package
auditing, and three explicitly opted-in live Codex scenarios in disposable containers.
