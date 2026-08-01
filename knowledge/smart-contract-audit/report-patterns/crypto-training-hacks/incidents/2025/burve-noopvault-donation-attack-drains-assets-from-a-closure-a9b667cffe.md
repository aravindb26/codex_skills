# Crypto Training Exploit Pattern Stub: Burve — NoopVault donation attack drains assets from a closure

Source:
- https://crypto.training/hacks/56956-burve-noopvault-donation-attack-drains-assets-from-a-closure/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/price-manipulation, logic/price-calculation

Dedupe:
- id: `56956-burve-noopvault-donation-attack-drains-assets-from-a-closure`
- fingerprint: `a9b667cffeb43310a0a977dfce96bee2c90499d7049c7787751b799bf677fa6d`

Core exploit idea:
- A donation changes the vault's asset balance without increasing shares; the stale share price then lets the attacker withdraw the donated assets.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
