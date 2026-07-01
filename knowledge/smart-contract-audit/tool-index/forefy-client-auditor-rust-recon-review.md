# Forefy Candidate Review: Client Auditor And Rust Recon

Checked: 2026-07-01

Registry: <https://forefy.com/skills>

## Client Auditor

- Source: <https://github.com/DarkNavySecurity/web3-skills/tree/96b485e7229fdb260fa74c29d4d123661a466927/client-auditor>
- Decision: installed as a narrowly scoped companion skill.
- Local path: `/home/dinesh/.codex/skills/client-auditor/`
- Use only for blockchain nodes, execution/consensus clients, P2P networking, RPC handlers, bridge components, and related Go/Rust/C++ systems.
- Do not use it as a replacement for `rust-review` or `c-review`; those retain stronger language-level unsafe, FFI, memory-safety, concurrency, and panic coverage.
- Do not route ordinary Solidity, Solana-program, or other smart-contract audits through this skill.
- Its multi-agent workflow requires explicit user authorization before spawning subagents.

Why it adds value:

- consensus and finality invariants
- P2P identity, peer, and network-surface review
- RPC and serialization boundaries
- state/resource exhaustion
- memory/concurrency depth lens
- cross-subsystem verification and adversarial review

## Rust Recon

- Skill source: <https://github.com/NVN404/rust-recon/tree/caaaa1f42039850fe0cbfd709202e3e08baf757f>
- Extractor source: <https://github.com/NVN404/rust-recon-tool/tree/eeea39ffc9c26de803e6f7eecb0ad95b837ed617>
- Forefy Solana benchmark score observed: `0.9733333333` across two runs.
- Decision: do not install or replace existing Solana skills yet.

Blocking issues:

- The skill runbook clones `rust-recon` and then attempts `cargo install --path cli`, but the CLI is in the separate `rust-recon-tool` repository.
- The extractor's `clean` command removes root-level `CLAUDE.md`, `.cursorrules`, and `.github/copilot-instructions.md` as legacy cleanup, which can delete user-owned project files.
- `rust-recon facts` deploys AI configuration by default unless `--no-setup` is supplied.
- The extractor currently has only three unit tests despite its broad AST/fact extraction claims.

Revisit only after upstream fixes the installer path and restricts cleanup to files it can prove it created. Until then, use the installed Solana audit skills, Trailmark, and manual account/instruction mapping.
