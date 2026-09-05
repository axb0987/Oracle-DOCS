# Deleting an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm.htm
- Fetched: 2026-09-05 02:39 CDT

# Deleting an Alarm

Delete an alarm in Monitoring.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm.htm#)
- 

- On the Alarm Definitions list page, find the alarms that you want to work with. If you need help finding the list page or the alarms, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Select the checkbox for each alarm that you want to delete.
- Go to Actions and select Delete alarms .
- Confirm the deletion.
The deleted alarms are removed from the compartment and are no longer displayed on the Alarm Definitions page.
- 

Use the[oci monitoring alarm delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/delete.html)command and required parameters to delete an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[DeleteAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/DeleteAlarm)
