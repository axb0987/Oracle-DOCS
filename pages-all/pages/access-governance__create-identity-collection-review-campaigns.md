# Certify Group Memberships with Identity Collections Review Campaigns
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collection-review-campaigns.htm
- Fetched: 2026-09-05 03:13 CDT

# Certify Group Memberships with Identity Collections Review Campaigns

As an Administrator or Campaign Administrator , certify group memberships by creating on-demand Identity Collections Review campaigns from the Oracle Access Governance Console. These can be one-time or periodic policy review campaigns.

Currently, you can certify group membership for systems managed by Oracle Cloud Infrastructure (OCI) and Oracle Access Governance. If you select to review OCI IAM groups and it contains a few members provisioned from Oracle Access Governance, then with this review, you can only accept or revoke directly assigned members. For members provisioned from Oracle Access Governance, choose to review the OCI Access Bundles using the Which permissions? tile.

## Navigate to Campaigns

Campaigns are created from the Oracle Access Governance Console. Go to Campaigns page to launch the on-demand access review process.

- Sign in to the Oracle Access Governance Console.
- Select one of the following options to navigate to the screen:
- On the Oracle Access Governance Console home page, select the Access Reviews tab. Select the Define a new campaign tile.
- From the Navigation Menu , select Access Reviews , and then Campaigns . From the Campaigns page, select Create a campaign .
- Select one of the system types for which you want to run Campaigns. For more information, see[Eligible System Types to Launch Access Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#types-of-access-certifications).
On the Create a new access review campaign workflow page, define the selection criteria for your campaign.

## Select Criteria for Access Reviews

In the Selection criteria dimension, you select appropriate criteria for your Policy Review Campaigns. All criteria can be searched by name .
Currently, you can certify group membership for systems managed by Oracle Cloud Infrastructure (OCI) and Oracle Access Governance. In one campaign, you can certify membership either for OCI groups or for Identity collections created within Oracle Access Governance. You can't combine two different types of groups in one campaign.

- Select one or more criteria tiles to include in any order. You don't need to update each criteria. The selection values are derived from the integrated orchestrated system. Available tiles are:

Option Description
Which tenancies? To filter and select cloud account. Select the Refine further link to select compartment and domain for your cloud account. Available only for Oracle Cloud Infrastructure (OCI) system.
Which identity collections? To filter and select identity collections for which you wish to review the group membership. You can search specific policy by its name or add filters on policy's creation date to limit the scope of your search results.
- After selection, select Apply my selections .
- To update your selection criteria, select the Modify button on the relevant tile.
The panel on the right-side of the page shows you the effect of your selection and provides you with an estimate of included policies considered for review.
- Once you've made your selection, select I'm good, go to workflows button to proceed to the Assign workflow dimension.

## Add Access Reviewers by Selecting Approval Workflow

In the Assign Workflow dimension, you select the approval workflow for your access review.

- Select which approval workflow you want to assign to this access review campaign.
A list of the available workflows shows all approval workflows defined in your system. Consider[Self Certification Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#self-certification-guardrails)and[Fallback Mechanism](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before selecting the workflow. For details on how to create and manage approval workflows see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm).
- After you have selected your workflow, click the View approval workflow link to see a graphical representation of the selected workflow.
- Select the scope of justification required for review decisions. You can select for reviewers to add comments for all the review decisions, for revoke decisions only, or keep the justification field as optional.
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
- In the Who owns this campaign? field, select campaign owner.
Consider[Self Certification Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#self-certification-guardrails)and[Fallback Mechanism](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before assigning the campaign owner.
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
