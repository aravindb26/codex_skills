# Crypto Training Exploit Pattern Stub: Burve — Reserve share overflows due to strict reward calculation

Source:
- https://crypto.training/hacks/56958-h-9-reserve-share-overflows-due-to-too-strict-reward-calcula/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `56958-h-9-reserve-share-overflows-due-to-too-strict-reward-calcula`
- fingerprint: `bd74bf05fb6da3f5e35ca01f3c59259d05ae43d119545b31e3f198c90a46f6a8`

Core exploit idea:
- 1. ReserveLib.deposit mints shares as amount * shares / balance. 2. Dust residuals leave balance tiny while amount > 0 still mints. 3. Repeated inflation drives shares n…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
