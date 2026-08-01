# Crypto Training Exploit Pattern Stub: DayContract / Polarx — Spot Manip + Rigid Principal Guarantee

Source:
- https://crypto.training/hacks/2026-03-DayContract/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$10.6K attacker profit; ~$29.7K protocol insolvency

Tags:
- oracle/price-manipulation, logic/missing-check

Dedupe:
- id: `2026-03-DayContract`
- fingerprint: `aede2860291c89f4d548111affdea647d1e244fc8c4de96ad027eb4ef32ad9aa`

Core exploit idea:
- DayContract.deposit converts USDT → LP via Pancake spot reserves (no TWAP). withdraw always calls vault.settlePrincipal(user, fullPrincipal, 0), and the vault’s _ensureU…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
