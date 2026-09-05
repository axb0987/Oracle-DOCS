# Understanding Reviewer's Actions for Effective Access Certification
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm
- Fetched: 2026-09-05 03:16 CDT

# Understanding Reviewer's Actions for Effective Access Certification

As an Access Reviewer, you can certify access privileges using the My Access Reviews feature. You can review identity, access control, and ownership review tasks, bulk approve low-risk items, check the AI/ML-equipped prescriptive analytic insights, review high-risk items, and make informed decisions based on AI/ML-driven recommendations provided by Oracle Access Governance. You can also reassign or delegate your review tasks to some other reviewer.

## Access Review Task Types in Oracle Access Governance

After a campaign is launched, the Campaigns service in Oracle Access Governance actively tracks the access for the identities in scope, generates intelligent insights, and creates the access reviews. Based on the Access Review type, Oracle Access Governance generates identity review, access control, and/or ownership review tasks.

Here are a few details about each access review task:

### Identity Review Tasks

Identity Review tasks include certification of identity access rights, evaluating user accounts, permissions, and roles. These are initiated when you launch an on-demand Identity Review task, or are initiated on occurrence of some identity event, such as department change, manager change, and so on. A single campaign may generate multiple review tasks. For example, when you launch Identity Access Reviews , Oracle Access Governance may generate access reviews tasks for accounts, permissions, or roles associated with a single identity on the My Access Reviews → Identity page.

Oracle Access Governance generates prescriptive insights and provide recommendations so that reviewers can make an informed decision to either Approve or Reject the required identity access.

### Access Control Review Tasks

Access Control Review tasks include audit of Identity and Access Management (IAM) policies, and identity collections, initiated by on-demand Policy Review and Identity Collections Review campaigns. For example, when you launch review for domain administrator policy for your tenancy, Oracle Access Governance may generate access review tasks for the Policy type on the My Access Reviews → Access control page.

Oracle Access Governance generates prescriptive insights and provide recommendations so that reviewers can make informed decision to either Approve or Reject entire policy at once, or make decision to Approve or Reject specific policy statement in that policy.
Note  
  
For an OCI policy, reviews are limited to the basic policy constructs. Advanced syntax including the "where" clause are beyond the scope of our supported feature.

### Ownership Review Tasks
Ownership Review tasks include:
- Audit of Identity and Access Management (IAM) Unmatched accounts , initiated by event-based access reviews. These tasks help you to review any unmatched accounts for identities in Oracle Access Governance. While setting up an unmatched account event, you can select to remove the unmatched accounts automatically. As a reviewer, you can select an identity to match to, or you can remove the unmatched account
- Ownership review of Oracle Access Governance resources. These tasks help you to review and verify that only authorized owners are managing Oracle Access Governance resources. For example, you may want to run periodic campaigns to review group ownership of Identity Collections defined in Oracle Access Governance.

You can view all the past ownership reviews run for the resource in the Access Review trail section. Based on the approval workflow selected in the campaign, either primary owner or an active Oracle Access Governance workforce identity is chosen as the reviewer. As a reviewer, you can change primary and/or additional owners of the resources, certify the current ownership, or reassign the review task to some other active Oracle Access Governance user.

## Intelligent Insights - Review Recommendations based on Prescriptive Analytics

Oracle Access Governance leverages prescriptive analytics to generate insights and recommend required actions on the review tasks. This enables access reviewers to make corrective decisions, lessen the administrative burden, and reduce cost.

Prescriptive analytics goes beyond prediction and involves action-oriented recommendations. These are data-driven guidance. Oracle Access Governance performs complex calculations and considers many dimensions such as organization, location, resource, and the sensitivity of that resource before recommending a decision. On a high-level, analysis of the permission is based on the following factors:
- Comparison with peers reporting to the same manager
- Comparison with peers with the same job code
- Comparison with peers in the same organization
- Recent changes in a user profile

As a reviewer, you get data-driven recommendation which simplifies the review process and mitigates the manual effort involved in identifying the anomalous permissions. From the Insights page, you can also track trail of reviews happened on a specific access, necessary for auditing purposes. You also get to track series of event changes involved for that access. All these details help you to make an informed decision for that access.

## Audit Trail: Monitoring Access Review and Access Request Decisions

Audit Trail in Oracle Access Governance captures the history of request approval and access review tasks. It records decisions made during access requests and reviews, including whether access was accepted, rejected, or revoked, along with any justifications provided.

### In Scope - What it Tracks
- Approval and access review decisions, including decisions to accept, reject, or revoke access, with justifications.
- Approve and revoke events for access granted by requests or directly assigned accesses in Managed Systems (Grant Type Request and Grant Type Direct ).
- Revoke of identity accesses for event-based reviews that are triggered when there are identity attributes changes. This doesn't show access revoked through policy when there are attribute changes.
- Approval of access requests with SOD violations. These requests are identified by the icon indicating that request was approved even though there were separation of duties violations from the Risk Management Cloud.
- Time-limit access reviews approved or requested with appropriate justification. All time-limit accesses are identified by the  

  
clock icon.

### Out of Scope - What it Doesn't Track
- Access granted or revoked through policies, as these are reviewed at the policy level, not the identity level.
- Updates made directly in Orchestrated systems. For example, a role is removed from the Orchestrated Systems

## Recent Change Events Log: Tracking Attribute Changes

The Recent Changes Log tracks identity attribute changes that are enabled in the Event-based Setup . For Campaigns (non-event-based), it shows all the change events for attributes with Event-based Setup enabled that occurred for the given identity over the past six months. For event-based campaigns, it logs only changes for the attribute triggering the review.

### In Scope - What it Tracks
- Attribute change, such as department updates, if enabled in the Event-Based Setup.
- Changes in attribute that triggered the event-based reviews to perform micro-certification.
- For Campaigns, changes in identity attributes, enabled for Event-Based Setup, for the past six months.
- Access Request approval and reviews for accesses granted by requests or directly assigned accesses in Managed Systems.
- Revocation reviewed through event-based access reviews (not policy-based)

### Out of Scope - What it Doesn't Track
- Specific access that was lost or gained due to attribute change.

Example : If a person's department changes and the department attribute has been enabled in Event-based Setup -&gt; Change events , the changed attribute value will display in this section. It will only show which the changed attribute value and does not show what specific access was lost or gained due to the attribute change. For this mover scenario, all the accesses that the identity currently possesses need to be reviewed as a review task.

## Delegating your Review Tasks

Delegating an access review task allows you to transfer your forthcoming review tasks to some other reviewers either temporarily or indefinitely. Typically, you would want to delegate a review item to some other reviewer or an identity collection during your absence, such as vacation.

With delegation, the ownership of review items does not change. A backup reviewer is assigned in absence of the intended reviewer so that no delays happen. On the Insights page, the reviewer can see complete details from the Access Review Trail . For example, as a manager going on vacation, you can delegate your review tasks to the team lead. During your absence, the team lead can continue to take decisions on your behalf which you can see from the Access Review Trail . However, the prime responsibility to review access review tasks will still be with the manager. You can delegate your access reviews using the self-service feature, that is from My Stuff → My Preferences . For more information, see[Manage Delegation Preferences](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-delegation-preferences.htm).

## Reassigning a Review Task

Reassigning an access review task allows you to change reviewer for your pending review tasks to some other reviewers permanently. With reassignment, the ownership of review items changes. The review tasks are moved from the original reviewer and are assigned to the new reviewer. Only the new reviewer can see the reassignment details in the access review trail.

Typically, you would reassign your pending review items when there is a change in responsibility. For example, as a manager exiting the company, you can reassign your existing review tasks to your manager or your replacement. This shifts your pending review items to the new reviewer.

## Bulk Changes - Managing Multiple Review Items Simultaneously

Oracle Access Governance allows you to approve, reject, or reassign multiple review items simultaneously, rather than making the same decisions individually. Reviewing multiple items at once reduces the administrative burden and saves time.

Use the data-driven recommendations to efficiently make a decision to approve or reject multiple requests at once. For example, while performing periodic access reviews for your team, you can approve all low-risk review items, with the Accept recommendation at once. You can even select multiple or all items to reassign the tasks to some other reviewer.
Here's what you can bulk-review for each review task:
- For identity review tasks, you can approve or reject multiple review tasks simultaneously. You can even reassign multiple identity review tasks at once.
- For access control tasks, for a policy, you can approve or reject all statements at once.
- For access control tasks, for an identity collection, you can approve or reject all members at once.
- For event-based reviews, you can configure to auto-approve low-risk tasks. You can also configure to auto remove unmatched accounts.

Bulk changes combined with prescriptive analytics allow you to speed up the process, improving operational efficiency without compromising security.

## Accept Temporary Access for Identity Access Reviews

You can temporarily accept access while certifying identity access to a permission. Access can be accepted for an indefinite period or set to expire based on a specified expiration period.
The expiration period depends on the access bundle configuration. Temporary access is applicable for following reviews:
- Assignment Type : Permission
- Granted Permission Type : Access Bundle
