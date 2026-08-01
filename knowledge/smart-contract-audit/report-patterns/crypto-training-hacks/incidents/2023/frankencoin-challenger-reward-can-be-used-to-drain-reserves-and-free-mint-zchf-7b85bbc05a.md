# Crypto Training Exploit Pattern Stub: Frankencoin — CHALLENGER_REWARD can be used to drain reserves and free-mint ZCHF

Source:
- https://crypto.training/hacks/20021-h-06-challenger-reward-can-be-used-to-drain-reserves-and-fre/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, access-control/unbounded-parameter, loss-of-funds/direct-drain

Dedupe:
- id: `20021-h-06-challenger-reward-can-be-used-to-drain-reserves-and-fre`
- fingerprint: `7b85bbc05a6edb653ce1119bcf898fd3458b44d28723122e04da5748d24a6776`

Core exploit idea:
- 1. Position records a liquidation price that the owner sets — at open time via _liqPrice, or later via adjustPrice. There is no upper bound. 2. When a challenge ends, Mi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
