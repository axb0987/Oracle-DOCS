# Getting Confirmation Results for a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-confirm-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Getting Confirmation Results for a Subscription

Get confirmation results for a subscription in Notifications. The status of a new subscription that requires confirmation is Pending (`PENDING`). When the topic is confirmed, the subscription status changes to Active (`ACTIVE`).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-confirm-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-confirm-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-confirm-subscription.htm#)
- 

These steps show how to get confirmation results for a subscription[in a compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm). You can also list subscriptions[in a topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/list-subscription-topic.htm). And you can[get a subscription's details](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm): A Pending banner indicates lack of confirmation (for a subscription type that requires confirmation) while no such banner indicates that the subscription is active.

On the Subscriptions list page, under Subscription OCID , select the subscription that you want to work with. If you need help finding the list page or the topic, see[Listing Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-subscription.htm).
The page lists subscriptions in the selected compartment. The value in the State column indicates the confirmation status: Pending indicates lack of confirmation while Active indicates received confirmation.
- 

Use the[oci ons subscription confirm](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/confirm.html)command and required parameters to get confirmation results for a subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[GetConfirmSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/GetConfirmSubscription)
