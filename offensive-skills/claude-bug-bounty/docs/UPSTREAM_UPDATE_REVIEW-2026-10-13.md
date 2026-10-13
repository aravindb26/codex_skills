# Upstream Update Review: 2026-10-13

Reviewed `shuvonsec/claude-bug-bounty` at
`40b03eeea639ef930123924aa316a89566d5180b`.

## Included

- deterministic validation and evidence-provenance guidance
- scope-hardening and target-resume guidance
- bounded investigation-loop and isolated compounding-memory guidance
- `agentic-app-audit`, `mcp-server-audit`, and `llm-redteam` reference skills

These improve Web2/source-code and AI-application review quality by separating leads from verified
findings, preserving evidence provenance, and requiring concrete cross-identity, canary, or action
proof. They remain outside the active Web3 skill directory.

## Intentionally Excluded

- broad active command runners and credential-spray workflows
- Claude hooks and MCP integrations
- `web3-audit`, because Web3 routing remains under `/home/dinesh/.codex/skills/` and the Web3
  knowledge base
- cloud post-access workflows unless a program explicitly authorizes that phase

No upstream instructions were allowed to override Codex, program scope, safe harbor, or evidence
requirements.
