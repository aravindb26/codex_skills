# Crypto Training Exploit Pattern Stub: Entangle Trillion — dynamic delegatecall lets a compromised master drain Compounder

Source:
- https://crypto.training/hacks/51376-vulnerability-in-compounder-contract-allowing-compromised-eo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dependency/unsafe-external-call, access-control/missing-auth

Dedupe:
- id: `51376-vulnerability-in-compounder-contract-allowing-compromised-eo`
- fingerprint: `4590b4430696eabf5316c7d98bfe5d2bac192a4ac816627448fa838c7666a4e9`

Core exploit idea:
- Compounder.compound accepts a callee and payload from its authorized master then runs the pair with delegatecall. If that master EOA is compromised, it can run arbitrary…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
