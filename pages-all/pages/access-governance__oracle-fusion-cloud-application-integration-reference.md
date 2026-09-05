# Oracle Fusion Cloud Application Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Fusion Cloud Application Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Fusion Cloud Applications and Oracle Access Governance.

## Oracle Fusion Cloud Applications Components Certified for Integration with Oracle Access Governance

The Oracle Fusion Cloud Applications to integrate with Orchestrated System is as follows.

### Certified Components

Certified Components
Component Type Component
System The versions of Oracle Fusion Cloud Applications you can use for Oracle Access Governance are:
- Oracle Fusion Cloud Applications 24C (11.13.24.07.0) or later

## Grant Default Roles and Permissions

Before configuring your orchestrated system you should setup either an HCM or ERP service account and grant permissions required to integrate with Oracle Access Governance.

### Grant Default Roles/Permissions

Role Code for HCM Service Account
Role Name Role Code
IT Security Manager ORA_FND_IT_SECURITY_MANAGER_JOB
Integration Specialist ORA_FND_INTEGRATION_SPECIALIST_JOB
Application Implementation Consultant ORA_ASM_APPLICATION_IMPLEMENTATION_CONSULTANT_JOB
Application Diagnostic Administrator ORA_FND_DIAG_ADMINISTRATOR_JOB
Human Resource Specialist ORA_PER_HUMAN_RESOURCE_SPECIALIST_JOB
HCM Capital Management Integration Specialist ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_INTEGRATION_SPECIALIST_JOB
HCM Capital Management Application Administrator ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_APPLICATION_ADMINISTRATOR_JOB

Role Code for ERP Service Account
Account Type Value
IT Security Manager ORA_FND_IT_SECURITY_MANAGER_JOB
Integration Specialist ORA_FND_INTEGRATION_SPECIALIST_JOB
Application Implementation Consultant ORA_ASM_APPLICATION_IMPLEMENTATION_CONSULTANT_JOB
Access Request Security Administrator ORA_GTG_ACCESS_REQUEST_SECURITY_ADMINISTRATOR_JOB

## Grant Permissions as a Custom User

Create a custom role instead of using the default roles to ensures least privilege by granting only the necessary fine-grained permissions.

Note  
  
You must grant the required data security policies and associate them with the relevant roles to enable access to the appropriate dataset (for example,`/workers`). If the correct data security policies aren't configured, API calls would not fail (200 OK), but the response will contain no data (count would be 0). For further details, see[Data Security Policies](https://docs.oracle.com/en/cloud/saas/applications-common/24b/facsa/data-security.html#Data-Security-Policies).

Privileges
EndPoint/Functionality Privileges In Function Security Policies Application
/userAccounts

Privilege Name: Use REST Service - User Accounts

Privilege Code:`PER_REST_SERVICE_ACCESS_USER_ACCOUNTS_PRIV`HCM
/workers

Privilege Name: Use REST Service - Workers

Privilege Code:`PER_REST_SERVICE_ACCESS_WORKERS_PRIV`HCM
/atomservlet/employee/

Privilege Name: Use Atom Feed - Employees Workspace

Privilege Code:`PER_ATOM_WORKSPACE_ACCESS_EMPLOYEES_PRIV`HCM
/dataSecurities

Privilege Name: Manage Data Access for Users

Privilege Code:`FUN_MANAGE_DATA_ACCESS_FOR_USERS_PRIV`ERP
/finBusinessUnitsLOV

Privilege Name: Get Enterprise Structures Using REST Service

Privilege Code:`FUN_GET_ENTERPRISE_STRUCTURES_REST_SERVICE_PRIV`ERP
/fixedAssetBooksLOV

Privilege Name: View Fixed Asset Books

Privilege Code:`FA_VIEW_FIXED_ASSET_BOOKS_PRIV`ERP

/scim/Users

/scim/Roles

Privilege Name: Use REST Service - Identity Integration

Privilege Code:`ASE_REST_SERVICE_ACCESS_IDENTITY_INTEGRATION_PRIV`HCM + ERP
/setIdSetsLOV/

Privilege Name: Manage Application Reference Data Set

Privilege Code:`FND_APP_MANAGE_REFERENCE_DATA_SET_PRIV`ERP
/commonLookupsLOV

Privilege Name: Manage Application Common Lookup

Privilege Code:`FND_APP_MANAGE_COMMON_LOOKUP_PRIV`HCM + ERP

/advancedAccessRequests/action/getSecurityContextLOV

/advancedAccessRequests/action/getSecurityValue

Privilege Name: Access Requests

Privilege Code:`GTG_ACCESS_REQUESTS_PRIV`ERP
/advancedControlsRolesProvisioning

Privilege Name: Use REST Service for Advanced Access Control Role Analysis

Privilege Code:`GTG_REST_SERVICE_ACCESS_ADVANCED_ACCESS_CONTROL_ROLE_ANALYSIS_PRIV`SOD
/projectOrganizationsLOV

Privilege Name: Get Project Setups

Privilege Code:`PJF_GET_PROJECT_SETUPS_PRIV`ERP
/positionsLov

Privilege Name: Search Position

Privilege Code:`PER_SEARCH_POSITION_PRIV`HCM
/locationsV2

Privilege Name: Manage Location

Privilege Code:`PER_MANAGE_LOCATION_PRIV`HCM
/jobsV2

Privilege Name: Manage Jobs

Privilege Code:`PER_MANAGE_HR_JOB_PRIV`HCM

Aggregated Privileges
EndPoint/Functionality Aggregated Privileges As Role Into The Role Hierarchy Application
/areasOfResponsibility

Privilege Name: Use REST Service - Areas of Responsibility Read-only

Privilege Code:`ORA_PER_REST_SERVICE_ACCESS_AREAS_OF_RESPONSIBILITY_RO`HCM + AOR
/areasOfResponsibility

Privilege Name: Use REST Service - Areas of Responsibility

Privilege Code:`ORA_PER_REST_SERVICE_ACCESS_AREAS_OF_RESPONSIBILITY`HCM + AOR
/hcmCountriesLov

Privilege Name: Use REST Service - HCM Countries List of Values

Privilege Code:`ORA_PER_REST_SERVICE_ACCESS_HCM_COUNTRIES_LOV`HCM

/hcmBusinessUnitsLOV

/legalEmployersLov

Privilege Name: Use REST Service - Workforce Structure List of Values

Privilege Code:`ORA_PER_REST_SERVICE_ACCESS_WORKFORCE_STRUCTURE_LOVS`HCM
/actionsLOV

Privilege Name: Use REST Service - Person Reference Data Lists of Values

Privilege Code:`ORA_PER_REST_SERVICE_ACCESS_PERSON_REFERENCE_DATA_LOVS`HCM
/dataAccessSetLedgersLOV

Privilege Name: Review Revenue Management Accounting Period Status

Privilege Code:`ORA_GL_REVENUE_MANAGEMENT_PERIOD_STATUS_REVIEW_DUTY`ERP
/talentReviewManagersLOV

Privilege Name: Use REST Service - Talent Review Managers List of Values

Privilege Code:`ORA_HRR_REST_SERVICE_ACCESS_TALENT_REVIEW_MANAGERS_LOV`HCM

## Supported Configuration Modes for Oracle Fusion Cloud Applications

You can use Oracle Access Governance integrations to set up different configuration modes depending on the requirement for on-boarding identity data, and provisioning accounts.

### Supported Modes

The Oracle Fusion Cloud Applications Orchestrated System supports the following modes:
- Authoritative Source

You can use Oracle Fusion Cloud Applications as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage Oracle Fusion Cloud Applications user profile records in Oracle Fusion Cloud Applications including Role and Permission List assignments to these records.

## Supported Operations When Provisioning To Oracle Fusion Cloud Applications

To provision an account from Oracle Access Governance to Oracle Fusion Cloud Applications there are certain operations that are supported.

The Oracle Fusion Cloud Applications Orchestrated System supports the following account operations when provisioning a user:
- Create User Account
- Update User Account
- Enable User Account
- Disable User Account
- User Account Linking ( PersonNumber ) [Use Outbound transformation to link person to the user account]
- Change Password
- Add Role Assignment
- Update Role Assignment
- Remove Roles
- Assign Procurement Agent
- Disable Procurement Agent
- Update Procurement Agent
- Assign AOR Template
- Remove AOR Template
Note  
  

- When you update a user account or its attributes directly in Oracle Fusion Cloud Applications, the incremental data load captures the related Procurement Agents and shows the changes in Oracle Access Governance. Direct updates to Procurement Agents in Oracle Fusion Cloud Applications would not be ingested by Oracle Access Governance.
- While linking PersonNumber with the User account, if you get an error, such as "Applying List binding LOV_PersonNumber", then run the following HCM jobs: Compute Users ACL by Events, Compute Users ACL, Compute Users With Large ACL . For steps, see[Schedule ACL Processes](https://docs.oracle.com/en/cloud/saas/human-resources/faeos/schedule-acl-processes.html).

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Fusion Cloud Applications attributes.

### Oracle Fusion Cloud Applications Supported Attributes

- Data with minimum attribute set being ingested by Oracle Access Governance from Oracle Fusion Cloud Applications HCM with support from JML.
- Data with minimum attribute set of person record being ingested by Oracle Access Governance from Oracle Fusion Cloud Applications HCM and ERP modules.
- Data with AOR attribute support. Oracle Access Governance does not manage provisioning or de-provisioning of AORs.

### Default Matching Rules
- Identity Matching Rules : Employee user name Equals Employee user name .
- Account Matching Rules : User login Equals Employee user name .

Default Attributes - Authoritative Source for HCM with JML Support
Attribute Name on Oracle Access Governance Display Name on Oracle Access Governance HCM with User account / Both with User Account HCM with Person / Both with Person ERP
name Name userName emails~EmailAddress,PersonId userName
displayName Display Name displayName names~DisplayName displayName
lastName Last name name~familyName names~LastName name~familyName
firstName First name name~givenName names~FirstName name~givenName
email Email emails~value emails~EmailAddress emails~value
emailType Email Type emails~type emails~EmailType emails~type
status Status active workRelationships~assignments~AssignmentStatusType active
personNumber Person Number workerInformation~personNumber PersonNumber workerInformation~personNumber
managerPersonNumber Manager person number managerPersonNumber (indirect) managerPersonNumber (indirect) NA
managerUid Manager Uid managerScimUserID (indirect) Manager Person ID (indirect) workerInformation~manager
jobCode Job Code workerInformation~job workRelationships~assignments~JobCode workerInformation~job
organizationName Organization Name workerInformation~department workRelationships~assignments~DepartmentName workerInformation~department
businessUnit Business Unit workRelationships~assignments~BusinessUnitId workRelationships~assignments~BusinessUnitId NA
preferredLanguage Preferred Language preferredLanguage preferredLanguage NA
gender Gender legislativeInfo~Gender legislativeInfo~Gender NA
personId Person Identification PersonId PersonId NA
startDate Start Date workRelationships~StartDate workRelationships~StartDate NA
workerType Worker Type workRelationships~WorkerType workRelationships~WorkerType NA
legalEmployerNameWithLegislationCode Legal EmployerName with Legislation Code legalEmployerNameWithLegislationCode legalEmployerNameWithLegislationCode NA
terminationDate Termination Date workRelationships~TerminationDate workRelationships~TerminationDate NA
periodOfServiceId PeriodOfService Id workRelationships~PeriodOfServiceId workRelationships~PeriodOfServiceId NA
legalEntityId Legal Entity Id workRelationships~LegalEntityId workRelationships~LegalEntityId NA
assignmentEffectiveStartDate Assignment Effective Start Date workRelationships~assignments~EffectiveStartDate workRelationships~assignments~EffectiveStartDate NA
positionCode Position Code workRelationships~assignments~PositionCode workRelationships~assignments~PositionCode NA
gradeCode Grade Code workRelationships~assignments~GradeCode workRelationships~assignments~GradeCode NA
locationCode Location code workRelationships~assignments~LocationCode workRelationships~assignments~LocationCode NA
assignmentEffectiveEndDate Assignment Effective End Date workRelationships~assignments~EffectiveEndDate workRelationships~assignments~EffectiveEndDate NA
actionCode Action Code workRelationships~assignments~ActionCode workRelationships~assignments~ActionCode NA
actionTypeCode Action Type Code workRelationships~assignments~ActionTypeCode workRelationships~assignments~ActionTypeCode NA
projectedStartDate ProjectedStartDate workRelationships~assignments~ProjectedStartDate workRelationships~assignments~ProjectedStartDate NA
proposedUserPersonType Proposed User Person Type workRelationships~assignments~ProposedUserPersonType workRelationships~assignments~ProposedUserPersonType NA
managerAssignmentNumber Manager Assignment Number workRelationships~assignments~managers~ManagerAssignmentNumber workRelationships~assignments~managers~ManagerAssignmentNumber NA
futureStartDate Future Start Date future~workRelationships~StartDate future~workRelationships~StartDate NA
futureEffectiveStartDate Future Effective Start Date future~workRelationships~assignments~EffectiveStartDate future~workRelationships~assignments~EffectiveStartDate NA
futureEffectiveEndDate Future Effective End Date future~workRelationships~assignments~EffectiveEndDate future~workRelationships~assignments~EffectiveEndDate NA
futureActionCode Future Action Code future~workRelationships~assignments~ActionCode future~workRelationships~assignments~ActionCode NA
futureActionTypeCode Future Action Type Code future~workRelationships~assignments~ActionTypeCode future~workRelationships~assignments~ActionTypeCode NA
country Location workRelationships~LegislationCode workRelationships~LegislationCode NA
addressType Address Type addresses~AddressType addresses~AddressType NA
postalCode Location postal code addresses~PostalCode addresses~PostalCode NA
townOrCity Town or city addresses~TownOrCity addresses~TownOrCity NA
region1 Region1 addresses~Region1 addresses~Region1 NA
region2 Region2 addresses~Region2 addresses~Region2 NA
floorNumber Floor number addresses~FloorNumber addresses~FloorNumber NA
building Building addresses~Building addresses~Building NA
addressLine1 AddressLine1 addresses~AddressLine1 addresses~AddressLine1 NA
phoneNumber Phone Number phones~PhoneNumber phones~PhoneNumber NA
extension Phone Extension phones~Extension phones~Extension NA
phoneType Phone Type phones~PhoneType phones~PhoneType NA
lastWorkingDate Last Working Date workRelationships~LastWorkingDate workRelationships~LastWorkingDate NA

Default Attributes - Managed System
Oracle Fusion Cloud Applications User Entity Oracle Fusion Cloud Applications Attribute Name Display Name on Oracle Access Governance Oracle Access Governance Attribute Display Name Applicable to HCM/ ERP/ BOTH
FA User id (SCIM) uid Unique Id Both
userName name Name Both
password password Password Non-Reconcilable
externalId externalID External ID Both
displayName displayName Display Name Both
name.familyName familyName Family Name Both
name.givenName givenName Given Name Both
emails.value email Email Both
emails.type emailType Email Type Both
active status Status Both
workerInformation.personNumber personNumber Person Number Both
workerInformation.manager managerUid Manager Uid Both
workerInformation.job jobCode Job Code Both
Roles securityContextsWithValues Roles Roles

Both

ERP
Area of Responsibility (AoR) ResponsibilityId UID UID

Both

HCM
ResponsibilityName responsibilityName responsibilityName

Both

HCM
ResponsibilityType responsibilityType responsibilityType

Both

HCM
AssignmentNumber assignmentNumber assignmentNumber

Both

HCM
AssignmentName assignmentName assignmentName

Both

HCM
ActiveStatus activeStatus activeStatus

Both

HCM
StartDate startDate startDate

Both

HCM
templateCode TemplateCode TemplateCode

Both

HCM
Procurement Agents procurementBusinessUnits Procurement business units

Both

ERP
AssignmentId assignmentId Assignment Id
StatusCode statusCode Status code
ManageRequisitionsAllowedFlag manageRequisitionsAllowed Manage requisitions allowed
AccessLevelToOtherAgentsRequisitions accessLevelToOtherAgentsRequisitions Access level to other agents requisitions
ManageOrdersAllowedFlag manageOrdersAllowed Manage orders allowed
AccessLevelToOtherAgentsOrders accessLevelToOtherAgentsOrders Access level to other agents orders
ManageAgreementsAllowedFlag manageAgreementsAllowed Manage agreements allowed
AccessLevelToOtherAgentsAgreements accessLevelToOtherAgentsAgreements Access level to other agents agreements
ManageNegotiationsAllowedFlag manageNegotiationsAllowed Manage negotiations allowed
AccessLevelToOtherAgentsNegotiations accessLevelToOtherAgentsNegotiations Access level to other agents
ManageSourcingProgramsAllowedFlag manageSourcingProgramsAllowed Manage sourcing programs allowed
AccessLevelToOtherAgentsSourcingPrograms accessLevelToOtherAgentsSourcingPrograms Access level to other agents sourcing programs
ManageCatalogContentAllowedFlag manageCatalogContentAllowed Manage catalog content allowed
ManageSuppliersAllowedFlag manageSuppliersAllowed Manage suppliers allowed
ManageQualificationsAllowedFlag manageQualificationsAllowed Manage qualifications allowed
AccessLevelToOtherAgentsQualifications accessLevelToOtherAgentsQualifications Access level to other agents qualifications
ManageChecklistsAllowedFlag manageChecklistsAllowed Manage checklists allowed
AccessLevelToOtherAgentsChecklists accessLevelToOtherAgentsChecklists Access level to other agents checklists
ManageAslAllowedFlag manageAslAllowed Manage Approved Supplier List Entries Allowed
AnalyzeSpendAllowedFlag analyzeSpendAllowed Analyze Spend Allowed

## Support for Custom Fields in HCM/Both Mode

Create system attribute to support Assignment DFF from Oracle Fusion Applications for Oracle HCM or Both , integrated as an Authoritative Source.

- Create a system attribute from the Manage Integrations page. For more details, see[Create System Attribute](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#system-attribute).
- In the Value source step, select Included in inbound data from the system .
- In the What is the system attribute name? field, enter exact nomenclature. See[System Attribute Name in the Supported Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-supportassignmentdff__supported-custom-table)table.

You can see the custom attributes in the Identity Attributes page, listed as Custom attribute.
- From the Identity Attributes page, update the identity flag for the identity attribute. See[Modify Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#customattributes-settings).
- Perform data load for the orchestrated system. To load data, see[Initiate Data Load](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#initiate-data-load).
- After successful data load, you can view the value in the Enterprise-Wide Browser and the identity attributes page.

### Supported Custom Attributes

Here's a list of custom attributes supported for Oracle Fusion Applications integrated as an Authoritative Source with Oracle HCM or Both mode.

Supported Custom Attributes
AG Name System Attribute Name Multivalued Data Type
Preferred Name names~KnownAs FALSE String
Middle Name names~MiddleNames FALSE String
Assignment Status Type workRelationships~assignments~AssignmentStatusType FALSE String
Legal Employer Name workRelationships~LegalEmployerName FALSE String
Business Unit Name workRelationships~assignments~BusinessUnitName FALSE String
Title workRelationships~assignments~AssignmentName FALSE String
Department workRelationships~assignments~DepartmentId FALSE String
Rehire workRelationships~RecommendedForRehire FALSE String
Citizenship citizenships~Citizenship FALSE String
Home Email emails~EmailAddress[emails~EmailType='H1'] FALSE String

Descriptive Flex Fields
AG Name System Attribute Name Example
Assignment DFF workRelationships~assignments~assignmentsDFF~&lt;DFFName`workRelationships~assignments~assignmentsDFF~joblocation`
Worker DFF workersDFF~&lt;DFFName&gt;`workersDFF~bloodGroup`

## Support for Additional Attributes for Lookup Objects

You can now load and use additional attributes for Oracle Fusion Cloud Applications lookup objects, such as Job , Position , and Location to support attribute-based access management operations in Oracle Access Governance.

### Inbound Transformation Script

Currently,`job`,`position`, and`location`objects are supported.
Use inbound transformation script to access lookup object attribute values
```

```

- location is the name of lookup object
- M3- Dallas is one sample value of location which will be from attribute LocationCode
- city is an attribute referred from lookup object
Sample script to extract job
```

```

Sample script to extract position
```

```

### Location Attributes Supported by Oracle Access Governance

```

```

### Job Attributes Supported by Oracle Access Governance

```

```

### Position Attributes Supported by Oracle Access Governance

```

```
