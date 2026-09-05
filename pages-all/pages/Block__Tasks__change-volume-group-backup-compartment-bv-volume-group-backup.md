# Moving a Volume Group Backup to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Moving a Volume Group Backup to Another Compartment

Move a volume group backup in the Block Volume service to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm#)
- 

- On the Volume Group Backups list page, find the volume group backup that you want to work with. If you need help finding the list page or the volume group backups, see[Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-volume-group-backup.htm).
- From the Actions menu (three dots) for the volume group backup, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[`oci bv volume-group-backup change-volume-group-backup-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/change-compartment.html)command and specify the`--volume-group-backup-id`and`--compartment-id`parameters to move a volume group backup to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ChangeVolumeGroupBackupCompartment`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/ChangeVolumeGroupBackupCompartment)operation to and specify the`volumeGroupBackupId`attribute in the request body and the`compartmentId`attribute for the`ChangeVolumeGroupBackupCompartmentDetailsReference`
