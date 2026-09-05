# Grouping Notifications for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm
- Fetched: 2026-09-05 02:40 CDT

# Grouping Notifications for an Alarm

Update an alarm in Monitoring to group notifications.

Group notifications when you want alarm-level notifications. Compare to[Splitting Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

## When to Group Notifications

Following are reasons to group notifications.
- Get alarm-level notifications. No matter how many metric streams are firing at a particular time, receive only one notification.
- Suppress at the level of the alarm. See[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm)and[Removing a Suppression from a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm).

You can always view status at the level of the alarm, whether notifications are grouped or split. See[Listing Status of Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status.htm).

## Behavior of Grouped Notifications

In the following description of grouped notification behavior, consider an alarm with two[trigger rules](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm): a critical trigger rule for 95 percent and a warning trigger rule for 90 percent.
- When many metric streams fire at the same time, then only one (alarm-level) notification is sent.
- When the alarm isn't in firing status, and multiple trigger rules are breached at the same time (such as both the critical 95 percent trigger rule and the warning 90 percent trigger rule), then an alarm-level notification is sent for the highest-priority trigger rule only (such as critical 95 percent).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Message grouping section, select Group notifications across metric streams .
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm to send a message for each metric stream. Set`--is-notifications-per-metric-dimension-enabled`to`false`.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm to send a message for each metric stream.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set`isNotificationsPerMetricDimensionEnabled`to`false`
