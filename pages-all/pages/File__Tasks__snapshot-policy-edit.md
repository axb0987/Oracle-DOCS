# Editing a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-edit.htm
- Fetched: 2026-09-05 02:05 CDT

# Editing a Snapshot Policy

Update a snapshot policy to change the policy's name or the prefix of snapshots created according to the policy's schedules.

To edit a snapshot policy's schedules, see[Editing a Schedule](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-edit.htm).
Tip  
  
Modifications to a snapshot policy only affect future snapshots created according to its schedules.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-edit.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Edit .
- In the Edit snapshot policy dialog box, update the following details:

- Name : Enter a new name for the schedule. Avoid entering confidential information.
- Policy prefix : Enter a new prefix to apply to all future snapshots created by this policy.
- Select Update .
- 

Use the[`oci fs filesystem-snapshot-policy update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/update.html)command with the required parameters to update a snapshot policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/UpdateFilesystemSnapshotPolicy)to update a snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
