# Persistence and transactions

Apply JPA guidance only to JPA code; JDBC and R2DBC have different lifecycle and transaction behavior.

- Locate the transaction boundary around the business operation. With proxy-based transactions, self-invocation does not apply the called method's transactional advice. Check the actual caller, transaction manager, propagation and rollback rules, including caught or checked exceptions. An existing outer transaction can still be active.
- Treat readOnly as a transaction hint, not a write prohibition. Verify writes through production-like boundaries; a transaction on the test itself can hide a missing application boundary.
- Inspect SQL and fetch behavior for the affected query. Bound collection results. Choose projections, fetch joins or entity graphs based on required data; do not switch everything to EAGER. Collection fetch joins with pagination need particular care. Inspect equality/hashCode and toString for mutable identifiers and relationship traversal.
- For duplicate requests or lost updates, establish the invariant and enforce it at the database boundary where needed. An exists-then-insert check is not concurrency protection. Decide uniqueness, locking/versioning and retry behavior from the required semantics. Verify overlapping transactions and persisted results, not just mock calls.
- Follow the existing migration tool. Preserve applied migrations; add compatible changes and consider existing data and deployment order. Do not replace migrations with automatic schema updates.

Official references: [transaction proxies and settings](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html), [JPA queries and fetch graphs](https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html), [Hibernate query language](https://docs.hibernate.org/orm/6.6/querylanguage/html_single/). Match the target provider/version before applying examples.
