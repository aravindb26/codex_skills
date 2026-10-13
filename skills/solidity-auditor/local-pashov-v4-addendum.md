# Pashov Solidity Auditor v4 Addendum

Source reviewed: `pashov/skills` Solidity Auditor v4.1 at commit
`92b0ea6786e6c210bc9a839e4813d50876c1c550` on 2026-10-13.

This is a Codex-compatible companion to the locally customized Solidity auditor. It preserves
the useful v4 review controls without replacing the local `SKILL.md`, local Solodit addendum, or
Codex coverage/gate workflow.

## Apply When

Use these controls during a Solidity audit when one pass has not exhausted meaningful coverage,
when several agents or reasoning paths produce overlapping candidates, or when a report is being
assembled from multiple review passes. Do not use repeated passes as a reason to skip the mandatory
first-pass read of every in-scope file.

## Distinct Mechanisms And Function Isolation

- Keep the primary deduplication key scoped to `(contract, function, bug class)`.
- Never merge candidates only because they affect the same contract, symptom, protocol area, or
  consequence. Different functions remain different candidates unless exact root-cause analysis
  proves otherwise.
- Within one `(contract, function)`, perform a second mechanism pass over description, attack path,
  broken invariant, and fix. Preserve coexisting bugs instead of collapsing them into one vague
  finding.
- Canonicalize synonymous bug-class labels per contract/function so later passes recognize the same
  class, but do not use label similarity to merge different mechanisms.

## Completeness And Fix Preservation

- Before final reporting, account for every raw `(contract, function)` candidate. No candidate may
  disappear silently during deduplication or report assembly.
- Preserve every materially distinct mechanism, attacker path, and code-level fix. If two fixes
  address different checks or expressions, retain them as separate mitigation options or separate
  findings after the exact-root-cause review.
- A lead remains a lead until the current code path and evidence satisfy the normal finding gate;
  agreement between reviewers is not proof.

## Bounded Repeated Passes

When useful, run another bounded pass with a changed lens such as invariants, execution ordering,
economic impact, integration behavior, or boundary values. Each pass must read the current coverage
ledger, target new ground, and record what it checked and killed. Stop when the pass produces no
new meaningful mechanism, when the coverage ledger is complete, or when the program/time budget
requires a documented stop.

## Report Language

Use simple technical sentences: name the actor, action, and concrete effect; keep Solidity
identifiers exact; describe what the code does rather than using severity adjectives or metaphors.
Keep the local report template and evidence requirements authoritative. Do not silently convert a
source-only lead into a confirmed finding.

## Codex Adaptation

The upstream shell assembler, Claude-specific agent protocol, ToolSearch calls, and AskUserQuestion
interface are not copied here. Use the Codex coverage ledger, candidate-verification card, audit-gate
receipt, and normal `apply_patch`/terminal workflow as the equivalent controls.

The upstream default-discovery exclusions never override the current program's explicit scope.
If interfaces, deployment scripts, mocks, fixtures, tests, generated bindings, or another file
class is in scope, include it in the coverage ledger and read it; exclude only what the program
actually excludes or what the current workflow proves is out of scope.
