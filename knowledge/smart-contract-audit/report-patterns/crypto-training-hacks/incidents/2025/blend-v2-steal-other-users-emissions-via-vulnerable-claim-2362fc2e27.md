# Crypto Training Exploit Pattern Stub: Blend v2 — Steal other users' emissions via vulnerable claim

Source:
- https://crypto.training/hacks/62062-h-02-user-can-steal-other-users-emissions-due-to-vulnerable/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62062-h-02-user-can-steal-other-users-emissions-due-to-vulnerable`
- fingerprint: `2362fc2e27f2c3cf7838de7109ea24cc2703fa6149ef464bf0027571809801f6`

Core exploit idea:
- 1. execute_claim can deposit exchanged backstop LP to a different to address. 2. It updates to's share balance without update_emissions(to). 3. A fresh to later claims w…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
