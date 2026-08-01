# Crypto Training Exploit Pattern Stub: Owner burns liquidity from an arbitrary NFT position — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/64081-h-3-owner-can-steal-funds-on-withdraw-by-burning-wrong-unisw/

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
- access-control/missing-owner-check, logic/state-update

Dedupe:
- id: `64081-h-3-owner-can-steal-funds-on-withdraw-by-burning-wrong-unisw`
- fingerprint: `58e6294e56b5ae82276b92fd7587da895b9a1213de5ccc03f837ac5bb8077d30`

Core exploit idea:
- This bug report discusses an issue found in the stNXM contract, where the owner is able to steal funds from the vault and the protocol is unable to recover them. The bug…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
