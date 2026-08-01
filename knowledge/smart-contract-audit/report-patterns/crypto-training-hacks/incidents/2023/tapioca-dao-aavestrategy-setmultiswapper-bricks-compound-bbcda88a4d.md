# Crypto Training Exploit Pattern Stub: Tapioca DAO — AaveStrategy setMultiSwapper bricks compound

Source:
- https://crypto.training/hacks/27529-h-39-aavestrategysol-changing-swapper-breaks-the-contract-co/

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
- id: `27529-h-39-aavestrategysol-changing-swapper-breaks-the-contract-co`
- fingerprint: `bbcda88a4db45c955c6be8d7fd76663ab7f8d4d0047bba76d3093f44b8e0a311`

Core exploit idea:
- 1. Constructor approves the initial multiSwapper for rewardToken. 2. setMultiSwapper only stores the new address. 3. New swapper has zero allowance → compound transferFr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
