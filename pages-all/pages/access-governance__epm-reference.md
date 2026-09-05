# Oracle Cloud Performance Management Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/epm-reference.htm
- Fetched: 2026-09-05 03:14 CDT

# Oracle Cloud Performance Management Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Cloud Enterprise Performance Management and Oracle Access Governance.

## Supported Configuration Modes for Oracle Cloud Enterprise Performance Management

You can use Oracle Access Governance integrations to set up different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

The Oracle Cloud Enterprise Performance Management Orchestrated System supports the following modes:
- Managed System

You can manage Oracle Cloud Enterprise Performance Management user accounts and groups from Oracle Access Governance.

## Supported Operations when Provisioning to Oracle Cloud Enterprise Performance Management

Oracle Cloud Enterprise Performance Management Orchestrated System supports the user management, role management, and group management operations.

An Oracle Cloud Enterprise Performance Management account is a essentially an OCI User containing any OCI predefined roles for EPM or OCI Groups containing any OCI predefined roles for Oracle EPM. The Oracle Cloud Enterprise Performance Management Orchestrated System supports the following account operations when provisioning a user:
- Create Account
- Update Account
- Predefined Roles ( OCI predefined roles for EPM )
- Application Roles ( EPM Application Roles )
- Assign Groups ( EPM Groups or OCI Groups containing any OCI predefined roles for EPM )
- Revoke Groups ( EPM Groups or OCI Groups containing any OCI predefined roles for EPM )

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate with Oracle Enterprise Performance Management (EPM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-enterprise-performance-management-epm.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Cloud Enterprise Performance Management attributes.

These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from Oracle Cloud Enterprise Performance Management:

  
`OCI ID`will map to`Unique ID`  

Default Attributes for Oracle Cloud Enterprise Performance Management
Entity Oracle Cloud Enterprise Performance Management Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Identity attribute display name Transformation Supported?
User OCI ID uid Unique Id No
userlogin name User login Yes
firstname firstName First name Yes
lastname lastName Last name Yes
email email Email Yes
password password Password No
resetpassword resetPassword Reset password No
Predefined Roles predefinedRoles Predefined roles No No
Application Roles epmApplicationRoles applicationRoles Application roles No
Groups epmGroups groups Groups No
