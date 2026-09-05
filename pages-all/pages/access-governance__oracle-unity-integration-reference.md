# Oracle Unity Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-unity-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Oracle Unity Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Unity and Oracle Access Governance.

## Oracle Unity Components Certified for Integration with Oracle Access Governance

The Oracle Unity components that you can integrate with are listed below.

Certified Components
Component Type Component
System Oracle Unity as a Managed System as Oracle Cloud Services.
APIs Oracle Unity APIs with OAUTH 2.0 Authorization and IAM Identity Domains APIs

## Supported Configuration Modes for Oracle Unity Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Oracle Unity Orchestrated System supports the following mode:
- Managed System

You can manage Oracle Unity accounts, roles, and organizations from Oracle Access Governance .

## Supported Operations When Provisioning to Oracle Unity

When you provision an account from Oracle Access Governance to Oracle Unity certain operations are supported.

The Oracle Unity Orchestrated System supports the following account operations when provisioning a user:

- Create Account
- Revoke Account
- Enable Account
- Disable Account
- Assign Role
- Remove Role
- Assign Organization
- Remove Organization

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Unity attributes.

Account Attribute Mapping
Entity Oracle Unity Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User __UID__(id) uid Unique Id
__NAME__(userName/email) name User login
name fullname Full name
__ENABLE__(active) status Status
email email Email
admin admin Admin
Role roles roles Roles
organizations organizations Organizations

Organizations is a multivalued attribute.

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Oracle Unity orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Email`

## Known Behaviors

The following known behaviors exist while working with orchestrated system.
- Automatic Role Assignment : The Analytic User role is automatically assigned to every user account.
-
