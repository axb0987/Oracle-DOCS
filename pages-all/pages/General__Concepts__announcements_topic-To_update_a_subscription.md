# Updating an Announcement Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm
- Fetched: 2026-09-05 02:10 CDT

# Updating an Announcement Subscription

You can update an active subscription by changing its name, description, or Notifications topic.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_update_a_subscription.htm#)
- 

- On the Subscriptions list page, find the subscription you want to update, and then select the subscription name. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- Select Edit .
- (Optional) Select Name , and then update the subscription name. Avoid entering confidential information.
- (Optional) Select Description , and then update the description. Avoid entering confidential information.
- (Optional) Under Display preferences , select Time zone , and then select the time zone that you prefer for announcement time stamps.
- (Optional) Select Language , and then select the language that you prefer for displaying announcements delivered by email. By default, the language is set to whatever you configured in the Console language selector.
- (Optional) Under Notifications topic , do one of the following:
- To use an existing Notifications topic, select Use existing topic , and then select a topic from the selected compartment. (If needed, to list resources in a different compartment, select Compartment and select a compartment.)
- To create a new Notifications topic, select Create new topic , and then provide the following:

Option Description
Compartment Select the compartment where you want to create the topic.
Name Enter a name for the topic. (Avoid entering confidential information.)
Description Enter a description for the topic. (Avoid entering confidential information.)
- Under Subscription , select Subscription protocol , and then select the protocol used by subscription endpoints. The information you must provide about the subscription endpoint depends on the protocol.
- Do one of the following:
- If you selected Email , then select Email address and enter a valid email address. For more information, see[Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm).
- If you selected Function , then specify the Oracle Cloud Infrastructure Functions application and function by selecting an Oracle Functions application and then Function . (If needed, select Function compartment to list resources in a different compartment.) For more information, see[Creating a Function Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-function.htm).
- If you selected HTTPS custom URL , then select URL and enter a valid HTTPS URL. For more information, see[Creating an HTTPS (Custom URL) Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-https.htm).
- If you selected PagerDuty , select URL and enter a valid PagerDuty URL. For more information, see[Creating a PagerDuty Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-pagerduty.htm).
- If you selected Slack , select URL and enter the URL of a valid Slack channel. For more information, see[Creating a Slack Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm).
- If you selected SMS , specify a Country and Phone Number . For more information, see[Creating an SMS Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm).
Note  
  
SMS subscriptions are limited to the OC1 commercial realm only.
- (Optional) To add another subscription protocol to this topic, perform one of the following actions, depending on what's available:
- Select Add subscription , and then repeat the previous step.
- Select + Another subscription , and then repeat the previous step.
- When you're ready, select Save changes .
- 

Use the[oci announce announcement-subscription update](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/update.html)command and required parameters to update an announcement subscription:

```

```

For example, to change a subscription name:
```

```

Or, to change a subscription description:
```

```

Or, to change the subscription's preferred time zone by specifying the IANA Time Zone Database format:
```

```

Or, to change the subscription's Notifications topic:
```

```

For more information about Notifications topic options, see[UpdateSubscriptionDetails](https://docs.oracle.com/iaas/api/#/en/notification/latest/datatypes/UpdateSubscriptionDetails).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/UpdateAnnouncementSubscription)
