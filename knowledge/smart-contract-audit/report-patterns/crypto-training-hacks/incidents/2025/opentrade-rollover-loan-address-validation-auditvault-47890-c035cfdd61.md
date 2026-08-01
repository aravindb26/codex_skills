# Crypto Training Exploit Pattern Stub: OpenTrade rollover loan-address validation — AuditVault 47890

Source:
- https://crypto.training/hacks/47890-opentrade-loan-validation/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, access-control/missing-auth

Dedupe:
- id: `47890-opentrade-loan-validation`
- fingerprint: `c035cfdd615662fa1642625bb5496af5c52dc5abb237da554feebbbe55d8b622`

Core exploit idea:
- The rollover entry point accepts an arbitrary loan address instead of validating pool ownership.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
