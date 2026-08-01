# Crypto Training Exploit Pattern Stub: Liquity V2 scrvUSD branch urgent-redemption arbitrage — permissionless cherry-picking of undercollateralized troves with a 2% bonus

Source:
- https://crypto.training/hacks/2025-07-ActivePoolScrvUsdUrgentRedemption/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$4,204.55 USD (net ETH profit 1.669775970301739864 ETH)

Tags:
- logic/incorrect-state-transition, access-control/missing-auth, defi/flash-loan-attack

Dedupe:
- id: `2025-07-ActivePoolScrvUsdUrgentRedemption`
- fingerprint: `6d9c32f58379fe8f34cd9b1bee427a5adf69cd96855cc96d2f21f7245407f40f`

Core exploit idea:
- Liquity V2 lets a collateral branch be shut down when its total collateral ratio falls below the shutdown collateral ratio (SCR). Once shut down, normal borrowing and re…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
