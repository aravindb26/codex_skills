# Codex Security Reference Boundary

Source: <https://github.com/openai/codex-security>

Reviewed snapshot: `8c85943cd222b76ccb75317b4b17d9ac3ba1647d` on 2026-10-13.

This directory is a reference copy for authorized Web2/source-code AppSec work. It is not an
active default Codex skill and must not be routed into Solidity, Vyper, Solana, Cosmos, Move, or
other Web3 contest audits.

Use the current upstream deep-scan, scope-preservation, finding-normalization, recovery, and cost
accounting code only when the Codex Security CLI/plugin is explicitly being used. Scanner output is
a lead source, not a confirmed finding. Apply the program's scope, safe harbor, manual source
review, evidence, duplicate, and validation gates before reporting anything.

The local `.env.example` is preserved as a user configuration template. Never place real API keys,
tokens, or credentials in this directory or in the private skills backup.
