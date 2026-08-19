# Crypto Training Exploit Pattern Stub: Remora Pledge: removing a shared forwarder calls `deleteUser`, wiping `calculatedPayout` still owed to every other forwarding holder

Source:
- https://crypto.training/hacks/61174-a-single-holder-can-grief-the-payouts-of-all-holders-forwa/

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
- id: `61174-a-single-holder-can-grief-the-payouts-of-all-holders-forwa`
- fingerprint: `43bf5130d77bfebb72de082efca8fbcfaa64dfc0d2a760e0319de7c966ed3220`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
