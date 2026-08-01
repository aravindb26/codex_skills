# Crypto Training Exploit Pattern Stub: NLX — non-refunded excess fee in `_setPricesFromPriceFeeds`

Source:
- https://crypto.training/hacks/50881-non-refunded-excess-fee-in-setpricesfrompricefeed-function/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- fee/missing-refund, oracle/pyth-update

Dedupe:
- id: `50881-non-refunded-excess-fee-in-setpricesfrompricefeed-function`
- fingerprint: `4f155d5996eea405386a778c2a40806418973ac67b71794f19d8efaf22c8d380`

Core exploit idea:
- 1. _setPricesFromPriceFeeds reads updateFee = pyth.getUpdateFee(...) and requires msg.value >= updateFee. 2. It calls pyth.updatePriceFeeds{value: updateFee}(...) — only…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
