# Crypto Training Exploit Pattern Stub: Expired PT redemption has no slippage bound — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62492-h-11-missing-slippage-protection-in-expired-pt-redemption-ca/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- defi/slippage, input-validation/missing

Dedupe:
- id: `62492-h-11-missing-slippage-protection-in-expired-pt-redemption-ca`
- fingerprint: `eb6b263b042ecfea2f7fd5aed17219fe49c0dcb75e91cc7ab6cf430956208b6f`

Core exploit idea:
- This bug report discusses a vulnerability found in the _redeemPT function of the PendlePTLib.sol contract. When PT tokens expire, the function calls redeemExpiredPT whic…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
