# Crypto Training Exploit Pattern Stub: Royco RecipeOrderbook — successful transfers on non-existent tokens let attackers steal reward tokens

Source:
- https://crypto.training/hacks/46673-successful-transfers-on-non-existent-tokens-allows-attackers/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, token/codeless-token-transfer, loss-of-funds/reward-theft

Dedupe:
- id: `46673-successful-transfers-on-non-existent-tokens-allows-attackers`
- fingerprint: `3495846fc48ef7d336260928cc27c87c9e3dfd72989124f9245413348f675f0c`

Core exploit idea:
- 1. Solmate's SafeTransferLib does not check that a token has code. A CALL to a codeless address returns success with empty returndata, and the library's iszero(returndat…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
