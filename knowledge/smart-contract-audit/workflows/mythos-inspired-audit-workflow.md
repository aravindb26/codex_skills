# Mythos-Inspired Audit Workflow

Purpose:
- Make Codex audit like a disciplined multi-pass security team, not a single blind scanner.
- This is inspired by public descriptions of Mythos / Glasswing workflows, but it is our own local workflow. It does not require Mythos access.

Use when:
- Starting a new smart contract audit, Web3 contest, bounty target, or serious source-code review.
- Re-auditing a candidate before deciding whether it is submit-worthy.

Do not use as:
- A replacement for scope, rules, known issues, or manual reading.
- A promise that every bug will be found.

## Phase 0: Program Lock

Goal:
- Prevent wasted work on out-of-scope, duplicate, or non-rewardable branches.

Actions:
- Read every available program source completely before hunting: program page, scope, exclusions, rewards, severity definitions, duplicate rules, safe harbor, testing constraints, known issues, prior audits, V12/excluded AI outputs, local notes, and attachments.
- If any source is inaccessible, JS-rendered, partial, ambiguous, or missing, mark it as a Program Lock gap and ask for pasted text, screenshots, exports, or local files.
- Identify trusted roles, allowed attacker model, deployment assumptions, and required PoC format.
- Search the local knowledge base for protocol type and major primitives.
- Do not start serious hunting until Program Lock is complete or the remaining gaps are explicitly listed as residual risk.

Outputs:
- Program Memory: compact locked summary of rules, scope, exclusions, severity bar, reward logic, trusted roles, PoC/report requirements, and rejection risks.
- Rules/source coverage ledger: each program source and whether it was read fully.
- Scope summary.
- In-scope file list.
- Exclusion list.
- Known duplicate-risk sources.
- Initial triage bar: what counts as High/Critical for this program.

## Phase 1: Map

Goal:
- Build the first mental model before serious hunting.

Actions:
- Enumerate every in-scope file.
- Map contracts/modules, actors, permissions, state-changing entry points, external integrations, and value flows.
- Track money flow: where value enters, exits, moves, gets locked, gets minted, or gets burned.
- Identify likely high-risk modules.

Outputs:
- Architecture map.
- Entry-point table.
- Money-flow map.
- First file-risk ranking.

## Phase 2: Full First-Pass Reading

Goal:
- Remove blind spots before calling the audit mature.

Actions:
- Read every in-scope file line by line.
- For each file, record main purpose, critical state, trust assumptions, state transitions, and suspicious snippets.
- Mark first-pass coverage complete only when every line has been read enough to explain its role.
- Do not rely on scanners, summaries, or pattern matching as a substitute for reading.

Outputs:
- Coverage ledger.
- Per-file notes.
- Suspicious-logic queue.
- Unknown-primitives queue.

## Phase 3: Learn Unknowns

Goal:
- Stop shallow auditing caused by unfamiliar primitives.

Actions:
- For every unknown primitive, integration, math method, VM behavior, standard, or protocol mechanism, learn it before trusting it.
- Search `/home/dinesh/.codex/knowledge/smart-contract-audit/` first.
- If local memory is insufficient, use primary sources: official docs, standards, source code, protocol docs, incident reports, or prior audits.
- Distill any useful new lesson into the knowledge base.

Outputs:
- Unknowns resolved or explicitly listed as residual risk.
- Relevant pattern notes linked.

## Phase 4: Invariant Build

Goal:
- Convert understanding into breakable claims.

Actions:
- Extract explicit invariants from docs and implicit invariants from code.
- Write invariants per module and per cross-module flow.
- Include accounting, solvency, authorization, lifecycle, rounding, oracle, bridge, queue, and integration invariants.
- Build edge-case sets: zero, dust, max, stale, boundary, partial, repeated, cross-chain delay, callback, and malicious integration.

Outputs:
- Invariant ledger.
- Edge-case ledger.
- Candidate attack surfaces.

## Phase 5: Attack Pass

Goal:
- Try to break each meaningful logic path.

Actions:
- For each high-risk entry point, reverse ordering assumptions, repeat calls, split flows, force boundary values, and test stale state.
- Trace from entry point to final state effect.
- Check helpers, modifiers, inherited behavior, external calls, callback paths, events, and downstream accounting.
- Use relevant skills such as `audit-context-building`, `behavioral-state-analysis`, `state-invariant-detection`, `dimensional-analysis`, `fp-check`, and focused audit skills.
- Search Solodit/report stubs for similar historical bugs when a pattern appears.

Outputs:
- Candidate findings.
- Killed branches with exact reason.
- Branches requiring PoC.

## Phase 6: Verification Pass

Goal:
- Kill weak findings before they waste submission time.

Actions:
- For each candidate, try to disprove it first.
- Check actual execution path, scope, known issues, intended behavior, duplicates, trusted-role dependence, offchain dependence, and severity bar.
- Re-read the full path from entry point to final state effect.
- Use a second-pass mindset: assume the first-pass candidate is wrong until the code and PoC prove otherwise.

Outputs:
- `STRONG SUBMIT-WORTHY` or `NOT WORTH SUBMITTING`.
- Strongest rejection argument.
- Evidence beating or failing that argument.

## Phase 7: PoC / Harness

Goal:
- Prove only survivors.

Actions:
- Build the smallest useful PoC.
- Prefer real protocol contracts and minimal mocks.
- Prove the exact claimed impact: fund loss, fund lock, unauthorized state change, solvency break, invariant break, or rewardable impact.
- Run narrow tests and record exact commands and output.
- Keep harness clean.

Outputs:
- PoC file path.
- Command run.
- Observed output.
- Impact proof.

## Phase 8: Triage Report

Goal:
- Make the finding easy to accept and hard to dismiss.

Actions:
- Write root cause, attack path, impact, scope fit, duplicate check, intended-behavior check, trusted-role check, PoC command, output, and mitigation.
- Avoid overclaiming.
- If the issue is real but weak, mark `NOT WORTH SUBMITTING`.

Outputs:
- Final report or killed-branch note.

## Phase 9: Learning Loop

Goal:
- Make the next audit stronger.

Actions:
- Save accepted findings into `finding-library.md`.
- Save missed findings into `miss-library.md`.
- Save rejected findings into `rejected-findings/`.
- Save dead branches into `dead-branches.md`.
- Save new attack patterns from articles/reports into the correct knowledge-base folder.

Outputs:
- Updated knowledge base.

## Minimum Live Update Format

Use this during active audits:

Status:
- coverage:
- checked:
- killed:
- alive:
- next:

Verdict:
- `STRONG SUBMIT-WORTHY`
- `NOT WORTH SUBMITTING`

Why:
- evidence-backed points only

Residual risk:
- unread files, untested paths, unresolved unknowns, or duplicate-risk gaps
