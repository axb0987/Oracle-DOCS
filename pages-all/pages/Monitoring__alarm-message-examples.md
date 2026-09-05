# Example Alarm Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm
- Fetched: 2026-09-05 02:40 CDT

# Example Alarm Messages

View examples of alarm messages sent by Monitoring.

To render alarm parameters in the body of alarm messages, see[Using Dynamic Variables in Alarm Messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).

## Notifications Destination

Note  
  

To send alarm messages to an email address or other subscription type, select the topic that contains the subscription as the notification destination for the alarm. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm).

You can optionally[split messages by metric stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

### Email (Formatted)

Formatted email messages are sent for the following alarm configuration: Send formatted messages , for an Email subscription (available when the alarm destination is a topic, from the Notifications service).
Tip  
  

- To send email alarm messages, create an email subscription by selecting the option for a new topic during the alarm creation process. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm). Or create an email subscription separately in the Notifications service, and then select the parent topic when configuring the alarm. To create the subscription separately, see[Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm).
- To configure an alarm to send formatted messages, see[Formatting Messages for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm). For supported subscription protocols and message types, see[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting)).

The subject line of a formatted email message includes the following text and[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm):
```

```

Example subject line:
```

```

The bold heading at the top of a formatted email message is the same as its subject line.

The content of a formatted email message depends on the alarm configuration under Message grouping : Either Group notifications across metric streams (grouped example) or Split notifications per metric stream (split example).

Vertical and horizontal scrollbars are provided for the Dimensions and Metric values, ordered by dimension fields in formatted email messages (Mac only).

#### Grouped Example

The following example is for an alarm configured for Group notifications across metric streams (under Message grouping ). For this alarm configuration, all qualifying metric streams are identified in the message.
[

#### Split Example

The following example is for an alarm configured for Split notifications per metric stream (under Message grouping ). For this alarm configuration, a single metric stream is identified in the message. For more information about split messages, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).
[

### Email (Pretty JSON)

Pretty JSON email messages are sent for the following alarm configuration: Send Pretty JSON messages (raw text with line breaks) , for an Email subscription (available when the alarm destination is a topic, from the Notifications service).
Tip  
  

- To send email alarm messages, create an email subscription by selecting the option for a new topic during the alarm creation process. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm). Or create an email subscription separately in the Notifications service, and then select the parent topic when configuring the alarm. To create the subscription separately, see[Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm).
- To configure an alarm to send pretty JSON messages, see[Formatting Messages for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm). For supported subscription protocols and message types, see[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting)).

The subject line of a pretty JSON email message is the alarm name (`title`parameter). For descriptions of alarm message parameters, see[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm).

The content of a pretty JSON email message depends on the alarm configuration under Message grouping : Either Group notifications across metric streams (grouped example) or Split notifications per metric stream (split example).

#### Grouped Example

The following example is for an alarm configured for Group notifications across metric streams (under Message grouping ). For this alarm configuration, all qualifying metric streams are identified in the message.

```

```

#### Split Example

The following example is for an alarm configured for Split notifications per metric stream (under Message grouping ). For this alarm configuration, a single metric stream is identified in the message. For more information about split messages, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

```

```

### Email (Raw)

Raw email messages are sent for the following alarm configuration: Send raw messages , for an Email subscription (available when the alarm destination is a topic, from the Notifications service).
Tip  
  

- To send email alarm messages, create an email subscription by selecting the option for a new topic during the alarm creation process. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm). Or create an email subscription separately in the Notifications service, and then select the parent topic when configuring the alarm. To create the subscription separately, see[Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm).
- To configure an alarm to send raw messages, see[Formatting Messages for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-friendly-formats.htm).

The subject line of a raw email message is the alarm name (`title`parameter). For descriptions of alarm message parameters, see[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm).

The content of a raw email message depends on the alarm configuration under Message grouping : Either Group notifications across metric streams (grouped example) or Split notifications per metric stream (split example).

#### Grouped Example

The following example is for an alarm configured for Group notifications across metric streams (under Message grouping ). For this alarm configuration, all qualifying metric streams are identified in the message.

`{"dedupeKey": "exampleuniqueID","title": "High CPU Utilization","body": "Follow runbook at http://example.com/runbooks","type": "OK_TO_FIRING","severity": "CRITICAL","timestampEpochMillis": 1684337663852,"timestamp": "2023-05-17T15:34:23.852Z","alarmMetaData":[{"id": "ocid1.alarm.oc1.iad.exampleuniqueID","status": "FIRING","severity": "CRITICAL","namespace": "oci_computeagent","query": "CpuUtilization[1m].mean() > 90","totalMetricsFiring": 4,"dimensions":[{"instancePoolId": "Default","resourceDisplayName": "wordpress","faultDomain": "FAULT-DOMAIN-2","resourceId": "ocid1.instance.oc1.iad.exampleid","availabilityDomain": "sOZD:US-ASHBURN-AD-1","imageId": "ocid1.image.oc1.iad.exampleid","region": "us-ashburn-1","shape": "VM.Standard.E4.Flex"},{"instancePoolId": "Default","resourceDisplayName": "oke-0","faultDomain": "FAULT-DOMAIN-1","resourceId": "ocid1.instance.oc1.iad.exampleid","availabilityDomain": "sOZD:US-ASHBURN-AD-2","imageId": "ocid1.image.oc1.iad.exampleid","region": "us-ashburn-1","shape": "VM.Standard.E3.Flex"},{"instancePoolId": "Default","resourceDisplayName": "oke-2","faultDomain": "FAULT-DOMAIN-3","resourceId": "ocid1.instance.oc1.iad.exampleid","availabilityDomain": "sOZD:US-ASHBURN-AD-1","imageId": "ocid1.image.oc1.iad.exampleid","region": "us-ashburn-1","shape": "VM.Standard.E3.Flex"},{"instancePoolId": "Default","resourceDisplayName": "oke-1","faultDomain": "FAULT-DOMAIN-2","resourceId": "ocid1.instance.oc1.iad.exampleid","availabilityDomain": "sOZD:US-ASHBURN-AD-3","imageId": "ocid1.image.oc1.iad.exampleid","region": "us-ashburn-1","shape": "VM.Standard.E3.Flex"}],"alarmUrl":"https://cloud.oracle.com/monitoring/alarms/ocid1.alarm.oc1.iad.exampleid?region=us-ashburn-1","alarmSummary": "Alarm \"High CPU Utilization\" is in a \"FIRING\" state; because 4 metrics meet the trigger rule: \"CpuUtilization[1m].mean() > 90\", with a trigger delay of 1 minute"}],"metricValues":[{"CpuUtilization[1m].mean()":"92"},{"CpuUtilization[1m].mean()":"95"},{"CpuUtilization[1m].mean()":"93"},{"CpuUtilization[1m].mean()":"91"}]}],"notificationType": "Grouped messages across metric streams","version": 1.5}`

#### Split Example

The following example is for an alarm configured for Split notifications per metric stream (under Message grouping ). For this alarm configuration, a single metric stream is identified in the message. For more information about split messages, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

`{"dedupeKey": "exampleuniqueID","title": "High CPU Utilization","body": "Follow runbook at http://example.com/runbooks","type": "OK_TO_FIRING","severity": "CRITICAL","timestampEpochMillis": 1684337663852,"timestamp": "2023-05-17T15:34:23.852Z","alarmMetaData":[{"id": "ocid1.alarm.oc1.iad.exampleuniqueID","status": "FIRING","severity": "CRITICAL","namespace": "oci_computeagent","query": "CpuUtilization[1m].mean() > 90","totalMetricsFiring": 4,"dimensions":[{"instancePoolId": "Default","resourceDisplayName": "wordpress","faultDomain": "FAULT-DOMAIN-2","resourceId": "ocid1.instance.oc1.iad.exampleid","availabilityDomain": "sOZD:US-ASHBURN-AD-1","imageId": "ocid1.image.oc1.iad.exampleid","region": "us-ashburn-1","shape": "VM.Standard.E4.Flex"}],"alarmUrl":"https://cloud.oracle.com/monitoring/alarms/ocid1.alarm.oc1.iad.exampleid?region=us-ashburn-1","alarmSummary": "Alarm \"High CPU Utilization\" is in a \"FIRING\" state; because the resources with dimensions listed below meet the trigger rule: \"CpuUtilization[1m].mean() > 90\", with a trigger delay of 1 minute"}],"metricValues":[{"CpuUtilization[1m].mean()":"92"}]}],"notificationType": "Split messages per metric streams","version": 1.5}`

### Slack

Slack messages are sent when the alarm is configured for a topic that includes a Slack subscription.
Tip  
  
To send Slack alarm messages, create a Slack subscription by selecting the option for a new topic during the alarm creation process. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm). Or create a Slack subscription separately in the Notifications service, and then select the parent topic when configuring the alarm. To create the subscription separately, see[Creating a Slack Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm).

The title of a Slack message includes the following text and[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm):
```

```

The title is linked to the alarm.

Example Slack message title:
```

```

For descriptions of`title`,`body`, and other parameters, see[Alarm Message Format](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm).  
  

### SMS

SMS messages are sent when the alarm is configured for a topic that includes an SMS subscription.
Tip  
  
To send SMS alarm messages, create an SMS subscription by selecting the option for a new topic during the alarm creation process. See[Selecting a Topic as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm). Or create an SMS subscription separately in the Notifications service, and then select the parent topic when configuring the alarm. To create the subscription separately, see[Creating an SMS Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm).

An SMS message includes the following text and[alarm message parameters](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm):
```

```

Example SMS alarm message:  
  

Text in example SMS alarm message:
```

```

## Streaming Destination

The following example shows an alarm message sent when the alarm destination is a stream (Streaming service). In this example, the alarm is titled "High CPU Utilization" and continues to be in the FIRING state.
Tip  
  

To send alarm messages to a stream, select the stream as the notification destination for the alarm. See[Selecting a Stream as the Notification Destination for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm).

While the example shows line breaks, messages sent to streams are in raw JSON format (no line breaks).

For descriptions of`title`,`body`, and other parameters, see[Alarm Message Format](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm).
```

```
