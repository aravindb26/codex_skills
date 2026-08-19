# Codex Security Reference

Source: <https://github.com/openai/codex-security>

Reviewed snapshot: `613469a79f6d73a7f9ccf43295e0cd7afdc5fc1b`

Purpose: local reference copy of OpenAI Codex Security workflows for authorized Web2/source-code security scans, finding validation, tracking, attack-path analysis, and writeups.

Use rules:

- Treat this as reference-only unless the Codex Security plugin/tooling is explicitly installed and invoked.
- Use for source-code AppSec, not as default smart-contract audit context.
- Scanner output is a lead source only; validate manually against scope, exploitability, impact, and false-positive risk.
- Keep any scan artifacts in an audit-specific workspace or `.context/` path so they can be cleaned up at audit end.
