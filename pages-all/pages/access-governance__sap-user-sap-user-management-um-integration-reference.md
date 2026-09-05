# SAP User Management (UM) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-sap-user-management-um-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# SAP User Management (UM) Integration Reference

## SAP User Management (UM) Components Certified for Integration with Oracle Access Governance

The SAP User Management (UM) components that you can integrate with are listed below.

Certified Components
Component Type Component
System

The managed system can be any one of the following:
- 

SAP NetWeaver 7.4 with SAP BASIS 7.40 and SAP Business Suite release: BS 7i 2013 with the following constituents:

SAP Enhancement Package 7 for SAP ERP 6.0

SAP Enhancement Package 3 for SAP CRM 7.0

SAP Enhancement Package 3 for SAP SRM 7.0

SAP Enhancement Package 3 for SAP SCM 7.0
- 

SAP NetWeaver 7.5 with SAP BASIS 7.50 and SAP Business Suite release: BS 7i 2016 with the following constituents:

SAP Enhancement Package 8 for SAP ERP 6.0

SAP Enhancement Package 4 for SAP CRM 7.0

SAP Enhancement Package 4 for SAP SRM 7.0

SAP Enhancement Package 4 for SAP SCM 7.0

SAP BW/4 HANA 1.0 with component DW4CORE Release 100 SP 0003
- 

SAP NetWeaver 7.51 with SAP BASIS 7.51

SAP S/4 HANA 1610 with component S4CORE Release 101 SP 0000
- 

SAP ABAP Platform 1809

SAP S/4HANA 1809 with component S4CORE Release 103 SP 0000

SAP BW/4 HANA 2.0 with component DW4CORE Release 200 SP 0001

SAP BPC 11.1 with component BPC4HANA Release 200 SP 0001
- 

SAP ABAP Platform 1909

SAP S/4HANA 1909 with component S4CORE Release 104 SP 0000
- 

SAP ABAP Platform 2020

SAP S/4HANA 2020 with component S4CORE Release 105 SP 0000
- 

SAP ABAP Platform 2021

SAP S/4HANA 2021 with component S4CORE Release 106 SP 0000
- 

SAP ABAP Platform 2022

SAP S/4HANA 2022 with component S4CORE Release 107 SP 0000
External Code

The connector works with SAP JCo 3.0.2 or later. The following SAP custom code files are required:
- 

sapjco3.jar version 3.0.2 or later
- 

Additional file for Linux: libsapjco3.so version 3.0

Note: There are different distribution packages (JCo) 3.0 available for various supported platforms and processors. See, JCo documentation for more information about using JCo 3.0 packages as per your environment.

## Supported Configuration Modes for SAP User Management (UM) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

SAP User Management (UM) Orchestrated System supports the following mode:
- Managed System

You can manage SAP User Management (UM) accounts.

## Supported Operations When Provisioning To SAP User Management (UM)

When you provision an account from Oracle Access Governance to SAP User Management (UM) certain operations are supported.

The SAP User Management (UM) Orchestrated System supports the following account operations when provisioning a user:

- Create user
- Update user
- Delete user
- Reset password
- Add group
- Remove group
- Add role
- Remove role
- Add parameter
- Remove parameter
- Add profile
- Remove profile

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with SAP User Management (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-integrate-oracle-access-governance-with-sap-user-management-um.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default SAP User Management (UM) attributes.

Default Attributes for SAP User Management (UM) - Managed System
Entity SAP User Management (UM) Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User USERNAME;BAPIBNAME name User login
BAPIPWD password Password
USERNAME;BAPIBNAME uid Unique Id
User Lock;NONE;NONE;NONE lockOut User lock
FIRSTNAME;ADDRESS;FIRSTNAME;ADDRESSX firstName First name
LASTNAME;ADDRESS;LASTNAME;ADDRESSX lastName Last name
TITLE_P;ADDRESS;TITLE_P;ADDRESSX title Title
USERALIAS;ALIAS;BAPIALIAS;ALIASX alias Alias
E_MAIL;ADDRESS;E_MAIL;ADDRESSX email Email
TEL1_NUMBR;ADDRESS;TEL1_NUMBR;ADDRESSX telephoneNumber Telephone number
TEL1_EXT;ADDRESS;TEL1_EXT;ADDRESSX telephoneExtension Telephone extension
GLTGV;LOGONDATA;GLTGV;LOGONDATAX startDate Start date
GLTGB;LOGONDATA;GLTGB;LOGONDATAX endDate End date
FAX_NUMBER;ADDRESS;FAX_NUMBER;ADDRESSX faxNumber Fax number
FAX_EXTENS;ADDRESS;FAX_EXTENS;ADDRESSX faxExtension Fax extension
BUILDING_P;ADDRESS;BUILDING_P;ADDRESSX building Building
ROOM_NO_P;ADDRESS;ROOM_NO_P;ADDRESSX roomNumber Room number
FLOOR_P;ADDRESS;FLOOR_P;ADDRESSX floorNumber Floor number
FUNCTION;ADDRESS;FUNCTION;ADDRESSX function Function
DEPARTMENT;ADDRESS;DEPARTMENT;ADDRESSX department Department
ACCNT;LOGONDATA;ACCNT;LOGONDATAX accountingNumber Accounting number
KOSTL;DEFAULTS;KOSTL;DEFAULTSX costCenter Cost center
LANGU;DEFAULTS;LANGU;DEFAULTSX logonLanguage Logon language
USTYP;LOGONDATA;USTYP;LOGONDATAX userType User type
DATFM;DEFAULTS;DATFM;DEFAULTSX dateFormat Date format
TZONE;LOGONDATA;TZONE;LOGONDATAX timeZone Time zone
START_MENU;DEFAULTS;START_MENU;DEFAULTSX startMenu Start menu
COMPANY;COMPANY;COMPANY;COMPANYX company Company
LIC_TYPE;UCLASS;UCLASS;UCLASSX contractualUserType Contractual user type
COMM_TYPE;ADDRESS;COMM_TYPE;ADDRESSX communicationType Communication type
LANGU_P;ADDRESS;LANGU_P;ADDRESSX communicationLanguage Communication language
PERNR personnelNumber Personnel number
Entitlement
Groups GROUPS~USERGROUP groups Groups
Parameter PARAMETER1~PARID parameterID Parameter Id
PARAMETER1~PARVA parameterValue Parameter value
Profile PROFILES~PROFILE profileName Profile name
Role ACTIVITYGROUPS~AGR_NAME roleName Role name
ACTIVITYGROUPS~FROM_DAT startDate Start date
ACTIVITYGROUPS~TO_DAT endDate End date

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the SAP User Management (UM) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.USERNAME;BAPIBNAME = Identity.name`
