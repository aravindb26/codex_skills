# Crypto Training Exploit Pattern Stub: Statusl — global MP cap broken on unstake causes permanent DoS

Source:
- https://crypto.training/hacks/65329-global-mp-cap-invariant-can-be-broken-on-unstake-causing-ari/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65329-global-mp-cap-invariant-can-be-broken-on-unstake-causing-ari`
- fingerprint: `e5880c77e32a2e2a236eef1ede2a4fda92d5a3f87060b7a6b089a992c1911b7b`

Core exploit idea:
- 1. Protocol assumes totalMPAccrued totalMaxMP.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
