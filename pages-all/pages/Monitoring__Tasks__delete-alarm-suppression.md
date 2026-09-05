# Removing a Suppression from a Single Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm
- Fetched: 2026-09-05 02:39 CDT

# Removing a Suppression from a Single Alarm

Remove a suppression of an alarm in Monitoring. For example, if the alarm has an existing (expired) alarm-wide suppression, remove it so you can add another one. An alarm can have only one alarm-wide suppression at a time.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

See also[Removing Suppressions from Multiple Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression-multiple.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- On the alarm details page, select Edit alarm suppression .
- In the Edit alarm suppression panel, select X for the alarm suppression that you want to remove.
- When prompted, select Remove suppression .
- 

Use the[oci monitoring alarm-suppression delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-suppression/delete.html)command and required parameters to delete an alarm suppression:

```

```

Note  
  
You can alternatively use the[oci monitoring suppression remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/suppression/remove.html)command. A dimension-specific suppression can't be removed with this command.

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[DeleteAlarmSuppression](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmSuppression/DeleteAlarmSuppression)operation to delete a dimension-specific alarm suppression.
Note  
  
You can alternatively use the[RemoveAlarmSuppression](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Suppression/RemoveAlarmSuppression)
