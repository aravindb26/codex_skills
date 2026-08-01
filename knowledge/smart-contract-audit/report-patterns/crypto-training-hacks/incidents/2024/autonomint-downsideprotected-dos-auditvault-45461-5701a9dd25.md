# Crypto Training Exploit Pattern Stub: Autonomint downsideProtected DoS — AuditVault 45461

Source:
- https://crypto.training/hacks/45461-autonomint-downside-dos/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, dos/frozen-funds

Dedupe:
- id: `45461-autonomint-downside-dos`
- fingerprint: `5701a9dd25d701f042bcf7fd07ed3f6d4c337681df70b1df07a2550aa2a3f656`

Core exploit idea:
- An attacker can set downsideProtected so settlement underflows and the protocol is permanently unavailable.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
