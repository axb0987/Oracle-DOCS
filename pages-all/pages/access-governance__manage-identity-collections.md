# Manage Identity Collections
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-collections.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Identity Collections

Oracle Access Governance users can view and manage identity collections from the Oracle Access Governance Console.

## View and Search Identity Collections

You can view existing identity collections and manage the ones that you created, or are authorized to manage, using the Oracle Access Governance Console.

Follow the steps to navigate to the Identity Collections page:
- Sign in to the Oracle Access Governance Console with appropriate user role.
- Click the icon, and select Access Controls and then Identity Collections . You will see the Identity Collections page where you can view and manage existing identity collections.

Here, you can see the count of existing identity collections and see the identity collections summary in the grid format, that includes:

Use the Actions menu icon to Edit , Delete , View revision request , Cancel revision request , or View details of the identity collection. Owners of identity collection or authorized users (selected while creating/modifying an identity collection) can edit or delete the identity collection.

### Search and Filter Identity Collections
You can use the Search field to locate the required identity collection by its name. You can narrow down the results by applying suggested filters:
- Updated Last Month : You can view all the identity collections that were updated within the last month.
- Updated Last Week : You can view all the identity collections that were updated within the last week.
- Created by Me : You can view the identity collections that you have created.
- Status Draft : You can view the identity collections that aren't active and are in the draft state.
- Status Active : You can view the identity collections that have been created and can be used within Oracle Access Governance.
- Status In Progress : Identity collections that is not yet active and identity collection members are not yt finalized. It can be due to associated access guardrail.
- Status Failed : Identity collections that failed due to some internal system error
- Revision Pending Yes : For in-progress or pending revisions awaiting approval decision or additional information.
- Revision Pending No : Resources with no revision requests or all previous revision requests have been reviewed and completed.

You can limit the scope of the identity collections displayed by selecting the scope list of values, located in the top right of the Identity Collections page. The default value for scope is All which displays all Identity Collections. Select Managed for systems to restrict the scope of the identity collections displayed to those which manage groups for a system.

## Edit Identity Collections

The Edit an Identity Collection page provides the same guided tasks as you see while creating a new identity collection. You cannot edit an identity collection with an in progress or pending revision status. Owner of the identity collection and/or authorized users can modify its description, owners, associate access guardrails, add named identities, or update membership rules.
To do so:
- Click the Actions menu icon corresponding to the identity collection that you want to modify, and then select Edit .
- On the Review and submit step:
- With no revision approval workflow, select Update to update the identity collection.
- With revision approval workflow, select Publish to send revisions for approval.
- (Optional) Select Back to edit values, or select Cancel to discard your changes.
Note  
  
If approval is required, resource updates are implemented only after approval.

## Delete Identity Collections

You can delete an identity collection as long as it is not associated with any delegation. You cannot delete an identity collection with an in progress or pending revision status. If you are the owner of the identity collection or you have been given the rights by the identity collection creator, then you can delete the identity collection.

- Click the Actions menu icon corresponding to the identity collection that you want to delete, and then select Delete .
- On the confirmation pop-up, click Delete to remove the identity collection.
Note  
  
If approval is required, resource deletion is implemented only after approval.
- (Optional) Click Cancel to retain the identity collection.

## View Details for an Identity Collection

You can view identity collection creation details, member details and its association.
- Click the Actions menu icon corresponding to the identity collection that you want to view, and then select View details .
You will see the following details:
- Insights based on membership rules or size.
- Revision approval workflow, owner, associated access guardrail, description of the identity collection.
- Break up of identities in the collection that are included either through Membership rule or directly through Included named identities .
- If you have created an identity collection through Membership rule , you can see all the rules that helped to create the collection.
- If you have excluded an identity in the collection, you can see a list of excluded member(s).
- If you have created an identity collection directly using named identities, you can see a list included member(s).

### Actions
On the resource details page, use the Actions button to perform the following actions:
- Manage system groups : To add, edit or delete system groups managed by the identity collection
- Edit : Edit an identity collection. You cannot edit an identity collection with an in progress or pending revision status.
- Delete : Delete an identity collection. You cannot delete with an in progress or pending revision status.
- View revision history : To view all active versions of a resource, including those that are created, modified, requested, remediated, approved, or rejected.
- View approval workflow : Applicable only for pending revisions to view the applicable workflow for the resource revision.
- View revision request : To view revision information organized in three tabs, detailing summary of changes, request trail of resource revisions, resource details, and currently implemented changes. Applicable only for pending revisions
- Cancel revision request : Applicable only for pending revisions to cancel the currently requested revision for the resource

## View Revision Request

For Revision requested , Info Requested or Delete Requested revision status, you can view revision request details. You won't see this option for resources with no or completed revisions, having Revision status as None .
- On the Identity Collections page, click the icon and select View revision request . For more information, see[View Revision Request Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm#revision-revision-request-details).

### Cancel revision request

As an owner of an identity collection, you can cancel a revision before its approval decision.
-
