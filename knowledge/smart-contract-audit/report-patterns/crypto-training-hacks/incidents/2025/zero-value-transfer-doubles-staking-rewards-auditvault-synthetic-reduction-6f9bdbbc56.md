# Crypto Training Exploit Pattern Stub: Zero-value transfer doubles staking rewards — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44004-c-01-malicious-users-can-steal-all-staking-rewards-from-stak/

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
- logic/reward-calculation, logic/state-update

Dedupe:
- id: `44004-c-01-malicious-users-can-steal-all-staking-rewards-from-stak`
- fingerprint: `6f9bdbbc568e09871fac502f07cc8bc0bc06076687a094e3162608589a5f71c4`

Core exploit idea:
- The report details a critical bug in the _claimToCredit() function of the StakedCSX.sol contract. This function has a logical error where the addition assignment operato…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
