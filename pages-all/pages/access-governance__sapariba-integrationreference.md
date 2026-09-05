# SAP Ariba Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sapariba-integrationreference.htm
- Fetched: 2026-09-05 03:16 CDT

# SAP Ariba Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between SAP Ariba and Oracle Access Governance.

## SAP Ariba Components Certified for Integration with Oracle Access Governance

Lists the software components and their versions required for integrating SAP Ariba with Oracle Access Governance.

### Certified Components

Certified Components
Component Type Component
Managed System SAP Ariba
API
- For Account Provisioning : Import Users web service,`version 1`
- For Reconciliation: Master Data Retrieval API for Sourcing,`version 1.0.0`

## Supported Configuration Modes for SAP Ariba

You can use Oracle Access Governance integrations to set up different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

The SAP Ariba Orchestrated System supports the following modes:
- Managed System

You can manage SAP Ariba user accounts and groups from Oracle Access Governance.

## Supported Operations when Provisioning to SAP Ariba

SAP Ariba Orchestrated System supports the user management and group management operations.

The SAP Ariba Orchestrated System supports the following account operations when provisioning a user:
- Create User
- Update User
- Enable User
- Disable User
- Assign Groups
- Revoke Groups

## Default Supported Attributes

Oracle Access Governance supports the following default SAP Ariba attributes.

These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from SAP Ariba:

  
`UniqueName`will map to`User login`  

- Data for the user accounts as identities being ingested by Oracle Access Governance from SAP Ariba.

  
`PasswordAdapter`will map to`User Type`  

Default Attributes for SAP Ariba
Entity SAP Ariba Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Transformation Supported? Mandatory?
User UniqueName uid Unique Id
UniqueName name User login Yes Mandatory
Name_en displayName Name Yes Mandatory
EmailAddress email Email Mandatory
PasswordAdapter userType User type Yes, with 'Enterprise User' Mandatory
Organization organization Organization Type: ADMIN
Supervisor supervisor Supervisor No
supervisorUserType Supervisor user type No
LocaleID locale Locale No
Phone phone Phone number No
active status Status No
TimeZoneID timezone Timezone No
