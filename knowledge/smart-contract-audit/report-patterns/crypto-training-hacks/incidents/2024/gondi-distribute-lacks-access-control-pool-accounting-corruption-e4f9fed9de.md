# Crypto Training Exploit Pattern Stub: Gondi — distribute() lacks access control (Pool accounting corruption)

Source:
- https://crypto.training/hacks/35205-h-03-function-distribute-lacks-access-control-allowing-anyon/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35205-h-03-function-distribute-lacks-access-control-allowing-anyon`
- fingerprint: `e4f9fed9de3e42cfc7d9a226c29568fe9182b7fa35d0d15cd45ed4a079b323d5`

Core exploit idea:
- 1. distribute() is permissionless. 2. Attacker crafts a loan: principalAddress = Junk, sole lender = Pool. 3. Junk is transferred to the Pool; loanLiquidation does total…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
