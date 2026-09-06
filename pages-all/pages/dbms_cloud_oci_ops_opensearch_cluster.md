# OpenSearch Cluster Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#dcoc-content-body)

## OpenSearch Cluster Functions

Package: DBMS_CLOUD_OCI_OPS_OPENSEARCH_CLUSTER

### BACKUP_OPENSEARCH_CLUSTER Function

Backup the opensearch cluster details.

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`backup_opensearch_cluster_details`

(required) Backup the opensearch cluster details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPENSEARCH_CLUSTER Function

Creates a new OpensearchCluster.

Syntax
```

```

Parameters

Parameter Description

`create_opensearch_cluster_details`

(required) Details for the new OpensearchCluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPENSEARCH_CLUSTER Function

Deletes a OpensearchCluster resource by identifier

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPENSEARCH_CLUSTER Function

Gets a OpensearchCluster by identifier

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPENSEARCH_CLUSTERS Function

Returns a list of OpensearchClusters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only OpensearchClusters their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) unique OpensearchCluster identifier

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

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPENSEARCH_VERSIONS Function

Lists the supported Opensearch versions

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`work_request_id`

(optional) The ID of the asynchronous work request.

`source_resource_id`

(optional) The ID of the source resource to list work requests.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### OPENSEARCH_CLUSTER_RESTORE Function

Restore the opensearch cluster details.

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`restore_opensearch_cluster_details`

(required) Restore the opensearch cluster details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESIZE_OPENSEARCH_CLUSTER_HORIZONTAL Function

Resize the opensearch cluster horizontal details.

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`resize_opensearch_cluster_horizontal_details`

(required) Resize the opensearch cluster horizontal details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESIZE_OPENSEARCH_CLUSTER_VERTICAL Function

Resize the opensearch cluster vertical details.

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`resize_opensearch_cluster_vertical_details`

(required) Resize the opensearch cluster vertical details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPENSEARCH_CLUSTER Function

Updates the OpensearchCluster

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_id`

(required) unique OpensearchCluster identifier

`update_opensearch_cluster_details`

(required) Update the opensearch cluster details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OpenSearch Cluster Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-2147658D-A90B-4E17-A4EA-BAC73CE1AADA)
- [BACKUP_OPENSEARCH_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-EA33A2F2-FCDF-40E1-A2A7-74BC31264FDE)
- [CREATE_OPENSEARCH_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-6C860218-C4FF-4CDE-B7A2-2F4482074F67)
- [DELETE_OPENSEARCH_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-46B424AB-75E9-4FC8-B275-64D737AF03A3)
- [GET_OPENSEARCH_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-F2EF1A9D-C7A0-4B27-BB18-F6FAB614ACE2)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-265A1F27-7DAE-494E-BA7F-A475BC851E97)
- [LIST_OPENSEARCH_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-FF144F46-4CD3-4818-B147-E67E95028C99)
- [LIST_OPENSEARCH_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-0EAF0AB1-B799-4362-B7B4-CE7F5960FB36)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-9B9BE1D5-392C-45D4-BC16-353AC3443A2F)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-0310A9F1-522F-4DBD-BAC4-0EAE86D2F4D7)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-06601C65-54D6-4C8C-9514-2CEFEBD69F53)
- [OPENSEARCH_CLUSTER_RESTORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-5D6D72FF-2AD7-4A9E-9798-AD8427043B64)
- [RESIZE_OPENSEARCH_CLUSTER_HORIZONTAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-C621CCC0-1F95-41D5-967E-0FC15B78521D)
- [RESIZE_OPENSEARCH_CLUSTER_VERTICAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-82413B0A-BA50-44C8-A869-EF1AF6C8EDFF)
- [UPDATE_OPENSEARCH_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster.html#ADSDK-GUID-A208B8AD-362B-41B5-BC8D-A7CDF31BC60D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
