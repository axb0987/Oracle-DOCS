# Unlocking a Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-replication.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking a Replication

Unlock a locked File Storage replication to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-replication.htm)snapshot locks.

## Required IAM Policy

To remove locks, in addition to[permissions to manage the replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-managing-replications.htm#managing_replications_topic_required_iam_policy), you need permissions to manage locks.

To unlock a replication, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-replication.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-replication.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-replication.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
- Select the replication that you want to unlock.
- On the replication's details page, next to select Remove resource lock .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/remove.html)oci fs replication remove`command and required parameters to unlock a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveReplicationLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/RemoveReplicationLock)operation to unlock a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
