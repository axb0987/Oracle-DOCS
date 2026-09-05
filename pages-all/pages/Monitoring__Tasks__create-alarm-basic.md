# Creating a Basic Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm
- Fetched: 2026-09-05 02:38 CDT

# Creating a Basic Alarm

Create a basic alarm in Monitoring to notify you when metrics meet specified triggers.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
The Create Alarm page opens in Basic mode (the default view). The following steps describe how to create an alarm in Basic mode .
- Enter a user-friendly name for the alarm. Avoid entering confidential information.

This name is sent as the title for notifications related to this alarm, unless you specify a notification title ( Notification subject in the Console).

The subscription type determines the rendering of the alarm name or notification title.
- For email notifications, the name or notification title is part of the subject line.
- For HTTPS notifications, the name or notification title is the title field of the published message.
- For PagerDuty notifications, the name or notification title is used in the title field of the published message.
- For Slack messages, the name or notification title is part of the title.
- For SMS messages, the name or notification title is part of the message.
- (Optional) For Alarm summary , enter a custom alarm summary, using dynamic variables if you want.

The Alarm summary field corresponds to the`alarmSummary`alarm message parameter. For information about the parameter's default appearance in formatted messages, see[Alarm Message Format](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm).

Example with dynamic variables:
```

```

To look up dynamic variables for a parameter, see[Dynamic Variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm#alarm-parameters-dynamic).

You can disable HTML escaping by using the longer dynamic variable for an alarm parameter. For example, to render the value of the`query`parameter in the alarm message with HTML escaping disabled, enter the dynamic variable`{{{query}}}`.
- In the Metric description area, enter values to specify the metric to evaluate for the alarm.

- Compartment : Select the compartment that contains the resources that emit the metrics evaluated by the alarm. The selected compartment is also the storage location of the alarm. By default, the first accessible compartment is selected.
- Metric namespace : Select the service or application that emits the metrics for the resources that you want to monitor. The Metric namespace list shows metric namespaces for the selected compartment. For example, if the current compartment contains load balancers, then the list includes oci_lbaas .
- Resource group : Select the group that the metric belongs to. A[resource group](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__resourcegroupdefinition)is a custom string provided with a custom metric, and isn't applicable to service metrics.
- Metric name : Select the name of the metric that you want to evaluate for the alarm. You can select any OCI metric or custom metric if the data exists in the selected compartment and metric namespace.
- Interval : Select the aggregation window, or the frequency at which data points are aggregated. You can create a custom interval if needed. See also[Interval](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).
- Statistic : Select the function to use to aggregate the data points.
- Mean - The value of Sum divided by Count during the specified time period.
- Rate - The per-interval average rate of change.
- Sum - All values added together.
- Max - The highest value observed during the specified time period.
- Min - The lowest value observed during the specified time period.
- Count - The number of observations received in the specified time period.
- P50 - The value of the 50th percentile.
- P90 - The value of the 90th percentile.
- P95 - The value of the 95th percentile.
- P99 - The value of the 99th percentile.
- In the Metric dimensions area, specify optional filters to narrow the metric data that's evaluated.

- Dimension name : Select a qualifier that's specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.
- Dimension value : Select the value to use for the specified dimension. For example, if you selected`resourceId`as the dimension, select the resource identifier for the instance that you're monitoring.
- Additional dimension : Add another name-value pair for a dimension, as needed.
- Aggregate metric streams : Select this checkbox to return the combined value of all metric streams for the selected statistic.
- In the Trigger rule area, specify one or more conditions that must be satisfied for the alarm to be in the firing state. A condition can specify a threshold, such as 90% for CPU utilization, or an absence.

- For Operator , select the operator to use in the condition threshold. See[Predicate Operators](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#predicate).
- For Value , enter the value to use for the condition threshold. For the between and outside operators, enter both values for the range.
- For Trigger delay minutes , enter the number of minutes that the condition must be maintained before the alarm is in the firing state.
- For Alarm severity , select the perceived type of response required when the alarm is in the firing state for this condition (trigger rule).
- For Alarm body , enter the human-readable content of the notification for this condition (trigger rule).

We recommend providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Example: "High CPU usage alert. Follow runbook instructions for resolution." Optionally insert[dynamic variables](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)to render the value of associated[alarm message parameters](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm)in alarm messages. For example, insert`{{query}}`to render the value of`query`.
- To add another trigger rule (condition), select Additional trigger rule .
Note  
  
The chart under the Trigger rule section dynamically displays the last six hours of emitted metrics according to selected fields for the query. Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power). To switch views of data in the chart, see[Switching Table and Graph Views for an Alarm Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-chart-toggle-view.htm).
- In the Destination area under Define alarm notifications , select the provider of the destination to use for alarm notifications.

- Destination service : Select one of the following values:
- Notifications : Send alarm notifications to a[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition). Each[subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition)in the topic receives an[alarm message](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm).
- Streaming : Send[alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm)to a[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts).
Note  
  
If you expect more than 60 messages per minute, select Streaming . For more information, see[Alarm Message Limits](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits-alarm-messages).
- Compartment : Select the compartment that contains the resources that emit the metrics evaluated by the alarm. The selected compartment is also the storage location of the alarm. By default, the first accessible compartment is selected.
- Stream (for Streaming only): The[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#howstreamingworks)to use for alarm notifications.
- Topic (for Notifications only): The[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition)to use for notifications. Each topic supports one or more[subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition)protocols, such as PagerDuty.
- (Optional) Notification subject (for Notifications only): Custom notification title, using dynamic variables if you want.

Example with dynamic variables:
```

```

To look up dynamic variables for a parameter, see[Dynamic Variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-format.htm#alarm-parameters-dynamic).

You can disable HTML escaping by using the longer dynamic variable for an alarm parameter. For example, to render the value of the`query`parameter in the alarm message with HTML escaping disabled, enter the dynamic variable`{{{query}}}`.

The subscription type determines the rendering of the notification title (or alarm name, if notification title isn't specified).
- For email notifications, the name or notification title is part of the subject line.
- For HTTPS notifications, the name or notification title is the title field of the published message.
- For PagerDuty notifications, the name or notification title is used in the title field of the published message.
- For Slack messages, the name or notification title is part of the title.
- For SMS messages, the name or notification title is part of the message.
- To create a new topic (and a new subscription) in the selected compartment, select Create a topic and then enter the following values:
- Topic name : A user-friendly name for the topic. For example, enter: "Operations Team" for a topic used to notify operations staff of firing alarms. Avoid entering confidential information.
- Topic description : Description of the new topic.
- Subscription protocol : Medium of communication to use for the new topic. Select the type of subscription that you want to create, then enter values in the associated fields. For details about each subscription type, select the links.
- [Email : Enter an email address.
- [Function : Select the compartment and application that contain the function that you want, and then select the function.
- [HTTPS (Custom URL) : Enter the URL that you want to use as the endpoint.
- [PagerDuty : Enter the integration key portion of the URL for the PagerDuty subscription. (The other portions of the URL are hard-coded.)
- [Slack : Enter the Slack endpoint, including the webhook token.
- [SMS : Select the country for the phone number, and then enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en). Example: +14255550100
- For Message grouping , select one of the following options.

- Group notifications across metric streams : Collectively track metric status across all metric streams. Send a message when metric status across all metric streams changes.
- Split notifications per metric stream : Individually track metric status by metric stream. Send a message when metric status for each metric stream changes. For an example, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/split-messages.htm).
- For Message Format , select an option for the appearance of messages that you receive from this alarm (for Notifications only).

- Send formatted messages : Simplified, user-friendly layout. To view supported subscription protocols and message types for formatted messages (options other than Raw ), see[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
- Send Pretty JSON messages (raw text with line breaks) : JSON with new lines and indents.
- Send raw messages : Raw JSON blob.
- (Optional) To receive notifications at regular intervals when the alarm is firing, select Repeat notification? and then specify the period of time to wait before resending the notification. See[Best Practices for Your Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/alarmsbestpractices.htm).
- (Optional) To suppress evaluations and notifications for a specified length of time, select Suppress notifications . This option is useful for avoiding alarm notifications during system maintenance periods. Specify a start time, end time, and an optional description. See[Best Practices for Your Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/alarmsbestpractices.htm)and[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm).
- (Optional) To save the alarm without starting to evaluate metric data, clear the Enable this alarm? checkbox.
- (Optional) Add one or more tags to the alarm: Select Show advanced options to show the Add Tags section.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create alarm .

The Alarm Definitions page lists the new alarm. If the alarm is enabled, then Monitoring begins evaluating the configured metric, sending alarm messages when the metric data satisfies a trigger rule.
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)
