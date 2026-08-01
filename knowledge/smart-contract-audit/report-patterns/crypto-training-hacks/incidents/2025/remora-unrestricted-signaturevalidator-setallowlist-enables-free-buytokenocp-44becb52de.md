# Crypto Training Exploit Pattern Stub: Remora — unrestricted `SignatureValidator::setAllowlist` enables free `buyTokenOCP`

Source:
- https://crypto.training/hacks/63776-signaturevalidatorsetallowlist-is-unrestricted-leading-to-fr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier, auth/allowlist-spoof, logic/free-mint

Dedupe:
- id: `63776-signaturevalidatorsetallowlist-is-unrestricted-leading-to-fr`
- fingerprint: `44becb52de4bc7bd7161f837cf44dd063cbd8b00a32c779adf671ee769927035`

Core exploit idea:
- 1. SignatureValidator.setAllowlist is external with no restricted / onlyOwner guard. 2. TokenBank inherits it, so anyone can point the bank at a MaliciousAllowlist whose…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
