# Approval Workflows in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm
- Fetched: 2026-09-05 03:17 CDT

# Approval Workflows in Oracle Access Governance

Approval Workflows are structured processes designed to automate approvals based on predefined workflows. These workflows ensure that access requests, micro-certifications and access reviews are reviewed and approved by the appropriate stakeholders, enhancing security and compliance.

For example, when a user requests access to an access bundle by using a self-service module, the approval workflow associated with that request triggers a notification by using email to the approvers, who then review the request and decide to approve, reject it, or request further information. The result of the approval process is updated and provisioning activities are triggered in the specific orchestrated system. To create and manage approval workflows, see[Create Approval Workflows](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm#create-approval-workflow)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm#manage-approval-workflow).

## Built-In Approval Workflow Templates

Oracle Access Governance offers approval workflow templates which you can use as a foundation to design the custom workflows. You can combine several templates in parallel or sequentially to create your own approval workflows.

### Beneficiary

The approval request is sent to the identity receiving the access (the beneficiary), allowing them to self-approve specific permission. The user requesting the access should approve it themselves. Suitable for low-risk permissions where the beneficiary is trusted to approve their own access

Example : Use this for requesting access to pre-approved, non-licensed enterprise software, where the beneficiary self-approves the request.

### Beneficiary's Manager

The approval request is sent to the beneficiary's manager. Use this to validate whether the access is appropriate, relevant, or within business scope.

Example : Use this when requesting access to a licensed third-party tool.

### Business Approvers

The approval request is sent to one or more business approvers to review and approve requests based on business needs. This role grants approval responsibility only and doesn't provide ownership or management of access resources.
Add business approvers when creating or updating access bundles or roles.
- For access requests, if no business approvers are configured, the request is sent to the owners. If no owners are available, the access request is canceled.
- If a campaign uses a business approvers workflow, the review is automatically assigned to the resource owner. For example, Access Bundle reviews are assigned to the Access Bundle primary owner.

Example : Send an approval request to the Business Approvers to confirm that the requested access is needed for the user's job.

### Primary Owner

The approval request is sent to the resource's primary owner. Configure to allow or disallow self-approval. If the self-approval is set to Yes , then the approver and beneficiary can be the same identity.

Example : Sending an approval request to the access bundle primary owner to approve database related permissions within an access bundle.

### Owners

The approval request is sent to the resource owners (primary and additional owners) to ensure proper usage of the resource. You may configure to allow or disallow self-approval. If the self-approval is set to Yes , then the approver and beneficiary can be the same identity.

Example : Sending an approval request to the access bundle owners to approve access requests to the access bundle.

### Custom User

The approval request is directed to a specific, predefined identity, typically for centralized control. Suitable for scenarios requiring specialized approval authority.

Example : Sending an approval request to an IT administrator when a contractor requests access to an enterprise team collaboration application.

### Management Chain

The approval request follows a hierarchical structure, starting from the beneficiary's manager and moving up the chain as needed. Suitable for business-critical permissions requiring multi-level approvals.

Example : Use this when an identity is requesting a "Contributors" role permission to publish and download updates on a client-facing storage system.

### Identity Collections
The approval request is directed to a pre-defined identity collection or group, for collaborative decision-making. Suitable for cases where multiple approvals or unanimous approval is required from all members. You can configure:
- Minimum number of approvals required to proceed with the request.
- Veto power to deny the request, if any member rejects.
- Escalated identity collection who receives the request upon expiry of the original request timeline.

If the group lacks enough members, then the request is canceled. See[Handling of Large Groups in Approval Workflows](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-handling-large-groups). Example : Use this when an identity is requesting a database-admin privilege access to route a request to the Database Admin identity collection.

## Escalation Handling in Approval Workflows

While configuring your approval workflows, you can set an escalation time—the number of days to wait before escalating the approval request to the next approver. This happens because the original approver didn't respond within the configured time.

Applies to : Beneficiary , Beneficiary's manager , Owner , Custom User , Management Chain template types

First Escalation happens when an approval task hasn’t been completed in time. Searches the original approver’s management chain for the first available active manager. Subsequent Escalations occur if even the escalated approver doesn’t take action. Now, the system starts its next search from the manager of the last person who had the task, continuing up the chain.

Each time the escalation timer expires for a request, Oracle Access Governance follows a structured process to move the task forward. A notification email is sent to the escalated approver (manager or an identity part of escalated identity collection) to inform them about the escalated task.
- First Escalation: Searches the approver’s management chain to find the first active manager included in Oracle Access Governance.
- Subsequent Escalations: Searches manager of the most recent approver the task was escalated to, conitinuing up the management chain.
- Ceiling Consideration: If an escalation ceiling (maximum number of hierarchy levels) is set, the search stops one level before reaching it.
Applies to : Identity Collection template types
- Searches each member part of the escalated identity collection and assigns the task to anyone who hasn’t already received it. If the task has already been escalated to all of them, no further action is taken. If an escalation ceiling (maximum number of hierarchy levels) is set, the search stops one level before reaching it.

## Handling Large Group Approvals: Members Limit and Criteria

When you select an identity collection for any part of the approval workflow, such as approvals, escalations, or delegations, then Oracle Access Governance enforces a member limit.

You can select identity collection of any size but only a maximum of 25 members can actively receive and approve tasks. Oracle Access Governance selects the first 25`ACTIVE/WORKFORCE`members.
If fewer than 25`ACTIVE/WORKFORCE`members are available, then`CONSUMERS`are added to reach the 25 members limit. However, no`CONSUMER`member receives an approval task, instead a fallback mechanism is kicked-in, as follows.
- For access reviews, see[Fallback Mechanism in Access Review](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review).
- For access requests, Oracle Access Governance searches up the approver’s management chain until it finds an`ACTIVE/WORKFORCE`, who is then assigned as the approver.
Note  
  
For escalated or delegated approval workflows, consumer members are not considered and the fallback mechanism doesn't apply.

Membership Change in Approval Assignment

The review tasks always remain with the assigned 25 members. If a member is removed from an identity collection or becomes`INACTIVE/CONSUMER`, the tasks are passed to another member in the group to maintain the 25 members count.

## Auto-Approval Matrices and Criteria

The following tables summarizes the key criteria for auto-approval across the two matrices.

Approver is requestor or workflow has auto-approval IC and requestor is a member? Workflow allows auto-approve if AGR or SOD violations present? Workflow allows self-approval? Is approver beneficiary? Are violations present? Auto-approval Action
Yes No No No No Approve
Yes No No No Yes No action
Yes No No Yes No No action
Yes No No Yes Yes No action
Yes No Yes No No Approve
Yes No Yes No Yes No action
Yes No Yes Yes No Approve

Workflow is configured to auto-approve if no AGR or SOD violations are detected? Are violations present? Auto-approval Action
Yes No Approve
