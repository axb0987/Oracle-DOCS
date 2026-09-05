# Key Features
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/key-features.htm
- Fetched: 2026-09-05 03:15 CDT

# Key Features

Key features of Oracle Access Governance include the following:

## Access Reviews

Process to evaluate and certify the access privileges granted to identities within an enterprise. It checks and certifies if privileges granted are still required and align with the current job at work. With Access Reviews, you can make swift and accurate review decisions by examining insights and AI-powered recommendations based on prescriptive analytics.

Key Functions
- Multiple types of campaigns to support periodic or ad-hoc reviews
- Configurable self-certification capability to allow self-reviews.
- Intelligent fall-back mechanism to avoid sudden termination of campaigns. It auto-assign the next applicable reviewer or campaign owner.
- Automated micro-certifications, triggered only when there are changes in the system of record, occurrence of an important date or time milestone, or detection of an orphan account.
- Review Identity, Access Control, and Ownership review tasks.
- Delegate or Reassign review tasks to other reviewer.

## Access Review Campaigns

Periodic or ad hoc snapshot-based reviews, capturing all the relevant access information at a given point of time, and then assessing and generating access review tasks. It improves certification efficiency by providing actionable insights based on prescriptive analytics.
Key Functions
- Certify identity accesses and assigned privileges across all orchestrated systems connected with Oracle Access Governance.
- Certify membership in a group to verify if only eligible set of members are assigned to a group. This is commonly known as "Group membership reviews."
- Verify the principle of least-privilege by reviewing policy and policy constructs with policy reviews.
- Review accountability of resources by running resource ownership reviews.

## Access Controls

Permission management and administration feature that governs how resource access is granted to identities across your enterprise or organization. With Oracle Access Governance, you can leverage the Attribute-Based Access Control (ABAC), grant access to role Role-Based Access Control (RBAC), or Policy-Based Access Control (PBAC) permission models.
Key Functions
- Role-based access control (RBAC) : Assign permissions to users associated with their job profile or functions.
- Attribute-based access control (ABAC) : Assign membership to identity collections based on core or custom identity attributes
- Policy-based access control (PBAC) : Assign permissions to users by defining a policy.
- Request access to roles or access bundles directly via self-service module, and processed only after approval.

## Approval Workflows

Code-less workflow templates to obtain approvals for tasks in Oracle Access Governance. You can choose out-of-the-box or build your own sequential or parallel workflow paths.

- Involves code-less workflow creation.
- Intelligent fall-back mechanism to avoid sudden termination of tasks.
- Sends notification emails about assigned and pending access reviews.
- Supports complex multistage approvals through sequential or parallel workflows to meet your business needs.
- Reviewer can make decisions to accept, revoke, or reassign items in access reviews or request approval task.
- Get suggestions for the intelligent workflow based on selected criteria.

## Centralized Enterpise-wide Visibility into Access Profiles

With Enterprise-wide Browser, you gain insights into access usage to detect and prevent any potential misuse. With Enterprise-wide Browser, you get comprehensive visibility on all the components, access information, and resources within an enterprise framework.
Key Functions
- Centralized dashboard with multiple browsing views to view access information. The access is presented across multiple anchoring points:
- Identities : Understand who has access to what.
- Identity collections : Group identities logically.
- Organizations : View access within specific organizational units.
- Roles : Explore role-based access.
- Policies : Understand access policies.
- Permissions : View details of specific permissions.
- Applications and resources : Identify which applications and resources are accessed.
- Advanced search capabilities, including keyword search, suggested filters, and advanced filters to get specific and relevant results.
- Generate monthly access review report based on the date range and access review Enterprise-wide Browser. You can see breakdown of pending, approved, or revoked access review decisions for user role, user account and permission.
- Generate spontaneous user-created access reviews for a resource within Enterprise-wide Browser.

## Correlation

Correlation or Matching Rules allows you to configure a set of rules to match and associate ingested identity or account to an existing identity. With this, you can leverage identity matching and account matching to build a composite identity profile. These are beneficial to automatically associate multiple accounts incoming from Managed systems with identities and avoid accumulation of unmatched accounts.
Key Functions
- Configure rules for Identity-Identity Matching for Authoritative Sources
- Configure rules for Identity-Account Matching for Managed Systems and Authoritative Sources
- Match an unmatched account with an existing identity, manually.

## Data Transformation

Data Transformation feature in Oracle Access Governance allows you to modify and transform incoming identity and account data from Authoritative Source or Managed Systems, or transform outgoing data being provisioned to Managed Systems.
Key Functions
- Inbound Transformation for Identity Attributes
- Inbound Transformation on Account Attributes
- Outbound Transformation on Account Attributes using Identity Attributes
- Composite Identity Profile Transformation within Oracle Access Governance

## Event Data Publishing

Export and continually publish data events in real-time to external systems using the Data Feed service. Data Feed publishes real-time updates as a continuous stream in a sequential order.
Key Functions
- Publishes real-time updates as a continuous stream in a sequential order to OCI Streams.
- Publishes the following data components to external systems:
- All the active identities, workforce, or consumers are published as IDENTITY events to OCI Buckets and OCI streams.
- All the available OCI IAM group ingested into Oracle Access Governance will be published as GROUP events.
- All the available OCI policies ingested into Oracle Access Governance will be published as TARGET_ACCESS_POLICY_STATEMENT events.
- All available resources across all orchestrated systems ingested into Oracle Access Governance will be published as RESOURCE events.
- Access mapping for OCI policies and OCI resources.

## Identity Intelligence

Oracle Access Governance analyzes each identity and its privileges, builds insights into potential high-risk assignment and security violations, and recommends remediations. This enables access reviewers to make corrective decisions quickly. This feature enables:

- Assimilation and analysis of identity data and access privileges.
- Recognition of contextual insights and identification of security blind spots.
- Remediation recommendations enable access reviewers to make corrective decisions quickly.

## Identity Orchestration

Oracle Access Governance brings together diverse Authoritative Sources and Managed Systems by supporting low-code integrations. It facilitates data transformations and correlation rules which ensures data coherence. It extracts the required identity data from various systems into Oracle Access Governance and enables businesses to perform robust access control, intelligent access reviews, and perform fulfillment through account provisioning.

Key Functions
- Specialized and generic low-code integration with various on-premises systems and cloud applications and systems.
- Extract only the required information, such as identity attributes, permission assignments, and policies, into Oracle Access Governance.
- Support transformation and correlation rules for identity and account attributes, to build composite identity profile and account information.
- Process the identity data and using it for access controls, access reviews, workflows, and so on.
- Provision and synchronize data between the orchestrated systems to support Identity Lifecycle.

## Identity Orchestration with JML Support

Oracle Access Governance supports creation, modification, and deletion of identity accounts and their access permissions based on attribute change in the integrated Orchestrated system. You can configure access controls to automatically provision and de-provision accounts as part of the Identity Lifecycle Management. It supports all the three stages – Joiners, Movers, and Leavers (JML).
Key Functions
- Account Creation : Provisioning of new accounts whenever a new user is detected. The provisioning is completed based on access request, roles, or defined policies.
- Account Modification : Automated modification of account attributes when identity attributes are updated in the authoritative source and synchronized. Oracle Access Governance assigns new permissions and revoke or disable unessential permissions associated with the account.
- Account Deletion: Permanently delete accounts when no longer required, such as when employee leaves the organization.

## Micro-Certifications: Event-Based and Time-Driven Access Reviews

Event-Based Reviews are the action-oriented reviews carried out by Oracle Access Governance whenever an event, such as change event, timeline event, or unmatched account event, is detected. These generate near real-time access reviews so that prompt actions can be taken whenever these pre-defined events are detected.
Key Functions
- Launch change event type review based on update in core and custom identity attributes.
- Launch time-driven access reviews annually on a given date.
- Configure set up to trigger unmatched account event to detect orphan account.
- Define auto-actions for low-risk access reviews or unmatched accounts.
- Generate insights on event-based access reviews.

## Reporting and Analytics

Oracle Access Governance enables reporting and analytics by providing various out-of-the-box summary reports and insights.
Key Functions
- 360-degree visibility into identities, accounts, policies, roles, resources and permissions in an intuitive dashboard.
- Discover, determine risk, and monitor accounts with privileged access for anomalous behavior.
- Monthly report on access reviews based on the date range and access review type or event type

## Self Service

Oracle Access Governance empower users to independently request or complete routine tasks without the administrative intervention.
Key Functions
- Request access to roles or access bundles created within Oracle Access Governance
- Change account passwords for Managed Systems
- Review or approve user access permissions
- Delegate access request or access review tasks to other users.
- View your own accesses, containing details on granted roles, permissions, accounts, ownership, resources, and so on.

## User Interface
