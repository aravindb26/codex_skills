# Crypto Training Exploit Pattern Stub: Alchemix — infinite minting of FLUX through `voter.poke()`

Source:
- https://crypto.training/hacks/38110-infinite-minting-of-flux-through-voterpoke-immunefi-alchemix/

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
- governance/proposal-manipulation, reward-calculation/unbounded-accrual, loss-of-funds/direct-drain

Dedupe:
- id: `38110-infinite-minting-of-flux-through-voterpoke-immunefi-alchemix`
- fingerprint: `4ec96b1eedd7b2eb53a1aa7b6b1dbc0e33b7271a17e9ad17f64e754a6a9582a6`

Core exploit idea:
- 1. poke(tokenId) calls _vote(tokenId), which unconditionally calls FluxToken.accrueFlux(tokenId). 2. accrueFlux does unclaimedFlux[tokenId] += claimableFlux(tokenId) — i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
