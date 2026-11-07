# Crypto Training Exploit Pattern Stub: EtherVista — swap's constant-product (K) check multiplies two uint112 reserves, so the invariant overflows and the pool drains

Source:
- https://crypto.training/hacks/2026-10-ethervista/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- arithmetic/integer-overflow, defi/invariant-bypass, access-control/privileged-role-takeover

Dedupe:
- id: `2026-10-ethervista`
- fingerprint: `96aa94ee7b2caef3b03ca26bed38bb9e53eb48b6cc6b40532f7cf122a5e9de93`

Core exploit idea:
- EtherVista is a Uniswap-V2-style AMM (token0 = WETH, token1 = VISTA). Its swap ends with the stock-looking constant-product check require(balance0 balance1 >= reserve0 r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
