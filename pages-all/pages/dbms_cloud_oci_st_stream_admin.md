# Streaming Admin Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#dcoc-content-body)

## Streaming Admin Functions

Package: DBMS_CLOUD_OCI_ST_STREAM_ADMIN

### CHANGE_CONNECT_HARNESS_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`connect_harness_id`

(required) The OCID of the connect harness.

`change_connect_harness_compartment_details`

(required) The connect harness will be moved into the compartment specified within this entity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_STREAM_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. The stream will also be moved into the default stream pool in the destination compartment.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`change_stream_compartment_details`

(required) The stream will be moved into the compartment specified within this entity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_STREAM_POOL_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`stream_pool_id`

(required) The OCID of the stream pool.

`change_stream_pool_compartment_details`

(required) The stream pool will be moved into the compartment specified within this entity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECT_HARNESS Function

Starts the provisioning of a new connect harness. To track the progress of the provisioning, you can periodically call`CONNECT_HARNESS`Type object tells you its current state.

Syntax
```

```

Parameters

Parameter Description

`create_connect_harness_details`

(required) The connect harness to create.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STREAM Function

Starts the provisioning of a new stream. The stream will be created in the given compartment id or stream pool id, depending on which parameter is specified. Compartment id and stream pool id cannot be specified at the same time. To track the progress of the provisioning, you can periodically call`GET_STREAM`Function. In the response, the `lifecycleState` parameter of the`STREAM`Type object tells you its current state.

Syntax
```

```

Parameters

Parameter Description

`create_stream_details`

(required) The stream to create.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STREAM_POOL Function

Starts the provisioning of a new stream pool. To track the progress of the provisioning, you can periodically call GetStreamPool. In the response, the `lifecycleState` parameter of the object tells you its current state.

Syntax
```

```

Parameters

Parameter Description

`create_stream_pool_details`

(required) The stream pool to create.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECT_HARNESS Function

Deletes a connect harness and its content. Connect harness contents are deleted immediately. The service retains records of the connect harness itself for 90 days after deletion. The `lifecycleState` parameter of the `ConnectHarness` object changes to `DELETING` and the connect harness becomes inaccessible for read or write operations. To verify that a connect harness has been deleted, make a`GET_CONNECT_HARNESS`Function request. If the call returns the connect harness's lifecycle state as `DELETED`, then the connect harness has been deleted. If the call returns a \"404 Not Found\" error, that means all records of the connect harness have been deleted.

Syntax
```

```

Parameters

Parameter Description

`connect_harness_id`

(required) The OCID of the connect harness.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STREAM Function

Deletes a stream and its content. Stream contents are deleted immediately. The service retains records of the stream itself for 90 days after deletion. The `lifecycleState` parameter of the `Stream` object changes to `DELETING` and the stream becomes inaccessible for read or write operations. To verify that a stream has been deleted, make a`GET_STREAM`Function request. If the call returns the stream's lifecycle state as `DELETED`, then the stream has been deleted. If the call returns a \"404 Not Found\" error, that means all records of the stream have been deleted.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STREAM_POOL Function

Deletes a stream pool. All containing streams will also be deleted. The default stream pool of a compartment cannot be deleted.

Syntax
```

```

Parameters

Parameter Description

`stream_pool_id`

(required) The OCID of the stream pool.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECT_HARNESS Function

Gets detailed information about a connect harness.

Syntax
```

```

Parameters

Parameter Description

`connect_harness_id`

(required) The OCID of the connect harness.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STREAM Function

Gets detailed information about a stream, including the number of partitions.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STREAM_POOL Function

Gets detailed information about the stream pool, such as Kafka settings.

Syntax
```

```

Parameters

Parameter Description

`stream_pool_id`

(required) The OCID of the stream pool.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECT_HARNESSES Function

Lists the connectharness.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`id`

(optional) A filter to return only resources that match the given ID exactly.

`name`

(optional) A filter to return only resources that match the given name exactly.

`limit`

(optional) The maximum number of items to return. The value must be between 1 and 50. The default is 10.

`page`

(optional) The page at which to start retrieving results.

`sort_by`

(optional) The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.

Allowed values are: 'NAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STREAM_POOLS Function

List the stream pools for a given compartment ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`id`

(optional) A filter to return only resources that match the given ID exactly.

`name`

(optional) A filter to return only resources that match the given name exactly.

`limit`

(optional) The maximum number of items to return. The value must be between 1 and 50. The default is 10.

`page`

(optional) The page at which to start retrieving results.

`sort_by`

(optional) The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.

Allowed values are: 'NAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STREAMS Function

Lists the streams in the given compartment id. If the compartment id is specified, it will list streams in the compartment, regardless of their stream pool. If the stream pool id is specified, the action will be scoped to that stream pool. The compartment id and stream pool id cannot be specified at the same time.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment. Is exclusive with the `streamPoolId` parameter. One of them is required.

`stream_pool_id`

(optional) The OCID of the stream pool. Is exclusive with the `compartmentId` parameter. One of them is required.

`id`

(optional) A filter to return only resources that match the given ID exactly.

`name`

(optional) A filter to return only resources that match the given name exactly.

`limit`

(optional) The maximum number of items to return. The value must be between 1 and 50. The default is 10.

`page`

(optional) The page at which to start retrieving results.

`sort_by`

(optional) The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.

Allowed values are: 'NAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONNECT_HARNESS Function

Updates the tags applied to the connect harness.

Syntax
```

```

Parameters

Parameter Description

`connect_harness_id`

(required) The OCID of the connect harness.

`update_connect_harness_details`

(required) The connect harness is updated with the tags provided.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STREAM Function

Updates the stream. Only specified values will be updated.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`update_stream_details`

(required) The stream is updated with the values provided.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STREAM_POOL Function

Updates the specified stream pool.

Syntax
```

```

Parameters

Parameter Description

`stream_pool_id`

(required) The OCID of the stream pool.

`update_stream_pool_details`

(required) The pool is updated with the provided fields.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Streaming Admin Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-AE2181FB-895A-4BCC-86F2-22D38571E0A9)
- [CHANGE_CONNECT_HARNESS_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-5FCEE00B-701C-4784-8CE6-7736E8390C7E)
- [CHANGE_STREAM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-12D34646-A474-4761-870C-98930311E415)
- [CHANGE_STREAM_POOL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-9F072C84-8603-46B0-9961-F0975EC57852)
- [CREATE_CONNECT_HARNESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-70BB2B2C-C09C-4BE5-B3F1-A1007A14D16A)
- [CREATE_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-450BF965-DD50-4881-82D3-FA1B90E23BEE)
- [CREATE_STREAM_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-5F8FAC5A-76AE-4352-89E9-878880E0C327)
- [DELETE_CONNECT_HARNESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-E0CBC041-750F-4F5A-BB41-8167CDA86E42)
- [DELETE_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-7D8B8F70-1AE9-40EC-BB62-B2973A78065B)
- [DELETE_STREAM_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-4C9EC037-5F9D-4193-BBEA-22AB07C0059B)
- [GET_CONNECT_HARNESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-DB253C19-E628-4847-A22C-77532356D993)
- [GET_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-7F129D58-CBF4-4424-83DD-98EE7F952525)
- [GET_STREAM_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-B9FBD238-D292-47D8-A7B6-9336200DE8B5)
- [LIST_CONNECT_HARNESSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-0E45A68B-660D-4DA2-AEBF-3D05F2BFC0BD)
- [LIST_STREAM_POOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-1AC8533F-C670-44BC-9D92-0D0433A297AD)
- [LIST_STREAMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-7220B9EC-9F10-4A61-8ECC-C2F999F82D73)
- [UPDATE_CONNECT_HARNESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-EBF2946E-A176-4C88-84C1-467694912030)
- [UPDATE_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-F4BF125C-CF26-4C9D-B451-1FB6ED16B013)
- [UPDATE_STREAM_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream_admin.html#ADSDK-GUID-35D2A376-4903-4CA2-B7A4-B5B45EFB2F33)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
