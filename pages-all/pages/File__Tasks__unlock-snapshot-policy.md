# Unlocking a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot-policy.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking a Snapshot Policy

Unlock a locked File Storage snapshot policy to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-snapshot-policy.htm)snapshot policy locks.

## Required IAM Policy

To remove locks, in addition to[permission to manage the snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#required-iam-service-policy), you need permissions to manage locks.

To unlock a snapshot policy, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot-policy.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, from the Actions menu, select Resource lock and then Remove .
- 

Use the &lt;TBD&gt; command and required parameters to unlock a snapshot policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveFilesystemSnapshotPolicyLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/RemoveFilesystemSnapshotPolicyLock)operation to unlock a snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
