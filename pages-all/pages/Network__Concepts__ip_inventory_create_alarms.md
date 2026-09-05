# Creating Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_create_alarms.htm
- Fetched: 2026-09-05 02:41 CDT

# Creating Alarms

Create alarms and be notified when IP utilization of a subnet crosses a utilization threshold.

## Using the Console

- Open the navigation menu and select Networking . Under IP management , select IP Address Insights .
- Use filters to refine the search. You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources. For more information about the available filters, see[Viewing IP Address Insights](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm).
- Expand the name of the VCN that contains the subnet.
- Select the name of the subnet to open the subnet details page.
- On the Monitoring tab, select Create Alarm .

The Create alarm page opens.
- Enter a user-friendly name for the alarm. Avoid entering confidential information.
- For Alarm severity , select the perceived type of response required when the alarm is in the firing state.
- In the Metric description area, enter values to specify the metric to evaluate for the alarm.

- Metric name : Select the name of the metric that you want to evaluate for the alarm. You can select any OCI metric or custom metric if the data exists in the selected compartment and metric namespace.
- Interval : Select the aggregation window, or the frequency at which the alarm needs to be triggered.
- Statistic : Select the function to use to trigger the alarm.
- Rate : The per-interval average rate of change.
- Sum : All values added together.
- Mean : The value of Sum divided by Count during the specified time period.
- Min : The lowest value observed during the specified time period.
- Max : The highest value observed during the specified time period.
- Count : The number of observations received in the specified time period.
- P50 : The value of the 50th percentile.
- P90 : The value of the 90th percentile.
- P95 : The value of the 95th percentile.
- P99 : The value of the 99th percentile.
- In the Trigger rule area, specify the condition that must be satisfied for the alarm to be in the firing state. The condition can specify a threshold, such as 90% for CPU utilization, or an absence.

- Operator : Select the operator to use in the condition threshold.
- Value : Enter the value to use for the condition threshold. For the between and outside operators, enter both values for the range.
- Trigger delay in minutes : Enter the number of minutes that the condition must be maintained before the alarm is in the firing state.
- In the Topic and subscription area, specify the type of communication channel preferred to receive the alarm notification.

- Select the Create new topic option to create a new communication channel and subscription to receive alarm notifications. Select the Select existing topic to use an existing topic name and subscription.
- Select the compartment where the existing topic resides or where you want to create the new topic.
- Enter a topic name .
- In the Subscription area, select a preferred type of communication channel to receive the alarm notification under Subscription protocol and provide the respective email addresses, phone numbers, or slack channels.
- Expand Advanced options and provide the following optional information:

- 
- Alarm body : Enter the human-readable content of the notification for the trigger rule that you defined.

We recommend providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Example: "High CPU usage alert. Follow runbook instructions for resolution." Optionally insert[dynamic variables](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)to render the value of associated[alarm message parameters](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm)in alarm messages. For example, insert {{query}} to render the value of query.
- 
- Message format : Select an option for the appearance of messages that you receive from this alarm (for Notifications only).
- Send formatted messages : Simplified, user-friendly layout. To view supported subscription protocols and message types for formatted messages (options other than Raw ), see[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
- Send pretty JSON messages : JSON with new lines and indents.
- Send raw messages : Raw JSON blob.
- Repeat notification : To receive notifications at regular intervals when the alarm is firing, select this checkbox and then specify the period of time to wait before resending the notification. See[Best Practices for Your Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/alarmsbestpractices.htm).
- Suppress notification : To suppress evaluations and notifications for a specified length of time, select this checkbox. This option is useful for avoiding alarm notifications during system maintenance periods. Specify a start time, end time, and an optional description. See[Best Practices for Your Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/alarmsbestpractices.htm)and[Suppressing a Single Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm).
- Tags : (Optional) Add one or more tags to the alarm.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create alarm .
