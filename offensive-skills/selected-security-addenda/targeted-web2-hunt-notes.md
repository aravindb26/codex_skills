# Targeted Web2 Hunt Notes

Source distilled from selected `uphiago/recon-skills` paths:

- `redteam/hunt-write-gap/SKILL.md`
- `redteam/hunt-business-logic/SKILL.md`
- `recon/source-leak-hunt/SKILL.md`
- `recon/github-secret-hunting/SKILL.md`
- `redteam/hunt-mcp-security/SKILL.md`
- `redteam/vmware-vcenter-attack/SKILL.md`

Use these only when the current program is Web2/source-code/AppSec and the target surface matches.

## Write-Gap And Business Logic

Prioritize flows where a user can create, edit, approve, cancel, refund, export, invite, transfer, or delete something.

Check:

- read endpoint has auth but sibling write endpoint does not
- UI hides a transition but server accepts direct calls
- one-time action can be replayed or raced
- price, quantity, currency, coupon, balance, role, status, or approval fields are trusted from the client
- state can move backward into an editable state after finalization
- cancellation/refund path fails to reverse all side effects
- low-privileged user can invoke manager/admin workflow steps through API or GraphQL

Proof requires control vs exploit contrast using approved test data, not only a `200 OK`.

## Source Leak And Client Bundle Review

When source maps, JS bundles, mobile bundles, debug files, or public repos are in scope:

- extract API base URLs, hidden routes, feature flags, GraphQL operation names, tenant IDs, and internal environment names
- separate public client identifiers from real secrets
- verify that any leaked token/key is live only against an approved test resource
- chain route discovery into authz testing only when the discovered endpoint is currently reachable
- do not treat historical archive paths as current exposure without live confirmation

Use secret validation only within the program's written rules. Never spray or test credentials broadly.

## MCP And LLM-App Surfaces

For apps exposing AI agents, MCP servers, tool calls, or prompt-driven workflows:

- map tools, permissions, token sources, filesystem/network access, and approval boundaries
- test whether untrusted content can influence tool arguments, file paths, URLs, or shell commands
- look for confused-deputy behavior where a low-privileged user causes the agent/server to use higher-privileged credentials
- verify whether tool outputs leak secrets, environment variables, hidden system prompts, private files, or cross-tenant data
- treat prompt injection as report-worthy only when it causes a concrete boundary break

## VMware And Enterprise Appliance Targets

Use only for approved enterprise appliance testing such as VMware/vCenter/Workspace ONE.

Safe checks:

- identify product, version, build, exposed services, SSO metadata, and management endpoints
- map applicability to official vendor advisories before any exploit attempt
- separate version exposure from confirmed exploitability
- avoid password spraying and RCE/file-upload probes unless the program explicitly permits them
- prefer detection-only probes and source/config evidence when testing production appliances

Report only demonstrated impact: unauthenticated sensitive data, authenticated privilege boundary break, approved synthetic file access, or confirmed vulnerable state under allowed testing rules.
