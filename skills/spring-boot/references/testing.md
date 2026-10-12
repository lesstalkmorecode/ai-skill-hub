# Tests that exercise the relevant boundary

Inspect wrapper commands, CI, profiles and test plugins/source sets before selecting checks. Maven test may omit Failsafe integration tests; Gradle check covers only tasks actually wired into it. Do not report unexecuted suites as passing.

| Evidence needed | Suitable starting point |
| --- | --- |
| Pure business decisions | Unit test without a Spring context |
| MVC binding, validation, serialization and filters | MVC slice using the project's supported mock setup |
| Reactive HTTP behavior | WebFlux slice and WebTestClient |
| JPA mappings, queries or database constraints | Persistence test against the relevant database engine |
| Application wiring or real HTTP boundary | SpringBootTest with the appropriate environment |

Match annotation packages, mock-bean APIs and test clients to resolved dependencies. Do not copy Boot 4 examples into Boot 3 or replace MockBean/MockitoBean without checking availability and scope.

Use Testcontainers when database-specific behavior needs it and the project supports containers. ServiceConnection requires version support and the relevant test dependency; DynamicPropertySource remains valid for custom properties or unsupported connection types. If Docker is unavailable, report the gap; an H2 substitution does not establish PostgreSQL compatibility.

Flush/clear or use separate transactions when required to observe constraints and persisted state. Server work on a random port does not share the test thread's rollback transaction. Isolate test data and clean up only owned resources. Coordinate concurrency tests with bounded synchronization rather than arbitrary sleeps.

Official references: [Boot test scopes and clients](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html), [Testcontainers integration](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html). Consult the matching release and existing CI configuration.
