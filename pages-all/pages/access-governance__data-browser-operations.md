# Performing Account Lifecycle Operations in Data Browser
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm
- Fetched: 2026-09-05 03:13 CDT

# Performing Account Lifecycle Operations in Data Browser

You can perform account actions and operations on entitlements/permissions associated with Managed system using Data Browser in Oracle Access Governance.

Applicable for :`AG_AppOwner_Admin`,`AG_AppOwner_Admin_Restricted (as the resource owner for that orchestrated syste,), AG_User`(as the resource owner for that orchestrated system)

## Account Actions

You can use account operations to troubleshoot matching issues, review account details, manage account status, and perform other supported operational actions.
From the Data browser dashboard, you can perform the following actions:
- View Matching Insights : Review matching insights associated with the account, such as No Match, Multi-match, Manual Match, or User Deleted.
- View Identity Details : Open the associated identity details for the selected account. This action is available only to users who are both EWB Administrators and Application Owner . To see all application roles, see[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#application-roles-and-responsibilities-reference)
- View Details : View account attributes, metadata, and imported account information.
- Edit Account : Change supported account attributes for Managed system that support account updates.
- Enable Account : Enable a disabled account in the Managed system.
- Disable Account : Disable an active account in the Managed system.
- Match to Identity : Manually associate the account with an identity.
- Undo Manual Match : Remove a manually created identity association from the account.
- Delete Account : Delete the account from the Managed system when supported. Here's how you can perform the listed actions:

- Sign in to Oracle Access Governance as an the application owner administrator.
- From the navigation menu , select Service Administration , and then select Orchestrated Systems .
- Select the Data browser option from the action menu for the orchestrated system you want to manage.
- From the action menu for the account, select and complete the operation.
To understand each action in detail, see[Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).

## Granted Permission Actions

You can use granted permission operations to revoke permissions, view account details, and retry failed provisioning.
You can perform the following actions:
- View Account Details : View the account associated with the selected permission.
- Retry Provisioning : Retry failed or pending provisioning operations for permissions provisioned through Oracle Access Governance requests or policies. Applicable for Grant Type Request or Grant Type Policy .
- Revoke Permission : Remove the selected permission assignment from the associated account. Here's how you can perform action on granted permissions:

- Sign in to Oracle Access Governance as an Application Owner.
- From the navigation menu , select Service Administration , and then Orchestrated Systems .
- Select the Data browser option from the action menu for the orchestrated system you want to configure.
- For a specific granted permission, from the action menu for the orchestrated system, select the operation.
While performing account operations, a transitional state indicator with an icon and tool tip are displayed. After the process is complete, the final status is displayed in the Status column. For failed or pending statuses, you might again retry provisioning for the permissions provisioned within Oracle Access Governance. See[Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- To retry provisioning, select one or more failed permissions, and select Retry provisioning . For complete details, see[Retry Provisioning for Failed or Pending Accesses](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#retry-provisioning-for-failed-or-pending-accesses).

Based on the application role, you can perform account management and matching insights operations from other modules in Oracle Access Governance.

For example:
- Use Manage Integrations → Matching rules to perform identity matching operations such as matching accounts to identities or viewing matching insights. See[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules).
- For Service Desk Administrator (`AG_ServiceDesk_Admin`) application role, you can perform supported account management operations such as editing accounts, disabling accounts, retrying provisioning operations, and deleting accounts from the Manage Identities page. See[Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support)
