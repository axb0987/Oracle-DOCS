# Enabling an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-alarm.htm
- Fetched: 2026-09-05 02:39 CDT

# Enabling an Alarm

Enable an alarm in Monitoring.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-alarm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-alarm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-alarm.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Select Alarm is enabled .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to enable an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to enable an alarm.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set`isEnabled`to`true`
