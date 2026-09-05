# Listing Log Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log-group.htm
- Fetched: 2026-09-05 02:37 CDT

# Listing Log Groups

View a list of the log groups in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log-group.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Log Groups .
The Log groups list page opens. All log groups in the selected compartment are displayed in a table.
- To view the log groups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the log groups in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a log group to open its details page, where you can view its status and perform other tasks.

To perform an action on a log group directly from the list table, select an available option from the Actions menu in the row for that log group:
- Move resource :[Move the log group to another compartment](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-log-group.htm).
- Edit :[Update the settings of the log group](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log-group.htm).
- Manage tags : Add one or more tags to the log group. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the log group](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log-group.htm).

To create a log group, select Create log group .
- 

Use the[oci logging log-group list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-group/list.html)command and required parameters to list the log groups in a compartment:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListLogGroups](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroupSummary/ListLogGroups)
