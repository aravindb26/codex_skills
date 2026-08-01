# Crypto Training Exploit Pattern Stub: CAP Labs — fee auction charges for zero assets

Source:
- https://crypto.training/hacks/61536-fee-auction-zero-assets/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- defi/fee-manipulation, defi/sandwich-attack, input-validation/missing

Dedupe:
- id: `61536-fee-auction-zero-assets`
- fingerprint: `7832c502058b8315617e7d0eb3a3eba38e3ce67713d36dc8f5797ffc4fbd2719`

Core exploit idea:
- FeeAuction.buy does not bind a purchase to an auction or require a non-empty basket. A front-runner drains the basket, then the victim pays the doubled price for zero ou…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
