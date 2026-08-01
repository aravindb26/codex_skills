# Crypto Training Exploit Pattern Stub: Bybit Cold-Wallet Heist — `DelegateCall` masterCopy Overwrite of a Gnosis Safe

Source:
- https://crypto.training/hacks/2025-02-Bybit/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$1.46–1.5B — 401,346.77 ETH + 8,000 mETH + 15,000 cmETH + 90,375.55 stETH drained from B…

Tags:
- access-control/secret-exposure, dependency/unsafe-external-call

Dedupe:
- id: `2025-02-Bybit`
- fingerprint: `c4d925fabc2d83bcb1bb0ed651f8c023cde26073c70db618c1f18151494df404`

Core exploit idea:
- This was not an exploit of a flaw in the Gnosis Safe contracts. The Safe behaved exactly as designed. It was a supply-chain / signing-infrastructure compromise: the atta…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
