# Crypto Training Exploit Pattern Stub: Ajna Finance — self-controlled liquidation via `bucketTake` / `take` accounting

Source:
- https://crypto.training/hacks/2026-08-ajnafinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$775K campaign across 7 Ajna ERC20 pools. This PoC is the cbETH/WETH instance: 48.127 cb…

Tags:
- logic/liquidation-logic, oracle/missing-validation, logic/missing-check

Dedupe:
- id: `2026-08-ajnafinance`
- fingerprint: `64936f240639b3ac9361506fb3726b14f78d29183236e1913e43d1bb60b78579`

Core exploit idea:
- Ajna is permissionless and oracle-free by design. Auction and bucket prices come only from the pool's own Fenwick/bucket state. An attacker who controls both sides of a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
