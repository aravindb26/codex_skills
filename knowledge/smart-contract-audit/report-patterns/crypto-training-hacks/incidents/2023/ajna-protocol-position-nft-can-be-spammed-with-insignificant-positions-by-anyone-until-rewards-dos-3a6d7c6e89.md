# Crypto Training Exploit Pattern Stub: Ajna Protocol — Position NFT can be spammed with insignificant positions by anyone until rewards DoS

Source:
- https://crypto.training/hacks/20071-h-03-position-nft-can-be-spammed-with-insignificant-position/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-authorization, dos/griefing, logic/reward-calculation

Dedupe:
- id: `20071-h-03-position-nft-can-be-spammed-with-insignificant-position`
- fingerprint: `3a6d7c6e89d45c2af53a2fe50fda6a1009a8d621eca5a7440d88bce3fdc78621`

Core exploit idea:
- 1. PositionManager.memorializePositions is external and — unlike burn(), moveLiquidity() and reedemPositions(), which are all gated by mayInteract (owner-or-approved) —…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
