# Crypto Training Exploit Pattern Stub: Frankencoin — Transfer position ownership to address(0) DoSes end()

Source:
- https://crypto.training/hacks/20019-h-04-transfer-position-ownership-to-addr0-to-dos-end-challen/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `20019-h-04-transfer-position-ownership-to-addr0-to-dos-end-challen`
- fingerprint: `edd86d4b4ac8f19a88f23fa760a3078628bd1dd6e1b8bcc9aebce557f7170e19`

Core exploit idea:
- 1. Owner about to lose a challenge calls transferOwnership(address(0)). 2. Winning bid creates an excess refund path in end(). 3. zchf.transfer(owner, excess) reverts be…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
