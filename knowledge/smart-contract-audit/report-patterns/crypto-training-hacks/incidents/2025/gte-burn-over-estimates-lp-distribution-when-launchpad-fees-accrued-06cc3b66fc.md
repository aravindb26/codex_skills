# Crypto Training Exploit Pattern Stub: GTE — burn over-estimates LP distribution when launchpad fees accrued

Source:
- https://crypto.training/hacks/64851-h-03-gtelaunchpadv2pairburn-over-estimates-distribution-amou/

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
- id: `64851-h-03-gtelaunchpadv2pairburn-over-estimates-distribution-amou`
- fingerprint: `06cc3b66fc727c3bf6037fd85492e76a984644dbc019fc46c32661920b21f1c3`

Core exploit idea:
- 1. Accrued launchpad fees sit in pair balances but are excluded from reserves. 2. mint prices LP against reserves; burn pays out against full balances. 3. Mint + burn ca…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
