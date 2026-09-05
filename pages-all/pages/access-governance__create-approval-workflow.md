# Create Approval Workflows
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm
- Fetched: 2026-09-05 03:13 CDT

# Create Approval Workflows

Oracle Access Governance users with the Access Control Administrator or Administrator application role can create approval workflows from the Oracle Access Governance Console.

## Navigate to Approval Workflow

- Sign in to the Oracle Access Governance Console with the appropriate application role. See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference).
- From the navigation icon, select Access Controls , and then Approval Workflows . The Approval Workflows page opens to view and manage the existing workflows.
- Select the + Create approval workflow button.

The Create a new approval workflow page is displayed to configure an approval workflow.

## Add a New Approval Workflow

You can customize an approval workflow using the built-in approval templates.
- In the Create a new approval workflow page, click the plus icon. The Add a new approval side pane is displayed.
- Select one of the built-in templates from the Which type of approval? list. For more information, see[Built-In Approval Workflow Templates](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-approval-workflows-types).
- Based on the approval template selected, configure the required fields. See[Configure Approval Templates](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm#workflow-configure-approval-templates)and[Advanced Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm#workflow-advanced-settings).
- Continue designing the workflow, if required:
- Add parallel : To add a workflow at the same level and receive an approval request at the same time as the previously configured workflow.
- Add next : To add stages to the approval workflow that run sequentially. The approval for a previous stage must complete before next stages can be run.
- Select one of the following for parallel approval workflow:
- All : The stage is marked as 'Approved' only if every template in the stage is approved.
- Any : The stage is marked as 'Approved' if at least one template in the stage is Approved.
- Select Next .

### Configure Approval Templates

Configure the approval template fields as per the template type.

Configure the following fields:

Field Name Description
Owner, Primary Owner, and Business Approvers
Should self approval be allowed? Select Yes to allow self-approval, where a user can approve their own tasks (access request or access review) without the intervention of an external approver.
Custom User
Which user? Select the user to whom you want to send an approval task when a custom user template type is selected.
Should self approval be allowed? Select Yes to allow self-approval, where a user their own access rights without the intervention of an external approver.
Management Chain
Management chain ceiling? The upper limit of hierarchy beyond which approval requests should not be sent. Select one of the following:
- Number of levels up
- Number of levels from top
- Identity collection
How many levels up? Enter the number of levels up the approval request should go, starting from beneficiary’s manager. The approval request is not sent beyond the defined number of levels.
How many levels down from top? Enter the number of levels from top the approval request should stop, starting from the top-most role in the organization.
Ceiling identity collection

Identity collection whose members represent the end of the management chain. Approvals will not be assigned to any member of this identity collection or to any of their managers and above.
Should the workflow continue when the approval result is rejected? Select Yes or No to configure whether a workflow should continue after a rejection is received. For example, as per the defined approval sequence, if the beneficiary’s manager rejects the request, should the workflow still proceed to gather approval from the Management Chain.
Identity Collection
Approval identity collection Select an identity collection that should receive an approval request.
Do all members need to approve? Select if the approval is required by all the members to approve a request. Select Yes to get approval from all members, and No to configure further.
How many members should approve? Select the minimum number of members required to approve the request before marking it as approved.
Should approvers have veto power? Select Yes to allow the approval request to be rejected if any single member rejects it. Any one member’s rejection acts as a veto, halting an approval workflow and marking it as rejected.
Which identity collection should requests escalate to? Select the identity collection whose members should receive escalations.
Should self approval be allowed? Select Yes to allow self-approval, where a user can approve their own access rights (access request or access review) without the intervention of an external approver.

### Advanced Settings for Approval Templates

Additionally, you can configure or update the default advanced settings while configuring an approval workflow:

Configure the following advanced settings:

Field Name Description
How many days between notifications? Duration (in days) before sending a reminder over email.
How many days to wait before escalating the approval request? If no action is taken within the configured number of days, the request is forwarded and escalated to the next approver. See[Escalation Handling](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-escalation-matrix-approval-workflows).
Which identity collection should never receive escalations? Select the identity collection who should never receive an escalated approval requests, even after delays. For example, Board of Members identity collection for a campaign approval task.
Should the approval request have an expiration time? Select Yes or No .
How should we handle pending approvals after the approval request expires If an approval request has an expiration time, select one of the following to close the pending tasks:
- Approve all
- Reject all
How many days until the approval request expires? Configure how many days an approval request remains active before it expires.
Should the workflow continue when the approval result is rejected? Select Yes or No to configure whether a workflow should continue after a rejection is received. For example, as per the defined approval sequence, if the beneficiary’s manager rejects the request, should the workflow still proceed to gather approval from the Management Chain.

## Add Details

With the Add details step, you can add a name to the approval workflow and give a short description of the workflow.
To add details:
- Enter the name of the workflow in the What do you want to call this approval workflow? field.
- Enter a short description of the workflow in the How do you want to describe this approval workflow? field.
- On entering the details, click Next to go to the Review and submit step.
- Optionally, you can click:
- Save Draft : To save your changes and later come back and edit the workflow or details
- Cancel : To cancel the current process.
- Back : To go back to the previous step.

## Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

## Review and Submit

The Review and submit step displays the information you have added in the previous steps. In this screen, you can click:
- Publish : To publish the workflow
- Save Draft : To save your changes and later come back and edit the workflow or details
- Cancel : To cancel the current process
-
