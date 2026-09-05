# Integrate Oracle Access Governance with SAP S/4HANA
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-s4hana.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate Oracle Access Governance with SAP S/4HANA

Oracle Access Governance enables API-based seamless integration with SAP S/4HANA for enabling identity orchestration, automating onboarding of accounts and roles, reconciliation of accounts. Oracle Access Governance supports account management and role management for SAP S/4HANA accounts as a Managed System .

SAP S/4HANA is a comprehensive cloud-based procurement and spend management service that helps businesses streamline and optimize their procurement processes, from sourcing to payment. With this integration, you can update, enable, and disable identity accounts. You can assign or revoke roles for accounts from Oracle Access Governance.

## Overview: SAP S/4HANA Orchestrated System

You can establish a connection between SAP S/4HANA and Oracle Access Governance by entering connection details and configuring the orchestrated system. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## SAP S/4HANA Integration Architecture Overview

You can perform full data load for accounts in SAP S/4HANA. Once a connection is established, you can perform remediation tasks for user accounts and roles.

SAP S/4HANA integration leverages the following SOAP APIs for full incremental data load.
- Use the SAP S/4HANA Business Users Read SOAP API to read data, and perform full data load in Oracle Access Governance.
- Use the Business Users SOAP API to update account attributes and assign roles to accounts from Oracle Access Governance.

## Functional Overview: Use Cases Supported for SAP S/4HANA Integration

SAP S/4HANA integration supports account management and role management for SAP S/4HANA accounts. The SAP S/4HANA orchestrated system supports management of accounts for Business Users SAP S/4HANA.
- Configure SAP S/4HANA Orchestrated System

See[Configure Integration Between Oracle Access Governance and SAP S4Hana](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-s4hana.htm)  

- [Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or Configure the matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/saphana-integrationreference.htm#saps4hana-default-attributes).
- [Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and roles that can be managed by Oracle Access Governance  

- Update Account

Modify account attributes, such as locking or unlocking the account by editing the LockedIndicator attribute account.
Note  
  
As a user with`AG_ServiceDesk_Admin`role, use the Edit Account feature from the Manage Identities page to update the account.
- [Enable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-enable-account)

If only permissions are different, then account remains enabled but Add  
account or permission data and/or Remove account or permission data operations are triggered in the Orchestrated System to update the permissions for that account.
- [Disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-revoke-account)

If all the permissions are deleted, then SAP S/4HANA accounts are disabled with Update Account and Remove account or permission data operations.
- [Assign Roles as Permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)
- [Revoke Roles as Permissions](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)

### Example: Use Case for SAP S/4HANA

SAP S/4HANA Orchestrated System is used for managing accounts and roles across SAP S/4HANA cloud service using Oracle Access Governance.
Scenario : A policy violation is detected due to multiple failed sign-in attempts for an SAP S/4HANA account. To take immediate action, a user with the`AG_ServiceDesk_Admin`role can modify account attributes immediately without undergoing business approvals. Use Oracle Access Governance to seamlessly manage accounts and role assignments to SAP S/4HANA. In this scenario, you would lock an account of the user.
- Configure your SAP S/4HANA instance with Oracle Access Governance using the steps defined in[Configure Integration Between Oracle Access Governance and SAP S4Hana](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-s4hana.htm).
- Perform data load to reconcile existing accounts. Full Data Load for Day 0 and Lookup Data Load for Day N activities would trigger to ingest data from SAP S/4HANA into Oracle Access Governance.
- Configure your orchestrated system settings to further add matching rules, transformations, notification settings, and so on. For details, see[Configure Settings for Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-ariba.htm#sapariba-functional-overview).
- As a`AG_ServiceDesk_Admin`user, from the Manage Identities page, perform the following
- From the Identities list, select the Actions icon and select View details . The Identity details page is displayed with the Permissions tab selected by default.
- Select the Accounts tab.
- Select the Actions icon corresponding to the account that you want to edit.
- Select Edit Account .
- Clear the Account locked check box and save the details.
-
