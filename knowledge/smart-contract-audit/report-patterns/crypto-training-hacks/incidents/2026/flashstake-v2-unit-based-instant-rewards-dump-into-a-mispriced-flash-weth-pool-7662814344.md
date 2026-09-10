# Crypto Training Exploit Pattern Stub: Flashstake V2 — Unit-based instant rewards dump into a mispriced FLASH/WETH pool

Source:
- https://crypto.training/hacks/2026-08-flashstakev2/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 0.545290142368948672 WETH drained from the FLASH/WETH reward pool (~$886); attacker net 0…

Tags:
- logic/reward-calculation, oracle/missing-validation, logic/missing-check

Dedupe:
- id: `2026-08-flashstakev2`
- fingerprint: `7662814344bfda63c4c704e2fb99ea90f82242ea02f669c8417dccf5e876fb82`

Core exploit idea:
- 1. Flashstake V2 pays yield up front. A user locks FLASH for a chosen number of seconds. getMintAmount() sizes the minted FLASH as amountIn expiry FPY / (1e18 365 days)…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
