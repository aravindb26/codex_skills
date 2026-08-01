# Crypto Training Exploit Pattern Stub: Basin — `WellUpgradeable` can be upgraded by anyone

Source:
- https://crypto.training/hacks/36913-h-01-wellupgradeable-can-be-upgraded-by-anyone-code4rena-bas/

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
- access-control/missing-caller-check, upgradeable/unauthorized-uups-upgrade, governance/admin-takeover

Dedupe:
- id: `36913-h-01-wellupgradeable-can-be-upgraded-by-anyone-code4rena-bas`
- fingerprint: `9dd4588f8b4429449a95713e15267720004c61807fb3c7c88a12638173fd3e63`

Core exploit idea:
- 1. WellUpgradeable is Basin's upgradeable Well variant: UUPSUpgradeable + OwnableUpgradeable, deployed behind an ERC-1967 proxy. 2. OpenZeppelin's docs are explicit: the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
