# Setting Up Contextual Notifications for an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/contextual-notifications-compute.htm
- Fetched: 2026-09-05 01:50 CDT

# Setting Up Contextual Notifications for an Instance

You can get messages when something happens with a compute instance. Use contextual notifications in the Console to create event rules and alarms for an instance. Quick start templates are available.

This feature is available in the Console only.

## Before You Begin

For administrators: To set up contextual notifications for an instance, use the following policy.

```

```

## Steps

Important  
  
Information in the Console might be shown in a different order than is presented here. Regardless of the order presented, all required and optional fields are the same.

These steps show how to set up a contextual notification for an instance, for the first time.

- On the Compute Instances list page, select the instance that you want to view. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- Select Monitoring .
- Under Notifications , select Create notification .
- In the Create notification window, enter the following information.

- Quickstart : Select to view a list of quickstart templates.
- Template selection : Select the quickstart template that you want.

An example quick start template lets you set up notifications for high CPU usage.

Alarm or event rule settings depend on the selected template.
- Create new topic : Select this option to set up a new topic if you don't have an existing one to use for these notifications.
- Compartment : Select the compartment to store the new topic in.
- Topic name : Enter a name.
- Subscription : Select a subscription protocol and then provide the requested information.
- 

Email : Enter an email address.
- 

Slack : Enter a Slack endpoint.

Endpoint format:

Sends a message to the specified Slack channel by default when you publish a message to the subscription's parent topic .
Message contents and appearance vary by message type. See[alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm),[event messages](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm), and[connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm).

Endpoint format (URL):
```

```

The &lt;webhook-token&gt; portion of the URL contains two slashes (/).
Query parameters aren't permitted in URLs.

To create an endpoint for a Slack subscription (using a webhook for the Slack channel), see[the Slack documentation](https://api.slack.com/incoming-webhooks#create_a_webhook).
- SMS (for cell phone text messages): Enter a country and a phone number.
- Tagging (under Advanced options ): Add one or more tags to the alarm or event rule to be created with the selected quickstart template. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create notification .
- Confirm the new subscriptions if needed.
For more information, see[Confirming a Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/confirm-subscription.htm).
