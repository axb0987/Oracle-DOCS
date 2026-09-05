# Snapshot Locks
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot_lock_overview.htm
- Fetched: 2026-09-05 02:05 CDT

# Snapshot Locks

Use snapshot locks to protect File Storage snapshots from deletion and to help meet retention requirements.
You can use two kinds of locks: resource-based locks and time-based locks. Use resource-based locks for basic protection that you can change later. Use time-based locks (governance or compliance) when you need to keep a snapshot or file system undeletable for a set duration—or, in governance mode, optionally indefinitely.
Note  
  
When a snapshot is locked, it (or the file system or was generated for) can't be deleted. However, depending on the type of lock, you might still be able to update, move, or change the snapshot's settings (see the[table](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot_lock_overview.htm#lock-types-summary)).

## Resource-Based Locks

Use OCI resource-based locks for fundamental protection. If you have the required IAM permissions, you can[add](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm#top),[change](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-snapshot.htm#top), or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm#top)these locks.

You can select one of these types:
- Delete lock: Blocks deletion. Other updates, such as editing metadata, are allowed.
- Full lock: Blocks deletion, updates, and moving the snapshot.

## Time-Based Locks

Use time-based locks for compliance or to protect snapshots for a set period. In the OCI Console, set a lock duration in days. You can also use Legal hold in governance mode for protection that doesn't end until you remove it.

Select a time-based lock mode: governance or compliance .

Key definitions:
- Lock duration: Days the lock will prevent deletion of a snapshot. Minimum is 1 day, maximum is 100 years (36,500 days). Governance mode allows a time-limited or indefinite lock (with Legal hold ). Compliance must be time-bounded.
- Cool-off duration: Compliance-only period (in days) when you can change or remove the lock if you have permissions. After cool-off, the lock is fully enforced and can only be extended. Default is 14 days; set to`0`to enforce immediately.
Note  
  
If a snapshot has an active time-based lock, you can't delete the snapshot or the file system that contains it.

### Governance Lock

A governance lock blocks snapshot deletion for the locked duration and takes effect immediately (no cool-off period).

Use this when you want temporary or indefinite protection, but still need flexibility. With the right permissions, you can change the lock duration or remove the lock.

Optionally select Legal hold for indefinite protection. You can remove a legal hold at any time (with permissions).

### Compliance Lock

Use a compliance lock for strict, non-editable retention. Set a lock duration and a Cool-off duration . During cool-off, you can edit or remove the lock. After cool-off, the lock can't be removed or shortened (only extended).
Caution  
  
We recommend compliance locks only for strict retention needs. After the cool-off period, no user can remove or reduce the lock duration, regardless of their permissions.

### Lock Types Comparison

This table compares lock types and the actions they allow:

Snapshot Lock Type Comparison
Lock Type Prevents Deletion Allows Lock Setting Changes Has Lock Duration (Days) Has Cool-off Duration Can Be Removed Later Uses
Resource-based: Delete lock Yes Yes (if you have permissions) No No Yes (with required permissions) Prevents deletion. Other changes are allowed.
Resource-based: Full lock Yes Yes (if you have permissions) No No Yes (with required permissions) Prevents deletion, updates, and move.
Time-based: Governance Yes (until the lock duration ends) Yes (if you have permissions) Yes (or indefinite with Legal hold ) No Yes (with required permissions) Flexible retention. Optional Legal hold for indefinite lock.
Time-based: Compliance Yes (until the lock duration ends) Limited (after cool-off, you can only extend duration) Yes (time-bounded) Yes Yes (during cool-off only) Strict retention. After cool-off, lock can't be removed or shortened.

### Switching between Lock Types

You can change a snapshot's time-based lock mode sometimes. Add a resource-based lock at any time.
- Governance to compliance: You can switch from governance mode to compliance mode. To enforce compliance immediately, set the cool-off duration to`0`.
- Compliance to governance: You can switch from compliance mode back to governance mode only during the cool-off period. After cool-off, switching is not allowed.
- Resource-based locks: These are independent. You can use both a resource-based and a time-based lock, but the most restrictive lock applies.

For example, if a snapshot has both types of lock: when the time-based lock's retention period ends, the resource lock (if present) might still block deletion or updates until you remove it.

## Use Cases

Common scenarios for snapshot locks include:
- Prevent accidental deletion: Add a resource-based lock as a quick, removable safeguard.
- Ransomware recovery: Use a time-based lock to keep a known-good snapshot protected for the recovery window.
- Regulatory retention: Use a compliance lock to retain snapshots as required for audits or regulations.
- Internal governance: Use a governance lock when you want flexibility to adjust retention or remove the lock.
- Legal hold: Use governance mode with legal hold to keep a snapshot protected until regulatory or legal needs end.

## Required IAM Permissions

To manage snapshot locks, you must have permissions to create, update, and remove locks. Required permissions vary by lock type and mode (resource-based, governance, or compliance).

For details on File Storage permissions, see[Policy Details for the File Storage service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Considerations

Before you use snapshot locks, keep these points in mind:
- File system deletion can be blocked: If any snapshot in a file system has an active time-based lock, you can't delete the file system until the retention period ends and any Legal hold is removed.
- Compliance locks become immutable: After cool-off, you can only extend the retention period; you can't remove the lock or shorten it. During cool-off, you can still change or remove the lock.
- Cool-off defaults: The default cool-off duration is 14 days. Set cool-off to`0`to enforce immediately.
- End of retention: After the retention period completes, the snapshot lock is lifted automatically and the snapshot is treated as unlocked (regular mode).
- Expiration time doesn't override locks: A snapshot's Expiration time is separate from snapshot locks. If a delete operation is attempted after expiration (manually or by automated cleanup) while the snapshot is locked, the delete operation fails until the lock is removed (resource-based) or the lock period ends (time-based, and any Legal hold is removed).
- Policy-based snapshots: You can create a snapshot policy to automatically apply time-based locks to new snapshots.[Learn more](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm#top).
Note  
  
You can't create a snapshot policy to apply resource-based locks.
- Clones and replications: If you clone a file system or snapshot, or replicate a file system to a target file system, snapshot lock properties aren't inherited (copied) to the clone or the replication target. If you need retention or deletion protection in the clone or target, configure snapshot locks separately there.
-
