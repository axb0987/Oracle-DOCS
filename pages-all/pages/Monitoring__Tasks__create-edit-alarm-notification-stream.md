# Selecting a Stream as the Notification Destination for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm
- Fetched: 2026-09-05 02:38 CDT

# Selecting a Stream as the Notification Destination for an Alarm

Select the stream to send alarm notifications to.

For an example of sending[alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm)to a[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts), see[Streaming Destination](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-examples.htm#streaming-destination). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Destination area under Define alarm notifications , provide the following values:

- Destination service : Select Streaming .
- Compartment : Select the compartment that contains the stream that you want. This compartment can be a different compartment than the one specified for the alarm and metric. By default, the first accessible compartment is selected.
- Stream : Select the stream that you want to use for alarm notifications.
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--destinations`parameter to select a stream as the alarm's notifications destination.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`destinations`
