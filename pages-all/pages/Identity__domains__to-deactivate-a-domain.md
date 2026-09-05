# Deactivating an Identity Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm
- Fetched: 2026-09-05 02:21 CDT

# Deactivating an Identity Domain

You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed. An identity domain must be deactivated before it can be deleted.

You can't deactivate the Default identity domain or the identity domain to which you're signed in (the current domain).

Before you deactivate an identity domain, all Cloud, Oracle, Custom, and Enterprise applications must be deactivated. All applications created by App Services in Oracle Cloud Services (for example, AnalyticsINST-OAC1) must also be deactivated, but "entitlement" apps in Oracle Cloud Services (for example, ADWC) don't need to be deactivated.

Immediately after the administrator starts deactivating an identity domain, the identity domain moves to a deactivating state and users can no longer authenticate to it.
Note  
  
Paid tier identity domains continue to incur costs when deactivated . To avoid incurring additional costs, you should delete the identity domain.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#)
- 

- On the Domains list page, select the domain that you want to deactivate. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Deactivate .
- Select More actions , and then select Deactivate .
- Select Deactivate domain to confirm the deactivation.

The identity domain is in an Inactive status.
- 

Use the[oci iam domain deactivate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/deactivate.html)and required parameters to deactivate an identity domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeactivateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/DeactivateDomain)
