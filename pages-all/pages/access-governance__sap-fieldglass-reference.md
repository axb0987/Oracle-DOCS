# SAP Fieldglass Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-fieldglass-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# SAP Fieldglass Reference

## SAP Fieldglass Components Certified for Integration with Oracle Access Governance

The SAP Fieldglass components that you can integrate with are listed below.

Certified Components
Component Type Component
System SAP Fieldglass

## Supported Configuration Modes for SAP Fieldglass Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

SAP Fieldglass Orchestrated System supports the following mode:
- Managed System

You can manage SAP Fieldglass users and groups.

## Supported Operations When Provisioning To SAP Fieldglass

When you provision an account from Oracle Access Governance to SAP Fieldglass certain operations are supported.

The SAP Fieldglass Orchestrated System supports the following account operations when provisioning a user:

- Create Account
- Update Account
- Revoke Account
- Assign Group
- Remove Group

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with SAP Fieldglass](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-fieldglass.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default SAP Fieldglass attributes.

Account Attribute Mapping
Entity SAP Fieldglass Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User id uid Unique Id
name name User login
name.givenName firstName First name
name.familyName lastName Last name
name.formatted formattedName Display name
name.honorificPrefix prefix Prefix

__ACCOUNT__.emails.value,type:Work email Email
title title Title
locale locale Locale
timezone timeZone Time zone
active status Status
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User;manager.value managerUid Manager
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User;employeeNumber employeeNumber Employee number
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User;division businessUnit Business unit
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User;costCenter costCenter Cost center
urn:ietf:params:scim:schemas:extension:Fieldglass:2.0:User;loginAuthType loginAuthType Login auth type
Group __ACCOUNT__.groups groups Groups

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the SAP Fieldglass orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`Login = Employee user name`

## Known Issues

The following known issues exist with the SAP Fieldglass orchestrated system.
- Worker is a restricted group in SAP Fieldglass which restricts the ability to to assign this group to the User. If you try to assign the Worker group you will see the error message:

Failed to perform provisioning operation on target.

Failed to update account :: HTTP 400 Error : Not able to parse input, or input does not match required entities or validation failures. {"schemas":["urn:ietf:params:scim:api:messages:2.0:Error"],"detail":"Error with operation 1:[Error adding user z250623070211608633112c6: Additional Roles : INVALID-VALUE]","status":"400"}
- It is not possible to assign or revoke the default SAP Fieldglass group to a User,

If you do not assign a group to a user then SAP Fieldglass will by default assign the default group, D027_DEFAULT to your user, and you will see the error message:

Failed to perform provisioning operation on target.

Failed to update account :: HTTP 400 Error : Not able to parse input, or input does not match required entities or validation failures. {"schemas":["urn:ietf:params:scim:api:messages:2.0:Error"],"detail":"Unsupported for default group","status":"400"}
-
