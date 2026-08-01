# Crypto Training Exploit Pattern Stub: Moonwell cbETH Oracle Incident — Mispriced Collateral Enables Near-Free Liquidation

Source:
- https://crypto.training/hacks/2026-02-Moonwell/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2026

Chain:
- Base

Loss / impact summary:
- ~$1.78M protocol-wide bad debt (cbETH $1.03M, WETH $479K, USDC $233K, EURC, cbBTC, cbXRP,…

Tags:
- oracle/stale-price, oracle/missing-validation

Dedupe:
- id: `2026-02-Moonwell`
- fingerprint: `62eeb6d1af57c8790567ea769382b7c09088a588b8485202c650239f6c95c6ee`

Core exploit idea:
- Moonwell (a Compound-v2 fork on Base) values collateral and debt for liquidations through its ChainlinkOracle. For cbETH that oracle reads a ChainlinkOEVWrapper, which i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
