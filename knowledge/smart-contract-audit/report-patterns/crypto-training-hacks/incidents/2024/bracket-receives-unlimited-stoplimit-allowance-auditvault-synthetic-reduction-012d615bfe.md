# Crypto Training Exploit Pattern Stub: Bracket receives unlimited StopLimit allowance — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44375-h-5-attacker-can-drain-stoplimit-contract-funds-through-brac/

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
- logic/missing-allowance, dependency/unsafe-external-call

Dedupe:
- id: `44375-h-5-attacker-can-drain-stoplimit-contract-funds-through-brac`
- fingerprint: `012d615bfee43baafe2a3296c07843c509ae00ad6fa28e204effe83d17408126`

Core exploit idea:
- This bug report discusses a vulnerability found in a contract called "StopLimit". The issue was discovered by a group of individuals and can be exploited by an attacker…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
