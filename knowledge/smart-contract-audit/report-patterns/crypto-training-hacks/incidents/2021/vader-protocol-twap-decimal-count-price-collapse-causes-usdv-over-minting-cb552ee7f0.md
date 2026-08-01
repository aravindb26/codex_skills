# Crypto Training Exploit Pattern Stub: Vader Protocol — TWAP decimal-count price collapse causes USDV over-minting

Source:
- https://crypto.training/hacks/42334-h-04-twaporacle-doesnt-calculate-vaderusdv-exchange-rate-cor/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/price-manipulation, arithmetic/decimal-mismatch, logic/price-calculation

Dedupe:
- id: `42334-h-04-twaporacle-doesnt-calculate-vaderusdv-exchange-rate-cor`
- fingerprint: `cb552ee7f06a4ca6b6ed1eb88740e52b2685a4fe8a9b4afdfd2f2fedfe3c413b`

Core exploit idea:
- The oracle receives a ratio and has to express it in the quoted token's smallest units. For an 18-decimal token, that requires multiplying by 10 18. The audited code mul…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
