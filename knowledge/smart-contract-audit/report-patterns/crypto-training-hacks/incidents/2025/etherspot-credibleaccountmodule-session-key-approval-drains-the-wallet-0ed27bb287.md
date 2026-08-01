# Crypto Training Exploit Pattern Stub: Etherspot CredibleAccountModule — session-key approval drains the wallet

Source:
- https://crypto.training/hacks/62847-c-01-sessionkey-owner-drain-smart-wallet/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-owner-check, logic/missing-validation

Dedupe:
- id: `62847-c-01-sessionkey-owner-drain-smart-wallet`
- fingerprint: `0ed27bb2879bfd7a44170f3cd96c48ca792cc344f979ec9faa3452c004c9a65c`

Core exploit idea:
- Session-key call validation allows any ERC20 approve target. The key owner chooses itself as spender, then calls transferFrom to remove every token held by the smart wal…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
