# Local Solodit Addendum: Proxy Upgrade Companion Mini-Skill

## Purpose
- Extend `proxy-upgrade-safety` with distilled High/Medium Solodit upgradeability patterns.
- Do not replace `SKILL.md`.
- Use this for missing exploit shapes around migrations, diamonds, delegatecall modules, initializer gaps, and operational upgrade failures.

## When To Use

Use after reading `proxy-upgrade-safety/SKILL.md` when code uses:
- Transparent/UUPS/beacon/diamond proxies, clone factories, upgradeable modules, delegatecall plugins, facet cuts, reinitializers, or migration scripts.

## Companion Workflow

1. Load the original proxy skill first.
2. Search current code with the extra terms below.
3. Map every proxy, implementation, initializer, upgrade function, facet, and delegatecall module.
4. Check storage layout, initializer state, auth, selector routing, and upgrade/migration liveness.
5. Search Solodit stubs by proxy type, facet function, initializer, and upgrade path before escalating.

## Extra Search Terms

```text
initializer
reinitializer
_disableInitializers
upgradeTo
upgradeToAndCall
_authorizeUpgrade
diamondCut
facet
selector
fallback
delegatecall
CALLTYPE_DELEGATECALL
implementation
beacon
storage gap
__gap
initData
```

## Missing / Sharper Patterns To Check

### 1. Migration and reinitializer liveness failure

Shape:
- Upgrade/migration can permanently fail due to invalid array lengths, stale init state, missing dependency initialization, or wrong reinitializer ordering.

Questions:
- Can bad migration input brick future upgrades?
- Are all new module dependencies initialized exactly once?
- Does the upgrade path work from every deployed historical version?

### 2. Diamond facet replay and selector drift

Shape:
- Diamond cuts can be replayed, old updates re-executed, selectors shadowed, or facets modified without the intended auth.

Questions:
- Is `diamondCut` access controlled and replay protected?
- Are removed/replaced selectors still reachable through fallback?
- Can selector collisions route user calls to admin/facet logic?

### 3. Delegatecall module survives ownership or context change

Shape:
- A delegatecall-enabled module/fallback handler remains installed after NFT/account ownership, safe signer, or plugin ownership changes.

Questions:
- Can a new owner inherit a dangerous delegatecall module?
- Does delegatecall write to storage that belongs to the current owner/account unexpectedly?
- Are modules cleared on transfer, migration, or uninstall?

### 4. Implementation/proxy mismatch beyond storage

Shape:
- Proxy and implementation disagree on access model, immutable variables, self-address checks, constructor assumptions, or context.

Questions:
- Does implementation use `address(this)` or immutable values expecting direct deployment?
- Does proxy call implementation functions that assume constructor initialization?
- Are implementation-only functions callable directly with harmful effects?

### 5. Upgrade auth exists but wrong actor/path controls it

Shape:
- `_authorizeUpgrade` or admin checks exist, but another module, initializer, delegatecall path, or role sync issue bypasses them.

Questions:
- Can an initializer grant upgrade role after deployment?
- Can delegatecall set admin/implementation slots?
- Can role/owner transfer leave upgrade admin stale or inconsistent?

## False-Positive Filters

Do not escalate unless:
- The affected contract is upgradeable or delegatecall-based in the in-scope deployment.
- The issue can corrupt storage, block upgrades, bypass auth, brick a proxy, or change user-fund logic.
- The path is not only a theoretical old-version issue outside accepted deployment state.
- Admin-only upgrade risk violates program assumptions or causes direct user impact.
