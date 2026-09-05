# Adding a Schedule to a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:46 CDT

# Adding a Schedule to a User-defined Backup Policy

Add a schedule to a user-defined (custom) backup policy in Block Volume.
Important  
  
Indefinite retention is not supported for backups created through backup policies.
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, select the backup policy that you want. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- On the details page, select Schedules and then select Add schedule .

## Add Schedule

On the Add schedule page, enter the following information.
- Schedule Type : Select the backup frequency and then select values for associated options, such as hour of the day, day of the week, day of the month, and month of the year.
- Backup type : Select Full or Incremental .
- Timezone : Select UTC or Regional Data Center Time .

## Data Retention

Select the time period the backup is retained before automatic deletion. The retention period cannot be shortened if the retention lock is enabled.

Retention Period
- Retention time amount: The amount of time that the backup is kept.
- Retention time unit: Select the time unit for the retention period: DAYS or YEARS.
- Retention lock: When enabled, prevents the backup from being deleted until the retention period is reached.
Warning  
  
Once the retention lock is enabled, the retention period cannot be reduced or removed.
Tip  
  
Prevent deletion only prevents deletion of backups that have not expired. Expired backups continue to get deleted automatically.

## Prevent Deletion

Controls whether the backup can be deleted based on its retention and Prevent deletion settings.
Prevent deletion: The following options are available:
- No retention period: Enabling Prevent deletion prevents any user from deleting the backup.
- Configured retention period: Enabling Prevent deletion prevents deletion of the backup until the retention period is reached. The Prevent deletion option can be enabled or disabled.
- A configured retention period and Retention lock is enabled. Prevent deletion is disabled.
Important  
  
When enabled, only users with the`RETENTION_RULE_PREVENT_DELETION`privilege may increase or decrease the backup retention period.

## Add Schedule

Select Add schedule . The schedule is added to the backup policy.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/create.html)oci bv volume-backup-policy create`command and specify the`--schedules`parameter to add a schedule to a user-defined backup policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy)CreateVolumeBackupPolicyDetails`operation and specify the`schedules`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupPolicyDetails)CreateVolumeBackupPolicyDetails`
