# Configuration and operational behavior

- Trace effective values through profiles, environment variables, imports and command-line overrides. Avoid fixing the wrong property source. Prefer validated ConfigurationProperties for a related group of new settings; preserve compatible names and defaults.
- Keep secrets out of committed configuration, URLs, logs and exception responses. Inspect what logging actually emits, including request bodies and entity string output. Preserve the project's secret provider rather than introducing a new one.
- For startup failures, inspect the earliest relevant cause, bean conditions and dependency/configuration changes. Do not hide missing beans with broad scanning, overriding or exclusions without explaining the resulting behavior.
- Review Actuator exposure separately from endpoint availability and authorization. Do not expose all endpoints for debugging. Keep liveness independent of shared external systems; evaluate readiness dependencies according to whether this instance can serve traffic.
- Change virtual threads, connection pools, timeouts or graceful shutdown only for an observed requirement. Virtual threads do not increase database capacity or fix blocking reactive code. Check runtime compatibility and operational evidence before tuning.
- Extend existing packaging, Compose and CI only when the task needs it. Verify affected startup/probe behavior using allowed local fixtures; do not deploy or contact production to validate a documentation recommendation.

Official references: [property precedence and binding](https://docs.spring.io/spring-boot/reference/features/external-config.html), [Actuator exposure and probes](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html), [graceful shutdown](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html). Use documentation for the target release.
