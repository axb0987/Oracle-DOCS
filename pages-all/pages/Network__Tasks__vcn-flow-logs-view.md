# Listing and Viewing Flow Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm
- Fetched: 2026-09-05 02:47 CDT

# Listing and Viewing Flow Logs

List flow logs and view flow log configuration details from the Network Command Center.
You can view captured logging information from the Network Command Center, or from the[Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). This page documents how to view flow logs from the Network Command Center.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm#)
- 

- Open the navigation menu and select Networking . Under Network Command Center , select Flow logs .

The Flow logs list page opens. All flow logs in the selected compartment are displayed in a table.
- To view the flow logs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select the flow log to view details about its configuration
- To view the captured flow log data, select To view more logging data, click here .

For more information about flow log contents, examples, and limitations and other considerations, see[Details for VCN Flow Logs](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vcn_flow_logs.htm).

## Filtering List Results

Use filters to limit the flow logs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a flow log to open its details page, where you can view its status and perform other tasks. See[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)for more about logging and logs.

Use the buttons above the table to perform the following actions:
- Enable flow logs : See[Enabling Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm#vcn-flow-logs-enable).
- Edit :[Editing a Flow Log](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-update.htm#vcn-flow-logs-update).
- Delete : See[Deleting a Flow Log](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm#vcn-flow-logs-delete).

To perform other actions on a flow log directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that flow log:
- View details : Open the details page for the VCN.
- Copy OCID : Copy the OCID of the VCN to the clipboard.
- Move resource :[Move the VCN to another compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm).
- Add tags : Add one or more tags to the flow log. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete tags : Delete one or more tags from the flow log. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Deleting a Flow Log](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm#vcn-flow-logs-delete)
- 

Use the[oci logging log list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/list.html)command and required parameters to list the logs in a log group.

```

```

For a complete list of parameters and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListLogs](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSummary/ListLogs)
