# Crypto Training Exploit Pattern Stub: Index Fun — Seller pays the buyer's trade fee in token swaps

Source:
- https://crypto.training/hacks/63700-index-fun-seller-pays-the-buyer-s-trade-fee-in-token-swaps/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation, logic/incorrect-order-of-operations

Dedupe:
- id: `63700-index-fun-seller-pays-the-buyer-s-trade-fee-in-token-swaps`
- fingerprint: `05937e7c545822f84ff470d798af5bd5866f4f87ec3bc35d6a83d11940e2a339`

Core exploit idea:
- Settlement deducts the buyer fee from the seller's proceeds instead of charging the buyer, systematically transferring value from sellers.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
