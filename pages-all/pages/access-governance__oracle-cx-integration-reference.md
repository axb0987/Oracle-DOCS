# Oracle Customer Experience (CX) Sales Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-cx-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Customer Experience (CX) Sales Integration Reference

Lists certified components, supported operations, matching rules, default out-of-the-box supported attributes for the integration between Oracle CX (Sales) and Oracle Access Governance.

## Oracle CX (Sales) Components Certified for Integration with Oracle Access Governance

The following Oracle CX (Sales) system considerations

Certified Components
Component Type Component
System Oracle Fusion Cloud Applications 24C (11.13.24.07.0) or later

## Supported Configuration Modes for Oracle CX (Sales) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on the requirement for on-boarding identity data, and provisioning accounts.

Oracle CX (Sales) Orchestrated System supports the following mode:
- Managed System

## Supported Operations when provisioning to Oracle CX (Sales)

Oracle CX (Sales) Orchestrated System supports the following account operations when provisioning an identity:

- Create Account (Resource user with assigned organization and organization role)
- Update Account (Resource user with assigned organization and organization role)
- Delete Account (Resource User gets deleted)
- Assign resource role
- Revoke resource role

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Oracle CX (Sales)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-cx.htm).

## Default Supported Attributes for Oracle CX (Sales)

Oracle Access Governance supports the following default Oracle CX (Sales) attributes.

Default Attributes for Oracle CX - Managed System
Entity Oracle CX Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity Attribute Display Name
resourceUser __UID__ (ResourcePartyNumber) uid Unique Id
__NAME__ (ResourceEmail) name Name
FirstName firstName First name
LastName lastName Last name
BusinessUnit businessUnit Business unit
LegalEntity legalEntity Legal entity
PersonType personType Person type
ResourceStartDate startDate Start date
ResourceEndDate endDate End date
ResourceOrganizationId resourceOrganization Resource Organization
ResourceOrgRoleCode resourceOrganizationRole Resource Organization Role
resourceRoles roles Roles
RESOURCEORGANIZATION __UID__ (OrganizationId) uid Unique Id
__NAME__ (Name) name Name
RESOURCEORGANIZATIONROLE __UID__ (RoleCode) uid Unique Id
__NAME__ (RoleName) name Name
RESOURCEROLE __UID__ (RoleCode) uid Unique Id
__NAME__ (RoleName) name Name
RoleDescription description Description

## Default Matching Rules

To map accounts to identities in Oracle Access Governance, assign a matching rule for each orchestrated system.

The default matching rule for the Oracle CX (Sales) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

To apply matching rule, see[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules).

After implementation of matching rule, you can view[matching insights](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules__insights-matching-rules)
