# Revision Management in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm
- Fetched: 2026-09-05 03:16 CDT

# Revision Management in Oracle Access Governance

Revision Management refers to initiating, tracking, reviewing, and implementing changes to key resources in Oracle Access Governance. With revision management, all changes are tracked, reviewed, and approved before being implemented, providing both security and transparency for resource management.

## Overview

Revision Management allows users to initiate, review, approve, and track resource revisions before the changes are implemented.

Revision Management helps enterprises:
- Review the impact of changes
- Safeguard against unauthorized or erroneous changes
- Maintain comprehensive history of changes

Applies to :[Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm#identity-collections-adddetails),[Consumer Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#select-consumer-users),[Active Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#select-identities-for-activation), and[Organizations](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#create-and-manage-organizations).

## Revision Status

Each revision follows a defined lifecycle, represented by different statuses:
- None : No revision has been requested or active revisions exist.
- Revision requested : Revisions awaiting review and approval.
- Info Requested : Reviewers require more information before a decision can be made.
- Delete Requested : Resource deletion has been requested and awaiting review and approval.
- You can’t create new access or ownership reviews for identity collections that are pending deletion, and they will not be available for selection on the Campaigns page. For more information, see[Create Identity Collection Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collection-review-campaigns.htm)and[Create Ownership Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-ownership-reviews.htm).
- Approved : The revision is approved and be applied as the current version.
- Rejected : The revision was rejected at an approval stage.
- Cancelled : The revision was withdrawn before its completion.

When an identity collection is updated or deleted, related access review tasks are automatically auto-canceled. Any remediation requests with pending revisions are automatically rejected.

## Viewing Revision Request Details

When reviewing a revision request or viewing revision details, you can see revision information organized in three tabs, detailing summary of changes, approval request trail of resource revisions, resource details, and currently implemented changes.

This action is available only for pending revisions.

- Revision Summary

The Revision summary tab provides the high-level overview of changes (inclusions or exclusions) requested for a resource. It also includes the approval request trail of resource revisions completed for the resource.
- Revision Details

The Revision details tab provides preview of all the elements of the resource as they’ll look if the revision is approved. Key information, such as Name, Description, Primary Owner, Tags, Revision approval workflow. This tab ensures stakeholders have all necessary specifics to evaluate the revision fully.
- Current Details

The Current details tab provides the view of the resource elements for the current active revision. This allows reviewers to compare current implementation with the proposed changes.
To view revision request for a resource,
- Click the More menu icon corresponding to the resource and then select View revision request .

## Resource Revision History

All active versions of a resource, including those that are created, modified, requested, remediated, approved, or rejected, are preserved as Revision History. Revisions are retained for a maximum of 30 days . Administrators and resource owners can access the revision history from resource's details page.

- On the left pane, you'll see all previous versions of a resource.
- On the right pane, you can see revision summary providing overview of the changes made to the resource, displaying inclusions and exclusions of changes, and showing approval trail for each revision.
- On the right pane, you can see revision details of the resource after a revision. It displays resource details as they appear following the changes are made in that specific revision.
To view revision history for a resource,
- Click the More menu icon corresponding to the resource that you want to view, and then select View details .
- From the Actions list, select View revision history .

## Notification Service

The requestor and their manager receives approval status over email for a revision request.
You can customize email content (body and subject). Use the following templates for revision management.

Template name Description
Approval status of revision request for Active and consumer identities Send email notification to requestor and their manager to receive approval status over email for a revision request for Active Identities and Consumer Identities.
Approval status of revision request for IC and Organizations Send email notification to for requestor and their manager to receive approval status over email for a revision request for Identity Collections and Organizations revisions.
Approval Assignment Revision Sends an email notification to the approver to review and take action on a new revision request.
Approval Escalation Revision Send escalation email notification to escalated approver or group to take action on a pending revision request. For more details, see[Configure Notification Types](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm#configure-notification-types)
