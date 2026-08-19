# Crypto Training Exploit Pattern Stub: Remora Pledge: `changeStablecoin` swaps the payment token's decimals without rescaling raw-unit accounting

Source:
- https://crypto.training/hacks/61176-accounting-on-paymentsettler-will-be-corrupted-when-changi/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61176-accounting-on-paymentsettler-will-be-corrupted-when-changi`
- fingerprint: `d3a263a4181bfe763c58e24cd2dbc561e279213a097b3107d47d20b53f4c9386`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
