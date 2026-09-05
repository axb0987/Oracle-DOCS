# Formatting Messages for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm
- Fetched: 2026-09-05 02:40 CDT

# Formatting Messages for an Alarm

Update an alarm in Monitoring to send messages with friendly formatting or other format options.

For more information about friendly formatting, see[Friendly formatting (on the "Overview of Notifications" page)](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- On the Edit alarm page, under Message Format , select the formatting option that you want.
For friendly formatting, select Send formatted messages .
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm to use the message format option that you want:

```

```

The following example specifies friendly formatting:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm to use the message format option that you want.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set`messageFormat`to the option you want. For friendly formatting, set it to`ONS_OPTIMIZED`
