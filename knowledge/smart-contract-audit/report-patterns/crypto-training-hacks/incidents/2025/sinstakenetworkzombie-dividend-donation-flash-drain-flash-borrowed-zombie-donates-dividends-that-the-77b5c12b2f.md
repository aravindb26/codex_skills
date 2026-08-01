# Crypto Training Exploit Pattern Stub: SinstakeNetworkZombie dividend-donation flash-drain — flash-borrowed ZOMBIE donates dividends that the same-tx buyer/seller immediately withdraws, netting excess ZOMBIE convertible to WBNB

Source:
- https://crypto.training/hacks/2025-06-SinstakeZombie/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~705.13 USD (~1.1016 WBNB realized as profit) [output.txt:1564,1565,1784]

Tags:
- logic/incorrect-order-of-operations, defi/fee-manipulation, oracle/spot-price

Dedupe:
- id: `2025-06-SinstakeZombie`
- fingerprint: `77b5c12b2fc6d83c9e85b5b50f4db3b25bb20611dd59d9ea10deeb4774a4ce10`

Core exploit idea:
- SinstakeNetworkZombie is a "dividend yield" contract: users deposit ZOMBIE (the project ERC-20), receive internal dividend-bearing shares (tokenBalanceLedger_), and earn…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
