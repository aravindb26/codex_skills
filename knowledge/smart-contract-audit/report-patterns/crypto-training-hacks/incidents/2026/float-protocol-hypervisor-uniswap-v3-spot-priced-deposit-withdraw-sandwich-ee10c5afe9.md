# Crypto Training Exploit Pattern Stub: Float Protocol Hypervisor — Uniswap V3 spot-priced deposit/withdraw sandwich

Source:
- https://crypto.training/hacks/2026-08-floatprotocol/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 10.706591043820923462 ETH (~$28K) output.txt

Tags:
- defi/sandwich-attack, oracle/spot-price, oracle/missing-circuit-breaker

Dedupe:
- id: `2026-08-floatprotocol`
- fingerprint: `ee10c5afe92f50a29600046c1cd0302f4f0298439af5dac44fabfa15f0806f6b`

Core exploit idea:
- Float's Hypervisor (Gamma/Visor concentrated-liquidity vault) prices LP shares off getTotalAmounts(), which values the Uni V3 position at the pool's instantaneous slot0…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
