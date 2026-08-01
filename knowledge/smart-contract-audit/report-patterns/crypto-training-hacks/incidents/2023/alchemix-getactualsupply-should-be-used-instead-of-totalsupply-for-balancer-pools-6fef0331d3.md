# Crypto Training Exploit Pattern Stub: Alchemix — `getActualSupply` should be used instead of `totalSupply` for Balancer pools

Source:
- https://crypto.training/hacks/38187-getactualsupply-should-be-used-instead-of-totalsupply-for-ba/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `38187-getactualsupply-should-be-used-instead-of-totalsupply-for-ba`
- fingerprint: `6fef0331d31a0ee0ee439b0b38a5a6e2c97da44320311049973d3af584aa40b0`

Core exploit idea:
- 1. _depositIntoBalancerPool computes the join's bptAmountOut (the minimum-output / slippage-protection floor) from IERC20(balancerPool).totalSupply(). 2. Real Balancer p…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
