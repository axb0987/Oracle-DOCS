# Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-integrate-with-otm-gtm.htm
- Fetched: 2026-09-05 03:16 CDT

# Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)

Oracle Transport and Global Trade Management (OTM/GTM) can be integrated with Oracle Access Governance as a Managed system to reconcile and provision accounts and manage role assignments.

## Overview: Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)

Integration between Oracle Access Governance and Oracle Transport and Global Trade Management (OTM/GTM) streamlines user lifecycle management of Oracle Transport and Global Trade Management (OTM/GTM) users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through access reviews of accounts and roles.

## Oracle Transport and Global Trade Management (OTM/GTM) Integration Architecture Overview

You can perform full data load for accounts in Oracle Transport and Global Trade Management (OTM/GTM). After a connection is established, you can perform provisioning, remediation, and management tasks for user accounts, roles, and business intelligence roles.

Oracle Transport and Global Trade Management (OTM/GTM) integration supports management of accounts, including the following use cases.
- Centralized User Provisioning :

Perform Oracle Transport and Global Trade Management (OTM/GTM) account updates. Create, Update, Enable, Disable, and Delete accounts from within Oracle Access Governance. See[Manage Account Lifecycle with Service Desk Executive Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- Access Control :

Assign or revoke Oracle Transport and Global Trade Management (OTM/GTM) roles and Business intelligence roles, and Business intelligence application from Oracle Access Governance.

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes. See[Automated Provisioning for Joiners, Movers, and Leavers (JML) Process](https://docs.oracle.com/en-us/iaas/Content/access-governance/jml-process.htm).
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance access guardrails and Identity collection. See[Access Guardrails - Enforce Preventive Access Control Conditions](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm)
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Oracle Transport and Global Trade Management (OTM/GTM). See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm)
- Access Reviews and Attestation :

Periodically review and certify Oracle Transport and Global Trade Management (OTM/GTM) user access to ensure appropriate entitlements. See[Access Reviews Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm).
- Audit and Compliance Support :

Track and maintain full audit trail and recent changes of all user and access-related changes to meet regulatory and internal compliance requirements. See[Audit Trail: Monitoring Access Decisions](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#audit-trail-monitoring-access-decisions).

## Functional Overview: Use Cases Supported for Oracle Transport and Global Trade Management (OTM/GTM) Integration

Oracle Transport and Global Trade Management (OTM/GTM) integration supports management of Oracle Transport and Global Trade Management (OTM/GTM) accounts, roles and business intelligence roles from Oracle Access Governance:

- 

Configure Oracle Transport and Global Trade Management (OTM/GTM) Orchestrated System

See[Configure Integration with Oracle Transport and Global Trade Management (OTM/GTM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-configure-integration-otmgtm.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-gtm-integration-reference.htm#oracle-otm-default-matching-rules).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts, roles and business intelligence roles, and business intelligence applications that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. You can update entitlements.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)

Delete an account associated with an identity. This will remove access for the account.
- [Enable/Disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-enable-account)
