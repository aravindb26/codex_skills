# Crypto Training Exploit Pattern Stub: Phi — `shareBalance` bloating eventually blocks curator rewards distribution

Source:
- https://crypto.training/hacks/41089-h-03-sharebalance-bloating-eventually-blocks-curator-rewards/

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
- dos/unbounded-growth, gas/enumeration-cost, logic/missing-cleanup

Dedupe:
- id: `41089-h-03-sharebalance-bloating-eventually-blocks-curator-rewards`
- fingerprint: `a20f7e571fb28b648ee70bf8539f9102ee34dbf663610ea872c892178c67ef6f`

Core exploit idea:
- 1. Cred tracks each cred's curator share balances in an EnumerableMap (shareBalance[credId]). Buying adds/increases an entry; selling decreases it. 2. When a curator ful…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
