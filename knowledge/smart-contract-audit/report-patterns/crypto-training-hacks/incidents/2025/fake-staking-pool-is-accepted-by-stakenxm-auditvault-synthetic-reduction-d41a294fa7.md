# Crypto Training Exploit Pattern Stub: Fake staking pool is accepted by stakeNxm — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/64082-h-4-owner-can-steal-funds-from-contract-by-calling-stakenxm/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `64082-h-4-owner-can-steal-funds-from-contract-by-calling-stakenxm`
- fingerprint: `d41a294fa7e200e023a2099dc9bbfc75b5756a5ee33878cd1828acbfde934e4d`

Core exploit idea:
- This bug report discusses a vulnerability found in the stNXM contract, which allows the contract owner to steal funds from the contract. The bug was found by multiple in…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
