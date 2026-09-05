# Using Dynamic Variables in Alarm Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm
- Fetched: 2026-09-05 02:40 CDT

# Using Dynamic Variables in Alarm Messages

Update an alarm in Monitoring to include values of alarm message parameters in messages.
See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

## How Dynamic Variables are Rendered

Note  
  
Insert dynamic variables that respect the maximum length for all supported use cases. Dynamic variables that exceed the maximum are considered invalid. For example, consider a dynamic variable for use in`title`. A supported use case for`title`is an email subject line, at a maximum length of 250 characters. In this case, the dynamic variable for a resource name (`{{dimensions.<dimension-name>}}`) is invalid because it's 256 characters and thus exceeds the maximum.

The value of an[alarm message parameter](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm)is rendered in an alarm message when you insert the associated dynamic variable into supported fields. For example, enter the following as the alarm body:
```

```

In the following image of an alarm message, the alarm body ( Body ) is rendered as: CRITICAL alarm triggered because threshold got breached due to [CpuUtilization[1m].mean():92] at 2023-08-15T19:51:00Z
[

Dynamic variables appear in notifications that contain body elements.
- If data is available for a dynamic variable, then the variable is resolved and data appears in its place. The previous example alarm message shows`[CpuUtilization[1m].mean():92]`in place of the dynamic variable`{{metricValues}}`.
- If no data is available for a dynamic variable, then the variable is unresolved and it appears as coded. For example, if no metric values are available for the dynamic variable`{{metricValues}}`, such as when the alarm is in the OK state, then the dynamic variable`{{metricValues}}`appears in the alarm message.
- SMS messages lack body elements, so dynamic variables aren't resolved.

## Looking Up Dynamic Variables

To look up a dynamic variable for a parameter, see[Dynamic Variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm#alarm-parameters-dynamic).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- On the Edit alarm page, find the field that you want to add dynamic variables to.

- Alarm body (`body`alarm message parameter): Rendered as a field within the body of the alarm message.
- Alarm summary (`alarmSummary`alarm message parameter): Rendered as a field within the body of the alarm message.
- Notification subject (`title`alarm message parameter): Rendering depends on the type of message. For a formatted email message, renders as the subject line. For a Slack message, renders as the title. For an SMS message, renders as part of the message.
Note  
  
Insert dynamic variables that respect the maximum length for all supported use cases. Dynamic variables that exceed the maximum are considered invalid. For example, consider a dynamic variable for use in`title`. A supported use case for`title`is an email subject line, at a maximum length of 250 characters. In this case, the dynamic variable for a resource name (`{{dimensions.<dimension-name>}}`) is invalid because it's 256 characters and thus exceeds the maximum.

For information about the default appearance of these alarm message parameters in formatted messages, see[Alarm Message Format](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm).
- Insert dynamic variables for the[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm)that you want.

Example with dynamic variables:
```

```

To look up dynamic variables for a parameter, see[Dynamic Variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm#alarm-parameters-dynamic).

You can disable HTML escaping by using the longer dynamic variable for an alarm parameter. For example, to render the value of the`query`parameter in the alarm message with HTML escaping disabled, enter the dynamic variable`{{{query}}}`.
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm to use dynamic variables in the field that you want:

```

```

With line breaks:
```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm to use the message format option that you want.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set the field that you want (`alarmSummary`,`body`, or`notificationTitle`
