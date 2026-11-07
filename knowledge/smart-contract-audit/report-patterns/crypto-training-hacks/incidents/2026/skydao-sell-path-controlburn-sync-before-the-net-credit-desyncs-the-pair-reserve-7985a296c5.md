# Crypto Training Exploit Pattern Stub: SKYDAO sell path — controlburn + sync() before the net credit desyncs the pair reserve

Source:
- https://crypto.training/hacks/2026-09-skydao/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- 183,482.883991401873856911 USDT leaves the SKYDAO/USDT pair output.txt:256. One wei of US…

Tags:
- logic/incorrect-order-of-operations, logic/state-update, defi/price-manipulation

Dedupe:
- id: `2026-09-skydao`
- fingerprint: `7985a296c53fe36353841cdc0d8ef47b8e7438c980b472732d79fd9c2b2c7771`

Core exploit idea:
- SKYDAO is a fee-on-transfer token (35% tax) paired with USDT on PancakeSwap V2. A sell (to == pair) does not just take a tax. It calls the unverified pool controller's s…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
