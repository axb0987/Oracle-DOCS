# View Access Details and Manage Account
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm
- Fetched: 2026-09-05 03:16 CDT

# View Access Details and Manage Account

As an Oracle Access Governance user, you can view your own accesses from the My Stuff , and then My Access page. You can view comprehensive details on granted roles, permissions, accounts, ownership, organizations, identity collections, identity attributes, cloud resources, and policies. You can also change your account password if the account is provisioned within Oracle Access Governance.
Note  
  
Some account attribute values might be masked (displayed as asterisks, "********") based on your organization's policies. See:[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

## Identities

While exploring access profile details in an Enterprise-wide Browser , for an identity, you can view its associated roles, permissions, accounts, ownership, organizations, identity collections, identity attributes, cloud resources, delegations, and policies. You will see the same set of information when exploring your own accesses within Oracle Access Governance, or when managers view identity details for their team members.

For Identities, you can see the following information:

Identity Access Profile Information
Access Component Description
Identity Collections Count and details of the identity collection associated with the identity. You can further browse through this identity collection by selecting the View details link. This can either be Oracle Access Governance identity collection or an ingested identity collection, such as OCI groups.
Permissions Count and access rights detail associated with this identity. It gives clarity of how this access was granted, for which resource this permission has been granted, and whether it is a role, permission, or a privilege assigned to the identity. For each permission, use the More actions icon to view permission, resource, and account details. You can even run access reviews for entitlements assigned to identities.
Organizations Count and details of Oracle Access Governance organizations associated with the selected identity.
Accounts Get count and account details associated with this identity. It gives you details like account name, the orchestrated system name associated with the account, resource name, how the access has been granted, password change status. When viewing access information for an entire enterprise from the Enterprise-wide Browser page, you can click the More actions icon to browse further or create access reviews.

When viewing your own accesses using the My Access menu option, if the account is provisioned within Oracle Access Governance and Password Change status flag is set to Applicable , then you can change your password. To do so, select Change password and follow the instructions to change your password.
Roles Count and details of roles assigned to this identity using the Oracle Access Governance Access Control framework. If you want to see the ingested roles available from Managed Systems, then see the Permissions tab.
Policies Count and details of policies used for granting access to the selected identity. You can further browse a policy to view policy statement details by selecting the View details link. The policies assigned can either be Oracle Access Governance policies or cloud policies ingested from OCI.
Violations Count and details of violations triggered by access guardrails. This includes all or open violations related to access requests either made by you or assigned to you. Select the View details link to view insights into specific security risk. Select the View access bundle details to view access bundle details that was requested.
Cloud Resources Count and cloud resource details that specify resource name, its type, the associated privilege granted to the identity along with the policy name that granted this privilege. You can also get insights on compartment and tenancy name for that resource. For further insights on resource, select the View details link where you can view reference count summary for that resource along with the pie charts showing the breakdown of identities (in percentage %) having access to the selected resource based on organization, job-code, and location.
Ownership Count and details of access controls components owned by this identity, such as identity collections, roles, policies,
Delegations Details of delegations set for this identity. Someone with the Enterprise-wide Access Administrator application role can view delegation details, but cannot edit them.
Identity Attributes Core and custom identity attributes along with its value. The attributes are logically sectioned under meaningful headings for relevancy.

## Reset Password for Managed System Accounts

You or your manager can request password reset for an account, if it's enabled for that system. Use the system generated password or create one manually, based on the configuration set by the administrator.
The Reset password option is not available in the following cases:
- The password change status is Not Applicable or Never Attempted .
- The application owner or administrator disables user password resets for the system. See[Manage Account Settings for your Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-accountsettings).
- The orchestrated system does not support password change operations.

Your manager can change account password from the Who Has Access to What , and then the My Directs' Access page.

You can set your own password, as long as it complies with the configured password policy settings. Additionally, specify the number of days the password is valid, with the maximum allowed duration enforced by password policy. After the allowed duration, the password is automatically replaced with a system-generated password, and you must request a new password to regain access. To set password policy, see[Configure Password Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#configure-password-policy).

- In the Oracle Access Governance Console, select the navigation menu , and then go to My Stuff → My Access .
- On the My Access page, select the Accounts tab.
- For an account, select the Actions icon, and then select Reset password .
- Select one of the following:
- Select Choose your own password to enter the appropriate password manually. This option is available only if configured by the administrator.
- Copy the auto generated password to use the system generated password.
- Enter the number of days you need the password to be valid.
- Select Submit .

You can't re-request the password if the previous request is still in-progress. Check the activity logs for the orchestrated system to view the Update Account activity for password reset.

## Manage Extension for Expiring Access

You can request an extension for access that is about to expire. If your request is approved, your access will be extended for the specified period. If the extension is not granted, your access will be removed upon expiry.
You must request extension before it expires. Use the Status:Soon Expiring to filter the accesses that are about to expire in the My Access → Permissions page. You can request an extension several times before the access expires.

If you're unable to request an extension, it's likely because an approval workflow hasn't been attached to the access bundle. Check the access bundle configuration.

- In the Oracle Access Governance Console, select the navigation menu , and then go to My Stuff → My Access .
- On the My Access &gt; Permissions tab.
- (Conditional) Select the Status:Soon Expiring suggested filter to view the accesses that are about to expire.
- For an access, select the Actions icon and then select Manage extension .
On the Manage extension page, you'll see the access expiry end date and time.
- Select the Request extension button. The Request extension pop-up window is displayed.
- Select the date or time until which you want to request an extension. You can request an extension only up to the maximum period allowed by the access bundle configuration.
- Enter justification and select Submit .
