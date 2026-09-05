# Oracle Access Governance Glossary
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/glossary.htm
- Fetched: 2026-09-05 03:14 CDT

# Oracle Access Governance Glossary

Look up product terminology.

## A

  
Access Bundle  
A collection of permissions associated with an application or service. Access Bundles are used to assign permissions to identities through a policy or by request.

  
Access Control  
A mechanism to govern (approve or revoke) access privileges, such as permissions, accounts and role membership assigned to users, or access controls that grant access.

  
Access Guardrails  
Access Guardrails in Oracle Access Governance are security constraints that allow you to define and enforce conditions to regulate and restrict access to sensitive resources. Access Guardrails ensure only authorized identities meeting predefined criteria can gain access. If these conditions are not met, a violation is triggered, allowing you to either block access immediately or provide a grace period for compliance.

  
Access Profile (My Access)  
All access information associated with an identity, including their accounts, set of permissions, and role memberships, representing the logical level of access over applications, service and/or resource.

  
Access Review campaigns  
The mechanism to govern (approve or revoke) the access privileges such as permissions, accounts and role membership assigned to users, and also govern the access privileges associated with OCI IAM Policies.

  
Account  
A representation created in Managed Systems that may include access permissions for resources in the Managed system. Account attributes can be account name, description, status and so on. Accounts could be associated with an Identity either through provisioning process or through discovery process. Any unassociated account would be marked as an Unmatched account that could be a rogue account or a valid orphaned account.

  
Account Profiles  
In Oracle Access Governance, Account Profiles serve as reusable templates that streamline and standardize the creation of user accounts across managed systems. By predefining and storing default values for account attributes, they minimize manual input and simplify the provisioning process. This eliminates the need to repeatedly enter account details for each access bundle. An account profile can be linked to multiple access bundles, as it is not specific to any single one.

  
Attributes  
The data elements that store information related to an object such as Identity, Role, and Permission. For example, the attributes for an identity are first name, last name, department, manager, cost center, position, and email address.

  
Authoritative Source  
A repository or system that contains identity information and is considered to be the primary or most reliable source for this information. For example, HR system (such as Fusion Apps HCM, Oracle EBS, PeopleSoft) for user attributes such as employee's first name, last name, department, manager, cost center, position, and email address.

  
Audit Event  
Audit Events record operational activities happening in Oracle Access Governance. Audit Events focus on security and compliance. These events essentially track user actions, containing details of who did what, and when in the system. All the CRUD operations happening within Oracle Access Governance are recorded and published as Audit Events in near real-time to OCI Streams. For example, for an access bundle creation, audit event record details like Who created the bundle?  
What permissions are included? , Who can request access? , and access bundle details.

## C

  
Campaign Selection Criteria  
The set of rules that defines the scope of an access review campaign.

  
Campaign Owner  
A user in Oracle Access Governance that has special permissions to manage the access review campaigns they own. Campaign owner is defined while creating an access review campaign.  

  
Correlation  
The process to determine whether an ingested account or an identity belongs to the existing identity to build a composite identity profile.

  
Consumer User  
An identity who is either an individual, such as customers, alumni, and outsourced partners, or as a service identity, such as devices which are configured not to access the Access Governance service during the billing period, regardless of whether the individual or service is actively accessing the hosted service at any given time.

## D

  
De-provisioniong  
The process of removing user access to an application, service, software system, or hardware. This process happens automatically when access permissions are revoked during an access review campaign, or when a role membership or permission is revoked through an access policy in Oracle Access Governance.

  
Delegations  
Temporary transfer of responsibility for completing a task, such as performing access reviews, or approving request) to another Oracle Access Governance active user. The original assignee still retains the ownership.

  
Data Feed  
Data Feed is an Oracle Access Governance service used to send data events to an external system. A data event can be an update related to Oracle Access Governance data components, such as creation of new account, modification in resources, or alteration to policy. Data Feed publishes real-time updates as a continuous stream in a sequential order.

  
Diagnostic Service Logs  
Diagnostic Service Logs record service failures and errors, including additional details for troubleshooting. It uses the OCI Logging service to publish logs detailing why and how an event failure happened in the system for debugging. For example, when the campaign creation displays the System Ended status, it publishes the error message with its failure details.

  
Downstream Systems  
See[Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/glossary.htm#glossary-m).

## E

  
Event-based access reviews  
Continuous access reviews that are triggered when user attributes such as organization, department, manager, location, are updated.

  
Event Data Publishing  
Process to export and continually publish data events in real-time to external systems.

  
Entitlements  
See[Permission](https://docs.oracle.com/en-us/iaas/Content/access-governance/glossary.htm#glossary-p).

## G

  
Grant Type  
A method used to provision access to identities for a specific resource. These resources can be provisioned directly, through a policy, or can be requested by an identity.

## H

  
High-risk Access  
High-risk permissions exhibit numerous outliers that indicate uncommon or unexpected access compared to peer segmentation. These anomalies suggest potential security concerns or elevated risks. All high-risk items receive a Review recommendation, requiring reviewers to individually assess these permissions with priority to make informed decisions.

## I

  
Identity  
A unique representation of a user or machine in Oracle Access Governance, with attributes like first name, last name, username, email and other attributes sourced from one or multiple Authoritative systems.

  
Identity Collection  
A set of identities, created to assign access privileges over applications and resources to its members.

  
Identity Orchestration  
Oracle Access Governance brings together diverse Authoritative Sources and Managed Systems by supporting low-code integrations. It facilitates data transformations and correlation rules which ensures data coherence, extracts the required identity data from various systems into Oracle Access Governance, enables businesses to perform robust access control, intelligent access reviews, and perform fulfillment through account provisioning.

  
Identity Hub  
The Identity Orchestration engine of Oracle Access Governance that fetches or reconciles identity and access data from identity orchestration, and provisions identity and access data from Oracle Access Governance to the identity orchestration.

  
Inbound Data Transformations  
Inbound data transformations allow you to modify identity or account data values during the data ingestion process.

  
Insights &amp; Recommendations  
A set of prescriptive analytics and identity intelligence from identity and access data, enabling access reviewers and approvers to take quick and correct actions efficiently.

## J

  
Joiner-Mover-Leaver  
Refers to the different types of provisioning supported by an Identity Governance and Administration service.  

- Joiner refers to action taken by the system when an identity joins the company, such as assigning some birth-right access privileges.
- Mover refers to the acton taken by the system when an identity moves within the same organization, for example, changes in access privileges when user changes location or job.
- Leaver refers to the actions taken by the system when an identity leaves the company, such as revoking access over all corporate applications and systems.

## L

  
Low-risk Access  
Low-risk permissions exhibit minimal to no outliers and are common among peer segmentation—such as those with similar organization, location, resource type, and sensitivity level. All low-risk items receive an Accept recommendation, allowing reviewers to efficiently bulk-approve these access requests.

## M

  
Managed System  
Applications and services containing accounts and respective access privileges but do not serve as a trusted source of identities in your enterprise information. By establishing an orchestrated system, Oracle Access Governance manages user accounts and access permissions for these applications leveraging the defined access controls.

  
Matching Rules  
Also called Correlation Rules. See[Correlation](https://docs.oracle.com/en-us/iaas/Content/access-governance/glossary.htm#glossary-c).

## N

Notification

Automated email alerts to keep you informed of significant events occurring within the Oracle Access Governance service instance. These resources can be related to account operations, approval operations, review tasks, or error alerts.

## O

  
Overview  
The first page users see when they log in into the Oracle Access Governance service. This page shows the widgets available to users to track their access privileges, access review and approval tasks.

  
Orchestrated System  
Oracle Access Governance can be integrated with various applications and systems. These systems can be authoritative sources of identity data (for example, HR systems, Active Directory) or managed systems in which access privileges are granted (for example, applications, databases).

  
Orphan Account  
An identity account not associated with any active identity.

  
Organization  
Logical and hierarchical grouping of identities, such as belonging to same business unit, to control access management and access reviews operations within an enterprise.

## P

  
Permission  
A specialized type of assignment that defines access rights and the set of actions an identity can perform over specified resources and applications, for example, access to some sections in Oracle Access Governance console.

  
Policy  
Policies are the mechanism by which you can provide resource access to identities within your organization. Policies associate resources and permissions with identities by means of roles and access bundles.

  
Provisioning  
The process of adding user's access to an application, service and/ or software system, or hardware. Provisioning occurs automatically when certain access permissions are approved, or when some role membership or permission is assigned to a user through an access policy in Oracle Access Governance.

## R

  
Resource &amp; Application  
The external system, cloud service, database, directory server, or other source of identity data to be managed and audited by an identity management system.

  
Role  
A collection of permissions and access bundles associated with one or multiple applications or services. Roles are used to assign permissions to identities through policies, or by request.

## S

  
Service Account  
The administrative account or any account on any system that manages that system. It can be assigned to an Identity or Identity Collection.

  
Service Instance  
With respect to Oracle Access Governance, Service Instance refers to cloud application instance running on Oracle Cloud Infrastructure (OCI). Each instance is uniquely identified by an Oracle Cloud Identifier (OCID), along with compartment, region, license type, allowing you to manage these across cloud environment. Oracle Access Governance service instance have a format`AG-<servicename>`, having an`AG`prefix.

## W

  
Workflow  
A business process that orchestrates end-to-end activities, involving sequential and parallel steps, through which an access request or review passes, from initiation to completion.

  
Workforce User
