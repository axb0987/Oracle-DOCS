# Creating an Email Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-email.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating an Email Subscription

Create an email subscription in Notifications to receive notifications by email. An email subscription can reference any email address, including an alias for a distribution list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-email.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-email.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-email.htm#)
- 

These steps show how to open the Create subscription panel from the details page for the topic that you want to add the subscription to. You can also open this panel from the[Subscriptions list page , specifying the topic in the panel: Select Create subscription , and then select a Subscription topic .

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- On the topic's details page, select Subscriptions .
- Select Create subscription .
- In the Create subscription panel, for Protocol , select Email .
- Enter an email address.
- Select Create .

Notifications creates the email subscription and sends a confirmation URL to the email address. The confirmation URL is valid for three (3) days. The subscription is pending until confirmation is received.
- 

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create an email subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create an email subscription.

Example:
```

```

## What's Next

To activate the new subscription, navigate to the[confirmation URL](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm#email)that was sent to the email address.

Although a new subscription must be in the same compartment as its parent topic, you can move it to another compartment after creation. See[Moving a Subscription to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm)
