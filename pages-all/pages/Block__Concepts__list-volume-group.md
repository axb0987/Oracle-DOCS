# Listing Volume Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Listing Volume Groups

List volume groups in the Block Volume service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Volume Groups .

The Volume Groups list page opens. All volume groups in the selected compartment are displayed in a table.
- To view the volume groups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the volume groups in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a volume group to open its details page, where you can view its status and perform other tasks.

To perform an action on a volume group directly from the list table, select an available option from the Actions menu in the row for that volume group:
- View details : Open the details page for the volume group.
- Edit name : Edit the name of the volume group.
- Create volume group backup :[Back up the volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-volume-group-backup.htm).
- Create volume group clone :[Clone the volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm)
- Move resource :[Move the volume group to another compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm).
- Copy OCID : Copy the OCID of the volume group to the clipboard.
- Manage Tags : Add one or more tags to the volume group. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm).

To create a volume group, select Create volume group .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/list.html)oci bv volume-group list`command and required parameters to list volume groups:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ListVolumeGroups)ListVolumeGroups`operation and specify the`compartmentId`
