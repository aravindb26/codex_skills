# Crypto Training Exploit Pattern Stub: AXION buyback liquidity burn — AuditVault 43530

Source:
- https://crypto.training/hacks/43530-axion-buyback-liquidity/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/spot-price, logic/price-calculation

Dedupe:
- id: `43530-axion-buyback-liquidity`
- fingerprint: `3a9e2455cc538bb7a66e29c78202831a35bcdae69bb24024d4899d566a7d22a6`

Core exploit idea:
- The V3AMO buyback uses a spot-derived amount and burns ten times the requested liquidity.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
