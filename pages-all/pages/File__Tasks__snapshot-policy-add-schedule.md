# Adding a Schedule to a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm
- Fetched: 2026-09-05 02:05 CDT

# Adding a Schedule to a Snapshot Policy

Add schedules to a snapshot policy.

A snapshot policy can contain a maximum of 10 schedules, and schedules must be a combination of schedule type, effective from, and snapshot retention duration that's unique to the policy. You can add schedules to a snapshot policy at the same time you[create the snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm). You can add more schedules to an existing policy, if needed.

When you create a snapshot schedule, you can configure the time that the schedule becomes effective, how often the schedule runs, provide other timing details, and set the[retention duration](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__retention)for snapshots created by the schedule. For more information, see[Schedule Types and Timing](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__schedule-types).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Schedules and then Add schedule .
- Select Add schedule .
- In the Add schedule panel, provide the following details:
- (Optional) Schedule prefix : Enter a prefix for all snapshots created by the schedule. Avoid entering confidential information.
- Schedule type : Select the[frequency](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__schedule-types)at which the snapshots are taken:

- Hourly: A snapshot is created hourly, but not necessarily at the top of each hour.

Note  
  
A snapshot policy can contain only one schedule set to create snapshots hourly.
- Daily: A snapshot is created every 24 hours.
- Weekly: A snapshot is created on selected day of the week.
- Monthly: A snapshot is created on a selected day of the month.
- Yearly: A snapshot is created on a selected month and day of the year.
- (Optional) Schedule effective from : Choose whether the schedule becomes effective immediately, or at a selected date and time. For more information, see[Schedule Types and Timing](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__schedule-types).
- (Optional) Schedule details : Depending on the schedule type, select the Time format and add the details in the corresponding fields. If you don't select a specific value, and leave the default value of Automatic , the system chooses an available value for you.
- (Optional) Snapshot retention duration : The duration that the snapshot is retained before it's deleted by the system. If you don't provide a value, the system sets a default value. For more information, see[retention time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__retention).
- Select Add .
- 

Use the[`oci fs filesystem-snapshot-policy update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/update.html)command and the`--schedules`parameter to add schedules to a snapshot policy:

```

```

The following example includes a`schedules`object with multiple schedules:
```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/UpdateFilesystemSnapshotPolicy)to add a schedule to an existing snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
