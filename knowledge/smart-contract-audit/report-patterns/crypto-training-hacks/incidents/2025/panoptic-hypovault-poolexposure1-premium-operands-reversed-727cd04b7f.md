# Crypto Training Exploit Pattern Stub: Panoptic Hypovault — poolExposure1 premium operands reversed

Source:
- https://crypto.training/hacks/62092-h-01-the-poolexposure-for-token1-is-erroneously-calculated-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-math

Dedupe:
- id: `62092-h-01-the-poolexposure-for-token1-is-erroneously-calculated-a`
- fingerprint: `727cd04b7f145d72380cfe5a6338b974208521924f612703ba24c28585f500e3`

Core exploit idea:
- 1. Short premium is an asset; long premium is a liability. 2. poolExposure0 correctly does short − long; poolExposure1 reverses operands. 3. NAV understated (1050 vs 125…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
