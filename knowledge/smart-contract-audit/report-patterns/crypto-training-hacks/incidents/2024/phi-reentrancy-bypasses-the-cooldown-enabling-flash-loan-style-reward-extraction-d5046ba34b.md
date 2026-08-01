# Crypto Training Exploit Pattern Stub: Phi — reentrancy bypasses the cooldown, enabling flash-loan-style reward extraction

Source:
- https://crypto.training/hacks/41092-h-06-reentrancy-vulnerability-allows-bypass-of-cooldown-lead/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/single-function, access-control/stale-state-read, economic/flash-loan-reward-extraction

Dedupe:
- id: `41092-h-06-reentrancy-vulnerability-allows-bypass-of-cooldown-lead`
- fingerprint: `d5046ba34b1e6a1d0e32ea3e852bfb6ab33aaacbe8550b99d6a121f3ba0ba2e9`

Core exploit idea:
- 1. Cred.buyShareCred refunds any excess ETH payment via a raw call to msg.sender — and only after that call returns does it arm lastTradeTimestamp, the state a 10-minute…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
