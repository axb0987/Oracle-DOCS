# Overview of Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm
- Fetched: 2026-09-05 02:49 CDT

# Overview of Notifications

Use the Oracle Cloud Infrastructure Notifications service to set up communication channels for publishing messages using topics and subscriptions.

The Notifications service lets you know when something happens with your resources in Oracle Cloud Infrastructure. Using alarms, event rules, and connectors, you can get human-readable messages through supported endpoints, including email and text messages (SMS). You can also automate tasks through custom HTTPS endpoints and Oracle Cloud Infrastructure Functions. You can also directly publish messages.
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31657)to the service.

## How Notifications Works

The Notifications service enables you to set up communication channels for publishing messages using topics and subscriptions . When a message is published to a topic, the Notifications service sends the message to all of the topic's subscriptions.

[Standard header metadata](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#)

When delivering messages, Notifications appends the following header metadata.

For all messages:
- `Content-Type`
- `X-OCI-NS-MessageId`
- `X-OCI-NS-TopicOcid`
- `X-OCI-NS-TopicName`
- `X-OCI-NS-MessageType`
- `X-OCI-NS-UnsubscribeURL`

For confirmation messages:
Note  
  
See also[HTTPS (Custom URL) Confirmation URL](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/confirm-subscription.htm#https).
- `X-OCI-NS-ConfirmationURL`
- `X-OCI-NS-SubscriptionId`

For message signature validation:
- `X-OCI-NS-Signature`
- `X-OCI-NS-Timestamp`
- `X-OCI-NS-SignatureVersion`
- `X-OCI-NS-SigningCertURL`

When a subscriber's endpoint does not acknowledge receipt of the message, the Notifications service retries delivery. This situation can occur when the endpoint is offline. For example, the email server for an email address may be down.

[Delivery retry details](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#)

Notifications retries delivery following these steps until either (a) acknowledgement is received or (b) the subscription's retry duration is over. By default, the retry duration is two hours.
- Immediate retry.
- Exponential backoff retry for the period of the subscription's retry duration, using the following timing:
- 1 minute
- 2 minutes
- 4 minutes
- 8 minutes
- 16 minutes
- 32 minutes
- Discarding of the message at the end of the retry duration.

To change a subscription's retry duration, see[Updating a Subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/update-subscription.htm).

## Notifications Concepts

The following concepts are essential to working with Notifications. friendly formatting A setting to increase human readability of messages.

Supported subscription protocols:
- [Email](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts)

Supported message types:
- 

Alarm messages (when Notifications is the destination)

See[alarm message examples](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)and[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm).
- 

Connector messages (when Notifications is the target service)

See[connector message examples](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm)and[Updating a Connector to Use Friendly Formats](https://docs.oracle.com/iaas/Content/connector-hub/update-service-connector-friendly-format.htm). message The content that is published to a topic . Each message is delivered at least once per subscription . Every message sent out as email contains a link to unsubscribe from the related topic. notification A configuration for sending messages , such as an alarm or event rule. Each message is sent to subscriptions in the specified topic . The following types of notifications are available:
- 

Contextual notification : Created from a quick start template or focused options that are relevant to the given resource.

For instructions with a compute instance, see[Setting Up Contextual Notifications for an Instance](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/contextual-notifications-compute.htm).
- 

Traditional notification : Created from a[supported integration point](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#Flow).

Example scenarios for traditional notifications include[automatically resizing VMs](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/scenarioa.htm),[sending alarm messages to Slack and SMS](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/scenariob.htm), and[filing Jira tickets for reminders](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/scenarioc.htm). After creating the notification, you can manage it as usual. For example, if the notification is an alarm, manage it using the Alarms page in the Console. subscription An endpoint for a topic . Published messages are sent to each subscription for a topic . Supported subscription protocols:
- Email :

Sends an email message when you publish a message to the subscription's parent topic .
Note  
  
Follow best practices for integrating with Email Delivery. See[Maintain a Positive Email Sender Reputation](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationbestpractices.htm#email-reputation).
Message contents and appearance vary by message type. See[alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm),[event messages](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm), and[connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm).

Some message types use[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
- Function :
Runs the specified[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)when you publish a message to the subscription's parent topic . For example, runs a function to[resize VMs](https://docs.oracle.com/iaas/Content/Notification/Tasks/scenarioa.htm)when an associated alarm is triggered.
- HTTPS (Custom URL) :

Sends specified information when you publish a message to the subscription's parent topic .
- PagerDuty :
Creates a PagerDuty incident by default when you publish a message to the subscription's parent topic .
- Slack :
Sends a message to the specified Slack channel by default when you publish a message to the subscription's parent topic .
Message contents and appearance vary by message type. See[alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm),[event messages](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm), and[connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm).
- SMS :
Sends a text message using Short Message Service (SMS) to the specified phone number when you publish a message to the subscription's parent topic . Supported endpoint formats:[E.164 format](https://www.itu.int/rec/T-REC-E.164/en).
Note  
  

International SMS capabilities are required if SMS messages come from a phone number in another country. We continuously add support for more countries so that more users can receive SMS messages from local phone numbers.

SMS subscriptions are enabled only for messages sent by the following Oracle Cloud Infrastructure services: Announcements, Monitoring, and Connector Hub. SMS messages sent by unsupported services are dropped. See[Cause: Unsupported resource used for SMS](https://docs.oracle.com/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm#sms-unsupported-method).

The Notifications service delivers SMS messages from a preconfigured pool of numbers. You might receive SMS messages from multiple numbers. Message contents and appearance vary by message type. See[SMS alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm#sms)and[SMS connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm#top__sms).

Available Countries and Regions

You can use Notifications to send SMS messages to the following countries and regions:

Country or region ISO code
Australia`AU`
Brazil`BR`
Canada`CA`
Chile`CL`
China`CN`
Costa Rica`CR`
Croatia`HR`
Czechia`CZ`
France`FR`
Germany`DE`
Hungary`HU`
India`IN`
Ireland`IE`
Israel`IL`
Japan`JP`
Lithuania`LT`
Mexico`MX`
Netherlands`NL`
New Zealand`NZ`
Norway`NO`
Philippines`PH`
Poland`PL`
Portugal`PT`
Romania`RO`
Saudi Arabia`SA`
Singapore`SG`
South Africa`ZA`
South Korea`KR`
Spain`ES`
Sweden`SE`
Switzerland`CH`
Ukraine`UA`
United Arab Emirates`AE`
United Kingdom`GB`
United States`US`topic A communication channel for sending messages to subscriptions . Each topic name is unique across the tenancy.
Note  
  
Messages sent out as email by the Oracle Cloud Infrastructure Notifications service are processed and delivered through Oracle resources in U.S.-based regions.

## Flow of Message Publication and Delivery

Resources publish messages to the configured topic . Notifications then delivers messages to active subscriptions in the topic.

Resources that can send messages include alarms, announcement subscriptions, event rules, connectors, and[contextual notifications (alarms and event rules)](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/create-contextual-notification.htm). (A user, service, or app can also send a message through[direct publication](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/publishingmessages.htm).)

For example, consider an alarm configured to send messages to a topic. This topic contains email, Slack, and SMS subscriptions. When the alarm trigger rule is breached, the alarm publishes a message to the topic. Notifications then delivers the message to the topic's active subscriptions. In this example, the Slack subscription is pending because it hasn't been confirmed yet. Notifications delivers the message to the email and SMS subscriptions only, because these are the only active subscriptions in the topic.

For metrics that track published and delivered messages, see[Available Metrics: oci_notification](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Reference/notificationmetrics-reference.htm#Availabl).

### Alarms

When an alarm's trigger rule is breached, the alarm sends[an alarm message](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)to the configured topic . Notifications then delivers the message to active subscriptions in that topic. See[Managing Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm).

A[contextual notification](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/create-contextual-notification.htm)can include an alarm.

[

### Announcement Subscriptions

An[announcement subscription](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm)sends[console announcement messages](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm)to the configured topic . Notifications then delivers the message to active subscriptions in that topic.
[

### Event Rules

When triggered, an[event rule](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm#definitions)sends[an event message](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm)to the configured topic . Notifications then delivers the message to active subscriptions in that topic. See[Managing Rules for Events](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm).

A[contextual notification](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/create-contextual-notification.htm)can include an event rule.

[

### Connectors

A connector sends a[connector message](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm)to the configured topic . Notifications then delivers the message to active subscriptions in that topic. See[Managing Connectors](https://docs.oracle.com/iaas/Content/connector-hub/managingconnectors.htm).
[

### Direct Publication

A user (or a service or app) sends a message to the configured topic . Notifications then delivers the message to active subscriptions in that topic. See[Publishing a Message to a Topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/publishingmessages.htm).

[

## Creating Automation with Functions and Events

You can create automation by publishing messages to topics that include function subscriptions. For an example of a function subscription, see[Scenario A: Automatically Resizing VMs](https://docs.oracle.com/iaas/Content/Notification/Tasks/scenarioa.htm).

You can create also automation based on state changes of topics and subscriptions (Notifications resources) by using[event](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm)types, rules, and actions.

## Availability

The Notifications service is available in all Oracle Cloud Infrastructure commercial regions. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the[list](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About__The)of available regions, along with associated locations, region identifiers, region keys, and availability domains.

## Service Comparison for Sending Email Messages

Consider the following service features when deciding whether to use the Notifications service or the Email Delivery service to send your email messages. For more information about Email Delivery, see[Overview of the Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).

Service Feature Notifications service Email Delivery service
Requires confirmation before sending email. Yes No
Allows email decorations, such as signatures. Yes No
Allows raw email messages. No Yes
Supports MIME attachments. No

Yes
Supports special handling for failed email delivery. No

Yes
Priced for small messages (less than 32 KB, with a 64-KB limit). Yes No
Priced for large messages (greater than 32 KB, with a 2-MB limit). No Yes

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Ways to Access Notifications

You can access the Notifications service using the Console or the[Notifications REST API](https://docs.oracle.com/iaas/api/#/en/notification/latest/). Instructions for the Console, CLI, and API are included throughout this guide. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Console: To access Notifications using the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password. Open the navigation menu and select Developer Services . Under Application Integration , select Notifications .

API: To access Notifications through API, use[Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/).

CLI: See[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

Administrators: For common policies that give groups access to Notifications resources, see[IAM Policies (on the Securing Notifications page)](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm#iam-policies).

## Limits on Notifications

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

### Limits for Publishing Messages

All limits are per tenancy.

#### PublishMessage API Limits

Following are limits for the[PublishMessage](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/PublishMessage)API operation.

Limit type Limit amount
Message size per request 64 KB
Messages per minute (also known as Transactions Per Minute, or TPM) 60 per topic

#### Message Delivery Limits for Subscriptions

Following are message delivery rates by subscription type. During a traffic spike, the message delivery might be delayed or dropped for subscriptions where the delivery rate exceeds the threshold.

Subscription type Messages delivered per minute
Email 10
HTTP (any endpoint that begins with`http:`or`https:`60
Oracle Functions 60
Slack 60
SMS 6

## Security

Learn about security for Notifications.

Grant access to topics and subscriptions. See[Securing Notifications](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm)
