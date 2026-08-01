# Crypto Training Exploit Pattern Stub: USDT claim underflows when contract has a larger balance — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44006-h-02-the-usdt-reward-claiming-functionality-of-vestedstaking/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, dos/frozen-funds

Dedupe:
- id: `44006-h-02-the-usdt-reward-claiming-functionality-of-vestedstaking`
- fingerprint: `d38491119d44743e9efd7f7a03fe60665749f106cc8090b33e70fdf51a41e66c`

Core exploit idea:
- This bug report describes a high-risk issue in the claimRewards function of the VestedStaking.sol contract. The issue affects the calculation of USDT rewards and can be…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
