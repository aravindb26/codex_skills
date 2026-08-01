# Crypto Training Exploit Pattern Stub: LEND — CoreRouter redemption payout is miscalculated

Source:
- https://crypto.training/hacks/58376-lend-corerouter-redemption-payout-is-miscalculated/

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
- logic/price-calculation, arithmetic/precision-loss

Dedupe:
- id: `58376-lend-corerouter-redemption-payout-is-miscalculated`
- fingerprint: `02a2c844fea1d1a30c5a36d5c190ccf0bce22a0450cb31c574d591921ea998df`

Core exploit idea:
- redeem() computes the payout from the wrong exchange-rate side, paying more assets than the shares burned and depleting reserves.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
