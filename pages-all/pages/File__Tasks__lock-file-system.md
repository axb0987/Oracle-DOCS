# Locking a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-file-system.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking a File System

Lock a File Storage file system to prevent updates, moves, and deletions of the resource. Locks help protect resources against tampering.

Important  
  
A lock on a file system resource doesn't prevent authorized users from changing the contents of the file system. Users can still create, change, and delete files on a file system with a resource lock.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-file-system.htm)file system locks.

## Required IAM Policy

To create locks, in addition to[permissions to manage the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm#policy), you need permissions to manage locks.

To lock a file system, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, from the Actions menu, select Add resource lock .
- In the Add lock panel, select the lock type and select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/add.html)oci fs file-system add`command and required parameters to lock a file system:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddFileSystemLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/AddFileSystemLock)operation to lock a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
