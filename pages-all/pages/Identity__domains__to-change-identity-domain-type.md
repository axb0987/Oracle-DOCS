# Changing an Identity Domain's Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm
- Fetched: 2026-09-05 02:21 CDT

# Changing an Identity Domain's Type

Change an identity domain's type in IAM.

Each identity domain type is associated with a different set of features and object limits. For information to help you decide which domain type is appropriate for what you want to do, see[IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm).

For more information for what validations to expect when changing domain types, see[Changing your Identity Domain Type](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm#changing-domain-type).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm#)
- 

- On the Domains list page, select the domain that you want to work with. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Change domain type .
- Select Edit domain , and then select Change domain type .
- In the Change domain type panel, select the domain type you want to change to, and then select Change domain type .
- 

Use the[oci iam domain change-domain-license-type](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/change-domain-license-type.html)command and required parameters to change an identity domain's type:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeDomainLicenseType](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/ChangeDomainLicenseType)
