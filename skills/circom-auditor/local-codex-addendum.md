# Codex Local Addendum

Use this skill only when the scoped target actually contains Circom circuits or directly
related circuit constraints. The original `SKILL.md` supplies the Circom-specific workflow;
this addendum supplies workspace routing and reporting constraints.

- Re-anchor on `/home/dinesh/.codex/AGENTS.md`, the current program memory, and the exact scope
  before using the delegated or local Circom workflow.
- The original skill's default artifact exclusions never override explicit program scope. Record
  every in-scope circuit/include/helper file in the coverage ledger and read it before concluding.
- Treat the original skill's findings and leads as candidates. Apply the workspace finding gate,
  exact duplicate/known-issue checks, scope rules, and evidence requirements before surfacing a
  report.
- Read only the relevant Circom references after the broad audit context and invariants are
  established. Do not bulk-load unrelated Solidity, Web2, or offensive skills.
- Preserve the distinction between source-only constraint reasoning, fresh runtime/witness
  evidence, and historical evidence. A generated report or agent agreement is not proof by
  itself.
- For a finding, record the exact circuit/template, constraint path, malicious witness or
  input, verifier acceptance path, impact, and the strongest concrete refutation attempt.
- Keep the workspace's final verdict labels and report standard authoritative. Do not claim that
  an audit is complete until every in-scope circuit has a first-pass read and the audit gate is
  satisfied.
