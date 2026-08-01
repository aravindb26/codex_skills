# Crypto Training Exploit Pattern Stub: MCAI tax-wallet allowance bypass — privileged `transferFrom` drains the Uniswap V2 pair

Source:
- https://crypto.training/hacks/2025-01-MCAI/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Ethereum

Loss / impact summary:
- ~12.03 WETH / ETH (12.028506355387210510 ETH extracted by the attacker EOA)

Tags:
- access-control/missing-auth, access-control/centralization, logic/wrong-condition

Dedupe:
- id: `2025-01-MCAI`
- fingerprint: `00006e913cbb1c5c171558efe9746406000f375e9dad03f16ba1f43d7bf7dcad`

Core exploit idea:
- Memecast AI (MCAI) is a generic fee-on-transfer meme token with a Uniswap V2 MCAI/WETH pool. Its ERC-20 transferFrom does not enforce the spender allowance in the normal…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
