# Lockbox Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#dcoc-content-body)

## Lockbox Common Types

### DBMS_CLOUD_OCI_LOCKBOX_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_T Type

Defined by partner while creating a lockbox. These attributes provides context for creating access request

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the context attribute

`description`

(optional) The description of the context attribute

`default_value`

(optional) An optional default value used when access request context value is not provided

`l_values`

(optional) List of context attribute values.

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_TBL Type

Nested table type of dbms_cloud_oci_lockbox_access_context_attribute_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_COLLECTION_T Type

Contains context attribute entries defined while creating or updating a lockbox.

Syntax
```

```

Fields

Field Description

`items`

(required) List of context attributes.

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_MATERIALS_T Type

Access materials details.

Syntax
```

```

Fields

Field Description

`details`

(required) The contents of the material. This is a map that contains the various fields needed for access.

### DBMS_CLOUD_OCI_LOCKBOX_ACTIVITY_LOG_T Type

The log of the action taken by different persona on the access request, e.g. approve/deny/revoke

Syntax
```

```

Fields

Field Description

`user_id`

(optional) User OCID of the persona

`user_level`

(optional) Level of the persona

Allowed values are: 'LEVEL1', 'LEVEL2', 'LEVEL3', 'ADMIN', 'OPERATOR'

`action`

(optional) The action take by persona

Allowed values are: 'APPROVE', 'DENY', 'REVOKE', 'CANCEL'

`message`

(optional) The action justification or details.

`time_updated`

(optional) The time the action was taken. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_LOCKBOX_ACTIVITY_LOG_TBL Type

Nested table type of dbms_cloud_oci_lockbox_activity_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_T Type

An access request to a customer's resource. An access request is a subsidiary resource of the Lockbox entity.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the access request, which can't be changed after creation.

`lockbox_id`

(required) The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.

`display_name`

(required) The name of the access request.

`description`

(required) The rationale for requesting the access request and any other related details..

`requestor_id`

(required) The unique identifier of the requestor.

`lifecycle_state`

(required) Possible access request lifecycle states.

Allowed values are: 'IN_PROGRESS', 'WAITING', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'FAILED'

`lifecycle_state_details`

(required) Details of access request lifecycle state.

Allowed values are: 'PROCESSING', 'WAITING_FOR_APPROVALS', 'APPROVED', 'AUTO_APPROVED', 'CANCELLING_ACCESS', 'EXPIRED', 'REVOKED', 'DENIED', 'ERROR'

`access_duration`

(required) The maximum amount of time operator has access to associated resources.

`context`

(optional) The context object containing the access request specific details.

`activity_logs`

(required) The actions taken by different persona on the access request, e.g. approve/deny/revoke

`time_created`

(required) The time the access request was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(required) The time the access request was last updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_expired`

(required) The time the access request expired. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_reminded`

(required) The time the access request was last reminded. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`reminder_count`

(required) The count of times the access request was reminded.

`requestor_location`

(required) The location of the requestor. Format with be two letters indicatiog operator's country code defined by https://jira-sd.mc1.oracleiaas.com/browse/SSD-17880 Example: `US`

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_SUMMARY_T Type

Summary information for an access request.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the access request, which can't be changed after creation.

`lockbox_id`

(required) The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.

`display_name`

(required) The name of the access request.

`description`

(required) The rationale for requesting the access request.

`requestor_id`

(required) The unique identifier of the requestor.

`requestor_location`

(optional) The two-char country code of the requestor while creating the access request Example: `US`

`lifecycle_state`

(required) The current state of the access request.

`access_duration`

(optional) The maximum amount of time operator has access to associated resources.

`time_created`

(required) The time the access request was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(required) The time the access request was last updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_expired`

(required) The time the access request expired. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_lockbox_access_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_COLLECTION_T Type

Results of access request search. Contains both AccessRequestSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of AccessRequestSummary.

### DBMS_CLOUD_OCI_LOCKBOX_APPROVER_INFO_T Type

The approver data for this approver level.

Syntax
```

```

Fields

Field Description

`approver_type`

(required) The approver type of this approver level.

Allowed values are: 'GROUP', 'USER'

`approver_id`

(required) The group or user ocid of the approver for this approver level.

### DBMS_CLOUD_OCI_LOCKBOX_APPROVER_LEVELS_T Type

The approver levels.

Syntax
```

```

Fields

Field Description

`level1`

(required)

`level2`

(optional)

`level3`

(optional)

### DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_T Type

Group/User OCIDs of those who can approve/deny/revoke operator's request to access associated resources.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the approval template, which can't be changed after creation.

`display_name`

(required) The approval template display name.

`lifecycle_state`

(optional) The current state of the approval template.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`approver_levels`

(optional)

`compartment_id`

(required) The unique identifier (OCID) of the customer compartment where the approval template is located.

`auto_approval_state`

(optional) The auto approval state of the lockbox.

Allowed values are: 'ENABLED', 'DISABLED'

`time_created`

(required) The time the the approval template was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the approval template was updated. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_SUMMARY_T Type

Summary info for an approval tmeplate.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the approval template, which can't be changed after creation.

`display_name`

(required) The approval template display name.

`lifecycle_state`

(optional) The current state of the approval template.

`approver_levels`

(optional)

`compartment_id`

(required) The unique identifier (OCID) of the customer compartment where the approval template is located.

`auto_approval_state`

(optional) The auto approval state of the lockbox.

Allowed values are: 'ENABLED', 'DISABLED'

`time_created`

(required) The time the the approval template was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the approval template was updated. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_lockbox_approval_template_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_COLLECTION_T Type

Results of approval template search. Contains both ApprovalTemplateSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ApprovalTemplateSummary.

### DBMS_CLOUD_OCI_LOCKBOX_CHANGE_APPROVAL_TEMPLATE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the resource is located.

### DBMS_CLOUD_OCI_LOCKBOX_CHANGE_LOCKBOX_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the resource is located.

### DBMS_CLOUD_OCI_LOCKBOX_CREATE_ACCESS_REQUEST_DETAILS_T Type

The configuration details for a new access request. We don't accept a compartmentId parameter because it is implied to be the same as the lockbox as a subsidiary resource. The requestorId is also based on the caller user info.

Syntax
```

```

Fields

Field Description

`lockbox_id`

(required) The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.

`display_name`

(optional) The name of the access request.

`description`

(required) The rationale for requesting the access request.

`context`

(optional) The context object containing the access request specific details.

`access_duration`

(required) The maximum amount of time operator has access to associated resources.

### DBMS_CLOUD_OCI_LOCKBOX_CREATE_APPROVAL_TEMPLATE_DETAILS_T Type

The configuration details for a new approval template.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the resource is located.

`display_name`

(optional) approval template identifier

`approver_levels`

(optional)

`auto_approval_state`

(optional) The auto approval state of the lockbox.

Allowed values are: 'ENABLED', 'DISABLED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_CREATE_LOCKBOX_DETAILS_T Type

The information about new Lockbox.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Lockbox Identifier

`resource_id`

(required) The unique identifier (OCID) of the customer's resource.

`lockbox_partner`

(optional) The partner using this lockbox to lock a resource.

Allowed values are: 'FAAAS', 'CANARY'

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the resource is located.

`partner_id`

(optional) The unique identifier (OCID) of partner resource using this lockbox to lock a resource

`partner_compartment_id`

(optional) Compartment Identifier

`approval_template_id`

(optional) Approval template ID

`max_access_duration`

(optional) The maximum amount of time operator has access to associated resources.

`access_context_attributes`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOCKBOX_EXPORT_ACCESS_REQUESTS_DETAILS_T Type

Details for generating report of Access Requests to export action

Syntax
```

```

Fields

Field Description

`lockbox_id`

(required) The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.

`time_created_after`

(required) Date and time after which access requests were created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)

`time_created_before`

(required) Date and time before which access requests were created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)s

### DBMS_CLOUD_OCI_LOCKBOX_HANDLE_ACCESS_REQUEST_DETAILS_T Type

The details for handling access request.

Syntax
```

```

Fields

Field Description

`action`

(required) The action take by persona

Allowed values are: 'APPROVE', 'DENY', 'REVOKE', 'CANCEL'

`message`

(optional) Action justification or details.

### DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_T Type

Description of Lockbox.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) Lockbox Identifier, can be renamed

`compartment_id`

(required) Compartment Identifier

`partner_id`

(optional) The unique identifier (OCID) of partner resource using this lockbox to lock a resource

`parent_lockbox_id`

(optional) The unique identifier (OCID) of lockbox resource using to reference parent lockbox in hybrid oma setup

`partner_compartment_id`

(optional) Compartment Identifier

`resource_id`

(required) The unique identifier (OCID) of associated resource that the lockbox is created for.

`lockbox_partner`

(optional) The partner using this lockbox to lock a resource.

Allowed values are: 'FAAAS', 'CANARY'

`time_created`

(required) The time the the Lockbox was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Lockbox was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Lockbox.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`access_context_attributes`

(optional)

`approval_template_id`

(optional) Approval template ID

`max_access_duration`

(optional) The maximum amount of time operator has access to associated resources.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_SUMMARY_T Type

Summary of the Lockbox.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) Lockbox Identifier, can be renamed

`lockbox_partner`

(optional) The partner using this lockbox to lock a resource.

Allowed values are: 'FAAAS', 'CANARY'

`compartment_id`

(required) Compartment Identifier

`partner_id`

(optional) The unique identifier (OCID) of partner resource using this lockbox to lock a resource

`partner_compartment_id`

(optional) Compartment Identifier

`resource_id`

(required) The unique identifier (OCID) of associated resource that the lockbox is created for.

`approval_template_id`

(optional) Approval template ID

`max_access_duration`

(optional) The maximum amount of time operator has access to associated resources.

`time_created`

(required) The time the the Lockbox was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Lockbox was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Lockbox.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_lockbox_lockbox_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_COLLECTION_T Type

Results of a lockbox search. Contains both LockboxSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of lockboxes.

### DBMS_CLOUD_OCI_LOCKBOX_UPDATE_APPROVAL_TEMPLATE_DETAILS_T Type

The action to be updated.

Syntax
```

```

Fields

Field Description

`approver_levels`

(optional)

`display_name`

(optional) approval template identifier

`auto_approval_state`

(optional) The auto approval state of the lockbox.

Allowed values are: 'ENABLED', 'DISABLED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_UPDATE_LOCKBOX_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Lockbox Identifier

`approval_template_id`

(optional) Approval template ID

`max_access_duration`

(optional) The maximum amount of time operator has access to associated resources.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_lockbox_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_LOCKBOX', 'UPDATE_LOCKBOX', 'DELETE_LOCKBOX', 'MOVE_LOCKBOX', 'CREATE_ACCESS_REQUEST', 'APPROVE_ACCESS_REQUEST', 'REVOKE_ACCESS_REQUEST', 'CREATE_APPROVAL_TEMPLATE', 'MOVE_APPROVAL_TEMPLATE', 'UPDATE_APPROVAL_TEMPLATE', 'DELETE_APPROVAL_TEMPLATE', 'CREATE_PARTNER', 'REMIND_ACCESS_REQUEST', 'CREATE_ACCESSCONTEXTATTRIBUTE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_lockbox_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_lockbox_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_LOCKBOX', 'UPDATE_LOCKBOX', 'DELETE_LOCKBOX', 'MOVE_LOCKBOX', 'CREATE_ACCESS_REQUEST', 'APPROVE_ACCESS_REQUEST', 'REVOKE_ACCESS_REQUEST', 'CREATE_APPROVAL_TEMPLATE', 'MOVE_APPROVAL_TEMPLATE', 'UPDATE_APPROVAL_TEMPLATE', 'DELETE_APPROVAL_TEMPLATE', 'CREATE_PARTNER', 'REMIND_ACCESS_REQUEST', 'CREATE_ACCESSCONTEXTATTRIBUTE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_lockbox_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Lockbox Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-7EC331BA-6B7D-421C-85DA-D126172B822C)
- [DBMS_CLOUD_OCI_LOCKBOX_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-265E75FA-2F1E-4950-80FF-B3953F9C98AF)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-B14FD4C5-A174-4CAC-9CC0-F5A7B8E30987)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-F56A32AB-BB34-46EF-90B9-9F3D10B1A1CB)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_CONTEXT_ATTRIBUTE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-322C0430-9084-40C3-8F23-6B1A01B6346A)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_MATERIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-8770C7C3-D9C0-474C-A8D6-58BB537E2C59)
- [DBMS_CLOUD_OCI_LOCKBOX_ACTIVITY_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-3A3723EB-1638-495C-BAA3-04BDCEE1BA79)
- [DBMS_CLOUD_OCI_LOCKBOX_ACTIVITY_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-C0C6D76C-E5F3-48F2-8E0A-BD9E97EE0BC6)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-C2B680FC-6E92-4C71-81BA-DF8574164D32)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-74D6BCBD-0C8B-449A-9455-2821BDF68E52)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-CEA20168-0381-4391-9481-D13CDB2DBF8C)
- [DBMS_CLOUD_OCI_LOCKBOX_ACCESS_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-DE599ECC-73B8-483F-AC27-98231319700B)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVER_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-EF5B517A-0561-4C4C-B2F4-806B90FDA709)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVER_LEVELS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-97596CC2-705B-46AE-82CE-3D8C09DBD409)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-D701676B-8E3A-4C6F-BD84-755754B1A30F)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-07B16BCE-5947-49DE-9CB3-89C4C875D09D)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-3DEBE6FD-92D8-4DA0-9697-70FE008EFCF7)
- [DBMS_CLOUD_OCI_LOCKBOX_APPROVAL_TEMPLATE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-9024DA00-CB55-4817-82FC-C42CCC4892F3)
- [DBMS_CLOUD_OCI_LOCKBOX_CHANGE_APPROVAL_TEMPLATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-19B53EBE-9E5F-4A70-BE98-51A7A5D5CA26)
- [DBMS_CLOUD_OCI_LOCKBOX_CHANGE_LOCKBOX_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-78BC4B84-220F-415D-990C-2D25076E43D8)
- [DBMS_CLOUD_OCI_LOCKBOX_CREATE_ACCESS_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-D56684B8-162F-4242-8C20-FBD209152832)
- [DBMS_CLOUD_OCI_LOCKBOX_CREATE_APPROVAL_TEMPLATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-E39C3DFB-2405-4D8C-8982-5C271F6B14C0)
- [DBMS_CLOUD_OCI_LOCKBOX_CREATE_LOCKBOX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-682285AC-A41A-43B9-B970-27CC84E3B358)
- [DBMS_CLOUD_OCI_LOCKBOX_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-F287CF1A-199C-4060-B443-99A44D08F1C8)
- [DBMS_CLOUD_OCI_LOCKBOX_EXPORT_ACCESS_REQUESTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-10C7AA40-4FB8-41F3-B006-B02B37427C48)
- [DBMS_CLOUD_OCI_LOCKBOX_HANDLE_ACCESS_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-8E8148DD-C624-496B-B3C4-28CA75028E64)
- [DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-AEF4F94D-53F7-46FF-8CFA-9AFF4A0BDF63)
- [DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-1D850C08-8F64-4FBE-A76F-11C034E129A1)
- [DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-2D7B04D1-D7B5-47CD-8EFF-035A85CCE33F)
- [DBMS_CLOUD_OCI_LOCKBOX_LOCKBOX_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-503D7BDB-A845-4AA8-BF96-4E57B7DA2D4A)
- [DBMS_CLOUD_OCI_LOCKBOX_UPDATE_APPROVAL_TEMPLATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-6DE20BA0-D09B-4188-A6A3-343F6B6973F9)
- [DBMS_CLOUD_OCI_LOCKBOX_UPDATE_LOCKBOX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-8DC5E46D-6E18-4773-BFFB-101989804EAC)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-829BE22B-4786-4AFA-9FE0-1222DF3B3C41)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-47E2ED5B-A64D-4B0F-9C9F-364628AFD24F)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-5F6E8AD4-E548-48FB-B422-B19B1489A560)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-EC67BCA9-213D-477D-BB04-9A0CEDA9886A)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-8EA3ACE7-0655-4B6C-9B7C-12C520BDBE86)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-BDD007EA-3F32-471D-926B-954EE81DAE48)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-7FF73589-338C-4591-8173-13BDAFA32789)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-A65AC0FE-1C63-45DD-9782-EA8356AF7CEF)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-5D8DF685-1980-48B4-A73C-8B0104B977AA)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-E3B856F0-8DB7-44E3-BE00-17E0A72D8149)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-7E746DAD-481E-4C79-9670-5FF3A58C4A9E)
- [DBMS_CLOUD_OCI_LOCKBOX_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/lockbox_t.html#ADSDK-GUID-8243C840-3257-4E70-A40F-2DF1D67C1175)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
