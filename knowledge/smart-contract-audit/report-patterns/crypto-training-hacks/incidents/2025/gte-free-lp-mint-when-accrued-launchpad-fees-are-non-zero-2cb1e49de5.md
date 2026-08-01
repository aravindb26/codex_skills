# Crypto Training Exploit Pattern Stub: GTE — free LP mint when accrued launchpad fees are non-zero

Source:
- https://crypto.training/hacks/64853-h-05-gtelaunchpadv2pair-permits-minting-lp-tokens-for-free-w/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64853-h-05-gtelaunchpadv2pair-permits-minting-lp-tokens-for-free-w`
- fingerprint: `2cb1e49de5b9c6f8a792d2d50dbc10dc85885aec647035e43ea36691b814d9b5`

Core exploit idea:
- 1. Reserves = balances − fees. 2. mint without transfer sees amount = fees → free LP. 3. Burn cashes out the free share of pool assets. 4. HARM: both tokens stolen with…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
