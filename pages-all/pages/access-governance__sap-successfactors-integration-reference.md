# SAP SuccessFactors Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-successfactors-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# SAP SuccessFactors Integration Reference

## SAP SuccessFactors Components Certified for Integration with Oracle Access Governance

The SAP SuccessFactors components that you can integrate with are listed below.

Certified Components
Component Type Component
System SAP SuccessFactors

## Supported Configuration Modes for SAP SuccessFactors Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

SAP SuccessFactors Orchestrated System supports the following modes:
- Authoritative Source

You can use SAP SuccessFactors as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System

You can manage SAP SuccessFactors accounts, and groups.

## Supported Operations When Provisioning To SAP SuccessFactors

When you provision an account from Oracle Access Governance to SAP SuccessFactors certain operations are supported.

The SAP SuccessFactors Orchestrated System supports the following account operations when provisioning a user:
- Create User

Only an Employee with an Employee ID is supported.
- Update User
- Enable User

Employee cannot be enabled. The underlying User associated with the Employee will be enabled.
- Disable User

Employee cannot be disabled. The underlying User associated with the Employee will be disabled.
- Add Group
Note  
  
Currently only static groups are supported. Dynamic groups are not supported.
- Remove Group
Note  
  
Currently only static groups are supported. Dynamic groups are not supported.

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with SAP SuccessFactors](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-successfactors.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default SAP SuccessFactors attributes.

Default Attributes for SAP SuccessFactors - Authoritative Source
Entity SAP SuccessFactors Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Supported Module User/Employee
User UserEntity.userId uid Unique Id User &amp; Employee
UserEntity.username name Employee user name User &amp; Employee
UserEntity.email email Email User &amp; Employee
UserEntity.country country Country User &amp; Employee
UserEntity.state state State User &amp; Employee
UserEntity.city city City User &amp; Employee
UserEntity.citizenship citizenship Citizenship User &amp; Employee
UserEntity.empId employeeNumber Employee number User &amp; Employee
UserEntity.jobLevel jobLevel Job level User &amp; Employee
UserEntity.married married married User &amp; Employee
UserEntity.status status Status User &amp; Employee
UserEntity.businessPhone phone Phone User &amp; Employee
UserEntity.cellPhone mobile Mobile User &amp; Employee
UserEntity.firstName firstName First name User &amp; Employee
UserEntity.lastName lastName Last name User &amp; Employee
UserEntity.gender gender Gender User &amp; Employee
UserEntity.salutation salutation Salutation User &amp; Employee
UserEntity.middleName middleName Middle name User &amp; Employee
PerPersonal.personIdExternal externalPersonId External person id User &amp; Employee

Employee EmpJob.managerId managerUid Manager Employee
EmpJob.company company Company Employee
EmpJob.department department Department Employee
EmpJob.jobCode jobCode Job Code Employee
EmpJob.division division Division Employee
EmpJob.location location Location Employee
EmpJob.businessUnit businessUnit Business unit Employee
EmpJob.payScaleArea payScaleArea Payscale area Employee
EmpJob.employmentType employmentType Employment type Employee
EmpJob.isFulltimeEmployee isFulltimeEmployee Full-time employee Employee
EmpEmployment.startDate startDate Start date Employee
EmpEmployment.endDate endDate End date Employee
EmpEmployment.isContingentWorker isContingentWorker Contingent worker Employee

Default Attributes for SAP SuccessFactors - Managed System
Entity SAP SuccessFactors Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Transformation Updateable Field
User UserEntity.userId uid Unique Id No No
UserEntity.username name User login Yes No
UserEntity.password password Password No Yes
UserEntity.email email Email Yes Yes
UserEntity.country country Country No Yes
UserEntity.state state State No Yes
UserEntity.city city City No Yes
UserEntity.citizenship citizenship Citizenship No Yes
UserEntity.empId employeeNumber Employee number No No
UserEntity.jobLevel jobLevel Job level No Yes
UserEntity.married married Marital status No Yes
UserEntity.status status Status Yes Yes
UserEntity.firstName firstName First name Yes Yes
UserEntity.lastName lastName Last name Yes Yes
UserEntity.gender gender Gender No Yes
UserEntity.salutation salutation Salutation No Yes
UserEntity.middleName middleName Middle name No No
UserEntity.businessPhone phone Phone No Yes
UserEntity.cellPhone mobile Mobile No Yes
UserEntity.fax fax Fax No Yes
PerPersonal.personIdExternal externalPersonId External person id No No

Group groupId_staticGroup groups Groups No No
Dynamic Group groupId_dynamicGroup dynamicGroups Dynamic Groups No No
Note  
  
For Managed System mode, only User related attributes are supported. Employee provisioning is not supported.

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the SAP SuccessFactors orchestrated system is:

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
