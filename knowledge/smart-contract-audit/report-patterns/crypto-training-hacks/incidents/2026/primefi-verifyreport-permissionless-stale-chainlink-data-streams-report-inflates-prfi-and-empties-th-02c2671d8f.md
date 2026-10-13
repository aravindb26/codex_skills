# Crypto Training Exploit Pattern Stub: PrimeFi `verifyReport` — permissionless stale Chainlink Data Streams report inflates PRFI and empties the WHYPE reserve

Source:
- https://crypto.training/hacks/2026-09-primefinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- HyperEVM

Loss / impact summary:
- 425.521620381705945356 WHYPE borrowed out of the lending reserve (aWHYPE balance after th…

Tags:
- oracle/stale-price, access-control/missing-auth, defi/undercollateralized-borrow, auth/signature-replay

Dedupe:
- id: `2026-09-primefinance`
- fingerprint: `02c2671d8fed27216f1d88c078b68d08cf8ebf5cb6e339c897610b99a37e4261`

Core exploit idea:
- PrimeFi's HyperEVM market prices PRFI through DataStreamConsumer, a Chainlink Data Streams middleware. Anyone may call verifyReport. The function does not skip the signa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
