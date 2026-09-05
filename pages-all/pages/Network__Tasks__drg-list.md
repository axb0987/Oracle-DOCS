# Listing DRGs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm
- Fetched: 2026-09-05 02:44 CDT

# Listing DRGs

List the Dynamic Routing Gateways (DRGs) in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm#)
- 

- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .

The Dynamic routing Gateways list page opens. All DRGs in the selected compartment are displayed in a table.
- To view the DRGs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the DRGs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a DRG to open its details page, where you can view its status and perform other tasks.

To create a DRG, select Create dynamic routing gateway .

To perform other actions on a DRG directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that DRG:
- View details : Open the details page for the DRG.
- Copy OCID : Copy the OCID of the DRG to the clipboard.
- Manage tags : Add one or more tags to the DRG. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Move resource : See[Moving a DRG to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm).
- Terminate : See[Deleting a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm)
- 

Use the[network drg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/list.html)command and required parameters to list the DRGs in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListDrgs](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/ListDrgs)
