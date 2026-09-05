# ARCON PAM Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/arcon-pam-integration-reference.htm
- Fetched: 2026-09-05 03:13 CDT

# ARCON PAM Integration Reference

## Arcon PAM Components Certified for Integration with Oracle Access Governance

The Arcon PAM components that you can integrate with are listed below.

Certified Components
Component Type Component
System ARCON Privileged Access Management

## Supported Configuration Modes for Arcon PAM Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Arcon Privileged Access Management (Arcon PAM) Orchestrated System supports the following mode:
- Managed System

You can manage Arcon PAM accounts, groups and roles.

## Supported Operations When Provisioning To Arcon PAM

When you provision an account from Oracle Access Governance to Arcon Privileged Access Management (Arcon PAM) certain operations are supported.

The Arcon PAM Orchestrated System supports the following account operations when provisioning a user:
- Create User
- Update User
- Enable User
- Disable User
- Add Role
- Remove Role
- Add Group
- Remove Group
- Add Line of Business
- Remove Line of Business
- Add Multi-factor Authentication
- Remove Multi-factor Authentication
- Add Service
- Remove Service
Note  
  
Only Permanent services are currently supported. One-time and Time-based services are not currently supported.

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with ARCON PAM](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-arcon-pam.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Arcon PAM attributes.

These attributes are mapped depending on the direction of the connection, for example:
- Data being provisioned into Arcon PAM from Oracle Access Governance:

  
`account.lastName`will map to`User.name.familyName`  

Default Attributes for Arcon PAM
Entity Arcon PAM Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User id uid Unique Id
userName name User login
displayName displayName Name
ValidTillDate endDate End date
emails.value emails Email
domainName domainName Domain name
phoneNumbers.value phone Phone
userTypeId userType User type
name.formatted fullName Full name
name.familyName lastName Last name
name.givenName firstName First name
name.middleName middleName Middle name
LobPrimary primaryLob Primary line of businesses
IsActive status Status
password password Password
Roles roles Roles
Groups groups Groups
LOBS lobs Line of businesses
Multi-factor Authentication userDualAuthFactType mfas Multi-factor authentications
Services AccessTypeId accessTypeId Access type
StartDateTime accessDurationStartDate Access duration start date
EndDateTime accessDurationEndDate Access duration end date
hours perSessionHours Per session duration in hours
minutes perSessionMinutes Per session duration in minutes
StartTime accessPeriodStartTime Access period start time
EndTime accessPeriodEndTime Access period end time

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Arcon PAM orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.name = Identity.userName`
