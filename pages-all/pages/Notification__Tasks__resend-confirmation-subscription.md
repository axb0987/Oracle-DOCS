# Resending the Confirmation URL for a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/resend-confirmation-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Resending the Confirmation URL for a Subscription

If you can't find the confirmation URL to activate a pending Notifications subscription, resend the confirmation URL to the subscription's endpoint.

The option to resend subscription confirmation URLs is available for pending subscriptions only. A subscription is pending when its type requires confirmation but hasn't received it yet (function subscriptions don't require confirmation). After receiving confirmation, the subscription is active.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/resend-confirmation-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/resend-confirmation-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/resend-confirmation-subscription.htm#)
- 

These steps show how to resend confirmation results for a subscription listed[in a compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm). You can also list subscriptions[in a topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/list-subscription-topic.htm).

- On the Subscriptions list page, find the subscription that you want to work with. If you need help finding the list page or the subscription, see[Listing Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-subscription.htm).
- From the Actions menu (three dots) for the subscription, select Resend Confirmation .
- 

Use the[oci ons subscription resend-confirmation](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/resend-confirmation.html)command and required parameters to resend a subscription's confirmation URL:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[ResendSubscriptionConfirmation](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/ResendSubscriptionConfirmation)operation to resend a subscription's confirmation URL.

## What's Next

See[Confirming a Subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)
