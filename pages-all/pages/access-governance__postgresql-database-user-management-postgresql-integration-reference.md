# Database User Management (PostgreSQL) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/postgresql-database-user-management-postgresql-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Database User Management (PostgreSQL) Integration Reference

## Database User Management (PostgreSQL) Components Certified for Integration with Oracle Access Governance

The Database User Management (PostgreSQL) components that you can integrate with are listed below.

Certified Components
Component Type Component
System PostgreSQL 17.x
External Code The connector works with postgresql-42.7.5.jar or later. The following custom code file is required:
- postgresql-42.7.5.jar

## Supported Configuration Modes for Database User Management (PostgreSQL) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Database User Management (PostgreSQL) Orchestrated System supports the following mode:
- Managed System

You can manage Database User Management (PostgreSQL) accounts, roles, and privileges.

## Supported Operations When Provisioning To Database User Management (PostgreSQL)

When you provision an account from Oracle Access Governance to Database User Management (PostgreSQL) certain operations are supported.

The Database User Management (PostgreSQL) Orchestrated System supports the following account operations when provisioning a user:

- Create user
- Update user
- Delete user
- Reset password
- Add role
- Remove role
- Add privilege
- Remove privilege

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Database User Management (PostgreSQL)](https://docs.oracle.com/en-us/iaas/Content/access-governance/postgresql-integrate-oracle-access-governance-with-database-user-management-post.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Database User Management (PostgreSQL) attributes.

Default Attributes for Database User Management (PostgreSQL) - Managed System
Entity Database User Management (PostgreSQL) Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity Attribute Display Name
User usename name User login
usename uid Unique Id
usecreatedb createDb Create db
usesuper superUser Superuser
userepl initiateReplication Initiate replication
usebypassrls bypassRLS Bypass row level security
passwd password Password
valuntil passwordExpiry Password expiry
useconfig runTimeConfiguration Runtime configuration
Role roles roles Roles
Privilege privileges privileges Privileges

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Database User Management (PostgreSQL) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.usename = Identity.name`
