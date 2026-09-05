# Integrate with SAP SuccessFactors
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-successfactors.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with SAP SuccessFactors

## Overview: Integrate Oracle Access Governance with SAP SuccessFactors

Oracle Access Governance can be integrated with SAP SuccessFactors, enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts.

SAP SuccessFactors can be integrated with Oracle Access Governance as an authoritative source or managed system, allowing you to reconcile human capital management (HCM) details, and provision and manage identities and accounts.

## SAP SuccessFactors Integration Architecture Overview

You can perform full data load for accounts in SAP SuccessFactors. Once a connection is established, you can perform remediation and management tasks for user accounts, and static groups.

Oracle Access Governance uses OAuth to authorize access to the SAP SuccessFactors OData API, This enables Oracle Access Governance to perform reconciliation and provisioning tasks on HCM details held in SAP SuccessFactors.

## Functional Overview: Use Cases Supported for SAP SuccessFactors Integration

SAP SuccessFactors integration supports management of SAP SuccessFactors accounts by Oracle Access Governance, including the following use cases.

- 

Configure SAP SuccessFactors Orchestrated System

See[Configure Integration Between Oracle Access Governance and SAP SuccessFactors](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-successfactor.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-successfactors-integration-reference.htm#sap-successfactors-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements (Employee).
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions.This allows you to update entitlements (Group).
- 

[Enable/disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance)
