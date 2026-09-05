# Integrate with Peoplesoft
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-peoplesoft.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Peoplesoft

## Overview: Integrate Oracle Access Governance with PeopleSoft

Oracle Access Governance can be integrated with PeopleSoft enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of PeopleSoft accounts.
Oracle Access Governance allows you to create an integration with one or more of these modules:
- PeopleSoft Human Capital Management (HCM)
- PeopleSoft Enterprise Learning Management (ELM)
- PeopleSoft Financials and Supply Chain Management (FSCM)
For each module, you can select either of these options:
- The PeopleSoft module as an authoritative (trusted) source of identity information allowing for reconciliation of employees created or modified in PeopleSoft.
- PeopleSoft User Management as a Managed System enabling provisioning of PeopleSoft application accounts.

## Peoplesoft Integration Architecture Overview

Integration with PeopleSoft allows you to retrieve identity data from a system, transport it to Oracle Access Governance, and ingest. Once a system is connected, you can perform provisioning and remediation tasks which are then reflected in the Managed System.

PeopleSoft integration is implemented using an Agent-based connection type. This means that a direct connection is not available, so an indirect connection is made between Oracle Access Governance and the required PeopleSoft instance using the[Access Governance Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#access-governance-agent). The PeopleSoft integration supports the following flows:
- If you select the[Authoritative Source](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)configuration mode when you setup a PeopleSoft Orchestrated System, then Oracle Access Governance will retrieve identity data from the PeopleSoft instance and treat it as an authoritative (trusted) source of identity information.
- If you select the[Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)configuration mode, then Oracle Access Governance will allow you to manage PeopleTools-based PSOPRDEFN user profile records in PeopleSoft applications. This enables the provisioning of new accounts in PeopleSoft from Oracle Access Governance.

The connection is made through PeopleSoft's Component Interface, and database views created by the PeopleSoft database service user. This results in a full load of relevant identity and account data into Oracle Access Governance each time the load is executed. If this is the first time that the load is made, then relevant identity and account structures are created in Oracle Access Governance as appropriate. On subsequent dataload runs, all data is loaded to Oracle Access Governance and the ingestion process updates any changes since the last dataload in the appropriate identity and account artefacts.

Once the connection and Day0 dataload are completed, you can provision accounts using Oracle Access Governance's provisioning engine which will take any provisioning request and pass it through the agent and onwards to PeopleSoft. Provisioning supports create, update, and revoke operations.

## PeopleSoft Integration Functional Overview

PeopleSoft integration supports usecases for HRMS and ERP including configuration of the Orchestrated System, dataload, account creation and revocation, change password, and assign and remove roles.

### Configure PeopleSoft Orchestrated System
The first task you need to carry out is setup and configuration of the PeopleSoft Orchestrated System. This gives Oracle Access Governance the details for how to connect to the PeopleSoft system from which you want to load data, or manage permissions. Optionally you can configure further elements of the Orchestrated System before running the initial dataload including:
- [Notification Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm)
- [Identity/Account Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)
- Apply data transformations to[inbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-inbound-transformations-for-identity-and-account-attributes)and[outbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes)data
- [Identity attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)

### Load Data

Once you have setup and verified your Orchestrated System, you can run dataloads to ingest identity and account details from PeopleSoft, depending on the configuration mode you have selected, Authoritative Source or Managed System .

Data loaded in Authoritative Source mode will consist of user data from the PeopleSoft system. If the user is new, then a new identity is created in Oracle Access Governance. If the identity already exists in Oracle Access Governance, then any updates initiated in the PeopleSoft system will be applied.

Data loaded in Managed System mode comprises account data and roles from PeopleSoft. If the account is new, then a new account is created in Oracle Access Governance together with the associated roles, These roles will be created in Oracle Access Governance as permissions. Accounts and permissions loaded from PeopleSoft can be managed by Oracle Access Governance. You can remediate permissions associated with a managed system account. If the account only has one permission assigned then remediation of this permission will also result in the revoking of the account.

### Create Account
An account can be created in Oracle Access Governance in two ways:
- Ingested account data from PeopleSoft.
- When a role, policy, or access bundle containing PeopleSoft roles is assigned to an identity. If you have an identity in Oracle Access Governance then you can request an account by using the Request a new access functionality in the Oracle Access Governance console. If you make an access request for an access bundle, or role, once approved, a provisioning operation will be initiated. The provisioning process will, if there is not an existing account managed by Oracle Access Governance, create an account on the PeopleSoft instance. If an account managed by Oracle Access Governance already exists, then the PeopleSoft roles for that account are updated based on the values in the access bundle. The account created in PeopleSoft equates to a PeopleTools-based PSOPRDEFN user profile record.

For further details about account creation, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm).

### Assign Permissions

You can assign permissions to a PeopleSoft account using the Request a new access functionality of Oracle Access Governance. This allows you to request an access bundle containing permissions which equate to roles on the PeopleSoft system. When you request an access bundle, either directly or through an Oracle Access Governance role or policy, a provisioning operation is initiated which updates the roles in your PeopleSoft instance with the permissions included in the referenced access bundle.

For further details about permission assignment, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). To learn more about roles and policies, refer to[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm), and[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).

### Remove Permissions

You can remove permissions from an account by revoking the permissions from the role, policy or access bundle to which it is assigned. In this case, the permission assignment is revoked from all users to whom the role, policy or access bundle is applied. Say you had an access bundle with two permissions, PSFT_Admin , and PSFT_Developer which had previously been provisioned to PeopleSoft, you could update the access bundle containing these permissions to remove PSFT_Developer and add PSFT_Composer , resulting in the access bundle containing PSFT_admin, and PSFT_Composer. This change would be reflected following the next provisioning operation by removing the PSFT_Developer role and assigning the PSFT_Composer role. PSFT_Admin would remain assigned.

Another way to remove a permission would be by revoking role, policy or access bundle assignment from a specific account. This would be done using the revoke operation in access reviews.

For further details about permission assignment, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role),[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy), or[Manage Access Bundles -&gt; Delete an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-bundles.htm#view-and-manage-access-bundles).

### Change Password

The ability to change an account password is provided by the My Access functionality in Oracle Access Governance Console. If you change the account password in this page, the details will be sent to the PeopleSoft instance in the next provisioning operation, and the password change is applied you your PeopleSoft account.

For further details about changing passwords, refer to[Change Account Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password).

### Revoke Account

If you select to revoke an account within an access review, provisioning tasks will be created to revoke the account within PeopleSoft. For further details about revoking accounts, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role), or[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy).

### An Example Account Lifecycle
Let's look at an example. You have created a new Orchestrated System which is connected to the MyPSFT instance which contains HRMS and ERP data for your organization. The Orchestrated System is configured for Authoritative Source and Managed System modes. On the first dataload, identity and account data is loaded into Oracle Access Governance. At this time the following details are created in Oracle Access Governance:
- An Oracle Access Governance identity is created, say MyAGIdentity , comprising authoritative data such as name, email, and location.
- An account is created in Oracle Access Governance for existing PeopleSoft roles, say PSFTRole_Composer . We now have the following:
- MyAGIdentity
- MyPSFTAccount
- PSFTRole_Composer

After some time MyAGIdentity moves into a development role requiring the PeopleSoft developer role. An access bundle PSFTBundle_Developer is created in Oracle Access Governance which contains the development permissions required. This access bundle can be assigned as a result of a policy, role or request. Let's say the user requests the access bundle using the Request a new access option. On approval, the request triggers a provisioning operation which applies the changes to MyPSFT , assigning the PeopleSoft roles corresponding to the permissions contained in PSFTBundle_Developer access bundle.
We now have the following:
- MyAGIdentity
- MyPSFTAccount
- PSFTRole_Composer
- PSFTBundle_Developer
Additional accounts may be mapped to the MyAGIdentity identityover time from other Managed Systems giving us a profile like this:
- MyAGIdentity
- MyPSFTAccount
- MyOracleDBAccount
- MyMSTeamsAccount

MyAGIdentity then decides to change his password. Using the My Access functionality in Oracle Access Governance Console, he changes his password, which propagates the change to MyPSFT using Oracle Access Governance provisioning.
MyAGIdentity then moves into a role which means they no longer require an account on PeopleSoft. In this case a revoke account provisioning task can be generated by revoking the identity's account as part of an access review. Alternatively, their association with PeopleSoft roles can be removed by removing the identity from the relevant Oracle Access Governance role or policy. In either case, this will result in a provisioning task which will revoke the account from PeopleSoft, together with any related roles. The profile would now resemble:
- MyAGIdentity
- MyOracleDBAccount
- MyMSTeamsAccount

If the PeopleSoft Orchestrated System is configured in Authoritative Source mode and you make an identity inactive then the the MyAGIdentity identity, is effectively disabled. In this case a provisioning task will be generated and provisiong to the Managed System.
We now have the following:
-
