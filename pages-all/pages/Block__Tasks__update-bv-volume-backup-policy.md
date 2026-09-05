# Updating a Schedule for a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:47 CDT

# Updating a Schedule for a User-defined Backup Policy

Update a schedule in a user-defined (custom) backup policy in Block Volume.
Important  
  
Retention rules enforced when editing an individual volume backup do not apply when editing a backup policy. Users can modify policy settings, including increasing or decreasing retention periods and enabling or disabling Retention Lock.
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-bv-volume-backup-policy.htm#)
- 

## Navigate to Schedule

Navigate to the schedule you want.
- On the Backup Policies list page, select the backup policy that you want. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- Select Schedules .
- Find the schedule that you want to edit.
- From the Actions menu (three dots) , select Edit .

## Edit Schedule

On the Edit schedule page, edit the following information.
- Schedule Type : Select the backup frequency and then select values for associated options, such as hour of the day, day of the week, day of the month, and month of the year.
- Backup type : Select Full or Incremental .
- Timezone : Select UTC or Regional Data Center Time .

## Data Retention

The options selected when the backup was created determine the data retention options available.

No Retention Lock Enabled

If Retention lock is disabled, the retention period and lock can be set. See[Adding a Schedule to a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm).

Retention Lock Enabled

If the Retention lock was enabled, the retention period cannot be reduced or removed. You can increase the duration of the retention period.

## Prevent Deletion

Controls whether the backup can be deleted based on its retention and Prevent deletion settings.
Prevent deletion: The following options are available:
- No retention period: Enabling Prevent deletion prevents any user from deleting the backup.
- Configured retention period: Enabling Prevent deletion prevents deletion of the backup until the retention period is reached. The Prevent deletion option can be enabled or disabled.
- A configured retention period and Retention lock is enabled. Prevent deletion is disabled.
Important  
  
When enabled, only users with the`RETENTION_RULE_PREVENT_DELETION`privilege may increase or decrease the backup retention period.

## Update schedule

After making your changes to the schedule, select Update .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/update.html)oci bv volume-backup-policy update`command and specify the parameters to update the schedule for a volume backup policy:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/UpdateVolumeBackupPolicy)UpdateVolumeBackupPolicy`operation and specify the`policyId`parameter and the`definedTags`,`destinationRegion`,`displayName`,`freeformTags`and/or`schedules`attributes in the[`UpdateVolumeBackupPolicyDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeBackupPolicyDetails)
