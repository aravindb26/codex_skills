# Crypto Training Exploit Pattern Stub: ether.fi Liquid / Veda AtomicQueue — Unauthenticated `solver` Drain

Source:
- https://crypto.training/hacks/2026-09-etherfivedaatomicqueue/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 14.445541086626480232 liquidETH + 7.047848 USDC in the PoC (14445541086626480232 wei + 70…

Tags:
- access-control/missing-auth, logic/missing-validation, dependency/unsafe-external-call

Dedupe:
- id: `2026-09-etherfivedaatomicqueue`
- fingerprint: `54ec94ef2b6a897f1c168918356118a5a7565aa867c1e90c94adbf396a5c1647`

Core exploit idea:
- 1. ether.fi Liquid withdrawals on Ethereum share a Veda AtomicQueue (AtomicQueue.sol). Users who want to sell liquidETH (or other vault shares) for a want asset approve…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
