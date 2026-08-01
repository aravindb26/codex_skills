# Crypto Training Exploit Pattern Stub: Behodler — Double transfer in ERC677 `transferAndCall`

Source:
- https://crypto.training/hacks/42454-h-03-double-transfer-in-the-transferandcall-function-of-erc6/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `42454-h-03-double-transfer-in-the-transferandcall-function-of-erc6`
- fingerprint: `0b0debc3d601fb9c4f7a4a1f9d6a368675286603dbea57f422eaf1661c396eb6`

Core exploit idea:
- transferAndCall calls super.transfer and then _transfer again for the same _value, so the sender is debited twice and the receiver is credited twice.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
