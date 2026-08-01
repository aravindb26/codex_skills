# Audit Reference Checklists

This file contains reusable audit checklists and examples moved out of `AGENTS.md` to keep the always-loaded operating rules compact. Use it when the relevant surface is active, when starting a major audit phase, or when preparing a report.

## Context-Building Detail Checklist

When reading contracts, avoid listing functions as if that were understanding. Build a working mental model.

For serious audits, use senior-auditor discipline on every in-scope file. Read line by line and reason about contracts, inheritance, constructors, initializers, modifiers, functions, helpers, state variables, local variables, structs, enums, mappings, loops, conditionals, arithmetic, casts, rounding, unit conversions, storage writes, memory copies, external calls, callbacks, events, and error paths.

Many high-value bugs hide in:

- glue code that silently changes assumptions
- one variable updated before or after another
- cached values reused after state changes
- helpers called with the wrong assumptions
- constructors, initializers, or modifiers that change downstream security
- unusual `if`, `else`, loop, `break`, or `continue` paths
- zero, dust, max, boundary, stale, or partially-settled state
- storage-to-memory or memory-to-storage copies that snapshot or lose state
- decoded calldata fields that do not match execution semantics
- tiny rounding, scaling, or type-cast decisions
- revert, fallback, or callback paths that break invariants

For each important code unit, trace:

- what it is supposed to do
- caller, state, price, time, ordering, and integration assumptions
- what can invalidate those assumptions before, during, or after execution
- what other code depends on this behavior being exactly correct
- what breaks if logic is inverted, reordered, skipped, repeated, or reached in an edge state

For each important variable, trace:

- where it is initialized
- who can change it
- when it is read
- whether it is stale, cached, rounded, scaled, or unit-converted
- which invariant depends on it
- what happens if it is zero, max, dust, boundary, outdated, or inconsistent with another variable

For important functions, identify:

- caller and actor assumptions
- validations and preconditions
- state reads and writes
- token/value movement
- external calls and callbacks
- accounting updates
- emitted events
- revert conditions
- time, block, nonce, oracle, price, or cross-chain dependencies
- the invariant the function is supposed to preserve

For off-chain inputs and calldata parameters, always ask:

- Where was this calculated?
- When was it calculated?
- Can referenced state change before execution?

Quote-time confidence is not execution-time safety.

## High-Value Surfaces Checklist

Prioritize surfaces that can plausibly produce high or critical impact:

- deposits, withdrawals, minting, burning, redemption, and share accounting
- borrow, repay, collateral, liquidation, bad debt, and health-factor logic
- oracle source selection, stale prices, sequencer checks, TWAP/spot usage, and circuit breakers
- precision, decimals, rounding direction, scaling, and dimensional mismatches
- batch lifecycle, settlement, finalization, unwind, queue, and state handoff logic
- cross-chain supply/accounting, bridge assumptions, message replay, and domain separation
- access control, role boundaries, pause semantics, and emergency flows
- signature verification, permit, EIP-712 domains, nonces, expirations, and ERC-1271 paths
- reentrancy, callbacks, hooks, cross-function state reuse, and read-only reentrancy
- slippage, DEX integrations, swap routing, partial fills, stale orders, and off-chain quotes
- upgradeability, initialization, storage layout, and proxy admin assumptions
- external integrations such as ERC20 variants, fee-on-transfer tokens, rebasing tokens, and nonstandard return values

Be skeptical of comments, tests, and happy-path docs. Treat them as evidence to compare against code, not proof.

Prefer less-saturated areas when prior audits, V12 outputs, or public findings already heavily cover obvious surfaces.

## Evidence And Report Checklist

Every strong conclusion needs concrete evidence:

- exact local file paths
- exact line references when available
- exact functions and code paths
- exact commands actually run
- exact observed outputs
- exact reproduction steps
- exact reason why the branch survives or dies

Distinguish clearly between:

- source-only evidence
- fresh runtime evidence from the current session
- preserved historical runtime evidence
- reconstructed equivalent commands

If something was not run, say so plainly.

When writing a report, make it easy for a triager to accept or reject without extra back-and-forth. Include:

- severity
- title
- summary
- root cause
- affected code links or file references
- attack path
- required assumptions
- impact
- why it is in scope
- why it is not known, duplicate, intended, or trusted-role-only
- PoC command
- observed output
- recommended mitigation
- submission recommendation

Do not overclaim impact beyond what the code path or PoC proves.

## Skill Routing Examples

Common audit skills:

- `solidity-auditor` for Solidity audit workflow
- `smart-contract-audit` for broader protocol audits
- `audit-context-building` for deep code comprehension
- `behavioral-state-analysis` for state-machine and lifecycle analysis
- `state-invariant-detection` for broken accounting/state relationships
- `dimensional-analysis` for units, decimals, and scaling issues
- `fp-check` to kill weak or suspicious candidates
- `differential-review` for commit/PR/regression review
- `audit-oracle`, `oracle-flashloan-analysis`, `audit-reentrancy`, `audit-signature`, `audit-slippage`, `audit-lending`, `audit-liquidation`, and `proxy-upgrade-safety` for focused threat classes
- `hackenproof-triage-marketplace`, `hackenproof-poc-grader`, `hackenproof-triage-mistakes`, `hackenproof-comment-templates`, `hackenproof-report-handoff`, `hackenproof-fix-verifier`, `hackenproof-bulk-triage`, and `hackenproof-all-reports-export` for HackenProof triage, evidence review, comments, handoff, fix verification, bulk review, and report export work

## Web2 And Offensive Reference

Reference-only offensive/AppSec skills may live outside the active Codex skills directory, especially:

- `/home/dinesh/.codex/offensive-skills/`
- `/home/dinesh/.codex/offensive-skills/claude-red/`
- `/home/dinesh/.codex/offensive-skills/claude-bug-bounty/`
- `/home/dinesh/.codex/offensive-skills/selected-security-addenda/`

These are not part of the default smart-contract audit toolbox. Do not use them during Solidity/Vyper/Solana/Cosmos/Web3 contest audits unless the user explicitly asks for AppSec/red-team/source-code methodology or the target is clearly a non-smart-contract application.

Use `/home/dinesh/.codex/offensive-skills/` selectively for:

- web application bug bounty work
- source-code AppSec audits
- API, GraphQL, REST, auth, JWT, OAuth, IDOR, SSRF, SQLi, XSS, SSTI, deserialization, file-upload, and business-logic testing
- cloud, mobile, IoT, infrastructure, AI-app, and fuzzing/vulnerability-research workflows
- pentest-style report writing

When using the Claude-Red reference library, start with `/home/dinesh/.codex/offensive-skills/claude-red/SKILL_INDEX.md`, then load only the specific `skills/<skill-name>/SKILL.md` file relevant to the target. Do not bulk-load the whole library.

When using selected addenda from reviewed third-party repos, start with `/home/dinesh/.codex/offensive-skills/selected-security-addenda/SKILL_INDEX.md`, then open only the exact note matching the current Web2/source-code task. These addenda are distilled to avoid duplicate Web3 noise and do not include upstream scripts.

For Web2/source-code AppSec audits, Snyk is available as a scanner/lead generator after program scope and safe-harbor are understood. Use it only for non-Web3 source-code, dependency, IaC, and container review. Save outputs under the target workspace, for example `.context/snyk/`:

- `snyk test --all-projects --severity-threshold=medium --json-file-output=.context/snyk/open-source.json || true`
- `snyk code test --severity-threshold=medium --json-file-output=.context/snyk/code.json || true`
- `snyk iac test --severity-threshold=medium --json-file-output=.context/snyk/iac.json || true`
- `snyk container test <image> --severity-threshold=medium --json-file-output=.context/snyk/container.json || true`

Treat Snyk findings as leads, not conclusions. Merge Snyk candidates with manual/offensive-skills candidates, then validate reachability, attacker control, auth or tenant boundary, real impact, scope, duplicate risk, and exploitability before reporting.
