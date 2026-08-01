# Crypto Training Exploit Pattern Stub: Monolith — free-debt rounding allows unbacked borrow

Source:
- https://crypto.training/hacks/64955-h-1-user-can-abuse-rounding-issue-in-order-to-borrow-unbacke/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64955-h-1-user-can-abuse-rounding-issue-in-order-to-borrow-unbacke`
- fingerprint: `6e4d38ce0e677b41682ae34c1176e5cdbbb712c91bd337475513bb09bc58ff8e`

Core exploit idea:
- 1. Free-debt share math rounds personal debt up. 2. Redeem + debase loops inflate freeShares / freeDebt; residual shares can survive after the last free-debt wei is repa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
