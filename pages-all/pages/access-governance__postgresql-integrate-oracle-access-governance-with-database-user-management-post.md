# Integrate Oracle Access Governance with Database User Management (PostgreSQL)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/postgresql-integrate-oracle-access-governance-with-database-user-management-post.htm
- Fetched: 2026-09-05 03:16 CDT

# Integrate Oracle Access Governance with Database User Management (PostgreSQL)

## Overview: Integrate Oracle Access Governance with Database User Management (PostgreSQL)

Integration between Oracle Access Governance and Database User Management (PostgreSQL) streamlines user lifecycle management of Database User Management (PostgreSQL) users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of users, roles, and privileges.

Database User Management (PostgreSQL) can be integrated with Oracle Access Governance as a managed system, allowing you to reconcile users, roles, and privileges, and provision identities and accounts.

## Database User Management (PostgreSQL) Integration Architecture Overview

You can perform full data load for accounts in Database User Management (PostgreSQL). Once a connection is established, you can perform remediation and management tasks for user accounts, roles, and privileges.

Database User Management (PostgreSQL) integration supports management of Database User Management (PostgreSQL) accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Database User Management (PostgreSQL) user identity updates. Create, modify, and delete accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke Database User Management (PostgreSQL) users, roles, and privileges using governance policies defined in Oracle Access Governance

Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Database User Management (PostgreSQL).
- Access Reviews and Attestation :

Periodically review and certify Database User Management (PostgreSQL) user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for Database User Management (PostgreSQL) Integration

Database User Management (PostgreSQL) integration supports management of Database User Management (PostgreSQL) accounts by Oracle Access Governance, including the following use cases.

- 

Configure Database User Management (PostgreSQL) Orchestrated System

See[Configure Integration with Database User Management (PostgreSQL)](https://docs.oracle.com/en-us/iaas/Content/access-governance/db-user-postgresql-configure-integration-with-database-user-management-postgresql.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rule](https://docs.oracle.com/en-us/iaas/Content/access-governance/postgresql-database-user-management-postgresql-integration-reference.htm#postgresql-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts, roles, and privileges that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions.This allows you to update entitlements.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
