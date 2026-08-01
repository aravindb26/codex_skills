# Crypto Training Exploit Pattern Stub: LEND — Incorrect distribution of LEND tokens to users

Source:
- https://crypto.training/hacks/58384-lend-incorrect-distribution-of-lend-tokens-to-users/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/state-update

Dedupe:
- id: `58384-lend-incorrect-distribution-of-lend-tokens-to-users`
- fingerprint: `4a1cb03a8c4a317585323452c0cd3ed7bb9fab024a98105afbfacc9544e236ac`

Core exploit idea:
- The distribution loop credits a user's reward before applying the global index delta, resulting in an over-credit that the reserve must fund.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
