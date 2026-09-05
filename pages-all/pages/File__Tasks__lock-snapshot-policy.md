# Locking a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot-policy.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking a Snapshot Policy

Lock a File Storage snapshot policy to prevent updates including pausing and unpausing the policy, moves, and deletions. Locks help protect resources against tampering.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-snapshot-policy.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot-policy.htm)locks.

## Required IAM Policy

To create locks, in addition to[permission to manage the snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#required-iam-service-policy), you need permissions to manage locks.

To lock a snapshot policy, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot-policy.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, from the Actions menu, select Resource lock and then Add .
- In the Add lock panel, select the lock type and select Add .
- 

Use this command and required parameters to lock a snapshot policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddFilesystemSnapshotPolicyLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/AddFilesystemSnapshotPolicyLock)operation to lock a snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
