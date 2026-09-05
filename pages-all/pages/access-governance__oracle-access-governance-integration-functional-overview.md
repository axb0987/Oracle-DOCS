# Oracle Access Governance Integration Functional Overview: Supported Operations in Orchestrated System
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Access Governance Integration Functional Overview: Supported Operations in Orchestrated System

Oracle Access Governance enables integration with many native, direct or specialized applications and systems, either as an authoritative source or managed system.
This integration support allows you to manage use cases including configuration of orchestrated systems, data load, account creation and revocation, password change, and assignment and removal of roles.

## Configure Orchestrated System

The first task you need to carry out to enable integration of your application or system with Oracle Access Governance is setup and configuration of an orchestrated system. This gives Oracle Access Governance details of how to connect to the target application or system from which you want to load data, or manage permissions. Optionally you can configure further elements of the Orchestrated System before running the initial dataload including:
- [Notification Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm)
- [Identity/Account Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)
- Apply data transformations to[inbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-inbound-transformations-for-identity-and-account-attributes)and[outbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes)data
- [Identity attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)

## Load Data

Once you have setup and verified your orchestrated system, you can run dataloads to ingest identity and account details, depending on the configuration mode you have selected, Authoritative Source or Managed System .

Data loaded in Authoritative Source mode will consist of user data from the orchestrated system. If the user is new, then a new identity is created in Oracle Access Governance. If the identity already exists in Oracle Access Governance, then any updates initiated in the orchestrated system will be applied.

Data loaded in Managed System mode comprises account data and permissions from the orchestrated system. If the account is provisioned from Oracle Access Governance, then a new account is created, together with associated permissions, in the orchestrated system. Accounts and permissions directly loaded from your orchestrated system can be managed by Oracle Access Governance. You can remediate permissions associated with a managed system account. If the account only has one permission assigned then remediation of this permission will also result in the revoking of the account.

## Create Account

An account can be created in Oracle Access Governance in two ways:
- Ingesting account data from your orchestrated system.
- When a role, policy, or access bundle containing application permissions is assigned to an identity. If you have an identity in Oracle Access Governance then you can request an account by using the Request a new access functionality in the Oracle Access Governance console. If you make an access request for an access bundle or permission which is approved, a provisioning operation will be initiated. The provisioning process will, if there is no existing account managed by Oracle Access Governance, create an account on the chosen application. If an account managed by Oracle Access Governance already exists, then the permissions for that account are updated based on the values in the access bundle.

For further details about account creation, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm).

## Assign Permissions

You can assign permissions to an account using the Request a new access functionality of Oracle Access Governance. This allows you to request an access bundle containing permissions applicable to your application. When you request an access bundle, either directly or through an Oracle Access Governance role or policy, a provisioning operation is initiated which updates the permissions in your application with the permissions included in the referenced access bundle.

For further details about permission assignment, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). To learn more about roles and policies, refer to[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm), and[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).

## Remove Permissions

You can remove permissions from an account by revoking the permission from the role, policy or access bundle to which it is assigned. In this case, the permission assignment is revoked from all users to whom the role, policy or access bundle is applied. Say you had an access bundle with two permissions, Admin , and Developer which had previously been provisioned to your application. You could update the access bundle containing these permissions to remove Developer and add Composer , resulting in the access bundle containing Admin , and Composer . This change would be reflected following the next provisioning operation, by removing the Developer role and assigning the Composer role. Admin would remain assigned.

Another way to remove a permission would be by revoking role, policy or access bundle assignment from a specific account. This would be done using the revoke operation in access reviews.

For further details about permission assignment, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role),[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy), or[Manage Access Bundles -&gt; Delete an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-bundles.htm#view-and-manage-access-bundles).

Users with the`AG_ServiceDesk_Admin`role can directly revoke permissions from the Manage Identities page, using the Revoke permission operation. The Grant Type of these permissions must either be`DIRECT`or Access Bundles granted through`REQUEST`. You cannot revoke permissions for Oracle Cloud Infrastructure (OCI) or Oracle Identity Governance (OIG) systems. For detailed steps, see[Revoke one or multiple permissions for an Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#revoke-one-or-multiple-permissions-for-an-account).

## Reset Password

You can reset password for accounts managed by Oracle Access Governance from the My Access page. Use the system generated password or create the own manually, based on the configuration set by the administrator. For further details about changing passwords, see[Change Account Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password)and[Configure Password Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#configure-password-policy).

## Revoke Account

If you revoke an account in an access review, provisioning tasks will be created to revoke the account in the corresponding application. For further details about revoking accounts, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role), or[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy).

Users with the`AG_ServiceDesk_Admin`role can now directly disable accounts managed by Oracle Access Governance from the Manage Identities page, using the Disable account operation. Once disabled all the associated accesses are revoked. The accounts can still be managed by Oracle Access Governance. For detailed steps, see[Disable and Enable an Account Managed by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance).

You may delete accounts using the Delete account operation. For deleted accounts, all the associated accesses are removed and you can no longer manage the accounts from Oracle Access Governance. For detailed steps, see[Delete an Account Managed by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance).

## Enable Account

Users with the`AG_ServiceDesk_Admin`role can re-provision the accounts and the accesses using the Enable account operation from the Manage Identities page. Once enabled, all the accounts and accesses are re-provisioned, into Oracle Access Governance. For detailed steps, see[Disable or Enable an Account Managed by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance)
