# Moving a Boot Volume Backup to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Moving a Boot Volume Backup to Another Compartment

Move a boot volume backup in the Block Volume service to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm#)
- 

- On the Boot Volume Backups list page, find the boot volume backup that you want to work with. If you need help finding the list page or the boot volume backup, see[Listing Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm).
- From the Actions menu (three dots) for the boot volume backup, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[`oci bv boot-volume-backup change-boot-volume-backup-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume-backup/change-compartment.html)command and specify the`--boot-volume-backup-id`and`--compartment-id`parameters to move the boot volume backup to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ChangeBootVolumeBackupCompartment`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/ChangeBootVolumeBackupCompartment)operation and specify the`bootVolumeBackupId`attribute in the request body and the`compartmentId`attribute in the[`ChangeBootVolumeBackupCompartmentDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/ChangeBootVolumeBackupCompartmentDetails)
