# Crypto Training Exploit Pattern Stub: Reward claim reentrancy pays twice — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/35121-h-8-malicious-users-can-steal-reward-tokens-via-re-entrancy/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/single-function, logic/state-update

Dedupe:
- id: `35121-h-8-malicious-users-can-steal-reward-tokens-via-re-entrancy`
- fingerprint: `3c43ab18ed22951a8b8bdb9e5149d0c8b68553e0cad64ad85fde880536033dd2`

Core exploit idea:
- This bug report discusses a vulnerability in which malicious users can steal reward tokens through a re-entrancy attack. The vulnerability is caused by a function that u…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
