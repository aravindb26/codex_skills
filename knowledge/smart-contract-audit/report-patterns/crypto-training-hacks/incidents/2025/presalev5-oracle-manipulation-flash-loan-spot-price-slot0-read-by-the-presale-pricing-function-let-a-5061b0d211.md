# Crypto Training Exploit Pattern Stub: PresaleV5 oracle manipulation — flash-loan spot-price (`slot0`) read by the presale pricing function let an attacker buy tokens cheap and sell them at fair price

Source:
- https://crypto.training/hacks/2025-08-PresaleV5/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- 2.3157 ETH (attacker net profit)

Tags:
- oracle/spot-price, oracle/price-manipulation, governance/flash-loan-attack, logic/price-calculation

Dedupe:
- id: `2025-08-PresaleV5`
- fingerprint: `5061b0d211546d19ea3d28cc3592cdb3a78165823a12a61363985a3c9bd52eef`

Core exploit idea:
- PresaleV5 is an ETH/USDT-based token presale ("dynamic sale") whose token price is not a fixed schedule but is derived on-chain from a Uniswap V3 pool. The price functio…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
