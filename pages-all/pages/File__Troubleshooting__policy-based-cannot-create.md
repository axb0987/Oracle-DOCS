# Can't Attach a Snapshot Policy to a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/policy-based-cannot-create.htm
- Fetched: 2026-09-05 02:06 CDT

# Can't Attach a Snapshot Policy to a File System

When creating or updating a file system and attaching a snapshot policy, an error occurs.

## The snapshot policy is in an invalid state

You can't attach a snapshot policy that's in a DELETING, DELETED, or FAILED state.

Attach a snapshot policy to the file system that's ACTIVE or INACTIVE.

## The file system is a replication target

A file system that's a replication target can't have snapshot policies attached.

Attach a snapshot policy to another file system, such as the source file system for the replication. Or, you could[delete the replication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/fsreplication-managing-replications.htm)
