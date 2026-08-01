# Crypto Training Exploit Pattern Stub: Mellow Flexible Vaults — native token withdrawals permanently bricked

Source:
- https://crypto.training/hacks/62108-h-3-unable-to-withdraw-native-tokens-because-vault-and-redee/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `62108-h-3-unable-to-withdraw-native-tokens-because-vault-and-redee`
- fingerprint: `f8ef493ceda1b53f7442c7785c08cb262f115c801c263967b6cff9997de58e5d`

Core exploit idea:
- 1. Protocol lists native token (0xEeee…eEEeE) as a supported asset. 2. Liquid-asset queries always call ERC20 balanceOf on the asset address. 3. Native sentinel has no c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
