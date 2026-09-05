# Getting an Alarm's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm
- Fetched: 2026-09-05 02:39 CDT

# Getting an Alarm's Details

Get details for an alarm in Monitoring.

## Before You Begin

IAM policies: To get alarm details, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[Get Alarm Details and History](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#get-alarm-history).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm#)
- 

On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
The details page opens and displays information about the alarm. Access the various resources associated with the alarm by selecting their links or tabs.
- 

Use the[oci monitoring alarm get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/get.html)command and required parameters to get details for an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[GetAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/GetAlarm)
