# Crypto Training Exploit Pattern Stub: Foundation — Creators can steal sale revenue from owners' sales

Source:
- https://crypto.training/hacks/42485-h-02-creators-can-steal-sale-revenue-from-owners-sales-code4/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `42485-h-02-creators-can-steal-sale-revenue-from-owners-sales-code4`
- fingerprint: `a6530e02e76058c4fd92e2e115422eaab4a586c5fcc6c647fcd1ee594e7fd362`

Core exploit idea:
- 1. Secondary sales should pay ~10% royalty to creators and the rest to the seller. 2. If getRoyalties lists the seller as a recipient, the market treats the sale as a cr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
