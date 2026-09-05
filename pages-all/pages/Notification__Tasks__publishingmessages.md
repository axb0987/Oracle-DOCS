# Publishing a Message to a Topic
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/publishingmessages.htm
- Fetched: 2026-09-05 02:49 CDT

# Publishing a Message to a Topic

Directly publish a message to a topic in Notifications.

Each message is broadcast to all subscriptions in the specified topic . Every message sent out as email contains a link to unsubscribe from the related topic.

Publish messages to function subscriptions to create automation. For example, see[Scenario A: Automatically Resizing VMs](https://docs.oracle.com/iaas/Content/Notification/Tasks/scenarioa.htm).

For important limits information, including message delivery rates by subscription type, see[Limits on Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#limits).

## Before You Begin

Meet the following prerequisites:
- Ensure that you have the correct IAM policies. See[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/manage-topic.htm#policies).
- You need an existing topic with at least one subscription. For details, see[Creating a Topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-topic.htm)and[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/manage-topic.htm#policies).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/publishingmessages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/publishingmessages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/publishingmessages.htm#)
- 

- On the Topics list page, find the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- From the Actions menu (three dots) for the topic, select Publish message .
- In the Publish message panel, enter the following information.

- Message : Enter the content that you want to send.
Note  
  
Message size limit per request: 64 KB.
- Title : Enter the title that you want to send.
- For email notifications, the title is used as the subject line of the message.
- For PagerDuty notifications, the title is used in the title field of the published message.
- HTTPS, Slack, and SMS notifications don't use titles.
- Select Publish .
- 

Use the[oci ons message publish](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/message/publish.html)command and required parameters to publish a message to a topic:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[PublishMessage](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/PublishMessage)operation to publish a message to a topic.

## Troubleshooting

For troubleshooting information related to published messages, see[Message Not Received](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm#msgno)
