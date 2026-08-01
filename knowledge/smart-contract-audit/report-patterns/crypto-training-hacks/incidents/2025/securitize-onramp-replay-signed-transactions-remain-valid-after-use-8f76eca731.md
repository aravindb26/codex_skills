# Crypto Training Exploit Pattern Stub: Securitize OnRamp replay — signed transactions remain valid after use

Source:
- https://crypto.training/hacks/64270-missing-nonce-validation-in-signature-verification-allows-tr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/replay, auth/signature-validation, logic/missing-validation

Dedupe:
- id: `64270-missing-nonce-validation-in-signature-verification-allows-tr`
- fingerprint: `8f76eca731569bf1cb29457931d723ba6a9702a5d99e512f1e5316d5d6504232`

Core exploit idea:
- executePreApprovedTransaction includes a nonce in the signed payload, but only increments the stored nonce. It never requires the supplied nonce to equal the current exp…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
