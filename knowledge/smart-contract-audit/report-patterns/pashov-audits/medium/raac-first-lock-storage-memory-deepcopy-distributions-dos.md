# Pashov Audit Pattern: First lock deep-copies append-only distributions array

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: gas/liveness, reward cursor initialization

## Core Idea

A first-user initialization path copies a storage struct containing a dynamic `distributions` array into memory only to read `distributions.length`. Solidity deep-copies the array, so first-time lock or onboarding gas grows with reward history.

## Broken Invariant

Historical reward distributions must not make new-user onboarding unbounded when only the current distribution length is needed.

## Where To Look

- `RewardData memory`
- `memory rData`
- `distributions.length`
- first-lock or first-stake branches
- append-only reward histories

## Attack Path

Let the distribution array grow normally over time. A new user entering for the first time pays to copy the full history and can eventually run out of gas.

## False-Positive Checks

- Confirm the struct contains a dynamic array.
- Confirm the code uses a storage-to-memory struct assignment.
- Confirm the user is new and cannot skip the initialization branch.
- Confirm direct storage length read would avoid the copy.

## PoC Shape

Append many distributions, then compare gas for first lock before and after growth. The failing path should require no malicious token behavior.
