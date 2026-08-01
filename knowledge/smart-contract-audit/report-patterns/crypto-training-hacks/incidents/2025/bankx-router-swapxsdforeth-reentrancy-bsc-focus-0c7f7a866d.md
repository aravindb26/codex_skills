# Crypto Training Exploit Pattern Stub: BankX Router — `swapXSDForETH` Reentrancy (BSC focus)

Source:
- https://crypto.training/hacks/2025-02-BankX/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~$43K across BSC + ETH + Optimism

Tags:
- reentrancy/single-function, logic/incorrect-state-transition

Dedupe:
- id: `2025-02-BankX`
- fingerprint: `0c7f7a866de999255cc9fc0f8a5e9205740089342a66019d6a4f47417976337a`

Core exploit idea:
- swapXSDForETH pulls amountInMax XSD into the pool (not the quoted amount), swaps WETH out, unwraps, and safeTransferETHs to msg.sender before burnpoolXSD(amountInMax/10).

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
