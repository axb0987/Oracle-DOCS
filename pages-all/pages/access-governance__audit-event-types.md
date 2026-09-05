# Supported Audit Events and Operations in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm
- Fetched: 2026-09-05 03:13 CDT

# Supported Audit Events and Operations in Oracle Access Governance

List of supported audit events for each operation.

## Audit Event Services and Operations

The following audit event services and operations are available in Oracle Access Governance:

Feature Operation Audit Event Type Sample Audit Event
Reset password Create reset password request`com.oracle.idm.agcs.audit.pm-selfservice.createPasswordResetRequest`[Create Reset Password Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__reset-password-request)
Approval Request Create`com.oracle.idm.agcs.audit.approvals.createApprovalProcess`[Create Approval Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__CreateApprovalInstance)
Delete`com.oracle.idm.agcs.audit.pm-selfservice.deletePermissionApprovalRequest`[Delete Permission Approval Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__deletePermissionApprovalRequest)
Complete`com.oracle.idm.agcs.audit.approvals.completeApprovalRequest`[Complete Approval Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__completeApprovalRequest)
Delete`com.oracle.idm.agcs.audit.approvals.deleteInstance`[Delete Approval Request Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__delete-approval-request)
Access Request Create extension request`com.oracle.idm.agcs.audit.pm-selfservice.createExtensionRequest`[Create Extension Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__sample-access-request-ext)
Create access request for identity`com.oracle.idm.agcs.audit.pm-selfservice.createAccessRequest`[Create Access Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__create-access-request)
Action tasks (approve, reject, request information, or provide information) for Access Requests User actions on access requests`com.oracle.idm.agcs.audit.approvals.createTaskActions`[Create Task Actions](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#sample-audit-events__create-task-action)
Approvals for Access Requests External APIs Approve tasks async`com.oracle.idm.agcs.audit.permission-manager-external.createApprovalWorkRequest`
Approve tasks sync`com.oracle.idm.agcs.audit.permission-manager-external.decideApprovals`
List my approval tasks`com.oracle.idm.agcs.audit.permission-manager-external.listMyApprovalTasks`
List approval tasks`com.oracle.idm.agcs.audit.permission-manager-external.listAllApprovalTasks`
Get approval task by id`com.oracle.idm.agcs.audit.permission-manager-external.getApprovalTask`
Get status for async approvals`com.oracle.idm.agcs.audit.permission-manager-external.getApprovalWorkRequest`
Approval Workflows Create`com.oracle.idm.agcs.audit.approvals.createApprovalProcess`
Update`com.oracle.idm.agcs.audit.approvals.updateApprovalProcess`
Delete`com.oracle.idm.agcs.audit.approvals.deleteApprovalProcess`
Access bundles Create`com.oracle.idm.agcs.audit.permission-manager.createAccessBundle`
Update`com.oracle.idm.agcs.audit.permission-manager.updateAccessBundle`
Delete`com.oracle.idm.agcs.audit.permission-manager.deleteAccessBundle`
Roles Create`com.oracle.idm.agcs.audit.permission-manager.createRole`
Update`com.oracle.idm.agcs.audit.permission-manager.updateRole`
Delete`com.oracle.idm.agcs.audit.permission-manager.deleteRole`
Identity collections Create`com.oracle.idm.agcs.audit.identity-collection.createIdentityGroup`
Update`com.oracle.idm.agcs.audit.identity-collection.updateIdentityGroup`
Delete`com.oracle.idm.agcs.audit.identity-collection.deleteIdentityGroup`
Policies Create`com.oracle.idm.agcs.audit.permission-manager.createPermissionAssociation`
Update`com.oracle.idm.agcs.audit.permission-manager.updatePermissionAssociation`
Delete`com.oracle.idm.agcs.audit.permission-manager.deletePolicy`
Guardrails Create`com.oracle.idm.agcs.audit.sod.createAccessGuardrail`
Update`com.oracle.idm.agcs.audit.sod.updateAccessGuardrail`
Delegations Create`com.oracle.idm.agcs.audit.approvals.createDelegation`
Update`com.oracle.idm.agcs.audit.approvals.updateDelegation`
Delete`com.oracle.idm.agcs.audit.approvals.deleteDelegation`
Campaigns Create`com.oracle.idm.agcs.audit.campaign-api.createCampaign`
Update`com.oracle.idm.agcs.audit.campaign-api.updateCampaign`
Delete`com.oracle.idm.agcs.audit.campaign-api.deleteCampaign`
Terminate`com.oracle.idm.agcs.audit.campaign-api.terminateCampaign`
Change owner`com.oracle.idm.agcs.audit.campaign-api.changeOwner`
Access reviews Submit Bulk actions on access reviews`com.oracle.idm.agcs.audit.campaign-api.submit`
Create an access review from EWB (same as Create Campaign)`com.oracle.idm.agcs.audit.campaign-api.createCampaign`
Event-based setup Create`com.oracle.idm.agcs.audit.campaign-api.createEventType`
Update`com.oracle.idm.agcs.audit.campaign-api.updateEventType`
Delete`com.oracle.idm.agcs.audit.campaign-api.deleteEventType`
Manage Permissions Provision retry`com.oracle.idm.agcs.audit.permission-manager.retryAccessBundle`
Revoke`com.oracle.idm.agcs.audit.permission-manager.revokePermission`
Manage Account for Identity Update`com.oracle.idm.agcs.audit.permission-manager.accountUpdate`
Disable/Enable`com.oracle.idm.agcs.audit.permission-manager.accountUpdate`
Delete`com.oracle.idm.agcs.audit.permission-manager.accountUpdate`
Manage AG status Update`com.oracle.idm.agcs.audit.identity-collection.updateActiveGroup`
Manage AG sub type Update`com.oracle.idm.agcs.audit.identity-collection.updateConsumerGroup`
Manage identity Activate`com.oracle.idm.agcs.audit.entity-manager.activateIdentitiesList`
Terminate`com.oracle.idm.agcs.audit.entity-manager.terminateIdentitiesList`
Organizations Create`com.oracle.idm.agcs.audit.identity-collection.createAgOrganization`
Update`com.oracle.idm.agcs.audit.identity-collection.updateAgOrganization`
Delete`com.oracle.idm.agcs.audit.identity-collection.deleteAgOrganization`
Manage inbound transformations Create`com.oracle.idm.agcs.audit.identity-lifecycle.createMappingRule`
Update`com.oracle.idm.agcs.audit.identity-lifecycle.updateTargetMappingRule`
Delete`com.oracle.idm.agcs.audit.identity-lifecycle.deleteTargetMappingRule`
Manage matching rules Update`com.oracle.idm.agcs.audit.identity-lifecycle.updateMatchingRule`
Manage outbound transformations Create`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Update`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Delete`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage access bundle recommendations Accept`com.oracle.idm.agcs.audit.access-bundle-onboarding.acceptRecommendationAccessBundle`
Edit`com.oracle.idm.agcs.audit.access-bundle-onboarding.updateRecommendationAccessBundle`
Reject`com.oracle.idm.agcs.audit.access-bundle-onboarding.rejectRecommendationAccessBundle`
Bulk Accept`com.oracle.idm.agcs.audit.access-bundle-onboarding.createProfileAccessBundleBulk`
Create rec-systems task`com.oracle.idm.agcs.audit.access-bundle-onboarding.createRecommendationTask`
Orchestrated systems Create`com.oracle.idm.agcs.audit.target-management.createTarget`
Manage integration settings`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage notification settings`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage ownership settings`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage data load settings`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage account lifecycle`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Data load now`com.oracle.idm.agcs.audit.target-management.rescheduleNow`
Disable`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Activate`com.oracle.idm.agcs.audit.target-management.patchTargetDetails`
Manage account attributes for orchestrated system Create`com.oracle.idm.agcs.audit.target-management.createTargetEntityAttribute`
Update`com.oracle.idm.agcs.audit.target-management.updateTargetEntityAttribute`
Delete`com.oracle.idm.agcs.audit.target-management.deleteTargetEntityAttribute`
Manage account profiles for orchestrated system Create`com.oracle.idm.agcs.audit.access-bundle-onboarding.createAccountProfile`
Update`com.oracle.idm.agcs.audit.access-bundle-onboarding.updateAccountProfile`
Delete`com.oracle.idm.agcs.audit.access-bundle-onboarding.deleteAccountProfile`
Manage global key values Create`com.oracle.idm.agcs.audit.ingestion-global-lookup.createGlobalCollection`
Update`com.oracle.idm.agcs.audit.ingestion-global-lookup.updateGlobalCollection`
Delete`com.oracle.idm.agcs.audit.ingestion-global-lookup.deleteGlobalCollection`
Data Enablement Manage Settings Save`com.oracle.idm.agcs.audit.data-enablement.saveConfigConnectivityDetails`
Publish Data`com.oracle.idm.agcs.audit.data-enablement.createEnablementOperation`

## Sample Audit Events

Refer a few sample audit event payload for the supported services.

[Create Extension Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Create Access Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Delete Permission Approval Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Create Reset Password Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Create Approval Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Complete Approval Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Delete Approval Request Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Create Task Actions](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Create Approval Work Request](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[Decide Approvals](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[List My Approval Tasks](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```

[List All Approval Tasks](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#)

```

```
