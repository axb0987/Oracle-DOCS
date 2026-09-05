# Oracle Infinity Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-infinity-oracle-infinity-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Infinity Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Infinity and Oracle Access Governance.

## Oracle Infinity Components Certified for Integration with Oracle Access Governance

The Oracle Infinity components that you can integrate with are listed below.

Certified Components
Component Type Component
System Oracle Infinity as a Managed System as Oracle Cloud Services.

## Supported Configuration Modes for Oracle Infinity Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for provisioning accounts.

Oracle Infinity Orchestrated System supports the following mode:
- Managed System

You can manage Oracle Infinity accounts.

## Supported Operations When Provisioning to Oracle Infinity

When you provision an account from Oracle Access Governance to Oracle Infinity certain operations are supported.

The Oracle Infinity Orchestrated System supports the following account operations when provisioning a user:

- Create Account
- Delete Account

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Oracle Infinity](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-infinity-integrate-with-infinity.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Infinity attributes.

### Default Supported Account Attributes

Entity Oracle Infinity Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User id (__UID__) uid Unique Id
userLogin (__NAME__) name User login

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Oracle Infinity orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`
