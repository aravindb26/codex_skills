# Crypto Training Exploit Pattern Stub: Summer.fi FleetCommander — NAV Inflation via Empty-Ark Donation of Undervalued vgUSDC

Source:
- https://crypto.training/hacks/2026-07-SummerFi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- ~5.60M DAI reproduced on FleetA (5597682112787981084159961 wei); full incident ~6.02M inc…

Tags:
- defi/donation-attack, oracle/price-manipulation, defi/flash-loan-attack

Dedupe:
- id: `2026-07-SummerFi`
- fingerprint: `c1f3ad36c75fc61e26f301fa11e3f52048bbc8ea757615f967484b817aa7d530`

Core exploit idea:
- 1. Summer.fi Lazy Summer FleetCommander prices shares from the sum of each ark's totalAssets() with no smoothing, donation resistance, or empty-ark gate.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
