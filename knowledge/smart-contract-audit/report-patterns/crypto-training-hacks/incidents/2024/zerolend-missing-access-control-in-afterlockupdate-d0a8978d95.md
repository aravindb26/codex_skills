# Crypto Training Exploit Pattern Stub: ZeroLend — Missing access control in afterLockUpdate

Source:
- https://crypto.training/hacks/40821-missing-accesscontrol-in-afterlockupdate-cantina-none-zerole/

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
- unknown

Dedupe:
- id: `40821-missing-accesscontrol-in-afterlockupdate-cantina-none-zerole`
- fingerprint: `d0a8978d95a58f0554928cc649dc66db6343cbc26eaa64f319899c07981645f8`

Core exploit idea:
- 1. afterLockUpdate is intended to be called only by ZeroLocker after lock changes. 2. It is external with no caller restriction. 3. Anyone holding pool tokens can self-r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
