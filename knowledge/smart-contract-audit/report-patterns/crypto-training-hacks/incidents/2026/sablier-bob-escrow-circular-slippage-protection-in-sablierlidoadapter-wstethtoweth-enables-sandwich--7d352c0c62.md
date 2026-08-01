# Crypto Training Exploit Pattern Stub: Sablier Bob Escrow — Circular slippage protection in `SablierLidoAdapter::_wstETHToWeth` enables sandwich attacks

Source:
- https://crypto.training/hacks/65583-circular-slippage-protection-in-sablierlidoadapter-wstethtow/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/spot-price

Dedupe:
- id: `65583-circular-slippage-protection-in-sablierlidoadapter-wstethtow`
- fingerprint: `7d352c0c62e9c5ebc9f223471fe039aadea8bb4232ec767217c2f9db580f1812`

Core exploit idea:
- 1. _wstETHToWeth sets minEthOut from Curve get_dy (current reserves). 2. exchange reads the same reserves — so a sandwich that depresses the pool makes both quote and sw…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
