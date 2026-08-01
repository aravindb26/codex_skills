# Crypto Training Exploit Pattern Stub: Optimism Interop — malicious tokens at deterministic addresses steal cross-chain funds

Source:
- https://crypto.training/hacks/50077-malicious-tokens-can-be-deployed-at-deterministic-addresses/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Optimism

Loss / impact summary:
- unknown

Tags:
- access-control/misplaced-trust, cross-chain/address-assumption, loss-of-funds/unbacked-mint

Dedupe:
- id: `50077-malicious-tokens-can-be-deployed-at-deterministic-addresses`
- fingerprint: `4ba9af7160636a0221c174e30e9c88882992258945a79c45c30d20a8f5cabf96`

Core exploit idea:
- 1. Superchain tokens are deployed through a generic CREATE2 factory that exists at the same address on every interop chain. A token's address therefore depends only on (…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
