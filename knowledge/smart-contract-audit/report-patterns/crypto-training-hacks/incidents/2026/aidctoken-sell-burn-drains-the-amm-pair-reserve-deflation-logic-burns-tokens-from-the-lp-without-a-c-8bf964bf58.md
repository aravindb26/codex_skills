# Crypto Training Exploit Pattern Stub: AIDCToken sell-burn drains the AMM pair reserve — deflation logic burns tokens from the LP without a counterpart

Source:
- https://crypto.training/hacks/2026-06-AIDC/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~220.13 WBNB (≈ $132k at BNB ≈ $600)

Tags:
- logic/incorrect-order-of-operations, oracle/price-manipulation, logic/state-update, defi/fee-manipulation

Dedupe:
- id: `2026-06-AIDC`
- fingerprint: `8bf964bf58873d5fb6004a8d145fa1c30f7be7ce9357136680f82b7b3c5c1383`

Core exploit idea:
- AIDC is an ERC-20 ("AI Data Credit") with a custom AMM tax. On every non-whitelisted sell into the PancakeSwap V2 AIDC/WBNB pair, _sellTransfer does not actually burn an…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
