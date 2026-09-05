# Editing an Identity Domain's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm
- Fetched: 2026-09-05 02:21 CDT

# Editing an Identity Domain's Details

You can edit details for an identity domain in IAM. For example, you can select whether to show the identity domain on the sign-in page or upgrade a domain by changing the domain type.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm#)
- 

- On the Domains list page, select the domain that you want to work with. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Edit domain .
- Select Edit domain .
- Change the display name, description, or whether to show the domain on the sign-in page.

- For the display name, use only letters, numerals, hyphens, periods, or underscores. The name can contain up to 100 characters.
Note  
  
Changing an identity domain's display name has consequences; for example, bookmarked URLs must be updated to use the new name.
- To change an identity domain's type, see[Changing an Identity Domain's Type](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm). To review all the identity domain types, see[IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm).
- (Optional) Under Remote region disaster recovery , select Enable remote region disaster recovery .
You must be subscribed to the paired region to enable remote region disaster recovery. For example, if your home region is US East (Ashburn), then you must be subscribed to US West (Phoenix). For more information, see[Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings).
- Select Save .
- 

Use the[oci iam domain update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/update.html)command and required parameters to edit certain details for an identity domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/UpdateDomain)
