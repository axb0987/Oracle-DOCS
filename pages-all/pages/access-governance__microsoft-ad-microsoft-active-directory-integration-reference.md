# Microsoft Active Directory Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/microsoft-ad-microsoft-active-directory-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Microsoft Active Directory Integration Reference

## Microsoft Active Directory Components Certified for Integration with Oracle Access Governance

The Microsoft Active Directory components that you can integrate with are listed below.

Certified Components
Component Type Component
System Microsoft Active Directory/ Microsoft Active Directory Lightweight Directory Services (AD LDS)
- Installed on Microsoft Windows Server 2025, 64-bit platform
- Installed on Microsoft Windows Server 2022, 64-bit platform
- Installed on Microsoft Windows Server 2019, 64-bit platform.
- Installed on Microsoft Windows Server 2016, 64-bit platform.
- Installed on Microsoft Windows Server 2012, 64-bit platform.
- Installed on Microsoft Windows Server 2012 R2, 64-bit platform.
- Installed on Microsoft Windows Server 2008, both 32-bit and 64-bit platforms.
- Installed on Microsoft Windows Server 2008 R2, both 32-bit and 64-bit platforms.

## Supported Configuration Modes for Microsoft Active Directory Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Microsoft Active Directory Orchestrated System supports the following mode:
- Authoritative Source

You can use Microsoft Active Directory as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage Microsoft Active Directory accounts and groups.

## Supported Operations When Provisioning To Microsoft Active Directory

When you provision an account from Oracle Access Governance to Microsoft Active Directory certain operations are supported.

The Microsoft Active Directory Orchestrated System supports the following account operations when provisioning a user:

- Create user
- Update user
- Delete user
- Enable user
- Disable user
- Reset password
- Add group
- Remove group

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-microsoft-active-directory.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Microsoft Active Directory and Microsoft Active Directory Lightweight Directory Services attributes.

Default Attributes for Microsoft Active Directory/Microsoft Active Directory Lightweight Directory Services - Authoritative Source
Entity Microsoft Active Directory/Microsoft Active Directory Lightweight Directory Services Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User ObjectGUID uid Unique Id
sAMAccountName name Employee user name
givenName firstName First name
middleName middleName Middle name
sn lastName Last name
displayName displayName Name
distinguishedName fullDN User full DN
mail email Email
manager managerLogin Manager
containerDN Container DN

- For Microsoft Active Directory: userAccountControl
- For Microsoft Active Directory Lightweight Directory Services: msDS-UserAccountDisabled status Status
department department Department
l location Location
c country Country
o organizationName Organization Name
homePhone homePhone Home Phone
mobile mobile Mobile
description description Description
employeeNumber employeeNumber Employee Number
employeeId employeeId Employee Id

Default Attributes for Microsoft Active Directory/Microsoft Active Directory Lightweight Directory Services - Managed System
Entity Microsoft Active Directory/Microsoft Active Directory Lightweight Directory Services Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User ObjectGUID uid Unique Id
sAMAccountName name User Login
unicodePwd password Password
distinguishedName fullDn User full DN
userPrincipalName userPrincipalName User principal name
givenName firstName First name
middleName middleName Middle name
sn lastName Last name
displayName fullName Name
cn commonName Common name
__parentDN__ organizationName Organization (Parent distinguished name)

- For Microsoft Active Directory: userAccountControl
- For Microsoft Active Directory Lightweight Directory Services: msDS-UserDontExpirePassword passwordNeverExpires Password never expires
pwdLastSet userMustChangePasswordAtNextLogon User must change password at next logon

- For Microsoft Active Directory: userAccountControl
- For Microsoft Active Directory Lightweight Directory Services: ms-DS-UserPasswordNotRequired passwordNotRequired Password not required
lockoutTime accountisLockedout Account is locked out
telephoneNumber telephoneNumber Telephone number
accountExpires accountExpirationDate Account expiration date
mail email Email
postOfficeBox postOfficeBox Post office box
l location Location
st state State
postalCode zip Zip
homePhone homePhone Home phone
mobile mobile Mobile
pager pager Pager
facsimileTelephoneNumber fax Fax
ipPhone iPPhone IP phone
title title Title
department department Department
company company Company
manager manager Manager
physicalDeliveryOfficeName office Office
c country Country
streetAddress street Street
homeDirectory homedirectory Home directory

- For Microsoft Active Directory: userAccountControl
- For Microsoft Active Directory Lightweight Directory Services: msDS-UserAccountDisabled status Status
o oAsOrganization Organization (o)
description description Description
employeeNumber employeeNumber Employee Number
employeeId employeeId Employee Id
Group Name

memberOf

member groups as entitlement

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Microsoft Active Directory and Microsoft Active Directory Lightweight Directory Services (AD LDS) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new.

Screen value :

`Employee user name = Employee user name`

Attribute name :

`Account.sAMAccountName = Identity.name`
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.sAMAccountName = Identity.name`
