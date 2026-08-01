# Crypto Training Exploit Pattern Stub: Karak — [H-03] A DoS on snapshots due to a rounding error in calculations

Source:
- https://crypto.training/hacks/41067-h-03-a-dos-on-snapshots-due-to-a-rounding-error-in-calculati/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, dos/permanent, rounding/share-price

Dedupe:
- id: `41067-h-03-a-dos-on-snapshots-due-to-a-rounding-error-in-calculati`
- fingerprint: `327320afcc5eb463a01e57d1562aa7d796d9cb25c1eecdc716eb04a9492e350f`

Core exploit idea:
- 1. NativeVault.startSnapshot() calls _transferToSlashStore(), which computes slashedAssets = node.totalRestakedETH - convertToAssets(balanceOf(nodeOwner)). 2. NativeVaul…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
