# Unlocking an Export
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-export.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking an Export

Unlock a locked File Storage export to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

Resource unlocking is available using the API only. Run the RemoveExportLock operation to remove a lock from an export. You can also[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-export.htm)export locks.

## Required IAM Policy

To remove locks, in addition to[permissions to manage exports](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#iam), you need permissions to manage locks.

To unlock an export, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-export.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-export.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-export.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Exports .
- Select the export that you want to unlock.
- On the export's details page, next to select Remove resource lock .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/remove.html)oci fs export remove`command and required parameters to unlock an export:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveExportLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/RemoveExportLock)operation to unlock a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
