# Scenario B: Sending Alarm Messages to Slack and SMS
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm
- Fetched: 2026-09-05 02:49 CDT

# Scenario B: Sending Alarm Messages to Slack and SMS

Set up automatic notifications to a Slack channel and an SMS phone number when alarms are triggered.

This scenario involves setting up a Slack endpoint for a channel and creating an alarm that sends a message to both that channel and an SMS phone number. When the alarm fires, the Notifications service sends the[alarm message](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)to the destination topic, which then fans out to the topic's subscriptions. In this scenario, the topic's subscriptions include the Slack channel and SMS phone number as well as your email address.

[

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're a member of the Administrators group, you already have the required access to execute this scenario. Otherwise, you need access to[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Authenti)and[Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Authenti).

## Task 1: Set up your Slack endpoint

[Create an incoming webhook to your Slack app](https://api.slack.com/messaging/webhooks#create_a_webhook).

Example of an incoming webhook to a Slack app (equivalent to the Slack endpoint for your subscription):`https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`

Once you set up your Slack endpoint, you can complete all other scenario steps in the Console. Alternatively, you can use the Oracle Cloud Infrastructure CLI or API, which lets you execute the individual operations yourself.

## Task 2: Create the Topic

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- 

Note  
  
Another Console workflow for this scenario involves creating a new topic and the first subscription when you[create the alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm), then[creating additional subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/create-subscription.htm)in that topic.

- Open the Create Topic panel: On the Topics list page, select Create topic . If you need help finding the list page, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- For Name , type the following: Alarm Topic
- Select Create .
- 

Use the[oci ons topic create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/create.html)command and required parameters to create a topic:

```

```

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateTopic](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/CreateTopic)operation to create a topic.

Example:
```

```

## Task 3: Create the Subscriptions

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- 

- Select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#create-topic)(example name was Alarm Topic ): On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- Create the Slack subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Slack .
- Fill in the remaining fields.

Field Description
URL

Type (or copy and paste) the Slack endpoint that you created earlier. Include the[webhook token](https://api.slack.com/incoming-webhooks#create_a_webhook).

Example endpoint:
```

```

- Select Create .
- Confirm the new Slack subscription: Navigate to the[confirmation URL](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm#slack)that was sent to Slack.
- Create the SMS subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select SMS .
- Fill in the remaining fields.

Field Description
Country Select the country for the phone number. See[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#prerequisites).
Phone Number Enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en).
- Select Create .
- Confirm the new SMS subscription: Follow the instructions[received on the phone](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm#sms).
- Create the email subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Email .
- Fill in the remaining fields.

Field Description
Email Type an email address.
- Select Create .
- [Confirm the new email subscription:](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)Open the email and navigate to the confirmation URL.
- 

Note  
  
After creating the subscriptions,[confirm them](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create each subscription:

```

```

Slack subscription example:

```

```

SMS subscription example:

```

```

Email subscription example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Note  
  
After creating the subscriptions,[confirm them](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create each subscription.

Slack subscription example:
```

```

SMS subscription example:
```

```

Email subscription example:
```

```

## Task 4: Create the Alarm

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#)
- 

- Open the Create Alarm page.
- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
- 

Select Create Alarm .
- For Alarm name , type the following: Utilization Alarm
- 

Under Metric description , select the metric, interval, and statistic.

Field Example value for this scenario
Compartment Select the compartment that contains the instance you want to monitor for high CPU utilization.
Metric namespace oci_computeagent
Metric name CpuUtilization
Interval 1m
Statistic Count
- 

Under Trigger rule , set up the alarm threshold.

Field Example value for this scenario
Operator greater than
Value 90
Trigger delay minutes 1
- Under Notifications , Destinations , select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#create-topic).

Field Example value for this scenario
Destination Service[Notifications Service
Compartment Select the compartment that contains[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#create-topic).
Topic Select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenariob.htm#create-topic).
- 

Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an alarm:

```

```

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an alarm.

Example:
```

```
