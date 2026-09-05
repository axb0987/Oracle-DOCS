# Getting an Identity Domain's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm
- Fetched: 2026-09-05 02:21 CDT

# Getting an Identity Domain's Details

View the details of an identity domain in IAM.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm#)
- 

On the Domains list page, select the domain that you want to work with. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).

The details page opens and displays the following information about the domain. Access the various resources associated with the domain by selecting their links or tabs.
- OCID : The Oracle Cloud ID for the domain.
- Domain type : The[type of domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm).
- Description : The description of the domain.
- Domain replication : Shows whether the domain has been[replicated](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm).
- Home region : Shows the home region of the domain.
- Created : Shows the date the domain was created.
- Show domain on login : Displays whether the domain shows at sign in or not.
- Domain URL : The URL of the domain.
- Regional URL : The URL of the region.
- Status : Shows whether the domain is active or not.
- Remote region disaster recovery : The region for remote disaster recovery.
- Remote region disaster recovery status : Shows whether remote region disaster recovery is enabled or not.
- 

Use the[oci iam domain get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/get.html)command and required parameters to get identity domain information:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/GetDomain)
