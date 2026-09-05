# Creating a Boot Volume Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Creating a Boot Volume Backup

Create a backup for a boot volume.

You can create a backup of a boot volume using the Oracle Cloud Infrastructure Block Volume service. Boot volume backups are point-in-time snapshots of a boot volume. For more information about boot volume backups, see[Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm).

You can also configure a backup policy that creates backups automatically based on a specified schedule and retention policy. Backup policies work the same as they do with block volumes. See[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for more information.

For information to help you decide whether to create a backup or a clone of a boot volume, see[Differences Between Boot Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm#backupsvsclones).
Note  
  
Boot volume backup size might be larger than the source boot volume size. See[Boot Volume Backup Size](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm#Size)for more information. See also[Boot volume backup size larger than expected](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#bootBackupSize).
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

## Boot Volume Backup Size

Boot volume backup size may be larger than the source boot volume size. Some of the reasons for this could include the following:
- 

Any part of the boot volume that has been written to is considered initialized, so will always be part of the boot volume backup.
- 

Many operating systems write or zero out the content, which results in these blocks marked as used. The Block Volume service considers these blocks updated and includes them in the volume backup.
- 

Boot volume backups also include metadata, which can be up to 1 GB in additional data. For example, in a full backup of a 256 GB Windows boot disk, you may see a backup size of 257 GB, which includes an additional 1 GB of metadata.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm#)
- 

To create a boot volume backup using the console, follow these steps.
- In the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- Select Backups .
- Select Create Boot Volume Backup .

## 1. Basic Information

On the Create boot volume backup panel, enter the following information.
- 

Enter a name for the backup. Avoid entering confidential information.
- Select the backup type, either incremental or full. See[Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm#backuptypes)for information about backup types.
- (Optional) Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

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

Select Create boot volume backup .

The backup is complete when its state is no longer listed as CREATING in the State column on Boot Volume Backups list page.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume-backup/create.html)oci bv boot-volume-backup create`command and specify the`--boot-volume-id`parameter to create a new boot volume backup:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/CreateBootVolumeBackup)CreateBootVolumeBackup`operation and specify the`bootVolumeId`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateBootVolumeBackupDetails)CreateBootVolumeBackupDetails`
