# PagerDuty Integration Walkthrough
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm
- Fetched: 2026-09-05 02:49 CDT

# PagerDuty Integration Walkthrough

Learn how to integrate Oracle Cloud Infrastructure Notifications with PagerDuty so you can trigger PagerDuty incidents.

## Overview

Integrating with PagerDuty involves the following tasks.
- [Creating a PagerDuty endpoint](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#endpoint)
- [Creating a PagerDuty subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#sub)
- [Testing the subscription (optional)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#test)
- [Automatically triggering PagerDuty incidents](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#trigger)

## Create a PagerDuty Endpoint

To complete this procedure, you must have one of the following roles in PagerDuty: Manager, Admin, Global Admin, or Account owner base role.

- Go to PagerDuty.
- From the Configuration menu, select Services .
- On your Services page:
- If you are creating a service for your integration, select +Add New Service .
- If you are adding your integration to an existing service, select the name of the service you want to add the integration to. Then select the Integrations tab and select the +New Integration button.
- Type an Integration Name in the format`monitoring-tool-service-name`.

If you are creating a service for your integration, in Incident Settings, specify the Escalation Policy , Notification Urgency , and Incident Behavior for your new service.
- Select your preferred endpoint type from the Integration Type menu based on the following options:

- 

Oracle Cloud Infrastructure Monitoring : If you only want messages published by alarm (using[the alarm message format](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)). For this endpoint type, PagerDuty responds according to message format:
- Messages that use the generic message formats are ignored. For example, if your event rule triggers the publication of a message to the topic containing this subscription, or if you directly publish a message to the topic using the Notifications service, then no PagerDuty incident is created.
- Messages that use the alarm message format are processed. For example, if your alarm triggers publication of a message to the topic, which is in the alarm message format, then a PagerDuty incident is created.
- 

Custom Event Transformer : If you want any messages to generate a PagerDuty incident, whether they come from event rules, alarms, connectors,[console announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm), or direct publications. Messages sent to this endpoint follow the generic message format.

For more information about Custom Event Transformer , see[the PagerDuty documentation](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTc5-custom-event-transformer).
- Select the Add Service or Add Integration button to save your new integration.
You are redirected to the Integrations page for your service.
- Copy the Integration Key and the Integration URL for your new Integration and keep it in a safe place for later use.

Example of a PagerDuty Integration Key and Integration URL (at the time this document was published):
You now have the integration key needed to create a PagerDuty subscription in Notifications.

## Create a PagerDuty Subscription

To complete this procedure, you must have access to Notifications and permissions to create topics and subscriptions. See[Securing Notifications (IAM Policies)](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm#iam-policies).

- On the Topics list page, select Create topic . If you need help finding the list page, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- In the Create subscription panel, for Protocol , select PagerDuty .

The URL field is displayed with a space for you to add the integration key.

- 

Protocol : Select PagerDuty .
- 

URL : Type (or copy and paste) the integration key portion of the URL for your PagerDuty subscription. This portion is[the PagerDuty endpoint](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/pagerduty.htm#endpoint). (The other portions of the URL are hard-coded.)
- Select Create .

The PagerDuty subscription has been created. It remains in "Pending" status until confirmation is received.
- Confirm the new PagerDuty subscription:
- Go to PagerDuty.
- Access the incident titled "Oracle Notification Service Subscription Confirmation."
- Select the Confirmation URL link.

Example of confirmation incident (at the time this document was published) :
Now that you have a confirmed subscription that references your PagerDuty endpoint, you can test the integration by directly publishing a message to its parent topic.

## Test a PagerDuty Subscription (Direct Publish)

To complete this procedure, you must have access to Notifications and permissions to publish messages. See[Securing Notifications (IAM Policies)](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm#iam-policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#)
- 

- On the Topics list page, find the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- From the Actions menu (three dots) for the topic, select Publish message .
- In the Publish message dialog box, provide values for the following fields: enter the items required by your integration type.
- 

For Custom Event Transformer , enter a Message and Title .

Example Message: "Non-optimal utilization detected. An application or process may be consuming more CPU than usual."

Example Title: "Non-Optimal Alarm"
- 

For Oracle Cloud Infrastructure Monitoring, enter a Message containing a JSON blob with key-value pairs for`severity`(string, required) and one or more of the following:`title`(string),`body`(string), and`alarmMetaData`(JSON blob or array).
Example JSON blob:

```

```

The`severity`value is flexible for testing. For production, use a PagerDuty-supported value, such as`critical`,`error`,`warning`, or`info`.
- Select Publish .

A PagerDuty incident is triggered containing the content of your message.

Example of triggered PagerDuty incident (at the time this document was published):

Example of the content of a triggered PagerDuty incident (at the time this document was published):

You have confirmed that directly publishing a message triggers a PagerDuty incident. Next, use your new subscription to trigger PagerDuty incidents from alarms, events, and connectors.
Note  
  
To check the endpoint URL or other details of the PagerDuty subscription, see[Getting a Subscription's Details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm). For troubleshooting information related to published messages, see[Message Not Received](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm#msgno).
- 

Use the[oci ons message publish](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/message/publish.html)command and required parameters to publish a message to a topic:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[PublishMessage](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/PublishMessage)operation to publish a message to a topic.

Example request for a PagerDuty endpoint of the Custom Event Transformer type:
```

```

## Trigger a PagerDuty Incident

Trigger an incident in PagerDuty from an alarm, event, connector, or announcement subscription using a subscription in Notifications.

When creating an alarm, event rule, connector, or announcement subscription, select the Notifications topic that contains the PagerDuty subscription. For instructions on creating these resources, see the following documentation.
- [Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)
- [Creating an Events Rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm)
- [Creating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector.htm)
- [Creating an Announcement Subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm)
Note  
  
To check the endpoint URL or other details of the PagerDuty subscription, see[Getting a Subscription's Details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm)
