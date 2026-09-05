# Listing Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/list-subscriptions.htm
- Fetched: 2026-09-05 02:12 CDT

# Listing Subscriptions

View the subscriptions in Organization Management that a root compartment owns.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/list-subscriptions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/list-subscriptions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/list-subscriptions.htm#)
- 

Only parent tenancies can view the list of subscriptions in an organization.

- From the parent tenancy, open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Subscription Mapping .
- On the Subscription Mapping list page, the available subscriptions are listed with the following information:

- Subscription ID
- Subscription type
- Number of Mapped tenancies (not shown for a child tenancy)
- Expiration date
- 

Use the[oci organizations subscription list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription/list.html)command and required parameters to list the subscriptions that a compartment owns:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSubscriptions](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Subscription/ListSubscriptions)
