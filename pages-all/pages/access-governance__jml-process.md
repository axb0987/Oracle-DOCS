# Account Lifecycle Management - Automated Provisioning for Joiners Movers and Leavers (JML) Process
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/jml-process.htm
- Fetched: 2026-09-05 03:15 CDT

# Account Lifecycle Management - Automated Provisioning for Joiners Movers and Leavers (JML) Process

Oracle Access Governance supports automated provisioning and de-provisioning of accounts and accesses based on the identity lifecycle stage. Identity Lifecycle involves three key stages - Joiners, Movers, and Leavers, popularly known as the JML process. Support for this process involves creation, modification, and deletion of identity accounts and their access permissions based on attribute change in the integrated Orchestrated system.

This process ensures that identities get the required access automatically without raising the access request manually. It not only reduces the administrative burden but also ensures data integrity and compliance. Other ways of provisioning are to request the access manually or directly provision it from the Managed System. For more information, see[View My Access Requests](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-my-access-requests.htm).

As a user with`AG_ServiceDesk_Admin`role, you can directly manage account lifecycle without any approval workflows. From the Manage Identities → Identities page , you can enable, disable, delete accounts, or terminate all accounts and associated accesses for an identity. You can also retry provisioning for failed or pending statuses, and revoke permissions assigned directly or through requests. For detailed steps, see[Manage Account Lifecycle with Service Desk Executive Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).

With Oracle Access Governance:
- Joiners get their birth-right access when they join the enterprise.
- Movers get the necessary accesses when they change roles, get internal transfers, or get promotions within the enterprise.
- Leavers have their account revoked (delete or disabled) once they exit the enterprise.

In Oracle Access Governance, your identity information is built up using a set of Core and Custom identity attributes. Whenever you create, modify, or update an identity record in the Authoritative Source, Oracle Access Governance ingests the latest data in the upcoming data load operation, and initiates the corresponding provisioning/de-provisioning operations. Oracle Access Governance achieves this granular and flexible access control mechanism by using the Policy-Based Access Control (PBAC) model. Oracle Access Governance assigns membership to identities using the attributes ( Attribute-Based Access Control (ABAC) ), and then provisioning the identities based on defined policies. A policy may further leverage the Role-Based Access Control model to assign appropriate role-based permissions ingested from identity attributes.

Supported Operations : Create Account, Read Account, Assign Permissions, Revoke Permissions, Change Password, Disable Account, Update Account, Delete Account. For additional details, refer to the specific Orchestrated System documentation as mentioned in[Supported Integrations in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/supported-integrations-in-oracle-access-governance.htm).

## Employees Onboarding - Joiners Provisioning

When a new employee joins or gets hired in an enterprise, a new record gets created in the Authoritative Source, such as Oracle HCM. Once identities are onboarded in Oracle Access Governance, birth-right access or default set of accounts and permissions can be provisioned, based on the Access Control configurations done in Oracle Access Governance.

Joiners process ensures that every new employee gets the necessary account and permissions to start-off their onboarding process.

When an identity gets onboarded and is Active in Oracle Access Governance, all the identity attributes are compared against the defined policies. If an Oracle Access Governance policy grants certain Role or Access Bundle access to identities belonging to a specific department, then they are provisioned for that role or Access Bundle.

Scenario : When a new employee, Alice , joins the Customer Success department of the Sales division, Joiners provisioning ensures Alice receives all the mandatory accounts and permissions applicable to her division and her department. Let's look at how to achieve this in Oracle Access Governance.

### Executing Joiners Provisioning in Oracle Access Governance

Taking the above scenario, let's look at the high-level steps involved to achieve Joiners provisioning in Oracle Access Governance:
- As an Access Control Administrator , set up the Access Control configuration, as follows:
- Create an Identity Collection based on membership rules. For example, create an Identity Collection with membership rule as Source Organization equals Sales and another Identity Collection where Department equals Customer Success . For more details, refer to[Create Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm).
- Create an Access Bundle or Role , and package access to necessary permissions. For example, create an Access Bundle Sales_AB with permissions applicable to Sales and another Access Bundle Customer_Success_AB with permissions applicable to Customer Success . For more details, refer to[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- Create a Policy and associate the permissions part of the Access Bundle with Identity Collection. For example, create a Policy Sales_Policy and associate Sales_AB with Sales Identity Collection. Similarly, create Customer_Success_Policy and associate Customer_Success_AB with Customer Success Identity Collection. For more details, refer to[Create a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#create-a-policy).
- Authoritative Source registers a new record of an employee. For example, HR adds a new record of Alice with Business Unit as Sales and Department as Customer Success .
- Orchestrated System performs data load, ingests latest data and builds composite identity profile in Oracle Access Governance. For more information, refer to[Identity Orchestration Process Flow](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm).

A new identity profile gets created in Oracle Access Governance. The attributes are matched against the defined policies and appropriate provisioning operations are triggered. For Joiners , Orchestrated System triggers Create Account and Add account or permission data provisioning operations to assign new accounts and permissions.

### Validate Joiners Provisioning in Oracle Access Governance

- As an Enterprise-wide Access Administrator , you can search identity to view complete identity details displaying identity attributes, permissions, account information. You can also view identity collection details to verify the new member list.
- As an Identity Manager, you can see comprehensive identity details for the direct reports in the Who has Access to What → My Directs' Access .
- As a User , you can validate your accounts and permissions from the My Stuff → My Access page.

Depending on the Account settings configured for the Orchestrated system, a User or User manager will receive notification whenever new accounts are created. By default, the notifications are sent to User . For more information, refer to[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

## Employee Transfers - Movers Provisioning

When an employee internally transfers, relocates, or gets promotion within an organization, a record gets updated for that employee in the Authoritative Source. Upon transferring, identity should only have access to suitable privileges relevant to the new job profile. Remaining accounts and permissions should be revoked based on the Account Lifecycle settings. You can achieve this automatic provisioning based on the Access Control configurations done in Oracle Access Governance.

Movers process ensures that only the necessary and correct set of permissions or accounts are assigned to the employees that they require in their new role.

Scenario : When an employee, Alice , gets internal transfer from the Customer Success department to the Cloud Sales department of the Sales division, Movers provisioning ensures Alice receives all the privileges applicable to her new role, and revokes or disables prior accounts and permissions needed by her former role. In this example, Alice will continue to have permissions applicable for Sales division but will get new privileges relevant in the Cloud Sales department. If no longer applicable, her prior accounts gets either disabled or revoked, and permissions associated with the accounts are also removed. Let's look at how to achieve this in Oracle Access Governance.

### Executing Movers Provisioning in Oracle Access Governance

Taking the above scenario, let's look at the high-level steps involved to achieve Movers provisioning in Oracle Access Governance:
- As an Access Control Administrator , you must have this minimum set-up, as follows:
- Create an Identity Collection based on membership rules. For example, create an Identity Collection with membership rule as Department equals Cloud Sales and another Identity Collection where Department equals Customer Success . For more details, refer to[Create Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm).
- Create an Access Bundle or Role , and package access to necessary permissions. For example, create an Access Bundle Cloud_Sales_AB with permissions applicable to Cloud Sales and another Access Bundle Customer_Success_AB with permissions applicable to Customer Success . For more details, refer to[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- Create a Policy and associate the permissions part of the Access Bundle with Identity Collection. For example, create a Policy Cloud_Sales_Policy and associate Cloud_Sales_AB with Cloud Sales . For more details, refer to[Create a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#create-a-policy).
- Authoritative Source records an update for the identity. For example, HR updates Alice's department from Customer Success to Cloud Sales .
- Orchestrated System performs data load, ingests latest data and builds composite identity profile in Oracle Access Governance. Based on your account lifecycle settings for an orchestrated system, permissions or accounts are either disabled or revoked. For more information, refer to[Identity Orchestration Process Flow](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm).

Users with the`AG_ServiceDesk_Admin`role can directly revoke permissions from the Manage Identities page, using the Revoke permission operation. The Grant Type of these permissions must either be`DIRECT`or Access Bundles granted through`REQUEST`. You cannot revoke permissions for Oracle Cloud Infrastructure (OCI) or Oracle Identity Governance (OIG) systems. For detailed steps, see[Revoke one or multiple permissions for an Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#revoke-one-or-multiple-permissions-for-an-account).

### Validate Movers Provisioning in Oracle Access Governance

For Movers , Orchestrated System typically triggers the following operations:
- To disassociate former permissions with the identity accounts, it triggers Remove account or permission data .
- To disable the accounts, it triggers Update Account , or to delete the accounts, it triggers Revoke .
- To associate new accounts and permissions, it triggers Create Account and Add account or permission data .
- If only permissions are different, then Account remains enabled but Add account or permission data and/or Remove account or permission data operations are triggered to update the permissions for that account.
- If a disabled account is enabled, then it triggers Update Account along with Add account or permission data and/or Remove account or permission data . You can verify the changes on the Oracle Access Governance Console:
- As an Enterprise-wide Access Administrator , you can search identity and view complete identity details displaying identity attributes, permissions, account information. You can also view identity collection details to verify the new member list.
- As a User , you can validate your accounts and permissions from the My Stuff → My Access page.

Depending on the Account settings configured for the Orchestrated system, a User or User manager will receive notification whenever new accounts are created. By default, the notifications are sent to User . The existing accounts can either be deleted or disabled depending on the Account Settings. For more information, refer to[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

## Employees Offboarding - Leavers De-Provisioning

When an employee exits the enterprise, a record gets deleted or disabled in the Authoritative Source. Upon exiting, all the accounts and associated privileges assigned to that identity will either be deleted or disabled from the Managed System.

Leavers process ensures that all accounts and permissions assigned to the identity are automatically revoked upon their exit. When an identity exits, and is marked Inactive in Oracle Access Governance, identity accesses are either revoked or disabled based on account settings.

Users with the`AG_ServiceDesk_Admin`role can directly revoke permissions from the Manage Identities page, using the Revoke permission operation. The Grant Type of these permissions must either be`DIRECT`or Access Bundles granted through`REQUEST`. You cannot revoke permissions for Oracle Cloud Infrastructure (OCI) or Oracle Identity Governance (OIG) systems. For detailed steps, see[Revoke one or multiple permissions for an Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#revoke-one-or-multiple-permissions-for-an-account).

Users with the`AG_ServiceDesk_Admin`role can now directly disable accounts managed by Oracle Access Governance from the Manage Identities page, using the Disable account operation. Once disabled all the associated accesses are revoked. The accounts can still be managed by Oracle Access Governance. For detailed steps, see[Disable and Enable an Account Managed by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance).

Scenario : When an employee, Alice , exits the enterprise, Leavers de-provisioning ensures all the assigned accounts and permissions applicable to her role gets revoked (delete or disabled). Let's look at how to achieve this in Oracle Access Governance.

### Executing Leavers De-Provisioning in Oracle Access Governance

Taking the above scenario, let's look at the high-level steps involved to achieve Leavers de-provisioning in Oracle Access Governance:
- As an Access Control Administrator , you must have this minimum set-up, as follows:
- An Identity Collection based on membership rules. For more details, refer to[Create Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm)
- An Access Bundle or Role where necessary permissions are packaged together. For more details, refer to[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm)and[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm).
- A Policy that associates the permissions (through Access Bundle) with Identity Collection. For more details, refer to[Create a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#create-a-policy).
- Authoritative Source deactivates an existing record of an employee in the system.
- Orchestrated System performs data load, ingests latest data. For more information, refer to[Identity Orchestration Process Flow](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm).

When an identity profile is deactivated and the data load is successful, a Revoke or Update Account provisioning task is triggered to either delete or disable the identity's accounts. Permissions associated with the account gets revoked and Remove account or permission data is triggered to remove permissions from the Managed system. For more information, refer to[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings)
