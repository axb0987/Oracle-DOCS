# Locking a Snapshot Using Resource Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking a Snapshot Using Resource Lock

Lock a File Storage snapshot to prevent updates, moves, and manual deletions. Locks help protect resources against tampering.

Important  
  
A lock on a snapshot doesn't prevent the system from automatically deleting a snapshot with an expiration date. Expiring snapshots are still deleted, even if they have a resource lock.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-snapshot.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-snapshot.htm)locks.

## Required IAM Policy

To create locks, in addition to[permissions to manage the snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#Required_IAM_Service_Policy), you need permissions to manage locks.

To lock a snapshot, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot that you want to lock.
- On the snapshot's details page, from the Actions menu, select Add resource lock .
- In the Add lock panel, select the lock type and select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/add.html)oci fs snapshot add`command and required parameters to lock a snapshot:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddSnapshotLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/AddSnapshotLock)operation to lock a snapshot.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
