# Deleting a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Deleting a Subscription

Delete a subscription in Notifications.

Note  
  
Every message sent out as email contains a link to unsubscribe from the related topic.

You can alternatively[unsubscribe](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/unsubscribe-subscription.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm#)
- 

These steps show how to delete a subscription from the Subscriptions page (list for[a compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm)). You can also list subscriptions[in a topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/list-subscription-topic.htm).

- On the Subscriptions list page, find the subscription that you want to work with. If you need help finding the list page or the subscription, see[Listing Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-subscription.htm).
- From the Actions menu (three dots) for the subscription, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci ons subscription delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/delete.html)command and required parameters to delete a subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[DeleteSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/DeleteSubscription)
