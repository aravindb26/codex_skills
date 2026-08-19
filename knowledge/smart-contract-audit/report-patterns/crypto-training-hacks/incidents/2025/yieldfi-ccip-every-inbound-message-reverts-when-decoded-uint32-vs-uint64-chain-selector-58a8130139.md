# Crypto Training Exploit Pattern Stub: YieldFi CCIP: every inbound message reverts when decoded (`uint32` vs `uint64` chain selector)

Source:
- https://crypto.training/hacks/55537-all-ccip-messages-reverts-when-decoded-cyfrin-none-yieldfi-m/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55537-all-ccip-messages-reverts-when-decoded-cyfrin-none-yieldfi-m`
- fingerprint: `58a8130139faead01cd5647e16a4b5367946aa9be198867ba8e13202bc4a8c27`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
