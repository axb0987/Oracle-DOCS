# Resource Locking
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resource_locking.htm
- Fetched: 2026-09-05 02:52 CDT

# Resource Locking

Learn about resource locking and quota policies for child tenancies in an organization.

If your tenancy is a child tenancy under a parent tenancy in an[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm), the Quota Policies page displays a lock icon next to the name of the quota policy in the Quota Name column, for any quota policies that were created and locked by the parent tenancy using[governance rules](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm#governance_rules).

Such quota policies can't be changed, because they're controlled by the parent tenancy's governance rules. For more information, see[Using Governance Rules](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm#governance_rules).

For more information, also see the following[Service Limits API](https://docs.oracle.com/iaas/api/#/en/limits/)operations and CLI commands to manage resource locking:
- [AddQuotaLock](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/AddQuotaLock)and[addlock](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/addlock.html)
- [RemoveQuotaLock](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/RemoveQuotaLock)and[removelock](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/removelock.html)
