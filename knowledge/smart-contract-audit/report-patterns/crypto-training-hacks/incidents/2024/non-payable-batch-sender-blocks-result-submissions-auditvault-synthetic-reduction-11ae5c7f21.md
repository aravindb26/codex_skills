# Crypto Training Exploit Pattern Stub: Non-payable batch sender blocks result submissions — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/55233-h-6-attacker-can-exploits-batch-sender-role-to-block-result/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds, dependency/unchecked-return-value

Dedupe:
- id: `55233-h-6-attacker-can-exploits-batch-sender-role-to-block-result`
- fingerprint: `11ae5c7f214d76b8e1ea248c7acc2cd10055e9a8e27cb9d9d89d173a875919a7`

Core exploit idea:
- This bug report discusses an issue with the SEDA protocol that allows an attacker to exploit the batch sender role and block result submissions by using a contract that…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
