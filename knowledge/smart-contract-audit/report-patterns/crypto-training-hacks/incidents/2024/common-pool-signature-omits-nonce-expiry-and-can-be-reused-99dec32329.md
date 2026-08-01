# Crypto Training Exploit Pattern Stub: Common Pool — signature omits nonce/expiry and can be reused

Source:
- https://crypto.training/hacks/52006-signature-does-not-take-all-parameters-into-account-and-can/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/incomplete-scope, auth/replay

Dedupe:
- id: `52006-signature-does-not-take-all-parameters-into-account-and-can`
- fingerprint: `99dec323294e61879dff5759734a90f1be4c207a6696feeedc69ec96c66b4583`

Core exploit idea:
- 1. Signed digest is keccak256(abi.encode(DEPOSIT_STRUCT, multicall/amount)) only. 2. sig.nonce and sig.expiry are checked but not bound into the digest. 3. Observer re-s…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
