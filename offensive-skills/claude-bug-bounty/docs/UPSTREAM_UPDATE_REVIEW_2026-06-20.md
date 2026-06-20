# Upstream Update Review - 2026-06-20

Source: https://github.com/shuvonsec/claude-bug-bounty

Reviewed upstream range:

- Previous local source commit: `59a3c32cc9c222dd660f8475ab24b0318f8b7d2a`
- Current upstream commit reviewed: `2a64de3`

## Decision

Do not directly overwrite the local filtered install.

Reason: upstream added useful Web2/AppSec material, but the updated skills now reference active command/tool files such as `tools/bypass_403.sh`, `tools/waf_encoder.py`, `tools/multipart_mutator.py`, `tools/graphql_audit.sh`, and slash-command workflows that are intentionally not installed in this reference-only setup. A direct copy would create broken or noisy instructions.

## Useful New Patterns To Remember

Use these as manual review prompts during Web2/source-code/AppSec audits, not as automatic tool commands.

- Soft-block WAF detection: `200 OK` can still be a block page. Compare response body, vendor signatures, and body length against a known block baseline before treating a bypass as real.
- WAF bypass concepts: encoding layers, SQL token splitting, HTML/entity encoding, Unicode normalization, multipart parser confusion, content-type confusion, duplicated headers, and origin-server discovery.
- File upload parser mismatch: multipart boundary quirks, duplicate filename parameters, per-part content types, RFC 2231 filenames, and UTF-16LE per-part decoding in Node/Busboy-style stacks.
- Next.js/Node multipart paths: Busboy and Undici can parse multipart/form-data differently from edge filters or WAFs; review server-side parser behavior instead of trusting edge inspection.
- AI/AppSec patterns: MCP tool-description poisoning, MCP resource/tool access control, indirect prompt injection through uploaded RAG documents, vector-DB/RAG poisoning, system prompt extraction only when it exposes secrets or tool maps, and model/API key leakage.
- LFI/file inclusion escalation: file read alone is often weak; chase source disclosure, secrets, `php://filter`, iconv chains, log poisoning, `.user.ini`/`.htaccess` auto-prepend, session inclusion, and `/proc/self/environ` only where the runtime allows it.
- Insecure deserialization: PHP magic methods and `phar://`, Java ysoserial-style gadget surfaces, Python pickle/session signing, and Node serialization sinks.
- Framework quick-wins: check known risky defaults and 1-day patterns, but only report when the vulnerable code path is reachable and in scope.

## Explicitly Not Installed

The following upstream additions remain excluded unless the user explicitly wants them reviewed/installed later:

- active tool scripts
- slash commands
- agents
- MCP integrations
- Web3/meme-coin/smart-contract material
- credential-spray style workflows
- dedicated GraphQL/mobile/CI skills that duplicate existing Claude-Red coverage unless a specific target needs them

## How To Use This Review

For Web2/source-code audits, this note can seed manual hypotheses after the normal flow:

1. Read scope and safe harbor.
2. Map roles, routes, data flows, and trust boundaries.
3. Run Snyk where useful.
4. Use offensive-skills for manual candidate generation.
5. Pull patterns from this note only when they match the target's actual stack.
6. Validate reachability, attacker control, security-boundary impact, and reportability before escalating.
