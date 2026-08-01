# Crypto Training Exploit Pattern Stub: Hiding a staked NFT inflates share ownership — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/64083-h-5-owner-can-hide-a-staked-nft-via-removetokenidatindex-and/

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
- logic/price-calculation, access-control/missing-owner-check

Dedupe:
- id: `64083-h-5-owner-can-hide-a-staked-nft-via-removetokenidatindex-and`
- fingerprint: `5bc8fd738ba51d4be7202992808bb5d9c8a4f05c860285c8180926690707bfc7`

Core exploit idea:
- Summary: The bug report describes a vulnerability in the stNXM smart contract that allows the owner to manipulate the value of the staked Nexus NFT without withdrawing i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
