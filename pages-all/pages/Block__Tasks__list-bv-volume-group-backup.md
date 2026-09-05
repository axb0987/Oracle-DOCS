# Listing Volume Group Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Volume Group Backups

Learn how to list volume group backups in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-backup.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Volume Group Backups .

The Volume Group Backups list page opens. All volume group backups in the selected compartment are displayed in a table.
- To view the volume group backups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the volume group backups in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a volume group backup to open its details page, where you can view its status and perform other tasks.

To perform an action on a volume group backup directly from the list table, select an available option from the Actions menu in the row for that volume group backup:
- View Details : Open the details page for the volume group backup.
- Edit name : Edit the name of the volume group backup.
- Restore volume group :[Restore a volume group from the volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm).
- Copy to Another Region :[Copy the volume group to another region](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm).
- Move resource : Move the volume group backup to another compartment.
- Copy OCID : Copy the OCID of the volume group backup to the clipboard.
- Copy original volume group OCID : Copy the OCID of the original volume group to the clipboard.
- Manage Tags : Add one or more tags to the volume group backup. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-group-backup.htm).

To create a volume group backup, see[Creating a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-group-backup.htm).
- 

Use the[`oci bv volume-group-backup list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-backup/list.html)command and specify the`--compartment-id`parameter to view the volume group backup backups in that compartment:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/ListVolumeGroupBackups)ListVolumeGroupBackups`operation and specify the`compartmentId`
