# Crypto Training Exploit Pattern Stub: Mute.Io — dMute: attacker can push lock items to victim's array

Source:
- https://crypto.training/hacks/16040-h-03-dmutesol-attacker-can-push-lock-items-to-victims-array/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `16040-h-03-dmutesol-attacker-can-push-lock-items-to-victims-array`
- fingerprint: `2000e52a4d731df6d71c87fad58604b1547061b872713b17db4b079ab45f4611`

Core exploit idea:
- Anyone can LockTo dust for any address, inflating their lock array. RedeemTo iterates the entire array even when redeeming one index, so enough spam makes redeem exceed…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
