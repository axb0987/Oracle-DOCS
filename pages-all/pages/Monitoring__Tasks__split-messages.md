# Scenario: Split Messages by Metric Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm
- Fetched: 2026-09-05 02:40 CDT

# Scenario: Split Messages by Metric Stream

Walk through setting up an alarm to send a message for each metric stream. In this example, you want to be notified whenever a server exceeds a threshold. With this setup, you receive server-specific messages.
Caution  
  
With messages split by metric stream, consider the number of resources monitored by the alarm. If hundreds of resources simultaneously trigger the alarm to fire, then several messages are sent at the same time. Lots of messages can flood the phone (SMS), inbox (email), or other messaging endpoint, and some messages might be delayed because of service limits. For more information on limits and best practices, see[Alarm Message Limits](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#limits-alarm-messages).

## Required IAM Policy

This topic describes access requirements for the scenario.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're a member of the Administrators group, you already have the required access to complete this scenario.

Administrators: For common policies allowing users to manage alarms and create topics, see[Alarm Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#alarm-groups).

## Goal

The goal of this hypothetical scenario is to receive separate alarm messages per server. Let's say that you are monitoring 50 servers that emit a custom CPU utilization metric and you want to know if any exceed 80 percent CPU utilization. You want to receive a message whenever an individual server's metrics trigger the alarm.

## Setting Up This Scenario

Setup involves creating a threshold alarm enabled for metric stream-specific messages. In this hypothetical scenario, you select the custom metric`MyCustomCPUMetric`and the resource group`MyServerResourceGroup`.

You can complete these tasks in the Oracle Cloud Infrastructure Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- On the Create alarm page, under Define alarm , enter an Alarm name .

Example: Server-Specific Messages

Optionally change the Alarm severity and enter message text for Alarm body .
- Under Metric description , select the custom metric and define the query.

- Compartment : Select the compartment .
- Metric namespace : Select the namespace for the[custom metric](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
- Resource group :`MyServerResourceGroup`
- 

Metric name :`MyCustomCPUMetric`
Note  
  
Any OCI metric or custom metric can be selected.
- Interval : 1m
- Statistic : Count
- Skip Metric dimensions .
- Under Trigger rule , set the threshold to 80 and delay messages by 10 minutes:

- Operator : greater than
- Value : 80
- Trigger delay minutes : 10
- Under Set alarm notifications , Destination , provide the following values:

- Destination service : Notifications
- Compartment : Select the compartment containing the topic.
- Topic : Select the topic that you want to send notifications to. In this scenario, the topic already exists, and contains the subscriptions you want (SMS, email, and others).
This scenario uses a[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition)for alarm notifications. You can opt to use a[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts)instead, which is helpful when you expect a high volume of alarm notifications. For more information, see[Alarm Message Limits](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#limits-alarm-messages).
- Under Message grouping , select Split notifications per metric stream .
This option is required to receive a message for each metric stream.
- Select Repeat notification? and leave the default setting at 60 minutes.
Messages are sent every hour as long as the alarm is in`Firing`state for one or more metric streams.
- Select Save alarm .
Monitoring begins evaluating metrics for servers in the selected compartment, sending a single alarm message (per subscription) for each metric stream.
- 

Create the alarm using the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command. To configure the alarm for split messages by metric stream, set`--is-notifications-per-metric-dimension-enabled`to`true`.

[Example command](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm#)

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create the alarm. To configure the alarm for split messages by metric stream, set`isNotificationsPerMetricDimensionEnabled`to`true`.

[Example request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm#)

```

```
