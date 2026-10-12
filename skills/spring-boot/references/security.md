# Security boundaries

- Identify the actual mechanism: browser session/cookie, bearer token, OAuth2 client or resource server. Preserve the established issuer, authorities and ownership rules. Do not add authentication just because a service uses Spring Boot.
- Inspect filter-chain ordering, matchers and fallback behavior. For protected object access, enforce the caller's tenant/ownership boundary as well as route-level roles. An authenticated user must not gain access merely by changing an ID.
- Do not disable CSRF based only on the words REST, JWT or stateless. Establish whether browsers automatically attach credentials, including cookies or HTTP Basic. CORS is not authorization or a substitute for CSRF protection.
- Use the configured token verifier; decoding claims alone does not authenticate a JWT. Check signature, issuer, expiry and required audience validation against the application's contract. Do not introduce a custom token parser for routine resource-server work.
- Test allowed access, absent/invalid credentials and insufficient permissions for the affected route. Include cross-owner access when relevant. Keep security filters enabled in tests meant to prove security. A mock user/JWT can test authorization mapping but does not prove signature or issuer validation.

Official references: [authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html), [CSRF and browser credentials](https://docs.spring.io/spring-security/reference/features/exploits/csrf.html), [JWT resource servers](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html). These servlet examples require the corresponding reactive APIs in WebFlux applications.
