# Listing Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm
- Fetched: 2026-09-05 02:37 CDT

# Listing Logs

View a list of the logs contained in a log group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
The Logs list page opens. All logs in the selected log group are displayed in a table.
- To view the logs in a different compartment, select the Log group filter to switch compartments. You can also enter an OCID for any logs whose OCIDs match the value you entered.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the logs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a log to open its details page, where you can view its status and perform other tasks.

To perform an action on a log directly from the list table, select an available option from the Actions menu in the row for that log:
- Disable logging : Disable the log.
- Change log group : Move the log to a different log group.
- Edit :[Update the settings of the log.](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm)
- Delete :[Delete the log](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm).
- Manage tags : Add one or more tags to the log. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

To create a log, select Create custom log .
- 

Use the[oci logging log list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/list.html)command to list logs:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[/iaas/api/%23/en/logging-management/latest/LogSummary/ListLogs](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSummary/ListLogs)
