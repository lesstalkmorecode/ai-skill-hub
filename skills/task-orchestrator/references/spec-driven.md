# Spec-driven workflow

Spec-driven is an optional mode; once selected, draft a spec automatically and require user approval before implementation. Missing repository spec support or an applicable task spec is a reason to draft, not to stop for a storage or mode choice.

1. **Intake:** Gather the user's task, supplied context, constraints, and validation preferences. Read relevant repository guidance and code to ground the proposed behavior.
2. **Discover:** Check repository guidance, project configuration, and existing spec locations for a configured workflow and applicable task specs. The portable pack's bundled spec skill does not configure the target repository. Reuse applicable specs as context and follow configured proposal conventions; do not overwrite approved or living specs with an unapproved draft.
3. **Draft:** Create a task-specific draft covering outcome, observable behavior, acceptance criteria, non-goals, assumptions/open questions, and a test plan with applicable checks. Use the configured repository workflow when available. Otherwise, draft in-memory in the conversation by default. Write a lightweight draft file when the user explicitly requested durable spec files or the repository has an established spec location; use that location and format, or a minimal `spec/changes/<change-name>.md` file when durable files were requested without a repository convention. Do not install a spec framework. If essential context is missing, present the draft with the unresolved questions and ask only for the information needed to revise it, rather than offering a storage/mode menu.
4. **Approval:** Present the draft itself, or a concise summary and link to the draft files, including acceptance criteria, test plan, and unresolved questions. Explicitly ask the user to review and approve it, then stop and wait. Selecting Spec-driven, asking for implementation, an existing spec, and silence do not approve the current draft. Do not edit implementation code or dispatch implementation workers before explicit approval. If the user rejects the draft or requests edits, revise it, present the revised draft, and ask for approval again; edit requests alone are not approval.
5. **Implement:** After explicit approval of the presented draft and resolution of blocking questions, implement against that approved spec. Pass the approved baseline and approval references, relevant spec sections and all assigned criteria to implementation workers; do not copy draft history or unrelated spec sections. If implementation requires a material change to the approved behavior or scope, revise the spec and obtain approval before implementing that change.
6. **Review and verify:** Review the final changes against the approved draft spec and run allowed checks. Review in the main session by default; independent reviewers are optional unless user/project rules require them. For delegated task reviews give correctness/risk reviewers the exact approved baseline and approval references, relevant spec sections, every assigned criterion and matching implementation/check evidence. For final integration review give reviewers every approved criterion and evidence against the integrated final state. Each reviewer MUST report coverage gaps, unsupported satisfaction claims, skipped checks and unresolved findings within its assigned scope. The coordinator reconciles partial reports and ensures final review and Spec Coverage cover every approved criterion; narrow task reviews do not satisfy the final gate. Reconcile their reports into the mandatory Spec Coverage section below. Update or archive spec artifacts only as required by the repository workflow and authorized task.

### Mandatory Spec Coverage and completion gate

In Spec-driven mode, every final response MUST include a section titled `Spec Coverage`. This is automatic: never ask whether the user wants coverage, and never omit it because no implementation occurred, checks were skipped, or work stopped early. This requirement applies to conversation drafts and configured repository specs alike.

Use the approved draft spec as the coverage baseline; identify its file/version or conversation draft and approval. List every acceptance criterion separately, preserving its identifier and meaning (assign stable AC identifiers when absent). The task is not considered complete until every approved criterion is classified as exactly one of: `satisfied`, `partially satisfied`, `not verified`, or `out of scope`. Do not hide missing criteria in a summary or silently remove them from the baseline.

- `satisfied`: the full criterion is implemented and supported by verification evidence against the final state.
- `partially satisfied`: an identified part is implemented and verified; state the unmet or unverified remainder and remaining work.
- `not verified`: evidence is absent, insufficient, skipped, or unavailable; state implementation status separately, including `not implemented` where appropriate.
- `out of scope`: exclusion is supported by the approved scope or an explicitly approved scope revision; cite that basis. An unfinished criterion cannot be relabeled out of scope to claim completion.

For every satisfied or partially satisfied criterion, include implementation references and concrete verification evidence: actual command/check, result, and relevant test/scenario or static inspection. Link shared evidence to each criterion it supports; a generic "tests passed" does not establish coverage. If evidence cannot support the claim, classify it as `not verified`. Respect validation limits and name skipped checks and their reasons; do not invent runs or results.

When no implementation occurred, still list all criteria, normally as `not verified`, with implementation `not implemented` and verification `not run` plus the reason. Existing behavior may be marked satisfied only when inspected and verified. Before draft approval, identify the baseline as an unapproved draft, list its criteria as not verified/not implemented, and state `awaiting approval`; if no criteria can yet be drafted, explicitly state that no approved spec or acceptance criteria exist and why. Never imply draft approval or implementation completion.

Classification alone does not establish verified completion. Partial satisfaction, unverified required criteria, missing essential evidence, and unresolved material findings leave implementation incomplete; report remaining work. Check that the row count and identifiers match every approved criterion before sending the final response.

### Spec-driven final answer template

Use this template for every Spec-driven final response; repeat the row for every criterion and replace all placeholders with actual evidence or explicit limits:

```markdown
Outcome: <complete / incomplete / blocked / awaiting approval; behavior changed or no implementation>
Changed files: <paths or none>

## Spec Coverage

Baseline: <approved spec/version and approval reference, or unapproved draft/no approved spec>

| Criterion | Status | Implementation | Verification evidence / limits | Remaining work |
| --- | --- | --- | --- | --- |
| <AC ID and criterion> | <satisfied / partially satisfied / not verified / out of scope> | <file/symbol or not implemented> | <actual check, result, scenario; or not run + reason; approved exclusion if out of scope> | <none or concrete gap> |

Review: <correctness and risk review results, coverage gaps, unresolved findings, or reviews not performed + reason>
Checks: <actual commands/results; skipped or unavailable checks + reasons>
```

For targets using the bundled `spec/project.md` and `spec/{current,changes,archive}` profile, load [spec-workflow](../../spec-workflow/SKILL.md) and use the relevant explore/propose sections to prepare the draft, then stop at the approval gate before apply. Use other target conventions when configured and preserve this approval gate. A request for one action does not authorize the others. Sync and archive require the repository workflow and task authorization.

Delegation remains subject to user/project authorization and runtime permission; Spec-driven mode does not imply a team. Do not require a team choice or a choice between in-memory and file storage before drafting.
