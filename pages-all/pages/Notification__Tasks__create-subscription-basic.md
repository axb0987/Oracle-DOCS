# Creating a Subscription (Any Type)
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-basic.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating a Subscription (Any Type)

Create any valid type of subscription in Notifications to receive notifications.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-basic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-basic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-basic.htm#)
- 

These steps show how to open the Create subscription panel from the details page for the topic that you want to add the subscription to. You can also open this panel from the[Subscriptions list page , specifying the topic in the panel: Select Create subscription , and then select a Subscription topic .

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- On the topic's details page, select Subscriptions .
- Select Create subscription .
- In the Create subscription panel, select the type of subscription that you want to create, then enter values in the associated fields.
- Email : Enter an email address.
- 

Function : Select the compartment and application that contain the function that you want, and then select the function.
- 

HTTPS (Custom URL) : Enter the URL that you want to use as the endpoint. Endpoint format:
```

```

For prerequisites, see[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-https.htm#prereqs). Query parameters aren't permitted in URLs.
- 

PagerDuty : Enter the integration key portion ([PagerDuty endpoint](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/pagerduty.htm#endpoint)). The other portions of the URL are hard-coded. Full endpoint format:
```

```

Query parameters aren't permitted in URLs.
- 

Slack : Enter the[Slack endpoint](https://api.slack.com/incoming-webhooks#create_a_webhook), including the webhook token. Endpoint format:
```

```

The &lt;webhook-token&gt; portion of the URL contains two slashes (/).Query parameters aren't permitted in URLs.
- 

SMS : Select the country for the phone number, and then enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en). Example:`+14255550100`

For more information about each subscription type, see "subscription" under[Notifications Concepts](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#concepts).
- (Optional) Tags : Add one or more tags to the subscription.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
Notifications creates the subscription. If the subscription type requires a[confirmation](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm), then Notifications sends a confirmation URL to its endpoint and the subscription is pending until confirmation is received. The confirmation URL is valid for three (3) days.
- 

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create a subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create a subscription.

## What's Next

Confirmation is required for some protocols, such as email. In this case, the new subscription remains in Pending (`PENDING`) status until confirmation is received. Notifications sends a confirmation URL to the subscription endpoint, such as an email address for an email subscription. The confirmation URL is valid for three (3) days. To confirm a new subscription, or to review subscription protocols that require confirmation, see[Confirming a Subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Although a new subscription must be in the same compartment as its parent topic, you can move it to another compartment after creation. See[Moving a Subscription to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm)
