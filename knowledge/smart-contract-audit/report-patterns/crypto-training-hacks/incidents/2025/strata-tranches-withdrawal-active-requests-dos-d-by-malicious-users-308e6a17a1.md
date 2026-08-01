# Crypto Training Exploit Pattern Stub: Strata Tranches — withdrawal active requests DoS'd by malicious users

Source:
- https://crypto.training/hacks/63223-users-can-get-their-withdrawal-active-requests-dosed-by-mali/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63223-users-can-get-their-withdrawal-active-requests-dosed-by-mali`
- fingerprint: `308e6a17a1d58fe54fe1b5bfcaef02473ed0f9b9a30d5a562a48f9f6433b654f`

Core exploit idea:
- Anyone can call transfer(..., victim, 1 wei) and inflate the victim's request array. finalize iterates all entries → OOG after ~35k spam (shown via sample×extrapolate).

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
