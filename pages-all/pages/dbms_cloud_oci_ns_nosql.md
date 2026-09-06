# NoSQL Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#dcoc-content-body)

## NoSQL Functions

Package: DBMS_CLOUD_OCI_NS_NOSQL

### CHANGE_TABLE_COMPARTMENT Function

Change a table's compartment.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`change_table_compartment_details`

(required) Specifications of the source and target compartments.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INDEX Function

Create a new index on the table identified by tableNameOrId.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`create_index_details`

(required) Specifications for the new index.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REPLICA Function

Add a replica for this table

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`create_replica_details`

(required) Specifications for the new replica

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TABLE Function

Create a new table.

Syntax
```

```

Parameters

Parameter Description

`create_table_details`

(required) Specifications for the new table.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INDEX Function

Delete an index from the table identified by tableNameOrId.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`index_name`

(required) The name of a table's index.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`is_if_exists`

(optional) Set as true to select \"if exists\" behavior.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPLICA Function

Delete the specified replica table in the remote region.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`l_region`

(required) A customer-facing region identifier

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ROW Function

Delete a single row from the table, by primary key.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`key`

(required) An array of strings, each of the format \"column-name:value\", representing the primary key of the row.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`is_get_return_row`

(optional) If true, and the operation fails due to an option setting (ifVersion et al), then the existing row will be returned.

`timeout_in_ms`

(optional) Timeout setting for this operation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TABLE Function

Delete a table by tableNameOrId.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`is_if_exists`

(optional) Set as true to select \"if exists\" behavior.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORK_REQUEST Function

Cancel a work request operation with the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INDEX Function

Get information about a single index.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`index_name`

(required) The name of a table's index.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROW Function

Get a single row from the table by primary key.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`key`

(required) An array of strings, each of the format \"column-name:value\", representing the primary key of the row.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`consistency`

(optional) Consistency requirement for a read operation.

Allowed values are: 'EVENTUAL', 'ABSOLUTE'

`timeout_in_ms`

(optional) Timeout setting for this operation.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TABLE Function

Get table info by identifier.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Get the status of the work request with the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INDEXES Function

Get a list of indexes on a table.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`name`

(optional) A shell-globbing-style (*?[]) filter for names.

`lifecycle_state`

(optional) Filter list by the lifecycle state of the item.

Allowed values are: 'ALL', 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TABLE_USAGE Function

Get table usage info.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`compartment_id`

(optional) The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.

`opc_request_id`

(optional) The client request ID for tracing.

`time_start`

(optional) The start time to use for the request. If no time range is set for this request, the most recent complete usage record is returned.

`time_end`

(optional) The end time to use for the request.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TABLES Function

Get a list of tables in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of a table's compartment.

`name`

(optional) A shell-globbing-style (*?[]) filter for names.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) Filter list by the lifecycle state of the item.

Allowed values are: 'ALL', 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

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

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

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

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

List the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of a table's compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PREPARE_STATEMENT Function

Prepare a SQL statement for use in a query with variable substitution.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of a table's compartment.

`statement`

(required) A NoSQL SQL statement.

`is_get_query_plan`

(optional) Include a query execution plan in the result.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### QUERY Function

Execute a SQL query.

Syntax
```

```

Parameters

Parameter Description

`query_details`

(required) SQL query statement and ancillary information.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_STATEMENT Function

Check the syntax and return a brief summary of a SQL statement.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of a table's compartment.

`statement`

(required) A NoSQL SQL statement.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ROW Function

Write a single row into the table.

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`update_row_details`

(required) Specifications for the putting of a table row.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TABLE Function

Alter the table identified by tableNameOrId, changing schema, limits, or tags

Syntax
```

```

Parameters

Parameter Description

`table_name_or_id`

(required) A table name within the compartment, or a table OCID.

`update_table_details`

(required) Specifications for the alteration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://nosql.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [NoSQL Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-AF3B5EC7-6B7E-4DB2-B072-F95E271F0334)
- [CHANGE_TABLE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-E63EE592-F50C-4F69-96C1-8E6122C19CA7)
- [CREATE_INDEX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-E2F0B8DA-E46D-414B-B4DC-641D869EAD7D)
- [CREATE_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-7F2B4603-7913-4070-A530-2F8328B08C5C)
- [CREATE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-4F0F943E-A4A9-4C52-9D6B-4610A08F6F46)
- [DELETE_INDEX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-E0D0283C-1AB4-4ACD-BD0A-4CAC7938261C)
- [DELETE_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-C19716D6-1271-43C5-B46D-155731D0C3D4)
- [DELETE_ROW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-4EA2689D-D17A-44EC-907F-372D8B53E7D8)
- [DELETE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-26D2D378-44FA-474B-BD45-053FE53057A0)
- [DELETE_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-5F5A3101-BDB3-47C0-A44D-675A5EECE512)
- [GET_INDEX Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-142021DC-66C9-4322-9AB3-463DA570E45F)
- [GET_ROW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-ACEC6990-9DD8-44BF-AE5E-3AB3400859AB)
- [GET_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-30E693ED-5CE6-4C33-889F-54F718ACD2AC)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-E645DDA2-B6E5-419C-80EA-99165A96BD45)
- [LIST_INDEXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-4F606AD0-6E4C-46D1-AF02-2CAD3BA6985F)
- [LIST_TABLE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-C9B89026-0F88-40FA-9816-B48F1BCEE927)
- [LIST_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-A414618B-7D60-45CC-B56D-0D20B2D79661)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-1549D34B-E79E-4962-9EF6-2FE1ABD362D8)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-3CAFE620-88A1-414A-8662-A3CF94AB0054)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-41842F82-B273-47CD-820F-FD543E3021B4)
- [PREPARE_STATEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-27EA3D8C-B199-403F-8CDE-CC8E5398446A)
- [QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-BADB53F5-9207-41C5-BAC6-A1296E2C6644)
- [SUMMARIZE_STATEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-5BC85B6D-5B8F-4D98-A200-706CFB59CE0F)
- [UPDATE_ROW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-5B1A4C17-975F-4C6F-9805-A32137CAABF0)
- [UPDATE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ns_nosql.html#ADSDK-GUID-FC7FA089-A71C-414C-BF1F-EC191E510FD4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
