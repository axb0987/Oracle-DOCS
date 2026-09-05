# Deleting an Identity Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm
- Fetched: 2026-09-05 02:21 CDT

# Deleting an Identity Domain

Delete an identity domain in a tenancy in IAM.
Before you can delete an identity domain, you must deactivate the apps in the identity domain and then deactivate the identity domain. See[Deactivating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm).

Deleting an identity domain irreversibly deletes all users, groups, applications, and other resources in the domain. Any policies granting permissions to users, groups, or dynamic groups in the domain are no longer in effect after the domain is deleted. We recommend updating such policies to remove references to the identity domain name or the identity domain's resources, or deleting them altogether. Deleting an identity domain also invalidates any IAM policy that references it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm#)
- 

- On the Domains list page, select the domain that you want to work with. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Delete .
- Select Delete .
- Read the warning and then type the name of the identity domain to confirm the deletion.
- Select Delete .
- 

Use the[oci iam domain delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/delete.html)command and required parameters to delete an identity domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/DeleteDomain)
