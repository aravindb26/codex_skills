# Circom Auditor

A runtime-neutral skill for security review of Circom circuits. It audits for
soundness, completeness, privacy, and constraint bugs while keeping an efficient
path for both Codex and Claude-style agent runtimes.

Built for:

- Circom developers who want a soundness check before a commit.
- ZK security researchers looking for fast witness-manipulation leads.
- Protocol teams that want repeatable local or delegated circuit review.

This is not a replacement for a formal audit. Treat it as a high-signal review
assistant that still needs human validation.

For deep AI scans focused on vulnerability discovery in any cryptography code,
visit [zkao.io](https://zkao.io).

## Runtime Behavior

- **Codex:** defaults to delegated mode when `spawn_agent`-style subagents are
  available. Codex delegated mode uses the same 17 generated audit bundles as
  the Claude workflow, with at most 6 agents running at once. If subagents are
  unavailable, or if you ask for "local mode", "no subagents", or
  "single-agent pass", Codex uses the deterministic local workflow.
- **Claude-style runtimes:** default to the high-throughput 17-agent workflow
  when `Agent`, `Read`, `Glob`, and `Grep` are available. Ask for "local mode",
  "no subagents", or "single-agent pass" to avoid spawning agents.
- **Unknown runtimes:** use the local Codex fallback workflow.

Parallel/subagent review is the default in Codex and Claude-style runtimes when
subagent tooling is available.

Every audit starts with the circom-auditor banner and a visible markdown
progress console. Local audits show phase-level progress. Delegated audits show
one row per selected agent, including the agent lens, current status, and final
result. Delegated audits run at most 6 agents in parallel; remaining selected
agents stay queued until a worker slot opens. Native subagent UI is
runtime-dependent, so the markdown console is the portable fallback.

## Usage

Audit every in-scope `.circom` file in a repo:

```text
Use $circom-auditor to audit the Circom circuits in this repo.
```

Audit specific files:

```text
Use $circom-auditor to audit circuits/Spend.circom circuits/MerkleRoot.circom.
```

Run a delegated audit when the runtime supports subagents:

```text
Use $circom-auditor to run a delegated parallel audit of this repo.
```

Run a local-only audit in Codex or Claude:

```text
Use $circom-auditor to audit this repo in local mode with no subagents.
```

Also write the final report to `assets/findings/`:

```text
Use $circom-auditor --file-output to audit this repo.
```

## What Gets Scanned

Default scope is all in-scope `.circom` files under the current repo. If files
are named explicitly, only those files and their in-scope local includes are
audited.

Excluded by default:

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

Vendored and external circomlib files are treated as peripheral context. The
auditor focuses on your in-scope code and flags caller-side misuse of library
preconditions.

## Context Builder

The shared helper script discovers scope, resolves includes, collects local
docs and prior findings, and creates audit bundles:

```bash
python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD"
```

For specific files:

```bash
python3 skills/circom-auditor/scripts/build_audit_context.py --repo "$PWD" --files path/to/A.circom path/to/B.circom
```

If the script is run from outside the skill directory layout, pass
`--skill-dir /path/to/skills/circom-auditor` so bundled references resolve
correctly.

Generated files include:

- `source.md`: source bundle plus include graph and peripheral manifest.
- `docs-context.md`: local `assets/docs/` markdown/text files, if present.
- `prior-findings.md`: local `assets/findings/*.md`, if present.
- `agent-1-bundle.md` through `agent-17-bundle.md`: delegated audit bundles.

URL lists in `assets/docs/` are not fetched automatically. Fetch external docs
only when the user explicitly authorizes network access.

## Version Checks

Normal audits do not perform remote version checks. This keeps Codex runs
deterministic and avoids network failures in restricted environments.

When you want to check for updates, ask explicitly, for example:

```text
Check whether $circom-auditor is up to date.
```

## References

The main skill keeps runtime selection and core workflow in `SKILL.md`.
Detailed runtime-specific instructions live in:

- `references/orchestration/codex.md`
- `references/orchestration/claude.md`

Audit judgment and output format live in:

- `references/judging.md`
- `references/report-formatting.md`

Specialized audit lenses live in `references/hacking-agents/`, and broad attack
catalogs live in `references/attack-vectors/`.

## Tips

- Target hot circuits when possible. Smaller scopes leave more context for
  concrete witness paths.
- Put protocol notes and threat models in `assets/docs/`; the auditor uses them
  to understand intended semantics.
- Keep previous reports in `assets/findings/`; the auditor revalidates still
  relevant issues.
- Prefer strict primitives such as `Num2Bits_strict` and `Bits2Num_strict`.
- Run more than once for high-risk code. LLM review is non-deterministic and
  different passes may surface different witness paths.
