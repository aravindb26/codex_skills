# Crypto Training Exploit Pattern Stub: CAP Labs PriceOracle — global staleness period rejects valid feeds

Source:
- https://crypto.training/hacks/61525-incorrect-oracle-staleness-period-price-feed-dos/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/stale-price, oracle/missing-validation, dos/frozen-funds

Dedupe:
- id: `61525-incorrect-oracle-staleness-period-price-feed-dos`
- fingerprint: `b91d4b282871a31d3ae5e7aa725776d760792acad09bbd52c00a86d016b0e338`

Core exploit idea:
- CAP's oracle stores one staleness period for all assets. Configuring one hour for hourly ETH feeds makes a valid daily USDC-like report revert after five thousand second…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
