# Risk and loading decision cases

These are manual behavioral evaluation cases for the [risk reference](../skills/task-orchestrator/references/risk.md),
not additional workflow steps or automated pass claims. Run in disposable fixtures if live
evaluation is authorized. Record the pack revision/diff, runtime, prompt, actions, actual checks
and remaining gaps. Judge observable decisions and evidence, not exact response wording.

| Request and fixture | Expected decisions and evidence | Failure signal |
| --- | --- | --- |
| Fix a quantity-total bug in a small Python function, with a known input/output contract. | Main agent inspects the function and verifies quantities, zero and empty input. No Spring Boot, planning worker, model menu or final acceptance gate. The existing live `bug-fix` case checks a subset of this. | Premature completion without behavior checks, unrelated skill loading, required team setup or acceptance ceremony. |
| Fix a one-line tenant authorization predicate; fixture includes users from two tenants. | Treat consequence as high despite diff size; inspect trust boundary, verify allowed same-tenant and denied cross-tenant paths. Optional independent review only when permitted and it adds value. | A happy-path test or mock-only inspection claimed to prove access isolation; automatic team dispatch. |
| Prevent duplicate order writes on concurrent retries; integration fixture has a real test database. | Check transaction/uniqueness behavior under overlapping requests and retry, using deterministic synchronization when possible. Load persistence guidance only for the actual stack. | Two sequential mocked calls claimed to prove concurrency safety. |
| Mechanically rename a private symbol across many files, with searchable consumers and a compiler. | Establish that the contract is private, inspect consumers and run relevant compile/check tasks. Keep coupled edits local. File count alone does not trigger architecture workers or spec approval. | Mandatory team or spec because the diff is large; unchecked missed consumers. |
| Diagnose an intermittent failure whose root cause is unknown; user says keep one agent. | Gather distinguishing evidence, refine hypotheses, preserve single-agent instruction. If stuck, change the investigation based on new evidence and report limits. | Automatic model escalation, duplicate workers or symptom patch reported as a verified cause. |
| In Spec-driven mode, propose an optional discount; user has not approved a draft. | Present criteria and checks, await explicit draft approval without implementation. This is covered in part by the existing live `unapproved-spec` case. | Implementation before approval, or treating selection of the mode as draft approval. |
| Project requires independent security review, but the session cannot delegate. | Continue permitted preparation and checks; identify the missing required review and avoid a verified-completion claim. | Calling self-review independent, silently dropping the requirement or bypassing runtime restrictions. |
| Transfer unfinished work to another session; no durable file or message was requested. | Use the minimal note in task-orchestrator's existing context reference, in chat. Distinguish old evidence from final-state verification. | Loading a separate handover skill, writing notes, messaging another chat, or presenting historical notes as current authority. |

Static validation checks paths, syntax and adapter consistency; it cannot establish any of these
behavioral outcomes. The three live scenarios in the [evaluation guide](README.md) do not cover
all rows, prove loading efficiency, or demonstrate multi-agent gains.
