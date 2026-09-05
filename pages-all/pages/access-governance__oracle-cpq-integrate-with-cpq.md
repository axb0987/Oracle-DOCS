# Oracle Configure, Price, Quote (CPQ) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-cpq-integrate-with-cpq.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Configure, Price, Quote (CPQ) Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Configure, Price, Quote (CPQ) and Oracle Access Governance.

## Oracle Configure, Price, Quote (CPQ) Components Certified for Integration with Oracle Access Governance

The Oracle Configure, Price, Quote (CPQ) components that you can integrate with are listed below.

Certified Components
Component Type Component
System Oracle Configure, Price, Quote (CPQ)
APIs REST APIs with OAUTH 2.0 Authorization

## Supported Configuration Modes for Oracle Configure, Price, Quote (CPQ) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Oracle Configure, Price, Quote (CPQ) Orchestrated System supports the following mode:
- Managed System

You can manage Oracle Configure, Price, Quote (CPQ) accounts, groups (sales and admin), and permissions from Oracle Access Governance .

## Supported Operations When Provisioning to Oracle Configure, Price, Quote (CPQ)

When you provision an account from Oracle Access Governance to Oracle Configure, Price, Quote (CPQ) certain operations are supported.

The Oracle Configure, Price, Quote (CPQ) Orchestrated System supports the following account operations when provisioning a user:

- Create Account
- Update Account
- Enable Account
- Disable Account
- Change Password
- Assign Sales Group
- Remove Sales Group
- Add Admin Group
- Remove Admin Group
- Add Permissions
- Remove Permissions

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Oracle Configure, Price, Quote (CPQ)](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-integrate-with-cpq.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Configure, Price, Quote (CPQ) attributes.

Account Attribute Mapping
Entity Oracle Configure, Price, Quote (CPQ) Account Attribute Oracle Configure, Price, Quote (CPQ) Account Attribute Oracle Configure, Price, Quote (CPQ) Display name
Personal Information partyNumber uid Unique Id
login name User login
password password Password
email email Email
admin admin Admin
firstName firstName First name
lastName lastName Last name
phone phone Phone number
jobTitle jobTitle Title
company.name company Company
User Settings type.value type Type
isWebServicesOnly isWebServicesOnly Web services only
status.value status Status
enabledForSso.value enabledForSso.value Enabled for SSO
Additional Settings units.value unit Unit
organizations organizations Organizations
approvalDelegate approvalDelegate Delegated approver
isNotifyEmail emailNotification Email notification
Sales Group variableName salesGroups Sales groups
Admin Group variableName adminGroups Admin groups
Permissions variableName permissions Permissions

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Oracle Configure, Price, Quote (CPQ) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`
