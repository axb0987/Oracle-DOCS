# Manage and Monitor Access Review Campaigns
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-review-campaigns.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage and Monitor Access Review Campaigns

Users with the Administrator application roles can manage and monitor all types of access review campaigns using the Oracle Access Governance Console.

Users with the following Oracle Access Governance roles can access these:
- Administrator : Can manage and monitor all campaigns in the Oracle Access Governance Console.
- Campaign Administrator : Can manage and monitor campaigns that they have created.
- Auditor : Can monitor all campaigns in Oracle Access Governance.
- Campaign Owner (User) : Can manage and monitor the campaigns that they own.

## Search and Apply Filters to View Available Campaigns

You can retrieve campaign by performing keyword search or applying filters based on campaign status. You can apply suggested filters to view focused information.
Primary/Secondary owners can only view the campaigns that they own, and not all the available campaigns.

- Log on to the Oracle Access Governance Console with a user assigned either the Administrator or Campaign Administrator application role.
- Select one of the following options to navigate to the Campaigns page:
- On the console home page, select the Access Reviews tab and then select one of the following options.
- To view in In progress or Ready for Approval campaigns, select the Show me my &lt;number&gt; ongoing campaigns tile.
- To view Ready for Approval campaigns, select the &lt;number&gt; campaigns are ready for approval tile.
- To view all campaigns, select the Show me all campaigns tile.
- Click the icon &gt; Access Reviews &gt; Campaigns .
- For keyword search, type campaign name in the Search field and press Enter on your keyboard.
- To view focused results, select one or more suggested filters available directly under the Search field.
- To apply filters based on campaign status, use the drop-down menu in the top-right corner of the page. Select one from the following:
- My ongoing campaigns : Displays campaigns with a Status of In progress or Ready for approval .
- My upcoming campaigns : Displays campaigns with a Status of Scheduled or Draft .
- My previous campaigns : Displays campaigns with a Status of Approved , System ended or Terminated .
- All campaigns : Displays all available campaigns.

## View Campaign Details

View campaign details to see the campaign description, selection criteria, review process, included identities or access control items considered for review, approval workflow, or perform additional actions on the campaign.

The information displayed and applicable actions vary based on the campaign state. Here's how you can view campaign details:

- Go to the Campaigns page
- For the campaign, select the corresponding Menu icon, and then select View campaign details .

## View Pending Access Review Tasks

For an In Progress campaign, view the details of pending access review tasks.
- Go to the Campaigns page.
- For the campaign, select the corresponding Menu icon, and then select View campaign details .
- On the View Campaign Details page, select the View pending review tasks link. The default filter, Review status Pending shows all the pending review tasks for the campaign.

### Reassign Pending Access Review Tasks

You can reassign pending review tasks to another reviewer, who isn't a beneficiary. For more information, see[Reassigning a Review Task](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#reassigning-a-review-task).

- On the View Campaign Details page:
- Select the checkbox at the row-level and then select the Reassign button.
- For each review task, select the reassign icon to reassign the access.
- In the Confirmation pop-up window, select the reviewer to whom you want to reassign.
- Enter the justification for reassignment, and then select Submit . A confirmation message is displayed.

### Download Pending Access Review Tasks
You can download CSV file to view a pending list of review tasks.
- On the View Campaign Details page, select the select CSV button.
- In the Download CSV data pop-up window, select the Download button.

## Edit an Access Review Campaign

You can edit a Draft or Scheduled campaign before it is launched to modify the details. You can edit the selection criteria, workflow and reviewer details, campaign details, and schedule of campaign. You can change campaign ownership for an ongoing campaign In Progress or Ready For Approval campaigns.

- Go to the Campaigns page
- For the campaign that you want to edit, select the corresponding Menu icon, and then select Edit .
The Edit campaign page provides the same guided workflow for entering your campaign parameters as the Create campaign page.
- On the Review and submit step, select Update . Select Back to edit values, or Cancel to discard the changes.

## Change Ownership for Campaigns

You can associate campaign ownership by adding primary and secondary owners as additional owners.
By default, the resource creator is selected as the resource owner. You can assign one primary owner and up to 20 additional owners for a campaign. For existing campaigns, campaign owner would be selected as the campaign owner, with no secondary owners.
- Go to the Campaigns page.
- For the campaign, select the corresponding Menu icon, and then select Change ownership .
- Select an Oracle Access Governance active user in the Who is the primary owner field.
- Select one or more users in the Who else owns it? field. You can add up to 20 additional owners.

The Primary Owner is displayed in the campaign list. All assigned owners can view and manage campaigns they own.

If the primary owner isn't a valid campaign owner, fallback mechanism is auto triggered to assign a new owner. See[Understanding Fallback Mechanism: Methods to Prevent Campaign Termination](https://docs.oracle.com/en-us/iaas/Content/access-governance/libraries/../working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)

## Clone a Campaign

To generate similar access reviews, you can clone an existing campaign. The cloned campaign uses the existing access review criteria. However, you can modify the campaign details, primary/secondary owner, or assign a new approval workflow.
Here's how you can clone an existing campaign:

- Select one of the following options to clone a campaign:or from the Actions menu on the campaign detail page
- On the Campaigns page, from the list, select Menu icon, and then select Clone corresponding to the campaign that you want to clone.
- On the Campaigns detail page, from the Actions menu, select Clone
- Select the Clone task to make a clone of the current access review campaign. You are taken to the Clone campaign page.
- On the Clone campaign page, enter the following information
- How often do you want this to run? : Select One time to run a single occurrence of this campaign, or select a recurring pattern like Quarterly , Monthly , Half-Yearly , or Yearly to run this access review campaign periodically.
- What do you want to call this campaign? : Provide a name for the cloned campaign.
- How do you want to describe this campaign? : Provide a description for the cloned campaign.
- Who is the primary owner? : Select an Oracle Access Governance active user.
- Who else owns it? : Select one or more users as secondary owners for this campaign. You can select up to 20 secondary owners.
- How would you like to schedule your campaign? : You can view this field only if you have selected to run your campaign one time. Select either Run now or Schedule Later . By default, the campaign is set to begin at the upcoming next hour, the following day of campaign creation.
- When do you want to Begin? : If you have set a recurring pattern, then select the start date of when you want to begin the campaign series. By default, the campaign is set to begin at the top of the next hour, the following day of campaign creation. If you want to change this, select the Select Date Time icon and add a new date/time.
- When do you want to End? : If you have set a recurring pattern, then select the end date of when you want to end the campaign series.
- Which approval workflow should be used? : Select the approval workflow that you want to assign to this access review campaign. For details on how to create and manage approval workflows see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm).
- When you have set your clone preferences, select Create to clone the current campaign.
(Optional) To save your changes and later come back and edit the workflow or details, select Save as draft , or to cancel the current process, select Cancel .

## Approve a Campaign

When the review tasks have been completed or the campaign due date has elapsed, the campaign moves to the Ready for Approval state. You can then Approve the campaign, and close the review process.

- Go to the Campaigns page
- For the campaign that you wish to approve, select the corresponding Menu icon, and then select Approve .
You will see a confirmation message stating that the campaign has been approved. You can view the approved campaigns in the my previous campaigns or All campaigns category.

## Terminate a Campaign

You can terminate a scheduled campaign at any point of time until a campaign is approved or system ended. For a periodic campaign, you can cancel all the ongoing (currently running) and upcoming (scheduled in future dates) access reviews campaigns for that series.

- Select the Terminate task to terminate the current access review campaign.
- On the Confirmation pop up dialog, select Terminate to end the campaign.
- If you have a periodic campaign, and want to terminate entire series, select Terminate Series .
For Draft campaigns, you can Delete the campaign.

## Delete a Campaign

You can delete Draft , Approved , System Ended , and Terminated campaigns.

- Select All campaigns from the upper right list.
- Select the appropriate suggested filters to see the campaign.
- For a campaign. select the corresponding Menu icon, and then select Delete .
- On the Confirmation pop up dialog, select Delete to end the campaign.
After deletion, the campaign records are permanently deleted, including campaign details, its review tasks, decisions, and related audit trail records. You can't view the review tasks on the Access Review page or any trail of reviews in the Audit Trail section.

## View and Download Access Review Reports

Once the campaign is launched, you can view and download access review report for each campaign. In addition to viewing report, you can also save the reports offline in PDF format or download the CSV data for record-keeping or further analysis or audit.
You see a report displaying access review details and a breakdown of pending, approved, or revoked access review decisions for user role, user account and permission.
- For identity access reviews, you see the bifurcation of the review decisions based on top five organization, source organization, roles, and applications.
- For access control reviews, you see a breakdown of pending, approved, revoked, or modified access review decisions along with grouping of top five created since date ranges for identity collections or policies.

For example, if you have an identity review campaign setup that impacts applications and different roles, you should see the report displaying the top five applications and top five roles for which these access reviews are generated.

- Go to the Campaigns page
- For a campaign that you wish to view report, select the corresponding Menu icon, and then select View report .
- If you want to retain a copy of the report, select Download &lt;certification type&gt; PDF , else select Close to return to the campaign.
- To download CSV data:
- Select Download CSV data to generate a comma-separated values file with data for the campaign.
-
