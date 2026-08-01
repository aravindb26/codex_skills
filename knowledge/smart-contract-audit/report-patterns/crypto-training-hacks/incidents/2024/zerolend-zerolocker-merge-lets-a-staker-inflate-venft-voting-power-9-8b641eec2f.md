# Crypto Training Exploit Pattern Stub: ZeroLend — `ZeroLocker.merge()` lets a staker inflate veNFT voting power ~9×

Source:
- https://crypto.training/hacks/40818-a-malicious-user-can-inflate-his-voting-power-via-merge-cant/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- governance/proposal-manipulation, logic/missing-check, logic/timestamp-dependence

Dedupe:
- id: `40818-a-malicious-user-can-inflate-his-voting-power-via-merge-cant`
- fingerprint: `8b641eec2fe19c1be1f5b02843ad7082f955f9fce38ea707751f3ca7fc68b99f`

Core exploit idea:
- 1. ZeroLocker is a Solidly/Curve-style voting-escrow veNFT: locking ZERO mints an NFT whose voting power (balanceOfNFT) decays linearly over the lock. 2. To stop flash-v…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
