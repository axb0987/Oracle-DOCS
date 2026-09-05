# ServiceNow UM Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-um-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# ServiceNow UM Integration Reference

## ServiceNow (UM) Components Certified for Integration with Oracle Access Governance

The ServiceNow (UM) components that you can integrate with are listed below.

Certified Components
Component Type Component
System ServiceNow release Xanadu or later

## Supported Configuration Modes for ServiceNow (UM) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

ServiceNow (UM) Orchestrated System supports the following modes:
- Authoritative Source

You can use ServiceNow (UM) as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage ServiceNow (UM) accounts, groups and roles.

## Supported Operations When Provisioning To ServiceNow (UM)

When you provision an account from Oracle Access Governance to ServiceNow (UM) certain operations are supported.

The ServiceNow (UM) Orchestrated System supports the following account operations when provisioning a user:
- Create User
- Update User
- Enable User
- Disable User
- Assign Group
- Assign Role
- Remove Group
- Remove Role

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with ServiceNow (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-servicenow-um.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default ServiceNow (UM) attributes.

Default Attributes for ServiceNow (UM) - Authoritative Source
Entity ServiceNow (UM) Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User sys_id uid Unique Id
name name Employee user name
first_name firstName First name
last_name lastName Last name
active status Status
email email Email
phone phone Phone
mobile_phone mobilePhone Mobile phone

Default Attributes for ServiceNow (UM) - Managed System
Entity ServiceNow (UM) Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Updateable Field Transformation
User sys_id uid Unique Id No No
user_name name User login Yes Yes
first_name firstName First name Yes Yes
last_name lastName Last name Yes Yes
title title Title Yes Yes
department department Department Yes No
phone phone Phone Yes No
mobile_phone mobilePhone Mobile phone Yes No
email email Email Yes Yes
locked_out accountisLockedout Account is locked out Yes No
date_format dateFormat Date format Yes No
calendar_integration calendarIntegration Calendar integration Yes No
time_zone timeZone Time zone Yes No
web_service_access_only webServiceAccessOnly Web service access only Yes No
internal_integration_user internalIntegrationUser Internal integration user Yes No
active status Status Yes No
Role roles Roles No No
Group groups Groups No No

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the ServiceNow (UM) orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.UserEntity.username = Identity.Name`
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.UserEntity.username = Identity.Name`
