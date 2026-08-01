# Crypto Training Exploit Pattern Stub: FEG SmartBridge — Wormhole relayer allowlist pollution → forged withdraw

Source:
- https://crypto.training/hacks/2024-12-FEGSmartBridge/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- ~$1M+ multi-chain (ETH ~96 ETH, Base ~73 ETH, BSC ~712 BNB after dump)

Tags:
- bridge/message-spoofing, bridge/missing-validation, access-control/broken-logic

Dedupe:
- id: `2024-12-FEGSmartBridge`
- fingerprint: `3ab0f191623ee3308ec8aceee7e51f1212cc143be39fbc36f7332d50b85dab18`

Core exploit idea:
- FEG’s Wormhole-based SmartBridge only lets the relayer call registerWithdraw. The relayer maintained a sourceAddress allowlist but updated that allowlist from bridge mes…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
