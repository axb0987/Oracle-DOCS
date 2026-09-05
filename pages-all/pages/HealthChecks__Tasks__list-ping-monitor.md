# Listing Ping Monitors
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Ping Monitors

List ping monitors in Health Checks.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Health Checks .
The Health checks list page opens. All HTTP and ping monitors in the selected compartment and region are displayed in a table.
- To view the HTTP and ping monitors in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the health checks in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a ping monitor to open its details page, where you can view its status and perform other tasks.

To perform an action on a ping monitor directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that ping monitor:
- Edit :[Update the ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/update-ping-monitor.htm#top).
- Enable :[Enable the ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm#top).
- Disable :[Disable the ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-ping-monitor.htm#top).
- Duplicate :[Duplicate the ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/duplicate-ping-monitor.htm#top).
- Copy OCID : Copy the OCID of the ping monitor to the clipboard.
- Move resource :[Move the ping monitor to another compartment](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm#top).
- Manage Tags : Add one or more tags to the ping monitor. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Add tags : Add one or more tags to the ping monitor. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View tags : View existing tags for the ping monitor. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/delete-ping-monitor.htm#top).

To[create a ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#top), select Create health check and select Ping for Request type .

To delete more than one monitor at a time, select the checkboxes next to the health check names and then select Delete .
- 

Use the[oci health-checks ping-monitor list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/ping-monitor/list.html)command and required parameters to list ping monitors:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ListPingMonitors](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitorSummary/ListPingMonitors)
