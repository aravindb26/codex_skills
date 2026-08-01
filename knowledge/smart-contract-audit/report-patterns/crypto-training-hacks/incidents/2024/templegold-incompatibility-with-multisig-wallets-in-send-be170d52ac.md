# Crypto Training Exploit Pattern Stub: TempleGold — incompatibility with multisig wallets in `send()`

Source:
- https://crypto.training/hacks/35290-incompatibility-with-multisig-wallets-in-templegoldsend-func/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/cross-chain-address-assumption, dos/permanent-revert, bridge/liveness

Dedupe:
- id: `35290-incompatibility-with-multisig-wallets-in-templegoldsend-func`
- fingerprint: `be170d52accef7c3f30ec0b047bcdfc16d360a6726aa3766b49c993dc14773ef`

Core exploit idea:
- 1. TempleGold.send(_sendParam, _fee, _refundAddress) is the entry point users call to bridge TEMPLE from one chain to another via LayerZero. 2. Before doing anything els…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
