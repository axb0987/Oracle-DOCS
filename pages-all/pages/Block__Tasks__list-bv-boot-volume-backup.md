# Listing Boot Volume Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Boot Volume Backups

Learn how to list boot volumes for a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes . In the Block Storage menu on the sidebar, select Boot Volume Backups .

The Boot Volume Backups list page opens. All boot volume backups in the selected compartment are displayed in a table.
- To view the boot volume backups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the boot volume backups in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a boot volume backup to open its details page, where you can view its status and perform other tasks.

To perform an action on a boot volume backup directly from the list table, select an available option from the Actions menu in the row for that boot volume backup:
- View details : Open the details page for the boot volume backup.
- Edit name : Edit the name of the boot volume backup.
- Restore Boot Volume :[Restore boot volume contents to the snapshot when the backup was taken](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm).
- Assign master encryption key : Assigns a master encryption key to the boot volume backup. See[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm).
- Copy to Another Region :[Copy the boot volume backup to another region](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm).
- Move resource :[Move the boot volume backup to another compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm).
- Copy OCID : Copy the OCID of the boot volume backup to the clipboard.
- Copy backup source OCID : Copy the OCID of the source boot volume.
- Manage Tags : Add one or more tags to the boot volume backup. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the boot volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-boot-volume-backup.htm).

To create a boot volume backup, see[Creating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm).
- 

Use the`oci bv boot-volume-backup list`command specify the`--compartment-id`parameter to list boot volume backups:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ListBootVolumeBackups`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/ListBootVolumeBackups)operation and specify the`compartmentId`
