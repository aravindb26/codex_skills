# Codex Orchestration

Use this workflow when running in Codex. When Codex exposes subagents through a
`spawn_agent`-style API, delegated mode is the default. Use local fallback mode
only when subagents are unavailable or when the user explicitly asks for local
mode, no subagents, or a single-agent pass.

## Delegated Mode (Default)

Use this mode by default when Codex subagents are available.

Use the generated bundles:

- `agent-1-bundle.md`: signal-field vector scan
- `agent-2-bundle.md`: range vector scan
- `agent-3-bundle.md`: selector/accumulator vector scan
- `agent-4-bundle.md`: binding-1 vector scan
- `agent-5-bundle.md`: binding-2 vector scan
- `agent-6-bundle.md`: regex/language vector scan
- `agent-7-bundle.md`: signal flow
- `agent-8-bundle.md`: range checks
- `agent-9-bundle.md`: arithmetic and field behavior
- `agent-10-bundle.md`: selectors and muxes
- `agent-11-bundle.md`: invariants
- `agent-12-bundle.md`: intent and binding
- `agent-13-bundle.md`: first-principles adversarial pass
- `agent-14-bundle.md`: free-flow pass
- `agent-15-bundle.md`: numerical gap hunting
- `agent-16-bundle.md`: binding gap hunting
- `agent-17-bundle.md`: composition gap hunting

For small scopes, choose the smallest set of bundles that covers the risk. For
large delegated scopes, use all 17 bundles unless the user asked for a smaller
parallel pass.

Run selected agents through a bounded worker pool with maximum concurrency 6.
Before spawning, print an agent progress console. Mark the first up to 6
selected agents as `Running`, later selected agents as `Queued`, and omitted
agents as `Skipped`:

```markdown
## Agent Progress

| Agent | Lens | Status | Current Work | Result |
|---|---|---|---|---|
| agent-1 | signal-field vector scan | Running | Slice scan | - |
| agent-2 | range vector scan | Running | Slice scan | - |
| agent-3 | selector/accumulator vector scan | Running | Slice scan | - |
| agent-4 | binding-1 vector scan | Running | Slice scan + docs | - |
| agent-5 | binding-2 vector scan | Running | Slice scan + docs | - |
| agent-6 | regex/language vector scan | Running | Slice scan | - |
| agent-7 | signal flow | Queued | Unconstrained witness flow | - |
| agent-8 | range checks | Queued | Bounds and aliasing | - |
| agent-9 | arithmetic/field | Queued | Wraparound, inverse, division | - |
| agent-10 | selectors/muxes | Queued | Gates and booleanity | - |
| agent-11 | invariants | Queued | Cross-template invariants | - |
| agent-12 | intent/binding | Queued | Domains, public inputs, replay | - |
| agent-13 | first principles | Queued | End-to-end attack paths | - |
| agent-14 | free flow | Queued | Independent adversarial pass | - |
| agent-15 | numerical gaps | Queued | Cross-lens numerical bugs | - |
| agent-16 | binding gaps | Queued | Cross-lens binding bugs | - |
| agent-17 | composition gaps | Queued | Cross-template composition bugs | - |
```

When an agent completes, mark it `Done` with a short result such as
`2 findings, 1 lead` or `no findings`, then immediately start the next queued
agent and mark it `Running`. If an agent fails, mark it `Blocked` with the
failure reason and still free that worker slot for the next queued agent.

Spawn each selected worker with a concrete, self-contained task. In Codex, use
the available subagent API rather than Claude's foreground `Agent` tool. Prompt
each worker with:

```text
You are auditing Circom circuits. This is read-only analysis; do not edit files.
Your agent id is <agent-id>.
Read the full bundle at <bundle-path> before producing findings.
Return only FINDING and LEAD blocks using the schema in the bundle.
Every FINDING must include a concrete proof/witness path. No proof means LEAD.
Every FINDING and LEAD must include `detected_by: <agent-id>`.
```

While workers run, do local review of include graph, docs, prior findings, and
obvious high-risk call sites.

After workers return:

1. Tag every raw FINDING and LEAD with its source agent id if the worker did not
   include `detected_by`.
2. Deduplicate by `group_key`, preserving every distinct mechanism, proof path,
   fix strategy, and detector set.
3. Union detector sets when multiple agents report the same deduplicated item.
   Sort detector ids numerically (`agent-2` before `agent-10`).
4. Validate each item with `judging.md`.
5. Optionally triage confirmed findings with fresh subagents if the user asked
   for triage or if the delegated run is large enough to justify it.
6. Include each item's detector set in the final report per
   `report-formatting.md`.
7. Include triager verdicts only for findings that were actually triaged.

## Local Fallback Mode

Use this mode only when subagents are unavailable or the user explicitly opts
out of subagents.

1. Print the banner from `SKILL.md`, then initialize a local progress console:

   ```markdown
   ## Audit Progress

   | Phase | Status | Notes |
   |---|---|---|
   | Scope and context | Running | Building source bundle |
   | Reference loading | Pending | `judging.md`, `report-formatting.md` |
   | Source review | Pending | Concrete witness paths |
   | Validation | Pending | Four judging gates |
   | Report | Pending | Final markdown |
   ```

   Update the table after each phase.

2. Build context with the helper script:

   ```bash
   python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD"
   ```

   For a specific scope, pass `--files` with the requested `.circom` paths.

3. Read the generated `source.md`. If present, also read `docs-context.md` and
   `prior-findings.md`.

4. Read `references/judging.md` and `references/report-formatting.md`.

5. For broad audits, read `references/attack-vectors/attack-vectors.md`. For a
   narrow audit, load only the relevant `references/hacking-agents/*.md` files.

6. Review the source for concrete witness manipulation paths:
   - unconstrained `<--` witness assignments.
   - `assert(...)` where an R1CS constraint was intended.
   - missing strict bit conversion or limb bounds.
   - comparator inputs that are not range constrained.
   - inverse/division without nonzero and multiplication pins.
   - selector, mux, and enable signals missing booleanity constraints.
   - unbound public inputs, nullifiers, commitments, signatures, or domains.
   - field wraparound and aliasing near the BN254 scalar field modulus.
   - caller-side violations of peripheral library preconditions.

7. Revalidate every candidate with the four gates in `judging.md`:
   refutation, reachability, trigger, and impact.

8. Produce the report with `references/report-formatting.md`. In local mode,
   omit triager verdicts and the `## Triager Reasoning` section.
