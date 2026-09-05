# Listing Block Volume Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Block Volume Backups

Learn how to list volume backups for a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volume Backups .

The Block Volume Backups list page opens. All volume backups in the selected compartment are displayed in a table.
- To view the volume backups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the volume backups in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a volume backup to open its details page, where you can view its status and perform other tasks.

To create a volume backup, see[Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm).
- 

Use the[`oci bv backup list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/list.html)command and specify the`--volume-backup-id`parameter to list volume backups:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ListVolumeBackups`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ListVolumeBackups)operation to and specify the`compartmentId`
