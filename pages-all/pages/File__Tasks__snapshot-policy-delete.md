# Deleting a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-delete.htm
- Fetched: 2026-09-05 02:05 CDT

# Deleting a Snapshot Policy

Delete a snapshot policy.

When you delete a snapshot policy, the policy and its schedules are deleted. The snapshots created by the policy remain on the file system.
Note  
  
The File Storage service retains deleted snapshot policies for 30 days after deletion. Scheduled snapshots aren't created during this time.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-delete.htm#)
- 

- On the Snapshot Policies list page, find the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- Select the policy you want to delete, and then select Delete .
- In the Delete snapshot policy panel, select Delete .
-   

- 

Use the[`oci fs filesystem-snapshot-policy delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/delete.html)command with the required parameters to delete a snapshot policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[DeleteFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/DeleteFilesystemSnapshotPolicy)to delete a snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
