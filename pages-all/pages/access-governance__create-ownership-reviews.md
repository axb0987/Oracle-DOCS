# Create Ownership Review Campaigns
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/create-ownership-reviews.htm
- Fetched: 2026-09-05 03:13 CDT

# Create Ownership Review Campaigns

You can review ownership of resources that are created within Oracle Access Governance by setting up on-demand Ownership Review Campaigns. These can be one-time or periodic review campaigns.

## Navigate to Review Ownership Campaigns

Ownership Campaigns are created from the Oracle Access Governance Console. Choose the Oracle Access Governance system to launch the on-demand ownership review process.

- Sign in to Oracle Access Governance Console.
- Select one of the following options to go to the Campaigns page:
- On the Oracle Access Governance Console home page, select the Access Reviews tab. Select the Define a new campaign tile.
- From the Navigation Menu, select Access Reviews &gt; Campaigns. . From the Campaigns page, select Create a campaign .
- Select the Oracle Access Governance review system, and then select Review ownership .

On the Create a new ownership review campaign workflow page, choose the resources for which you want to run the ownership reviews.

## Select Resources for Ownership Reviews

Select the resources for which you want to review ownership. By default, Oracle Access Governance considers ownership review for all the resources.

- Select the resource tile for which you want to review ownership. Clear the tile that you don't want to include in the review. You can select from:
- Access Bundles
- Approval Workflows
- Identity Collections
- Orchestrated System
- Policies
- Roles
- Access Guardrails
- Campaigns
- Select Next to refine your selection and apply filters in the Add filters step.

At any point of time, select Save draft to save the campaign and pick up later to work on the details.

## Apply Filters to Select Resources

Add filters to refine your selection. You can choose to review the ownership of resources that haven't been reviewed within the selected number of days. You can refine further to choose your specific resources by adding filters. By default, all the available resources are considered for ownership review.

- Add Filter in the Last Reviewed step to select the number of days since the last ownership review.
Example : Choose Over 90 days to include ownership review of resources that haven't been reviewed in the last three months or 90 days.
- Refine your selection in the Selection criteria step.
- Select the Add Filter button.
- Select one of the resources in the What do you want to refine? list.
- Select the search criteria to find your resources. You can search a resource by resource name, primary owner name, last updated, created date, or created by options.
- Select the logical operator of your choice.
- Select the value and click Apply .
- In the Selection filter section
- Select the edit icon to modify the value listed in the applied filter.
- Select the delete icon to remove the filter.
The panel on the right-side of the page shows you the effect of your selection and provides you with an estimate of included resources considered for ownership review. You can also view current filters selected for the campaign.
- Select Next to proceed to the Assign workflow step.

## Add Access Reviewers by Selecting Approval Workflow

In the Assign workflow dimension, you select the approval workflow for your access review.

- Select one of the following approval workflows to assign to the access review campaign.
- Owner , where primary owner of a resource will be assigned as the reviewer. Consider[fallback process](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm)before configuring this workflow.
- Custom User , and then select any active workforce Oracle Access Governance identity as a reviewer.
- After you have selected your workflow, click the View approval workflow link to see a graphical representation of the selected workflow.
- Select the scope of justification required for review decisions. You can select for reviewers to add comments for all the review decisions or keep the justification field as optional.
- Select Next to proceed to the Add details dimension.
At any point of time, select Save draft to save your campaign and pick up later to work on the details.

## Add Owners

You can add primary and secondary owners to the campaigns. For existing campaigns, primary owner is selected as the campaign owner, with no secondary owners.
By default, the resource creator is selected as the resource owner.
- Select an Oracle Access Governance active user in the Who is the primary owner field.
- Select one or more users in the Who else owns it? field. You can add up to 20 additional owners.

The Primary Owner is displayed in the campaign list. All assigned owners can view and manage campaigns they own.

If the primary owner isn't a valid campaign owner, fallback mechanism is auto triggered to assign a new owner. See[Understanding Fallback Mechanism: Methods to Prevent Campaign Termination](https://docs.oracle.com/en-us/iaas/Content/access-governance/libraries/../working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review).

## Add Campaign Details

In the Add details dimension, select campaign schedule cycle, give a meaningful name to your campaign, add a supporting description, and assign values to additional attributes, such as campaign owner, and when the campaign should start or end.
To add details :

- Select an appropriate schedule cycle in the How often do you want this to run? field.
- In What do you want to call this campaign? , enter a unique campaign name.
- In How do you want to describe this campaign , enter campaign description.
- Select one of the following for the Oracle Access Governance and Oracle Identity Governance (OIG) systems:

Option Description
Include account reviews Select this option if you want to include identity access reviews for accounts along with permissions. Clear the check box to exclude account reviews.
Include role reviews Select this option if you want to create identity access reviews for roles along with permissions. Clear the check box to exclude role reviews.
When reviewing permissions, reviews for accounts and roles are included by default. If you exclude both account and role reviews, only permission reviews are generated.
- Based on the schedule cycle selected in Step 1, select the time at which you want to launch the campaign.
- For One-Time, select either Run now or Schedule Later . By default, the campaign is set to begin at the top of the next hour, the following day of campaign creation.
- For campaign series, select the calendar icon and select the start and end date and time for the campaign.
- Once you have set your preferences, select Next to go to the Review and submit dimension.
- (Optional) You may select one of the additional actions:
- Save Draft : To save your changes and later come back and edit the workflow or details.
- Cancel : To cancel the current process.
- Back : To go back to the previous step.

## Review and Submit the Campaign

In the Review and submit dimension, review the campaign details and create the campaign.
To review and submit your campaign :

- Review the campaign information. For any changes, select the Back button.
-
