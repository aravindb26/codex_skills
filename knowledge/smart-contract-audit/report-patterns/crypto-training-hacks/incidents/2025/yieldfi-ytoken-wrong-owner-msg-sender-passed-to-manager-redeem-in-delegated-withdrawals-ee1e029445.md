# Crypto Training Exploit Pattern Stub: YieldFi YToken: wrong `owner` (`msg.sender`) passed to `Manager.redeem` in delegated withdrawals

Source:
- https://crypto.training/hacks/55538-incorrect-owner-passed-to-managerredeem-in-ytoken-withdrawal/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55538-incorrect-owner-passed-to-managerredeem-in-ytoken-withdrawal`
- fingerprint: `ee1e02944547747d91b803e77817c7f48650020fe3e35111db94c0221e9a9142`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
