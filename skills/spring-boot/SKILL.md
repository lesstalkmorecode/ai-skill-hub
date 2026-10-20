---
name: spring-boot
description: Implement, debug, or review Spring Boot services using the target project's versions, API contracts, persistence, security, and test setup.
---

# Spring Boot

Use directly or as domain guidance for an assigned role. Preserve the requested action: investigation and review remain read-only; planning does not authorize implementation. Follow any approved spec and role boundaries. Do not delegate or introduce another workflow.

## Establish the baseline

Inspect the affected module's build, wrapper, dependency management, configuration, nearby code and tests. Identify Java/Kotlin and Boot/Framework versions, Maven/Gradle, MVC/WebFlux, persistence technology, authentication and relevant CI commands. Resolve inherited versions when needed; do not infer compatibility from a dependency name alone.

Preserve existing architecture, package names, build tool, Lombok policy, API/error formats and supported runtime. Do not upgrade dependencies, replace libraries or add deployment infrastructure merely to match this guide. For new projects, use explicit choices first; establish missing consequential choices and verify compatible stable versions before scaffolding.

Prefer constructor injection for new collaborators. Use records for new Java DTOs only when the language baseline and serialization contract support them; do not convert entities or existing DTOs automatically. With Lombok entities, inspect generated equality, setters and string output rather than imposing a blanket ban.

## Load only affected topics

| Task touches | Reference |
| --- | --- |
| HTTP contracts, validation, error handling, outbound clients | [Web](references/web.md) |
| JPA queries, transactions, schema changes, concurrent writes | [Data](references/data.md) |
| Authentication, authorization, CSRF, security regressions | [Security](references/security.md) |
| Test selection, fixtures, Spring context or integration failures | [Testing](references/testing.md) |
| Properties, profiles, startup, Actuator or operational behavior | [Configuration](references/configuration.md) |

References contain decision checks, not mandatory features. Their official links may default to newer releases: select documentation matching the target's resolved versions before choosing APIs or imports. Report unavailable version evidence instead of silently changing the baseline.

## Learn from the project

Use the project's existing decisions and reuse applicable guidance already in context. When
user/project guidance supplies saved lessons, use [retrieval](../task-orchestrator/references/learning.md)
only for missing relevant guidance. Consider [lesson proposals and storage](../task-orchestrator/references/learning.md#capture-only-evidence-backed-candidates)
only after explicit final acceptance; saving still requires separate approval. Do not impose a
fixed convention set or silently edit this shared skill.

## Verify the changed behavior

Choose checks that expose the actual failure or acceptance condition using the project's configured tasks. A mocked collaborator cannot prove database, proxy or token-validation behavior. Report actual checks, skipped checks and remaining gaps; for reviews, return concrete findings and file/line evidence without fixing them. Loading this skill does not authorize test execution outside the assignment's limits.
