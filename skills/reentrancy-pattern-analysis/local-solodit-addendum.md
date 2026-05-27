# Local Solodit Addendum: Reentrancy Pattern Companion Mini-Skill

## Purpose
- Keep `reentrancy-pattern-analysis` aligned with the curated Solodit reentrancy memory.
- Avoid duplicating the larger addendum in `audit-reentrancy`.

## When To Use

Use after reading `reentrancy-pattern-analysis/SKILL.md` when callbacks, hooks, token transfers, native sends, minting, claiming, bridge callbacks, queue processing, or liquidation callbacks are present.

## Companion Workflow

1. Use this skill's original workflow for broad reentrancy detection.
2. Also read `/home/dinesh/.codex/skills/audit-reentrancy/local-solodit-addendum.md`.
3. Apply the Solodit-derived subpatterns from that file: mint/claim callbacks, limit bypass, flash-action callbacks, cross-contract shared state, read-only pricing, replay/message callbacks, guard misuse, callback auth, auction/liquidation, bridge accounting, queue/batch adapters, and callback griefing.
4. Escalate only if the current code path proves stale state, reachable reentry, missing protection, and rewardable impact.

## False-Positive Filters

Do not escalate unless:
- The callback/reentry target is reachable by an in-scope attacker.
- The stale or temporary state affects funds, accounting, authorization, replay protection, or liveness.
- Existing guards cover neither the same-function nor cross-function/cross-contract path.
