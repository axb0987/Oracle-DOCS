# Integrate with Fusion Cloud Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Fusion Cloud Applications

## Overview: Integrate Oracle Access Governance with Oracle Fusion Cloud Applications

Oracle Access Governance can be integrated with Oracle Fusion Cloud Applications enabling identity orchestration, including on-boarding of identity (user) data, worker information, and provisioning of Oracle Human Capital (HCM) and Oracle Enterprise Resource Planning (ERP) accounts.
Oracle Fusion Cloud Applications provides enterprise Human Capital Management (HCM) and Enterprise Resource Planning (ERP) functionality. Oracle Access Governance supports the following elements within Oracle Fusion Cloud Applications:
- Oracle Fusion Cloud Applications HCM and Oracle Fusion Cloud Applications ERP as an authoritative (trusted) source of identity information allowing for reconciliation of employees created or modified in Oracle Fusion Cloud Applications.
- Oracle Fusion Cloud Applications as a Managed System enabling provisioning of HCM and ERP application accounts.

## Oracle Fusion Cloud Applications Integration Architecture Overview

The integration of Oracle Fusion Cloud Applications allows for retrieving identity data and transferring the data to Oracle Access Governance. Once a connection is established, you can perform provisioning and remediation tasks which are visible in the Managed System.

Oracle Fusion Cloud Applications works with the Fusion Apps API to gain access to Oracle Fusion Cloud Applications through the REST API endpoints. This allows Oracle Fusion Cloud Applications to perform create, read, update, and delete operations on Oracle Access Governance.
- If you select the[Authoritative Source](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)mode, you can set up a Oracle Fusion Cloud Applications Orchestrated System, which then allows Oracle Access Governance to retrieve identity data from Oracle Fusion Cloud Applications as an authoritative (trusted) source of identity information.
- If you select the[Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)configuration mode, then Oracle Access Governance will allow you to manage HCM and ERP user profile records in Oracle Fusion Cloud Applications. This enables the provisioning of new accounts in Oracle Fusion Cloud Applications from Oracle Access Governance.

## Oracle Fusion Cloud Applications Integration Functional Overview

Oracle Fusion Cloud Applications integration supports both Oracle Human Capital (HCM) and Oracle Enterprise Resource Planning (ERP) modules including configuration of the Orchestrated System, user account creation, revocation, change password, and assigning and removal of roles.

- Configure Oracle Fusion Cloud Applications Orchestrated System

See[Configure Integration Between Oracle Access Governance and Oracle Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm)
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-default-supported-attributes-1).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance. You can also configure partial data loads for Oracle Fusion Cloud Applications. For more information, see[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system, depending on the configuration mode you have selected, Authoritative Source or Managed System or request an access for an identity. Ingestion of user records as data from Oracle Fusion Cloud Applications.

Oracle Access Governance supports ingestion from Person /Worker record or User Account . Person represents core HCM entity containing employment details, such as employee number, work relationships, job code, person record. User Account represents security identity that grants system access to Oracle Fusion Cloud Applications. Person is linked to a User Account.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. This allows you to update predefined roles, Oracle Fusion Cloud Applications application roles, OCI Groups and Oracle Fusion Cloud Applications groups.
- 

[Revoke Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-revoke-account)

Disable an account (Users) associated with an identity. This will remove accesses for the Oracle Fusion Cloud Applications user account.

### Assign Permissions using Security Context

Oracle Access Governance users can request access to resources and roles provided in[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). You can assign permissions to a Oracle Fusion Cloud Applications account using the Request a new access functionality of Oracle Access Governance. This allows you to request an access bundle containing permissions with security details to roles on the Oracle Fusion Cloud Applications system. For details on managing role and policies, see[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm)and[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).
Oracle Access Governance supports the following Security Contexts when integrated with Oracle Fusion Cloud Applications ERP:
- Business Units
- Asset Book Value
- Ledgers or Ledger Sets
- Reference Data Sets
- Data Access Sets
- Inventory Organization
- Intercompany Organization
- Cost Organization
- Manufacturing Plant

When you request an access bundle in Oracle Access Governance for a role, a provisioning operation begins which updates the roles in the Oracle Fusion Cloud Applications for the following types of scenarios:

### Creating Permission using Security Context during Policy Creation
While creating a policy with Oracle Access Governance for the following use cases:
- Create a new access bundle that has permission with security context and which is already associated with identity collection for the policy.
- Create a new access bundle that has permission with security context and which is already associated with identity collection for the policy. This is applicable in situations when the user already has the access bundle assigned with same permission, but with a different security context.

### Editing Permission for Removal of Security Context
You can edit the permissions entitlement using Oracle Access Governance for the following cases:
- Edit the access bundle that have permission with security context to change the security context from permission entitlement which is already associated with an identity collection for the associated policy.
- Edit the access bundle that have permission with security context to remove security context from permission entitlement which is already associated with identity collection through policy.

### Area of Responsibility (AOR)

Oracle Access Governance supports Area of Responsibility (AOR) in Fusion HCM. With AOR, organizations can assign responsibility-based access based on user's role and scope, such as Legal Employer or Business Unit. Oracle Fusion Cloud Applications assigns responsibilities to identities which control the visibility in the Work Contacts.

Oracle Access Governance ingests AOR as an account attribute when a user account is linked to a person. AOR assignments are managed using AOR templates. These templates are predefined in Oracle Fusion Cloud Applications and can be selected as permissions in an[Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-create-access-bundle).

You can assign Area of Responsibility (AOR) in Oracle Access Governance using an AOR Template with Granted permission type as Responsibility template . AOR assignments can be provisioned through policies or self-service requests. When granted, an AOR is created based on template attributes. See[AOR Template-Based Provisioning](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#create-aor-template)and[AOR Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm#oracle-fusion-integrationsettings__aor-integration).

### Procurement Agent (PO)

Oracle Access Governance supports provisioning Procurement Agents (PO Agents) for Oracle Cloud ERP, when the target user account is linked to associated worker/person information. You can include Procurement Agent access in an[Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-create-access-bundle)and provision it by granting the appropriate Procurement business unit permission to the user. During access bundle creation, select the permission with Granted permission type = Procurement business unit (not Role) to ensure Oracle Access Governance provisions the intended Procurement Agent entitlement.

Access Bundle displays all available business units. However, you must select a business unit that's configured as a Procurement Business Unit (that is Procurement is enabled for that business unit) to create or manage Procurement Agent (PO Agent). See[Configure Business Unit for Procurement Agent (PO Agent) in Oracle Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#po-agent).

When you update a user account or its attributes directly in Oracle Access Governance, the incremental data load captures the associated Procurement Agents and shows those changes in Oracle Access Governance, however, direct updates to Procurement Agents in Oracle Fusion Cloud Applications aren’t picked up by Oracle Access Governance.

## Preventive Segregation of Duties (SOD) Analysis

Oracle Access Governance allows you to perform preventive segregation of duties (SOD) analysis for Oracle Fusion Cloud Applications orchestrated systems during the provisioning process through integration with Oracle Fusion Cloud Risk Management and Compliance (RMC). Segregation of duties (SOD) separates activities such as approving, recording, and processing tasks so an enterprise can more easily prevent or detect unintentional errors and willful fraud. SOD constrains duties across roles so that unethical, illegal, or damaging activities are less likely.

### Segregation of Duties Analysis and Provisioning in Oracle Access Governance

When you configure an Oracle Fusion Cloud Applications orchestrated system you can enable Oracle Fusion Cloud Risk Management and Compliance (RMC) integration. Oracle Fusion Cloud Risk Management and Compliance (RMC) is a security and audit solution that controls user access to your Oracle Cloud ERP financial data, monitors user activity, and makes it easier to meet compliance regulations through automation. One of the features of RCMS is the use of controls to analyze SOD analysis within the Oracle Fusion Cloud Applications orchestrated system.
To enable Oracle Fusion Cloud Risk Management and Compliance (RMC) within Oracle Access Governance you should meet the following requirements:
- Configure an Oracle Fusion Cloud Applications orchestrated system to manage permissions. See[Integrate with Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm)and[Integrate with Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm).
- The Oracle Fusion Cloud Applications instance you are integrating with should have controls configured that define your SOD policies. Oracle Fusion Cloud Risk Management and Compliance (RMC) provides a library of ready-to-use controls for high-risk business processes, such as, AP, AR, GL, Payroll, and Compensation. These controls can be updated to reflect your enterprise using the graphical workbench provided with RMC. For further information, refer to the Oracle Fusion Cloud Risk Management and Compliance (RMC)[documentation](https://docs.oracle.com/en/cloud/saas/risk-management-and-compliance/index.html).

Once configured, Oracle Access Governance uses Oracle Fusion Cloud Risk Management and Compliance (RMC) to check for SOD violations when a user makes an access request for an access bundle. When you make the request, a Preventive SOD Analysis activity is started, which can be monitored in the[Activity Log](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#view-activity-log). This activity will make a check against Oracle Fusion Cloud Risk Management and Compliance (RMC) for any controls indicating that an SOD violation has taken place for the user and access requested. The Preventive SOD Analysis process runs asynchronously and returns results to the access request. If approved with violations, Oracle Access Governance handles the provisioning of SoD-flagged violations by passing approval decisions—including justifications and conditional acknowledgments—directly to Risk Management Cloud (RMC).
The following rules apply to this process:
- Preventive SOD Analysis can only run against a user that has already been created in Oracle Fusion Cloud Applications and is available to the Oracle Fusion Cloud Risk Management and Compliance (RMC) engine. Once this user is provisioned, any access requests made by the user will be analyzed by RMC if this option is enabled. See[Prequisites for Segregation of Duties (SoD) Check](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-rmc-segregation-of-duties.htm).
- Only one Preventive SOD Analysis task can run for a particular user at any one time. If your user creates a second access request while the Preventive SOD Analysis task from a previous access request is still running, then the second RMC request will fail. Other reasons why Preventive SOD Analysis task might fail include RMC unavailable, and no user account in Oracle Fusion Cloud Applications.
- Preventive SOD analysis is supported for requests for access bundles. Access requests for Oracle Access Governance roles are not supported for SOD analysis.

### Example: Preventive Segregation of Duties in Oracle Access Governance

Let's look at an example of preventive segregation of duties in Oracle Access Governance in action. Consider the example where a user in your organization is promoted from AR Analyst to AR Manager. To carry out their new duties, the user requests access to the AR Manager access bundle in Oracle Access Governance.
When the access request is made, a Preventive SOD Analysis task is run for that user and RMC identifies some SOD violations which are flagged in the access request. An example of such a violation might be:
- The user's current permissions allow them Create User on Oracle Fusion Cloud Applications ERP, while the access bundle requested includes Manage Compensation .

This combination of permissions has a potential for payroll fraud by creating ghost employees and setting compensation. This conflict is flagged in the access request, so that the approver can review the information in the request, and log into RMC for further information if required. On this basis the approver can make an informed decision on whether to approve or reject the request, or to request further information from the person requesting the access.

## Bithright Access and Early Termination for HCM Users

Oracle Access Governance grants birthright access to pre-hires and hires automatically, based on the start date or the joining date.

To configure birthright access in Oracle Access Governance, see[Granting Birthright Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm).

To configure early termination, see[Revoke Access for an Early Termination](https://docs.oracle.com/en-us/iaas/Content/access-governance/revoke-access-early-termination.htm).
- Oracle Access Governance sets system identity attribute`startDate`based on the HCM attributes that indicate the first day of employment.
- If an employee details are ingested in Oracle Access Governance with a`startDate`in future, Oracle Access Governance sets the status of the employee as Disabled .
- When an employee's`startDate`matches the current date, then Oracle Access Governance sets the status of the employee as Active .
- When an employee's`terminationDate`matches the current date, the status of the employee is set as Disabled .

For validation, see[Validate Configuration](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm#validate-configuration)
