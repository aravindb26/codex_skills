# Crypto Training Exploit Pattern Stub: Vesting claim updates index after an external call — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/31192-h-3-reentrancy-in-vestingsolclaim-will-allow-users-to-drain/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/single-function, logic/state-update

Dedupe:
- id: `31192-h-3-reentrancy-in-vestingsolclaim-will-allow-users-to-drain`
- fingerprint: `2af76b3a589e18145a77d984e1616bafd800f030292f15d9aef62d14a8b60ce7`

Core exploit idea:
- Issue H-3 is a vulnerability in the Vesting.sol contract that allows users to drain the contract by exploiting the claim() function. This is due to the contract executin…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
