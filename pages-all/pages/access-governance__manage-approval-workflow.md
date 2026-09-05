# Manage Approval Workflow
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Approval Workflow

Users with the Access Control Administrator or Administrator application role can monitor and manage the approvals using the Oracle Access Governance Console.

On creating a new approval, notification will be sent to the approvers via email, or you can either click on the link from the email or can log in to the self-service portal to access the existing approvals.

## View Workflow Details

You can view approval workflow details.

- Sign in to the Oracle Access Governance Console with the appropriate application role. See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference).
- From the navigation icon, select Access Controls , and then Approval Workflows . The Approval Workflows page opens to view and manage the existing workflows. A list of existing approvals defined are displayed.
- Click the Actions icon corresponding to the approval workflow and select View details .
- On the details page, click the Actions icon and select View to view approval details.

## Edit Workflow Details

You can edit workflow details to modify, add or delete approval workflow configurations, change enforcement criteria, change failure actions, or update general details.

- In the Approval Workflow screen, click corresponding to the approval request.
- From the pop-up menu click Edit .

Edit approval workflow screen appears.
- In the Build Approvals step, click Actions icon corresponding to the required workflow.
- From the pop-up menu click Edit .
- Modify the required details in the subsequent screens.
- Optionally, you can click corresponding to the Single Approver or All approvers required entity to either delete the approver, add next approver, or to add a parallel approver to the workflow.
- Navigate to the Add Details step.
- Modify the required details, and click Next .
- Navigate to the Review and Submit step and click:
- Publish : To publish the edits
- Back : To do any corrections, if required
- Save Daft : To save the workflow details
- Cancel : To retain the existing workflow details

## Delete Workflow

- In the Approval Workflow screen, click corresponding to the approval request.
- From the pop-up menu click Delete .
- In the confirmation pop-up, select:
- Confirm : To remove the workflow or
- Cancel : To retain the workflow

## Disable Workflow

When you disable an approval workflow, it can’t be assigned to new entities. However, any entity already using the workflow can continue to use it.
For example, if an access bundle uses a workflow that is later disabled, access requests for that access bundle can still use the disabled workflow. However, you cannot update or create new access bundles with an approval workflow that has been disabled.
- In the Approval Workflow screen, click Actions corresponding to the approval request.
- From the pop-up menu click Disable .
- In the confirmation pop-up, select:
- Confirm : To disable the workflow or
-
