# Crypto Training Exploit Pattern Stub: LMCV — failed Hyperlane message replay mints dPRIME repeatedly

Source:
- https://crypto.training/hacks/50682-unlimited-minting-by-reusing-failed-hyperlane-messages-halbo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/replay, bridge/missing-validation, logic/state-update

Dedupe:
- id: `50682-unlimited-minting-by-reusing-failed-hyperlane-messages-halbo`
- fingerprint: `9b03d6239acb8b058f3f16412a986b8ef776bf2af9761f192d5a732a8d1266e3`

Core exploit idea:
- A failed Hyperlane transfer remains in failedMessages after retry succeeds. The exact same origin, recipient, and nonce can be retried repeatedly, minting the amount aga…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
