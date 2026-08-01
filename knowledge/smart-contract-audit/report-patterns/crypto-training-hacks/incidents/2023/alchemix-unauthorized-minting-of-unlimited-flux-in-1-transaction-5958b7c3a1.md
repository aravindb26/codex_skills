# Crypto Training Exploit Pattern Stub: Alchemix — unauthorized minting of unlimited FLUX in 1 transaction

Source:
- https://crypto.training/hacks/38109-unauthorized-minting-of-unlimited-flux-in-1-transaction-immu/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier, reward-calculation/unbounded-accrual, loss-of-funds/direct-drain

Dedupe:
- id: `38109-unauthorized-minting-of-unlimited-flux-in-1-transaction-immu`
- fingerprint: `5958b7c3a142ff4600f0bab52c203e387483355568350f3ff9f36a57b4f90462`

Core exploit idea:
- 1. A veALCX position accrues FLUX once per epoch by calling voter.poke(tokenId), which internally calls _vote() → FluxToken.accrueFlux(tokenId). 2. poke() is missing the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
