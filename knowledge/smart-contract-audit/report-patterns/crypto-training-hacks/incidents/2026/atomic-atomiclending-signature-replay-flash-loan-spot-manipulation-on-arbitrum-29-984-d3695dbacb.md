# Crypto Training Exploit Pattern Stub: Atomic (AtomicLending) — Signature Replay + Flash-Loan Spot Manipulation on Arbitrum (~$29,984)

Source:
- https://crypto.training/hacks/2026-08-atomicatomiclendingoraclemanipulation/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Arbitrum

Loss / impact summary:
- ~$29,984.27 USDC (native USDC on Arbitrum)

Tags:
- auth/signature-replay, oracle/spot-price, oracle/price-manipulation, defi/flash-loan

Dedupe:
- id: `2026-08-atomicatomiclendingoraclemanipulation`
- fingerprint: `d3695dbacb405872028bd96ab251a425ed67ea143ee3c66cef3a68204273984f`

Core exploit idea:
- Two independent alerts describe the same drain from two depths:

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
