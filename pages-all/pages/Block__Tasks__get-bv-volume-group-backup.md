# Retrieving a Volume Group Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Retrieving a Volume Group Backup

Learn how to retrieve information for a specified volume group backup.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-group-backup.htm#)
- 

On the Volume Group Backups list page, select the volume group backup that you want. If you need help finding the list page or the volume group backups, see[Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-volume-group-backup.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/get.html)oci bv volume-group-backup get`command and specify the`--volume-group-backup-id`parameter to retrieve information for that volume group backup:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/GetVolumeGroupBackup)GetVolumeGroupBackup`operation and specify the`volumeGroupBackupId`
