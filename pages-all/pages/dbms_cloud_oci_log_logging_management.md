# Logging Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#dcoc-content-body)

## Logging Functions

Package: DBMS_CLOUD_OCI_LOG_LOGGING_MANAGEMENT

### CHANGE_LOG_GROUP_COMPARTMENT Function

Moves a log group into a different compartment within the same tenancy. When provided, the If-Match is checked against the resource ETag values. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`change_log_group_compartment_details`

(required) Request to change the compartment of a given resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LOG_LOG_GROUP Function

Moves a log into a different log group within the same tenancy. When provided, the If-Match is checked against the ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`log_id`

(required) OCID of a log to work with.

`change_log_log_group_details`

(required) Request to change the log group of a given log.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LOG_SAVED_SEARCH_COMPARTMENT Function

Moves a saved search into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`log_saved_search_id`

(required) OCID of the logSavedSearch.

`change_log_saved_search_compartment_details`

(required) Contains details indicating which compartment the resource should move to.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_UNIFIED_AGENT_CONFIGURATION_COMPARTMENT Function

Moves the unified agent configuration into a different compartment within the same tenancy. When provided, the If-Match is checked against the ETag values of the resource. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`unified_agent_configuration_id`

(required) The OCID of the Unified Agent configuration.

`change_unified_agent_configuration_compartment_details`

(required) Request to change the compartment of a given resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOG Function

Creates a log within the specified log group. This call fails if a log group has already been created with the same displayName or (service, resource, category) triplet.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`create_log_details`

(required) Log object configuration details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOG_GROUP Function

Create a new log group with a unique display name. This call fails if the log group is already created with the same displayName in the compartment.

Syntax
```

```

Parameters

Parameter Description

`create_log_group_details`

(required) Details to create log group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOG_SAVED_SEARCH Function

Creates a new LogSavedSearch.

Syntax
```

```

Parameters

Parameter Description

`create_log_saved_search_details`

(required) Specification of the saved search to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_UNIFIED_AGENT_CONFIGURATION Function

Create unified agent configuration registration.

Syntax
```

```

Parameters

Parameter Description

`create_unified_agent_configuration_details`

(required) Unified agent configuration creation object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOG Function

Deletes the log object in a log group.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`log_id`

(required) OCID of a log to work with.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOG_GROUP Function

Deletes the specified log group.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOG_SAVED_SEARCH Function

Deletes the specified LogSavedSearch.

Syntax
```

```

Parameters

Parameter Description

`log_saved_search_id`

(required) OCID of the logSavedSearch.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_UNIFIED_AGENT_CONFIGURATION Function

Delete unified agent configuration.

Syntax
```

```

Parameters

Parameter Description

`unified_agent_configuration_id`

(required) The OCID of the Unified Agent configuration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORK_REQUEST Function

Cancel a work request that has not started yet.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The asynchronous request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOG Function

Gets the log object configuration for the log object OCID.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`log_id`

(required) OCID of a log to work with.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOG_GROUP Function

Get the specified log group's information.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOG_SAVED_SEARCH Function

Retrieves a LogSavedSearch.

Syntax
```

```

Parameters

Parameter Description

`log_saved_search_id`

(required) OCID of the logSavedSearch.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_UNIFIED_AGENT_CONFIGURATION Function

Get the unified agent configuration for an ID.

Syntax
```

```

Parameters

Parameter Description

`unified_agent_configuration_id`

(required) The OCID of the Unified Agent configuration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The asynchronous request ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOG_GROUPS Function

Lists all log groups for the specified compartment or tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) Compartment OCID to list resources in. See compartmentIdInSubtree for nested compartments traversal.

`is_compartment_id_in_subtree`

(optional) Specifies whether or not nested compartments should be traversed. Defaults to false.

`display_name`

(optional) Resource name.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`sort_by`

(optional) The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOG_SAVED_SEARCHES Function

Lists LogSavedSearches for this compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) Compartment OCID to list resources in. See compartmentIdInSubtree for nested compartments traversal.

`log_saved_search_id`

(optional) OCID of the LogSavedSearch.

`name`

(optional) Resource name.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`sort_by`

(optional) The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOGS Function

Lists the specified log group's log objects.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`log_type`

(optional) The logType that the log object is for, whether custom or service.

Allowed values are: 'CUSTOM', 'SERVICE'

`source_service`

(optional) Service that created the log object, which is a field of LogSummary.Configuration.Source.

`source_resource`

(optional) Log object resource, which is a field of LogSummary.Configuration.Source.

`display_name`

(optional) Resource name.

`lifecycle_state`

(optional) Lifecycle state of the log object

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`sort_by`

(optional) The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICES Function

Lists all services that support logging.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_UNIFIED_AGENT_CONFIGURATIONS Function

Lists all unified agent configurations in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) Compartment OCID to list resources in. See compartmentIdInSubtree for nested compartments traversal.

`log_id`

(optional) Custom log OCID to list resources with the log as destination.

`is_compartment_id_in_subtree`

(optional) Specifies whether or not nested compartments should be traversed. Defaults to false.

`group_id`

(optional) The OCID of a group or a dynamic group.

`display_name`

(optional) Resource name.

`lifecycle_state`

(optional) Lifecycle state of the log object

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The asynchronous request ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The asynchronous request ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) Compartment OCID to list resources in. See compartmentIdInSubtree for nested compartments traversal.

`status`

(optional) Filter results by work request status.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELLING', 'CANCELED'

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order.

Allowed values are: 'operationType', 'status', 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOG Function

Updates the existing log object with the associated configuration. This call fails if the log object does not exist.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`log_id`

(required) OCID of a log to work with.

`update_log_details`

(required) Log config parameters to update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOG_GROUP Function

Updates the existing log group with the associated configuration. This call fails if the log group does not exist.

Syntax
```

```

Parameters

Parameter Description

`log_group_id`

(required) OCID of a log group to work with.

`update_log_group_details`

(required) LogGroup config parameters to update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOG_SAVED_SEARCH Function

Updates an existing LogSavedSearch.

Syntax
```

```

Parameters

Parameter Description

`log_saved_search_id`

(required) OCID of the logSavedSearch.

`update_log_saved_search_details`

(required) Updates to the saved search.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_UNIFIED_AGENT_CONFIGURATION Function

Update an existing unified agent configuration. This call fails if the log group does not exist.

Syntax
```

```

Parameters

Parameter Description

`unified_agent_configuration_id`

(required) The OCID of the Unified Agent configuration.

`update_unified_agent_configuration_details`

(required) Unified agent configuration to update. Empty group associations list doesn't modify the list, null value for group association clears all the previous associations.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Logging Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-56ADADED-C913-4587-9E87-B438D0DA827F)
- [CHANGE_LOG_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-413B4C40-B92A-4D73-BE15-FCC7D2553263)
- [CHANGE_LOG_LOG_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-6CDDFEAD-CB2D-497F-880F-B5A34E5BCE3F)
- [CHANGE_LOG_SAVED_SEARCH_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-86CE2966-4163-4AA2-99C2-38E81C5A6921)
- [CHANGE_UNIFIED_AGENT_CONFIGURATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-5A01560B-2188-46D9-9758-1A780F93885B)
- [CREATE_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-7049ACD2-90C0-4F0E-8C62-EBAD818AC18C)
- [CREATE_LOG_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-4AD854E0-3A9E-4A38-A442-BB72FDCA19B5)
- [CREATE_LOG_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-0AC0A95D-5B74-4542-A31A-CEC76632ED4F)
- [CREATE_UNIFIED_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-EC44ACB2-C1DA-4EC8-81DE-C8E997C8EC3B)
- [DELETE_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-C32A2805-76F6-471A-B871-F47C24E44E37)
- [DELETE_LOG_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-2D84F7CD-F4B0-4A6F-8197-0F9F09C6A9DD)
- [DELETE_LOG_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-ACE003D1-FC71-45CC-B2C9-92C3A9C7ABA4)
- [DELETE_UNIFIED_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-BDDC40E4-E3C9-4D7F-9FC0-4E7EA84791B3)
- [DELETE_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-4BBC890E-E7CC-442C-A088-4F25E5E84D4C)
- [GET_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-DFF2CC47-A6C6-491A-975D-B988A40C9DEB)
- [GET_LOG_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-0BDD9060-B709-4A2D-ACDF-259B5DF4EE34)
- [GET_LOG_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-D5674F9F-2349-4286-9A21-A1251445082C)
- [GET_UNIFIED_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-86414C62-EF07-4BA2-A601-C300B15AE6D0)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-9F438F7C-6005-4773-912E-F5E849B0B791)
- [LIST_LOG_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-69C864AF-F1EC-46AF-9FD4-E4EE3BE2956A)
- [LIST_LOG_SAVED_SEARCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-0EF7F57A-CEA2-48A5-A64E-990D6E2B4D16)
- [LIST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-A62493FF-8C6E-481D-B401-A43518CCBC46)
- [LIST_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-4346BEB1-DA41-4A7D-80FF-D7DF194CD22A)
- [LIST_UNIFIED_AGENT_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-13BDFCDE-692F-4469-98B2-966341D98585)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-6ADF4140-92DA-4871-82E4-0CEC6A32D4B2)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-FF13409C-FF22-4BD6-9DF5-8F5C1B7F93D3)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-6F156F5C-8091-447B-8256-F2CE4D2BA9DF)
- [UPDATE_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-7AC3FA01-2E3F-467A-B157-7169487299C9)
- [UPDATE_LOG_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-A3AE759D-3073-4F11-922F-505236EAC006)
- [UPDATE_LOG_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-D95400BB-466D-4822-8682-8443BCD72A42)
- [UPDATE_UNIFIED_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_log_logging_management.html#ADSDK-GUID-20E1F41E-0E08-4610-AB10-592E0A763011)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
