# Unmapping a Subscription from a Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm
- Fetched: 2026-09-05 02:12 CDT

# Unmapping a Subscription from a Tenancy

Unmap a subscription from a tenancy to revert the tenancy back to the default Oracle Universal Credits subscription.

Note  
  
This operation is valid only from the parent tenancy for a second, non-default Oracle Universal Credits subscription. The default Oracle Universal Credits subscription can't be unmapped. Unmapping a subscription from a tenancy reverts the tenancy back to the default Oracle Universal Credits subscription. For more information on setting the default subscription, see[Setting the Default Subscription](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-setdefault.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm#)
- 

To unmap a subscription, follow these steps:

- On the parent tenancy Subscription Mapping list page, select the subscription that you want to unmap. If you need help finding the list page, see[Listing Subscriptions](https://docs.oracle.com/iaas/Content/General/organization/list-subscriptions.htm).
- On the subscription mapping details page, under Mapped tenancies , select the Actions menu (three dots) for the tenancy whose subscription that you want to unmap, and select Unmap subscription from tenancy .
- Confirm the action. A notification is displayed that the unmapping operation was successful.
- 

Use the[oci organizations subscription-mapping delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/delete.html)command and required parameters to unmap a subscription by the subscription mapping ID:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSubscriptionMapping](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/DeleteSubscriptionMapping)
