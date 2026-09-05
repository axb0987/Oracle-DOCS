# Integrate Oracle Access Governance with Oracle Infinity
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-infinity-integrate-with-infinity.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate Oracle Access Governance with Oracle Infinity

Oracle Infinity can be integrated with Oracle Access Governance as a Managed system, allowing you to reconcile and provision accounts.

## Overview: Integrate Oracle Access Governance with Oracle Infinity

Integration between Oracle Access Governance and Oracle Infinity streamlines user lifecycle management of Oracle Infinity accounts, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through access reviews of accounts.

## Oracle Infinity Integration Architecture Overview

You can perform full data load for accounts in Oracle Infinity. Once a connection is established, you can perform provisioning, remediation, and management tasks for user accounts.

Oracle Infinity integration supports management of accounts, including the following use cases.
- Centralized User Provisioning :

Perform Oracle Infinity account updates. Create and delete accounts from within Oracle Access Governance. See[Manage Account Lifecycle with Service Desk Executive Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- Access Control :

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes. See[Automated Provisioning for Joiners, Movers, and Leavers (JML) Process](https://docs.oracle.com/en-us/iaas/Content/access-governance/jml-process.htm).
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance access guardrails and Identity collection. See[Access Guardrails - Enforce Preventive Access Control Conditions](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm)
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Oracle Infinity. See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm)
- Access Reviews and Attestation :

Periodically review and certify Oracle Infinity user access to ensure appropriate entitlements. See[Access Reviews Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm).
- Audit and Compliance Support :

Track and maintain full audit trail and recent changes of all user and access-related changes to meet regulatory and internal compliance requirements. See[Audit Trail: Monitoring Access Decisions](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#audit-trail-monitoring-access-decisions).

## Functional Overview: Use Cases Supported for Oracle Infinity Integration

Oracle Infinity integration supports management of Oracle Infinity accounts from Oracle Access Governance:

- 

Configure Orchestrated System

See[Configure Integration with Oracle Infinity](https://docs.oracle.com/en-us/iaas/Content/access-governance/infinity-configure-integrate-infinity.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-infinity-oracle-infinity-integration-reference.htm#oracle-infinity-default-matching-rules).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity using the self-service capability.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
