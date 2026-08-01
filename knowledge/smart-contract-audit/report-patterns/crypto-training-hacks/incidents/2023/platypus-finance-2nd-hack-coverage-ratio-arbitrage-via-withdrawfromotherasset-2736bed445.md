# Crypto Training Exploit Pattern Stub: Platypus Finance (2nd hack) — Coverage-Ratio Arbitrage via `withdrawFromOtherAsset`

Source:
- https://crypto.training/hacks/2023-07-Platypus02/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Avalanche

Loss / impact summary:
- ~$51K (one of several attack txs); this PoC profits 4,472.378061 USDC in a single flash-l…

Tags:
- logic/incorrect-state-transition, arithmetic/precision-loss

Dedupe:
- id: `2023-07-Platypus02`
- fingerprint: `2736bed44535c2180d619889564c10c7b224e1112d35a96637d9cbbec16f6997`

Core exploit idea:
- Platypus is a single-sided stableswap. Each token has an Asset LP contract that tracks two numbers: cash (underlying token actually held) and liability (what depositors…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
