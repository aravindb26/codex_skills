# Crypto Training Exploit Pattern Stub: Folks Finance mixes stable and variable debt — AuditVault 61091

Source:
- https://crypto.training/hacks/61091-folks-liquidation-mixing/

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
- logic/liquidation-logic, logic/incorrect-state-transition

Dedupe:
- id: `61091-folks-liquidation-mixing`
- fingerprint: `7dd041a3416ec51d237bd97e54562e18b28a8f027a3ccefa845df5a53a231632`

Core exploit idea:
- Liquidation merges stable debt into the variable bucket, changing the borrower’s debt semantics.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
