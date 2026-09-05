# Integrate with Oracle Health EHR (formerly Cerner Millennium)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-health-ehr-formerly-cerner-millennium.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Oracle Health EHR (formerly Cerner Millennium)

## Overview: Integrate Oracle Access Governance with Oracle Health EHR (formerly Cerner Millennium)

You can integrate Oracle Access Governance with Oracle Health EHR (formerly Cerner Millennium) for enabling identity orchestration, including on-boarding of identity user data and provisioning of Oracle Cerner accounts.

You can establish a connection between Oracle Health EHR (formerly Cerner Millennium) and Oracle Access Governance by entering connection details and configuring the connector. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance.

## Oracle Health EHR (formerly Cerner Millennium) Integration Architecture Overview

The integration of Oracle Health EHR (formerly Cerner Millennium) allows for retrieving identity data and transferring the data to Oracle Access Governance.

Oracle Health EHR (formerly Cerner Millennium) integration is implemented using an Agent-based connection type. This means that a direct connection is not available, so an indirect connection is made between Oracle Health EHR (formerly Cerner Millennium) and the required Cerner Millennium instance using the[Access Governance Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#access-governance-agent).

The Oracle Health EHR (formerly Cerner Millennium) application communicates with the Cerner API using the HTTP protocol. The Cerner API provides programmatic access to Cerner through the endpoint. Oracle Health EHR (formerly Cerner Millennium) applications uses the endpoints to perform create, read, and update, operations on directory data and directory objects, such as users, personnel groups, Organization, Organization Groups and Personal alias.

## Oracle Health EHR (formerly Cerner Millennium) Integration Functional Overview

Oracle Health EHR (formerly Cerner Millennium) integration supports configuration of the Cerner accounts which include user account creation, update, change password, and assigning and removal of roles.

### Configure Oracle Health EHR (formerly Cerner Millennium) Orchestrated System
The first task you need to carry out is to set up and configure Oracle Health EHR (formerly Cerner Millennium) Orchestrated System. This gives Oracle Access Governance the details for how to connect to the Oracle Health EHR (formerly Cerner Millennium) system from which you want to load data, or manage permissions. Optionally you can configure further elements of the Orchestrated System before running the initial dataload including:
- [Notification Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm)
- [Identity/Account Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)
- Apply data transformations to[inbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-inbound-transformations-for-identity-and-account-attributes)and[outbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes)data
- [Identity attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#rules-requirements-identity-attributes)

### Load Data

After setting up and verifying your Orchestrated System, you can ingest identity and account details from Oracle Health EHR (formerly Cerner Millennium), using the configuration mode - Managed System.

User data loaded in Managed System mode comprises of account data and roles of Oracle Health EHR (formerly Cerner Millennium). If the account is new, then a new account is created in Oracle Access Governance together with the associated roles, These roles will be created in Oracle Access Governance as permissions. Accounts and permissions loaded from Oracle Health EHR (formerly Cerner Millennium) can be managed by Oracle Access Governance. You can update the permissions associated with a managed system account. If the account only has one permission assigned then remediation of this permission will also result in the revoking of the account. If the user details such as identities exists in , then the updates initiated using system is applied.

### Create Account

As an Oracle Access Governance user you can request access to resources and roles provided in[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm).
The following ways allows you to create an user account in Oracle Access Governance:
- Ingestion of user records as data from Oracle Health EHR (formerly Cerner Millennium).
- When a role, policy, or access bundle containing Oracle Health EHR (formerly Cerner Millennium) roles is assigned to an identity. If you have an identity in Oracle Access Governance then you can request an account by using the Request a new access functionality in the Oracle Access Governance console. If you make an access request for an access bundle, or role, after approval, a provisioning operation is initiated. The provisioning process will, if there is not an existing account managed by Oracle Access Governance, create an account on the Oracle Health EHR (formerly Cerner Millennium) instance. If an account managed by Oracle Access Governance already exists, then the Oracle Health EHR (formerly Cerner Millennium) roles for that account are updated based on the values in the access bundle.

### Assign Permissions

You can assign permissions to a Oracle Health EHR (formerly Cerner Millennium) account using the Request a new access functionality of Oracle Access Governance. This allows you to request an access bundle containing permissions which equate to roles on the Oracle Health EHR (formerly Cerner Millennium) system. When you request an access bundle, either directly or through an Oracle Access Governance role or policy, a provisioning operation is initiated which updates the roles in your Oracle Health EHR (formerly Cerner Millennium) instance with the permissions included in the referenced access bundle.

For further details about permission assignment, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). To learn more about roles and policies, refer to[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm), and[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).

### Remove Permissions

You can remove permissions from an account by revoking the permissions from the role, policy or access bundle to which it is assigned. In this case, the permission assignment is revoked from all users to whom the role, policy or access bundle is applied. Another way to remove a permission would be by revoking role, policy or access bundle assignment from a specific account. This would be done using the revoke operation in access reviews.

For further details about permission assignment, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role),[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy), or[Manage Access Bundles -&gt; Delete an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-bundles.htm).

### Change Password

The ability to change an account password is provided by the My Access functionality in Oracle Access Governance Console. If you change the account password in this page, the details will be sent to the Oracle Health EHR (formerly Cerner Millennium) instance in the next provisioning operation.

For more details, refer to[Change Account Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password)
