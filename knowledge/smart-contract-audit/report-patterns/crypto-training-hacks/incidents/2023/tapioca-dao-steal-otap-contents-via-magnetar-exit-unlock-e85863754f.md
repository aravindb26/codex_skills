# Crypto Training Exploit Pattern Stub: Tapioca DAO — steal oTAP contents via Magnetar exit/unlock

Source:
- https://crypto.training/hacks/27532-h-42-attacker-can-steal-victims-otap-position-contents-via-m/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27532-h-42-attacker-can-steal-victims-otap-position-contents-via-m`
- fingerprint: `e85863754fff0038e610d25dcff0cdfbd555d13ec9ead3df04512a748883d038`

Core exploit idea:
- 1. Victim approves Magnetar for oTAP so they can exit via the helper. 2. Attacker exits victim oTAP with a fake unlock target (no-op). 3. Attacker unlocks real tOLP with…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
