# Crypto Training Exploit Pattern Stub: Notional v4 — redeemNative reentrancy freezes yield tokens

Source:
- https://crypto.training/hacks/63524-redeemnative-reentrancy-enables-permanent-fund-freeze-system/

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
- unknown

Dedupe:
- id: `63524-redeemnative-reentrancy-enables-permanent-fund-freeze-system`
- fingerprint: `5aedc8a5745f972995012473246020b509fa61fb037f13e8550579226d1af895`

Core exploit idea:
- redeemNative snapshots balance, swaps via a path including a malicious token that reenters initiateWithdraw (moves N yield tokens and decrements accounting). After retur…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
