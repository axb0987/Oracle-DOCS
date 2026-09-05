# Integrate with Microsoft Active Directory
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-microsoft-active-directory.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Microsoft Active Directory

## Overview: Integrate Oracle Access Governance with Microsoft Active Directory

Integration between Oracle Access Governance and Microsoft Active Directory streamlines user lifecycle management of Microsoft Active Directory users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of users and groups.

Microsoft Active Directory can be integrated with Oracle Access Governance as an authoritative source or managed system, allowing you to reconcile users and groups, and provision identities and accounts.

## Microsoft Active Directory Integration Architecture Overview

You can perform full data load for accounts in Microsoft Active Directory. Once a connection is established, you can perform remediation and management tasks for user accounts and groups.

Microsoft Active Directory integration supports management of Microsoft Active Directory accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Microsoft Active Directory user identity updates. Create, and modify accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke Microsoft Active Directory group memberships using governance policies defined in Oracle Access Governance

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Microsoft Active Directory.
- Access Reviews and Attestation :

Periodically review and certify Microsoft Active Directory user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for Microsoft Active Directory Integration

Microsoft Active Directory integration supports management of Microsoft Active Directory accounts by Oracle Access Governance, including the following use cases.

- 

Configure Microsoft Active Directory Orchestrated System

See[Configure Integration Between Oracle Access Governance and Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-microsoft-active.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/microsoft-ad-microsoft-active-directory-integration-reference.htm#microsoft-ad-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. This allows you to update entitlements.
- 

[Enable/disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance)
