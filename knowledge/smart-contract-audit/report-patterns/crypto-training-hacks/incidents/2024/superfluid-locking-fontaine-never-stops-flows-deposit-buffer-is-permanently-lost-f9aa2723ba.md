# Crypto Training Exploit Pattern Stub: Superfluid Locking — `Fontaine` never stops flows; deposit buffer is permanently lost

Source:
- https://crypto.training/hacks/43734-h-3-fontaine-never-stops-the-flows-to-the-tax-and-recipient/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- lifecycle/missing-close, funds/locked, streaming/buffer

Dedupe:
- id: `43734-h-3-fontaine-never-stops-the-flows-to-the-tax-and-recipient`
- fingerprint: `f9aa2723baabc81ff7d3e38ab92ebcaf45a48622b08d65c947d61524498c76ee`

Core exploit idea:
- 1. Superfluid reserves 4 hours of flow rate as a deposit buffer when a flow opens. 2. Fontaine.initialize opens a tax distributeFlow and a recipient createFlow. 3. There…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
