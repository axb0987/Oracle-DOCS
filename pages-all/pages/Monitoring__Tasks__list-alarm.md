# Listing Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm
- Fetched: 2026-09-05 02:39 CDT

# Listing Alarms

List alarms in Monitoring.

## Before You Begin

IAM policies: To list alarms, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[List Alarms and Alarm Status](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#list-alarms-and-status).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
- To view the alarms in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the alarms in the list. Perform one of the following actions depending on the options that you see:
- To filter the list by alarm status, select a status value from the Status list.
- To filter the list by tag, select add under Tag filters .
- To search for an alarm by name, enter the name in the search box on the upper right.

## Actions

In the list table, select the name of an alarm to open its details page, where you can view its status and perform other tasks.

To create an alarm, select Create Alarm .

To perform an action on more than one alarm at a time, select the checkboxes next to the alarm names and then select an action from the Actions menu (three dots) above the table.
- 

Use the[oci monitoring alarm list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/list.html)command and required parameters to list alarms:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[ListAlarms](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmSummary/ListAlarms)
