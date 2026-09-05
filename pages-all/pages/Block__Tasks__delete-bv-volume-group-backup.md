# Deleting a Volume Group Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Deleting a Volume Group Backup

Learn how to delete a volume group backup.

Important  
  
When you delete a volume group backup, all backups for the volumes included in the volume group backup are deleted.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-group-backup.htm#)
- 

- On the Volume Group Backups list page, select the volume group backup that you want. If you need help finding the list page or the volume group backups, see[Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-volume-group-backup.htm).
- From the Actions menu (three dots) for the volume group backup, select Terminate and confirm the selection when prompted.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/delete.html)oci bv volume-group-backup delete`command and specify the`--volume-group-backup-id`parameter to delete a volume group:

```

```

When you delete a volume group backup, all volume backups in the group are deleted.

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteVolumeGroupBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/DeleteVolumeGroupBackup)
