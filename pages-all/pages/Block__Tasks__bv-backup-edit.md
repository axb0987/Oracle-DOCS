# Updating a Block Volume Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/bv-backup-edit.htm
- Fetched: 2026-09-05 01:45 CDT

# Updating a Block Volume Backup

Edit the configuration of a block volume backup.
Note  
  
To use backup retention features, you must configure the correct IAM policies. See[Required IAM Policies for Backup Retention Features](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backup-retention-IAM-Policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/bv-backup-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/bv-backup-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/bv-backup-edit.htm#)
- 

Edit the following block volume backup options using the console.
- On the Block Volume Backups list page, locate the backup you want to work with. If you need help finding the list page, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm).
- Select the Actions menu (three dots) , and then select Edit .

## Basic Information

Edit basic information.

Name : Edit the backup name. Avoid entering confidential information.

## Data Retention

The options selected when the backup was created determine the data retention options available.
- No retention period (keep until deleted): If no retention period was set you have the following options.
- Select Set up retention period to set the retention period and enable the retention lock. Set the following options.
- Retention time amount: Sets the retention duration.
- Retention time unit: Sets the unit of time used for the retention duration.
- Retention lock: Enabling the Retention lock prevents users from deleting the backup until the end of the retention period.
- A configured retention period and Retention lock is disabled . The options are as follows:
- You can increase or decrease the duration of the retention period.
- Prevent deletion: When enabled, the backup cannot be deleted during the retention period. The Prevent deletion option can be enabled or disabled.
- A configured retention period and Retention lock is enabled . The options are as follows:
- You can only increase the duration of the retention period. The retention period cannot be reduced or removed.
- Prevent deletion is disabled.
Important  
  
When Retention lock is enabled, only users with the`RETENTION_RULE_LOCK`privilege may increase the retention period. The following is true:
- No other backup modifications are permitted, except enabling or disabling Indefinite hold .
- Display-name changes, tag updates, and encryption-key rotations are blocked.
- Retention Lock cannot be disabled and the backup remains protected until its retention period expires.

## Prevent Deletion

Controls whether the backup can be deleted based on its retention and Prevent deletion settings.
Prevent deletion: The following options are available:
- No retention period: Enabling Prevent deletion prevents any user from deleting the backup.
- Configured retention period: Enabling Prevent deletion prevents deletion of the backup until the retention period is reached. The Prevent deletion option can be enabled or disabled.
- A configured retention period and Retention lock is enabled. Prevent deletion is disabled.
Important  
  
When enabled, only users with the`RETENTION_RULE_PREVENT_DELETION`privilege may increase or decrease the backup retention period.

## Indefinite Hold

Keeps this backup until the hold is removed. Overrides Prevent deletion and data retention settings.

Indefinite hold: When enabled, keeps the backup indefinitely until the hold is removed.
Important  
  
Users with the`RETENTION_RULE_INDEFINITE_HOLD`privilege may enable or disable indefinite hold on a backup.

## Update Backup

Select Update . The changes are saved.
- 

Use the[`oci bv backup update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/update.html)command and specify the`--volume-backup-id`parameter to edit a block volume backup:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`UpdateVolumeBackup`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/UpdateVolumeBackup)operation to update a block volume backup.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
