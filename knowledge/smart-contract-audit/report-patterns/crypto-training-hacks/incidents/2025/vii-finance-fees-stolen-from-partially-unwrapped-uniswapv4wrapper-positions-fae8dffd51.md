# Crypto Training Exploit Pattern Stub: VII Finance — fees stolen from partially unwrapped `UniswapV4Wrapper` positions

Source:
- https://crypto.training/hacks/61328-fees-can-be-stolen-from-partially-unwrapped-uniswapv4wrapper/

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
- unknown

Dedupe:
- id: `61328-fees-can-be-stolen-from-partially-unwrapped-uniswapv4wrapper`
- fingerprint: `fae8dffd518adaae05f680f2a932853fae880ea68044e648eea7694fd772e247`

Core exploit idea:
- 1. Partial unwrap of a V4-wrapped position accumulates fees into tokensOwed and pays a proportional share to the unwrapper. 2. tokensOwed is never decremented, so the sa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
