# Arsen Critical-Flow Audit Workflow

Purpose:
- Prioritize the small set of protocol paths where value, trust, and security-critical state concentrate.
- Use AI to reduce navigation and context-building time while keeping security judgment with the auditor.

Source:
- Captured from the user-provided Arsen security-auditor methodology on 2026-09-12.
- This file records the useful workflow, not a claim that the source guarantees complete bug discovery.

Use when:
- The program lock is complete or its remaining gaps are explicitly recorded.
- The architecture and broad in-scope file map are available.
- A serious smart-contract or Web3 audit is moving from orientation into focused hunting.

Do not use as:
- A replacement for the complete program rules, scope, known-issue checks, skills, knowledge base, or PoC requirements.
- Permission to skip any in-scope file or to declare coverage complete before the required first pass.
- A reason to trust an AI-generated system summary without checking it against source code.

## Stage 1: Map the System

Answer: what are the main actions, actors, trust boundaries, and value movements?

Actions:
- Read the relevant program documents, protocol documentation, and integration code.
- Divide the repository into understandable sections instead of asking for one explanation of the entire repository.
- Identify actors, permissions, assumptions, invariants, integrations, and state-changing entry points.
- Store the compact map in the current program memory or audit workspace. JSON is acceptable when it makes the structure easier to query, but it does not replace the required ledgers.
- Check every AI-generated summary against the actual code and record unresolved gaps.

Outputs:
- Actors and trust-boundary map.
- Protocol actions and module map.
- Initial invariant and assumption list.
- Initial list of value-carrying or security-critical flows.

## Stage 2: Follow Critical Value Flows

Select the flows that can directly move, create, destroy, lock, or misprice value, or that control a security-critical state transition.

Common examples:
- deposit, mint, borrow, repay, withdrawal, redeem, and liquidation
- swap, liquidity update, fee settlement, and reward claim
- bridge transfer, message verification, proof acceptance, and finalization
- position update, oracle update, auction settlement, and callback execution

For each selected flow, trace it end to end:
- Who can call each step?
- What can the caller control?
- What state does each step read and mutate?
- Where does value enter, exit, or move between components?
- What must never happen?
- Which assumptions and invariants must remain true?
- Which helpers, integrations, callbacks, inherited functions, and downstream accounting affect the result?

Do not stop at the public entry point. Continue until the final asset transfer, state transition, or externally observable effect.

## Stage 3: Maintain a Thinking Workspace

Keep explicit working artifacts for:
- architecture and value-flow diagrams
- per-flow invariants
- actor capabilities and trust assumptions
- attack ideas and their current status
- unanswered questions and unknown primitives
- code paths already checked and paths requiring a second pass

If a function or flow cannot be explained in one clear sentence, return to the code and resolve the gap before relying on it for a finding.

## Stage 4: Run the AI Audit Pass

Only after the system map and critical-flow understanding exist:
- Search the knowledge base for prior bug patterns, accepted findings, rejected findings, and attacker lenses relevant to the protocol and selected flows.
- Read the original relevant skills and their local addenda.
- Convert the matched material into concrete hypotheses and invariant checks.
- Analyze one bounded module, flow, or hypothesis at a time rather than feeding the whole repository into one prompt.
- Use AI for navigation, decomposition, pattern generation, and tooling suggestions; verify every material claim against source code and runtime evidence.

The quality of the attack-pattern database and the order of the passes affect coverage. Running scanners or broad AI hunting before understanding the critical flows creates validation noise and can hide the important paths.

## Stage 5: Protocol-Specific Deep Pass

After the initial attack pass appears exhausted, identify the mechanism most capable of draining, locking, or corrupting protocol value and review it again.

Examples:
- lending: collateral valuation, debt accounting, liquidation math, and bad-debt handling
- bridges: message replay, domain separation, proof freshness, and mint/burn conservation
- AMMs and CLMMs: invariant math, tick/price transitions, liquidity accounting, zero-delta behavior, and boundary states
- staking and rewards: index updates, claim accounting, epoch cleanup, and boost/vote transitions
- vaults: share pricing, deposits/withdrawals, fees, rounding, queues, and settlement lifecycle

For integrations, inspect both sides of the interface and verify units, trust assumptions, callbacks, failure handling, and state freshness. For heavy mathematics, build focused invariant or fuzzing tests after manually understanding the equations. For new mechanisms, perform another invariant-first deep read.

## Compatibility and Completion Rules

- This workflow prioritizes deep review; it does not reduce the mandatory first-pass reading of every in-scope file.
- Critical-flow prioritization determines where to spend additional depth, not which scoped files may be ignored.
- Follow `/home/dinesh/.codex/knowledge/smart-contract-audit/workflows/mythos-inspired-audit-workflow.md` for the full multi-pass sequence, gates, and outputs.
- Follow `/home/dinesh/.codex/AGENTS.md` for program scope, evidence, duplicate checks, strengthening, PoC validation, reporting, and cleanup.
- Do not treat a passing scanner, AI hypothesis, or flashy PoC as a submit-worthy finding without the full triage gate.
- Continue the critical deep pass until the coverage ledger records the tested mechanisms, killed branches, surviving candidates, and meaningful residual uncertainty.
