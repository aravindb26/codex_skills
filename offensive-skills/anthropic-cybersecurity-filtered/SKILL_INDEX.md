# Anthropic Cybersecurity Skills Filtered Index

Filtered source: <https://github.com/mukul975/Anthropic-Cybersecurity-Skills>

Reviewed snapshot: `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed`

Purpose: advanced reference-only workflows for authorized Web2/source-code AppSec, API security, SCA/SBOM, mobile, thick-client, and supply-chain review. These complement Snyk and manual offensive methodology; they do not replace triage or exploit validation.

## Use Rules

- Use only after program policy, scope, safe harbor, and testing limits are understood.
- Load only the exact skill relevant to the current source-code or AppSec task.
- Treat scanner/tool output as leads, not proof.
- Inspect bundled scripts before running them and run only in authorized target workspaces.
- Do not bulk-load this pack into Solidity/Vyper/Solana/Cosmos/Web3 contest audits.

## Installed Skills

- `skills/performing-sca-dependency-scanning-with-snyk/SKILL.md`: Snyk SCA workflow for dependency vulnerability lead generation and triage.
- `skills/performing-web-application-vulnerability-triage/SKILL.md`: scanner-result triage, false-positive reduction, and evidence grading.
- `skills/implementing-secret-scanning-with-gitleaks/SKILL.md`: Gitleaks secret scanning and verification workflow.
- `skills/detecting-broken-object-property-level-authorization/SKILL.md`: OWASP API3 BOPLA field/property-level authorization testing.
- `skills/performing-api-inventory-and-discovery/SKILL.md`: API inventory, endpoint discovery, and surface mapping.
- `skills/performing-api-fuzzing-with-restler/SKILL.md`: stateful REST API fuzzing with RESTler.
- `skills/performing-android-app-static-analysis-with-mobsf/SKILL.md`: Android static analysis with MobSF.
- `skills/performing-thick-client-application-penetration-test/SKILL.md`: desktop/thick-client application security review.
- `skills/detecting-malicious-npm-packages/SKILL.md`: npm package malware and install-script triage.
- `skills/detecting-dependency-confusion/SKILL.md`: public/private package namespace confusion review.
- `skills/detecting-typosquatting-packages-in-npm-pypi/SKILL.md`: npm/PyPI typosquatting analysis.
- `skills/generating-and-analyzing-sboms/SKILL.md`: SBOM generation and vulnerability correlation.
- `skills/analyzing-sbom-for-supply-chain-vulnerabilities/SKILL.md`: SBOM risk analysis against supply-chain vulnerabilities.
- `skills/performing-cve-prioritization-with-kev-catalog/SKILL.md`: KEV/EPSS-driven CVE prioritization.

## Skipped By Design

Generic cyber, SOC, DFIR, malware, Active Directory, red-team infrastructure, and smart-contract skills were not imported. The smart-contract items are weaker than the existing Web3 audit stack and would add noise.
