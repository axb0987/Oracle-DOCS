# Deleting a Schedule
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-delete.htm
- Fetched: 2026-09-05 02:05 CDT

# Deleting a Schedule

Delete schedules from a snapshot policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-delete.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Schedules .
- Select the schedule or schedules you want to delete. Then from the Actions menu (three dots) , select Delete .
- When prompted, confirm the deletion.
- 

Use the[`oci fs filesystem-snapshot-policy update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/update.html)command and with the`--schedules`parameter to remove schedules from a snapshot policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/UpdateFilesystemSnapshotPolicy)to delete a snapshot policy's schedules.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
