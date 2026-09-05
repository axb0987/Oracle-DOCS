# Updating a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-subscription.htm
- Fetched: 2026-09-05 02:50 CDT

# Updating a Subscription

Update the delivery policy or tags for a subscription in Notifications.

When you update a subscription, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

For more information about the delivery retry (part of the delivery policy), see Delivery retry details in[Overview of Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-subscription.htm#)
- 

These steps show how to update the delivery policy from the Subscriptions list page. You can also update the delivery policy from the list of subscriptions for a[topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription-topic.htm), or from the[subscription's details page](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm).

- On the Subscriptions list page, find the subscription that you want to work with. If you need help finding the list page or the subscription, see[Listing Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-subscription.htm).
- From the Actions menu (three dots) for the subscription, select Update delivery policy .
- In the Update delivery policy panel, update the value for Max retry duration in minutes .
- Select Save .
- 

Use the[oci ons subscription update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/update.html)command and required parameters to update a subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[UpdateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/UpdateSubscription)
