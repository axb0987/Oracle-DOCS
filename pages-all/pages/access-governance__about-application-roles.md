# Application Roles
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm
- Fetched: 2026-09-05 03:12 CDT

# Application Roles

Oracle Access Governance offers several predefined application roles with different capabilities levels to perform the access management and governance operations. You can assign one or more application roles to users from your Oracle Access Governance cloud service instance. You can’t modify predefined application roles or modify permissions assigned within these roles.

## Administrator (`AG_Administrator`)

Oracle Access Governance Administrator has the highest level of access within Oracle Access Governance. Users with the Administrator role are responsible for managing all Oracle Access Governance operations, including managing Orchestrated systems, access controls, service administrative operations, and so on.
The prime responsibility of an Administrator is to
- Define foundational tasks available as part of the Service Administration module in Oracle Access Governance, such as setting up Orchestrated systems, managing identities, configuring core and custom identity attributes, configuring notifications, verifying data load operations in Oracle Access Governance.
- Configure Event-based Access Reviews to perform micro-certifications and manage unmatched accounts. For example, you can assign`AG_Administrator`to Security Administrators or Identity and Access Management Specialist to manage your Oracle Access Governance cloud service instance.

Typically,`AG_Administrator`would establish the first integration with the Authoritative source by creating an Orchestrated System, executing the full data load, setting rules to define Workforce and Consumer users.`AG_Administrator`can then assign owners to manage the Orchestrated system to any Oracle Access Governance active user.
An`AG_Administrator`has the full access to all features and functionalists within the service instance. They have the all the permissions to create, view, update, and delete the Oracle Access Governance resources:
- Orchestrated System
- Identity Collections
- Access Bundles
- Roles
- Policies
- Approval Workflows
- Access Guardrails
- Auto-generated Access Bundles
- Account Profiles

## Service Desk Administrator (`AG_ServiceDesk_Admin`)

Oracle Access Governance Service Desk Administrator is responsible for performing advanced account administrative functions directly within Oracle Access Governance. The prime responsibility of a Service Desk Administrator is to perform highly critical and urgent operations without the need of any approvals, especially related to Account Lifecycle Management operations.
Users with the Service Desk Administrator role can perform the account administrative functions from the Service Administration &gt; Manage Identities &gt; Identities page:
- View identity details for all the identities.
- View account details for permissions.
- Terminate all the accounts and accesses for an identity at once without any approvals. Once terminated, you can re-provision or activate the accounts and accesses, with Grant Type Policy .
- Enable, Disable or Delete, or Modify one or multiple accounts and attributes for an identity.
- Revoke one or more permissions assigned directly from the Managed System or provisioned through request.
- Retry provisioning for failed or pending status.
- Change Password for an account managed by Oracle Access Governance.
- Manage Delegations for approvals or access reviews. For example, you can assign`AG_ServiceDesk_Admin`to an IT Specialist to immediately terminate all accounts and accesses based on an incident response triggered by repeated failed login attempts to prevent potential unauthorized activity.
Additionally,`AG_ServiceDesk_Admin`can perform the following operations as part of Oracle Access Governance user:
- View orchestrated systems details along with activity logs.
- As a resource owner, view, update, or delete Oracle Access Governance resources that they own.
- As a reviewer associated with Approval workflows, approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.
- As an access reviewer, can review and certify the access review tasks if associated with a specific approval workflow.
- Manage Delegations

## Campaign Administrator (`AG_CampaignAdmin`)

Oracle Access Governance Campaign Administrators can initiate an access review process by creating Campaigns. They can modify, delete, and monitor self-created access review campaigns. They can view campaign report and download CSV data for offiline purposes.

Their prime responsibility is to schedule ad-hoc or periodic campaigns for Identity Access Reviews, Policy Reviews, Identity Collection Reviews, or Resource Ownership review across all systems.
Additionally, the Campaign Administrators:
- Can create approval workflows
- Can create identity collections
- As a resource owner modify, delete, and view resources that they own
- As a reviewer associated with Approval workflows, approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.

## Enterprise-wide Browser Access Administrator (`AG_Enterprise_Wide_Access_Admin`)

Oracle Access Governance Enterprise-wide Access Administrator get the comprehensive visibility on all the components, access information, and resources within an enterprise framework from the Who Has Access to What → Enterprise-wide Browser page.
Primarily, Enterprise-wide Access Administrators can:
- Browse access information using various perspectives, such as Identities, Identity Collections, Roles, Permissions, Policies, Resources, and Organizations.
- Run User-created reviews for identities, identity collections, policies from the Enterprise-wide Browser dashboard.
- Generate a monthly report on access reviews created from Enterprise-wide Browser.
- Download CSV and PDF screenshot.
Additionally, can:
- Can create Identity Collections
- As a resource owner, view, update, or delete Oracle Access Governance resources that they own.
- As a reviewer associated with Approval workflows, approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.

## Application Owner Administrator (`AG_AppOwner_Admin`)

Oracle Access Governance Application Owner Administrator is responsible for performing integrations with other systems by adding an Orchestrated system, modifying the connection settings, validating and loading the data in Oracle Access Governance. They can also configure an orchestrated system by editing the integration settings, configuring notification settings, configuring recommended access bundle, viewing data browser for accounts and permissions, defining transformation rules for inbound and outbound data for identity and account attributes, and defining correlation rules for matching identities and identity accounts.

Application Owner Administrator is primarily responsible to:
- Set up integrations with an application as an Authoritative Source or a Managed System by creating an orchestrated system
- Manage and configure the integrated systems
Note  
  
`AG_AppOwner_Admin`cannot activate identities or configure identity attributes for an orchestrated system. To do so, you need the`AG_Administrator`role.
- View accounts and granted permissions details from Data Browser details and perform account lifecycle operations from the Data Browser dashboard.
Additionally, Application Owner Administrator:
- Can create approval workflows
- Can create access guardrails
- Can create identity collections
- Can create access bundles
- Can manage auto-generated access bundles
- As a resource owner, can modify, delete, and view resources that they own. Resources can be any Oracle Access Governance entity (Access Bundles, Organizations, Identity Collections, Policies, Approval workflows, Orchestrated Systems, Access Guardrails, Auto-generated Access Bundles, or Roles).
- As a reviewer associated with Approval Workflows, can approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.
- As a user, can use the self-service module to request new access, track requests, assign preferences, and so on.

## Application Owner Restricted Administrator (`AG_AppOwner_Admin_Restricted`)

Oracle Access Governance Application Owner Restricted Administrator is responsible for creating a new integration with other systems by adding an orchestrated system as a Managed System. However, they can manage integrations and configure settings only for systems that they own as a resource owner.

Role Can Create Orchestrated System Can Manage Orchestrated System
Application Owner Administrator YES (Authoritative Source and Managed System) YES
Application Owner Restricted Administrator YES (Only Managed System) Limited to resources they own

Application Owner Restricted Administrator is primarily responsible to:
- Set up integrations with an application as a Managed System by creating an orchestrated system.
- Manage and configure the orchestrated system for which it is the resource owner.
Note  
  
`AG_AppOwner_Admin_Restricted`cannot activate identities or configure identity attributes for an orchestrated system. To do so, you need the`AG_Administrator`role.
Additionally, Application Owner Restricted Administrator:
- Can create approval workflows
- Can create identity collections
- Can create access bundles and auto-generated access bundles
- As a resource owner, can modify, delete, and view resources that they own. Resources can be any Oracle Access Governance entity (Access Bundles, Organizations, Identity Collections, Policies, Approval workflows, Orchestrated Systems, Access Guardrails, Auto-generated Access Bundles, or Roles).
- As a reviewer associated with approval workflows, approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.
- As a user, can use the self-service module to request new access, track requests, assign preferences, and so on.

Scenario : If Betty is assigned the`AG_AppOwner_Admin_Restricted`role, Betty can establish new integrations as a Managed System by creating a new orchestrated system from the Service Administration → Orchestrated Systems page. However, Betty cannot create Authoritative Source. Additionally, Betty can configure settings for the orchestrated systems only if Betty is assigned as the resource owner (primary owner or one of the additional owners) for the orchestrated system resource.

## Access Control Administrator (`AG_AccessControl_Admin`)

Oracle Access Governance Access Control Administrator is responsible for managing Access Control Administration in Oracle Access Governance.

Role Can Create Access Control Resources Can Manage Access Control Resources
Access Control Administrator YES YES
Access Control Restricted Administrator YES Limited to resources they own

Access Control Administrator is primarily responsible to:
- Create and Manage Identity Collections
- Create and Manage Access Bundles
- Create and Manage Approval Workflows
- Create and Manage Roles
- Create and Manage Policies
- Create and Manage Access Guardrails
- Create and Manage Organizations from the Manage Identities page
Additionally, Access Control Administrator:
- As a resource owner, can modify, delete, and view resources that they own. Resources can be any Oracle Access Governance entity (Access Bundles, Organizations, Identity Collections, Policies, Approval workflows, Orchestrated Systems, Access Guardrails, or Roles).
- As a reviewer associated with approval workflows, can approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.
- As a user, can use the self-service module to request new access, track requests, assign preferences, and so on.

## Access Control Restricted Administrator (`AG_AccessControl_Admin_Restricted`)

Oracle Access Governance Access Control Restricted Administrator is responsible for creating Access Controls resources in Oracle Access Governance.

Role Can Create Access Control Resources Can Manage Access Control Resources
Access Control Administrator YES YES
Access Control Restricted Administrator YES Limited to resources they own

Access Control Restricted Administrator is primarily responsible to:
- Create Identity Collections, Access Bundles, Approval Workflows, Roles, Policies, and Organizations.
Additionally, Access Control Restricted Administrator:
- As a resource owner, can modify, delete, and view resources that they own. Resources can be any Oracle Access Governance entity (Access Bundles, Organizations, Identity Collections, Policies, Approval workflows, Orchestrated Systems, Access Guardrails, or Roles).
- As a reviewer associated with Approval workflows, can approve access requests and review access tasks.
- As a user, can view the assigned privileges for self and direct reports.
- As a user, can use the self-service module to request new access, track requests, assign preferences, and so on.

Scenario : If Betty is assigned the`AG_AccessControl_Admin_Restricted`role, Betty can create access control resources, such as new identity collections, approval workflows, policies, roles, package permissions into Access Bundles using the Access Controls module. However, Betty can manage (View, edit, delete, and so on) these resources only if Betty is assigned as the resource owner (Primary Owner or one of the Additional Owners) for the resources.

## Auditor (`AG_AUDITOR`)

Oracle Access Governance Auditor role is responsible for monitoring all the campaigns. They can view campaign details, download access review report for each campaign. Download reports across all Oracle Access Governance entities .In addition to viewing report, Auditor can save the reports offline in PDF format or download the CSV data for record-keeping or further analysis or audit.
Additionally, depending on the ownership provided within Oracle Access Governance, an auditor can:
- As a campaign owner, can modify, delete, monitor self-owned access review campaigns.
- As an access reviewer, can review and certify the access review tasks if associated with a specific approval workflow.
- As a resource owner, view, modify and delete resources that they own.
- Create Identity Collections.
- Manage Identity Collections that they own.

## User (`AG_USER`)

Oracle Access Governance user is an end user responsible for viewing and managing their accesses using Oracle Access Governance. All the Oracle Access Governance Active Workforce users are assigned this role, by default.

Your cloud domain administrator can also assign this application role (`AG_USER`) from the OCI cloud service page. Users primarily engage in self-service tasks, which can include requesting permissions through Access Bundles or Roles, viewing access details, managing preferences, changing account passwords, and so on.
Additionally, depending on the ownership provided within Oracle Access Governance, an end user:
- As a campaign owner, can modify, delete, monitor self-owned access review campaigns.
- As an access reviewer, can review and certify the access review tasks if associated with a specific approval workflow.
- As a resource owner, view, modify and delete resources that they own.
- Create Identity Collections.
-
