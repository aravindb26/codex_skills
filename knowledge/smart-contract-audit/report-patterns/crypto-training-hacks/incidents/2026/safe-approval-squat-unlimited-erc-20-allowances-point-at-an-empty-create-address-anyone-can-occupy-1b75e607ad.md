# Crypto Training Exploit Pattern Stub: Safe approval squat — unlimited ERC-20 allowances point at an empty CREATE address anyone can occupy

Source:
- https://crypto.training/hacks/2026-10-safeapprovalsquat/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Avalanche

Loss / impact summary:
- The Safe's entire balance of four tokens output.txt:357. 3,078,123.681646 USDC (307812368…

Tags:
- unknown

Dedupe:
- id: `2026-10-safeapprovalsquat`
- fingerprint: `1b75e607ad249dc25a088372e4e22a6ad94036ab3996478be937e35a75b6269f`

Core exploit idea:
- On 2026-03-07 the Safe approved type(uint256).max of USDC, WAVAX, WETH.e, and BTC.b to 0x3725bD4D…. At block 98,603,854 that address still has no code, and the four allo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
