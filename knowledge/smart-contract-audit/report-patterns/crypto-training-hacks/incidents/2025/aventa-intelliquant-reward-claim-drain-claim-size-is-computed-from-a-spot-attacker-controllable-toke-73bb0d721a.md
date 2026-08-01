# Crypto Training Exploit Pattern Stub: Aventa / IntelliQuant reward-claim drain — claim size is computed from a spot, attacker-controllable token balance

Source:
- https://crypto.training/hacks/2025-04-AventaRewardClaim/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Ethereum

Loss / impact summary:
- ~16,019,528 AVENTA (≈ 16.0 M tokens), monetised to ~3.9 ETH by the PoC batch of 12 helper…

Tags:
- logic/reward-calculation, oracle/spot-price, access-control/broken-logic

Dedupe:
- id: `2025-04-AventaRewardClaim`
- fingerprint: `73bb0d721ada7e78012a900d6ea2c853a14bed69139547a80faa0851f3b9987a`

Core exploit idea:
- AventaRewardClaim.claim(user) is meant to pay AVENTA rewards to existing IntelliQuant holders. The amount it pays is IntelliQuant.balanceOf(user) read at call time — not…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
