# Moving a Subscription to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Moving a Subscription to a Different Compartment

Move a subscription in Notifications to another compartment. The associated topic remains in its current compartment.

Important  
  
To move resources between compartments, resource users must have sufficient access permissions for the compartment that the resource is being moved to and the current compartment. For more information about permissions for Notifications resources, see[Securing Notifications](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm).

The moved subscription is subject to policies of the destination compartment. Inherent policies in the destination compartment apply immediately and affect access to the moved resource through the Console. For more information about moving resources, see[Moving a Resource Between Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/To_move_a_resource_to_a_different_compartment.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm#)
- 

These steps show how to move a subscription from Subscriptions list page. You can also move a subscription from the list of subscriptions for a[topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription-topic.htm), or from the[subscription's details page](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/get-subscription.htm).

- On the Subscriptions list page, find the subscription that you want to work with. If you need help finding the list page or the subscription, see[Listing Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-subscription.htm).
- From the Actions menu (three dots) for the subscription, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci ons subscription change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/change-compartment.html)command and required parameters to move a subscription to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[ChangeSubscriptionCompartment](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/ChangeSubscriptionCompartment)
