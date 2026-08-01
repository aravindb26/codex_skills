# Crypto Training Exploit Pattern Stub: Alchemix — malicious user can mint unlimited FLUX tokens

Source:
- https://crypto.training/hacks/38179-malicious-user-can-mint-unlimited-flux-tokens-immunefi-alche/

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
- logic/missing-epoch-guard, accounting/double-counting, economic/unbounded-mint

Dedupe:
- id: `38179-malicious-user-can-mint-unlimited-flux-tokens-immunefi-alche`
- fingerprint: `bb80d1c73d9246c4a9e89c4dc2f8094b18f5499bdfba7ae0947fde4e3f83dac1`

Core exploit idea:
- 1. Users earn FLUX proportional to their veALCX's current locked value. Calling Voter.reset(tokenId) adds claimableFlux(tokenId) to the token's unclaimed FLUX balance —…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
