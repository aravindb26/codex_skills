# Crypto Training Exploit Pattern Stub: Beta (BETA) Presale — public `set()` + per-sender-only deposit cap let a recycled flash loan drain the presale

Source:
- https://crypto.training/hacks/2025-05-BetaPresale/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- 1.921686798824852706 WBNB + 46.474821659738262175 BUSD (≈ 1,700+ USD at the time)

Tags:
- access-control/missing-auth, logic/incorrect-order-of-operations, defi/fee-manipulation

Dedupe:
- id: `2025-05-BetaPresale`
- fingerprint: `efbf42cf73aeac1d731deb5d14c26ad8bfc64d810fb601fcefbbefd9715e0aa9`

Core exploit idea:
- The Beta token presale contract PresaleBEP20 has two compounding flaws in its deposit() flow. First, anyone can call the public, unguarded set() to overwrite withdrawAdd…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
