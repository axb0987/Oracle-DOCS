# Unlocking a Resource-based Snapshot Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking a Resource-based Snapshot Lock

Unlock a locked File Storage snapshot to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-snapshot.htm)snapshot locks.

## Required IAM Policy

To remove locks, in addition to[permission to manage the snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#Required_IAM_Service_Policy), you need permissions to manage locks.

To unlock a snapshot, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot that you want to unlock.
- On the details page, from the Actions menu, select Resource lock and then select Remove .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/remove.html)oci fs snapshot remove`command and required parameters to unlock a snapshot:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveSnapshotLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/RemoveSnapshotLock)operation to unlock a snapshot.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
