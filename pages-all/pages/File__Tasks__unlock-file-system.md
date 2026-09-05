# Unlocking a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-file-system.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking a File System

Unlock a locked File Storage file system to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override file system locks](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm).

## Required IAM Policy

To remove locks, in addition to[permissions to manage the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm#policy), you need permissions to manage locks.

To unlock a file system, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, from the Actions menu, select next to select Remove resource lock .
- Select Remove to confirm the removal.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/remove.html)oci fs file-system remove`command and required parameters to unlock a file system:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveFileSystemLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/RemoveFileSystemLock)operation to unlock a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
