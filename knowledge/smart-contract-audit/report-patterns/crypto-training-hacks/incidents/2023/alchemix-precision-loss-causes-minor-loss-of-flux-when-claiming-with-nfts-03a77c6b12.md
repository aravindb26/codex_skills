# Crypto Training Exploit Pattern Stub: Alchemix — Precision loss causes minor loss of FLUX when claiming with NFTs

Source:
- https://crypto.training/hacks/38185-precision-loss-causes-minor-loss-of-flux-when-claiming-with/

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
- arithmetic/precision-loss

Dedupe:
- id: `38185-precision-loss-causes-minor-loss-of-flux-when-claiming-with`
- fingerprint: `03a77c6b122b8920e8b0bf2787920d6d6c7d7140584ed4af5eb2b8cb94d0ea39`

Core exploit idea:
- 1. getClaimableFlux computes claimableFlux = (((bpt veMul) / veMax) veMax (fluxPerVe + BPS)) / BPS / fluxMul;. 2. The / veMax immediately followed by veMax is a no-op in…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
