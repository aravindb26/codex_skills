# Crypto Training Exploit Pattern Stub: Beanstalk Silo — legacy milestone stem decimal mismatch

Source:
- https://crypto.training/hacks/31276-the-previous-milestone-stem-should-be-scaled-for-use-with-th/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/decimal-mismatch, logic/state-update

Dedupe:
- id: `31276-the-previous-milestone-stem-should-be-scaled-for-use-with-th`
- fingerprint: `c5648a6421ea5a4ce78848399c7345d3b438f1fda63defacd3d064205e368934`

Core exploit idea:
- The upgrade moves gauge points to untruncated precision but leaves historic milestone stems truncated. Stem tip adds those incompatible units and depositors lose accrued…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
