# Crypto Training Exploit Pattern Stub: OracleLess executes attacker-controlled target — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44372-h-2-attackers-can-drain-the-oracleless-contract-by-creating/

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
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `44372-h-2-attackers-can-drain-the-oracleless-contract-by-creating`
- fingerprint: `fd2d42260e8316f72bb3ad6260021b256a96679cd05436a7c03051844032d9b3`

Core exploit idea:
- The OracleLess contract has a vulnerability that allows attackers to drain all USDT from the contract. This is caused by the createOrder() function not verifying if the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
