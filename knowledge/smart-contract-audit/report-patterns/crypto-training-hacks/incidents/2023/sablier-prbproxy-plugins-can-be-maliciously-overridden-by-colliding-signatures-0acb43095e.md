# Crypto Training Exploit Pattern Stub: Sablier / PRBProxy — Plugins can be maliciously overridden by colliding signatures

Source:
- https://crypto.training/hacks/54666-plugins-can-be-maliciously-overridden-by-colliding-signature/

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
- id: `54666-plugins-can-be-maliciously-overridden-by-colliding-signature`
- fingerprint: `0acb43095e46678d578354f6aabb492cd2063260ed9d18b04e54697c185929ca`

Core exploit idea:
- 1. Plugins are installed by mapping each selector from methodList() → plugin address. 2. There is no check that the selector is free; a later install overwrites the earl…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
