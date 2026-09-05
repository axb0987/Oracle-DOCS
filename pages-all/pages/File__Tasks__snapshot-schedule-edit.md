# Editing a Schedule
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-edit.htm
- Fetched: 2026-09-05 02:05 CDT

# Editing a Schedule

Update a snapshot policy's schedule to change its details and snapshot retention duration.

Changes to a schedule only affect future scheduled snapshots. If you change the retention duration in a schedule, the retention duration for past snapshots created by that schedule aren't affected.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-schedule-edit.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Schedules .
- Select the schedule or schedules that you want to edit, select the Actions menu (three dots) , and then select Edit .
- In the Edit schedule panel, update the details as required. For more information, see[Adding a Schedule to a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm).
- Select Update .
- 

Use the[`oci fs filesystem-snapshot-policy update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/update.html)command and with the`--schedules`parameter to update schedules in a snapshot policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/UpdateFilesystemSnapshotPolicy)to update a snapshot policy's schedules.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
