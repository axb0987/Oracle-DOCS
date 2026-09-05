# Creating a Volume Group Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Creating a Volume Group Backup

Create automatic point-in-time-consistent backups of all the volumes in a volume group.
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-group-backup.htm#)
- 

- On the Volume Groups list page, find the volume group that you want to back up. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/list-volume-group.htm).
- From the Actions menu (three dots) , select Create volume group backup .

## 1. Basic Information

On the Create volume group backup page, enter the following information.
- Volume Group Backup Name : Enter a name for the volume group backup.
- Backup type : Select a full or incremental backup type.

## 2. Data Retention

Select the time period the backup is retained before automatic deletion. The retention period cannot be shortened if the retention lock is enabled.

Retention Period
- No retention period (keep until deleted): No automatic deletion takes place. The backup is kept until it is deleted.
- Set up retention period: Selecting this option enables more options.
- Retention time amount: The length of time a backup is kept.
- Retention time unit: The unit of time for the retention period: DAYS or YEARS.
- Retention lock: When enabled, prevents the backup from being deleted until the retention period is reached.
Warning  
  
Once the retention lock is enabled, the retention period cannot be reduced or removed.
Tip  
  
Users can create manual backups with an indefinite retention period.
Tip  
  
Prevent deletion only prevents deletion of backups that have not expired. Expired backups are deleted automatically.
Important  
  
Users with the`RETENTION_RULE_INDEFINITE_HOLD`privilege may enable or disable indefinite hold on a backup.

## 3. Prevent Deletion

Controls whether the backup can be deleted based on its retention and Prevent deletion settings.
Prevent deletion: The following options are available:
- No retention period: Enabling Prevent deletion prevents any user from deleting the backup.
- Configured retention period: Enabling Prevent deletion prevents deletion of the backup until the retention period is reached. The Prevent deletion option can be enabled or disabled.
- A configured retention period and Retention lock is enabled. Prevent deletion is disabled.
Important  
  
When enabled, only users with the`RETENTION_RULE_PREVENT_DELETION`privilege may increase or decrease the backup retention period.

## 4. Indefinite Hold

Keeps this backup until the hold is removed. Overrides Prevent deletion and data retention settings.

Indefinite hold: When enabled, keeps the backup indefinitely until the hold is removed.
Important  
  
Users with the`RETENTION_RULE_INDEFINITE_HOLD`privilege may enable or disable indefinite hold on a backup.

## 5. Create Backup

Select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/create.html)oci bv volume-group-backup create`command and specify the`--volume-group-id`parameter to create a volume group backup of the specified volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CreateVolumeGroupBackup)CreateVolumeGroupBackup`
