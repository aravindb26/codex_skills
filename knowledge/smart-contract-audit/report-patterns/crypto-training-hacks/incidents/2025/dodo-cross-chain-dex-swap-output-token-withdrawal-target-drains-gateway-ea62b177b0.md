# Crypto Training Exploit Pattern Stub: DODO Cross-Chain DEX — swap output token ≠ withdrawal target drains gateway

Source:
- https://crypto.training/hacks/58578-h-1-missing-swap-withdrawal-validation-enables-accumulated-t/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/cross-contract-state-consistency, loss-of-funds/direct-drain, bridge/message-parameter-mismatch

Dedupe:
- id: `58578-h-1-missing-swap-withdrawal-validation-enables-accumulated-t`
- fingerprint: `ea62b177b0ce12baa00e90eb631971bd2787ac6a8c005c4b79186c64e348bd6c`

Core exploit idea:
- 1. onCall performs _doMixSwap(..., params.toToken) then withdraws decoded.targetZRC20. 2. Nothing requires toToken == targetZRC20. 3. Attacker crafts a message: swap BTC…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
