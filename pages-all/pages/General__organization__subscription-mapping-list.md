# Listing Subscription Mappings
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm
- Fetched: 2026-09-05 02:12 CDT

# Listing Subscription Mappings

List all subscription mappings.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm#)
- 

To list the mapped tenancies for a particular subscription:

- From the parent tenancy, open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Subscription Mapping .
- On the Subscription Mapping list page, select the subscription name for which you want to see the mapped tenancies.
Under Mapped tenancies , the tenancies mapped to the subscription are listed with the tenancy name and mapped date.
- 

Use the[oci organizations subscription-mapping list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/list.html)command and required parameters to list the subscription mappings for all the subscriptions owned by a particular compartment ID. Only the root compartment is allowed:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSubscriptionMappings](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/ListSubscriptionMappings)
