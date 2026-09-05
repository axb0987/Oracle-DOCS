# Deleting a Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-delete.htm
- Fetched: 2026-09-05 02:12 CDT

# Deleting a Tenancy

If certain validations are successful, start tenancy deletion. An OCI administrator can delete a child tenancy, depending on the type of child tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-delete.htm#)
- 

Child tenancies created from an organization, and standalone tenancies that were invited into an organization and which later become child tenancies, can both be deleted, but the procedures differ for these two types of child tenancies.
- If the tenancy was created from the Organization, follow the steps in[Delete a Created Child Tenancy of an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/../Tasks/deleting_tenancy.htm#deleting_tenancy__delete-createdchild)to delete a created child tenancy.
- If the tenancy was originally a standalone tenancy and was invited to became a part of the organization, the tenancy must first be removed from the organization before it can be deleted. See[Deleting Links to Invited Child Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm)for more information on invited tenancy removal.

After removal, see[Delete an Invited Child Tenancy of an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/../Tasks/deleting_tenancy.htm#deleting_tenancy__delete-invitedchild)to delete the tenancy, which deletes the tenancy and its associated subscription.

For more information on deleting a tenancy, see[Deleting a Tenancy and Cloud Account](https://docs.oracle.com/en-us/iaas/Content/General/organization/../Tasks/deleting_tenancy.htm).
- 

Use the[oci organizations organization-tenancy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/delete.html)command and required parameters to start tenancy deletion if certain validations are successful:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteOrganizationTenancy](https://docs.oracle.com/iaas/api/#/en/organizations/latest/OrganizationTenancy/DeleteOrganizationTenancy)
