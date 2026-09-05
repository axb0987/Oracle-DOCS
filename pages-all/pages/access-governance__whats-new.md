# What's New in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/whats-new.htm
- Fetched: 2026-09-05 03:16 CDT

# What's New in Oracle Access Governance

Here’s an overview of new features released, including documentation updates.

## August 2026

## Sequential Access Request Processing

Feature Description
Sequential Access Request Processing As an`AG_Administrator`, you can optionally enforce sequential processing of multiple access requests for a single identity, whether as an access bundle, role, or both. For more information, see[Enable Sequential Access Request Processing](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#sequential-access-request-enable).

## Reports

Feature Description
Reports You can now generate downloadable reports for, such as identities, access bundle assignments, accounts, and access bundles. For more information, see[Generate and Download Access Governance Reports](https://docs.oracle.com/en-us/iaas/Content/access-governance/reports-overview.htm#reports-overview).

## July 2026

## Microsoft Entra ID Orchestrated systems

Feature Description
Microsoft Entra ID Microsoft Entra ID Orchestrated systems now support using OCI Vault as a credential store. Existing Microsoft Entra ID Orchestrated systems that store credentials in Oracle Access Governance can also migrate those credentials to OCI Vault.

For more details, see[Integrate with Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-microsoft-entra-id.htm).

## June 2026

## PeopleSoft Orchestrated systems

Feature Description
PeopleSoft Oracle Access Governance now supports integration with PeopleSoft Enterprise Learning Management (ELM) and PeopleSoft Financials and Supply Chain Management (FSCM) applications as an authoritative source and a managed system. You can now perform identity reconciliation, account management, role assignments, and reconciliation operations in PeopleSoft ELM and PeopleSoft FSCM.

For more details, see[Configure Integration Between Oracle Access Governance and PeopleSoft](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-peoplesoft.htm#configure-integration-between-oracle-access-governance-and-peoplesoft).

## Campaigns

Feature Description
Primary and Secondary Owners Campaigns

You can add one primary and up to 20 additional owners for campaigns. For existing campaigns, campaign owner would be selected as the primary owner, with no secondary owners. You can also run ownership reviews for Campaigns.

See[Add Owners](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm#id_c3r_gnt_njc).
Delete Campaigns You can now delete campaigns in the Terminated , System ended , Draft or Approved statuses. See[Delete a Campaign](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-review-campaigns.htm#delete-campaign).

## New Approval Workflow Template - Business Approvers

Feature Description
Approval Workflow - Business Approvers

A new approval workflow template is available for reviewing and approving access requests based on business needs. You can assign business approvers to access bundles and roles without granting ownership or management privileges for the associated access resources. See[Business Approvers](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-approval-workflows-types__business-approver)and[Bundle Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-settings).

## May 2026

## Oracle Customer Experience (CX) Sales Orchestrated systems

Feature Description
Oracle Customer Experience (CX) Sales Oracle Access Governance now supports Oracle CX (Sales) integration as a managed system. This integration supports account provisioning and reconciliation operations for resource users, organizations, resource roles, and organization role assignments in Oracle CX (Sales).

For more details, see[Integrate Oracle Access Governance with Oracle Customer Experience (CX) Sales](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-cx.htm#integrate-oracle-access-governance-with-oracle-cx),[Configure Integration with Oracle Customer Experience (CX) Sales](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-with-oracle-cx.htm#oracle-cx-configure-integration-with-oracle-cx), and[Oracle Customer Experience (CX) Sales Integration Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-cx-integration-reference.htm#oracle-cx-oracle-cx-integration-reference).

## Data Browser for Orchestrated systems

Feature Description
Data Browser

You can now use the Data Browser dashboard to view reconciled accounts and granted permissions associated with a Managed system. You can review access data and perform supported account and permission management operations. See[Data Browser: View Accounts and Granted Permissions for Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm#data-browser-overview)and[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

## Mask Sensitive Managed System Account Attribute Values

Feature Description
Mask Sensitive Managed System Account Attribute Values Oracle Access Governance supports masking managed system account attribute values from the Account Attributes page. When enabled, the selected attribute values are displayed as asterisks (*). See[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

## Generic REST (Standard UI Driven)

Feature Description
Generic REST (Standard UI Driven) Oracle Access Governance now supports Generic REST (Standard UI-driven) integration to onboard REST-based applications as a Managed system using the Oracle Access Governance Console for account provisioning and reconciliation. You can use this for applications where direct connectors aren't available. See[Integrate with Generic REST (Standard UI-driven)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest-standard.htm).

## Area of Responsibility Templates

Feature Description
Provision Area of Responsibility (AOR) Assignments Using AOR Templates Oracle Access Governance now supports provisioning of Area of Responsibility (AOR) assignments using AOR templates defined in Oracle Fusion Cloud Applications. See[Area of Responsibility (AOR)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#oracle-fusion-ofa-functional-overview__aor-concept)and[AOR Template-Based Provisioning](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#create-aor-template).

## Global Identity Attributes Handling For Null Values

Feature Description
Identity Attribute Handling for Null Values

For Global Identity attributes, you can now configure attribute mappings to ignore null or empty values received from identity sources, ensuring that existing attribute values remain unchanged during synchronization. See[Manage Global Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).

## Delete Orchestrated Systems

Feature Description
Delete Orchestrated System

You can now delete an orchestrated system in the Draft state. See[Delete an Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#delete-orchestrated-system).

## April 2026

## Control User Password Resets for Orchestrated Systems

Feature Description
Control Password Resets Application owners can now enable or disable user password resets from the Account Lifecycle settings for orchestrated systems. Password resets are available only if supported by the system. See[Manage Account Settings for your Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-accountsettings).

## Session Idle Timeout

Feature Description
Administrative Settings - Session Idle Timeout As an Oracle Access Governance administrator, you can now configure the session idle timeout for the Oracle Access Governance service instance. If no idle timeout is configured, then a default timeout of 60 minutes is applied to each session. See[Session Idle Timeout](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#inactivity-timeout).

## Access Guardrail Condition: Identity Account on a System

Feature Description
Access Guardrail - New Condition Type You can now define access guardrails using a new condition that requires identities to have an account on a specified system before access is granted. See[Define Rules for Access Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-guardrails.htm#define-guardrails-rules).

## Oracle Identity Governance (OIG) Supported Modes

Feature Description
Oracle Identity Governance (OIG) Oracle Identity Governance (OIG) : When creating a new orchestrated system, you can now configure Oracle Identity Governance (OIG) as an authoritative source for identities and attributes, or for identity attributes only. Oracle Access Governance always manages permissions for the Oracle Identity Governance (OIG) for orchestrated system. See[Oracle Identity Governance - Add Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-identity-governance.htm#oig-add-details).

## Support of Resource Principal Authentication in Flat File Systems

Feature Description
Flat File: Resource Principal You can now integrate Oracle Access Governance with generic Flat File systems using Resource Principal authentication. Existing orchestrated systems must migrate from API key-based connections to the Resource Principal authentication method. See[Migrate API Key Access to Resource Principal Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#migrate-api-key-access-to-resource-principal-access).

## March 2026 Update

## Integrations - Orchestrated Systems

Feature Description
Oracle Warehouse Management Cloud (WMS) Oracle Warehouse Management Cloud (WMS) : Oracle Access Governance now supports identity orchestration to reconcile and provision accounts, companies, facilities as a Managed System. See[Integrate with Oracle Warehouse Management Cloud (WMS)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-wms-cloud.htm#integrate-with-wms-cloud).

## Approval Workflow templates

Feature Description
Approval Workflow Approval workflow templates are updated, as follows:
- Owner : The approval request is sent to the resource owners (primary and additional owners)
- Primary owner : The approval request is sent to the resource's primary owner

For approval workflow template details, see[Approval Workflows in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-approval-workflow-overview).

## Account Lifecycle Management

Feature Description
Birthright Access and Early Termination You can now assign birthright access to users based on the joining date and revoke accesses in case of early termination. For details, see[Granting Birthright Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm)and[Revoke Access for an Early Termination](https://docs.oracle.com/en-us/iaas/Content/access-governance/revoke-access-early-termination.htm).
Global Account Termination Settings Administrators can configure global account termination settings for all orchestrated systems. You can also define override rules based on identity attribute values to exclude specific users from account termination. See[Global Account Termination Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#global-account-termination-settings).
Account Settings for Orchestrated Systems If global account termination settings are enabled, application administrators (`AG_AppOwner_Admin`) can’t manage account termination settings at the orchestrated system level. Configure the account settings to support account management for both early termination and final termination of identities. See[Manage Account Settings for your Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-accountsettings).

## Integrations - Orchestrated Systems

Feature Description
OCI Vault for storing credentials for Oracle Fusion Cloud Applications Oracle Access Governance uses OCI Vault to store credentials for Oracle Fusion Cloud Applications. See[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm#oracle-fusion-integrationsettings).
Generic REST Connector: Resource Principal You can now integrate Oracle Access Governance with Generic REST Connector using Resource Principal authentication. You must migrate from API Key-based connections to Resource Principal. See[Migrate API Key Access to Resource Principal Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest.htm#migrate-api-key-access-to-resource-principal-access)and[Configure Generic REST](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest.htm#rest-configure).

## Identity/Account Matching Rules

Feature Description
Enhanced Account Correlation and Dynamic Matching Rules Improved identity/account correlation capabilities to apply rules to all incoming data, only new data, or disable matching entirely. You can now view insights for match results, including matched, unmatched, or multi-matched identities/accounts. See[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)and[Insights for Match Results](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules__insights-matching-rules).

## Authoritative Source - Source of Identity Attributes

Feature Description
Enhanced configuration for Authoritative Sources When creating a new orchestrated system, you can now configure whether to set the authoritative source as a source of identities and attributes, or identity attributes only. See[Integrate with Flat File](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-configure).

## February 2026 Update

## Self Service - Password Reset

Feature Description
Reset password for accounts managed by Oracle Access Governance You can now reset password for accounts managed by Oracle Access Governance. AG_Administrator can configure the password policy for the enterprise. For details, see Reset Password for Managed System Accounts and[Configure Password Policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#configure-password-policy).

## Integrations - Update to Orchestrated Systems

Feature Description
Integrate with Oracle Transport and Global Trade Management (OTM/GTM) Oracle Transport and Global Trade Management (OTM/GTM) : You can now provision multiple user roles from an access bundle and assign a default user role from Oracle Access Governance. See[Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-integrate-with-otm-gtm.htm).

## January 2026 Update

## Integrations - Update to Orchestrated Systems

Feature Description
Integrate with Palo Alto Networks Prisma Cloud Palo Alto Networks Prisma Cloud : Oracle Access Governance now supports identity orchestration to reconcile and provision accounts and manage groups as a Managed System. For details, see[Integrate with Palo Alto Networks Prisma Cloud](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-prisma-cloud.htm).
Integrate with Atlassian Jira Atlassian Jira : You now have support for JIRA integration using experimental APIs to reliably retrieve all necessary attributes from the JIRA environment. For details, see[Configure Integration Between Oracle Access Governance and Atlassian JIRA](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm).
Integrate with Eloqua Eloqua : You can now configure Eloqua using OAuth for secure authentication. For details to connect Oracle Access Governance to Eloqua using OAuth, see[Integrate with Eloqua](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-eloqua.htm).
Integrate with Oracle Fusion Cloud Applications Oracle Fusion Cloud Applications : Manage provisioning of procurement agents from Oracle Access Governance configured for ERP or Both application types. For details, see[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm#oracle-fusion-integrationsettings)and[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-default-supported-attributes-1).

## Event-driven Access Reviews

Feature Description
Event-based Setup → Change Events You can create, edit or delete change event configurations and apply filters to narrow the review scope to specific applications/permissions. For details, see[Configure and Manage Event-based Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-and-manage-event-based-access-reviews.htm).

## December 2025 Update

## Support for Editing User Capabilities from Oracle Access Governance for OCI IAM Orchestrated System

Feature Description
Integrate with Oracle Cloud Infrastructure (OCI) Oracle Cloud Infrastructure (OCI) : You can now edit user capabilities from Oracle Access Governance by creating an account profile for one or more OCI IAM domains, configured as Managed System. See[Edit User Capabilities for OCI Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#edit-user-capabilities-with-oci-account-profile).

## Account Lifecycle Settings - Delete Permissions for Disabled Accounts

Feature Description
Account Lifecycle Settings - Leaver Workflow For an orchestrated system, in the Account Lifecycle settings, you can now configure the system to delete all associated permissions for all accounts that are disabled when someone leaves the organization, or when a Leaver workflow is triggered for any reason. See[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

## Inbound Data Transformation - Multi-Attribute Association

Feature Description
Inbound Data Transformation You can use inbound transformation rule to map a value to multiple attributes at once. For example, see[Multiple Attribute Rule in Inbound Transformation](https://docs.oracle.com/en-us/iaas/Content/access-governance/transformation-for-inbound-and-outbound-rules.htm#multiple-attribute-rule-in-inbound-transformation).

## Oracle Fusion Cloud Applications Orchestrated System

Feature Description
Integrate with Oracle Fusion Cloud Applications Oracle Fusion Cloud Applications
- Oracle Access Governance now supports Assignment DFFs from Oracle Fusion Applications for Oracle HCM or Both , integrated as an Authoritative Source. See[Support for Assignment Descriptive Flex Fields (DFF)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-supportassignmentdff).
- New default attribute:`lastWorkingDate`. See[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-default-supported-attributes-1).

## Microsoft Active Directory Orchestrated System

Feature Description
Integrate with Microsoft Active Directory Microsoft Active Directory : New configuration fields are added
- Support referrals for provisioning and account management operations within a single forest.
- Support custom date-type attribute names for Large Integer syntax attributes.

See[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-microsoft-active.htm#microsoft-ad-integrationsettings).

## Manage Identity Attributes - Any System Available

Feature Description
Manage Identity Attributes To load attribute value when unique identity data is received from different authoritative sources, in the Identity Attributes page, select Any system available to retrieve the value from the orchestrated system with the most recent data load. See[Manage Global Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).

## November 2025 Update

## Administrative Settings from Oracle Access Governance Console

Feature Description
Administrative Settings from Oracle Access Governance Console As an AG_Administrator , you can customize console settings from the Service Administration → Settings tab. Currently, you can restrict or allow non-administrator users to export identity, account and enterprise-wide data to CSV from the Oracle Access Governance Console. For more details, see[Administrative Settings in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm).

## Approval Workflows - Auto Approval Decision Matrix

Feature Description
Approval Workflows - Auto Approval Decision The approvals workflow automatically approves access requests based on specific workflow configurations and presence of guardrails or SOD violations. For more details, see[Auto Approval Decision Matrix](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#auto-approval-matrices-and-criteria).

## Support to Create Complex Identity Attributes from Oracle Access Governance Console

Feature Description
Create Simple and Complex Identity Attributes for an Authoritative Source You can now create simple and complex identity attributes for an Authoritative Source and source its value from the source system or derive its value from a rule. In cases where complex custom attributes are defined, create an affiliation to use them for Oracle Access Governance features. For more details, see[Manage Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#customattributes-settings).

## Configure Partial Data Load Schedule Settings for an Orchestrated System

Feature Description
Configure Partial Data Load Schedule Settings for an Orchestrated System Enable incremental data ingestion by loading only the new or updated records since the last load, instead of performing a full data load on entire data set. Currently, this applies only for Oracle Fusion Cloud Applications . For more details, see[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings)and[Enable Atom Feeds for Partial Data Load](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-enable-atom-feeds-partial-dataload).

## Change Password for Directly Provisioned Accounts and Manager-Led Password Reset

Feature Description
Change Password You can now change the password for reconciled accounts, that is, accounts provisioned directly in the Managed Systems with Grant type as`DIRECT`. Additionally, Managers can change password on behalf of their direct reports from the Who Has Access to What , and then the My Directs' Access page. For more information, see[Change Account Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password)and[My Directs' Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm#team-access)

## Identity Attribute Visibility Controlled by Enabled Identity Flags on Who Has Access to What Pages

Feature Description
Identity Attribute visibility for enabled Identity flags Identity attributes are displayed on the Who Has Access to What pages and the identity attribute details page only if the corresponding identity flags are enabled. If these flags are not enabled, the identity attributes are not displayed. To enable flags, see[Manage Global Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).

## UI Console Navigation updates to Manage System Identity Attributes and Affiliations

Feature Description
Navigation updates to Manage Attributes and Affiliations. You can now manage identity attributes and affiliations from the Manage Integrations page for a specific Orchestrated system. See[Manage System Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-create-system-identity-attribute)and[Manage and Configure Affiliations](https://docs.oracle.com/en-us/iaas/Content/access-governance/affiliations-configure-affiliations.htm).

## October 2025 Update

## Revision Management support for Oracle Access Governance resources

Feature Description
Revision Management with approval workflow support Oracle Access Governance enables you to propose, review, and manage changes to key resources such as Identity Collections, Organizations, Active and Consumer Identities before implementation. If configured, resource edits or deletions go through an approval workflow, and users can track all changes, view detailed revision history, and approval request trail for the resources. For more information, see[Revision Management in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm).

## Flat File Orchestrated System supports Virtual Systems

Feature Description
Integrate with Flat File Flat File : Oracle Access Governance now supports multiple applications in a single Flat File orchestrated system as Virtual Systems.

Virtual Systems allow you to manage multiple related applications or domains as logical subsystems within a single orchestrated system integration. Each system share the same structural schema but has different data. See[Understanding Virtual Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#virtual-systems)and[Integrate with Flat File](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-configure).

## OCI IAM Domains as Authoritative Source or Managed System

Feature Description
Integrate with Oracle Cloud Infrastructure (OCI) Oracle Cloud Infrastructure (OCI) : You can now choose one or more OCI IAM domains as either Authoritative Source or Managed System, or both.

Authoritative Source domains are used to build identity profiles. The domains selected as Managed Systems are used for tasks like managing identities, running access reviews, and setting up access controls. See[Integrate with Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm).

## September 2025 Update

## Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Oracle Infinity Oracle Infinity : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle Infinity as a Managed System.

Oracle Infinity is a cloud-based digital analytics platform that helps organizations track, analyze, and optimize customer interactions and behavior, providing insights to improve customer experiences and business results.

To connect successfully, you must have an active connection with Oracle Cloud Infrastructure (OCI) orchestrated system in the same tenancy and domain as Oracle Infinity. With this integration, you can create and revoke Oracle Infinity accounts using Oracle Access Governance. See[Integrate with Oracle Infinity](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-infinity-integrate-with-infinity.htm#oracle-infinity-overview-infinity).

## Safeguard against Data Loss with Safety Check Settings

Feature Description
Safety Checks to prevent Data Loss You can now configure safety checks in the data load settings of your orchestrated system to prevent accidental or unintended data loss when managing identities in Oracle Access Governance. Specify the maximum allowed percentage decrease (% ↓) for identities, accounts, or permissions during data load; if a data load exceeds this limit, the operation will automatically fail. See[Configure Safety Checks for Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-safety-checks-for-orchestrated-systems).

## Access Bundles

Feature Description
Request Limited to Members of Organization As an Access Control Administrator, you can now configure access bundles and roles in Oracle Access Governance to limit their availability in the self-service request flow to members of specific organizations. You must create the relevant organization in Oracle Access Governance.

This provides granular access control by ensuring that only members of an organization can request designated permission sets. See[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm)

## August 2025 Update

## Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Oracle Transport and Global Trade Management (OTM/GTM) Oracle Transport and Global Trade Management (OTM/GTM) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle Transport and Global Trade Management (OTM/GTM) as a Managed System.

Oracle Transport and Global Trade Management (OTM/GTM) is a cloud-based solution that helps organizations manage, optimize, and streamline the transportation and global trade operations. With this integration, you can create, update, enable, disable, delete accounts, change password for accounts. You can also manage roles and business intelligence role assignments for identities from Oracle Access Governance. See[Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-integrate-with-otm-gtm.htm)
Integrate with Oracle Configure, Price, Quote (CPQ) Oracle Configure, Price, Quote (CPQ) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle Configure, Price, Quote (CPQ) as a Managed System.

Oracle Configure, Price, Quote (CPQ) is a cloud-based solution that streamlines and automates the configuration, pricing, and quoting processes for complex products and services, helping sales teams deliver accurate quotes. With this integration, you can create, update, enable, disable accounts. You can also change password for accounts and manage permissions and group assignment (Add/Remove Sales and Admin Group) for identities from Oracle Access Governance. See[Integrate with Oracle Configure, Price, Quote (CPQ)](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-integrate-with-cpq.htm)
Integrate with Oracle Unity Oracle Unity : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle Unity as a Managed System. To connect successfully, you must have an active connection with Oracle Cloud Infrastructure (OCI) orchestrated system in the same tenancy and domain as Oracle Unity.

With this integration, you can create, update, enable, and disable accounts. You can also manage role assignments for identities from Oracle Access Governance. See[Integrate Oracle Access Governance with Oracle Unity](https://docs.oracle.com/en-us/iaas/Content/access-governance/unity.htm)

## Access Guardrails for Identity Collections

Feature Description
Access Guardrails for Identity Collections Access Guardrails support is extended to Identity Collections. This allows Access Control Administrators to establish preventive access control measures, ensuring that authorized and compliant identities, those meeting predefined criteria, are members of an Identity Collection. If these conditions are not met, a violation is raised, and you can choose to block access immediately or allow a grace period for compliance.

## July 2025 Update

## Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Oracle APEX Oracle APEX : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle APEX as a Managed System.

Oracle APEX is a low-code development platform that enables users to rapidly design and build scalable, secure, and feature-rich applications with minimal programming required. With this integration, you can create, update, delete accounts, change password for accounts. You can also manage group and privilege assignment at workspace and global level for identities from Oracle Access Governance. See[Integrate Oracle Access Governance with Oracle APEX](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-oracle-apex.htm)
Integrate with SAP Fieldglass SAP Fieldglass : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in SAP Fieldglass as a Managed System.

SAP Fieldglass is a cloud-based vendor management system that helps organizations efficiently manage their external workforce providing visibility, compliance, and cost control over contract workers. With this integration, you can create, update, delete accounts. You can also manage group assignment for identities from Oracle Access Governance.
Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM): Use Resource Principal You can now integrate Oracle Access Governance with your Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) instance using Resource Principal authentication. You must migrate from API Key-based connections to Resource Principals, enabling more secure, streamlined, and compliant access to OCI IAM resources. For more information, see[Integrate with Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm)and[How To Migrate API Key Access To Resource Principal Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-policyhowto).
Integrate with Database Application Tables Oracle Access Governance now retains mapping for the associated identity attributes even after you update the Day N DBAT schema. Changes like modifying display names or adding new attributes will not override your existing mappings.

For example, if you map the "firstName" account attribute to a specific identity attribute and later change attribute display names, your original "firstName" mapping will remain intact.
Integrate with Flat File Oracle Access Governance now supports schema extension for Flat File orchestrated systems. You can create, edit, delete, and associate identity attributes for these custom attributes from the Oracle Access Governance Console. See[Schema Extension - Adding Custom Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-schemaextension).

## Campaigns and Access Reviews

Feature Description
Pending Access Reviews for a Campaign You can now view pending access review tasks for an in-progress campaign from the View Campaign Details page.

You can reassign pending access reviews to another reviewer, provided the reviewer is not a beneficiary.

In addition, you can download a list of pending access reviews for a campaign for audit and analysis purposes.

## June 2025 Update

## Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with SAP User Management (UM) SAP User Management (UM) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in SAP User Management (UM) as a Managed System.

SAP User Management (UM) handles the creation, maintenance, and control of user access across SAP systems. With this integration, you can create, update, password change accounts. You can manage group and role assignment for identities using Access Bundles from Oracle Access Governance. For more information, see[Integrate Oracle Access Governance with SAP User Management (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-integrate-oracle-access-governance-with-sap-user-management-um.htm).
Oracle Fusion Cloud Applications: Automated SoD Approvals handling through Oracle Access Governance Oracle Access Governance now automates the provisioning of SoD-flagged violations by passing approval decisions—including justifications and conditional acknowledgments—directly to Risk Management Cloud (RMC). This eliminates the need for re-approve SoD-flagged entitlement in RMC. For more information, see[Preventive Segregation of Duties](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#preventive-segregation-of-duties).

Campaigns

Feature Description
Access Reviews only for Certifiable entitlements in OIG For Oracle Identity Governance (OIG) system, you can only review entitlements that have the Certifiable flag selected.
- Which permissions? and Which roles? : Generates an access review only for entitlements and roles where the Certifiable flag is selected.
- Which applications : Generates access review for accounts and entitlements if the application has the Certifiable selected in OIG.

For more information, see[Access Reviews Campaigns Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm#access-reviews-campaigns-adddetails).

Application Roles

Feature Description
Application Owner`AG_App_Owner_Restricted_Admin`For new integrations,`AG_App_Owner_Restricted_Admin`cannot configure an authoritative source. Only`AG_App_Owner_Admin`or`AG_Administrator`can configure an authoritative source for an application.

Revoke OCI IAM Groups or OCI Application Roles from Manage Identities

Feature Description
Revoke OCI IAM Groups or OCI Application Roles From the Manage Identities page, users with AG_ServiceDesk_Admin role can now directly revoke one or more permissions (OCI IAM Groups or Application Roles) assigned directly or provisioned through request. For example, using Oracle Access Governance, you can revoke an application role for an identity.

## User Experience Enhancements

Feature Description
User Experience Enhancements With the new UI improvements, you can now easily search, filter, and select access bundles, roles, and self-service access requests. These enhancements provide better visibility and enable more informed decision-making

## May 2025 Update

Affiliations in Oracle Access Governance

Feature Description
Identity Attributes → Affiliations Oracle Access Governance now supports Affiliations, enabling flexible and complex identity representation. A single identity can represent multiple roles or relationships, such as being both an employee and a student, each with distinct access needs.

Administrators (`AG_Administrator`) can define and manage Affiliations from the Identity Attributes page. These attributes can be used across various features, including campaigns, event-based reviews, choosing identities for identity collections, or applying attribute conditions to enable/disable the available identity data set.

Using Affiliations, you can also segregate and simplify complex data types (like object arrays) into simpler data types.

Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Database User Management (PostgreSQL) Database User Management (PostgreSQL) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Database User Management (PostgreSQL) as a Managed System.

PostgreSQL is an open-source relational database management system widely used in big data applications, enterprise software, and web services.

With this integration, you can create and manage accounts, role assignments, and privilege assignment from Oracle Access Governance.
Integrate with Oracle Fusion Cloud Applications: OAuth-based Authentication Oracle Fusion Cloud Applications : Oracle Access Governance now supports OCI OAuth-based authentication to integrate with your Oracle Fusion Cloud Applications instance. In your integration settings, you must select the Do you want to use OCI IAM for authentication? check box and include the OCI IAM tenancy and confidential application details. For more information, see[Authenticating with OCI OAuth](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-oauth-prereqs).
Integrate with Oracle Fusion Cloud Applications HCM: Areas of Responsibility Support as an Account Attribute Oracle Fusion Cloud Applications HCM : Oracle Access Governance now supports data synchronization and reconciliation operations based on the additional Area of Responsibility (AOR) attributes.

In Oracle Fusion Cloud Human Capital Management (Fusion HCM), AOR defines security roles based on a person’s or team’s scope of responsibility, determining which records they can access and act upon.

To enable AOR integration, select the Do you want to enable areas of responsibility? check box in integration settings.

When an identity is linked to an AOR, Oracle Access Governance performs data loads and syncs the updated value based on AOR account attribute value. For reference AOR attributes, see[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#oracle-fusion-default-supported-attributes-1).
Integrate with Microsoft Active Directory: Active Directory Lightweight Directory Services (AD LDS) Microsoft Active Directory : Oracle Access Governance now supports Active Directory Lightweight Directory Services (AD LDS) as an extension to your existing Microsoft Active Directory orchestrated system. In the integration settings, select the Is this Active Directory is a Lightweight Directory Services (AD LDS) environment check box.

This integrations allows you to use dedicated directory services for each application than use for entire enterprise. For more information, see[Integrate Oracle Access Governance with Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-oracle-access-governance-with-microsoft-active-directory.htm).
Integrate with ServiceNow User Management ServiceNow User Management : Oracle Access Governance now supports identity orchestration, reconciliation, and centralized provisioning of identity accounts for ServiceNow, both as an Authoritative Source and a Managed System.

ServiceNow is a cloud-based platform that delivers digital workflows to automate business processes. The integration is facilitated through the Oracle Access Governance User Management application, certified and available on the ServiceNow marketplace.

With this integration, you can create and manage accounts, role assignment and group assignment from Oracle Access Governance. For more information, see[Integrate with ServiceNow](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-servicenow-um.htm).
Integrate with Microsoft Entra ID Microsoft Entra ID : Oracle Access Governance now supports Azure AD B2C integration as an extension to your existing Microsoft Entra ID orchestrated system.

With this integration, you can now manage internal and external identities, such as customers and partners, directly within Oracle Access Governance. You can manage identity accounts and group assignments for these identities.

Granting Time-Bound Access in Oracle Access Governance

Feature Description
Access Bundle In the access bundle creation workflow, in the Time limits task, you can set the expiration period. Choose Indefinitely for permanent access, or specify the maximum number of days or hours until which this access should be granted. Additionally, users will also receive notifications before the access permission is revoked, and can request an extension if allowed from the My Access page.
Approvals As an approver, you can now grant temporary access to an access bundle in addition to the existing configuration. Access can be approved for a specified duration, even if the access bundle allows a longer period. You may set the number of days or hours needed or define a specific start and end time for the access.
Request Access → Request access bundle As an AG_USER , you can now request temporary access to an access bundle. When making a request, choose Indefinitely for permanent access, specify the maximum number of days or hours needed, or set a specific start and end time for the access.
Access reviews You can now grant time-based access for a defined number of days while approving access review tasks. In the My Access Review page, while approving a request, choose Indefinitely for permanent access or set an expiration period for temporary access. This action is available for individual requests, ensuring precise control over each access approval.
Manage Identities As an AG_ServiceDesk_Admin user, you can now request an extension for the soon-to-expire access, based on the allowed number of days defined during access bundle configuration. Users can also request an extension themselves from the My Access page.

Configure Approval Workflows only for Violations in Access Bundle Requests

Feature Description
Configure Approval Workflows only for Violations in Access Bundle Requests You can now configure access bundles to trigger selected approval workflow only when an access request results in a violation against an access guardrail or Segregation of Duties (SoD), else request gets auto-approved.

Campaigns

Feature Description
Update Campaigns configuration to prevent generation of account review tasks In the Create Campaign workflow, you can now create identity access reviews only for permissions without creating account access reviews. This functionality is not available in campaigns created for OCI. For more information, see[Add Campaign Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm#access-reviews-campaigns-adddetails).

## April 2025 Update

Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Oracle Enterprise Performance Management (EPM) Oracle Enterprise Performance Management (EPM) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Oracle Enterprise Performance Management (EPM) as a Managed System.

Oracle Enterprise Performance Management (EPM) is a cloud-based software that helps businesses make informed decisions by streamline planning, budgeting, forecasting, and financial close processes with advanced analytics and automation. With this integration, you can create and manage predefined roles, application roles, and EPM group assignment from Oracle Access Governance. To connect successfully, you must have an active connection with Oracle Cloud Infrastructure (OCI) orchestrated system in the same tenancy and domain as Oracle Enterprise Performance Management (EPM). For more information, see[Integrate with Oracle Enterprise Performance Management (EPM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-enterprise-performance-management-epm.htm).

Get Failed Event Details with Diagnostic Service Logs using OCI Logging service

Feature Description
Diagnostic Service Logs You can now view diagnostic logs from Oracle Access Governance for performing informed troubleshooting using the OCI Logging service. You can view details in a JSON format whenever an operation is failed, such as a campaign creation is system ended. As an OCI Administrator, you can configure the Oracle Access Governance service logs for your service instance. For more information, see[Diagnostic Service Logs in Oracle Access Governance Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/diagnostic-service-logs-in-oracle-access-governance-overview.htm).

Campaigns

Feature Description
Campaign Ownership Change You can now change campaign ownership for an ongoing In Progress or Ready For Approval campaigns. For more information, refer[Campaign Ownership Change](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-review-campaigns.htm#campaign-ownership-change).

## March 2025 Update

Oracle Access Governance REST APIs Availability

Feature Description
Oracle Access Governance REST APIs Availability Oracle Access Governance released REST APIs to automate and extend Identity Governance and Administration (IGA) capabilities. The REST APIs will be available with an Oracle Access Governance Premium license. You can streamline access control processes, improve compliance, and enhance the overall identity management across diverse environments. For more details, see[Oracle Access Governance REST APIs](https://docs.oracle.com/en/cloud/paas/access-governance/pmapi/index.html).

Audit Events and Event Data Publisher in Oracle Access Governance

Feature Description
Audit Events as part of Event Data Publisher You can now get comprehensive audit trail of actions performed within Oracle Access Governance, in near real-time for compliance, creating customized reports, or for troubleshooting purposes. To configure receiving audit events in your OCI Stream, select the Audit event option on the Data Feed configuration page. You'll receive a JSON response, containing detailed interactions points, such as who initiated the request, which resource IDs were involved, what action was performed, request and response payloads for each action, along with additional details.
Additional Oracle Access Governance components supported for Event Data Publisher You can now receive additional data events, such as Access Guardrails, Permission Assignments, Roles, and so on for all Orchestrated systems managed by Oracle Access Governance. The setup configuration remains unchanged, Day 0 events will be exported to OCI Buckets and subsequent events are published to OCI Streams.

Integrate Oracle Access Governance with Orchestrated Systems

Feature Description
Integrate with Atlassian Jira Atlassian Jira : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Atlassian JIRA as a Managed System.

Atlassian Jira is a comprehensive project management and issue tracking tool that enables teams to plan, prioritize, monitor tasks effectively. With this integration, you can create and manage identity accounts and group assignment from Oracle Access Governance.
Integrate with PeopleSoft Human Capital Management (HCM) For PeopleSoft, you can now:
- Perform data load of identities for an employee or contractor data not associated with any user profile in PeopleSoft.
- Use extended support of default attribute to manage accounts. To support these feature updates, the existing configuration remains unchanged. However, as a prerequisite, an extended setup to create database views, synonyms, and grant permissions are required.
Integrate with Oracle Fusion Cloud Applications Human Capital (HCM) For Oracle Fusion Cloud Applications Human Capital (HCM):
- Authoritative Source: You can now perform identity data load and manage accounts based on a Person record, even if there is no associated User Account for that identity.
- Managed System: You can create and manage SCIM user accounts based on the Person record managed by Oracle Access Governance. For successful provisioning, you must add an outbound transformation rule to set the Person Number attribute value.

Managed System Account Management - Account Lifecycle Settings

Feature Description
Account Lifecycle Settings In the Orchestrated System Account Lifecycle settings, the following enhancements have been done:
- For a Joiner use case, you can now configure whether Oracle Access Governance should create new accounts or manage permissions only for the reconciled accounts. If the Allow Access Governance to create new accounts option is unchecked, Oracle Access Governance will not create new accounts but can only manage permissions for the existing accounts.
- For a Leaver use case, select Include accounts that are not created by Access Governance to disable or delete direct accounts (`grant_type Direct`) not provisioned or managed through Oracle Access Governance.
- For accounts with no remaining permissions (mover or leaver), you can now choose to Delete , Disable , or take No action . If you select No action , accounts will not be disabled or revoked and the user may have access to the accounts beyond the Oracle Access Governance scope.

For more information, see[Manage Account Lifecycle with Service Desk Executive Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).

Additional Service Enhancements

Feature Description
Campaigns → My Access Reviews You can now search identity access reviews based on Oracle Access Governance Organization name.
Who Has Access to What → Enterprise-wide Browser Compartment Reports For an OCI Orchestrated system, you can now you can now export compartment report using the Export compartment report button from the Enterprise-wide Browser page to view available resource details in that compartment along with access information for identities associated with these resources. For more information, see[Generate Compartment Report](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm#generate-compartment-report).

## February 2025 Update

Integrate Oracle Access Governance with New Orchestrated Systems

Feature Description
Integrate with SAP SuccessFactors SAP SuccessFactors : Oracle Access Governance now supports onboarding of identities, provisioning, and reconciliation of accounts in SAP SuccessFactors as an Authoritative Source and as a Managed System.

SAP SuccessFactors is a cloud-based Human Capital Management (HCM) software that helps organizations manage various HR functions, including talent management, onboarding, payrolls, or other HR processes. With this integration, you can manage identity accounts and group assignment from Oracle Access Governance. For more information, see[Integrate with SAP SuccessFactors](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-successfactors.htm#sap-successfactors-integration-overview).
Integrate with Workday Workday : Oracle Access Governance now supports onboarding of identities, provisioning, and reconciliation of accounts in Workday HCM as an Authoritative Source and as a Managed System.

Workday is a cloud-based Human Capital Management (HCM) and workforce management software that helps organizations streamline various HR functions, including talent management, workforce planning, onboarding, payrolls, or other core HR processes. With this integration, you can manage identity accounts and security group assignment from Oracle Access Governance. For more information, see[Integrate with Workday](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-workday.htm#workday-integration-overview).

Modify Account Attributes from Oracle Access Governance Console

Feature Description
Modify Account Attributes As a Service Desk Administrator (`AG_ServiceDesk_Admin`), Oracle Access Governance allows you to directly update default or custom account attributes without any approval workflow.

From the Manage Identities &gt; Account details page. Click the Edit Account operation to modify the value of account attributes. After you have updated the account attributes, it triggers the Update Account operation on the Orchestrated system.

For example, based on the attributes supported for an Orchestrated system, you can use this feature to update Account Name, Locked status, address change, password and so on. For more information, see[Modify Account Attributes from Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#modify-account-attributes).

## January 2025 Update

Access Guardrails in Oracle Access Governance

Feature Description
Access Guardrails in Oracle Access Governance Access Guardrails in Oracle Access Governance, allows you to establish preventive access control measures to ensure that authorized and compliant identities gain access. You can define a set of conditions that an identity must meet before gaining an access to a permission — such as completing mandatory trainings, or meeting policy requirements. If these conditions are not met, a violation is raised, and you can choose to block access immediately or allow a grace period for compliance. For more information, see[Enforce Preventive Access Control Conditions](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm).

AI-Powered Access Bundle Recommendation Engine in Oracle Access Governance

Feature Description
AI-Powered Access Bundle Recommendation Engine in Oracle Access Governance Oracle Access Governance now supports AI-powered intelligent Access Bundle Recommendation capability to instantly get a list of pre-bundled sets of permissions, based on usage patterns and relationship mapping from Managed Systems. Instead of manually creating access bundles and associating permissions, the system suggests access bundles that you can accept, edit, or reject, making access provisioning faster and more efficient. For more information, see[AI-Powered Access Bundle Generation for Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/ai-powered-access-bundle-generation-for-orchestrated-systems.htm).

Account Profiles in Oracle Access Governance

Feature Description
Account Profiles in Oracle Access Governance Oracle Access Governance simplifies permission management by letting you to define account profiles with supported or custom account attributes and default values. This avoids the need to repeatedly enter the account details required for provisioning in each Access Bundle.

While defining account profiles, you may choose to provide default values or choose to ask the requester to provide values during the self-service request. For Policy-Based Access Control (PBAC), default values are used.

You can associate an account profile to an access bundle to ensure consistent attribute application and easier updates. For more information, see[Account Profiles - Reusable Templates for Access Bundle Generation](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#account-profiles-reusable-templates-for-access-bundle-generation).

Global Key Values in Oracle Access Governance

Feature Description
Global Key Values Global Key Values in Oracle Access Governance is a set of key-value pair`{label,value}`containing keys for identity or account attributes with values — such as project codes with project names, language codes with languages, and so on. This simplifies transformation or account management operations. You can import the defined key-value pairs using a CSV file and use these values across orchestrated systems.

For example, you may import project codes with project names in a CSV file and use the values to derive value in inbound or outbound transformations and use it across your integrations. You can also use this to source value to custom account attributes. For more information, see[Manage Global Key-Values](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-global-key-values.htm).

Account Attributes for Account Management and Transformations in Oracle Access Governance

Feature Description
Account Attributes for Account Management and Transformations in Oracle Access Governance Account Attributes in Oracle Access Governance enables administrators to configure custom account attributes beyond the default account attributes supported for an orchestrated system, providing flexibility over account management operations. You can source values of these additional account attributes from the Managed System, from Global key values reference file, or define it when creating an access bundle.

You can use and configure these attributes for inbound or outbound transformations, or for account provisioning operations, such as account creation. You can also use these account attributes to define the account profile required for provisioning. For example, you can dynamically construct nested attributes containing array of values, such as address, and use it during provisioning access to a user. For more information, see[Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#account-attributes).

Integrate Oracle Access Governance with Arcon Privileged Access Management (Arcon PAM)

Feature Description
Integrate with Arcon Privileged Access Management (Arcon PAM) Arcon Privileged Access Management (Arcon PAM) : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in Arcon Privileged Access Management (Arcon PAM) as a Managed System.

Arcon Privileged Access Management (Arcon PAM) is a comprehensive solution managing privileged access across various IT environments, ensuring that only authorized users can access critical systems.

With this integration, you can centrally manage and monitor privileged accesses, streamline access reviews, enforces security policies across all systems, ensuring compliance with internal and regulatory requirements. For more information, see[Integrate with Arcon PAM](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-arcon-pam.htm).

New Orchestrated System: Database Application Tables (MySQL) and Database Application Tables (MSSQL)

Feature Description
Integrate with Database Application Tables (MySQL) Database Application Tables (MySQL) : Oracle Access Governance now supports on-boarding of identity (user) data, identity orchestration for provisioning and reconciliation of accounts in Database Application Tables (MySQL) as an Authoritative Source and as a Managed System. For more information, see[Integrate with Database Application Tables (MySQL)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-mysql.htm).
Integrate with Database Application Tables (MSSQL) Database Application Tables (MSSQL) : Oracle Access Governance now supports on-boarding of identity (user) data, identity orchestration for provisioning and reconciliation of accounts in Database Application Tables (MSSQL) as an Authoritative Source and as a Managed System. For more information, see[Integrate with Database Application Tables (MSSQL)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-mssql.htm).

ePrescribe, PPR and Taxonomy Attribute Support in Oracle Health EHR (formerly Cerner Millennium) Orchestrated Systems

Feature Description
Extending Support of Default Attributes for Oracle Health EHR (formerly Cerner Millennium) Orchestrated System Oracle Health EHR (formerly Cerner Millennium) Orchestrated System now supports additional default attributes for provisioning and transformation to enable seamless data integration. Oracle Health EHR (formerly Cerner Millennium) Orchestrated system now supports account attributes from the following functionalities :
- ePrescribe
- Taxonomy
- Patient-Provider Relationship (PPR) Clinical Decision Support

For more information, see[Oracle Health EHR (formerly Cerner Millennium) Integration Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-health-ehr-formerly-cerner-millennium-integration-reference.htm).

New Service Helpdesk Administrator role in Oracle Access Governance

Feature Description
New Service Helpdesk Administrator role for Advanced Administration in Oracle Access Governance A new application role AG_ServiceDesk_Admin is introduced in Oracle Access Governance. This role empowers administrators to modify accounts and perform other advanced administrative functions directly in the Oracle Access Governance Console.

Users with role can enable, disable, or delete accounts and can revoke permissions managed by Oracle Access Governance. Furthermore, users with this role can retry provisioning for failed or pending accesses.

For more information, see[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).

Account Lifecycle Management Operations in Oracle Access Governance

Feature Description
Account Lifecycle Management in Oracle Access Governance Oracle Access Governance users with AG_ServiceDesk_Admin role can now directly perform the following operations from the Manage Identities page.
- Suspend all the accounts and accesses for an identity at once, that have not been assigned directly in the Managed System, using the Terminate operation. Based on the account settings configured for your orchestrated system, account may be deleted or disabled. Once terminated, no accounts and associated accesses for that identity can be managed from Oracle Access Governance. You may again re-provision the accounts and the accesses, granted through policies ( Grant Type Policy ), using the Activate button, if required.
- Revoke one or more permissions assigned directly from the Managed System or provisioned through request.
- Retry provisioning of permissions with the Failed or Pending statuses. It is applicable for the permissions provisioned within Oracle Access Governance ( Grant type as Request or Policy )
- Disable or Delete one or multiple accounts managed by Oracle Access Governance. Once disabled all the associated accesses are removed. The accounts are still managed by Oracle Access Governance . You may re-provision the accounts and the accesses using the Enable account operation, if required.

For deleted accounts, all the associated accesses are removed and you can no longer manage the accounts from Oracle Access Governance.

For more information, see[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm).

## December 2024 Update

Publish Initial Data Event of Day-0 to Object Storage OCI Buckets

Feature Description
Event Data Publisher Event Data Publisher is now enhanced to export the initial data event (Day 0) to OCI Buckets irrespective of file size. The publishing status for the Day 0 export is sent as stream messages to OCI Streams. The incremental ongoing data events (Day N) will still be published based on file size, either to OCI Buckets or OCI Streams.

Orchestrated Systems

Feature Description
New Orchestrated System: Integrate with SAP Ariba SAP Ariba : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in SAP Ariba as a Managed System.

SAP Ariba is a comprehensive cloud-based procurement and spend management service that helps businesses streamline and optimize their procurement processes, from sourcing to payment. With this integration, you can create, update, enable, and disable identity accounts. You can manage group assignment for identities using Access Bundles from Oracle Access Governance. For more details, see[Integrate with SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-sap-ariba.htm).
New Orchestrated System: Integrate with SAP S/4HANA SAP S/4HANA : Oracle Access Governance now supports identity orchestration for provisioning and reconciliation of accounts in SAP S/4HANA as a Managed System.

SAP S/4HANA is an Enterprise resource planning (ERP) platform built to help businesses run real-time analytics and simplify complex business processes such as order-to-cash, procure-to-pay, plan-to-product, and request-to-service. With this integration, you can enable and disable identity accounts. You can manage role assignment for identities using Access Bundles from Oracle Access Governance. You can also update account by locking or unlocking identity accounts.

## November 2024 Update

Preventive Segregation of Duties (SOD) Analysis using Oracle Fusion Cloud Risk Management and Compliance (RMC)

Feature Description
Segregation of Duties (SOD) Analysis for Oracle Fusion Cloud Applications Oracle Access Governance now supports preventive SOD checks through Oracle Fusion Cloud Risk Management and Compliance (RMC). With this update, Oracle Access Governance raises potential conflicts as part of access request approval task. Currently, the SOD violations check is scoped for Oracle Access Governance Access Bundles. For more details, see[Manage Approvals](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approvals.htm).

Access Controls: Manage Assignment of OCI Cloud Services Application Roles

Feature Description
Assign users to OCI cloud service application roles from Oracle Access Governance You can now assign OCI cloud services application roles to identities with Oracle Access Governance. For this, package one or more OCI cloud services application roles in an access bundle, and assign it to users through a policy or an access request. You may further run identity access reviews for these assignments, if these are granted through user request. For more details, see[Create an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-overview).

Identity Access Reviews for OCI Permissions managed by Oracle Access Governance

Feature Description
Run Identity Access Reviews for OCI Permissions managed by Oracle Access Governance For assignments managed by Oracle Access Governance, you can certify identities assigned to OCI IAM groups and OCI cloud services application roles as part of OCI Access Bundles reviews (Grant Type as`REQUEST`). For more details, see[Review Accesses to Cloud Services Managed by Oracle Cloud Infrastructure (OCI)](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-oracle-cloud-infrastructure).

Event-Driven Incremental (Day-N) Data Load for Oracle Identity Governance (OIG) Orchestrated System

Feature Description
Event-Driven Incremental Data Load for OIG Oracle Access Governance now supports both event-driven and periodic snapshot-based incremental data load for OIG Orchestrated System. For event-driven data load, you can enable a new option, Do you want to enable OIG database incremental data load? , to load data automatically based on occurrence of specific system events or changelog, ensuring real-time updates. To enable this feature, the database user must be granted required privileges.

Data Load Settings for Orchestrated Systems

Feature Description
Data Load Settings for Orchestrated Systems You can now set how often data should be loaded and updated between Oracle Access Governance and orchestrated systems. You can configure the timing and frequency for all orchestrated system except for Flat File and Oracle Cloud Infrastructure (OCI IAM). For more details, see[Configure Data Load Schedule Settings for Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-data-load-settings-for-orchestrated-systems).

## September/October 2024 Update

Event Data Publisher in Oracle Access Governance

Feature Description
Event Data Publisher in Oracle Access Governance With Oracle Access Governance, you have the flexibility to export and continually publish data events to your cloud tenancy. You can export one-time and sequentially and continually publish ongoing data events to OCI Buckets or OCI Streams depending on the file size. See[Understanding Data Event Publishing Flow](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-feed.htm#understanding-data-event-publishing-flow).

Orchestrated Systems

Feature Description
Database Application Tables and Oracle Database User Management
- Oracle Access Governance now supports the following:
- Oracle Autonomous AI Database
- Oracle Database 23ai, 19c, 18c or 12c as a single database, pluggable database (PDB), or Oracle RAC implementation
- Oracle Access Governance now supports wallet-based authentication, in addition to basic authentication. To enable this, download the autonomous database wallet to your agent host, and then configure the Easy Connect URL for Database field in the orchestrated system. For more details, see[Configure Wallet for Autonomous AI Database Integration](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-oracle.htm#db-table-oracle-postconfig).
New Orchestrated System: Integrate with Oracle Health EHR (formerly Cerner Millennium) Oracle Health EHR (formerly Cerner Millennium) : You can enable identity orchestration for provisioning of accounts in Oracle Health EHR (formerly Cerner Millennium) as a Managed System. See[Oracle Health EHR ( formerly Cerner Millennium ) Integration Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-health-ehr-formerly-cerner-millennium-integration-reference.htm).

Delegations

Feature Description
Delegations
- Oracle Access Governance Administrator (`AG_Administrator`) can now manage delegations on behalf of Oracle Access Governance users. User Managers user can now update delegations for users they manage directly.
- To manage delegation settings, you can access delegations from multiple paths within the Oracle Access Governance Console.

See[Manage Delegation Preferences](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-delegation-preferences.htm).

Microsoft Entra ID Group Management

Feature Description
Microsoft Entra ID Group Management You can now manage group for Microsoft Entra ID. Oracle Access Governance supports provisioning of Security Group and Office Group using the Identity Collections functionality.

## August 2024 Update

New Application Roles in Oracle Access Governance

Feature Description
New Application Roles related to Orchestrated System New Application Owner Roles introduced for Orchestrated System:
- `AG_AppOwner_Admin`: Can create, manage, and configure all the integrations as part of Orchestrated systems. See[Application Owner Administrator](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-appowner).
- `AG_AppOwner_Admin_Restricted`: Can create new integrations with other systems by adding an Orchestrated system but manage and configure the integrations or resources that they own, as a resource owner. See[Application Owner Restricted Administrator](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-restrictedappowner).

See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference)listing all application roles.
New Application Roles related to Access Controls New Access Control Restricted Administrator Role introduced for Access Controls:
- `AG_AccessControl_Admin_Restricted`: Can create all the resources included in the Access Control module, such as Roles, Identity Collections, Policies, Approval Workflows, Access Bundles, and Organizations. However, they can manage only the integrations or resources that they own, as a resource owner. See[Access Control Restricted Administrator](https://docs.oracle.com/en-us/iaas/Content/access-governance/about-application-roles.htm#approle-accesscontrolrestrictedadmin).

See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference)listing all application roles.

Run Ownership Reviews and Identity Access Reviews based on Direct Permissions

Feature Description
Ownership Reviews You can schedule campaigns to review ownership of resources that are created within Oracle Access Governance, either periodically or on an ad hoc basis. By performing this review, you can ensure accountability of resources lies only with the designated owners. See[Resource Ownership](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#resourceownership).
Run Identity Access Reviews for directly assigned permissions You can now quickly certify privileges for all Orchestrated systems based on the permissions ingested directly (`DIRECT`) from a Managed System without provisioning it first from Oracle Access Governance. See[Identity Access Reviews based on Permissions Assigned Directly in Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#identity-access-reviews-for-reconciled-permissions).

Add Resource Owners

Feature Description
Add Primary and Additional Owners for Orchestrated Systems, Access Control Resources, and Organizations You can now add primary and additional owners for Oracle Access Governance resources. Any Oracle Access Governance active identity can be assigned as the resource owner. All the owners can read, update, or delete the resources that they own. See[Add Primary and Additional Owners](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#add-primary-additional-owners).

Orchestrated Systems

Feature Description
New Orchestrated System: Integrate with Oracle Fusion Cloud Applications Oracle Fusion Cloud Applications : You can enable identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts for Oracle Human Capital (HCM) and Oracle Enterprise Resource Planning (ERP) accounts. This includes using Oracle Fusion Cloud Applications as an Authoritative source and as a Managed System for account provisioning. See[Integrate with Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm).
New Orchestrated System: Integrate with Database Application Tables Database Application Tables : You can enable identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts for Database Application Tables both as an Authoritative source and as a Managed System. See[Integrate with Database Application Tables (Oracle)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables.htm).
Configure Account Settings You can now configure the account settings to support the Joiners, Movers, and Leavers process for your Orchestrated system. You can configure to send email to user or user manager when a new account is created. You can also choose to either disable or delete the account whenever an identity moves within or leaves your enterprise.

Access Controls

Feature Description
Provisioning Users to OCI IAM groups from Oracle Access Governance You can now provision users to OCI IAM groups from Oracle Access Governance. You can package multiple OCI IAM groups in an access bundle, and provision it to users through a policy or an access request.
Identity Lifecycle - Joiners, Movers, Leavers Process New article describing automated provisioning for Joiners, Movers, and Leavers (JML) process in Oracle Access Governance. See[Identity Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/access-governance/jml-process.htm).

New Articles for My Access and Language Support

Feature Description
Self-Service - My Access New article on viewing your access details and managing your accounts in Oracle Access Governance. See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm).
Language Support in Oracle Access Governance New article that lists various languages supported by Oracle Access Governance Console and steps to update your browser's locale settings. See[Supported Languages in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/supported-languages-in-oracle-access-governance.htm).

## July 2024 Update

Access Reviews

Feature Description
Access Reviews Fallback Mechanism New fallback process is introduced to assign a valid reviewer or a campaign owner whenever an invalid reviewer or an invalid campaign owner is detected. This will prevent sudden termination of a campaign.
New or Updated Access Reviews Articles New or updated articles for Access Reviews:
- Access Reviews in Oracle Access Governance - Certify Access Privileges with Campaigns and Event-Driven Micro Certifications
- Working with Access Review Campaigns
- Create Identity Access Review Campaigns
- Create Policy Review Campaigns
- Create Identity Collection Review Campaigns
- Manage and Monitor Access Review Campaigns
- Micro-Certifications: Event Driven Access Reviews
- Configure and Manage Event-based Access Reviews
- Understanding Reviewer's Actions for Effective Access Reviews
- Perform Access Reviews - Evaluate and Certify Access Review Tasks

## June 2024 Update

Orchestrated Systems

Feature Description
Integrate with Orchestrated Systems PeopleSoft : You can now perform identity reconciliation, user management, and role assignment with PeopleSoft integration.

## May 2024 Update

Who Has Access to What

Feature Description
Who Has Access to What Enterprise-wide Browser
As an Enterprise-wide Access Administrator or Administrator , get a comprehensive and centralized view of access information across your enterprise. Enterprise-wide Browser allows you to:
- Browse through access information using various perspective views, such as identities, identity collections, roles, permissions, policies, resources, and organizations.
- Use search capabilities and advanced filters to optimize your search query and locate specific access information.
- Customize the default access profile layout by hiding or showing columns or reordering columns for a better user experience.
- Run user-created identity and access control reviews and view the access review report.
- Download the CSV file for the first 500 records available in the access profile view or download the PDF screenshot of the access detail.
Who Has Access to What My Access

As an Oracle Access Governance user, you can view access profile details in the self service section. Go to My Stuff → My Access to view your access details. The account details visible on the My Accounts page is now available on the My Access → Accounts page.

Notifications

Feature Description
Notifications The following enhancements have been added to notifications:
- Notification delivery service: The ability to define an alternative to the default Oracle Access Governance notification email delivery service has been added. You can now configure an OCI email delivery service as an alternative. Refer to[Configure an OCI Email Delivery Service for Notifications](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm)for details.
- Recipient for Orchestrated System related notifications: You can now define an identity or email to act as the recipient for notifications relating to Orchestrated System operations. See[Configure Identity/Email For Orchestrated System Related Notifications](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-identityemail-for-orchestrated-system-related-notifications)for details.

OCI Data Handling

Feature Description
OCI Data Handling The Identity Attributes functionality has been enhanced to provide the ability to define which OCI domain Oracle Access Governance should use as the source of truth when ingesting identity data from a multi-domain OCI instance.

Integrations

Feature Description
System Integration PeopleSoft : You can now perform identity reconciliation, user management, and role assignment with PeopleSoft integration.
Integrations Updated[Data Transformation](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#data-transformation)topic within the Integration documentation.

## March/April 2024 Update

Orchestrated Systems

Feature Description
Integrate with Orchestrated Systems
- EntraID: Configuration has been updated to allow for certificate-based authentication, in addition to existing client secret authentication.
- Oracle Identity Governance: Configuration of the OIG Orchestrated System now includes data filters to limit the data transported and ingested from Oracle Identity Governance.
Integrate with Orchestrated Systems Integration documentation for the following managed systems has been updated:
- Oracle Identity Governance Agent: Additional prerequisites added. Troubleshooting section added.

Integration

Feature Description
New/Updated Integration Articles New/updated articles for integration:
- Identity Orchestration Overview
- Identity Orchestration Components
- Identity Orchestration Process Flow
- Manage Oracle Access Governance Agent for Indirect Integrations
- Manage Integrations with Orchestrated System
- Configure Settings for an Orchestrated System
- Supported Integrations with Oracle Access Governance
- Data Rules to Customize and Transform Identity and Account Attributes
Integration Landing Page Integration landing page has been updated:
- The[Integration landing page](https://docs.oracle.com/en/cloud/paas/access-governance/integrate.html)has been redesigned to include new integration articles, and to provide a drop down list for each specific integrations which, when selected, will display all relevant content relating to the chosen integration system.

## February 2024 Update

Orchestrated Systems

Feature Description
Integrate with Orchestrated Systems You can now integrate Oracle Access Governance with:
- Generic REST : You can perform user management and teams group assignment tasks via Oracle Access Governance.
- Oracle Siebel : You can perform user management and role grant management operations via Oracle Access Governance.

Unmatched Accounts

Feature Description
Delete Unmatched Accounts You now have the option to delete accounts which are unmatched from a Managed System. This is in addition to the current functionality allowing you to match an unmatched account to an identity.

Configurable Notifications

Feature Description
Configurable Notifications You can now customize and configure notifications. Notifications are sent for different types of event. You can now customize notifications in the following ways:
- Set the default logo
- Set the default language in which notifications are sent
- Enable notification type
- Disable notification type
- Set Subject for the notification email
- Set content for the notification email body

Data Transformation and Matching Rules

Feature Description
Identity Attributes For custom identity attributes, you now have the option to add a rule on how the attribute is populated. You can either use the value directly, or you can create a rule around the active value.

## January 2024 Update

Orchestrated Systems

Feature Description
Integrate with Orchestrated Systems You can now integrate Oracle Access Governance with:
- Microsoft Teams: You can perform user management and teams group assignment tasks via Oracle Access Governance.
- Oracle Primavera: You can perform user management and role grant management operations via Oracle Access Governance.

Data Transformation and Matching Rules

Feature Description
Outbound and Inbound Data Transformation You can transform the data coming into Oracle Access Governance or going out (provisioned) of Oracle Access Governance. You can apply transformation rules on the inbound and the outbound data, by writing methods in JavaScript, for objects, identity (user) object, account object, and custom user attributes.
Matching Rules You can now use matching or correlation rules to avoid orphan or unmatched accounts during the data ingestion process. You can set up these rules to match the identity data imported from different authoritative sources, and/or match multiple accounts with an identity to avoid unmatched account.

## December 2023 Update

Orchestrated Systems

Feature Description
Integrate with Orchestrated Systems You can now integrate Oracle Access Governance with Oracle Fusion Cloud Applications. With this integration, you can perform User management and Role grant management operations through Oracle Access Governance.

Outbound Data Transformations

Feature Description
Outbound Data Transformation Through Oracle Access Governance, you can now perform data transformation on the data provisioned into the Orchestrated system account.

Identity Collection can manage a new or existing Active Directory group on a Orchestrated System

Feature Description
Identity Collection can manage a new or existing Active Directory group on a Orchestrated System While creating an identity collection in Oracle Access Governance, you can now opt to manage a group on a Orchestrated system. The selected (new or existing) group in this Orchestrated system will be managed by this identity collection.

Reassignment of Identity and Access Reviews

Feature Description
Reassign Identity and Access Reviews Oracle Access Governance gives you the provision to reassign identity reviews and/or access review items to other users. In reassignment, the review tasks will be moved from the original reviewer and gets assigned to the new reviewer.

Access Governance Organization

Feature Description
Oracle Access Governance Organizations Oracle Access Governance administrators can now structure identities and form relationships between identities by creating and managing Organizations in the Oracle Access Governance Console.

Approval Workflows in the Event-Based Access Reviews

Feature Description
Approval Workflows in the Event-based Access Reviews You can now configure approval workflows for all the three event types - change event, timeline event and multi-event access reviews.

Unmatched Accounts Access Reviews

Feature Description
Unmatched Accounts Access Reviews You can now review unmatched accounts via event-based access reviews. This allows application owners and custom users to match an unmatched account to an existing Oracle Access Governance identity, or remove the account from the Orchestrated system.

Enhancement in Reporting of Campaign Details

Feature Description
Campaign Details' Report Enhancement In the campaign details page, for approval workflow summary, you can see count of total and pending reviews. A new link, View pending link , has been added that provides reviewer details, such as reviewer's name, email addresses, and count of pending reviews with each of them.

## November 2023 Update

Orchestrated Systems

Feature Description
Orchestrated Systems The following types of Orchestrated System have been added to Oracle Access Governance:
- Eloqua
- NetSuite
- Microsoft SQL Server
- Microsoft Entra ID (formerly Microsoft Azure Active Directory
- Flat File
Unmatched Accounts The ability to manage unmatched accounts has been added. You can search for unmatched accounts, and where appropriate, match them to an Oracle Access Governance identity.
OCI Group Membership Review OCI IAM group memberships can now be reviewed as part of Identity Collection access reviews.
Timeline Event Based Micro-certification Timeline based micro-certification to trigger user access reviews based on specific dates, such as anniversary dates, has been added to the Event-Based Access Review functionality.
Active Directory group management AD groups can now be managed from Oracle Access Governance using the Identity Collections functionality.

## September 2023 Update

Time-based Events

Feature Description
Time-based Events Time-based Events refer to an event which is raised for a particular date, for example, weekly, monthly, or when a user is granted access to an application on a given date, which is subject to an annual review. A review task is generated for the user on the date configured for the time-based event, to determine if the permission associated with the event is still appropriate

## July 2023 Update

List Requests that needs Approvals

Feature Description
Approvals

The Approvals page in the Oracle Access Governance console, lists access requests requiring your attention. All requests requiring approval will be displayed. These requests are listed as one access per row. If a request is made for multiple accesses, for example access to a database, a directory, and a cloud service, then this will be displayed as 3 rows requiring separate approvals in your approval list.

Viewing Access Requests

Feature Description
View My Requests

The My Access Requests screen, in the Oracle Access Governance console displays a list of access request raised by the logged-in user for Self or for others. You can either view the details, cancel a request or can provide information on the requests.

Request Access for Yourself or for Other Users

Feature Description
Request Access

As an Oracle Access Governance user you can request access to resources and roles. Requests can be made for yourself, or for others. This process creates an access request which is subject to an approval workflow.

Simplifying Process of Requesting Resource Permission

Feature Description
Create and Manage Access Bundle

An Access Bundle is a collection of permissions that packages access to resources, application features, and functionality into a requestable unit.

To access a particular resource, you do not have to request each permission associated with that resource individually, instead you request an access bundle containing all permissions associated with that resource. This simplifies the process of requesting resource permissions.

Using Oracle Access Governance console, you can now create a new access bundle and manage it.

Maintain Policies within your Oracle Access Governance Service

Feature Description
Manage Polices

Using policies you can now provide access to resources within your organization. These policies associate resources and permissions with identities by means of roles and access bundles. You can create and manage policies by using Oracle Access Governance Console.

Manage Roles

Feature Description
Manage Roles

You can now create and manage roles using Oracle Access Governance console. These roles are a group of access bundles. The access bundles contained within a role can span multiple targets. For example, a Database Administrator role groups together the DBAdmin_Oracle, DBAdmin_DB2, and DBAdmin_MySQL access bundles. To use a role you must associate identities to it via a policy.

Create and Manage Approval Workflow

Feature Description
Create and Manage Approval Workflow

In Oracle Access Governance, every permission, access request, or role that needs to be assigned to a user must be processed through an approval workflow. You as a resource administrator can design an approval workflow by specifying the required approval level and the number of approvers.

Later, as a Permission Manager you can use these workflows to obtain approvals before assigning or revoking user privileges.

You as a resource administrator can monitor and manage the approvals using the Oracle Access Governance Console.

Integrate Oracle Access Governance with Target Systems

Feature Description
Integrate with Orchestrated Systems
You can now connect Oracle Access Governance with the following systems by entering connection details and credentials for the target system.
- Active Directory
- Oracle e-Business User Management (UM)
- Oracle e-Business Employee Reconciliation (HRMS)
- Database User Management (Oracle)
- Oracle Unified Directory
- Oracle Internet Directory
- Database User Management (MySQL)
- Database User Management (DB2)

## May 2023 Update

New License Types for Oracle Access Governance

Feature Description
New License Types Oracle Access Governance rolls out new license types for its users:
- Access Governance for Oracle Cloud Infrastructure
- Access Governance for Oracle Workloads

Added Identity Activation Rules for License Management in Oracle Access Governance

Feature Description
Manage Identities You can now optimize Oracle Access Governance instance operating cost by managing which identities can use the Oracle Access Governance service. Identities excluded from the service will not have access to Oracle Access Governance functionality and will not be billed.

Identity Orchestration: Integrate Oracle Access Governance with Oracle Cloud Infrastructure Identity and Access Management (OCI IAM)

Feature Description
Integrate with OCI IAM You can now implement code-less integration of Oracle Access Governance directly with cloud services. This release supports Identity Orchestration set up between Oracle Access Governance and Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) system.

Policy Reviews

Feature Description
Policy Reviews You can review OCI IAM policies either one-time or periodically from Oracle Access Governance by creating Policy Review campaigns. In this campaign, access control of each cloud resource is evaluated up to the policy statement-level. The policy statements can either be accepted or revoked.

Who Has Access to What: Enterprise-wide Access and Individual's Access to Cloud Resources

Feature Description
Who Has Access to What The Who Has Access to What capability now includes:
- Ability to see individual's access to cloud resources. On the My Access page, you can now select a specific option from the Group by drop-down to view access to cloud resources assigned to you.
- 360-degree visibility into organization's cloud resources, identities who can access these resources, and assigned permissions. Here, you can view a comprehensive list of all resources across various systems or cloud tenancies Orchestrated with Oracle Access Governance.

New Capability that supports Custom Identity Attributes in Oracle Access Governance

Feature Description
Custom Identity Attributes. Oracle Access Governance now supports custom identity attributes in addition to core identity attributes for running various Oracle Access Governance operations.

Introduced Identity Collections functionality in Oracle Access Governance

Feature Description
Identity Collection You can now create and manage a collection of identities to perform Oracle Access Governance functions collectively on a group rather than performing for each individual identity. You can create an identity collection either by defining conditional rules, known as Membership Rules, and/or by directly selecting identity names.

Added Capability to Delegate your Access Review Tasks to an Identity or an Identity Collection

Feature Description
Delegation Oracle Access Governance now provides the capability to delegate your tasks by setting up your preferences. In this release, from the My Preferences screen, you can delegate your access review tasks to an identity or to an identity collection.
Note  
  
For this release, you must upgrade your current Oracle Access Governance agent to enable code-less integration with the systems. Refer[Agent Example Usage](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#agent-example-usage)to enable the auto-upgrade flag and upgrade your agent with the latest updates.

## February 2023 Update

New Available Region in Central UAE: Abu Dhabi

Feature Description
Available in UAE Central: Abu Dhabi Oracle Access Governance rolls out its services and is now available in the UAE Central Abu Dhabi region.

New Enterprise-wide Access functionality in Who Has Access to What

Feature Description
Who Has Access to What The Who Has Access to What capability now includes 360-degree visibility into organization resources, resource types, identities who can access these resources, and assigned permissions. Here, you can view a comprehensive list of all resources across various Orchestrated with Oracle Access Governance.

Auto Upgrade Feature for Oracle Access Governance Agent in Orchestrated Systems

Feature Description
New Auto Upgrade Flag for Oracle Access Governance Agent in Orchestrated Systems . You can now automatically install updates for the Oracle Access Governance Agent by enabling the autoupgrade flag during the configuration process. Through this flag, a scheduled task is run every 24 hours that checks and/or installs any updates available for the Oracle Access Governance agent. This is a crucial step and you must set this to prevent any issues in communication from the agent to the Access Governance Service. Refer[Agent Example Usage](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#agent-example-usage)to enable the auto-upgrade flag.

## October 2022 Update

## What's New in the October 2022 Update

Event-based Access Reviews

Feature Description
Event-based Access Reviews You can now launch event-based access reviews from Oracle Access Governance that initiate whenever a change is detected in a user lifecycle state or a user attribute, such as onboarding of new users, department change, job-code change, location change, retirement or exit of users, or manager change. Once configured, these are automatically triggered when one or more predefined event types occur.

Access Review Scheduler

Feature Description
Access Review Scheduler You can now schedule and run the Access Review Campaigns periodically which can be Monthly, Quarterly, Half-Yearly, or Yearly.

## June 2022 Update

On-Demand Access Reviews

Feature Description
On-Demand Access Reviews You can launch on-demand Access Review Campaigns to review user access assignments where individual access to a specific source is checked and either certified or remediated.

Who Has Access to What

Feature Description
Who Has Access to What You can use the Who Has Access to What functionality as a user or a user manager to see the number of applications, permissions, and roles assigned to you (self) or to your direct reports.

Identity Orchestration in Oracle Access Governance

Feature Description
