# Crypto Training Exploit Pattern Stub: Remora Pledge: uint64 `calculatedPayout` overflows on high-decimal stablecoin payouts, permanently bricking claims

Source:
- https://crypto.training/hacks/61173-distribution-of-payouts-will-revert-due-to-overflow-when-p/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61173-distribution-of-payouts-will-revert-due-to-overflow-when-p`
- fingerprint: `6aecf1eaaedd4e68bea2aa7df82df13d79986f434e3d291f75917b2776815b37`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
