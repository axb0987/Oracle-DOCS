# Moving a Block Volume Backup to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-backup-compartment-bv-volume-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Moving a Block Volume Backup to Another Compartment

Learn how to move a block volume backup in Block Volume to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-backup-compartment-bv-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-backup-compartment-bv-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-backup-compartment-bv-volume-backup.htm#)
- 

- On the Block Volume Backups list page, find the block volume backup that you want to work with. If you need help finding the list page or the block volume backup, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm).
- To view the block volume backups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu (three dots) for the block volume backup, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[`oci bv backup change-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/change-compartment.html)command and specify the`--compartment-id`and`--volume-backup-id`parameters to move a block volume backup to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ChangeVolumeBackupCompartment`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ChangeVolumeBackupCompartment)operation and specify the`volumeBackupId`attribute in the request body and the`compartmentId`attribute in the[`ChangeVolumeBackupCompartmentDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/ChangeVolumeBackupCompartmentDetails)
