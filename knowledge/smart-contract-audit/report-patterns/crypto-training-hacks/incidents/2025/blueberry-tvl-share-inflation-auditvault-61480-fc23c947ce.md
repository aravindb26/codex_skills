# Crypto Training Exploit Pattern Stub: Blueberry TVL share inflation — AuditVault 61480

Source:
- https://crypto.training/hacks/61480-blueberry-tvl-share-inflation/

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
- logic/price-calculation, defi/sandwich-attack

Dedupe:
- id: `61480-blueberry-tvl-share-inflation`
- fingerprint: `fc23c947ce841cd91c074592b0360e12d15b76546ef2a80609f44ee2d9188dfc`

Core exploit idea:
- TVL excludes in-flight assets, so a deposit mints twice the fair share amount.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
