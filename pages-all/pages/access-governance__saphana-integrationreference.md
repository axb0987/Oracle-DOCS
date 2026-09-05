# SAP S/4HANA Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/saphana-integrationreference.htm
- Fetched: 2026-09-05 03:16 CDT

# SAP S/4HANA Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between SAP S/4HANA and Oracle Access Governance.

## SAP S/4HANA Components Certified for Integration with Oracle Access Governance

Lists the software components and their versions required for integrating SAP S/4HANA with Oracle Access Governance.

### Certified Components

Certified Components
Component Type Component
Managed System SAP S/4HANA
API
- For Account Provisioning :`ManageBusinessUserIn`,`v1.0.0`
- For Reconciliation:`QueryBusinessUserIn, v1.0.0`

## Supported Operations when Provisioning to SAP S/4HANA

SAP S/4HANA Orchestrated System supports the user management and role management operations. The SAP S/4HANA orchestrated system supports management for Business User and Workforce User.

The SAP S/4HANA Orchestrated System supports the following account operations when provisioning a user:
- Update Account (only LockedIndicator )
- Enable Account
- Disable Account
- Add Role
- Remove Role

For more details, see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with SAP S4Hana](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-s4hana.htm#sap-s4hana-functional-overview).

## Supported Configuration Modes for SAP S/4HANA

You can use Oracle Access Governance integrations to set up different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

The SAP S/4HANA Orchestrated System supports the following modes:
- Managed System

You can manage SAP S/4HANA user workforce and business user accounts and roles from Oracle Access Governance.

## Default Supported Attributes

Oracle Access Governance supports the following default SAP S/4HANA attributes.

These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from SAP S/4HANA:

  
`User login`will map to`Employee user name`  

Default Attributes for SAP S/4HANA
Entity SAP S/4HANA Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
User PersonID uid Unique Id
UserLogin name User name
UserID userID User ID
PersonExternalID personExternalID person external id
FirstName firstName First name
LastName lastName Last name
PersonFullName displayName Name
MiddleName middleName Middle name
EmailAddress email Email
PersonUUID personUUID Person UUID
StartDate startDate Start date
EndDate endDate End date
LockedIndicator accountisLockedout Account locked
status status Status
