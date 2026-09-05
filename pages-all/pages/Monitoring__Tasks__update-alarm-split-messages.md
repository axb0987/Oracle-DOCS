# Splitting Notifications for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm
- Fetched: 2026-09-05 02:40 CDT

# Splitting Notifications for an Alarm

Update an alarm in Monitoring to split notifications.

Split notifications when you want metric stream-level notifications. Compare to[Grouping Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

## When to Split Notifications

Following are reasons to split notifications.
- Get a notification for each firing metric stream.
- Suppress at the level of a metric stream. See[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm)and[Removing a Suppression from a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm).
- View status at the level of a metric stream. See[Listing Metric Stream Status in an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm).
- You can always view status at the level of the alarm, whether notifications are grouped or split. See[Listing Status of Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status.htm).

For a scenario of split notifications with examples, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

## Behavior of Split Notifications

In the following description of split notification behavior, consider an alarm with two[trigger rules](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm): a critical trigger rule for 95 percent and a warning trigger rule for 90 percent.
- When many metric streams fire at the same time, then a notification is sent for each firing metric stream and associated trigger rule.
- When the metric stream isn't in firing status, and multiple trigger rules are breached at the same time (such as both the critical 95 percent trigger rule and the warning 90 percent trigger rule), then an metric stream-level notification is sent for the highest-priority trigger rule only (such as critical 95 percent).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Message grouping section, select Split notifications per metric stream .
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm to send a message for each metric stream. Set`--is-notifications-per-metric-dimension-enabled`to`true`.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm to send a message for each metric stream.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set`isNotificationsPerMetricDimensionEnabled`to`true`
