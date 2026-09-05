# Locking a Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-replication.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking a Replication

Lock a File Storage replication resource to prevent updates, moves, and deletions of the resource. Locks help protect resources against tampering.

Important  
  
A lock on a replication resource doesn't prevent the replication from proceeding. The replication process continues even if the resource is locked.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-replication.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-replication.htm)locks.

## Required IAM Policy

To create locks, in addition to[permissions to manage replications](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-managing-replications.htm#managing_replications_topic_required_iam_policy), you need permissions to manage locks.

To lock a replication, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-replication.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-replication.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-replication.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
- Select the replication that you want to lock.
- On the replication's details page, next to Resource Locking , select Add .
- In the Add lock panel, select the lock type and select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/add.html)oci fs replication add`command and required parameters to lock a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddReplicationLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/AddReplicationLock)operation to lock a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
