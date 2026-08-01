# Crypto Training Exploit Pattern Stub: Unverified-proxy USDT drain via recipient-only signature — signed 5-min/recipient message did not bind victim, token, amount, or nonce

Source:
- https://crypto.training/hacks/2025-07-unverified_8fd3/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- BNB Chain

Loss / impact summary:
- 502.42 USDT (502.420508729654666584, trace balance) — the on-chain attack tx drained the…

Tags:
- auth/signature-validation, auth/signature-replay, logic/missing-validation

Dedupe:
- id: `2025-07-unverified_8fd3`
- fingerprint: `28119b9eae058f830320c692295065b4f2ed5f0e70351248f924bb99038d9697`

Core exploit idea:
- A BNB-chain protocol exposed a delegatecall-based proxy (0xE641…106c) backed by an unverified implementation (0x8Fd3…7f0A). One of its functions (selector 0x97e76253) ta…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
