# Integrate Oracle Access Governance with SAP User Management (UM)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-integrate-oracle-access-governance-with-sap-user-management-um.htm
- Fetched: 2026-09-05 03:16 CDT

# Integrate Oracle Access Governance with SAP User Management (UM)

## Overview: Integrate Oracle Access Governance with SAP User Management (UM)

Integration between Oracle Access Governance and SAP User Management (UM) streamlines user lifecycle management of SAP User Management (UM) users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of groups, roles, parameters, and profiles.

SAP User Management (UM) can be integrated with Oracle Access Governance as a managed system, allowing you to reconcile groups, roles, parameters, profiles, and provision identities and accounts.

## SAP User Management (UM) Integration Architecture Overview

You can perform full data load for accounts in SAP User Management (UM). Once a connection is established, you can perform remediation and management tasks for groups, roles, parameters, and profiles.

SAP User Management (UM) integration supports management of SAP User Management (UM) accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform SAP User Management (UM) user identity updates. Create, modify, and delete accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke SAP User Management (UM) profiles, parameters, roles, and group memberships using governance policies defined in Oracle Access Governance.

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails.
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in SAP User Management (UM).
- Access Reviews and Attestation :

Periodically review and certify SAP User Management (UM) user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for SAP User Management (UM) Integration

SAP User Management (UM) integration supports management of SAP User Management (UM) accounts by Oracle Access Governance, including the following use cases.

- 

Configure SAP User Management (UM) Orchestrated System

See[Configure Integration Between Oracle Access Governance and SAP User Management (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-configure-integration-with-sap-user-management-um.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-sap-user-management-um-integration-reference.htm#sap-user-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions.This allows you to update entitlements.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
