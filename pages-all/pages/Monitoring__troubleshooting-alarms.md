# Troubleshooting Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/troubleshooting-alarms.htm
- Fetched: 2026-09-05 02:40 CDT

# Troubleshooting Alarms

Use troubleshooting information to identify and address common issues that can occur while working with alarms in Monitoring.

Before troubleshooting, ensure that you understand how alarms are evaluated. See[Illustration of Alarm Evaluation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#illustration-eval).

## Alarm Doesn't Fire

The alarm met the condition for firing, but it didn't fire. For example, a compute instance went down.

### Cause: Long trigger delay

The alarm expression didn't evaluate to true for consecutive minutes in the trigger delay period.

The following image of an alarm's metric chart includes a shaded area to indicate the trigger delay period. In this example, the alarm summary shown on the alarm details page is`Alarm fires when the Mean of CpuUtilization is greater than the threshold value of 80, with a trigger delay of 10 minutes`. The trigger delay starts at 1:30 (when the threshold is exceeded) and ends at 1:40. The alarm expression evaluates to true at 1:30, then evaluates to false at 1:32. This true evaluation doesn't continue for the full ten-minute trigger delay period, so the alarm doesn't fire.  
  

To view the metric chart for an alarm,[get its history](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm).

For more information about how alarms are evaluated, see[Illustration of Alarm Evaluation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#illustration-eval).

### Remedy: Shorten the trigger delay

If the trigger delay is too long, and you want the alarm to fire immediately after breaching the threshold, then update the alarm to use a shorter trigger delay. For example, set the trigger delay to one minute. See[Defining the Trigger Delay for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-delay.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm).

### Cause: Interval is shorter than the emission frequency

The alarm expression evaluated to true, causing the alarm to fire, but at the next interval, even though the last data point exceeded threshold, the alarm cleared. The alarm cleared because the interval is shorter than the frequency of emission for the selected metric.

The following image of an alarm's metric chart shows hourly data points for the selected metric,`StoredBytes`, from the`oci_object_storage`metric namespace. The alarm query is`StoredBytes[1m].sum() > 800000000`, which specifies a one-minute interval. This interval is shorter than the metric's emission frequency, which is one hour. (The frequency is documented at[Object Storage Metrics](https://docs.oracle.com/iaas/Content/Object/Reference/objectstoragemetrics.htm).)  
  

In this example, the alarm fires at 3:00 and clears at 3:01. If the interval had been set to one hour, then the alarm expression would continue evaluating to true, and alarm would continue firing, until 4:00.

To view the metric chart for an alarm,[get its history](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm).

For more information about how alarms are evaluated, see[Illustration of Alarm Evaluation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#illustration-eval).

### Remedy: Increase the interval

If you want the alarm to fire, then update the alarm interval to be the same or longer than the metric's emission frequency. For example, for the`StoredBytes`metric, update the alarm interval to at least one hour, if you want the alarm to fire at 3:01 and continue firing until 4:00 in the previous example. See[Selecting the Interval for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm).

### Cause: Wrong dimensions

The alarm expression didn't evaluate to true when a resource met the condition defined in the alarm because the resource was filtered out using dimensions.

For example, consider an alarm with dimensions selected for availability domain 1. The resource that met the condition is in availability domain 2. Alarm evaluation considers only resources that match the specified dimensions.

### Remedy: Update dimensions

Either remove the dimensions, or update them to include the resource. See[Selecting Dimensions for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-dimensions.htm).

### Cause: Wrong query

Common examples:

- The alarm query might specify the metric`MemoryUtilization`when you meant to select`CpuUtilization`.
- The alarm query might specify the statistic`mean()`when instead you want the alarm to monitor the sum of data points in an interval (`sum()`).

To check the query for an alarm,[get its details](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm).

For information about query elements, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm). For more information about how alarms are evaluated, see[Illustration of Alarm Evaluation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#illustration-eval).

### Remedy: Update the query
[Update the alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-basic.htm)to specify the metric that you want. To edit the MQL directly, see[Editing the MQL Expression When Updating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-mql.htm).

### Cause: The alarm is disabled

### Remedy: Enable the alarm

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm).

Note  
  
These steps are for the Console. For complete instructions, see[Enabling an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-alarm.htm).
- On the alarm's details page, select Alarm is enabled .

## Alarm Doesn't Send a Notification

When the alarm fires, it doesn't send a notification.

### Cause: The alarm or dimension is suppressed

### Remedy: Remove the suppression

See[Removing a Suppression from a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm)and[Removing Suppressions from Multiple Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression-multiple.htm).

### Cause: Subscription isn't part of the configured topic

For example, let's say that you aren't getting alarm messages in your in-box. The topic specified for the alarm might not have an email subscription for the email address that you want.

To check if the topic includes the expected subscription, see[Getting a Topic's Details](https://docs.oracle.com/iaas/Content/Notification/Tasks/get-topic.htm).

### Remedy: Update topic to include subscription

See[Creating a Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription.htm).

You could also update the alarm to reference a new topic and subscription, or an existing topic that includes the subscription that you want. See[Selecting a Topic as Notification Destination for an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm).

## Alarm Sends Too Many Notifications

When the alarm fires, it sends more notifications than expected.

### Cause: Repeat notifications are enabled

The alarm is configured to repeat alarm notifications when the alarm keeps firing without interruption.

### Remedy: Disable repeat notifications

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm).

Note  
  
These steps are for the Console. For complete instructions, see[Repeating Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-repeat-notifications.htm).
- Go to Actions and then select Edit alarm .
- Under Define alarm notifications , clear the Repeat notification? checkbox.
- Select Save alarm .

### Cause: Split notifications are enabled

The alarm is configured to send a notification for each metric stream that fires. For example, if 50 metric streams fire, then the alarm sends 50 notifications. This is expected behavior for split notifications. See[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/split-messages.htm).

For example, the following image shows an alarm metric chart with two metric streams that exceed the threshold at 1:30, causing the alarm to fire.  
  

Following is the alarm message sent for the compute instance with the metric value of 87.
[

Following is the alarm message sent for the compute instance with the metric value of 95.
[

To view the metric chart for an alarm,[get its history](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm).

If you didn't intend for the alarm to send a notification for each firing metric stream, then consider updating the alarm to group notifications instead. See[When to Group Notifications](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm#when). After this update, the alarm sends a single notification when the alarm fires, regardless of the number of metric streams that are firing.

## Alarm Resets

The[alarm history](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm)shows a RESET transition state.

An alarm resets to stop checking for an absent metric that triggered the Firing state. For more information, see[About the Internal Reset Period](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset).

## Alarm Doesn't Save (404 Error)

When trying to save a new or updated alarm, you see a 404 error preventing the creation or update of the alarm.

### Cause: Insufficient policies

A 404 error indicates that you don't have the required IAM policies.

### Remedy: Obtain required policies
See[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Alarm Fires and Clears Continually

Troubleshoot an alarm that keeps switching between`Firing`and`OK`status values.

Either the[alarm interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm)is too small or the[trigger delay](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-delay.htm)is too large (or both). The resource emits the specified metric at a greater frequency than the alarm interval.

For example, consider the metric`DatabaseAvailability`, which is emitted every 5 minutes.

API request (relevant portions):
```

```

Console configuration:

Field Value
Metric namespace[`oci_autonomous_database`](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-monitor-metrics.html#GUID-7850ED5B-0291-44CB-84D3-EC952C4A6C50)
Metric name`DatabaseAvailability`
Interval 1 minute
Statistic Mean
Trigger rule
- Operator : absent
- Trigger delay minutes :`3`
Message grouping Group notifications across metric streams Example: Alarm Switches Status

Following is an example of an alarm's status switching between`Firing`and`OK`status values from 1:00 to 1:08. Note the`OK`status at 1:01, 1:02, 1:06, and 1:07. At these times, the alarm evaluation results met the condition for the one-minute interval, but the status change was internally pending because of the three-minute trigger delay. The alarm status changed to`Firing`at 1:03 and 1:08 because three consecutive evaluations met the condition.

Time Value in metric chart* Alarm condition met? Alarm status
1:00`0`No`OK`
1:01`1`Yes. Status change is internally pending`OK`
1:02`1`Yes. Status change is internally pending`OK`
1:03`1`Yes`Firing`
1:04`1`Yes`Firing`
1:05`0`No`OK`
1:06`1`Yes. Status change is internally pending`OK`
1:07`1`Yes. Status change is internally pending`OK`
1:08`1`Yes`Firing`

*For value in metric chart,`0`means the metric is present while`1`means the metric is absent. For an example metric chart, see[Creating an Absence Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm).

To remedy this situation, update the following alarm configuration:

- Alarm interval to be equal to or greater than the frequency of the metric emission. See[Selecting the Interval for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm).
- Trigger delay to accommodate latency. See[Defining the Trigger Delay for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-delay.htm).

For example, update the interval to 10 minutes and update the trigger delay to 1 minute.

API request (relevant portions):
```

```

Console configuration:

Field Value
Metric namespace[`oci_autonomous_database`](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-monitor-metrics.html#GUID-7850ED5B-0291-44CB-84D3-EC952C4A6C50)
Metric name`DatabaseAvailability`
Interval 10 minutes
Statistic Mean
Trigger rule
- Operator : absent
- Trigger delay minutes :`1`
Message grouping Group notifications across metric streams Example: Metric is Present, Alarm is`OK`In this example, the metric is present at the expected times (every five minutes): 2:00, 2:05, and 2:10. At each time, the alarm evaluates for presence of the metric during the last ten minutes. The alarm's status remains`OK`for the listed times.

Time Value in metric chart* Alarm condition met? Alarm status
2:00`0`No`OK`
2:01`1`No`OK`
2:02`1`No`OK`
2:03`1`No`OK`
2:04`1`No`OK`
2:05`0`No`OK`
2:06`1`No`OK`
2:07`1`No`OK`
2:08`1`No`OK`
2:09`1`No`OK`
2:10`0`No`OK`
2:11`1`No`OK`*For value in metric chart,`0`means the metric is present while`1`means the metric is absent. For an example metric chart, see[Creating an Absence Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm). Example: Metric is Absent, Alarm is`Firing`In this example, the metric is present at 2:00, but absent at 2:05 and 2:10. Because the alarm interval is ten minutes, the alarm condition wasn't met at 2:05. At 2:10 the alarm changes to`Firing`status because the alarm condition is met (zero metrics were present for the ten-minute interval).

Time Value in metric chart* Alarm condition met? Alarm status
2:00`0`No`OK`
2:01`1`No`OK`
2:02`1`No`OK`
2:03`1`No`OK`
2:04`1`No`OK`
2:05`1`No`OK`
2:06`1`No`OK`
2:07`1`No`OK`
2:08`1`No`OK`
2:09`1`No`OK`
2:10`1`Yes`Firing`
2:11`1`Yes`Firing`*For value in metric chart,`0`means the metric is present while`1`means the metric is absent. For an example metric chart, see[Creating an Absence Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm)
