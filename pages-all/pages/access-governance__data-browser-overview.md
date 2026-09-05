# Data Browser: View Accounts and Granted Permissions for Managed Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm
- Fetched: 2026-09-05 03:13 CDT

# Data Browser: View Accounts and Granted Permissions for Managed Systems

Use Data Browser to explore accounts and granted permissions associated with a managed system. You can review reconciled access data, troubleshoot provisioning and account matching issues, and perform supported account and permission actions.

Role : Application Owner Administrator (`AG_AppOwner_Admin`),`AG_AppOwner_Admin_Restricted`,`AG_User`(as the resource owner for that orchestrated system)

Use Data Browser when you need to:
- Review account or permission data for a Managed system
- Troubleshoot failed provisioning or inconsistent account matching issues
- Validate directly assigned permissions and provisioned access
- Analyze matching and identity correlation results
- Perform supported operational actions on accounts and permissions

## Data Browser Views

Data Browser displays Accounts and Granted permissions within the selected Managed system.
- Accounts : The Accounts view displays all accounts associated with the selected Managed system. Use this view to:
- View accounts reconciled from Managed systems and created within Oracle Access Governance.
- Validate account attributes
- Troubleshoot account-to-identity correlation
- Review matching insights such as Matching rule, No Match, Multi-match, Manual Match, and User Deleted.
- View unmatched accounts and identities deleted from the authoritative source
- Perform supported account operations for managing account lifecycle. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops)
- Granted Permission : The Granted Permissions view displays all permissions assigned to accounts within the selected Managed system. Use this view to:
- Review permissions assigned to accounts (directly assigned or provisioned through Oracle Access Governance.
- Review provisioning status
- Troubleshoot failed or pending provisioning operations
- Validate access assignments
- Perform supported permission operations for access assignments. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

Note  
  
Some account attribute values might be masked (displayed as asterisks, "********") based on your organization's policies. See:[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

### Access views in Oracle Access Governance
You can view access information, accounts, permissions, and identities from multiple views in Oracle Access Governance, depending on the application role and operational needs.
- Use Enterprise-wide Browser (EWB) for enterprise-wide access visibility on all the components, access information, and resources within an enterprise framework. Typically used by users with the`AG_Enterprise_Wide_Access_Admin`application role. See[Explore Access Profile in an Enterprise](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm)
- Use Manage Identities for identity administration and identity-level operational tasks. Typically used by users with the`AG_ServiceDesk_Admin`application role. See[Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- Use My Access and My Directs’ Access to review your own access or access assigned to your direct reports. Typically used by managers and Oracle Access Governance users. See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#view-access-details-and-manage-account).
- Use Data Browser for reviewing reconciled accounts and permissions and performing account management operations at the orchestrated system-level, such as matching accounts with identities, retrying provisioning for failed operations, and revoking permissions. Typically used by users with the`AG_AppOwner_Admin`or`AG_AppOwner_Admin_Restricted`as the resource owner. See[Data Browser: View Accounts and Granted Permissions for Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm#data-browser-overview).

## Suggested Filters in Data Browser

Data Browser displays suggested filters to narrow down results. Use the Add an advanced filter option to apply additional filters.

### Suggested Filters for Accounts

Filter
AG provisioning linked Shows accounts managed or provisioned using Oracle Access Governance.
Matching rule Displays accounts correlated using matching rules.
No match To review orphan accounts, not matched to any identity. These accounts don't have a matching identity in the system. See[Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules).
Multi-match Displays accounts matched to several identities . Useful for reviewing matching conflicts. See[Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules)
Manual Match Displays manually matched accounts.
User deleted Displays orphan accounts that were previously linked to an identity, but the associated identity was deleted from the authoritative source. The account remains in the Managed system and is now marked with the`USER_DELETED`insight.
Status Filters accounts by Enabled or Disabled status

### Suggested Filters for Permissions

Filter
Access Governance type: Access Bundle Shows permissions assigned through Access Bundles.
Access Governance type: Permission Shows direct permission assignments
Access Governance type: Role Shows roles assigned to this account using the Oracle Access Governance Access Control framework.
Status: Active Displays active granted permissions for current access. You can revoke permission, if required
