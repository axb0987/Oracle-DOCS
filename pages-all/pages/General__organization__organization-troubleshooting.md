# Troubleshooting Organization Management
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-troubleshooting.htm
- Fetched: 2026-09-05 02:12 CDT

# Troubleshooting Organization Management

Use troubleshooting information to identify and address common issues that can occur while working with Organization Management.
- [Governance Rules that Need Attention](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-troubleshooting.htm#govrules_need_attention)

## Governance Rules that Need Attention

Sometimes governance rules require attention while attaching to one or many tenancies in the organization.

The[work request](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-management.htm)for a specific tenancy gives detailed[logs](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-logs.htm)and[error messages](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-list-errors.htm)about the issue. Some typical scenarios include:

- Creating a Tags governance rule and applying it to a tenancy, but the tenancy already has a tag namespace with the same name. For example, if you apply this kind of a rule to the parent tenancy, the template tag namespace prevents creation of another tag namespace with a matching name.
-
