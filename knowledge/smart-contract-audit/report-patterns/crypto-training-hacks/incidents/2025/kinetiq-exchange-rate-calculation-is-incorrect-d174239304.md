# Crypto Training Exploit Pattern Stub: Kinetiq — Exchange rate calculation is incorrect

Source:
- https://crypto.training/hacks/58616-h-08-exchange-rate-calculation-is-incorrect-pashov-audit-gro/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58616-h-08-exchange-rate-calculation-is-incorrect-pashov-audit-gro`
- fingerprint: `d17423930460a87d442199694f8e292384193a55bb8020a0ca0e7f3281d21251`

Core exploit idea:
- 1. Multiple StakingManagers share one ValidatorManager (global rewards/slashing) and one kHYPE. 2. Each manager stores local totalStaked / totalClaimed. 3. getExchangeRa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
