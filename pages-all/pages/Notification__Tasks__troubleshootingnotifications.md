# Troubleshooting Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm
- Fetched: 2026-09-05 02:50 CDT

# Troubleshooting Notifications

Use troubleshooting information to identify and address common issues that can occur while working with Notifications.

See also[Known Issues for Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../known-issues.htm).

## Message Not Received

Troubleshoot a missing message for a subscription.

A message you expected at a subscription was never received. The[flow of message delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow)didn't happen the way you thought it would. For example, you didn't get an email when a compute instance exceeded an alarm threshold.

Following are possible causes and remedies for this issue.

### Cause: Trigger not satisfied

The trigger configured for the message-sending resource might not have been satisfied in the time range you were looking for it. (The resource that sends the message could be[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow).)

For example, consider an alarm configured for a 90% threshold at a one-hour interval. Perhaps the most recent evaluation occurred before the compute instance exceeded the threshold. How to diagnose

Review history of the message-sending resource and compare findings to the topic's[published and delivered messages](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Reference/notificationmetrics-reference.htm#Availabl).
- 

Note the time when the trigger condition occurred.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm)for the resource to determine the time.

For example, you might[view metric charts for a Compute instance](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#view_default_metric_charts_for_compute_instance)and find that it exceeded the threshold defined in the alarm at 10:01.
- Find the related timestamp as recorded by the associated resource (alarm, event rule, or connector).
- 

For an alarm: Look for relevant alarm state transitions close to the time of the trigger condition.
Tip  
  
Assess alarms and messages using their unique identifiers. See[Prevent Processing of Duplicate Items](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationbestpractices.htm#duplicate). To view the format used by alarm messages, see[Message Format and Examples](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat).

[View alarm history.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm)A transition found around that time indicates that the alarm might have sent the message you're missing. An absence of transitions indicates that the alarm didn't send any messages. If you expected the alarm to transition, review its configuration.
- 

For an event rule: Look for matching events that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the event rule. See the Events Matched chart. A matching event around that time indicates that the event rule might have sent the message you're missing. An absence of matching events indicates that the event rule didn't send any messages. If you expected the event rule to detect a matching event, review its configuration.
- 

For a connector: Look for written messages that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the connector. See the Messages written to target chart. A written message around that time indicates that the connector might have sent the message you're missing. An absence of written messages indicates that the connector didn't send any messages. If you expected the connector to write a message, review its configuration.
- 

In the subscription's parent topic, look for message publish and delivery times that are close to the related timestamp from the previous step.

[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Published Messages Total Count and Delivered Messages Count metric charts. A published message that wasn't delivered could indicate an issue with the subscription's endpoint. How to fix

You can remedy this situation for future trigger conditions. Update the trigger configuration of the message-sending resource so that the trigger is satisfied when you expect it to be.

For example, update an alarm to use a shorter interval.

Following are instructions for updating message-sending resources:
- Announcements:[Updating an Announcement Subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)
- Alarms:[Updating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm.htm)
- Event rules:[Editing an Events Rule](https://docs.oracle.com/iaas/Content/Events/Task/update-events-rule.htm)
- Connectors:[Updating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/update-service-connector.htm)

### Cause: Resource didn't send message

The message-sending resource might not have sent the message to Notifications. (The resource that sends the message could be[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow).)

For example, you might expect an email for an event, while the event rule was accidentally configured for a different event. How to diagnose

Review history of the message-sending resource and compare findings to the topic's[published and delivered messages](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Reference/notificationmetrics-reference.htm#Availabl).
- 

Note the time when the trigger condition occurred.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm)for the resource to determine the time.

For example, you might[view metric charts for a Compute instance](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#view_default_metric_charts_for_compute_instance)and find that it exceeded the threshold defined in the alarm at 10:01.
- Find the related timestamp as recorded by the associated resource (alarm, event rule, or connector).
- 

For an alarm: Look for relevant alarm state transitions close to the time of the trigger condition.
Tip  
  
Assess alarms and messages using their unique identifiers. See[Prevent Processing of Duplicate Items](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationbestpractices.htm#duplicate). To view the format used by alarm messages, see[Message Format and Examples](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat).

[View alarm history.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm)A transition found around that time indicates that the alarm might have sent the message you're missing. An absence of transitions indicates that the alarm didn't send any messages. If you expected the alarm to transition, review its configuration.
- 

For an event rule: Look for matching events that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the event rule. See the Events Matched chart. A matching event around that time indicates that the event rule might have sent the message you're missing. An absence of matching events indicates that the event rule didn't send any messages. If you expected the event rule to detect a matching event, review its configuration.
- 

For a connector: Look for written messages that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the connector. See the Messages written to target chart. A written message around that time indicates that the connector might have sent the message you're missing. An absence of written messages indicates that the connector didn't send any messages. If you expected the connector to write a message, review its configuration. How to fix

You can remedy this situation for future trigger conditions. For example, update an event rule to match on the intended event.

Following are instructions for updating message-sending resources:
- Announcements:[Updating an Announcement Subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)
- Alarms:[Updating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm.htm)
- Event rules:[Editing an Events Rule](https://docs.oracle.com/iaas/Content/Events/Task/update-events-rule.htm)
- Connectors:[Updating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/update-service-connector.htm)

### Cause: Incorrectly configured subscription

The subscription might be incorrectly configured.

For example, an email subscription's endpoint might not match the expected email address, or a Slack subscription's endpoint might not include the correct webhook.

One indicator of an incorrectly configured subscription is a published message that doesn't get delivered. How to diagnose

[Get the subscription's details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm)and review configuration. For example, compare the endpoint of an email subscription to the expected email address.

Review history of the message-sending resource and compare findings to the topic's[published and delivered messages](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Reference/notificationmetrics-reference.htm#Availabl).
- 

Note the time when the trigger condition occurred.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm)for the resource to determine the time.

For example, you might[view metric charts for a Compute instance](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#view_default_metric_charts_for_compute_instance)and find that it exceeded the threshold defined in the alarm at 10:01.
- Find the related timestamp as recorded by the associated resource (alarm, event rule, or connector).
- 

For an alarm: Look for relevant alarm state transitions close to the time of the trigger condition.
Tip  
  
Assess alarms and messages using their unique identifiers. See[Prevent Processing of Duplicate Items](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationbestpractices.htm#duplicate). To view the format used by alarm messages, see[Message Format and Examples](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat).

[View alarm history.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm)A transition found around that time indicates that the alarm might have sent the message you're missing. An absence of transitions indicates that the alarm didn't send any messages. If you expected the alarm to transition, review its configuration.
- 

For an event rule: Look for matching events that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the event rule. See the Events Matched chart. A matching event around that time indicates that the event rule might have sent the message you're missing. An absence of matching events indicates that the event rule didn't send any messages. If you expected the event rule to detect a matching event, review its configuration.
- 

For a connector: Look for written messages that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the connector. See the Messages written to target chart. A written message around that time indicates that the connector might have sent the message you're missing. An absence of written messages indicates that the connector didn't send any messages. If you expected the connector to write a message, review its configuration.
- 

In the subscription's parent topic, look for message publish and delivery times that are close to the related timestamp from the previous step.

[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Published Messages Total Count and Delivered Messages Count metric charts. A published message that wasn't delivered could indicate an issue with the subscription's endpoint. How to fix You can remedy this situation for future trigger conditions.
- If the subscription is pending,[confirm it](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).
- If the subscription is incorrectly configured,[recreate it with correct configuration](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm). We recommend[deleting the incorrectly configured subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm).

### Cause: Dropped message

Notifications dropped the message received from[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow)that was intended for a subscription. This issue can occur when the subscription is pending or incorrectly configured. How to diagnose

In the subscription's parent topic, look for dropped function messages.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Failed Messages Count metric chart, and note the value of the metric dimension`endpointType`("ORACLE_FUNCTIONS" for a dropped function message). When a dropped function message exists, the counter of this metric chart increments, showing "ORACLE_FUNCTIONS" for`endpointType`. How to fix You can remedy this situation for future trigger conditions.
- If the subscription is pending,[confirm it](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).
- If the subscription is incorrectly configured,[recreate it with correct configuration](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm). We recommend[deleting the incorrectly configured subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm).

### Cause: The subscription isn't active

For example, a Slack subscription is in pending status because of a lack of confirmation. How to diagnose[Get the subscription's details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm)to confirm active status. If you can't find the subscription, it might have been deleted. How to fix You can remedy this situation for future trigger conditions. Either[confirm the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)to activate it, or if you can't find it,[recreate the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm).

### Cause: Unsupported resource used for SMS

SMS messages might not be enabled for the message-sending resource. SMS subscriptions are enabled only for messages sent by the following Oracle Cloud Infrastructure services: Announcements, Monitoring, and Connector Hub. See[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#prerequisites).

For example, consider an event rule configured to send messages to a topic. The topic contains an email subscription and an SMS subscription. However, SMS messages aren't enabled for the Events service. In this case, the SMS message is dropped. How to diagnose

In the subscription's parent topic, look for dropped SMS messages.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Failed Messages Count metric chart, and note the value of the metric dimension`endpointType`("SMS" for a dropped SMS message). For example, if an unsupported resource sends an SMS message to a topic containing an SMS subscription, then the SMS message is dropped. The counter of this metric chart increments, showing "SMS" for`endpointType`. How to fix You can remedy this situation for future trigger conditions. Create a message-sending resource that is enabled for sending SMS messages:
- Alarms:[Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)
- Announcements:[Creating an Announcement Subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm)
- Connectors:[Creating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector.htm)

### Cause: International SMS capabilities are missing

The SMS message might be sent to or from an unsupported locale. International SMS capabilities are required if SMS messages come from a phone number in another country. How to diagnose Confirm that you have the ability to send and receive SMS messages to and from other countries. We continuously add support for more countries so that more users can receive SMS messages from local phone numbers. See[SMS](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#concepts__sms). How to fix You can remedy this situation for future trigger conditions. Get international SMS capabilities.

### Cause: Suppressed email address

An email message might not be delivered if the email address is on a suppression list.

Reasons for suppression include bounce codes and user complaints. For more information, see[Managing the Suppression List](https://docs.oracle.com/iaas/Content/Email/Tasks/managingsuppressionlist.htm). How to diagnose

In the subscription's parent topic, look for dropped email messages.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Failed Messages Count metric chart, and note the value of the metric dimension`endpointType`("EMAIL" for a dropped email message). For example, if the email address is on a suppression list, then the email message is dropped. The counter of this metric chart increments, showing "EMAIL" for`endpointType`. How to fix

Update Your Distribution Lists: Ensure all recipient addresses are correct and active. Remove any invalid, obsolete, or misspelled addresses from your lists and aliases. Don’t resend emails to addresses that have hard bounced or reported spam, unless you have corrected the cause. For help with avoiding suppression lists in the future, see[Maintain a Positive Email Sender Reputation](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationbestpractices.htm#email-reputation).

If the domain’s mail server isn't configured correctly or has bugs, fix these before retrying. For example, returning hard bounce codes for valid email addresses results in valid recipients being suppressed. See also[Deleting an Email Address from Suppression List](https://docs.oracle.com/iaas/Content/Email/Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm).

### Cause: Monitoring permissions lacking for compartment

If your topic is in an[Oracle Platform Services managed compartments (named "ManagedCompartmentForPaas")](https://docs.oracle.com/iaas/Content/General/Reference/PaaSprereqs.htm#resources), then the Monitoring service might not have permissions to use it, and alarm messages sent to that topic might not be received. How to diagnose

[Get the topic's details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-topic.htm)to determine if its compartment is an Oracle Platform Services managed compartments (named "ManagedCompartmentForPaas"). How to fix You can remedy this situation for future trigger conditions. For more details, including steps for resolution, see[Alarm messages are not received in Oracle Platform Services managed compartments](https://docs.oracle.com/iaas/Content/Monitoring/known-issues.htm#paas-alarms-not-received).

## Subscription Disappeared

Identify events that might have caused a subscription to disappear.

A[subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#concepts__subscriptiondefinition)that you accessed before is no longer available.

The subscription was removed, either through explicit deletion or an unsubscription event (a call to[GetUnsubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/GetUnsubscription)).

### Remedy: Identify unsubscription and deletion events

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Audit .
- Select the compartment that contains the subscriptions that you want to monitor.
- Filter for unsubscription and deletion events by providing the following values.

- Filter by time : Select Custom .
- Start Date : Select the start date for the search window.
- End Date : Select the end date for the search window.
- Request action types : Select DELETE .
Note  
  
To filter for older unsubscription and deletion events, select GET (used for messages before July 18, 2023).
- Resource : Select ons-subscription .
- Event type : Select the following items:
- `com.oraclecloud.notification.GetUnsubscription`
- `com.oraclecloud.notification.DeleteSubscription`
Matching events are listed under Explore events .
- To determine if an event is related to the missing subscription, expand it to review its log data.
Example`message`for an unsubscription event:`"GetUnsubscription succeeded. Subscription removed from topic ocid1.onstopic.oc1.iad.exampleid"`
- (Optional) Select Export log data (JSON) to export the listed events.
For more information about using audit events, see[Audit Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm).

### Remedy: Send a notification for any unsubscription event

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- Select a compartment.
- Select Create Rule .
- On the Create Rule page, enter a friendly name and description. Avoid entering confidential information.
- Under Rule Conditions , provide the following values.

- Condition : Select Event Type .
- Service Name : Select Notifications .
- Event Type : Select Subscription - Get Unsubscription .
- Under Actions , provide the following values:

- Action Type : Select Notifications .
- Notifications Compartment : Select the compartment that contains the topic that you want to use for event messages.
- Topic : Select the topic that you want to use for event messages.
- Select Create Rule .

## Function Not Invoked or Run

Troubleshoot a function that didn't get invoked or didn't run as expected through a subscription.

The function configured in a function subscription either didn't get invoked or didn't run. The[flow of message delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow)for the function didn't happen the way you thought it would. For example, the configured function didn't[resize a VM when it exceeded memory](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm).

Following are possible causes and remedies for this issue.

### Cause: Resource didn't send message

The message-sending resource might not have sent the message to Notifications. (A message-sending resource could be[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow).)

For example, you might expect an event rule to send a message to the configured topic because an event occurred. However, the event rule might be accidentally configured for a different event that didn't happen. How to diagnose

Review history of the message-sending resource and compare findings to the topic's[published and delivered messages](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Reference/notificationmetrics-reference.htm#Availabl).
- 

Note the time when the trigger condition occurred.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm)for the resource to determine the time.

For example, you might[view metric charts for a Compute instance](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#view_default_metric_charts_for_compute_instance)and find that it exceeded the threshold defined in the alarm at 10:01.
- Find the related timestamp as recorded by the associated resource (alarm, event rule, or connector).
- 

For an alarm: Look for relevant alarm state transitions close to the time of the trigger condition.
Tip  
  
Assess alarms and messages using their unique identifiers. See[Prevent Processing of Duplicate Items](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationbestpractices.htm#duplicate). To view the format used by alarm messages, see[Message Format and Examples](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat).

[View alarm history.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm)A transition found around that time indicates that the alarm might have sent the message you're missing. An absence of transitions indicates that the alarm didn't send any messages. If you expected the alarm to transition, review its configuration.
- 

For an event rule: Look for matching events that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the event rule. See the Events Matched chart. A matching event around that time indicates that the event rule might have sent the message you're missing. An absence of matching events indicates that the event rule didn't send any messages. If you expected the event rule to detect a matching event, review its configuration.
- 

For a connector: Look for written messages that are close to the time of the trigger condition.

[View default metric charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)for the connector. See the Messages written to target chart. A written message around that time indicates that the connector might have sent the message you're missing. An absence of written messages indicates that the connector didn't send any messages. If you expected the connector to write a message, review its configuration. How to fix

You can remedy this situation for future trigger conditions. For example, update an event rule to match on the intended event.

Following are instructions for updating message-sending resources:
- Announcements:[Updating an Announcement Subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm)
- Alarms:[Updating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm.htm)
- Event rules:[Editing an Events Rule](https://docs.oracle.com/iaas/Content/Events/Task/update-events-rule.htm)
- Connectors:[Updating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/update-service-connector.htm)

### Cause: Dropped message

Notifications dropped the message received from[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow)that was intended for a function subscription. This issue can occur when the subscription is pending or incorrectly configured. How to diagnose

In the subscription's parent topic, look for dropped function messages.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Failed Messages Count metric chart, and note the value of the metric dimension`endpointType`("ORACLE_FUNCTIONS" for a dropped function message). When a dropped function message exists, the counter of this metric chart increments, showing "ORACLE_FUNCTIONS" for`endpointType`. How to fix You can remedy this situation for future trigger conditions.
- If the subscription is pending,[confirm it](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).
- If the subscription is incorrectly configured,[recreate it with correct configuration](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm). We recommend[deleting the incorrectly configured subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm).

### Cause: Function wasn't invoked

The function wasn't invoked even though Notifications delivered the message received from[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow). How to diagnose
Note  
  

The Notifications service has no information about a function after it's invoked.

If this is the first invocation, response might be delayed.
- Confirm Notifications delivery: In the subscription's parent topic, confirm that Notifications delivered the message to the function.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Delivered Messages Count metric chart, and note the value of the metric dimension`endpointType`("ORACLE_FUNCTIONS" for a delivered function message). When a function message is delivered, the counter of this metric chart increments, showing "ORACLE_FUNCTIONS" for`endpointType`.
- In the function, look for invocation and run times that are close to the time when the trigger condition occurred.
- [View the function's default metric charts](https://docs.oracle.com/iaas/Content/Functions/Reference/functionsmetrics.htm#Using_the_Console). Specifically, view both the Invocations and Duration metric charts. An absence of data points close that timestamp indicates that the function wasn't invoked or run.
- [View the function's service logs](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm). How to fix If the function was never invoked, then[contact Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

### Cause: Function wasn't run

The function wasn't run even though it was invoked after Notifications delivered the message received from[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow). How to diagnose
Note  
  

The Notifications service has no information about a function after it's invoked.

If this is the first invocation, response might be delayed.
- Confirm Notifications delivery: In the subscription's parent topic, confirm that Notifications delivered the message to the function.[View the topic's default metric charts.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-resource.htm)Specifically, view the Delivered Messages Count metric chart, and note the value of the metric dimension`endpointType`("ORACLE_FUNCTIONS" for a delivered function message). When a function message is delivered, the counter of this metric chart increments, showing "ORACLE_FUNCTIONS" for`endpointType`.
- In the function, look for invocation and run times that are close to the time when the trigger condition occurred.
- [View the function's default metric charts](https://docs.oracle.com/iaas/Content/Functions/Reference/functionsmetrics.htm#Using_the_Console). Specifically, view both the Invocations and Duration metric charts. A data point in Invocations that doesn't have a matching occurrence in Duration indicates that the function was invoked but not run.
- [View the function's service logs](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm). How to fix See[Troubleshooting OCI Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionstroubleshooting.htm).

## HTTPS (Custom URL) Subscription Confirmation Not Received

Troubleshoot a missing confirmation message for a new HTTPS (Custom URL) subscription.

The new HTTPS (Custom URL) subscription remains in Pending status after you[send the confirmation](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

The subscription never received the confirmation. The endpoint for the HTTPS (Custom URL) subscription never received the confirmation because the subscription's endpoint doesn't satisfy[prerequisites for HTTPS (Custom URL) subscriptions . For example, the endpoint isn't publicly accessible, or it doesn't support the unauthorized header requirement.

To remedy this issue, create a new subscription with an endpoint that satisfies prerequisites.

- Find an endpoint that satisfies[prerequisites for HTTPS (Custom URL) subscriptions .
- Using the selected endpoint,[create a new HTTPS (Custom URL) subscription .
- [Confirm the new subscription.](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)
We recommend[deleting the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm)
