# Crypto Training Exploit Pattern Stub: Tapioca DAO — Magnetar has no approval checking (position drain)

Source:
- https://crypto.training/hacks/27528-h-38-magnetar-contract-has-no-approval-checking-code4rena-ta/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27528-h-38-magnetar-contract-has-no-approval-checking-code4rena-ta`
- fingerprint: `02daac83361caa7afb1fd774f79c3cac8d9b56987b73f3f401a12c8ff2c37399`

Core exploit idea:
- 1. Users approve Magnetar on YieldBox so helpers can manage positions. 2. withdrawToChain(from=victim, receiver=attacker) has no operator check. 3. YieldBox only sees Ma…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
