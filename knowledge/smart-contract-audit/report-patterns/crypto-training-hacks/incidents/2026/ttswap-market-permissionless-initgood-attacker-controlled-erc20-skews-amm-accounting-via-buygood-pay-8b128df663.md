# Crypto Training Exploit Pattern Stub: TTSwap Market: permissionless `initGood` + attacker-controlled ERC20 skews AMM accounting via `buyGood`/`payGood`

Source:
- https://crypto.training/hacks/2026-04-TTSwapMarket/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- 5.098626217469779632 ETH (exact PoC / on-chain profit after 8 WETH Balancer repay)

Tags:
- logic/incorrect-initialization, logic/missing-check, oracle/price-manipulation

Dedupe:
- id: `2026-04-TTSwapMarket`
- fingerprint: `8b128df66318492b78c31d5e19c957c4e1cdd8d55a1ff46c499198a6caa02a76`

Core exploit idea:
- 1. Attacker CREATE-deploys a factory (nonce 0) that spawns a child exploit and a fake ERC20 good (spoofed transfer/balanceOf). 2. Child flash-loans 8 WETH from Balancer,…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
