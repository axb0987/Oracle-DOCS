# Create an Identity Collection
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm
- Fetched: 2026-09-05 03:13 CDT

# Create an Identity Collection

Identity Collections are groups of identities based on shared attributes or named identities. Identity collections comprise identities that have been on boarded from integrated systems using identity orchestration.

Identity Collections simplify tasks by allowing you to configure features for a collection of identities, rather than for each individual identity. You can use Identity Collections to
- Associate identities with appropriate access bundles or roles using policies.
- Delegate Access Review tasks to an Identity Collection.
- Assign as approvers in Approval Workflows.

## Navigate to Identity Collections

Here's how you can access the Identity Collections page:
- Sign in to the Oracle Access Governance Console .
- Click the icon, and select Access Controls and then Identity Collections . You will see the Identity Collections page where you can view and manage existing identity collections, or create new ones.
- To create a new identity collection, click the Create an identity collection button.

The Create a new identity collection page is displayed.

## Add Details

In the Add Details task, you can enter specifics about your identity collection. Here, you can give a meaningful name to your identity collection and add its supporting description.

Note  
  
By default, all identities enabled in the[License Management](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)service, can utilize all identity data attributes, including custom attributes, to create identity collections.

- Enter a name for your identity collection in the Name field.
- Add a description for your identity collection in the Description field.
- Add one or more tags to identify or search your identity collection.
- Add any access guardrail that you want to associate with this identity collection in the Select an access guardrail required for membership to be allowed .
- Select appropriate approval workflow to ensure all revisions (update or delete) to this identity collection are reviewed before implementation. By default, No Approval Required is selected. See[Revision Management in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm).
- Once you have set your preferences, select Next to go to the Add system step.
- (Optional) You may click Cancel to cancel the current process.

## Add system

The Add system task will display if you have at least one orchestrated system, in your enterprise, where you have selected to manage identities. This option allows you to select whether the identity collection you are creating will manage a group on the orchestrated system or not.

- Select Yes or No in response to the question Will this identity collection manage a group on a system? field.
- If your answer is No then this identity collection will not manage group for the system and you can select Next to go to the Add owners step. If your answer is Yes , then this identity collection will manage a group on a system, and you should complete the steps which follow.
- On selecting Yes , you will be prompted to identify a system for which the identity collection will manage a group. Select Add system . In the Add system panel, select the system name from the drop-down list. The selected (new or existing) group in this system will be managed by this identity collection.
- Complete the group details for the system. The details required will depend on the system type selected.
Check the Manage existing group check box if you want to create the identity collection from an existing group in the system. If you select this option then there is no requirement to enter the group details.
- Complete the account details for the system. The details required will depend on the system type selected.
- Click Save to save the group details of the system.
- Click Next to progress to identity selection, Save draft to save this as a draft identity collection, or Cancel to cancel the current process.

## Add Primary and Additional Owners

You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
For assigning resource ownership, you must have active Oracle Access Governance users. When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section.
No special application roles are necessary for assigning resource ownership. Any Oracle Access Governance active user can be assigned as the owner of the resources. All the owners can read, update, or delete the resources that they own. However, the Primary Owner is assigned as the access reviewer when you choose the Owner template in the approval workflow for performing Ownership reviews in Campaigns. For more information, refer[Types of Access Reviews Offered by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#types-of-access-certifications).

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Ownership settings tile. This will display the Ownership settings page for the selected orchestrated system.
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource.
You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

## Select Identities

In the Select Identities task, you have to select identities for your identity collection.
You can select identities based on:
- Membership rule : Set criteria based on certain conditional statements. Either one ( Any ) or all ( All ) the set conditions must be satisfied. The list of available attributes is determined by the data ingested from the orchestrated systems.
- Named identities : Search and select one or more users by their full name that you want to include in your identity collection. The list of available users is determined by the data ingested from the orchestrated systems.
- Both Membership rule and Named identities : You can have a combination of both membership rule and named identities to set criteria for your identity collection.
Note  
  
You can also exclude specific members from your identity collection, by selecting Manage exclusions and entering the identities you want to exclude.

### Add Identities based on Membership Rule

To add identities based on conditional statements, select the Membership rule tab. The identities satisfying the set criteria will automatically be included in that identity collection. For example, for an identity collection, if you set the conditional rule to Department Equals Finance , then all the human identities belonging to the Finance department will be included in that identity collection.

To set the conditional rule for identities, do the following:
- Select Any if any one of the set conditions should be satisfied, or select All if all the set conditions must be satisfied for that identity.
- Select the attribute name from the list
Note  
  
Based on the orchestrated systems, you can select both core and/or custom attributes. To enable custom attributes, see[View and Configure Custom Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings)
- Select the conditional operator. Based on the data type of the attribute selected, the usage of these operators will vary.
- Type the attribute value.
- Continue to add the conditional statements or rules for more attributes.

By default all the identities matching the criteria will be included.
- 

However, you can exclude certain identities from your conditional statements. Click the Manage Exclusions button next to Excluding # identity from the attribute conditions and then select the identities that you want to exclude from the identity collection.

As you set the conditions or add identities, you can see the effect on the right-side of the screen of which identities are excluded and the applied membership rule.
- Once you have set your preferences, select Next to go to the Review and submit step. You may select one of the additional actions:
- Save as draft : To save your changes and later come back and edit the identities.
- Cancel : To cancel the current process.
- Back : To go back to the previous step.

### Add Identities based on Named Identities

To directly add identities based on their full name, select the Included named identities tab.

All the available active identities (configured from the[Licence Management](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)page) will be displayed. In the user tile, you can view user details, such as full name, email address, organization name. Search or select one or more user tile that you want to include in your identity collection. As you select the identities, you can see the effect on the right-side of the screen of which identities are included. Once you have set your preferences, select Next to go to the Review and submit step.

## Review and Submit

The Review and Submit step displays the information you have added in the previous steps.
You can see the preview of your identity collection. For this, click the preview the identity collection link available on the right-side of the page. If you are satisfied with your identity collection preview, click Create . You may select addition actions:
- Save as draft : to save your changes and edit the identity collection later.
- Cancel : To cancel the process.
-
