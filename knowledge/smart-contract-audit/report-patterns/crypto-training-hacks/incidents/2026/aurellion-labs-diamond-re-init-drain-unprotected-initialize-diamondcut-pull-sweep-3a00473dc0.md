# Crypto Training Exploit Pattern Stub: Aurellion Labs Diamond Re-Init Drain — Unprotected `initialize` → `diamondCut` pull/sweep

Source:
- https://crypto.training/hacks/2026-05-AurellionLabs/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- Arbitrum

Loss / impact summary:
- 456,442.536622 USDC (~$456K) to attacker EOA

Tags:
- access-control/uninitialized-proxy, access-control/missing-auth, dependency/upgradeable-contract, access-control/missing-owner-check

Dedupe:
- id: `2026-05-AurellionLabs`
- fingerprint: `3a00473dc0daba338c3eedd3988c36f53f0cfc6ce871b14a264e526489306488`

Core exploit idea:
- 1. Users had granted unlimited USDC allowances to the Aurellion diamond 0x0adc…. That alone is normal; the bug is that the diamond’s ownership / init surface remained op…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
