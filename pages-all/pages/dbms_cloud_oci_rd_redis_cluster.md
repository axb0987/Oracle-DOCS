# Redis Cluster Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#dcoc-content-body)

## Redis Cluster Functions

Package: DBMS_CLOUD_OCI_RD_REDIS_CLUSTER

### CANCEL_WORK_REQUEST Function

Cancels the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The the asynchronous request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REDIS_CLUSTER_COMPARTMENT Function

Moves a Redis cluster into a different compartment within the same tenancy. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Parameters

Parameter Description

`redis_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`change_redis_cluster_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REDIS_CLUSTER Function

Creates a new Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Parameters

Parameter Description

`create_redis_cluster_details`

(required) Details for the new RedisCluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REDIS_CLUSTER Function

Deletes the specified Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Parameters

Parameter Description

`redis_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REDIS_CLUSTER Function

Retrieves the specified Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Parameters

Parameter Description

`redis_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The the asynchronous request ID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REDIS_CLUSTERS Function

Lists the Redis clusters in the specified compartment. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

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

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The the asynchronous request ID.

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

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The the asynchronous request ID.

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

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the resource affected by the work request.

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

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REDIS_CLUSTER Function

Updates the specified Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Parameters

Parameter Description

`redis_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`update_redis_cluster_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://redis.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Redis Cluster Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-8CC05B53-2A6A-49DC-A548-E5293E2A50A7)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-A8A88B64-8A7E-4277-85EA-B814E8FB3610)
- [CHANGE_REDIS_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-4CD2A47C-499D-453E-984B-7006E27524A5)
- [CREATE_REDIS_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-883D5F5F-BE4E-45EA-82F8-0B40304FF9A0)
- [DELETE_REDIS_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-5FFC2941-371A-486F-B046-7F8D0FE7B4E1)
- [GET_REDIS_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-E754AA7D-9D83-4E5B-BB8E-7FCC3AEB1B9D)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-496C8EB9-853E-4456-B710-65F78C5897FC)
- [LIST_REDIS_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-6569E42C-2ACA-4A2D-A6B6-14675BC39B91)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-F4F5C2A5-9D37-4562-923F-0EF605117D2E)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-5821C11D-6D87-48D2-AB12-E30EB5B61B80)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-B173A2EC-87B3-4CDB-A640-9DBB7A0F4984)
- [UPDATE_REDIS_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rd_redis_cluster.html#ADSDK-GUID-E2212C0D-E72D-4630-B1D8-1B72E9D4D720)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
