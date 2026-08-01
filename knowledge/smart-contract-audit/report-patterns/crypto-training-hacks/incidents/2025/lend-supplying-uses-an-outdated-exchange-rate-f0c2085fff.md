# Crypto Training Exploit Pattern Stub: LEND — Supplying uses an outdated exchange rate

Source:
- https://crypto.training/hacks/58378-lend-supplying-uses-an-outdated-exchange-rate/

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
- oracle/stale-price, logic/price-calculation

Dedupe:
- id: `58378-lend-supplying-uses-an-outdated-exchange-rate`
- fingerprint: `f0c2085fff25ba8f67c4b34ec05438f63d66c8c466bd1f84992bd756a1f53734`

Core exploit idea:
- Supply mints L-tokens with a cached exchange rate even after the market rate changes, creating unbacked accounting units.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
