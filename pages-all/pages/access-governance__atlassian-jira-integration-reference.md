# Atlassian JIRA Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/atlassian-jira-integration-reference.htm
- Fetched: 2026-09-05 03:13 CDT

# Atlassian JIRA Integration Reference

## Atlassian Jira Components Certified for Integration with Oracle Access Governance

The Atlassian Jira components that you can integrate with are listed below.

Certified Components
Component Type Component
System Atlassian Jira

## Supported Configuration Modes for Atlassian Jira Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Atlassian Jira Orchestrated System supports the following mode:
- Managed System

You can manage Atlassian Jira accounts and groups.

## Supported Operations When Provisioning To Atlassian Jira

When you provision an account from Oracle Access Governance to Atlassian Jira certain operations are supported.

The Atlassian Jira Orchestrated System supports the following account operations when provisioning a user:

- Create User
- Revoke User
- Assign Group
- Remove Group
- Add Product

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with Atlassian JIRA](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-atlassian-jira.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Atlassian Jira attributes.

Default Attributes for Atlassian Jira - Managed System
Atlassian Jira Entity Atlassian Jira Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User accountId uid Account type
accountType accountType Account type
emailAddress name User login
timeZone timeZone Time zone
locale locale Locale
displayName displayName Name
Products products products Products
Group groupId groups Groups

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Atlassian Jira orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Email`

Attribute name :

`Account.emailAddress = Identity.name`
