# Deleting an Export
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting an Export

Learn how to delete a File Storage export.

Note  
  
Deleting an export doesn't impact the data stored in the associated file system. Deleting an export disconnects any instance that mounts the file system with the deleted export path. Mount targets that have no exports still count toward your service limit.
Caution  
  
When you delete an export, you can no longer mount the file system using the file path specified in the deleted export.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Exports , and then select the export you want to delete.
- Select the Actions menu and then select Delete .
- When prompted, confirm the deletion.
- 

Use the[`fs export delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/delete.html)command and required parameters to delete an export:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/DeleteExport)operation to delete an export.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
