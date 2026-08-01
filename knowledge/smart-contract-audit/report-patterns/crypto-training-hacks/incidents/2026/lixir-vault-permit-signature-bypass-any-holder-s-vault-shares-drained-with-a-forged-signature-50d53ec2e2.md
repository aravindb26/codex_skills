# Crypto Training Exploit Pattern Stub: Lixir vault `permit` signature bypass — any holder's vault shares drained with a forged signature

Source:
- https://crypto.training/hacks/2026-06-LixirPermitDrain/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Ethereum

Loss / impact summary:
- 2.60 ETH, 4,477.72 USDC, 3,609.95 USDT, 24,182.56 LIX (≈ $33k at the time)

Tags:
- auth/signature-validation, logic/missing-check

Dedupe:
- id: `2026-06-LixirPermitDrain`
- fingerprint: `50d53ec2e2a64a8a604ade7c5fbeca2cafbd10af2b4687983db75922318bd400`

Core exploit idea:
- Lixir is a Uniswap-v3 active-liquidity manager. Users deposit into a per-pair vault (an ERC-20 "Lixir vault token", lv_X-Y A/B) and the vault parks the liquidity inside…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
