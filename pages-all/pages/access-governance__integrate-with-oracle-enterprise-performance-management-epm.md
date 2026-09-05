# Integrate Oracle Access Governance with Oracle Cloud Enterprise Performance Management
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-enterprise-performance-management-epm.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate Oracle Access Governance with Oracle Cloud Enterprise Performance Management

Oracle Access Governance enables API-based seamless integration with Oracle Cloud Enterprise Performance Management for enabling identity orchestration, automating onboarding of accounts and groups, provisioning and reconciliation of accounts. Oracle Access Governance supports account management, role management and group management for Oracle Cloud Enterprise Performance Management accounts as a Managed System .

## Overview: Integrate Oracle Access Governance with Oracle Cloud Enterprise Performance Management

Oracle Access Governance can be integrated with Oracle Cloud Enterprise Performance Management, enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts.

You can establish a connection between Oracle Cloud Enterprise Performance Management and Oracle Access Governance by entering connection details and configuring the orchestrated system. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console. You must have an existing active connection with Oracle Cloud Infrastructure for your service instance.

## Oracle Cloud Enterprise Performance Management Integration Architecture Overview

You can perform full data load for accounts in Oracle Cloud Enterprise Performance Management. Once a connection is established, you can perform remediation and management tasks for user accounts, predefined roles, EPM roles, OCI Groups,and EPM groups.

## Functional Overview: Use Cases Supported for Oracle Cloud Enterprise Performance Management Integration

Oracle Cloud Enterprise Performance Management integration supports management of Oracle Cloud Enterprise Performance Management accounts by Oracle Access Governance, including the following use cases.

- 

Configure Oracle Cloud Enterprise Performance Management Orchestrated System

See[Configure Integration Between Oracle Access Governance and Oracle EPM](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-epm-configure-integration-epm.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/epm-reference.htm#epm-default-supported-attributes).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements (Employee).
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. This allows you to update predefined roles, Oracle Cloud Enterprise Performance Management application roles, OCI Groups and Oracle Cloud Enterprise Performance Management groups.
- 

[Revoke Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-revoke-account)
