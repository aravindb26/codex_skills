# Claude Orchestration

Use this workflow by default in Claude-like runtimes where foreground `Agent`,
`Read`, `Glob`, and `Grep` tools are available. Do not use it only when the
user explicitly asks for local mode, no subagents, or a single-agent pass.

## Turn 1 - Discover

Print the banner from `SKILL.md` exactly, then make these parallel tool calls:

1. Bash `find` for in-scope `.circom` files using the exclude pattern in
   `SKILL.md`.
2. Locate `references/attack-vectors/attack-vectors.md` and resolve the
   `references/` directory.
3. Confirm `Agent` is available.
4. Read local `VERSION`.
5. Create a scratch directory under `/tmp`.

Do not perform a remote version check unless the user explicitly asked to check
or update the skill.

## Turn 2 - Prepare

Prefer the shared helper script:

```bash
python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD"
```

For specific files, add `--files path/to/A.circom path/to/B.circom`.

The script emits `source.md`, optional docs and prior-findings files, and all
17 agent bundles. Print line counts for every generated bundle and for
`source.md`; also print line counts for `docs-context.md` and
`prior-findings.md` when present. Do not inline bundle contents into agent
prompts.

Bundle layout:

| Bundle | Appended files after `source.md` |
|---|---|
| `agent-1-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/signal-field.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-2-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/range.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-3-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/selector-accumulator.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-4-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/binding-1.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` + docs if present |
| `agent-5-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/binding-2.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` + docs if present |
| `agent-6-bundle.md` | `senior-auditor-sop.md` + `attack-vectors/regex-language.md` + `hacking-agents/vector-scan-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-7-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/signal-flow-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-8-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/range-check-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-9-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/arithmetic-field-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-10-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/selector-mux-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-11-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/invariant-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-12-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/intent-binding-agent.md` + `hacking-agents/shared-rules.md` + docs if present |
| `agent-13-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/first-principles-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-14-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/free-flow-agent.md` + `hacking-agents/shared-rules.md` + docs if present |
| `agent-15-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/numerical-gap-agent.md` + `hacking-agents/shared-rules.md` |
| `agent-16-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/binding-gap-agent.md` + `hacking-agents/shared-rules.md` + docs if present |
| `agent-17-bundle.md` | `senior-auditor-sop.md` + `hacking-agents/composition-gap-agent.md` + `hacking-agents/shared-rules.md` |

Agents 1-6 are vector-scan shards. Agents 7-14 are single-lens specialists.
Agents 15-17 are gap hunters that hunt bugs across lens boundaries.

## Turn 3 - Spawn

Run the selected agents through a bounded foreground-agent queue with maximum
concurrency 6. For a full delegated audit, select all 17 agents. For smaller
scopes, use the smallest set of bundles that covers the risk, but keep at least
one first-principles or free-flow pass.

Before spawning, print this agent progress console. Mark the first up to 6
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

Spawn no more than 6 foreground `Agent` calls in one batch. As each batch
returns, update the table: completed agents become `Done` with a short result
count such as `2 findings, 1 lead` or `no findings`; failed agents become
`Blocked` with the failure reason. Then start the next queued agents, again with
no more than 6 running at once. Repeat until every selected agent is `Done` or
`Blocked`.

Single-lens prompt for agents 1-14:

Replace `agent-N` with the actual agent id (`agent-1`, `agent-2`, ...).

```text
You are a malicious prover. Your specialty, mindset, source, and output rules
are in your bundle. Read it fully before producing findings.

Read first:
- <bundle-path> (<line-count> lines) - source + SOP + specialty + shared rules.

Your agent id is agent-N. Every FINDING and LEAD block must include
`detected_by: agent-N`.

The bundle contains all in-scope source. Do not re-read in-scope files for the
initial scan. Use Read/Grep only for cross-file searches or out-of-scope context
such as circomlib, vendored includes, and peripheral files.

Every FINDING needs file, template, signal, root cause, minimal fix, and a
concrete proof. Without proof, emit a LEAD.

Output format and the mandatory mental-tool protocol are in shared-rules.md
inside your bundle.
```

Gap-hunter prompt for agents 15-17:

Replace `agent-N` with the actual agent id (`agent-15`, `agent-16`, or
`agent-17`).

```text
You are a malicious prover hunting the seams between lenses. Your gap-hunter
specialty, mindset, source, and output rules are in your bundle. Read it fully
before producing findings.

Read first:
- <bundle-path> (<line-count> lines) - source + SOP + gap-hunter specialty +
  shared rules.

Your agent id is agent-N. Every FINDING and LEAD block must include
`detected_by: agent-N`.

If a finding can be expressed with a single lens alone, drop it. Without
concrete proof of the seam, emit a LEAD.

Output format and gap-hunter-specific fields are in your bundle.
```

## Turn 4 - Deduplicate And Validate

Deduplicate every FINDING and LEAD from all workers, plus any still-valid prior
finding from `prior-findings.md`.

Rules:

- Tag every raw item with its source agent id if the worker did not include
  `detected_by`.
- Group by `group_key` (`Template | signal_or_local | bug-class`).
- Never merge across different `template:` fields.
- Never merge across different `local:` or signal fields within a template.
- Preserve every distinct mechanism, witness path, and fix strategy.
- Preserve and union detector sets. If `agent-2`, `agent-8`, and `agent-14`
  report the same deduplicated item, the final report item must say
  `Detected by: agent-2, agent-8, agent-14`.
- If two fixes add different constraints, check directions, strict conversions,
  or target signals, render them as separate fix options.
- Run a second pass at `(Template, signal)` ignoring `bug_class` to make sure no
  mechanism was silently dropped.
- Print `Completeness: N unique (Template, signal) in raw, N covered in final.`
  before triage.

Gate each deduplicated item exactly once using `judging.md`: refutation,
reachability, trigger, impact. `UNCERTAIN` means the item remains allowed for
reporting as a finding or lead rather than being silently rejected.

## Turn 5 - Triage

For every finding, spawn a fresh foreground `Agent` to validate whether the bug
is real and exploitable. Leads are not triaged. If there are zero findings,
skip this turn.

Use this prompt shape:

```text
Is the following a real bug that we can exploit?

---
<finding title, exactly as drafted for the report>

`<header line: TemplateName (file.circom:LL-LL) · signal: <signalName>` · Confidence: N>

**Description**
<finding description verbatim>

**Circuit / Constraint**
<the offending code block verbatim>

**Fix** (omit this section if the finding is below threshold and has no fix block)
<the diff verbatim>
---
```

Read every response in full. Attach:

- `triager_verdict`: `Exploitable` or `Not Exploitable`, decided from the
  substance of the response.
- `triager_reasoning`: one concise paragraph preserving concrete constraints,
  witness steps, and file:line references.

If the triage response is genuinely ambiguous, default to `Exploitable` and
note the uncertainty.

## Turn 6 - Output

Format the final report with `references/report-formatting.md`.

- Exclude rejected items.
- Keep findings the triager marks `Not Exploitable`; the disagreement is useful
  to the user.
- Include triager verdicts and a `## Triager Reasoning` section because this
  delegated Claude workflow ran triage.
- If `--file-output` was requested, write the report to the configured findings
  path.
