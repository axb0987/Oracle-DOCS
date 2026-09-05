# Copying a Volume Group Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Copying a Volume Group Backup

Learn how to copy a volume group backup.

For more information about copying volume backups and volume group backups to new regions, including required permissions, see[Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm#)
- 

- On the Volume Group Backups list page, select the volume group backup that you want. If you need help finding the list page or the volume group backups, see[Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-volume-group-backup.htm).
- From the Actions menu (three dots) for the volume group backup, select Copy to Another Region .
- In the Copy volume group backup panel, enter the following information.

- Name : Enter a name for the backup. Avoid entering confidential information.
- Compartment : Select the compartment that you want to copy the volume group backup to.
- Destination Region : Select the region that you want to copy the volume group backup to.
- Encryption : Select whether you want the volume group backup to use the Oracle-provided encryption key or your own Vault encryption key. If you select the option to use your own key, paste the OCID for encryption key from the destination region.
- Select Copy Volume Group Backup .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/copy.html)oci bv volume-group-backup copy`command and specify the`--destination-region`and`--volume-group-backup-id`parameters to copy a volume group backup:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CopyVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/CopyVolumeGroupBackup)operation to and specify the volumeGroupBackupId and destinationRegion attributes in the[CopyVolumeGroupBackupDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CopyVolumeGroupBackupDetails)
