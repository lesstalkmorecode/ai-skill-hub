# HTTP contracts and clients

- Inspect routes, DTOs, serialization settings and consumers before changing status codes, nullability, pagination or error bodies. Preserve existing contracts; avoid exposing entity graphs through new endpoints.
- Match MVC or WebFlux. Do not block a reactive event loop with JPA or synchronous HTTP; inspect an existing blocking boundary before proposing a change. Do not migrate an application to reactive execution for one endpoint.
- Validate at the relevant boundary. Verify nested validation, missing fields and null handling; a numeric constraint alone may allow null. Test malformed input separately from business-rule rejection. Keep authorization separate from input validation.
- Extend the established exception mapping. Preserve multiple errors for one field without duplicate-key failures. Use ProblemDetail where supported and compatible with the API; enabling it globally can change unrelated responses. Do not expose internal exception messages to clients.
- Choose an outbound client supported by the target version and execution model. Preserve configured builders, authentication, observability and timeouts. Retry only with understood idempotency and bounded attempts; a timed-out write may have succeeded remotely.

For an endpoint change, verify successful output and the relevant rejection path, including headers/body and persistence effects. A controller unit test alone does not verify serialization or filters.

Official references: [MVC validation](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-validation.html), [error responses](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html), [REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html). Use the target release's documentation.
