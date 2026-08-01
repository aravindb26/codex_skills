# Crypto Training Exploit Pattern Stub: TokenVault (Gangster Finance) — same-tx donate+deposit inflates fresh shares against the drip pool

Source:
- https://crypto.training/hacks/2025-06-TokenVault/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~3,226.51 USD (4.9836 WBNB) — attacker before 1.4702 WBNB, after 6.4538 WBNB

Tags:
- logic/incorrect-order-of-operations, defi/flash-loan-attack, logic/state-update

Dedupe:
- id: `2025-06-TokenVault`
- fingerprint: `2accb739e5c1c04e128a2195a8b96c71b2e09a7c7ec0292f712e561655626dba`

Core exploit idea:
- TokenVault is a staking/"vault" contract from Gangster Finance (an early BSC dividend-yield project). Holders stake a BEP20 token and earn a share of a "drip pool" that…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
