# Oracle Health EHR (formerly Cerner Millennium) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-health-ehr-formerly-cerner-millennium-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Health EHR (formerly Cerner Millennium) Integration Reference

## Oracle Health EHR (formerly Cerner Millennium) Components Certified for Integration with Oracle Access Governance

The Oracle Health EHR (formerly Cerner Millennium) to integrate with Orchestrated System is as follows.

### Certified Components

Certified Components
Component Type Component
System The versions of Oracle Health EHR (formerly Cerner Millennium) you can use for Oracle Access Governance are:
- Cerner Millennium, Security provisioning engine version 7.0.0

## Supported Configuration Modes for Oracle Health EHR (formerly Cerner Millennium)

You can use Oracle Access Governance integrations to set up different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

The Oracle Health EHR (formerly Cerner Millennium) Orchestrated System supports the following modes:
- Managed System

You can manage Oracle Health EHR (formerly Cerner Millennium) user profile records.

## Supported Operations When Provisioning To Oracle Health EHR (formerly Cerner Millennium)

To provision an account from Oracle Access Governance to Oracle Health EHR (formerly Cerner Millennium) there are certain operations that are supported.

The Oracle Health EHR (formerly Cerner Millennium) Orchestrated System supports the following account operations when provisioning a user:
- Create Account
- Update Account
- Enable Account
- Disable Account
- Password Change
- Add Organization
- Remove Organization
- Add Organization Group
- Remove Organization Group
- Add Personal Alias
- Remove Personal Alias
- Add Personal Group
- Remove Personal Group
- Add PPR access
- Remove PPR access
- Add Taxonomy
- Remove Taxonomy
- Add Role profile
- Remove Role profile

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Health EHR (formerly Cerner Millennium) attributes.

These attributes are mapped depending on the direction of the connection, for example:
- Data for user accounts, and personal alias as Identities being ingested by Oracle Access Governance from Oracle Health EHR (formerly Cerner Millennium).
- Data for the user accounts as Identities being ingested by Oracle Access Governance from Oracle Health EHR (formerly Cerner Millennium).

Default Attributes
Oracle Health EHR (formerly Cerner Millennium) User Entity Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name
ID uid Unique Id
username name User login
firstName firstName First name
lastName lastName Last name
middleName middleName Middle name
suffix suffix Honorific suffix
title title Title
PhysicianInd physician Physician
gender gender Gender
directoryIndicator directory Directory
logicalDomain logicalDomain Logical domain
birthdate dateOfBirth Date of birth
beginEffectiveDateTime startDate Start date
endEffectiveDateTime endDate End date

position position Position
inactiveAccount status Status
Password password Password
Organization Organization organizations Organizations
PersonalGroup personnelGroup personalGroups Personal groups
Organization Group organizationGroup organizationGroups Organization groups
Personal alias personnelAlias personalAliases Personal aliases
toPsoID aliasId Alias id
aliasPool aliasPool Alias pool
type aliasType Alias type
alias aliasName Alias name
beginEffectiveDateTime startDate Start date
endEffectiveDateTime endDate End date
Patient Provider Relationship (PPR access) pprAccess pprAccesses PPR acesses
Taxonomy Taxonomy taxonomies Taxonomies
toPsoID taxonomyPsoId Taxonomy PSO id
taxonomyId taxonomyId Taxonomy id
taxonomyType taxonomyType Taxonomy type
beginEffectiveDateTime startDate Start date
endEffectiveDateTime endDate End date
Role Profile roleProfile
toPsoID toPsoID Role PDO id
position position Position
display display display

## Troubleshooting

The following are the troubleshooting steps for Oracle Health EHR (formerly Cerner Millennium).
- The following error message is displayed while performing operations:

ERROR

Error occurred while establishing SOAP connection "OR' call: Connection Refused: connect.

Resolution

The Cerner server must be running and accessible from the agent location.
-
