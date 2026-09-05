# Removing Governance from Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm
- Fetched: 2026-09-05 02:12 CDT

# Removing Governance from Tenancies

Parent tenancies in an organization can remove governance (opt out themselves or child tenancies) from using governance rules.

- A parent tenancy can opt itself in or out.
- A parent tenancy can request that a child tenancy agree to[opt in](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm), or it can opt out a child tenancy.
- A child tenancy can be[opted in](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)by the parent tenancy or opt itself in, but a child tenancy can't opt itself out.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#)
- 

To opt out a parent or child tenancy from using governance rules while signed in as the parent tenancy :

- On the Tenancies list page, select the tenancy that you want to work with. If you need help finding the list page, see[Listing Organization Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm).
- On the details page, select Remove from organization governance .
- In the confirmation, select Remove from organization governance .

A message is displayed, indicating that your request to opt out of governance has been accepted, and your tenancy will be removed from organization governance soon.

After removing the tenancy from governance rules, you can no longer attach governance rules to the tenancy. To attach rules in the future, you need to[request the tenancy to opt in](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)again.

On the Tenancies list page, the Organization governance field displays Not joined , to indicate that the tenancy isn't using governance rules. The Governance state field on the tenancy's details page also shows Cost management only , to indicate that the tenancy is no longer using governance rules, and is instead only sharing[cost management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_cost_reporting.htm)details.
- 

Use the[oci organizations governance organization-tenancy remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/governance/organization-tenancy/remove.html)command and required parameters to opt a tenancy out of governance rules:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/OrganizationTenancy/RemoveGovernance)
