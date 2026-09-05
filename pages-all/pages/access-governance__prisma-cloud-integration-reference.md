# Prisma Cloud Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/prisma-cloud-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Prisma Cloud Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Prisma Cloud and Oracle Access Governance.

## Components Certified for Integration with Oracle Access Governance

The components that you can integrate with are listed below.

Certified Components
Component Type Component
System Prisma Cloud as a Managed System for all Cloud versions.

## Supported Configuration Modes for Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for provisioning accounts.

Prisma Cloud Orchestrated System supports the following modes:
- Managed System

You can manage accounts and entitlements for Prisma Cloud.

## Supported Operations When Provisioning to Prisma Cloud

When you provision an account from Oracle Access Governance to Prisma Cloud certain operations are supported.

The Prisma Cloud Orchestrated System supports the following account operations when provisioning a user:
- Create Account
- Update Account
- Delete Account
- Enable Account
- Disable Account
- Assign Groups
- Remove Groups For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#oracle-access-governance-integration-functional-overview)and[Integrate with Prisma Cloud](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-prisma-cloud.htm#integrate-with-prisma-cloud).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Infinity attributes.

Default Supported Account Attributes
Entity Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display Name
User __UID__(id) uid Unique Id
__NAME__(username) name User login
__ENABLE__(active) status Status
name.familyName lastName Last Name
name.formatted formattedName Formatted name
name.givenName firstName First name
primaryEnail email Email
primaryEmailType emailType Email type
SecondaryEmails secondaryEmails secondaryEmails Secondary emails
type type Type
__GROUP__ groups Groups

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`
