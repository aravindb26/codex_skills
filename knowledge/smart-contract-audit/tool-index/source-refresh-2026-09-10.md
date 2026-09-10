# Source Refresh - 2026-09-10

## Updated

- Code4rena reports: refreshed the newest 20 reports with the local deduping importer; imported 60 new High/Medium finding stubs, all from `2026-04-k2`.
- Crypto Training Hacks: refreshed the public hacks index with the local deduping importer; imported 14 new exploit-pattern stubs.
- HackenProof public skills: installed the distinct `hackenproof-report-quality-scorer` skill and its scoring rubric.
- OpenAI Codex Security: refreshed the isolated reference copy under `offensive-skills/codex-security-reference`.

## Checked And Skipped

- Solodit: refresh blocked because the configured API key returned HTTP 401 `Invalid API key`.
- Trail of Bits skills: checked current upstream, but did not overwrite local skills because several upstream changes are Claude Workflow/`uv`-oriented and would weaken the current Codex-adapted versions.
- Pashov skills: checked current upstream; skipped `fizz` because it is a heavy fuzz-suite generator with Claude-specific orchestration and would add default-audit noise.
- Solana Token Extensions Security: checked current upstream; skipped replacement because local copy contains deeper Token-2022 review guidance and addendum-style coverage.
- Auditmos, QuillAI, Cyfrin Solskill, OpenZeppelin skills, Nemesis, The Judge, SCV Scan, Foundry mainnet-fork PoC, DeFi Builder, Dark Navy installed skills: checked and local content is already current or intentionally curated.
- Claude Bug Bounty, Claude-Red, Recon Skills, Anthropic Cybersecurity Skills: checked, but no broad import performed because the remaining upstream content is duplicate, noisy, or not appropriate for default Web3 audit routing.
- Solidity Auditor Private V3: upstream check failed with `Repository not found` over SSH, so no comparison was possible in this run.

## Notes

- All additions were content-filtered for usefulness and duplicate/noise risk.
- No `AGENTS.md` behavior update was needed; existing routing already covers skills, knowledge, public report stubs, and source-code/offensive reference boundaries.
