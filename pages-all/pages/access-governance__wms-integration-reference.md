# Oracle Warehouse Management Cloud (WMS) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/wms-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Oracle Warehouse Management Cloud (WMS) Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration with Oracle Access Governance.

## Oracle Warehouse Management Cloud (WMS) Components Certified for Integration with Oracle Access Governance

Component Type Component
System Oracle Warehouse Management Cloud (WMS)

## Supported Configuration Modes for Oracle Warehouse Management Cloud (WMS) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Oracle Warehouse Management Cloud (WMS) Orchestrated System supports the following mode:
- Managed System

You can manage Oracle Warehouse Management Cloud (WMS) accounts, groups and companies, and facilities.

## Supported Operations when Provisioning to Oracle Warehouse Management Cloud (WMS)

When you provision an account from Oracle Access Governance to Oracle Warehouse Management Cloud (WMS) certain operations are supported.

The Oracle Warehouse Management Cloud (WMS) Orchestrated System supports the following account operations when provisioning a user:
- Create Account
- Update Account
- Enable Account
- Disable Account
- Delete Account
- Reset Password
- Assign Groups
Note  
  
You can't assign legacy groups using the Oracle Warehouse Management Cloud (WMS) orchestrated systems.
- Remove Groups
- Assign Facilities
- Remove Facilities
- Assign Companies
- Remove Companies

For more details see Oracle Access Governance Integration Functional Overview and Integrate with Oracle Warehouse Management Cloud (WMS).

## Default Supported Attributes

Entity WMS Attribute Name Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Data Type
User __UID__(id) uid Unique Id uid
__NAME__(username) name User login string
univ_id_1 uniqueName Unique name string
__ENABLE__(is_active) status Status boolean
auth_user_id.first_name firstName First name string
auth_user_id.last_name lastName Last name string
auth_user_id.email email Email string
__PASSWORD__(password) password Password string
password_life_in_days passwordLifeInDays Password expiry number
hire_type_id.key hireType Hire type lookup
auth_user_id.date_joined startDate Start date date
facility_id.key defaultFacility Default facility lookup
company_id.key defaultCompany Default company lookup
role_id.key role Role lookup
lang_code_id.key language Language lookup
default_group_id.id defaultGroup Default group lookup
__COMPANY__ companies Companies
__FACILITY__ facilities Facilities
__GROUP__ groups Groups
Groups(Entitlement) groups Groups
__UID__(id) uid Unique Id
__NAME__(name) name Name
Company Name: $(company_id.key)$ (custom description) description Description
Facilities(MVA) facilities Facilities
__UID__(code) uid Unique Id
__NAME__(name) name Name
Companies(MVA) companies Companies
__UID__(code) uid Unique Id
__NAME__(name) name Name

## Default Matching Rules

To map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

Mode Default Matching Rule

Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

Attribute name :

`Account.name = Identity.userName`
