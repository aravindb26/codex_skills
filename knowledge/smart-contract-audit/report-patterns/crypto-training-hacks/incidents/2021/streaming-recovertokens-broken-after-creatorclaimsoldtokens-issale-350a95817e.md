# Crypto Training Exploit Pattern Stub: Streaming — recoverTokens broken after creatorClaimSoldTokens (isSale)

Source:
- https://crypto.training/hacks/42396-h-10-recovertokens-doesnt-work-when-issale-is-true-code4rena/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/missing-state-update, loss-of-funds/locked-funds

Dedupe:
- id: `42396-h-10-recovertokens-doesnt-work-when-issale-is-true-code4rena`
- fingerprint: `350a95817e52df44ddfb072ac2ed90c24c04abb431d70227bf474bce224ae8e6`

Core exploit idea:
- creatorClaimSoldTokens does not update redeemedDepositTokens, so recoverTokens underflows and excess deposit tokens are permanently locked

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
