# Working on AI Skill Hub

This is a Codex guidance package, not an orchestration runtime. Keep project content in English.
Use native planning, tools, context management and compaction. Preserve user intent, existing
edits, authorization and honest evidence; do not add mandatory stages to ordinary coding.

- `plugin.json` describes the portable package; skills under `skills/` can be invoked directly.
- Optional `task-execution` adds risk/evidence decisions, not a replacement development loop.
  Its [risk reference](skills/task-execution/references/risk.md) owns shared engineering criteria.
- `spec-workflow` alone owns spec lifecycle, storage, approval and coverage. Ordinary work needs no spec.
- `review-workflow` is directly invocable and read-only. `spring-boot` is optional domain guidance.
- Only `implementer` and `reviewer` worker contracts exist. Delegation requires authorization and
  concrete benefit. Models/effort inherit native defaults unless the user explicitly requests supported settings.
- Keep canonical TOMLs in `adapters/codex/agents/` and regular copies in `.codex/agents/` identical.
  Keep runtime behavior in adapters; do not silently install or rewrite target-project guidance.
- [Learning](docs/learning.md) is optional and outside task completion. Load only supplied applicable
  lessons; persistent writes require authorization. Exclude private local knowledge from packages.
- [Session transfer](docs/session-transfer.md) is only a short optional note, not a standalone skill.
- When changing guidance, inspect affected contracts, adapters, docs and evals for contradictions.
  Remove obsolete components and references rather than maintaining compatibility layers without value.
- Run `python -m evals.validate`, `python -m unittest discover -s evals/tests -v` and `git diff --check`.
  Validate JSON/TOML, frontmatter, links, exact role inventories and packaging. Use target-project
  checks for application behavior; static validation does not prove agent compliance.
- Keep credentials, local notes, reports, lessons and machine configuration out of commits and
  distribution. Do not claim security, productivity or token savings without observed evidence.
