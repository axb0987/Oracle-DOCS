# Listing Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Volumes

View a list of the block volumes in your tenancy.

You can list all block volumes in a specific compartment. To view detailed information for a single volume, see[Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .

The Block Volumes list page opens. All block volumes in the selected compartment are displayed in a table.
- To view the block volumes in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the block volumes in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a block volume to open its details page, where you can view its status and perform other tasks.

To perform an action on a block volume directly from the list table, select an available option from the Actions menu in the row for that block volume:
- View details : Open the details page for the block volume.
- Edit :[Edit the block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm).
- Create Clone :[Clone the block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm).
- Create Manual Backup :[Manually back up the block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm).
- Assign master encryption key : Assign a master encryption key to the block volume. See[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm).
- Move resource :[Move the block volume to another compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm).
- Copy OCID : Copy the OCID of the block volume to the clipboard.
- Manage Tags : Add one or more tags to the block volume. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm).

To create a block volume, select Create block volume .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/list.html)oci bv volume list`command and required parameters to list the block volumes in your tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ListVolumes)ListVolumes`operation and specify the`compartmentId`
