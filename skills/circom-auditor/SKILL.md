---
name: circom-auditor
description: "Audit Circom circuits for soundness, completeness, privacy, and constraint bugs. Use when the user asks to audit, review, check, or find vulnerabilities in Circom code, or when they ask to run circom-auditor on a repo or specific .circom files."
---

# Circom Auditor

Use this skill to review Circom circuits for exploitable constraint bugs. The
skill directory is the directory containing this `SKILL.md`; bundled references
live under `references/`, and deterministic helper scripts live under
`scripts/`.

## Runtime Selection

- In Codex with `spawn_agent`-style subagents available, default to delegated
  mode in `references/orchestration/codex.md`. Delegated Codex runs use the
  same generated agent bundles as the Claude workflow, adapted to Codex
  subagent tooling. Use local Codex mode only when subagents are unavailable or
  when the user explicitly asks for local mode, no subagents, or a single-agent
  pass.
- In Claude with `Agent`/`Read`/`Glob`/`Grep` tools available, default to the
  17-agent workflow in `references/orchestration/claude.md`. Use a local
  single-agent Claude audit only when the user explicitly asks for local mode,
  no subagents, or a single-agent pass.
- If the runtime is unclear, follow the Codex local fallback workflow.

Do not run a remote version check during ordinary audits. Network may be
restricted; keep the audit deterministic from local files unless the user
explicitly asks to check for updates.

## Audit Console

Start every audit by printing this banner exactly, unless the user explicitly
asks for no banner:

```text

███████╗██╗  ██╗███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
╚══███╔╝██║ ██╔╝██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
  ███╔╝ █████╔╝ ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝
 ███╔╝  ██╔═██╗ ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝
███████╗██║  ██╗███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝
                       c i r c o m  ·  a u d i t o r
```

Then show a visible markdown progress console. In local mode, show audit
phases. In delegated mode, show one row per agent with its lens, status, and
result. Delegated mode uses a bounded worker pool: at most 6 agents may be
`Running` at once, and the remaining selected agents must stay `Queued` until a
slot opens. Update the console as phases or agents move from `Pending` to
`Queued`, `Running`, `Done`, `Skipped`, or `Blocked`.

If the runtime has a native subagent UI, use it, but still print a compact
markdown summary so transcripts record which agents ran and when they finished.
If the runtime only returns parallel agent results after the whole batch
finishes, spawn at most 6 agents in that batch, print the table before
spawning, then print an updated table before starting the next queued batch.

## Inputs

- Default scope: all in-scope `.circom` files under the current repo.
- Specific scope: if the user names one or more files, audit only those files
  plus local includes that are in scope.
- `--file-output`: also write the final report to
  `assets/findings/{project-name}-zksec-circom-audit-report-{timestamp}.md`.
- Delegated mode: default in Codex and Claude when subagent tooling is
  available; local mode is an explicit opt-out or fallback.

Exclude directories and artifacts matching:

```text
node_modules/
circuits/test/
tests/
__tests__/
dependencies/circomlib/
lib/circomlib/
build/
dist/
artifacts/
out/
*.test.circom
*_test.circom
*-test.circom
*.witness.json
*.r1cs
*.zkey
```

## Build Audit Context

Prefer the bundled helper script to ad hoc shell pipelines:

```bash
python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD"
```

For specific files:

```bash
python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD" --files path/to/A.circom path/to/B.circom
```

When the skill is installed somewhere else, resolve the script relative to the
directory containing this `SKILL.md`.

The script writes a scratch directory under `/tmp` unless `--out` is supplied.
It creates:

- `source.md`: in-scope Circom files plus an include graph and peripheral
  manifest.
- `docs-context.md`: local `assets/docs/` markdown/text context, if present.
- `prior-findings.md`: local `assets/findings/*.md`, if present.
- `agent-1-bundle.md` through `agent-17-bundle.md`: source plus specialized
  reference instructions for delegated mode.

If Python is unavailable, fall back to `rg --files -g '*.circom'` or `find`
with the exclude list above, then read includes manually with:

```bash
rg -n '^\s*include\s+"[^"]+"' <files>
```

## Required References

Always read:

- `references/judging.md` before validating candidates.
- `references/report-formatting.md` before producing a report.

For broad audits, also read:

- `references/attack-vectors/attack-vectors.md`

For targeted passes, load only the relevant file from
`references/hacking-agents/`:

- `vector-scan-agent.md`: classify templates and risky dependencies.
- `signal-flow-agent.md`: unconstrained witness flow and public/private
  binding.
- `range-check-agent.md`: aliasing, comparator inputs, limb bounds.
- `arithmetic-field-agent.md`: field wraparound, inverse/division patterns.
- `selector-mux-agent.md`: boolean selectors, disabled constraints, muxes.
- `invariant-agent.md`: cross-template invariants.
- `intent-binding-agent.md`: nullifier, replay, domain separation, docs.
- `first-principles-agent.md`: end-to-end semantic attacks.
- `free-flow-agent.md`: independent adversarial pass.

## Local Audit Workflow

1. Resolve scope with `scripts/build_audit_context.py`.
2. Read `source.md`, `references/judging.md`, and
   `references/report-formatting.md`.
3. For broad audits, read `references/attack-vectors/attack-vectors.md`.
4. Read project docs from `docs-context.md` if present; use them only to
   understand intended semantics, never to excuse missing constraints.
5. Revalidate any still-relevant issues from `prior-findings.md`.
6. Inspect the in-scope files for concrete witness manipulation paths:
   - `<--` assignments without paired constraints.
   - `assert(...)` used where a runtime constraint was intended.
   - missing `Num2Bits_strict`, `Bits2Num_strict`, comparator input bounds, or
     limb bounds.
   - division/inverse constraints without nonzero checks and multiplication
     pins.
   - selector, mux, and enable signals missing booleanity constraints.
   - public inputs, nullifiers, commitments, or signatures not bound to the
     intended domain/action.
   - field wraparound or aliasing near `p`, especially when values are later
     interpreted as integers.
   - peripheral library preconditions that callers fail to enforce.
7. For every candidate, apply the four gates in `judging.md` exactly once:
   refutation, reachability, trigger, impact.
8. Report confirmed findings and high-signal leads. Do not report style,
   optimization, deployer-intent assumptions, or self-harm-only issues.

## Delegated Audit Workflow

Build context with `scripts/build_audit_context.py`, then follow the
runtime-specific orchestration:

- Codex delegated mode: default when `spawn_agent`-style subagents are
  available; see `references/orchestration/codex.md`.
- Claude delegated mode: the default Claude workflow when `Agent`/`Read`/`Glob`
  /`Grep` are available; see `references/orchestration/claude.md`.

Worker outputs must be deduplicated by `group_key`, validated with
`references/judging.md`, and formatted with `references/report-formatting.md`.
Every confirmed finding needs a concrete proof or witness path. No proof means
the item remains a lead. Preserve detector provenance: tag every raw worker
`FINDING` and `LEAD` with the source agent id, union those ids during
deduplication, and include the final detector set in every reported finding and
lead.

## Output

Use `references/report-formatting.md`.

- In local mode, omit delegated-triage fields and sections.
- In delegated mode, include triage verdicts and reasoning only when triage
  workers were actually run.
- If there are no confirmed findings, say so plainly and include any leads or
  residual test gaps.
- If `--file-output` was requested, write the same report to the report path
  specified in `references/report-formatting.md` and mention the path in the
  final answer.
