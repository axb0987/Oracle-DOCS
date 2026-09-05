# Integrate Oracle Access Governance with Oracle Configure, Price, Quote (CPQ)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-integrate-with-cpq.htm
- Fetched: 2026-09-05 03:13 CDT

# Integrate Oracle Access Governance with Oracle Configure, Price, Quote (CPQ)

Oracle Configure, Price, Quote (CPQ) can be integrated with Oracle Access Governance as a Managed system, allowing you to reconcile and provision accounts, groups (sales and admin), and permissions.

## Overview: Integrate Oracle Access Governance with Oracle Configure, Price, Quote (CPQ)

Integration between Oracle Access Governance and Oracle Configure, Price, Quote (CPQ) streamlines user lifecycle management of Oracle Configure, Price, Quote (CPQ) users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through access reviews of accounts and roles.

## Oracle Configure, Price, Quote (CPQ) Integration Architecture Overview

You can perform full data load for accounts in Oracle Configure, Price, Quote (CPQ). Once a connection is established, you can perform provisioning, remediation, and management tasks for accounts, groups (sales and admin), and permissions.

Oracle Configure, Price, Quote (CPQ) integration supports management of accounts, including the following use cases.
- Centralized User Provisioning :

Perform Oracle Configure, Price, Quote (CPQ) account updates. Create, Reset password, Enable, Disable accounts from within Oracle Access Governance. See[Manage Account Lifecycle with Service Desk Executive Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- Access Control :

Assign or revoke permissions (groups and entitlements) using Access Control module of Oracle Access Governance.

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes. See[Automated Provisioning for Joiners, Movers, and Leavers (JML) Process](https://docs.oracle.com/en-us/iaas/Content/access-governance/jml-process.htm).
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance access guardrails and Identity collection. See[Access Guardrails - Enforce Preventive Access Control Conditions](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm)
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Oracle Configure, Price, Quote (CPQ). See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm)
- Access Reviews and Attestation :

Periodically review and certify Oracle Configure, Price, Quote (CPQ) user access to ensure appropriate entitlements. See[Access Reviews Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm).
- Audit and Compliance Support :

Track and maintain full audit trail and recent changes of all user and access-related changes to meet regulatory and internal compliance requirements. See[Audit Trail: Monitoring Access Decisions](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#audit-trail-monitoring-access-decisions).

## Functional Overview: Use Cases Supported for Oracle Configure, Price, Quote (CPQ) Integration

Oracle Configure, Price, Quote (CPQ) integration supports management of Oracle Configure, Price, Quote (CPQ) accounts, permissions, and groups from Oracle Access Governance:

- 

Configure Orchestrated System

See[Configure Integration with Oracle Configure, Price, Quote (CPQ)](https://docs.oracle.com/en-us/iaas/Content/access-governance/unity-configure-integrate-unity.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-cpq-integrate-with-cpq.htm#oracle-cpq-default-matching-rules).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts, groups (sales and admin), and permissions that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity using the self-service capability. This allows you to provision entitlements.
- 

[Change Account Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password)

Change Account Password from Oracle Access Governance.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. This allows you to update entitlements.
- [Enable/Disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-enable-account)
