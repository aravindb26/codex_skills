# Crypto Training Exploit Pattern Stub: API3 dAPI median can be moved by one compromised report

Source:
- https://crypto.training/hacks/17624-compromise-of-a-single-oracle-enables-limited-control-of-the/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2022

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- oracle/single-source, oracle/price-manipulation, oracle/missing-circuit-breaker

Dedupe:
- id: `17624-compromise-of-a-single-oracle-enables-limited-control-of-the`
- fingerprint: `3f2a15f2c663d9cb2ee57d8537dfbfabccbf8f70a702aa10d59196d4dc5bdd59`

Core exploit idea:
- For three values, the median is the middle ordered value. If two honest oracles report 598 and 603, a compromised third oracle can report 598, 601, 603, or any value in…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
