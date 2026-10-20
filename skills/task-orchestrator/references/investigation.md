# Investigation

Start from the requested behavior, triggering input, error or affected interface. Read applicable repository instructions, the relevant build/test commands and nearby examples of the same behavior. Search paths and symbols before reading whole modules; use existing search and navigation tools rather than building an index.

Trace the execution path from its entry point through the affected logic to important outputs or side effects. Inspect important callers, dependencies and interfaces to establish who supplies inputs, owns state and consumes results. Include configuration, generated sources or external boundaries only when they can change this path. Read enough existing tests to understand conventions and what they actually prove. Expand context to answer a specific unresolved question; do not map the entire repository by default.

For bugs, identify expected versus observed behavior and reproduce with an allowed focused check where practical. Distinguish runtime reproduction from source inspection. Form a root-cause hypothesis and choose a check that distinguishes plausible causes before patching symptoms. When a regression test adds value, confirm that it fails for the intended reason before the correction and passes afterward; a setup failure is not a reproduction.

Before changing a shared symbol or contract, inspect affected callers and consumers, compatibility expectations and relevant failure paths. Separate verified findings (with file/symbol or check evidence) from assumptions and unresolved questions. If evidence is inaccessible, state the limit and choose a safe scoped next step; ask for missing product decisions rather than inventing them.

Return or retain a concise account of the affected path, supported cause for a bug, likely impact, smallest correction and useful verification. No separate investigation document is required. An authorized fix may proceed; investigation-only stops at findings. If attempts yield no new evidence, use [recovery](recovery.md).
