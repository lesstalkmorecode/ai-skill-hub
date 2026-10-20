# AI Skill Hub

Lean Agentic Coding guidance for Codex: single-agent-first, evidence-driven, risk-adaptive and
selectively multi-agent. Codex supplies planning, tools, context management, compaction and the
execution loop. This package supplies decisions that need engineering judgment, optional domain
knowledge and two reusable worker contracts. It is not another orchestration framework.

## Architecture

Normal work stays in the main agent. Understand → explore → decide → act → verify → recover is
an adaptive behavioral model, not a required sequence of stages. A known local fix needs inspection,
a change and focused verification; an unknown bug needs distinguishing evidence before a patch.
Consequence, reach, reversibility and uncertainty determine evidence depth, never file count or
team size. See [risk and evidence](skills/task-orchestrator/references/risk.md) and the
[workflow guide](docs/workflow.md).

| Skill | Responsibility |
| --- | --- |
| [task-orchestrator](skills/task-orchestrator/SKILL.md) | Optional investigation, risk, verification and delegation decisions for uncertain or consequential changes. |
| [review-workflow](skills/review-workflow/SKILL.md) | Direct read-only review with actionable findings; no required worker. |
| [spec-workflow](skills/spec-workflow/SKILL.md) | Sole spec lifecycle, approval, storage and criterion-coverage authority when requested or required. |
| [spring-boot](skills/spring-boot/SKILL.md) | Optional framework guidance matched to actual project versions and affected topics. |

Use a skill directly when sufficient. Ordinary Codex tasks do not need this package's orchestrator.
Load only relevant guidance. Learning and session transfer are outside the coding loop.

Only two optional [worker roles](agents/README.md) remain:

| Role | Assignment |
| --- | --- |
| `implementer` | Bounded independent implementation with owned paths and actual checks. |
| `reviewer` | Independent read-only review of assigned correctness, design, security or other engineering concerns. |

The main agent handles planning, architecture, risk analysis and test design. Delegation requires
user/project authorization, runtime permission and a concrete benefit exceeding coordination cost.
High risk alone does not require a team. Workers inherit native runtime model/effort defaults;
explicit supported user preferences are honored without a model-routing subsystem.

## Use from source

Keep a checkout of this repository and open your target application in Codex:

```text
Use /absolute/path/to/ai-skill-hub/skills/task-orchestrator/SKILL.md.
Pack root: /absolute/path/to/ai-skill-hub.
Target project: the current workspace.
Fix duplicate orders when a request is retried and verify overlapping requests.
```

Or request a direct skill, such as `Use review-workflow to review the authentication diff without
edits.` For spec approval before coding, request `Use spec-workflow to propose order cancellation.`
It presents a draft and waits for explicit approval; ordinary fixes acquire no new approval gate.

After updating guidance, start a new chat or explicitly request a reread. The target repository's
instructions, versions and tools apply; this package does not silently rewrite them.

## Plugin packaging and optional agents

The root `plugin.json` describes the package. Skills are discovered under `skills/`; shared
contracts and references remain alongside them. Distribution uses the client's marketplace
configuration; see the [official plugin guide](https://developers.openai.com/plugins/build/plugins).
Stage a clean copy excluding credentials, lessons, local reports and machine settings. The manifest
and `.gitignore` do not filter private files out of a distribution.

Named workers are optional and registered separately. See [Codex setup](adapters/codex/README.md#register-named-agents)
for selecting and copying an adapter without replacing existing user configuration. Installation
does not automatically grant delegation permission or enforce read-only review.

## Optional extras

[Session transfer](docs/session-transfer.md) is a short note only when needed; no handover skill
or automatic file writing exists. [Lessons](docs/learning.md) are read only when supplied and
saved only when requested with appropriate authorization. No memory scan or final acceptance
ceremony belongs to coding completion. Keep private knowledge outside distributable packages.

## Development and validation

Follow [AGENTS.md](AGENTS.md). Canonical agent TOMLs and the regular `.codex/agents/` copies must
match. From this checkout, using Python 3.11+ (no third-party Python dependencies):

```bash
python -m evals.validate
python -m unittest discover -s evals/tests -v
git diff --check
```

Use `python3` if that is your interpreter name. Checks cover syntax, frontmatter, internal links,
role inventories and adapter consistency. The [evaluation guide](evals/README.md) separates those
checks from safe opt-in behavioral runs and package audits. See [controls](docs/controls.md) for
permission boundaries. Claim → evidence → observed result → remaining limitation applies to
completion reports; static checks do not establish agent behavior or measured efficiency gains.
