# Crypto Training Exploit Pattern Stub: Origin — arbitrary ERC20 can block offer finalization

Source:
- https://crypto.training/hacks/17097-origin-malicious-erc20-finalization-dos/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dependency/unsafe-external-call, dos/frozen-funds, input-validation/missing

Dedupe:
- id: `17097-origin-malicious-erc20-finalization-dos`
- fingerprint: `301739d018846a7108518f4b6ebd474368fe6c3ee9663aeb406cdaa6f440274f`

Core exploit idea:
- Offers store any ERC20 address. A malicious token that always reverts on transfer is called during finalization, permanently blocking settlement without an alternate rev…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
