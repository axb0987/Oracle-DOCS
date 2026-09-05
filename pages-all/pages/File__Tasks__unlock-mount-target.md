# Unlocking a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-mount-target.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking a Mount Target

Unlock a locked File Storage mount target to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override mount target locks](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-mount-target.htm).

## Required IAM Policy

To remove locks, in addition to[permissions to manage the mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#Required_IAM_Policy), you need permissions to manage locks.

To unlock a mount target, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-mount-target.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, From the Actions menu, select Resource lock , and then select Remove .
- To confirm your selection, click Remove .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/remove.html)oci fs mount-target remove`command and required parameters to unlock a mount target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveMountTargetLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/RemoveMountTargetLock)operation to unlock a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
