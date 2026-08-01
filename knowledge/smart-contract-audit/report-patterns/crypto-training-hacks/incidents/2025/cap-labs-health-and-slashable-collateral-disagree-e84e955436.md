# Crypto Training Exploit Pattern Stub: CAP Labs — health and slashable collateral disagree

Source:
- https://crypto.training/hacks/61537-health-vs-slashable-collateral/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, logic/state-update, dos/frozen-funds

Dedupe:
- id: `61537-health-vs-slashable-collateral`
- fingerprint: `e84e955436f1cb0600c0cd5c4383003ace0b4563ce0b8c222316d8b18fc55c86`

Core exploit idea:
- coverage includes current collateral while slashTimestamp limits slashing to the previous epoch. A fresh rescue deposit improves health but cannot be slashed in liquidat…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
