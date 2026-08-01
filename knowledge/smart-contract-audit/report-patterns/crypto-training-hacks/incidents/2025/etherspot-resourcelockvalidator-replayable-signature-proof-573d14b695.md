# Crypto Training Exploit Pattern Stub: Etherspot ResourceLockValidator — replayable signature proof

Source:
- https://crypto.training/hacks/61409-c-07-resource-lock-validator-signature-proof-replay/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/replay, auth/signature-replay

Dedupe:
- id: `61409-c-07-resource-lock-validator-signature-proof-replay`
- fingerprint: `573d14b695ab1345ffe610e358a026641e2521a9221f99ec021c0e7b9e877e18`

Core exploit idea:
- The validator checks a ResourceLock Merkle proof but never consumes it. EntryPoint can therefore submit the same call data with a different nonce, and the wallet execute…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
