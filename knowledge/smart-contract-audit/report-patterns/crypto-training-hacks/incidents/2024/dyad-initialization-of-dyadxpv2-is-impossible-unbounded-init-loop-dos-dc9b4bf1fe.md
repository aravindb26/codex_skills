# Crypto Training Exploit Pattern Stub: DYAD — Initialization of DyadXPv2 is impossible (unbounded init loop DoS)

Source:
- https://crypto.training/hacks/41691-h-04-initialization-of-dyadxpv2-is-impossible-pashov-audit-g/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/unbounded-loop, dos/block-gas-limit, upgrade-safety/uninitializable-contract, liveness/permanent-brick

Dedupe:
- id: `41691-h-04-initialization-of-dyadxpv2-is-impossible-pashov-audit-g`
- fingerprint: `dc9b4bf1fe31ad6b952a20a35e364cc124a26309e627475a1084fbd81699719a`

Core exploit idea:
- 1. DyadXPv2 is an upgradeable contract. On upgrade, initialize() runs once and must fit inside a single block. 2. initialize() eagerly loops over every DNFT (for i in 0.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
