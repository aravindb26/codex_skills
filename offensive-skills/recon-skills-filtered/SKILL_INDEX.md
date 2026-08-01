# Recon Skills Filtered Index

Filtered source: <https://github.com/uphiago/recon-skills>

Reviewed snapshot: `1db898cec0ce8775a5c5ce12e97632fce858f6a1`

Purpose: advanced reference-only workflows for authorized Web2/AppSec recon, source-code bounty work, and evidence building. These are lead generators and methodology helpers, not automatic proof.

## Use Rules

- Use only after program scope, safe harbor, and testing limits are understood.
- Load only the exact skill relevant to the current target or hypothesis.
- Treat scripts as optional helpers; inspect before running and run only on authorized targets.
- Do not bulk-load this pack into smart-contract audits.
- Do not submit a finding from this pack without fresh evidence, scope fit, duplicate checks, and real impact validation.

## Installed Skills

- `skills/recon-playbook/SKILL.md`: authorized external web/API assessment structure and recon discipline.
- `skills/evidence-hygiene/SKILL.md`: evidence capture, redaction, PoC safety, and report hygiene.
- `skills/cross-attack-chains/SKILL.md`: combine independently verified findings into higher-impact chains without overclaiming.
- `skills/hunt-write-gap/SKILL.md`: read-protected/write-open endpoint hunting.
- `skills/hunt-business-logic/SKILL.md`: financial and workflow business-logic bug patterns from public reports.
- `skills/hunt-source-leak/SKILL.md`: source maps, build artifacts, `.env`, `.git`, Swagger/OpenAPI, and bundle leak review.
- `skills/js-secrets-extraction/SKILL.md`: JavaScript bundle/source-map secret and endpoint extraction.
- `skills/github-secret-hunting/SKILL.md`: public GitHub credential and token leak hunting.
- `skills/hunt-mcp-security/SKILL.md`: MCP and AI-tool integration security review.
- `skills/vmware-vcenter-attack/SKILL.md`: VMware/vCenter external attack-surface review.
- `skills/unauth-api-flow-hijack/SKILL.md`: unauthenticated multi-step API flow abuse.
- `skills/hunt-schema-enumeration/SKILL.md`: schema and hidden-field enumeration via API error behavior.
- `skills/hunt-cicd/SKILL.md`: CI/CD, workflow injection, runner, OIDC, Jenkins, GitLab, artifact, and Terraform-state review.
- `skills/hunt-supabase/SKILL.md`: Supabase anon-key, RLS, RPC, bucket, and multi-tenant data-boundary review.
- `skills/firebase-supabase-attack/SKILL.md`: Firebase/Supabase exposed config and rules testing.
- `skills/hunt-grpc/SKILL.md`: gRPC reflection, metadata auth, gateway, and HTTP/2 edge cases.
- `skills/hunt-websocket/SKILL.md`: WebSocket origin, per-message auth, namespace, room, and upgrade-smuggling review.

## Skipped By Design

Generic Web3, meme-token, broad OSINT, mass recon, and vulnerability-class duplicates were not imported here because they either overlap existing Web3 skills or add too much operational noise.
