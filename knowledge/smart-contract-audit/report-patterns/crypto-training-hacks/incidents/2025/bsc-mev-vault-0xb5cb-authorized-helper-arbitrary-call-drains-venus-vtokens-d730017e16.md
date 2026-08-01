# Crypto Training Exploit Pattern Stub: BSC MEV Vault `0xb5cb…` — Authorized Helper Arbitrary Call Drains Venus vTokens

Source:
- https://crypto.training/hacks/2025-06-BSCArbitraryCall0xb5cb/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~$1.1M first tx; campaign ~$2M across follow-ups (TenArmor)

Tags:
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `2025-06-BSCArbitraryCall0xb5cb`
- fingerprint: `d730017e16377ec4ef1f6dfd4e9a90cd13ea2d32045ae3db97923a3ef11b8312`

Core exploit idea:
- A Venus-integrated MEV / strategy vault (0xb5cb…e1b0) gates sensitive operations (including vToken transfers via selector 0x0243f5a2) behind isAuthorized. Days before th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
