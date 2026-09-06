# Lockbox Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#dcoc-content-body)

## Lockbox Functions

Package: DBMS_CLOUD_OCI_LBX_LOCKBOX

### CANCEL_WORK_REQUEST Function

Cancels the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_APPROVAL_TEMPLATE_COMPARTMENT Function

Moves an ApprovalTemplate resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`approval_template_id`

(required) The unique identifier (OCID) of the approval template.

`change_approval_template_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LOCKBOX_COMPARTMENT Function

Moves a Lockbox resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`lockbox_id`

(required) unique Lockbox identifier

`change_lockbox_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ACCESS_REQUEST Function

Creates a new access request.

Syntax
```

```

Parameters

Parameter Description

`create_access_request_details`

(required) Details for the new access request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPROVAL_TEMPLATE Function

Creates a new approval template.

Syntax
```

```

Parameters

Parameter Description

`create_approval_template_details`

(required) Details for the new approval template.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOCKBOX Function

Creates a new Lockbox.

Syntax
```

```

Parameters

Parameter Description

`create_lockbox_details`

(required) Details for the new Lockbox.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPROVAL_TEMPLATE Function

Deletes an ApprovalTemplate resource by identifier

Syntax
```

```

Parameters

Parameter Description

`approval_template_id`

(required) The unique identifier (OCID) of the approval template.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOCKBOX Function

Deletes a Lockbox resource by identifier

Syntax
```

```

Parameters

Parameter Description

`lockbox_id`

(required) unique Lockbox identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_ACCESS_REQUESTS Function

Exports a list of AccessRequestSummary objects within a compartment and during a specified time range in text format. You can filter the results by problem severity.

Syntax
```

```

Parameters

Parameter Description

`export_access_requests_details`

(required)

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) A generic Id query param used to filter lockbox, access request and approval template by Id.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`lockbox_partner`

(optional) The name of the lockbox partner.

Allowed values are: 'FAAAS', 'CANARY'

`partner_id`

(optional) The ID of the partner.

`requestor_id`

(optional) The unique identifier (OCID) of the requestor in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName', 'id'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ACCESS_MATERIALS Function

Retrieves the access credential/material associated with the access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) The unique identifier (OCID) of the access request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ACCESS_REQUEST Function

Retrieves an access request identified by the access request ID.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) The unique identifier (OCID) of the access request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPROVAL_TEMPLATE Function

Retrieves an approval template identified by the approval template ID.

Syntax
```

```

Parameters

Parameter Description

`approval_template_id`

(required) The unique identifier (OCID) of the approval template.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOCKBOX Function

Gets a Lockbox by identifier

Syntax
```

```

Parameters

Parameter Description

`lockbox_id`

(required) unique Lockbox identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets details of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HANDLE_ACCESS_REQUEST Function

Handle the AccessRequest

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) The unique identifier (OCID) of the access request.

`handle_access_request_details`

(required) The details of handling access request

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ACCESS_REQUESTS Function

Retrieves a list of AccessRequestSummary objects in a compartment.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The client request ID for tracing.

`lockbox_id`

(optional) The unique identifier (OCID) of the associated lockbox.

`id`

(optional) A generic Id query param used to filter lockbox, access request and approval template by Id.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`lockbox_partner`

(optional) The name of the lockbox partner.

Allowed values are: 'FAAAS', 'CANARY'

`partner_id`

(optional) The ID of the partner.

`requestor_id`

(optional) The unique identifier (OCID) of the requestor in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName', 'id'

`time_created_after`

(optional) Date and time on or after which Access Requests were created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)

`time_created_before`

(optional) Date and time on or before which Access requests were created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPROVAL_TEMPLATES Function

Retrieves a list of ApprovalTemplateSummary objects in a compartment.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The client request ID for tracing.

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`id`

(optional) A generic Id query param used to filter lockbox, access request and approval template by Id.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only resources for which their lifecycleState matches the given lifecycleState.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName', 'id'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOCKBOXES Function

Returns a list of Lockboxes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) unique Lockbox identifier

`resource_id`

(optional) The ID of the resource associated with the lockbox.

`lockbox_partner`

(optional) The name of the lockbox partner.

Allowed values are: 'FAAAS', 'CANARY'

`partner_id`

(optional) The ID of the partner.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName', 'id'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a (paginated) list of errors for the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a (paginated) list of logs for the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`work_request_id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPROVAL_TEMPLATE Function

Updates the ApprovalTemplate

Syntax
```

```

Parameters

Parameter Description

`approval_template_id`

(required) The unique identifier (OCID) of the approval template.

`update_approval_template_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOCKBOX Function

Updates the Lockbox

Syntax
```

```

Parameters

Parameter Description

`lockbox_id`

(required) unique Lockbox identifier

`update_lockbox_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managed-access.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Lockbox Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-7F5A0043-1DC7-4BF6-A0F1-E112D7B53810)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-3D0B8DC9-5405-414D-B61E-FF29274E8DD0)
- [CHANGE_APPROVAL_TEMPLATE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-ECA8B461-00F2-48AE-BB74-AD7E7B613351)
- [CHANGE_LOCKBOX_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-2D113044-21FA-4841-9537-5DA6464BAF1E)
- [CREATE_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-2853F60C-0465-472C-881C-FF947883CD67)
- [CREATE_APPROVAL_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-062FD3DE-0BE3-45CD-AEE3-DEFDDF0C8EC4)
- [CREATE_LOCKBOX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-4745540E-822C-49D4-ACB5-C60105870F90)
- [DELETE_APPROVAL_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-6588AF79-A01A-4108-ACB2-CC86703A90D5)
- [DELETE_LOCKBOX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-5C3EBEF8-EEFB-450B-8A95-E775FA2992BA)
- [EXPORT_ACCESS_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-4B7D4B71-7D44-4423-AD1B-96A6E49615DE)
- [GET_ACCESS_MATERIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-C9E5C814-4BF9-4F71-B67A-3C967A885DCE)
- [GET_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-494732CF-400E-4A2F-9535-DF56EE87A1A5)
- [GET_APPROVAL_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-7F8172E5-6D2B-47E7-93A7-7DA811A02067)
- [GET_LOCKBOX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-E42B2E25-B26A-447D-93AC-E8C7119DE335)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-1009D165-1204-4662-B6ED-E0372438A036)
- [HANDLE_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-CAB46356-980E-47EC-BEF5-5BBCE46015C4)
- [LIST_ACCESS_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-0AB81021-BFF8-4957-888D-D67BEFDF5178)
- [LIST_APPROVAL_TEMPLATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-9B7CC304-C2A7-4950-906F-0057318E7C55)
- [LIST_LOCKBOXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-5DE052D0-556E-41F5-936E-9D4667FFFB55)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-982A0817-51E2-4A6F-9088-C3CA33C8A3AC)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-D9398563-A0ED-40BF-B02A-1605E2CD2D80)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-7CF94799-91C2-4E40-BA3B-14D1327ADCD1)
- [UPDATE_APPROVAL_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-7C25DEC8-55F9-4DBD-8019-8624D99F7BD7)
- [UPDATE_LOCKBOX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lbx_lockbox.html#ADSDK-GUID-3165C99D-2FC5-4DE8-A481-D6F930CADC7C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
