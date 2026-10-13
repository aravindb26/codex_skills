# Upstream Source Refresh - 2026-10-13

This refresh compared upstream content and behavior, not directory names alone.
Only distinct, useful, low-noise material was added, and local V3 skills and
addenda were preserved.

## Added or updated

- Pashov Solidity Auditor: added `local-pashov-v4-addendum.md` beside the local V3 skill. The upstream V4.1 loop, function-level deduplication, mechanism passes, completeness gate, and report-language improvements were adapted without overwriting the local skill.
- Trail of Bits Semgrep: added upstream `--max-target-bytes` handling and explicit oversized-file coverage reporting to the local script, documentation, and scan JSON contract.
- Forefy Nuclei Suggest: added a filtered Web2/AppSec reference under `offensive-skills/nuclei-suggest-reference`; it is inactive for Web3 and does not auto-run templates.
- Claude Bug Bounty: refreshed selected Web2/AI application, MCP, LLM, scope-hardening, evidence-provenance, investigation-loop, resume-card, compounding-memory, and validation material under `offensive-skills/claude-bug-bounty`.
- OpenAI Codex Security: refreshed the reference copy to commit `8c85943cd222b76ccb75317b4b17d9ac3ba1647d`, including current deep-scan recovery, cancellation, scope preservation, finding normalization, cost accounting, and regression coverage.
- Chase: added a conditional Sui/Move trace-analysis skill under `skills/chase-sui-trace-analysis` from commit `c8c4f18999024119ddb6cbf7f29dbf9e996f9016`. The package and MCP server were not installed.
- Pashov audit PDFs: imported 13 manually reviewed Medium pattern cards from Ensemble 2026-09-14, Pare 2026-09-17, and Pare 2026-10-01. Review decisions are recorded beside the cards.
- Pashov audit index: corrected stale local card paths that pointed to the removed `/home/dinesh/pashov-audits-output` directory.
- Code4rena importer: added a generic-status-title filter and verified the Blackhole report now produces `imported=0` with all 26 existing/status rows skipped.

## Feed results

- Solodit: refresh was blocked by HTTP 401 `Invalid API key`; no unauthenticated import was attempted.
- Pashov Markdown audits: no unreviewed High/Medium Markdown findings remained after deduplication.
- Crypto Training hacks: the refresh identified 41 URL-distinct cards not present in the local index; they are imported by the matching deduplicating importer.
- Code4rena: 100 current report pages were fetched with 0 failures; 26 URL/content-distinct High/Medium candidates were found, 2 new generic `Unmitigated` status stubs were removed as noise, 7 older generic status stubs were also cleaned, 24 substantive new cards were retained, and 1,080 existing findings were skipped.

## Reviewed without adding

- Trail of Bits ChatGPT metadata and similar UI-only changes: no audit behavior change.
- Pashov hub repositories that were educational, paid/closed-source, or duplicate/noise sources: tracked as discovery only.
- Existing Solidity, EVM, Solana, Move, Cosmos, triage, and source-code skills whose current content was unchanged or already covered locally: not duplicated.

## Routing rule

The additions remain conditional. Web3 audit skills and knowledge stay in the
active Web3 trees; Web2/AppSec references stay under `offensive-skills`; Sui
runtime analysis is selected only for Sui/Move transaction or deployment
questions. Nothing in this refresh changes the default Solidity audit workflow.
