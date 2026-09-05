# Listing Cost Analysis Scheduled Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-list.htm
- Fetched: 2026-09-05 01:44 CDT

# Listing Cost Analysis Scheduled Reports

View the Cost Analysis scheduled reports in the tenancy in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-list.htm#)
- 

- Select the tenancy's home region.

Scheduled reports are stored in an Object Storage bucket in the tenancy's home region.

For instructions on switching regions, see[Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin).
- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Scheduled Reports .
The Scheduled reports page opens. All scheduled reports in the tenancy are displayed in a table.

## Filtering List Results

Use filters to limit the scheduled reports in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a scheduled report to open its details page, where you can view its status and perform other tasks.

To perform an action on a scheduled report directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that scheduled report:
- View details : Open the details page for the scheduled report.
- Edit :[Edit the scheduled report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-update.htm).
- Delete :[Delete the scheduled report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-delete.htm).

To[create a scheduled report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-create.htm), select Create a scheduled report .
- 

Use the[oci usage-api schedule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage-api/schedule/list.html)command and required parameters to list the Cost Analysis scheduled reports in the tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSchedules](https://docs.oracle.com/iaas/api/#/en/usage/latest/Schedule/ListSchedules)
