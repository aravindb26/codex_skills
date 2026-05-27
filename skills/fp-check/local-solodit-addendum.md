# Local Solodit Addendum: Smart Contract False-Positive Check

## Purpose

Use this companion with `fp-check` when validating smart contract or Web3 bounty findings.

The goal is not only to decide whether a bug is technically real. The goal is to decide whether it is real, in scope, impact-backed, non-duplicate, and strong enough to survive triage.

## When To Use

Use this addendum when the candidate involves:

- smart contracts, blockchain runtimes, bridges, rollups, appchains, Cosmos/Solana/Substrate/Cairo/TON/Algorand programs, or Web3 protocol code
- a suspected high/critical impact claim
- a candidate that came from a scanner, skill checklist, Solodit pattern, article, X post, or previous report
- a branch that looks interesting but may be weak, duplicate-prone, or out of scope

## Companion Workflow

1. Restate the exact claim.
2. Identify the alleged root cause, attacker, trigger, asset, and impact.
3. Check the current program scope, exclusions, severity bar, trusted roles, known issues, prior audits, and AI-excluded outputs.
4. Search `/home/dinesh/.codex/knowledge/smart-contract-audit/` for related rejected findings, triage rejection patterns, accepted patterns, and Solodit stubs.
5. Compare the candidate against both accepted public bugs and rejected local branches.
6. Trace the real execution path from attacker-controlled input to final state effect.
7. Check whether upstream validation, modifiers, caller restrictions, pause state, oracle constraints, token behavior, or lifecycle state kills the path.
8. Define the strongest rejection argument before calling it valid.
9. Require runtime proof for high/critical claims when feasible.
10. Return only `STRONG SUBMIT-WORTHY` or `NOT WORTH SUBMITTING` unless the user asks for a middle bucket.

## False-Positive Filters

Mark `NOT WORTH SUBMITTING` if the claim depends on:

- admin, owner, multisig, keeper, oracle admin, relayer, or backend misuse unless the program explicitly includes that trust boundary
- deployer misconfiguration outside the accepted deployment model
- stale or unsupported historical state
- offchain service dishonesty where the contract is not expected to defend onchain
- a scanner warning without traced exploitability
- a revert-only grief with no meaningful asset, liveness, or bounty impact
- protocol fee loss where the program only rewards user-fund loss or chain halt
- dust-only loss unless the same root cause scales
- hypothetical token behavior not accepted by the protocol's token list or integration assumptions
- duplicate root cause, even if the surface or wording is different

## Evidence Requirements

For a surviving candidate, document:

- exact local file paths and line references
- attacker-controlled inputs and reachable call path
- all relevant preconditions
- exact state before and after the exploit
- value movement or invariant break
- why scope and severity rules accept the impact
- why known issues, Solodit patterns, and prior local rejected findings do not already cover it
- PoC command and observed output, if run

## Solodit-Informed Checks

Search accepted public report patterns for the same bug class, but do not copy their conclusion. Ask:

- Does this protocol have the same invariant and same missing guard?
- Is the exploit path reachable under this program's deployment and roles?
- Does the impact match the current program's severity bar?
- Is the current root cause distinct from known issues and likely duplicates?
- Would a triager group this with an already submitted issue?

## Output Requirements

When this addendum is used, include:

- verdict
- exact reason the branch survives or dies
- strongest rejection argument
- whether that rejection argument is beaten by evidence
- validation status: source-only, preserved historical runtime evidence, or fresh runtime evidence
