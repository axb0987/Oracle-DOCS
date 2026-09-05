# Listing Capture Filters
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm
- Fetched: 2026-09-05 02:43 CDT

# Listing Capture Filters

List the capture filters available in a particular compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#)
- 

- Open the navigation menu and select Networking . Under Network Command Center , select Capture filters .

The Capture filters list page opens. All capture filters in the selected compartment are displayed in a table.
- To view the capture filters in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the capture filters in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a capture filter to open its details page, where you can view its status and perform other tasks.

To create another capture filter, select Create capture filter .

To perform other actions on a capture filter directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that capture filter:
- View details : Open the details page for the capture filter.
- Copy OCID : Copy the OCID of the capture filter to the clipboard.
- Move resource : See[Moving a Capture Filter to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#top).
- Add tags : Add one or more tags to the capture filter. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View Tags : View the tags applied to the capture filter. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : See[Deleting a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#top)
- 

Use the[capture-filter list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/list.html)command and required parameters to list the capture filters in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListCaptureFilters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/ListCaptureFilters)
