# Crypto Training Exploit Pattern Stub: Zaros — draining the protocol fully

Source:
- https://crypto.training/hacks/38003-draining-the-protocol-fully-codehawks-zaros-git/

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
- economic-design/self-referential-margin, oracle-manipulation/self-inflicted-price-impact, loss-of-funds/direct-drain

Dedupe:
- id: `38003-draining-the-protocol-fully-codehawks-zaros-git`
- fingerprint: `5e2a1e91012017a12f529c25661b26dcfd475d48da9b5f822b8dc7c5d63fd3f5`

Core exploit idea:
- 1. Opening a new order moves the market's skew, which moves the mark price (price impact) — a real feature (skew-based pricing). 2. The margin check for that SAME new or…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
