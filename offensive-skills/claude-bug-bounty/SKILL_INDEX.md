# Claude Bug Bounty Skill Index

Reviewed through commit: `e363fa09f003d77a0420abcd081628cdbe7f8ed4`

Reference-only filtered Web2/AppSec/source-code bounty skills. Do not use as the default smart-contract audit toolbox.

## Methodology

- `bb-methodology`: Start-of-session bug bounty methodology, target selection, focused hunting, developer-psychology checks, anomaly detection, and workflow discipline.

## Recon And Attack Surface

- `web2-recon`: Web2 recon and asset-discovery pipeline. Use only when recon is in scope and safe-harbor permits the required activity.

## Vulnerability Classes

- `web2-vuln-classes`: Reference for Web2 bug classes such as IDOR, auth/access-control bypass, XSS, SSRF, SQLi, file upload, GraphQL, OAuth/OIDC, JWT, request smuggling, cache poisoning, SAML, MFA bypass, CSS injection, and cloud/infra misconfigurations.

## Payloads And Patterns

- `security-arsenal`: Payloads, bypass tables, wordlists, conditionally-valid chains, and always-rejected patterns. Use as a reference, not as proof of a vulnerability.

## Validation And Reporting

- `triage-validation`: Pre-report validation gates. Use before writing a report to kill weak, out-of-scope, theoretical, or duplicate-prone findings.
- `report-writing`: Bug bounty report-writing templates and impact-first reporting guidance. For Web3 reports, prefer the dedicated smart-contract audit report standards in the active knowledge base.

## Helper Tools

- `tools/lead_board.py`: Persistent Web2 recon lead ledger. Use after authorized recon to ingest observations, preserve statuses, pick next leads, and avoid forgetting attack surfaces during long Web2/source-code bounty work. Do not use for smart-contract audit lead tracking.
- Selected helper scripts referenced by the retained Web2 skills: 403 bypass confirmation, GraphQL audit, multipart mutation, parameter discovery, secret hunting, takeover checks, WAF encoding/response analysis, and wordlist support. Inspect before use and run only when the program scope permits it.

## Boundary

Excluded Web3, meme-coin, credential-spray, active command, agent, MCP, and tool-runner content is listed in `docs/FILTERED_INSTALL_NOTES.md`.

Recent upstream updates reviewed but not directly copied are summarized in `docs/UPSTREAM_UPDATE_REVIEW_*.md`.
