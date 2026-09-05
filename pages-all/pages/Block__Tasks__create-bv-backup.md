# Creating a Block Volume Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Creating a Block Volume Backup

Create a backup for a volume in the Block Volume service.

A volume backup is a copy of the volume's data stored independently in Object Storage with an independent lifecycle. For more information, see[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm). Create a manual backup for a volume by using the steps in this topic. To create backups based on a defined schedule and retention policy, see[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Manual backups support configurable retention periods that allow the backups to expire automatically when the retention criteria are met.

For information to help you decide whether to create a backup or a clone of a boot volume, see[Differences Between Block Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backupsvsclones). For more information about backups, see[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm)and[Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm).
Note  
  
The size of a volume backup might be larger than the current volume usage. See[Volume Backup Size](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#Size).
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm#)
- 

To create a block volume backup using the console, follow these steps.

## 1. Basic Information

Fill out this basic information.
- On the Block Volumes list page, select the volume that you want. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- On the details page, select Backups , and then select Create Block Volume Backup .
- On the Create block volume backup panel, enter the following information.
- Name : Enter a name for the backup. Avoid entering confidential information.
- Backup type : Select the[backup type](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backuptype), either incremental or full.
- Incremental: This backup type includes only the changes since the last backup.
- Full: This backup type includes all data on the volume.
- Tags : (Optional) Add tags to the backup. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

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

Select Create . The backup is created.

The backup is complete when the State column on the Block Volume Backups list page no longer displays CREATING .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/create.html)oci bv backup create`command and specify the`--volume-id`parameter to create a block volume backup.

```

```

The following is an example of the command.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CreateVolumeBackup)CreateVolumeBackup`operation and specify the`volumeId`attribute for the[`CreateVolumeBackupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupDetails)resource to create a block volume backup.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
