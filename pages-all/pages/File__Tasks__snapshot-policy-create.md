# Creating a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm
- Fetched: 2026-09-05 02:05 CDT

# Creating a Snapshot Policy

Create a snapshot policy for automatic snapshot creation and deletion. A snapshot policy contains up to 10 schedules for automatic snapshots. A snapshot policy won't create snapshots without schedules.

If you don't create a schedule when you create a policy and you want to add one or more schedules to an existing policy, see[Adding a Schedule to a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm#)
- 

- On the Snapshot Policies list page, select Create snapshot policy . If you need help finding the list page, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-list.htm).
- In the Create Snapshot Policy window, provide the following details:
- Snapshot policy name : Enter a name for the snapshot policy. Avoid entering confidential information.
- (Optional) Snapshot policy prefix : A prefix to apply to all snapshots created by this policy.
- Availability domain : Specify the availability domain that you want to create the snapshot policy in. The first availability domain selected in the leftmost panel list is used as default.
- Create in compartment : Specify the compartment that you want to create the snapshot policy in.
- (Optional) To create one or more schedules for the snapshot policy, select Add schedule . If you don't add schedules now, you can[add a schedule to a snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm)at any time after the snapshot policy is created. A snapshot policy can have a maximum of 10 schedules, and schedules within a snapshot policy must be a combination of Schedule Type , Schedule Effective From , and Snapshot Retention Duration that's unique to the policy.
- (Optional) Schedule prefix : Enter a prefix for all snapshots created by the schedule. Avoid entering confidential information.
- Schedule type : Select the[frequency](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__schedule-types)at which the snapshots are taken:

- Hourly: A snapshot is created hourly, but not necessarily at the top of each hour.

Note  
  
A snapshot policy can only contain one schedule set to create snapshots hourly.
- Daily: A snapshot is created every 24 hours.
- Weekly: A snapshot is created on selected day of the week.
- Monthly: A snapshot is created on a selected day of month.
- Yearly: A snapshot is created on a selected month and day of the year.
- (Optional) Schedule effective from : Choose whether the schedule becomes effective immediately, or at a selected date and time. For more information, see[Schedule Types and Timing](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__schedule-types).
- (Optional) Schedule details : Depending on the schedule type, select the Time format and add the details in the corresponding fields. If you don't choose a specific value, and leave the default value of Automatic , the system chooses an available value for you.
- (Optional) Snapshot retention duration : The duration that the snapshot is retained before it's deleted by the system. If you don't provide a value, the system sets a default value. For more information, see[retention time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__retention).
- (Optional) Select Add schedule to add more schedules to the policy.
- (Optional) To add tags to the snapshot policy, select Add tag .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Resource locks section, select a lock level for the resource:

- No Lock : No restrictions.
- Delete : Prevents the resource from being deleted.
- Full : Prevents all modifications except reading the resource.
- To create the snapshot policy, select Create .
- (Optional) To save the configuration as a Resource Manager stack, select Save as stack . For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
- 

Use the[`oci fs filesystem-snapshot-policy create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/create.html)command and required parameters to create a snapshot policy:

```

```

To create schedules at the time you create the policy, include the optional`schedules`parameter. For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[CreateFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/CreateFilesystemSnapshotPolicy)to create a snapshot policy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
