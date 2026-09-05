# Workday Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/workday-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Workday Integration Reference

## Workday Components Certified for Integration with Oracle Access Governance

The Workday components that you can integrate with are listed below.

Certified Components
Component Type Component
System Workday release 2020R2 or later

## Supported Configuration Modes for Workday Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Workday Orchestrated System supports the following modes:
- Authoritative Source

You can use Workday as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage Workday accounts, security groups and roles.

## Supported Operations When Provisioning To Workday

When you provision an account from Oracle Access Governance to Workday certain operations are supported.

The Workday Orchestrated System supports the following account operations when provisioning a user:
Note  
  
A worker is a generic term for any user registered in the Workday system. A worker with account only is a specific type of worker who is not an employee but still has a Workday account for certain purposes. This might include contractors, consultants, or other non-employee individuals who need access to Workday for specific tasks, like accessing benefits information or timekeeping, without being directly employed,

Supported operations
Operation Worker Worker with Account Only
Create Yes Yes
Update Yes Yes
Change Password Yes Yes
Enable No No
Disable No No
Revoke No No
Assign Security Group Yes Yes
Remove Security Group Yes Yes
Assign Role Yes Yes
Remove Role Yes Yes
Note  
  
Enable, disable, and revoke actions are not supported. To end an account in Workday, the employee must be terminated, or the contingent worker’s contract must be ended. Even after these actions, the account remains present in the Workday target system and is not completely deleted.

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with Workday](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-workday.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Workday attributes.

Default Attributes for Workday - Authoritative Source
Entity Workday Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User WID(__UID__) uid Unique Id
employeeID(__NAME__) name Employee user name
firstName firstName First name
lastName lastName Last name
fullName displayName Name
managerID managerUid Manager
emailAddressWork email Email
phoneNumberWork phoneNumber Phone number
phoneNumberHome homePhone Home phone
positionTitle title Title
streetAddress postalAddress Postal address
state state State
country country Country
postalCode postalCode Postal code
continuousServiceDate startDate Start date
terminationDate endDate End date
Active(__ENABLE__) status Status
costCenter costCenter Costcenter
company company Company
region region Region
userName(userID) accountUserName Account user name

Default Attributes for Workday - Managed System
Entity Workday Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User workerID(__UID__) uid Unique Id
employeeID(__NAME__) name User Login
workdayID workdayID Workday id
userName(userID) AccountUserName Account user name
password(__PASSWORD__) password Password
accountDisabled accountDisabled Account disabled
firstName firstName First name
lastName lastName Last name
fullName fullName Name
emailAddressWork workEmail Email
emailAddressHome homeEmail Home email
phoneNumberWork phoneNumber Phone number
phoneDeviceTypeWork workPhoneDeviceType Phone type
phoneNumberHome homePhone Home phone
phoneDeviceTypeHome homePhoneDeviceType Home phone type
municipality city City
postalCode postalCode Postal code
positionTitle position Position
workerType employeeType Employee type
hireDate(continuousServiceDate) provisionedOnDate Hire date
terminationDate terminationDate Termination date
managerName managerUid Manager
costCenter costCenter Cost center
supervisoryOrg supervisoryOrganization Supervisory organization
streetAddress address Address
country country Country
state state State
status(__ENABLE__) statusStatus
Roles Roles roles Roles
workdayID uid UID
Role name Name
Security Groups Security Groups securityGroups Security groups
workdayID uid UID
Security_Group name Name

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Workday orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new.

Screen value :

`Employee user name = Employee user name`

Attribute name :

`Account.employeeID(__NAME__) = Identity.name`
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.employeeID(__NAME__)e = Identity.name`
