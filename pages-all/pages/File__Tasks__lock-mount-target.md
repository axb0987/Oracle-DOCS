# Locking a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-mount-target.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking a Mount Target

Lock a File Storage mount target to prevent updates, moves, and deletions of the resource. Locks help protect resources against tampering.

Important  
  
A lock on a mount target resource doesn't prevent authorized users from mounting and accessing a file system, or changing the contents of the mounted file system.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-mount-target.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-mount-target.htm)locks.

## Required IAM Policy

To create locks, in addition to[permissions to manage the mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#Required_IAM_Policy), you need permissions to manage locks.

To lock a mount target, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-mount-target.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, from the Actions menu, select Resource lock and then select Add.
- In the Add lock panel, select the type of resource lock you want:
- Delete : Prevents the resource from being deleted.
- Full : Prevents all modifications except reading the resource.
- Select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/add.html)oci fs mount-target add`command and required parameters to lock a mount target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddMountTargetLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/AddMountTargetLock)operation to lock a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
