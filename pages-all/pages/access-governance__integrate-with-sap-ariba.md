# Integrate Oracle Access Governance with SAP Ariba
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-ariba.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate Oracle Access Governance with SAP Ariba

Oracle Access Governance enables API-based seamless integration with SAP Ariba for enabling identity orchestration, automating onboarding of accounts and groups, provisioning and reconciliation of accounts. Oracle Access Governance supports account management and group management for SAP Ariba accounts as a Managed System .

SAP Ariba is a comprehensive cloud-based procurement and spend management service that helps businesses streamline and optimize their procurement processes, from sourcing to payment. With this integration, you can create, update, enable, and disable identity accounts. You can assign or revoke groups for accounts from Oracle Access Governance.

## Overview: SAP Ariba Orchestrated System

You can establish a connection between SAP Ariba and Oracle Access Governance by entering connection details and configuring the orchestrated system. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## SAP Ariba Integration Architecture Overview

You can perform full data and incremental data load for identities in SAP Ariba. Once a connection is established, you can perform provisioning and remediation tasks for user accounts and groups.

SAP Ariba integration leverages two SAP Ariba APIs for provisioning and full and/or incremental data load.
- Use the SAP Ariba Import Users SOAP API to create, update, enable, disable accounts to existing supplier or customer organizations for SAP Ariba Strategic Sourcing solutions. You can assign and/or revoke identities from the SAP Ariba groups as from Oracle Access Governance.
- Use the SAP Ariba Master Data Retrieval API for Sourcing REST API to read data, and perform full or incremental data load in Oracle Access Governance.

## Functional Overview: Use Cases Supported for SAP Ariba Integration

SAP Ariba integration supports account management and group management for SAP Ariba accounts. The SAP Ariba orchestrated system supports management of accounts for Cloud Identity , Synchronized Identity , and Federated Identity models of SAP Ariba.

### Configure SAP Ariba Orchestrated System

First, set up and configure SAP Ariba Orchestrated System. For details, see[Configure Integration Between Oracle Access Governance and SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm). This configuration provides Oracle Access Governance the connection details on how to load data and manage permissions for this Orchestrated System.
Optionally, you can configure further elements of the Orchestrated System before running the initial data load including:
- [Notification Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm)
- [Identity and Account Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)
- Apply data transformations to[Inbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-inbound-transformations-for-identity-and-account-attributes)and[Outbound](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes)data
- [Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)
Note  
  
You can monitor the Activity Log to view all the provisioning and reconciliation operations performed for this Orchestrated System. For more details, see[View Activity Log](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#view-activity-log).

### Load Data

After setting up and verifying your Orchestrated System, you can ingest account details from SAP Ariba, using the configuration mode - Managed System . This indicates that SAP Ariba accounts and groups are ingested into Oracle Access Governance and can be managed by Oracle Access Governance.

Users in SAP Ariba are ingested as accounts and SAP Ariba groups are ingested as permissions in Oracle Access Governance.

### Account Management for SAP Ariba - Create, Update, Enable and Disable AccountThe following ways allows you to create an account in Oracle Access Governance:
- Ingestion of account and permissions as part of data load operation from SAP Ariba.
- When a role, policy, or access bundle containing SAP Ariba groups are assigned to an identity. Any active identity in Oracle Access Governance can request permissions by using the self-service Request a new access functionality in the Oracle Access Governance console. If you make an access request for an access bundle, or role, then after approval, a provisioning operation is initiated.

Here's how you can manage account operations using Oracle Access Governance
- Create Account : New accounts in SAP Ariba are created as part of group assignment. If you request SAP Ariba groups for an identity that does not have corresponding account in SAP Ariba, a new account is created and the requested groups based on the access bundle values, are assigned to it. To associate new accounts and groups, the orchestrated system triggers Create Account and Add Child Data operations.
- Update Account : If an SAP Ariba account is managed by Oracle Access Governance and corresponding account already exists in SAP Ariba, then SAP Ariba groups for that account are updated based on the values in the access bundle. Update Account provisioning task is triggered along with Remove Child Data and Add Child Data
- Enable Account : If only permissions are different, then account remains enabled but Add Child Data and/or Remove Child Data operations are triggered in the Orchestrated System to update the permissions for that account.
- Disable Account : If all the permissions are deleted, then SAP Ariba accounts are disabled with Update Account and Remove Child Data operations.

For more details, see[View Activity Log](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#view-activity-log).

### Assign Groups as Permissions

You can assign groups as permissions to a SAP Ariba account using the Request a new access functionality of Oracle Access Governance. This allows you to request an access bundle containing permissions which equate to groups on the SAP Ariba system.

When you request an access bundle, either directly or through an Oracle Access Governance role or policy, a provisioning operation, Add Child Data , is initiated which updates the groups in your SAP Ariba instance with the permissions included in the referenced access bundle.

If you request SAP Ariba groups for an identity that does not have corresponding account in the SAP Ariba instance, then a new account is also created on the SAP Ariba instance with Create Account operation.

For further details about permission assignment, refer to[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). To learn more about roles and policies, refer to[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm), and[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).

### Revoke Groups as Permissions

You can revoke group permissions from an account by removing the permission from the role, policy or access bundle to which it is assigned. In this case, the permission assignment is revoked from all users to whom the role, policy or access bundle is applied.

Another way to remove a permission would be by revoking role, policy or access bundle assignment from a specific account. This would be done using the revoke operation in access reviews.

If only permissions are different, then account remains enabled but Add Child Data and/or Remove Child Data operations are triggered to update the permissions for that account. If all the permissions are deleted, the SAP Ariba accounts are disabled.

For further details about permission assignment, refer to[Delete a Role](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm#delete-a-role),[Delete a Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#delete-a-policy), or[Manage Access Bundles -&gt; Delete an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-bundles.htm).

### Example: Joiner Use Case for SAP Ariba

SAP Ariba Orchestrated System is used for managing accounts and groups across SAP Ariba cloud service using Oracle Access Governance.
Scenario : A new employee joins as a Sourcing Manager in your team, and access to SAP Ariba must be provisioned automatically with appropriate group membership. For this example, assume you have established an integration with Authoritative Source, Oracle HCM, and Oracle Access Governance data is synced with this new employee information. Use Oracle Access Governance to seamlessly manage accounts and group membership to SAP Ariba.
- Configure your SAP Ariba instance with Oracle Access Governance using the steps defined in[Configure Integration Between Oracle Access Governance and SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm).
- Perform data load to reconcile existing accounts. Full Data Load for Day 0 and Lookup Data Load for Day N activities would trigger to ingest data from SAP Ariba into Oracle Access Governance.
- Configure your orchestrated system settings to further add matching rules, transformations, notification settings, and so on. For details, see[Configure Settings for Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-ariba.htm#sapariba-functional-overview).
- In Oracle Access Governance Access Controls section, perform the following
- Create an Access Bundle for your SAP Ariba Orchestrated System. Select appropriate Groups . For details, see[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- Create a policy within Oracle Access Governance and associate the access bundle with an identity collection, say Sourcing_Managers . Another way is to request access for this access bundle using the self-service functionality. For details, see[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm)and[Request Access to a Resource](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm#request-access-to-a-resource).
-
