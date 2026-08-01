# Crypto Training Exploit Pattern Stub: Entangle Trillion — missing Stargate allowance blocks LP deposits

Source:
- https://crypto.training/hacks/51370-broken-stargate-deposit-flow-due-to-missing-allowance-halbor/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-allowance, dependency/unsafe-external-call, dos/frozen-funds

Dedupe:
- id: `51370-broken-stargate-deposit-flow-due-to-missing-allowance-halbor`
- fingerprint: `3d03563ab5c22e8177474ab52d0cd057800b119163b1547ae201ac65b476eb94`

Core exploit idea:
- StargateSynthChef deposits LP by asking the Stargate staking contract to pull tokens from the chef, but it never approves that spender. Every fresh deposit fails at tran…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
