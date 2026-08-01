# Crypto Training Exploit Pattern Stub: Ammplify — H-10: `subtreeBorrowedX/Y` is node-only (makers underpaid)

Source:
- https://crypto.training/hacks/63176-h-10-takers-can-pay-significantly-less-fees-with-makers-losi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63176-h-10-takers-can-pay-significantly-less-fees-with-makers-losi`
- fingerprint: `13b7fec8607b8224e6f0e285c63accf91b53301c617373315cc0a0cda1fa48d7`

Core exploit idea:
- 1. Child holds large subtreeBorrowed; parent holds small own borrow. 2. Fee charge on parent adds only parent.subtreeBorrowedX (node-only). 3. Child mass ignored → fees…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
