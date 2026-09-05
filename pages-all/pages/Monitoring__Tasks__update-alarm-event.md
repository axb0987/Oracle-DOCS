# Getting Event-Based Notifications for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-event.htm
- Fetched: 2026-09-05 02:40 CDT

# Getting Event-Based Notifications for an Alarm

Get notified every time your event-based metric is emitted.

An event-based metric indicates a point-in-time event, such as a user login or shutdown of a database. For example, consider an alarm for user logins. Let's say that Sandy logs in at 9:00 and Alex logs in at 9:05. Event-based notifications ensures that you get a notification for the 9:00 login, and another notification for the 9:05 login.

Configuring an alarm for event-based notifications consists of enabling repeat notifications with a frequency of zero minutes. Compare to[Repeating Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-repeat-notifications.htm). That notification configuration is based on the alarm's firing status instead of events. If the previous example alarm was configured for repeated notifications every minute, then you'd receive a notification every minute until the alarm[resets](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#reset).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-event.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-event.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-event.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- In the Metric description section of the Create Alarm page, select a metric namespace and metric name.
- Select Repeat notification? .
- For Notification frequency , specify 0 minutes.
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an event-based alarm. Set`--repeat-notification-duration`to`PT0M`(zero minutes).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an event-based alarm.

When defining details for[CreateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/CreateAlarmDetails), set`repeatNotificationDuration`to`PT0M`
