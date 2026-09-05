# Best Practices for Subscriptions and Topics
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationbestpractices.htm
- Fetched: 2026-09-05 02:49 CDT

# Best Practices for Subscriptions and Topics

Review best practices for subscriptions and topics used with Oracle Cloud Infrastructure Notifications.

## Maintain a Positive Email Sender Reputation

When creating an[email subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__email), follow[Deliverability Best Practices](https://docs.oracle.com/iaas/Content/Email/Reference/deliverabilitybestpractices.htm#bestpractices)to maintain a positive email sender reputation. This practice can help you avoid being added to suppression lists. For more information about suppression lists, see[Managing the Suppression List](https://docs.oracle.com/iaas/Content/Email/Tasks/managingsuppressionlist.htm).

## Prevent Processing of Duplicate Items

An[alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#Flow)can trigger a message . The Notifications service then sends the message to[many types of subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptionprotocols), including email, HTTPS endpoints, and functions.

Depending on your goals, you might want to prevent your system from processing duplicate messages from a given message trigger. This situation is especially relevant when sending messages to function subscriptions, which can result in double invocations. (For an example of a function subscription, see[Scenario A: Automatically Resizing VMs](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/scenarioa.htm).)

To prevent your system from processing duplicate messages, write code that de-duplicates received messages by using identifiers specific to the trigger:
- For any message, consider using a custom de-dupe key entered in the body of the message.
- For[alarm](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#How)-triggered messages, use a combination of`dedupekey`and`timestampEpochMillis`from the[alarm message](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat).
- For[event](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm)-triggered messages, use`eventID`from the[event message](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm).
- For[directly published](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/publishingmessages.htm)messages, use`X-OCI-NS-MessageId`in the header (provided by Notifications). See[Standard header metadata](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm#hownw__header).

For handling duplicate requests sent to Oracle Cloud Infrastructure API endpoints, see[Retry Token](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#Retry).

For related troubleshooting information, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/../Tasks/troubleshootingnotifications.htm)
