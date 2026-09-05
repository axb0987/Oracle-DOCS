# PeopleSoft Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/peoplesoft-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# PeopleSoft Integration Reference

## PeopleSoft Components Certified for Integration with Oracle Access Governance

The PeopleSoft components that you can integrate with, depends on the configuration mode you selected for the orchestrated system.

### Certified Components in Authoritative Source Configuration Mode

Certified Components in Authoritative Source Configuration Mode
Component Type Component
System The versions of PeopleSoft HCM, ELM, and FSCM you can use as an authoritative (trusted) source of identity information for Oracle Access Governance are:
- PeopleSoft HCM, ELM, or FSCM 8.9 with PeopleTools 8.49
- PeopleSoft HCM, ELM, or FSCM 8.9 with PeopleTools 8.50
- PeopleSoft HCM, ELM, or FSCM 9.0 with PeopleTools 8.49
- PeopleSoft HCM, ELM, or FSCM 9.0 with PeopleTools 8.50
- PeopleSoft HCM, ELM, or FSCM 9.0 with PeopleTools 8.52
- PeopleSoft HCM, ELM, or FSCM 9.1 with PeopleTools 8.50
- PeopleSoft HCM, ELM, or FSCM 9.1 with PeopleTools 8.51
- PeopleSoft HCM, ELM, or FSCM 9.1 with PeopleTools 8.52
- PeopleSoft HCM, ELM, or FSCM 9.1 with PeopleTools 8.53
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.53
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.54
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.55
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.56
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.57
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.58
- PeopleSoft HCM, ELM, or FSCM 9.2 with PeopleTools 8.59

### Certified Components in Managed System Configuration Mode

Certified Components in Managed System Configuration Mode
Component Type Component
System The versions of PeopleSoft PeopleTools you can use to manage PeopleTools-based PSOPRDEFN user profile records in PeopleSoft applications are:
- PeopleTools 8.53
- PeopleTools 8.54
- PeopleTools 8.55
- PeopleTools 8.56
- PeopleTools 8.57
- PeopleTools 8.58
- PeopleTools 8.59
- PeopleTools 8.60.05
- PeopleTools 8.61.03
Note  
  
If you are using PeopleTools 8.54, full reconciliation operation may not work as expected. Apply PeopleSoft Patch 21109998 using the following URL for this operation to work successfully:

`https://support.oracle.com/`

### Certified Components in both Modes

Certified Components in both Modes
Component Type Component
System The versions of PeopleSoft HCM, ELM, and FSCM you can use in either Authoritative Source or Managed System mode are:
- PeopleSoft HCM, ELM, or FSCM 9.1
- PeopleSoft HCM, ELM, or FSCM 9.2
Database Oracle

## PeopleSoft Components Required For Integration with Oracle Access Governance

Integration of PeopleSoft with Oracle Access Governance requires several components to be present in your PeopleSoft environment.

Ensure the following components are installed in your PeopleSoft environment:
- Tuxedo and Jolt (the application server)
- PeopleSoft Internet Architecture (PIA)
- PeopleSoft Application Designer (2-tier mode)

## Configure Oracle Database Schema User Account

To access the PeopleSoft database schema you will need to create a service account on the Oracle database supporting PeopleSoft.

- Sign in to the Oracle database as a database administrator using SQL*Plus or similar. Create a service account using the following statements:
```

```

For example:
```

```

- Grant permission to PeopleSoft schema components to the service account you created, where`<PSFT>`is the name of the PeopleSoft schema for your environment. The list of schema components is different for each PeopleSoft component (HCM, ELM, and FSCM).

For PeopleSoft HCM:
```

```

For PeopleSoft ELM:
```

```

For PeopleSoft FSCM:
```

```

- Logout of the database and reconnect as the service account you created. Create synonyms for the schema components to which you granted access.

For PeopleSoft HCM:
```

```

For PeopleSoft ELM:
```

```

For PeopleSoft FSCM:
```

```

- Remain connected as the service account and create views to allow Oracle Access Governance to retrieve employee and person of interest (POI) information. There are two views,`Job_data_view.sql`for job data, and`Personal_data_view.sql`for personal data. These support the following features:
- Enables reconciliation of employee data, including those employees who do not have a user profile in PeopleSoft.
- Enables reconciliation of persons of interest (POI) such as contractors, where no PeopleSoft user profile is present.
- Supports attributes such as multiple job profiles, and manager department hierarchy.
- Allows for complex customizations when applying transformations during attribute reconciliation, such as having different attributes for employees versus POIs.

You can download the latest version of these scripts from[GitHub](https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/PEOPLESOFT)at`https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/PEOPLESOFT/1.0`.
Note  
  
If you have used a previous version of Oracle Access Governance where these views have not been created then you will see an error on the next data load. To rectify this, create the views as described and resubmit your data load.
Note  
  
Where a select field is set to null, you are able to substitute this with a value of your choice, allowing for customization of the view results.

## Configure PeopleSoft Service Account Using Peoplesoft PIA Web Interface

Integrating with PeopleSoft requires connecting to the PeopleSoft application using a service account.

You can create a service user to use for connecting to the PeopleSoft application by performing the following steps.
- Invoke the Peoplesoft PIA Web interface in a browser and navigate to Permission Lists.

People Tools → Security → Permission Lists
- Add a new value: AGCS_PERMLIST
- In the permission list add and assign access to the following Component Interfaces according to the values given in the table.
Note  
  
For PeopleSoft ELM and FSCM, CI_PERM_LIST is not available. Assign access for CI_PERM_LIST only to a PeopleSoft HCM configuration.

Component Interface Permissions
Component Interface Method Method Access
USER_PROFILE
Cancel Full Access
Get Full Access
Create Full Access
Save Full Access
ResetPassword Full Access
ResetPassword_Alpha Full Access
SetPassword Full Access
SetDescription Full Access
DELETE_USER_PROFILE
Cancel Full Access
Find Full Access
Get Full Access
Save Full Access
ROLE_MAINT
Cancel Full Access
Find Full Access
Get Full Access
Create No Access
Save No Access
CURRENCY
Cancel Full Access
Find Full Access
Get Full Access
Create No Access
Save No Access
CI_PERM_LIST (PeopleSoft HCM only)
Cancel Full Access
Find Full Access
Get Full Access
Create No Access
Save No Access
- Navigate to Roles.

People Tools → Security → Roles
- Add a new value: AGCS_ROLE
- Add AGCS_PERMLIST to the Permission List.
- Navigate to User Profile

People Tools → Security → User Profiles → User Profile
- Add a new value: AGCSSA
- Add Symbolic ID as SYSADM1.
- Set and confirm the password.
- Set ID Type as NONE.
- From Roles, select AGCS_ROLE.
- Save your changes.

## Supported Configuration Modes for PeopleSoft Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

PeopleSoft Orchestrated System supports the following modes:
- Authoritative Source

You can use PeopleSoft HRMS as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage PeopleTools-based PSOPRDEFN user profile records in PeopleSoft applications including Role and Permission List assignments to these records.

## Supported Operations When Provisioning To PeopleSoft

When you provision an account from Oracle Access Governance to PeopleSoft certain operations are supported.

The PeopleSoft Orchestrated System supports the following account operations when provisioning a user:
- Create User
- Update User
- Change Password
- Add Roles
- Remove Roles
Note  
  
Partial Data Load is supported for PeopleSoft HCM, but is not supported for PeopleSoft ELM or FSCM.

## Default Supported Attributes

Oracle Access Governance supports the following default PeopleSoft attributes. These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from PeopleSoft:`User.PROP_FIRST_NAME`will map to`Identity.firstName`
- Data being provisioned into PeopleSoft from Oracle Access Governance:`account.lastName`will map to`User.PROP_LAST_NAME`

PeopleSoft HCM Default Attributes - Authoritative Source
PeopleSoft Entity Attribute Name On PeopleSoft Managed System Oracle Access Governance Identity Attribute Name Oracle Access Governance Identity Attribute Display Name
User EMPL_ID uid Unique Id
EMPL_ID name Employee user name
EMPL_ID employeeNumber Employee number
FIRST_NAME firstName First name
LAST_NAME lastName Last name
MIDDLE_NAME middleName Middle name
PREF_FIRST_NAME PreferredFirstName Preferred first name
EMAIL email Email
PHONE phone Phone
NAME_TITLE title Title
ORGANIZATION_NAME organizationName Organization Name
addresses addresses as entitlement Addresses
COUNTRY country
CITY city
STATE state
ADDRESS1 address1
ADDRESS2 address2
ADDRESS3 address3
POSTAL postal
jobData
EMPL_RCD employeeRecord
EFF_DT startDate
EFF_SEQ employeeSequence
DEPTID department
JOBCODE jobCode
SETID_JOBCODE setIdJobCode
JOB_TYPE jobType
JOB_TITLE jobTitle
POSITION_NBR positionNBR
PER_ORG perOrg
POI_TYPE poiType
SUPERVISOR_ID supervisorUid
HR_STATUS hrStatus
EMPL_STATUS emplStatus
FULL_PART_TIME fullPartTime
ACTION action
ACTION_REASON actionReason
LOCATION_CODE location
POSTALADDRESS postalAddress
STREET street
ADDRESS2 address
CITY city
COUNTY county
STATE state
POSTALCODE postalCode
COMPANY company
EMPL_TYPE emplType
EMPL_CLASS emplClass
OFFICER_CODE officerCode
BUSINESS_UNIT businessUnit
TERMINATION_DT terminationDate
END_DATE endDate
REPORTS_TO reportsTo
MANAGER_DEPARTMENT_CODES managerDepartmentCodes
MANAGER_DEPARTMENT_LEVELS managerDepartmentLevels
MANAGER_DEPARTMENT_TITLES managerDepartmentTitles
DESCRIPTION description
LASTUPDDTTM lastUpdateTimestamp

PeopleSoft ELM and FSCM Default Attributes - Authoritative Source
PeopleSoft Entity Attribute Name On PeopleSoft Managed System Oracle Access Governance Identity Attribute Name Oracle Access Governance Identity Attribute Display Name Employee/User/Both
User EMPL_ID uid Unique Id Both
EMPL_ID name Employee user name Both
EMPL_ID employeeNumber Employee number Both
FIRST_NAME firstName First name Employee
LAST_NAME lastName Last name Employee
MIDDLE_NAME middleName Middle name Employee
PREF_FIRST_NAME PreferredFirstName Preferred first name Employee
EMAIL email Email Employee
PHONE phone Phone Employee
NAME_TITLE title Title Employee
addresses addresses as entitlement Addresses Employee
COUNTRY country
CITY city
STATE state
ADDRESS1 address1
ADDRESS2 address2
ADDRESS3 address3
POSTAL postal
jobData
EMPL_RCD employeeRecord
EFF_DT startDate
EFF_SEQ employeeSequence
DEPTID department
JOBCODE jobCode
SETID_JOBCODE setIdJobCode
JOB_TYPE jobType
JOB_TITLE jobTitle
POSITION_NBR positionNBR
PER_ORG perOrg
SUPERVISOR_ID supervisorUid
EMPL_STATUS emplStatus
FULL_PART_TIME fullPartTime
ACTION action
ACTION_REASON actionReason
LOCATION_CODE location
COMPANY company
EMPL_TYPE emplType
EMPL_CLASS emplClass
OFFICER_CODE officerCode
BUSINESS_UNIT businessUnit
END_DATE endDate
REPORTS_TO reportsTo
DESCRIPTION description
LASTUPDDTTM lastUpdateTimestamp

PeopleSoft HCM Default Attributes - Managed System
PeopleSoft Entity Attribute Name On PeopleSoft Managed System Oracle Access Governance Account Attribute Name Oracle Access Governance Account Attribute Display Name
User UserID uid Unique Id
UserID name User login
__PASSWORD__ password Password
EmailAddresses~EmailAddress~PrimaryEmail email Email
IDTypes~EMP~Empl_ID employeeId Employee id
IDTypes~CST~Set_ID customerSetId Customer set id
IDTypes~CST~Customer_ID customerId Customer id
IDTypes~VND~Set_ID vendorSetId Vendor set id
IDTypes~VND~Vendor_ID vendorId Vendor id
NavigatorHomePermissionList navigatorHomePermission Navigator home permission
ProcessProfilePermissionList processProfilePermission Process profile permission
RowSecurityPermissionList rowSecurityPermission Row security permission
PrimaryPermissionList primaryPermission Primary permission
UserDescription description Description
MultiLanguageEnabled multiLanguageEnabled Multi language enabled
SymbolicID symbolicId Symbolic id
UserIDAlias userIdAlias User id alias
LanguageCode languageCode Language
CurrencyCode currencyCode Currency
AlternateUserID alternateUserId Alternate user id
EffectiveDateFrom startDate Start date
EffectiveDateTo endDate End date
WorklistUser worklistUser Work list user
EmailUser emailUser Email user
ReassignWork reassignWork Reassign work
ReassignUserID reassignUserId Reassign work to
SupervisingUserID supervisingUserId Supervising user id
AccountLocked status Status

PeopleSoft ELM and FSCM Default Attributes - Managed System
PeopleSoft Entity Attribute Name On PeopleSoft Managed System Oracle Access Governance Account Attribute Name Oracle Access Governance Account Attribute Display Name
User UserID uid Unique Id
UserID name User login
__PASSWORD__ password Password
EmailAddresses~EmailAddress~PrimaryEmail email Email
IDTypes~EMP~Empl_ID employeeId Employee id
IDTypes~CST~Set_ID customerSetId Customer set id
IDTypes~CST~Customer_ID customerId Customer id
IDTypes~VND~Set_ID vendorSetId Vendor set id
IDTypes~VND~Vendor_ID vendorId Vendor id
NavigatorHomePermissionList navigatorHomePermission Navigator home permission
ProcessProfilePermissionList processProfilePermission Process profile permission
RowSecurityPermissionList rowSecurityPermission Row security permission
PrimaryPermissionList primaryPermission Primary permission
UserDescription description Description
MultiLanguageEnabled multiLanguageEnabled Multi language enabled
SymbolicID symbolicId Symbolic id
UserIDAlias userIdAlias User id alias
LanguageCode languageCode Language
CurrencyCode currencyCode Currency
AlternateUserID alternateUserId Alternate user id
EffectiveDateFrom startDate Start date
EffectiveDateTo endDate End date
WorklistUser worklistUser Work list user
EmailUser emailUser Email user
ReassignWork reassignWork Reassign work
ReassignUserID reassignUserId Reassign work to
SupervisingUserID supervisingUserId Supervising user id
AccountLocked status Status
role role as entitlement Roles

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each Orchestrated System.

The default matching rule for PeopleSoft orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new

Screen value :

`Employee user name = Employee user name`

Attribute name :

`Identity.userName = Identity.userName`
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`Employee id = Employee number`

Attribute name :

`Account.UserID = Identity.uid`.

Note  
  
If you have an existing orchestrated system created prior to support for employees/POIs then the account matching rule will display as`User login = Employee user name`. This should be modified to the value shown above, that is,`Employee id = Employee number`
