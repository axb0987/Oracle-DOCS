# Deleting a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting a Mount Target

Delete a File Storage mount target.

Caution  
  

Deleting the mount target also deletes all its exports of associated file systems. File systems are no longer available through the deleted mount target.

Deleting a mount target has no effect on file system data or file system snapshots.

High performance mount targets can't be immediately deleted. First, you must[downgrade the mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm)and then, after the billing cycle ends, you can delete the standard mount target. For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm#)
- 

- On the Mount Targets list page, find the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- Select the mount target you want to delete.
- On the details page, from the Actions menu, select Delete .
- When prompted, confirm the deletion.
- 

Use the[`fs mount-target delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/delete.html)command and required parameters to delete a mount target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/DeleteMountTarget)operation to delete a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
