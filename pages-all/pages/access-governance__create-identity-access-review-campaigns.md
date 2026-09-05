# Create Identity Access Review Campaigns
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm
- Fetched: 2026-09-05 03:13 CDT

# Create Identity Access Review Campaigns

As an Administrator or Campaign Administrator , certify identity accesses by creating on-demand Identity Access Review campaigns from the Oracle Access Governance Console. These can be one-time or periodic access review campaigns.

## Prerequisites

Before you create identity access review campaigns, consider the following:
- To create campaigns for access reviews, you must have Oracle Access Governance Administrator or Campaign Administrator role assigned to you.
- Enable the identity attributes (core and custom), and affiliations, from the Identity Attributes page. For example, you may need to define the campaigns based on Project Code or Cost Center . See[View and Configure Custom Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).
- You must select at least one selection criteria to run Campaigns to avoid significant resource consumption.
- Select the Oracle Access Governance system to run identity access reviews based on the permissions ingested directly from the Orchestrated systems.
- For the Oracle Access Governance system, select permissions assigned directly (`DIRECT`) or Access Bundles granted through request from the Which Permissions? tile. Permissions or accounts provisioned through policy aren't eligible in this review.
- You can't select specific permissions and roles in the same campaign as campaign as Which permissions? and Which roles? are mutually exclusive. This means that you can select either of the two when creating a campaign. However, you can review all the available permissions and roles when you select Who has access? and What are they accessing? .

For more information on Campaigns, see[Best Practices to work with Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#best-practices-to-work-with-campaigns).

## Navigate to Campaigns

Campaigns are created from the Oracle Access Governance Console. Go to Campaigns page to launch the on-demand access review process.

- Log in to the Oracle Access Governance Console.
- Select one of the following options to navigate to the screen:
- On the Oracle Access Governance Console home page, select the Access Reviews tab. Select the Define a new campaign tile.
- From the Navigation Menu , select Access Reviews , and then Campaigns . From the Campaigns page, select Create a campaign .
- Select one of the system types for which you want to run Campaigns. For more information, see[Eligible System Types to Launch Access Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#types-of-access-certifications).
On the Create a new access review campaign workflow page, define the selection criteria for your campaign.

## Select Criteria for your Access Reviews

In the Selection criteria dimension, you select appropriate criteria for your Identity Access Review Campaigns. The attributes configured in the Identity Attributes page are available as the selection criteria. All criteria can be searched by name .
The selection tiles are based on the system selected in the previous step. For example, for Oracle Cloud Infrastructure (OCI), you may see additional tiles, like Which tenancies? so that you can select your cloud account for which you want to run review.

- Select one or more criteria tiles that you wish to include in any order. You don't need to update each criteria. The selection values are derived from the integrated orchestrated system. Available tiles are:

Option Description
Who has access? To filter identities based on core or custom identity attributes.
- Select up to five attributes in the Which attributes do you want to add for selection? field.
- From each tab, select one or more available selection values.
What are they accessing? Select identities based on their access to applications or resources.
Which permissions? To select identities based on their access to permissions.
- For Oracle Identity Governance (OIG), you can select entitlements.
- For Oracle Access Governance, you can select permissions assigned directly in the Managed System or permissions provisioned through Access Bundle through Request within Oracle Access Governance . The permissions vary based on the orchestrated system.
- For OCI, you can review OCI IAM Groups and Application Roles assigned through Access Bundle via Request within Oracle Access Governance.
Which roles? To filter identities based on their roles.
- For Oracle Identity Governance (OIG), you can select directly assigned roles.
- For Oracle Access Governance, you can select roles assigned directly in the Managed System or created within Oracle Access Governance.
- For Oracle Cloud Infrastructure (OCI), you can review OCI Cloud services application roles assigned directly in OCI.
Which tenancies? To filter cloud account. Select the Refine further link to select compartment and domain for your cloud account. Available only for Oracle Cloud Infrastructure review system.
Use filter to select the relevant values. For example, for Oracle Access Governance scope, in the Which permissions? tile, select Access Bundle as the Granted Permission type , and set Limited as the Access Time Limit to review access bundles with a time-bound access. For Oracle Cloud Infrastructure (OCI), in the Access Time Limit list , select Limited .
- After selection, select Apply my selections .
- To update your selection criteria, select the Modify button on the relevant tile.
The panel on the right-side of the page shows you the effect of your selection and provides you with an estimate of included identities considered for review.
- Once you've made your selection, select I'm good, go to workflows button to proceed to the Assign workflow dimension.
At any point of time, select Save draft to save your campaign and pick up later to work on the details.

## Add Access Reviewers by Selecting Approval Workflow

In the Assign Workflow dimension, you select the approval workflow for your access review.

- Select which approval workflow you want to assign to this access review campaign.
A list of the available workflows shows all approval workflows defined in your system. Consider[Self Certification Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#self-certification-guardrails)and[Fallback Mechanism](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review)before selecting the workflow. For details on how to create and manage approval workflows see[Create Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm)and[Manage Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approval-workflow.htm).
- After you have selected the workflow, click the View approval workflow link to see a graphical representation of the selected workflow.

Note  
  
If a campaign uses a Business Approvers workflow, the review is assigned to the resource owner. For example, Access Bundle reviews are assigned to the Access Bundle primary owner, role reviews to the Access Governance role primary owner, OIG permission reviews to the permission owner, and OIG Role reviews to the role owner ingested from the orchestrated system. If the primary owner isn't a valid resource owner, fallback mechanism is auto triggered to assign a new owner. See[Understanding Fallback Mechanism: Methods to Prevent Campaign Termination](https://docs.oracle.com/en-us/iaas/Content/access-governance/working-with-access-review-campaigns.htm#fallback-mechanism-in-access-review).
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

In the Add details dimension, select campaign schedule cycle, give a meaningful name to your campaign, add a supporting description, and assign values to additional attributes, such as primary and secondary owner, and when the campaign must start or end.
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
- Select Next to go to the Review and submit dimension.
- (Optional) Select one of the additional actions:
- Save Draft : To save the changes and later come back and edit the workflow or details.
- Cancel : To cancel the current process.
- Back : To go back to the previous step.

## Review and Submit the Campaign

In the Review and submit dimension, review the campaign details and create the campaign.
To review and submit the campaign :

- Review the campaign information. For any changes, select the Back button.
-
