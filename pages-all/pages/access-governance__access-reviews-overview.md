# Access Reviews in Oracle Access Governance: Certify Access Privileges with Campaigns and Event-Driven Micro Certifications
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm
- Fetched: 2026-09-05 03:13 CDT

# Access Reviews in Oracle Access Governance: Certify Access Privileges with Campaigns and Event-Driven Micro Certifications

Access Reviews , also known as Access Certification or Access Attestation , is the process to evaluate and certify the access privileges granted to identities within an enterprise. It checks and certifies if privileges granted are still required and align with the current job at work. Use the Oracle Access Governance Access Reviews feature for reviewing the access privileges. Make swift and accurate review decisions by examining insights and AI-powered recommendations based on prescriptive analytics.

Enterprises have large distributed landscape across on-premises and cloud systems. To avoid excessive accumulation of irrelevant permissions, or unauthorized access to critical information, Access Reviews are run regularly to monitor and certify the accesses. These are vital for secure access management and compliance processes.

## Key Benefits of performing Access Reviews with Oracle Access Governance

Access Reviews help enterprises to govern frequent access changes, reduce cost, manage identity access lifecycle, maintain compliance, and strengthen the security posture. Enterprises handle voluminous access changes on daily basis. Regular reviews can proactively detect and remove excessive permissions or irrelevant privileges.

Oracle Access Governance Access Reviews feature offers various types to review access privileges. For example, use Campaigns to launch a set of ad hoc or periodic access reviews, or use micro-certifications, which are based on event change, timeline change, or detection of an orphan account.
Access Reviews in Oracle Access Governance helps to:
- Reduce cost by providing recommendations to remove non-essential and unwanted license or resources. For example, revoking application access for employees who no longer need it.
- Strengthen security posture of an enterprise by regularly reviewing accesses, ensuring that right resources have been granted just enough accesses for their role. For example, Oracle Access Governance performs automatic micro-certifications to detect event changes (location change, department change), timeline changes, or detect orphaned accounts that pose a security threat.
- Meet governance compliance and requirements by maintaining periodic access review audit reports. For example, ensuring compliance with industry regulations and compliance laws, such as GDPR, HIPAA, SOX, through regular access review campaigns.
- Simplify decision-making by recommending AI/ML-driven access review insights, such as peer group analysis, outlier detection, or recommendation. For example, Oracle Access Governance gives recommendation to revoke a high-risk privilege for an identity based on prescriptive analytics.

## Types of Access Reviews Offered by Oracle Access Governance

With Oracle Access Governance, you can run ad hoc or periodic Access reviews Campaigns over a set of identities, groups, accounts, roles, policies, and permissions. You can even run ownership reviews to verify resource ownership. Use near-real-time micro-certifications to run automatic reviews on specific components based on occurrence of an event change, timeline change, or unmatched accounts.

### Access Review Campaigns: Ad hoc or Periodic Access Reviews

Use Campaigns to initiate periodic or ad hoc access review process. These are snapshot-based reviews , capturing all the relevant access information at a given point of time, and then assessing and generating access reviews tasks. Any change made to the data after the campaigns are setup won't be reflected in these reviews.
The access review types and selection criteria[depend on Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-types-to-launch-access-review-campaigns).
- [Identity Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#identity-access-reviews)
- [Policy Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#policyreviews)
- [Identity Collection Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#identitycollectionsreviews)
- [Resource Ownership Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#resourceownership)

### Identity Access Reviews

Identity access reviews refer to assessing access privileges for identities in your enterprise, where access to a specific resource is verified or validated. You can certify access for Workforce and Consumers identities by running the identity access reviews. Reviewers, who are active Workforce users, can accept or revoke the assigned privileges.
Define selection criteria based on:
- Users (who has access?) : Select a set of core and custom identity attributes.
- Applications (what are they accessing?) : Select services, applications, or cloud accounts.
- Permissions (which permissions?) : Select permissions that are assigned directly in your Managed System, or permissions provisioned within Oracle Access Governance. You can use this criteria to quickly certify privileges for all Orchestrated Systems based on the permissions ingested directly from the Managed System. These are also called "reconciled permissions." For more information on running reviews based on permissions, refer to[Identity Access Reviews based on Permissions Assigned Directly in Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#identity-access-reviews-for-reconciled-permissions).
Note  
  

- For the Oracle Access Governance system, you can run reviews based on permissions assigned directly (`DIRECT`) or Access Bundles granted through request from the Which Permissions? tile. Permissions or accounts provisioned through policy are not eligible in this review.
- You can provision OCI IAM groups and application roles by creating an access bundle. For Oracle Cloud Infrastructure (OCI) system you can review OCI access bundles from the Which Permissions? tile. For the Oracle Access Governance system, you can run reviews based on permissions assigned directly (`DIRECT`) or Access Bundles granted through request from the Which Permissions? tile. Permissions or accounts provisioned through policy are not eligible in this review.
- Roles (which roles?) : Select roles provisioned to identities. You can also define the approval workflow to select the number of review levels, review duration, and reviewer details. For more information on creating identity access reviews, refer to[Create Identity Access Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm).

Example : You may run campaigns to evaluate and certify if junior associates or contractors in your organization have access to critical permissions or restricted information.

### Identity Access Reviews based on Permissions Assigned Directly in Managed Systems

You can certify identity accesses by running identity access reviews on the permissions ingested directly from the Managed System. These are also called "reconciled permissions." Reconciled permissions refer to inherent permissions that are provisioned directly in the Managed systems without provisioning these from Oracle Access Governance. Run these reviews by selecting the Oracle Access Governance system from the Campaigns page.

Using insights and recommendations, reviewers can take action to accept or revoke these permissions. However, to manage your accesses at a granular level, use Access Bundles to provision the permissions.

When you select a set of permissions from the Which Permissions? tile, the system generates review tasks for all the eligible identities having access to these permissions either directly or through a request (Access Bundles).
Here's what's included in the review:
- Identities with permissions granted directly with grant type DIRECT .
- Identities with permissions granted as part of Access Bundles with grant type Request .
- Identities with permissions granted through Roles with grant type Request .
- Accounts of the identities that are provisioned directly or requested.
Note  
  
Permissions or accounts provisioned through policy, or Oracle Identity Governance (OIG) and Oracle Cloud Infrastructure (OCI) identity accounts are not covered in this review.

The components eligible for review vary based on the selected criteria. For more details, refer to the table in[Eligible Orchestrated System Types to Launch Access Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-types-to-launch-access-review-campaigns).
Things to Remember
- Permissions assigned directly or Access Bundles granted through request are available for review in the Which Permissions? tile. The grant type must be Request or DIRECT for the permissions to be included in the reviews.
- If directly assigned permissions are associated with an Access Bundle, which is then provisioned to identities through Request , then you will see only the Access Bundle and not individual permissions. For roles provisioned to identities through Request , it shows up as a role under the Which roles? tile.

Example : If Read and Alter permissions are included in an Access Bundle and provisioned to identities via Request , you won't be able to view and review these particular permissions. You might select to review the Access Bundle.
- If an account contains permissions granted through policy, then no review task will be generated for that account.

Example : If an account contains four permissions, two of which are granted via policy, the review of permissions won't generate the account review task.

Scenario
You want to run access reviews for the identities based on Read and Update database permissions. Let's consider the following scenario:
- Alice has access to Read and Update permissions assigned directly.
- Jane has access to these permissions as part of Access Bundle, with additional Write permission.
- Betty being the database administrator has access to these permissions.
Here's what's included:
- For Alice , selected permissions will be reviewed.
- For Jane , Access Bundle will be reviewed with Read and Update and Write permissions only if Access Bundle is granted through Request .
- For Betty , role will be reviewed only if the role is granted through Request .
- Alice , Jane , and Betty identity accounts will be considered for review if the account or permissions associated with the account have not been provisioned using policy.

Reviewers can validate these access reviews from the My Access Reviews → Identity page following the process defined in[Perform Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/perform-access-reviews.htm).

Remediation Actions
As part of the closed-loop access remediation process,
- If a reviewer revokes the permission, it will be revoked from the Managed system.
- If a permission is part of an Access Bundle granted to the identity, you won't be able to revoke that single permission unless you revoke an entire Access Bundle.
- Accounts associated with permissions are not revoked if accounts contain permissions granted through policy.
- Identity accounts are revoked only when all the permissions associated with accounts are revoked.

### Policy Reviews

Review of Oracle Access Governance policies and OCI Identity and Access Management (IAM) policies to evaluate its effectiveness and compliance.

In Oracle Access Governance, you can create on-demand policy reviews, where you define the selection criteria to review policies. You can also define the approval workflow to select the number of review levels, review duration, and reviewer details. For more information, refer to[Create Policy Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-policy-review-campaigns.htm)and[Types of Certification Tasks in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#types-of-certification-tasks-in-oracle-access-governance).

Example : You may run quarterly reviews on the defined network and storage policy of your tenancy to assess if these meet the principle of least privilege and applicable regulatory requirements.

### Identity Collection Reviews

Membership review of a group to verify if only eligible set of members are assigned to a group. This is commonly known as "Group membership reviews."
You can create identity collection reviews for:
- Identity collections created in Oracle Access Governance
- OCI groups derived from Oracle Cloud Infrastructure (OCI)
Example : You can review if only eligible members are part of the Database Administrator group, managing and maintaining the database infrastructure for your project. An identity with the Sales Analyst role should not be associated with this group. For more information, refer to[Create Identity Collection Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collection-review-campaigns.htm)and[Types of Certification Tasks in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#types-of-certification-tasks-in-oracle-access-governance).

### Resource Ownership Reviews

Review ownership of resources that created within Oracle Access Governance, either periodically or on an ad hoc basis. By performing this review, you can ensure accountability of resources lies only with the designated owners.
Currently, you can run ownership reviews for the following Oracle Access Governance resources:
- Access Bundle
- Approval Workflows
- Identity Collections
- Orchestrated systems
- Policies
- Roles
- Access Guardrails
- Campaigns

Based on the approval workflow selected, the primary owner of a resource or any active workforce Oracle Access Governance identity will be considered for review. Reviewers can certify or change ownership of resources while performing reviews. For more information, refer to[Create Ownership Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-ownership-reviews.htm), and[Resource Ownership Review Task](https://docs.oracle.com/en-us/iaas/Content/access-governance/perform-access-reviews.htm#resource-ownership-review-task).

### Event-Based Micro-Certifications

Use Event-Based Setup to configure automated micro-certifications, triggered only when there are changes in the system of record, occurrence of an important date or time milestone, or detection of an orphan account. These are near real-time reviews and Oracle Access Governance continuously monitors profile changes to launch access reviews.

You must configure the attributes for which you want to enable event-based reviews. For more details, see[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).

As an active workforce user, you can review the event review tasks from the My Access Reviews → Identity page. If there's a change in event but no reviewable access items for that identity, then no review tasks will be generated for an identity.
You can configure event-based reviews for:
- Change event : Triggered by changes made in the identity profile, whenever an identity attribute is updated in the record system. These can be[Core or Custom attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Timeline event : Triggered on the occurrence of a particular date, such as the work anniversary date of an employee to perform access review.
- Unmatched event : Triggered when an onboarded account doesn’t match any identity within Oracle Access Governance.

## Eligible Orchestrated System Types to Launch Access Review Campaigns

The type of access reviews and what you can review in Oracle Access Governance depends on the system type chosen while running reviews. You can review access to systems managed by Oracle Access Governance including ownership reviews, review access for Oracle Cloud Infrastructure (OCI), and review access to systems managed by Oracle Identity Governance (OIG).

### Review Access to Systems Managed by Oracle Access Governance

Select this system to run access reviews or run resource ownership reviews . In the Oracle Access Governance system, you can run identity access reviews for all the orchestrated systems managed by Oracle Access Governance, such as Oracle Database, Flat File, Microsoft Active Directory, and so on.
We can broadly divide review requests into
- Review Access : To run identity access reviews, policy reviews, and identity collection reviews.
- Review Ownership : You can verify if only authorized owners are managing resources by running ownership reviews

#### Identity Access Reviews

Run identity access reviews for all the orchestrated systems using the Oracle Access Governance system. You can run these reviews based on core or custom identity attributes, applications they have access to, permissions granted from the Managed System, permissions provisioned within Oracle Access Governance as part of the Access Bundle, or roles granted to identities. For more information on running identity access reviews, refer to[Identity Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#identity-access-reviews).

Selection Criteria Eligible Components in Review
Who has access? to select identity attributes
- Permissions
- Access Bundles
- Roles
- Accounts
What are they accessing? to access applications
- Permissions
- Access Bundles
- Roles
- Accounts
Which permissions? to select Access Bundles`(REQUEST)`
- Access Bundle
- Roles
- Accounts
Which permissions? to select Permissions`(DIRECT)`
- Permissions
- Access Bundles
- Roles
- Accounts
Note  
  
If the account associated with the permissions is also included to give access through an Oracle Access Governance policy, then the account review tasks will not be generated.
Which roles? to select Roles`(REQUEST)`Roles

#### Policy Reviews

Run Oracle Access Governance policy reviews to evaluate policy effectiveness. Policies created within Oracle Access Governance are reviewed. Oracle Access Governance policies contains details of resources and permissions attached to a group of identities by the means of roles and/or access bundles.

#### Identity Collection Reviews

Run membership review of a group to verify if only authorized set of members are assigned to a group. This is commonly known as "Group membership reviews." You can run reviews for identity collections created in Oracle Access Governance.

#### Review Ownership

You can verify if only authorized owners are managing resources by running ownership reviews. For example, you may run ownership reviews to verify if only designated and authorized owners are managing the Approval workflows.

### Review Accesses for Cloud Services Managed by Oracle Cloud Infrastructure (OCI)

Select this system to certify identity access reviews, policy reviews, and OCI IAM identity collection membership reviews. Further, you can review assignment of OCI IAM groups and application roles managed by Oracle Access Governance.
The following review types are available:
- Identity Reviews (Direct) : Identity access rights by reviewing their application access, granted application roles.
- Identity Access Reviews for Accesses Managed by Oracle Access Governance : Identity access rights of OCI IAM groups and cloud services application roles assigned within Oracle Access Governance through access request.
Note  
  
If you request and assign Oracle Access Governance roles which includes the associated access bundles containing OCI IAM Groups or cloud services application roles, then choose to review Oracle Access Governance roles in the Oracle Access Governance system.
- Policy Reviews : OCI IAM policies that evaluates construct and functioning of a policy.
- Identity Collection Reviews : Group Memberships which evaluates that only eligible members have access to the group. If you choose to review OCI IAM groups and it contains a few members assigned from Oracle Access Governance, then with this review, you can only accept or revoke directly assigned members. For members assigned from Oracle Access Governance, choose to review the OCI Access Bundles using the Which permissions? tile.

#### Eligible Selection Criteria for Review in the Oracle Cloud Infrastructure (OCI) System

The components eligible for review vary based on the selected criteria, as follows:

Access Review Selection Criteria in the OCI System
Selection Criteria Eligible Components in Review
Which tenancies to select tenancies, cloud compartment, or domain
- OCI Accesses Managed by Oracle Access Governance
- Roles
- Identity Collections
- Policies
Note  
  
If you opt to refine further to select a specific domain, the service won't generate policy reviews.
Who has access? to select identity attributes
- OCI Accesses Managed by Oracle Access Governance
- Roles
What are they accessing? to access cloud services
- OCI Accesses Managed by Oracle Access Governance
- Roles
Which permissions? to select Access Bundles`(REQUEST)`
- Accesses Managed by Oracle Access Governance. It contains OCI Access Bundles
Which roles? to select application roles in OCI`(DIRECT)`Roles assigned Directly in OCI.
Which policies? to select OCI Policies Policies
Which identity collections? to select OCI IAM groups`(DIRECT)`Identity Collections
Note  
  
If you choose to review OCI IAM groups and it contains a few members assigned within Oracle Access Governance, then with this review, you can only accept or revoke directly assigned members. For assignments managed by Oracle Access Governance, choose to review the OCI Access Bundles using the Which permissions? tile.

### Review Access to Systems Managed by Oracle Identity Governance (OIG)

Select this system to certify access rights of an OIG identity by reviewing their application access, granted roles or permissions (entitlements). You cannot combine review for a specific permission (entitlement) and role in a single campaign.

## Usage Examples: Certifying Access Privileges with Access Review Campaigns and Event-based Reviews

Let's see some of the scenarios where campaigns and automated access reviews are useful.

### Example 1: Review Access Permissions for High-Profile Applications with Critical Functions

Scenario : To help your enterprise deter any harm against misuse of access rights for data sensitive applications, you need to schedule quarterly campaigns to certify access to critical functions, such as update and terminate permissions.
To do so, first select the system, then apply filters to select data sensitive applications using the What are they accessing? tile. Select appropriate permissions using Which permissions? . Complete the campaign steps to assign appropriate workflow and campaign details. Post this, the review tasks will be generated that the reviewer can review on the My Access Review page.
Note  
  
You can either create a campaign to review permissions or review roles but both cannot be selected in a single campaign. In this example, Which roles? will be disabled along with Which policies? As we selected to review identity access, policy and identity collection review selection parameters will also be disabled.

### Example 2: Review Policies for all Cloud Resources

Scenario : Your company updated their security protocols for data storage. As a cloud security administrator, you need to carry out on-demand access reviews of all the IAM policies available in your cloud account to ensure that it meets the latest security standards and regulations.

To do so, first select the system, add selection criteria to select cloud provider, cloud account, domain, or compartment. Complete the campaign steps to assign appropriate workflow and campaign details. In this example, the campaign reviewer can review all the applicable review tasks on the My Access Reviews → Access Control tab, with type Policy .

### Example 3: Group Membership Reviews for Project Groups

Scenario : As a project manager, carry out quarterly group membership review for your team to ensure only current team members have access to code repositories and access to required third-party applications. This process will help you to remove any unauthorized access as well as monitor and control project cost.

To do so, first select the OCI system, add selection criteria to select OCI groups, add an approval workflow along with campaign details. In this example, the campaign reviewer can review all the applicable review tasks on the My Access Reviews → Access Control tab, with type Identity Collection .

### Example 4: Enabling Automated Access Reviews for Employees Triggered by a Change Event

Scenario : As a business owner, you need to set up automated access reviews to perform micro-certifications whenever manager, job code, or location changes for an employee.
