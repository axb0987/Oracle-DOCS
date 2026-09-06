# Database Tools Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#dcoc-content-body)

## Database Tools Functions

Package: DBMS_CLOUD_OCI_DT_DATABASE_TOOLS

### ADD_DATABASE_TOOLS_CONNECTION_LOCK Function

Adds a lock to a DatabaseToolsConnection resource.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`add_resource_lock_details`

(required) AddResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_DATABASE_TOOLS_PRIVATE_ENDPOINT_LOCK Function

Adds a lock to a DatabaseToolsPrivateEndpoint resource.

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`add_resource_lock_details`

(required) AddResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_TOOLS_CONNECTION_COMPARTMENT Function

Moves the specified Database Tools connection to a different compartment in the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`change_database_tools_connection_compartment_details`

(required) Request to change the compartment of the DatabaseToolsConnection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_TOOLS_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves a Database Tools private endpoint into a different compartment in the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`change_database_tools_private_endpoint_compartment_details`

(required) Request to change the compartment of the DatabaseToolsPrivateEndpoint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE_TOOLS_CONNECTION Function

Creates a new Database Tools connection.

Syntax
```

```

Parameters

Parameter Description

`create_database_tools_connection_details`

(required) Details for the new `DatabaseToolsConnection`.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected. Accepted characters: ASCII alphanumerics plus underscore (U+005F LOW LINE \"_\") and dash (U+002D HYPHEN-MINUS \"-\")

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function

Creates a new Database Tools private endpoint.

Syntax
```

```

Parameters

Parameter Description

`create_database_tools_private_endpoint_details`

(required) Details for the new DatabaseToolsPrivateEndpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected. Accepted characters: ASCII alphanumerics plus underscore (U+005F LOW LINE \"_\") and dash (U+002D HYPHEN-MINUS \"-\")

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE_TOOLS_CONNECTION Function

Deletes the specified Database Tools connection resource.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function

Deletes the specified Database Tools private endpoint.

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_TOOLS_CONNECTION Function

Gets details of the specified Database Tools connection.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_TOOLS_ENDPOINT_SERVICE Function

Gets details for the specified Database Tools endpoint service.

Syntax
```

```

Parameters

Parameter Description

`database_tools_endpoint_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools Endpoint Service.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_TOOLS_PRIVATE_ENDPOINT Function

Gets details of a specified Database Tools private endpoint.

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the specified work request.

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

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_TOOLS_CONNECTIONS Function

Returns a list of Database Tools connections.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`display_name`

(optional) A filter to return only resources that match the entire specified display name.

`l_type`

(optional) A filter to return only resources their type matches the specified type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

`runtime_support`

(optional) A filter to return only resources with one of the specified runtimeSupport values.

Allowed values are: 'SUPPORTED', 'UNSUPPORTED'

`related_resource_identifier`

(optional) A filter to return only resources associated to the related resource identifier OCID passed in the query string.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_TOOLS_ENDPOINT_SERVICES Function

Returns a list of Database Tools endpoint services.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`display_name`

(optional) A filter to return only resources that match the entire specified display name.

`name`

(optional) A filter to return only resources that match the entire specified name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_TOOLS_PRIVATE_ENDPOINTS Function

Returns a list of Database Tools private endpoints.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`subnet_id`

(optional) A filter to return only resources their `subnetId` matches the specified `subnetId`.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`endpoint_service_id`

(optional) A filter to return only resources their `endpointServiceId` matches the specified `endpointServiceId`.

`lifecycle_state`

(optional) A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`display_name`

(optional) A filter to return only resources that match the entire specified display name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a paginated list of errors for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a paginated list of logs for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the compartment in which to list resources.

`resource_identifier`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.

Allowed values are: 'timeAccepted'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DATABASE_TOOLS_CONNECTION_LOCK Function

Removes a lock from a DatabaseToolsConnection resource.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`remove_resource_lock_details`

(required) RemoveResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DATABASE_TOOLS_PRIVATE_ENDPOINT_LOCK Function

Removes a lock from a DatabaseToolsPrivateEndpoint resource.

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`remove_resource_lock_details`

(required) RemoveResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_TOOLS_CONNECTION Function

Updates the specified Database Tools connection.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`update_database_tools_connection_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function

Updates the specified Database Tools private endpoint.

Syntax
```

```

Parameters

Parameter Description

`database_tools_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools private endpoint.

`update_database_tools_private_endpoint_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_DATABASE_TOOLS_CONNECTION Function

Validates the Database Tools connection details by establishing a connection to the database.

Syntax
```

```

Parameters

Parameter Description

`database_tools_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Database Tools connection.

`validate_database_tools_connection_details`

(required) Request to validate a DatabaseToolsConnection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbtools.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Tools Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-308C96A0-2406-4C96-AA3A-4A31EE11D18B)
- [ADD_DATABASE_TOOLS_CONNECTION_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-A9725292-CBC4-4CB6-8AEC-8151C9A47F67)
- [ADD_DATABASE_TOOLS_PRIVATE_ENDPOINT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-D42C295F-AD32-4912-8AC8-878F8D6BA595)
- [CHANGE_DATABASE_TOOLS_CONNECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-37B57F94-59B4-4586-9CDC-BD18B8A21BD5)
- [CHANGE_DATABASE_TOOLS_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-EDB8882F-0FB7-4502-A44E-EA0F4C8C2033)
- [CREATE_DATABASE_TOOLS_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-9102CA20-E662-45DC-8433-FDE1A125F045)
- [CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-F93F4EB2-7A9F-4C3E-BCF3-CDFB68EAB89E)
- [DELETE_DATABASE_TOOLS_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-7887AE98-33BF-4AB1-A9FA-56608B4A6E94)
- [DELETE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-AE9B47A3-A287-4D7F-928C-9A2EBB6E5ABE)
- [GET_DATABASE_TOOLS_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-F6EEAFE7-AB01-43EA-BF0D-9BA0D4D293D0)
- [GET_DATABASE_TOOLS_ENDPOINT_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-84E41BCE-0CB0-46D4-A0AC-ACCB42C05EC9)
- [GET_DATABASE_TOOLS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-2CC101F5-9585-4212-A7CB-33DB89E85830)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-724E27BC-6642-4D31-81A3-FDF1FC1F90BE)
- [LIST_DATABASE_TOOLS_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-DD76A0D9-0197-4228-9634-C9490CFB2DFE)
- [LIST_DATABASE_TOOLS_ENDPOINT_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-742EC960-727B-416C-8B29-5F63C57E2E0C)
- [LIST_DATABASE_TOOLS_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-D356E22C-4DB0-4997-9A04-FFD7BD4BC15C)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-AEABEF24-C8F9-4099-A03A-6A9DF2D3BDCE)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-6F71BEC1-4B79-4CBF-A67E-EBD376D72C5E)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-E147C783-3EAA-4036-895A-9808B31F8DE0)
- [REMOVE_DATABASE_TOOLS_CONNECTION_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-72E03C6A-3EBA-411F-A294-3599FD03B0C2)
- [REMOVE_DATABASE_TOOLS_PRIVATE_ENDPOINT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-86895BEB-5845-4481-9C64-309E4DB893BC)
- [UPDATE_DATABASE_TOOLS_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-BD97698F-8820-4227-A893-1C1C33E600E4)
- [UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-3167CEC4-065C-4C30-8DB4-D96785ACAACE)
- [VALIDATE_DATABASE_TOOLS_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dt_database_tools.html#ADSDK-GUID-806D94BF-AD51-4295-976F-32B657090DAA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
