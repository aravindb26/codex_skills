# Crypto Training Exploit Pattern Stub: FoomCash / FOOM Lottery — Groth16 verifier with `gamma == delta` lets anyone forge proofs

Source:
- https://crypto.training/hacks/2026-02-FoomCash_Groth16/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2026

Chain:
- Ethereum

Loss / impact summary:
- 19,695,576,757,802.19 FOOM (~$1.3M) — the FOOM Lottery pool drained to dust in one tx

Tags:
- auth/signature-validation, logic/missing-check, logic/missing-validation

Dedupe:
- id: `2026-02-FoomCash_Groth16`
- fingerprint: `adac78fb55640cbcd64c81c9e83e91c8446b23406edf65f38e5aaf689c06c5b8`

Core exploit idea:
- 1. FoomCash's FoomLottery is a Tornado-style shielded pool: you play() to deposit FOOM behind a commitment, and later collect() a reward by presenting a Groth16 zero-kno…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
