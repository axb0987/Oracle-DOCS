# Oracle APEX Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-oracle-apex-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle APEX Integration Reference

## Oracle APEX Components Certified for Integration with Oracle Access Governance

The Oracle APEX components that you can integrate with are listed below.

Certified Components
Component Type Component
System Oracle APEX
External Code The connector works with a script file. The following script file is required:
- oracle.ag.sql

## Supported Configuration Modes for Oracle APEX Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Oracle APEX Orchestrated System supports the following mode:
- Managed System

You can manage Oracle APEX accounts, groups, and privileges.

## Supported Operations When Provisioning To Oracle APEX

When you provision an account from Oracle Access Governance to Oracle APEX certain operations are supported.

The Oracle APEX Orchestrated System supports the following account operations when provisioning a user:

- Create user
- Update user
- Delete user
- Reset password
- Add group
- Remove group
- Add privilege
- Remove privilege

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Oracle APEX](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-oracle-apex.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle APEX attributes.

Default Attributes for Oracle APEX - Managed System
Entity Oracle APEX Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity Attribute Display Name
__UID__ (id) uid uid
User __NAME__ (user_name) name User login
workspace_user_name workspaceUserName Workspace user name
workspace_id workspace Workspace
account_locked accountLocked Account availability
first_name firstName First name
last_name lastName Last name
description description Description
email_address email Email
__PASSWORD__(web_password) password Password
default_schema defaultSchema Default schema
available_schemas availableSchemaCount Available schema count
failed_access_attempts failedAccessAttempts Failed access attempts
Entitlement Assignments
groups groups Groups
privileges privileges Privileges

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Oracle APEX orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`Workspace user name = Employee user name`

Attribute name :

`Account.workspace_user_name= Identity.name`

## Known Issues

The following known issues exist while working with Oracle APEX orchestrated system.
- Change Password : Oracle APEX Accounts provisioned from Oracle Access Governance are unable to signin to Oracle APEX using the updated password even though the Update account and Change password activities are triggered. Log in will result in an invalid credentials" error.
-
