# Integrate with ARCON PAM
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-arcon-pam.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with ARCON PAM

## Overview: Integrate Oracle Access Governance with Arcon Privileged Access Management (Arcon PAM)

Oracle Access Governance can be integrated with Arcon Privileged Access Management (Arcon PAM), enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts.

Arcon Privileged Access Management (Arcon PAM) can be integrated with Oracle Access Governance to ensure synchronized lifecycle management of privileged accounts within your enterprise, aligning with other identity-aware applications. Arcon PAM offers identity management for various models, including Cloud Identity, Synchronized Identity, and Federated Identity, making it a valuable choice for organizations seeking consistent management of accounts, groups, and roles.

## Arcon Privileged Access Management (Arcon PAM) Integration Architecture Overview

You can perform full data load for accounts in Arcon PAM. Once a connection is established, you can perform remediation tasks for user accounts, groups and roles.

Oracle Access Governance uses HTTPS to communicate with the Arcon PAM API, which provides programmatic access through SCIM API endpoints. These endpoints enable Oracle Access Governance to perform create, read, and update operations on various directory data and objects, including users, roles, multi-factor authentication, services, and groups.

## Functional Overview: Use Cases Supported for Arcon Privileged Access Management (Arcon PAM) Integration

Arcon PAM integration supports management of Arcon PAM accounts from Oracle Access Governance, including the following use cases.

- 

Configure Arcon PAM Orchestrated System

See[Configure Integration Between Oracle Access Governance and ARCON PAM](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-arcon-pam.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/arcon-pam-integration-reference.htm#arcon-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and roles that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements (Role, Group, Service) and account details (Line of Business, Multi-factor Authentication).
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. You can update entitlements (Role, Group, Service) and account details (Line of Business, Multi-factor Authentication).
- 

[Enable/disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance)
