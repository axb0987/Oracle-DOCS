# Locking an Export
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-export.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking an Export

Lock a File Storage export to prevent updates, moves, and deletions. Locks help protect resources against tampering.

Important  
  
A lock on an export doesn't prevent authorized users from mounting and accessing a file system, or changing the contents of the mounted file system.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-export.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-export.htm)locks.

## Required IAM Policy

To create locks, in addition to[permission to manage exports](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#iam), you need permissions to manage locks.

To lock an export, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-export.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-export.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-export.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Exports .
- Select the export that you want to lock.
- On the export's details page, next to Resource Locking , select Add .
- In the Add lock panel, select the lock type and select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/add.html)oci fs export add`command and required parameters to lock an export:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddExportLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/AddExportLock)operation to lock an export.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
