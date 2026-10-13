# Shared Scan Rules

## Reading

Your bundle is concatenated files: all in-scope source, the senior-auditor SOP (`senior-auditor-sop.md` — HOW to think), your specialty agent (WHAT to look for), and these shared rules (output format, dedup tags, AND the mandatory mental tool protocol). It has two source sections:

1. **Core source** (inline in `source.md`) — every in-scope `.circom` file with a `### path` header and a fenced code block. Read in parallel chunks (offset + limit), compute offsets from the line count in your prompt.
2. **Peripheral file manifest** — file paths under `# Peripheral Files (read on demand)` in the bundle. These are libraries (`circomlib`, project-vendored helpers, `node_modules/`-resolved includes) that the in-scope code calls into. Read only those relevant to your specialty.

Read the whole bundle once at the start before producing findings. When matching template names, check both `TemplateName` and `_TemplateName` (Circom convention for internal helpers). When matching signal names, check both `out` and `out[i]` array forms.

## Mental tool protocol — MANDATORY

The three tools in `senior-auditor-sop.md` are NOT optional. Each has a specific trigger. **When the trigger fires, you MUST emit the corresponding marker in your working text BEFORE continuing.** No skipping. The markers live in your reasoning stream — they do NOT go into the FINDING/LEAD output blocks. **The protocol applies continuously while you read source, not just before it** — every trigger fires the moment its condition occurs, throughout the entire review.

### Triggers → required markers

| Trigger (the condition) | Marker (required immediately, literal `[Tool: ...]` syntax) | Content |
|---|---|---|
| You open a new `template` or `component main` to read | `[Feynman: <TemplateName>]` | Explain what it *proves* in plain English — no `<--`/`<==`/`===`/`Num2Bits`/signal-vs-constraint jargon. Say what the verifier learns and what the prover had to know. Wherever your plain-English explanation gets fuzzy or you reach for Circom syntax to stay accurate, mark that spot — that is an unconstrained signal, and that is where bugs hide. |
| You stop on a constraint whose purpose isn't immediately clear | `[Socratic: <file:line> — what does this pin? what stays free?]` | A one-line question that drills past "because that's how it's written." If your first answer restates the constraint, ask again. Stop when the answer exposes the implicit belief the constraint rests on — typically the signal it assumes is bounded but never pins. |
| A constraint looks like it pins a signal / a check looks sufficient / a gate looks correct | `[Inversion: <TemplateName>]` | A concrete malicious-prover attempt: the field value (or gate/divisor set to zero, or aliased preimage) that satisfies every constraint yet breaks intent. Specific values like `in = p - 1`, not abstractions. |

### Rules

1. **Triggers are not optional.** If the condition fires, the marker follows. Always.
2. **Use the literal `[Tool: ...]` syntax.** The orchestrator greps your output for these tags after the run.
3. **You may emit a marker without a trigger.** Extra Feynman / Inversion markers are fine. You may NOT skip a marker after its trigger fired.
4. **The protocol applies to reasoning depth, not output volume.** Heavy use of these tools is what produces the audit work. Skipping them = surface-level scanning, the failure mode of every junior auditor.

The orchestrator verifies marker counts after every run. Skipped markers downgrade the value of your findings and are recorded as workflow violations.

## Scope discipline

There are three agent groups. **Vector-scan shards** (signal-field, range, selector-accumulator, binding-1, binding-2, regex-language) each grind one slice of the attack-vector catalog. **Single-lens agents** (signal-flow, range-check, arithmetic-field, selector-mux, invariant, intent-binding, first-principles, free-flow) own one reasoning lens. Both groups SHOULD cross-flag and weaponize aggressively — the dedup pass merges overlaps, so a redundant flag is cheaper than a missed bug. **Gap-hunter agents** (numerical-gap, binding-gap, composition-gap) own the seams BETWEEN lenses and MUST drop any finding expressible with a single lens alone — their value is exactly the bugs no single-lens scan can articulate.

## Cross-template propagation (the "weaponization" rule)

When you find a bug in one template, **weaponize that pattern across every other template in the bundle.** Search by template name AND by code pattern. Three concrete propagation rules:

1. **Same primitive, multiple consumers.** If you find that `circomlib.MontgomeryAdd` is unsound when `in[0] == in[1]`, then *every* template that calls `MontgomeryAdd` (directly or transitively through `EscalarMulFix`, `Pedersen`, `EdDSAVerifier`, etc.) inherits the bug. Trace the include graph and report every consumer.
2. **Same idiom, different file.** A `<--` without a paired `===` in `chacha.circom` means you check every `<--` in every other `.circom` file in scope. Missing a repeat instance is an audit failure.
3. **Same shape, different context.** A `LessThan(N)` whose operands are not `Num2Bits(N-1)`-bounded in one template is a recurring shape — search every `LessThan` / `LessEqThan` / `GreaterThan` / `GreaterEqThan` callsite in scope and verify operands.

After scanning: escalate every finding to its worst exploitable variant (a completeness break may hide a soundness break that lets the prover choose a bad witness). Then revisit every template where you found something and attack the other branches and signal flows.

## Do not report

- Style: snake_case vs camelCase, file layout, missing comments.
- Compile-time `assert(...)` used in its legitimate role (parameter sanity checks the user understands won't survive into R1CS).
- Self-harm-only bugs (the prover can only break their own proof; no third-party victim).
- Pure prover-side performance issues (large constraint count, slow witness gen) that don't change verification semantics.

## Output

Return structured blocks, no preamble. The only non-block text allowed is the mental-tool markers (`[Feynman: ...]` / `[Socratic: ...]` / `[Inversion: ...]`) in your working reasoning — they precede the blocks and never appear inside a FINDING/LEAD. Exception: vector-scan-agent outputs its classification block first.

- `FINDING` blocks have concrete, unguarded, exploitable witness paths. **Every FINDING must have a `proof:` field** — concrete field values, witness arrays, or call sequences from the actual code. No proof = LEAD, no exceptions.
- `LEAD` blocks have real code smells with partial witness paths — default to LEAD over dropping.
- **One vulnerability per item.** Same root cause = one item. Different fixes needed = separate items.
- Every `FINDING` and `LEAD` block must include `detected_by: agent-N`, where
  `agent-N` is the agent id supplied by the orchestrator prompt. If no id was
  supplied, use the bundle filename stem, such as `agent-8`.

```
FINDING | template: Name | local: signal_or_helper | bug_class: tag | group_key: TemplateName | signal_or_local | bug-class
detected_by: agent-N
path: caller-template → callee-template → constraint missing → impact
proof: concrete witness values demonstrating the bug (e.g., in = p - 1, out = whatever)
description: one sentence
fix: one-sentence suggestion (actual Circom snippet preferred)

LEAD | template: Name | local: signal_or_helper | bug_class: tag | group_key: TemplateName | signal_or_local | bug-class
detected_by: agent-N
code_smells: what you found
description: one sentence explaining the trail and what remains unverified
```

The `group_key` enables deduplication: `TemplateName | signal_or_local | bug-class`. Examples:

- `MontgomeryAdd | lambda | div-by-zero`
- `RangeProof | in[0] | comparator-input-not-range-checked`
- `BigMod | mod[i] | bigint-limb-out-of-range`
- `Decoder | success | one-sided-constraint`

Agents may add custom fields beyond the standard schema (see each agent's prompt for the additions specific to their specialty).
