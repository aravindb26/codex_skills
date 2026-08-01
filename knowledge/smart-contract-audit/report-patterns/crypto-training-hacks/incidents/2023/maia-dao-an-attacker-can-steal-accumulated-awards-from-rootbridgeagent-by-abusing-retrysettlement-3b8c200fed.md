# Crypto Training Exploit Pattern Stub: Maia DAO — An attacker can steal Accumulated Awards from RootBridgeAgent by abusing retrySettlement()

Source:
- https://crypto.training/hacks/26045-h-11-an-attacker-can-steal-accumulated-awards-from-rootbridg/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/gas-double-spend, loss-of-funds/reward-drain, dos/frozen-funds

Dedupe:
- id: `26045-h-11-an-attacker-can-steal-accumulated-awards-from-rootbridg`
- fingerprint: `3b8c200fed48958347623e74f1159caf37d541696a34a21e0550d7ac7c4b191a`

Core exploit idea:
- 1. Inside a single anyExecute (initialGas > 0), userFeeInfo.gasToBridgeOut is set once from the user's single branch-chain gas payment. 2. Each _retrySettlement calls _m…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
