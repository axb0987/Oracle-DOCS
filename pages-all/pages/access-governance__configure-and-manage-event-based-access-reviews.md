# Configure and Manage Event-based Access Reviews
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-and-manage-event-based-access-reviews.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure and Manage Event-based Access Reviews

You can perform micro certifications in Oracle Access Governance using the Event-Based Access Reviews . You can configure one or more predefined event types, which when triggered, creates the access reviews automatically. You can select to automatically approve the low-risk items, or reviewers can certify, that's accept or revoke accesses associated with the event.

## Configure Change Event Access Review

Configure Change event access reviews from the Event-Based Setup → Change page to trigger automatic occurrence of access review whenever a change in identity profile is detected.

Here's how you can configure Change events:

### Navigate to Change Event page
- Sign in on to the Oracle Access Governance Console with a user assigned the Administrator application role.
- Select from the navigation menu .
- Select Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Event-Based Setup page, select the Change tab. A list of available change events is displayed. Each change event has a status of Enabled or Disabled and an Actions drop-down menu , providing the option to Edit or View details .
- Select Create change event to create a new event or select Edit to update an existing change event.

### Edit Change Event Configuration
- From the Actions menu , select Edit for the event-type you want to enable. The Configure the event type page opens.
- Select the identity attribute from the list that must trigger the event-based access reviews.
- What do you want to name this event? : Enter a descriptive name.
- Attribute values to trigger this event for : Select attribute values . You can set value-based conditions only for Non-Boolean and Non-date-time attributes.
- Enable or disable this event-based access reviews : Set to Enable to activate this configuration.
- To automatically approve low risk task for this event type, select Yes .

### Configure Review Scope
- In the What type of access do you want to review list? , select the system types you want to include in the review.
- Select +Add filter to narrow down the review to specific applications, roles or permissions
- In the What do you want to refine? list, select one of the following:
- Permissions : Select specific entitlements or roles to review.
- Applications : Select specific orchestrated system
Note  
  
Available options might vary based on what you select for review.

### Select Approval Workflow
- Select an approval workflow for this event type access review. A list of the available workflows is visible. For more details, see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm). After you have selected the workflow, select the View approval workflow link to see a graphical representation of the selected workflow.
- Select the scope of justification required for review decisions. You can select for reviewers to add comments for all the review decisions, for revoke decisions only, or keep the justification field as optional.
- Select Save .

## Configure Shared Workflow for Several Change Events

Shared Workflow or Multi-event access review is considered whenever several change events are triggered for a single identity within a short span of time.

. To configure the shared workflow:
- Log on to the Oracle Access Governance Console with a user assigned the Administrator application role.
- Select from the navigation menu .
- Select Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Change tab, select Edit shared workflow .
- On the How do you want multi-event reviews to proceed? screen:
- Confirm to automatically approve low risk task for this event type by selecting Yes or No .
- Select an approval workflow for this event type access review. A list of the available workflows is visible. For more details, see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm). After you have selected the workflow, select the View approval workflow link to see a graphical representation of the selected workflow.
- Select the scope of justification required for access review decisions. You can select for reviewers to add comments for all the review decisions, for revoke decisions only, or keep the justification field as optional.
- Select the access review owner for this event type access review. By default, it's assigned to the administrator who configures this event type. Consider[Fallback Mechanism in Access Review](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before adding an owner.
- Select Save .

## Configure Timeline Event Access Reviews

Configure Timeline event access reviews from the Event-Based Setup → Timeline page to trigger automatic occurrence of access review annually on a particular date, such as job anniversary. By default, no automatic timeline event changes are per-configured. You must have at least one date attribute configured to enable this event type.
Here's how you can configure Timeline event:
- Log on to the Oracle Access Governance Console with a user assigned the Administrator application role.
- Select from the navigation menu.
- Click Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Event-Based Setup page, select the Timeline tab.
- To create events, select the Create timeline event button.
- On the Add a new timeline event configuration screen:
- Select date attribute in the Which date attribute should the event be triggered from? list. Date attributes are identity attributes with a Date type, that are enabled for event-based campaigns. For further details on defining attributes, review[View and Configure Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Enter number of days prior to the annual event date when the event should be triggered.
- Enter a unique event name in the What do you want to name this event? field.
- Choose to Enable or Disable the event-type.
- Select Yes to auto-approve low risk review task for this event type, else reviewers can take decision manually from the My Access Reviews → Identity page.
- Select the system for which you want to enable this event type. Based on your selection, a list of applicable applications are visible.
- Select the applications you want to include in the timeline event change. By default all applications will be included in the review.
- In the Choose your Workflow section,
- Choose an approval workflow for this event type access review. Consider[Self Certification Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#self-certification-guardrails)and[Fallback Mechanism in Access Review](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before configuring this workflow. For more details, see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm). Once you have selected your workflow, select the View approval workflow link to see a graphical representation of the selected workflow.
- Select the scope of justification required for review decisions. You can select for reviewers to add comments for all the review decisions, for revoke decisions only, or keep the justification field as optional.
- Select the access review owner for this event type access review. By default, it is assigned to the user who configures this event type. Consider[Fallback Mechanism in Access Review](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before adding an owner.
- Select Save to enable the event type changes.

## Configure Unmatched Accounts Access Review

Configure unmatched account event access reviews from the Event-Based Setup → Unmatched accounts page to trigger automatic occurrence of access review whenever an orphan account is detected in Oracle Access Governance. Reviewers can review access for the unmatched accounts from the My Access Reviews → Ownership page.

### Create an Unmatched Accounts EventTo create unmatched account events, complete the following tasks:
- Log on to the Oracle Access Governance Console with a user assigned the Administrator application role.
- Select from the navigation menu. Click Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Event-Based Setup page, select the Unmatched accounts tab.
- To create an unmatched account event configuration, select the Create an unmatched accounts event button. You are directed to the Add a new unmatched account event configuration page.

### Configure an Unmatched Accounts Event

- In What do you want to name this event? , add a meaningful name for the unmatched accounts event type.
- To enable this event type, in the Enable or disable this event-based access reviews option, select Enable .
- If you want the reviewer to take actions on the access reviews for unmatched accounts, in the auto remove unmatched accounts , select No .
- To automatically remove all unmatched accounts reported by this event, in the auto remove unmatched accounts option, select Yes . All unmatched accounts will be removed from your environment including Oracle Access Governance and any Managed Systems from which the account was ingested.
- Select one or more orchestrated systems for which you want to set up this event. By default, all the orchestrated systems are considered for the unmatched accounts event.
- In the Choose your Workflow section,
- Choose an approval workflow for this event type access review. For more details, see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm). Once you have selected your workflow, select the View approval workflow link to see a graphical representation of the selected workflow. You can select
- Application Owner , where access review owner will be assigned as the reviewer or certifier. Consider[Self Certification Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#self-certification-guardrails)and[fallback process](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before configuring this workflow.
- Custom User , where any active identity available in Oracle Access Governance can be assigned as the reviewer.
- Select the scope of justification required for review decisions. You can select for reviewers to add comments for all the review decisions, for revoke decisions only, or keep the justification field as optional.
- Select the access review owner for this event type access review. By default, it is assigned to the user who configures this event type. Consider[fallback process](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before adding an owner.
- Select Save .

## View Event Details

As an Administrator , you can view details on each event-type configured for your application in the Oracle Access Governance Console. You can view the date when the event was enabled, selected rules and systems for the event-type, approval process details, along with campaign owner.

To view event-based settings:
- Select from the navigation menu. Click Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- Select View details from the Actions drop-down menu for the event-type you want to view. The Event - &lt;event type name&gt; screen is displayed with the event details.

## Edit Event-based Access Reviews

Update the existing event details, as follows:

- Select the navigation menu.
- Click Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Event-Based Setup page, select the event type: Change , Timeline , or Unmatched accounts tab.
- From the Actions menu, select Edit .
- Update the details and select Save .

## Delete Event Type for Access Reviews

As an Administrator , you can delete Timeline or Unmatched Accounts events. You can disable the Change event but cannot delete it.
Delete an existing event type, as follows:

- Select from the navigation menu.
- Click Access Reviews and then Event-Based Setup . The Event-Based Setup landing page is displayed.
- On the Event-Based Setup page, select either Timeline or Unmatched accounts tab.
-
