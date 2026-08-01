# Crypto Training Exploit Pattern Stub: Tadle — `DeliveryPlace::settleAskTaker()` mistakenly uses `makerInfo.tokenAddress`

Source:
- https://crypto.training/hacks/38070-the-deliveryplacesettleasktaker-function-mistakenly-uses-mak/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/wrong-token, accounting/direct-drain, logic/state-corruption

Dedupe:
- id: `38070-the-deliveryplacesettleasktaker-function-mistakenly-uses-mak`
- fingerprint: `d093706f6417e21bc0138afd3a0fd129f64786cfcf4bf72e1ae1ad9fdf6ad573`

Core exploit idea:
- 1. When a buyer settles an ask taker position, settleAskTaker correctly pulls in the settlement amount using marketPlaceInfo.tokenAddress — the actual point token config…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
