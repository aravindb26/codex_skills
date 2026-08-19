# Crypto Training Exploit Pattern Stub: Elytra: receiveFromStrategy increments the vault's claimableAssets without decrementing the deposi

Source:
- https://crypto.training/hacks/63544-h-01-tvl-double-counts-assets-returned-from-strategy-to-vaul/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63544-h-01-tvl-double-counts-assets-returned-from-strategy-to-vaul`
- fingerprint: `2901fab1698749577700c12a2892163d7690641692169a72847842bd8355c925`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
