# Application Roles and Responsibilities Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm
- Fetched: 2026-09-05 03:13 CDT

# Application Roles and Responsibilities Reference

Lists all predefined application roles and corresponding responsibilities. Assign users one or more predefined Oracle Access Governance application roles to start your Identity Governance and Administration journey with Oracle Access Governance .

## Predefined Application Roles

Oracle Access Governance offers several predefined roles to get you started. A single user can hold multiple application roles, as needed.

Here's a list of application roles in Oracle Access Governance:

Oracle Access Governance Application Roles
Application Role Access and Action
Administrator`AG_Administrator`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-agadmin)
- Orchestrated Systems : Create and Manage integrations of Authoritative Sources and Managed systems applications with Oracle Access Governance as Orchestrated systems.
- Access Controls :
- Create and Manage Roles
- Create and Manage Identity Collections
- Create and Manage Organizations
- Create and Manage Policies
- Create and Manage Approval Workflows
- Create and Manage Access Guardrails
- Create and Manage Auto-Generated Access Bundles
- Access Reviews :
- Create Campaigns.
- Modify, Delete, Monitor all access review campaigns.
- Enable and Disable Event-based access reviews for micro-certifications.
- Modify, Delete, Monitor all event-based access reviews
- Define auto-action for low-risk access reviews or unmatched accounts
- Generate Event-Based Access Report and Access Reviews Campaign Report
- Manage Identities and Identity Attributes
- Deactivate or Activate all accounts and associated accesses for an identity managed by Oracle Access Governance
- Revoke one or more permissions assigned directly from the Managed System or provisioned through request.
- Retry Provisioning for Failed or Pending Status
- Enable, Disable, Delete one or multiple accounts
- Manage Notifications
- Settings :
- Create, Modify Security Settings
- Create, Modify Systems Settings
- Reports
- Request and download reports
- Delegations :
- Create, Modify own delegations
- Create, Modify other user's delegations
- Who Has Access to What - Enterprise-wide Browser
- View Enterprise-wide Access Insights
- Create user-created access reviews and download related reports
- Download CSV reports and PDF screenshot
Identity Attributes Admin`AG_IdentityAttributes_Admin`
- Create and Manage Identity Attributes
Service Desk Administrator`AG_ServiceDesk_Admin`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-servicedesk)Related to advanced account administrative functions performed directly from the Service Administration → Manage Identities page.
- View Identity details
- Terminate or Activate all accounts and accesses for an identity managed by Oracle Access Governance
- Enable, Disable, Delete, and Modify accounts
- Retry Provisioning for Failed or Pending Status
- Revoke permissions assigned directly from the Managed System or provisioned through request.
- Manage delegations
- Change Password
- View a list of orchestrated system defined in the Oracle Access Governance service instance.
Campaign Administrator`AG_CampaignAdmin`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-agcampaignadmin)Related to Access Reviews
- Create Campaigns
- Modify, Delete, Monitor self-created campaigns
- View Access Guardrails
Enterprise-wide Access Administrator`(AG_Enterprise_Wide_Access_Admin)`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-enterprisewidebrowser)Related to Who Has Access to What - Enterprise-wide Browser
- View access insights across an enterprise using Enterprise-wide Browser
- Create user-created access reviews and view corresponding time-range-based access review reports
- Download CSV reports and PDF screenshot
- View Access Guardrails
Access Control Administrator`AG_AccessControl_Admin`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-accesscontroladministrator)Related to Access Controls
- Create and Manage Roles
- Create and Manage Identity Collections
- Create and Manage Policies
- Create and Manage Approval Workflows
- Create and Manage Access Bundles
- Create and Manage Organizations
- Create and Manage Access Guardrails
Access Control Restricted Administrator`AG_AccessControl_Admin_Restricted`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-accesscontrolrestrictedadmin)Related to Access Controls
- Create Roles, Identity Collections, Policies, Approval Workflows, , Access Guardrails, Access Bundles, Organizations
- Manage resources that they own, as a resource owner
Application Owner Administrator`AG_AppOwner_Admin`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-appowner)Related to Orchestrated Systems
- Create Orchestrated systems (Authoritative Source and Managed System) to perform new integrations.
- Manage and configure all Orchestrated system defined in the Access Governance service instance.
- View Data Browser information for accounts and granted permissions
- View account and permission details
- Revoke one or more permissions assigned directly from the managed system or provisioned through requests
- Retry provisioning for permissions in Failed or Pending status
- Enable, disable, or delete one or more accounts
Related to Access Controls
- Create Access Bundles, Approval Workflows, Identity Collections, and Auto-generated Access Bundles
- Create and Manage Access Guardrails
- Manage resources that they own, as a resource owner
Application Owner Restricted Administrator`AG_AppOwner_Admin_Restricted`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-restrictedappowner)

Related to Orchestrated Systems
- Create Orchestrated systems (Only Managed System) to perform new integrations.
- Manage and Configure Orchestrated system settings that they own, as resource owner.
Related to Access Controls
- Create Access Bundles, Approval Workflows, Identity Collections, and auto-generated Access Bundles
- Manage resources that they own, as a resource owner.
- View Data Browser information for accounts and granted permissions as a resource owner
Auditor`AG_Auditor`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-agauditor)Related to Access Reviews
- Monitor all access review campaigns
- View Access Guardrails
- Request and download reports
User`AG_User`

[See Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-aguser)
- As a campaign owner - modify, delete, monitor self-owned access review campaigns.
- As an access reviewer - review and certify the access review tasks if associated with a specific approval workflow.
- As an end user - manage the self-service module to view your own accesses, change account password, request access, set preferences, set delegations, manage approvals or track access requests for self or direct reports.
- As a resource owner, view, modify and delete resources that they own.
- As a resource owner, view Data Browser information for accounts and granted permissions
- Create Identity Collections
Note  
  
All Oracle Access Governance active Workforce users are assigned the`AG_User`
