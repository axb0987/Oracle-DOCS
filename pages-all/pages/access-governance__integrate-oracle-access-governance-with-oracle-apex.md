# Integrate Oracle Access Governance with Oracle APEX
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-oracle-apex.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate Oracle Access Governance with Oracle APEX

## Overview: Integrate Oracle Access Governance with Oracle APEX

Integration between Oracle Access Governance and Oracle APEX streamlines user lifecycle management of Oracle APEX users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of users, groups, and privileges.

Oracle APEX can be integrated with Oracle Access Governance as a managed system, allowing you to reconcile workspace and global identities, and provision accounts and manage assignments of groups and privileges.

## Oracle APEX Integration Architecture Overview

You can perform full data load for accounts in Oracle APEX. Once a connection is established, you can perform remediation and management tasks for user accounts, groups, and privileges.

Oracle APEX integration supports management of Oracle APEX accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Oracle APEX user identity updates. Create, modify, and delete accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke Oracle APEX users, groups, and privileges using governance policies defined in Oracle Access Governance

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Oracle APEX.
- Access Reviews and Attestation :

Periodically review and certify Oracle APEX user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for Oracle APEX Integration

Oracle APEX integration supports management of Oracle APEX accounts by Oracle Access Governance, including the following use cases.

- 

Configure Oracle APEX Orchestrated System

See[Configure Integration with Oracle APEX](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-oracle-apex-integration-reference.htm#oracle-apex-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts, groups, and privileges that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. This allows you to update entitlements.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
