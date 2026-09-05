# Integrate with Workday
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-workday.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Workday

## Overview: Integrate Oracle Access Governance with Workday

Integration between Oracle Access Governance and Workday streamlines user lifecycle management of Workday users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of user security groups and roles.

Workday can be integrated with Oracle Access Governance as an authoritative source or managed system, allowing you to reconcile users, security groups, and roles, and provision identities and accounts.

## Workday Integration Architecture Overview

You can perform full data load for accounts in Workday. Once a connection is established, you can perform remediation and management tasks for user accounts, roles, and security groups.

Workday integration supports management of Workday accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Workday user identity updates. Create, and modify accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke Workday roles and security group memberships using governance policies defined in Oracle Access Governance

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Workday.
- Access Reviews and Attestation :

Periodically review and certify Workday user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for Workday Integration

Workday integration supports management of Workday accounts by Oracle Access Governance, including the following use cases.

- 

Configure Workday Orchestrated System

See[Configure Integration Between Oracle Access Governance and Workday](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-workday.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/workday-integration-reference.htm#workday-matchingrule).
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

[Enable/disable Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#disable-and-enable-an-account-managed-by-oracle-access-governance)
