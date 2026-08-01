# Crypto Training Exploit Pattern Stub: Ocean Protocol BPool / SideStaking gulp drain — pool internal records desynced from real token balance, harvestable via single-sided joins + exits

Source:
- https://crypto.training/hacks/2026-06-OceanBPoolSideStaking/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Polygon

Loss / impact summary:
- ~127,861 mOCEAN (minter-share / vesting token; attacker ends with 127,861.011180850512933…

Tags:
- logic/state-update, defi/fee-manipulation, oracle/price-manipulation

Dedupe:
- id: `2026-06-OceanBPoolSideStaking`
- fingerprint: `5da8a33246c95c7b5b3c10f2bf1e6f145aae6a6763f5abbfb548ffdfd50f7f97`

Core exploit idea:
- Ocean Protocol runs a fork of Balancer's BPool (contracts/pools/balancer/BPool.sol) wired to a SideStaking helper (contracts/pools/ssContracts/SideStaking.sol). Each poo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
