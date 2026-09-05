# Overriding a File System Lock
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm
- Fetched: 2026-09-05 02:04 CDT

# Overriding a File System Lock

Override the lock for a File Storage file system when performing an action such as an update, move, or deletion.

## Required IAM Policy

To override locks, in addition to[permissions to manage the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm#policy), you need permissions to manage locks.

To update or delete a file system with a full lock, you must have`RESOURCE_LOCK_REMOVE`and`RESOURCE_LOCK_ADD`permissions.

To move a file system with a full lock, you must have`RESOURCE_LOCK_REMOVE`permission in the source compartment and`RESOURCE_LOCK_ADD`in the target compartment. If the lock was created by a service,`RESOURCE_LOCK_REMOVE`and`RESOURCE_LOCK_ADD`permissions in the compartment of the lock.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-file-system.htm#)
- 

You can't use the Console to override a File Storage resource lock. Remove the lock, or use the CLI or API.
- 

Include the required`--is-lock-override`parameter with the command to override the lock on a file system. For example:

```

```

For more information and examples, see[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Include the required`isLockOverride`parameter as`true`with the operation to override the lock on a file system.

For more information and examples, see[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
