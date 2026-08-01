# Crypto Training Exploit Pattern Stub: Renzo — incorrect withdraw queue balance in TVL calculation

Source:
- https://crypto.training/hacks/33495-h-08-incorrect-withdraw-queue-balance-in-tvl-calculation-cod/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `33495-h-08-incorrect-withdraw-queue-balance-in-tvl-calculation-cod`
- fingerprint: `9bbb6044535e2cb9dc2ba15a37403de8e23d5e6a35c6b53dd58ffa841ff62e3c`

Core exploit idea:
- 1. TVL loops ODs (i) then collateral tokens (j). 2. Withdraw-queue oracle call uses collateralTokens[i] for price but balanceOf token j. 3. With 1 OD and 3 tokens, token…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
