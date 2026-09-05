# Listing VTAPs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm
- Fetched: 2026-09-05 02:48 CDT

# Listing VTAPs

List all Virtual Test Access Point (VTAPs) in a compartment.

See[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm)for more information and a feature overview.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#)
- 

- Open the navigation menu and select Networking . Under Network Command Center , select VTAPs .

The VTAPs list page opens. All capture filters in the selected compartment are displayed in a table.
- To view the VTAPs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the VTAPs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a VTAP to open its details page, where you can view its status and perform other tasks.

To create another VTAP, select Create VTAP .

To perform other actions on a VTAP directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that VTAP:
- View details : Open the details page for the capture filter.
- Copy OCID : Copy the OCID of the capture filter to the clipboard.
- Move resource : See[Moving a VTAP to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm#top).
- Add tags : Add one or more tags to the VTAP. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View Tags : View the tags applied to the VTAP. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : See[Deleting a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-delete.htm#top)
- 

Use the[vtap list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/list.html)command and required parameters to list all VTAPs in a compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVtaps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/ListVtaps)
