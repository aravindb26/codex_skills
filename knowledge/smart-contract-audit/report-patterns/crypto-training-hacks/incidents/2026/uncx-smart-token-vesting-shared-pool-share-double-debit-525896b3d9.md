# Crypto Training Exploit Pattern Stub: UNCX Smart Token Vesting — Shared-Pool Share Double-Debit

Source:
- https://crypto.training/hacks/2026-10-uncxsmarttokenvesting/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- This transaction keeps, after every flash loan is repaid: 55,601,598.708417972560603048 E…

Tags:
- logic/state-update, logic/incorrect-state-transition, logic/missing-check

Dedupe:
- id: `2026-10-uncxsmarttokenvesting`
- fingerprint: `525896b3d901070b5d9a505d2975bd418261fdb612636cb1d3961d4e42ee5eb9`

Core exploit idea:
- UNCX Smart Token Vesting V2 keeps every vesting of a given ERC-20 in one contract balance and tracks ownership with internal shares. release() pays a fraction of that wh…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
