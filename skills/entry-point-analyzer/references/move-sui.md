# Move Entry Point Detection (Sui)

## Entry Point Identification (State-Changing Only)

For Sui, analyze public functions that can be invoked through programmable transaction blocks and `entry` functions; applicability depends on the Sui Move version and function signature. Do not apply Aptos transaction-script reachability rules to Sui. Package-visible and private functions are not independent transaction entry points, though their callers still need review.

```move
// Public functions
public fun compute(obj: &mut Object): u64 { }

// Entry functions in Sui
public entry fun transfer(ctx: &mut TxContext) { }
```

### Visibility Rules
| Visibility | Include? | Notes |
|------------|----------|-------|
| `public entry fun` | **Yes** | Callable from transactions and modules |
| `public fun` | **Yes** | Callable from transactions and modules |
| `entry fun` | **Yes** | Callable from transactions, but not other modules |
| `fun` (private) | No | Not externally callable |
| `public(package) fun` | No | Only callable by other modules in the same package |

## Access Control Patterns

```move
// Object types have the key ability
public struct MyObject has key { id: ID, ... }

// Capability objects typically have names that end with "Cap"
public struct AdminCap has key { id: ID, ... }

// Shared objects can be created through Sui's sharing APIs
public struct Pool has key { id: ID, ... }

// Object ownership provides access control
public fun use_owned_object(obj: &mut MyObject) {
    // Only owner of obj can call this
}

// A shared object may be supplied by an arbitrary transaction; the function's
// signature and body still determine which operations and callers are allowed.
public fun use_shared(pool: &mut Pool) { }

// Shared Pool object gated by capability - only owner of AdminCap can call
public fun capability_gate(_cap: &AdminCap, pool: &mut Pool) {}
```

### Access Control Classification
| Pattern | Classification |
|---------|----------------|
| Owned object parameter | Owner of object |
| Shared object | Potentially transaction-accessible; inspect function visibility/signature, transaction constraints, and role/capability checks |

## Contract-Only Detection

### Package-protected Functions
```move
// Only callable by other modules in the same Move package
public(package) fun internal_fun() { }
```

`public(package)` is not an external transaction entry point. Confirm the target chain and Move version before interpreting visibility modifiers.

## Extraction Strategy

1. Parse all `.move` files
2. Find `module` declarations
3. Extract `public`, `public entry`, and `entry` functions
4. Extract object type declarations (`struct`'s that have the `key` ability)
5. Determine whether each object type is **owned** (passed as parameter to `transfer` or `public_transfer` functions) or **shared** (passed as parameter to `share` or `public_share` functions)
6. Analyze parameters:
   - Owned object type with "XCap" in name -> X role (e.g., AdminCap = Admin role, GuardianCap = Guardian role)
   - Owned object type without "Cap" in name -> Owner role
   - Shared object type -> Public

## Move-Specific Considerations

1. **Object Model**: Access control typically through object ownership (rather than runtime assertions)
2. **Capabilities**: `Cap` suffix typically indicates capability pattern
4. **Generic Types**: Type parameters may carry capability constraints
5. **Package Visibility**: `public(package)` limits callers to modules in the same package

## Common Gotchas

1. **Module Initializers**: `init` functions often create singletone shared objects and initial capabilities
2. **Object Wrapping**: Wrapped objects transfer ownership
3. **Shared vs Owned**: A shared object may be passed to a transaction by a non-owner; this does not bypass function-level authorization or transaction constraints. Owned objects are subject to ownership rules enforced by the runtime.
4. **Package Upgrades**: Upgrades can introduce new types and functions and change old ones in type-compatible ways
5. **Phantom Types**: Type parameters with `phantom` don't affect runtime
