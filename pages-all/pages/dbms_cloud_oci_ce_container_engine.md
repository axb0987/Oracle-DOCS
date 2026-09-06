# Container Engine Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#dcoc-content-body)

## Container Engine Functions

Package: DBMS_CLOUD_OCI_CE_CONTAINER_ENGINE

### CLUSTER_MIGRATE_TO_NATIVE_VCN Function

Initiates cluster migration to use native VCN.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`cluster_migrate_to_native_vcn_details`

(required) The details for the cluster's migration to native VCN.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COMPLETE_CREDENTIAL_ROTATION Function

Complete cluster credential rotation. Retire old credentials from kubernetes components.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CLUSTER Function

Create a new cluster.

Syntax
```

```

Parameters

Parameter Description

`create_cluster_details`

(required) The details of the cluster to create.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_KUBECONFIG Function

Create the Kubeconfig YAML for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`create_cluster_kubeconfig_content_details`

(optional) The details of the cluster kubeconfig to create.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NODE_POOL Function

Create a new node pool.

Syntax
```

```

Parameters

Parameter Description

`create_node_pool_details`

(required) The details of the node pool to create.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIRTUAL_NODE_POOL Function

Create a new virtual node pool.

Syntax
```

```

Parameters

Parameter Description

`create_virtual_node_pool_details`

(required) The details of the virtual node pool to create.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_WORKLOAD_MAPPING Function

Create the specified workloadMapping for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`create_workload_mapping_details`

(required) The details of the workloadMapping to be create.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CLUSTER Function

Delete a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NODE Function

Delete node.

Syntax
```

```

Parameters

Parameter Description

`node_pool_id`

(required) The OCID of the node pool.

`node_id`

(required) The OCID of the compute instance.

`is_decrement_size`

(optional) If the nodepool should be scaled down after the node is deleted.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`override_eviction_grace_duration`

(optional) Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M

`is_force_deletion_after_override_grace_duration`

(optional) If the underlying compute instance should be deleted if you cannot evict all the pods in grace period

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NODE_POOL Function

Delete a node pool.

Syntax
```

```

Parameters

Parameter Description

`node_pool_id`

(required) The OCID of the node pool.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`override_eviction_grace_duration`

(optional) Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M

`is_force_deletion_after_override_grace_duration`

(optional) If the underlying compute instance should be deleted if you cannot evict all the pods in grace period

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIRTUAL_NODE_POOL Function

Delete a virtual node pool.

Syntax
```

```

Parameters

Parameter Description

`virtual_node_pool_id`

(required) The OCID of the virtual node pool.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`override_eviction_grace_duration_vnp`

(optional) Duration after which Sk8s will give up eviction of the pods on the node. PT0M will indicate you want to delete the virtual node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M

`is_force_deletion_after_override_grace_duration_vnp`

(optional) If the underlying compute instance should be deleted if you cannot evict all the pods in grace period

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORK_REQUEST Function

Cancel a work request that has not started.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORKLOAD_MAPPING Function

Delete workloadMapping for a provisioned cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`workload_mapping_id`

(required) The OCID of the workloadMapping.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_ADDON Function

Disable addon for a provisioned cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`addon_name`

(required) The name of the addon.

`is_remove_existing_add_on`

(required) Whether existing addon resources should be deleted or not. True would remove the underlying resources completely.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ADDON Function

Get the specified addon for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`addon_name`

(required) The name of the addon.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLUSTER Function

Get the details of a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLUSTER_MIGRATE_TO_NATIVE_VCN_STATUS Function

Get details on a cluster's migration to native VCN.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLUSTER_OPTIONS Function

Get options available for clusters.

Syntax
```

```

Parameters

Parameter Description

`cluster_option_id`

(required) The id of the option set to retrieve. Use \"all\" get all options, or use a cluster ID to get options specific to the provided cluster.

`compartment_id`

(optional) The OCID of the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CREDENTIAL_ROTATION_STATUS Function

Get cluster credential rotation status.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NODE_POOL Function

Get the details of a node pool.

Syntax
```

```

Parameters

Parameter Description

`node_pool_id`

(required) The OCID of the node pool.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NODE_POOL_OPTIONS Function

Get options available for node pools.

Syntax
```

```

Parameters

Parameter Description

`node_pool_option_id`

(required) The id of the option set to retrieve. Use \"all\" get all options, or use a cluster ID to get options specific to the provided cluster.

`compartment_id`

(optional) The OCID of the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_NODE Function

Get the details of a virtual node.

Syntax
```

```

Parameters

Parameter Description

`virtual_node_pool_id`

(required) The OCID of the virtual node pool.

`virtual_node_id`

(required) The OCID of the virtual node.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_NODE_POOL Function

Get the details of a virtual node pool.

Syntax
```

```

Parameters

Parameter Description

`virtual_node_pool_id`

(required) The OCID of the virtual node pool.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Get the details of a work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORKLOAD_MAPPING Function

Get the specified workloadMapping for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`workload_mapping_id`

(required) The OCID of the workloadMapping.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_ADDON Function

Install the specified addon for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`install_addon_details`

(required) The details of the addon to be installed.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDON_OPTIONS Function

Get list of supported addons for a specific kubernetes version.

Syntax
```

```

Parameters

Parameter Description

`kubernetes_version`

(required) The kubernetes version to fetch the addons.

`addon_name`

(optional) The name of the addon.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'NAME', 'TIME_CREATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDONS Function

List addon for a provisioned cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'NAME', 'TIME_CREATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLUSTERS Function

List all the cluster objects in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(optional) A cluster lifecycle state to filter on. Can have multiple parameters of this name.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`name`

(optional) The name to filter on.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'NAME', 'TIME_CREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NODE_POOLS Function

List all the node pools in a compartment, and optionally filter by cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`cluster_id`

(optional) The OCID of the cluster.

`name`

(optional) The name to filter on.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'NAME', 'TIME_CREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`lifecycle_state`

(optional) A list of nodepool lifecycle states on which to filter on, matching any of the list items (OR logic). eg. [ACTIVE, DELETING]

Allowed values are: 'DELETED', 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED', 'INACTIVE', 'NEEDS_ATTENTION'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_POD_SHAPES Function

List all the Pod Shapes in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`availability_domain`

(optional) The availability domain of the pod shape.

`name`

(optional) The name to filter on.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'NAME', 'TIME_CREATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_NODE_POOLS Function

List all the virtual node pools in a compartment, and optionally filter by cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`cluster_id`

(optional) The OCID of the cluster.

`name`

(optional) The name to filter on.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'NAME', 'TIME_CREATED'

`lifecycle_state`

(optional) A virtual node pool lifecycle state to filter on. Can have multiple parameters of this name.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_NODES Function

List virtual nodes in a virtual node pool.

Syntax
```

```

Parameters

Parameter Description

`virtual_node_pool_id`

(required) The OCID of the virtual node pool.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`name`

(optional) The name to filter on.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'NAME', 'TIME_CREATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Get the errors of a work request.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Get the logs of a work request.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

List all work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`cluster_id`

(optional) The OCID of the cluster.

`resource_id`

(optional) The OCID of the resource associated with a work request

`resource_type`

(optional) Type of the resource associated with a work request

Allowed values are: 'CLUSTER', 'NODEPOOL'

`status`

(optional) A work request status to filter on. Can have multiple parameters of this name.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'ID', 'OPERATION_TYPE', 'STATUS', 'TIME_ACCEPTED', 'TIME_STARTED', 'TIME_FINISHED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORKLOAD_MAPPINGS Function

List workloadMappings for a provisioned cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The optional order in which to sort the results.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The optional field to sort the results by.

Allowed values are: 'NAMESPACE', 'TIMECREATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_CREDENTIAL_ROTATION Function

Start cluster credential rotation by adding new credentials, old credentials will still work after this operation.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`start_credential_rotation_details`

(required) The details for a kubernetes cluster to start credential rotation.

`opc_retry_token`

(optional) A token you supply to uniquely identify the request and provide idempotency if the request is retried. Idempotency tokens expire after 24 hours.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ADDON Function

Update addon details for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`addon_name`

(required) The name of the addon.

`update_addon_details`

(required) The details of the addon to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLUSTER Function

Update the details of a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`update_cluster_details`

(required) The details of the cluster to update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLUSTER_ENDPOINT_CONFIG Function

Update the details of the cluster endpoint configuration.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`update_cluster_endpoint_config_details`

(required) The details of the cluster's endpoint to update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NODE_POOL Function

Update the details of a node pool.

Syntax
```

```

Parameters

Parameter Description

`node_pool_id`

(required) The OCID of the node pool.

`update_node_pool_details`

(required) The fields to update in a node pool.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`override_eviction_grace_duration`

(optional) Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M

`is_force_deletion_after_override_grace_duration`

(optional) If the underlying compute instance should be deleted if you cannot evict all the pods in grace period

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIRTUAL_NODE_POOL Function

Update the details of a virtual node pool.

Syntax
```

```

Parameters

Parameter Description

`virtual_node_pool_id`

(required) The OCID of the virtual node pool.

`update_virtual_node_pool_details`

(required) The fields to update in a virtual node pool.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_WORKLOAD_MAPPING Function

Update workloadMapping details for a cluster.

Syntax
```

```

Parameters

Parameter Description

`cluster_id`

(required) The OCID of the cluster.

`workload_mapping_id`

(required) The OCID of the workloadMapping.

`update_workload_mapping_details`

(required) The details of the workloadMapping to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://containerengine.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Container Engine Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-95AB9C41-810F-4ED4-9439-4101F739104E)
- [CLUSTER_MIGRATE_TO_NATIVE_VCN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-D0D081DC-C253-4D2A-8111-8350192CDE71)
- [COMPLETE_CREDENTIAL_ROTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-A22CA677-E4C3-4F30-B9F3-89FF93431E87)
- [CREATE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-76CB5CD0-AC82-4862-B11C-C4C0DEAC6C3B)
- [CREATE_KUBECONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-72BA5805-C3C6-4456-9776-6F48CA76149B)
- [CREATE_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-B20C807B-99C1-4617-B47E-2951A2B4D634)
- [CREATE_VIRTUAL_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-FB22FC26-EF37-4E26-BD9A-CE54AF364523)
- [CREATE_WORKLOAD_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-5C7B1E3F-7A3F-422B-BC5B-A7AD9848FCAC)
- [DELETE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-9BCC5938-DB32-4BB7-B8DD-20396177838F)
- [DELETE_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-CCDED690-0A80-4992-B88E-E178467CC211)
- [DELETE_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-5982012E-E048-4E44-B0F3-FAB947864BC6)
- [DELETE_VIRTUAL_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-ECCB4B10-4319-477E-8916-44EFF58234E8)
- [DELETE_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-51A393D8-6B97-4C75-BF25-F9B2715B68AA)
- [DELETE_WORKLOAD_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-3F2B550D-8581-42E4-AC62-0BFDCB2FD642)
- [DISABLE_ADDON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-E9F5C2C5-A5F0-48D0-B1E6-1614CBCF12D1)
- [GET_ADDON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-0F87146D-C157-4B98-B5AB-2CD46763EE2D)
- [GET_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-C06AE19A-5C79-41D3-ADD4-246208664332)
- [GET_CLUSTER_MIGRATE_TO_NATIVE_VCN_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-24A2F516-2C1E-4C27-97E1-D5A64D831FEB)
- [GET_CLUSTER_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-2191B3E3-8E7C-40B9-BA27-6D79543C877B)
- [GET_CREDENTIAL_ROTATION_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-1F5BD21E-B944-4728-83FF-A161AA9990F9)
- [GET_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-BF46A4DE-6858-4B2D-A1B0-88D732CEDF62)
- [GET_NODE_POOL_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-7D9C89D6-2E09-46CA-9EBA-86C8DD5468F1)
- [GET_VIRTUAL_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-40B4C6A0-0292-4315-A8AD-7E40FA9B5C26)
- [GET_VIRTUAL_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-AFA89BFF-2B7F-4FB0-9484-7947F374BD80)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-6D053B96-03BB-4F1A-B623-2EC672E73802)
- [GET_WORKLOAD_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-F4963908-AF0C-4F7F-8486-813F3567CA00)
- [INSTALL_ADDON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-D2A3DF8F-B70F-479D-8DA2-346E59F48572)
- [LIST_ADDON_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-9BBA96D5-2719-4B0A-AD62-5D0FF954C0A4)
- [LIST_ADDONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-209D93E2-C81C-4D58-8438-324CFD539D53)
- [LIST_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-BD1DF750-0730-4217-9F09-B6F3CDD24EC1)
- [LIST_NODE_POOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-F812D28C-B4C8-4076-A672-15473ABD2EB4)
- [LIST_POD_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-F488F6A8-E1BA-4181-9B1C-4276272351B3)
- [LIST_VIRTUAL_NODE_POOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-003DB669-D230-431B-A66F-1D8EB1A3ED63)
- [LIST_VIRTUAL_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-1BCD5EB4-9AE1-4C32-925E-830D2FFBE093)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-29EC7475-C2F2-4584-ADFC-64108B3FA13F)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-6C892CDD-3FF6-4909-92A2-BC81C40340DD)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-58F1F8EB-7363-4E61-97EB-35498ACD24E2)
- [LIST_WORKLOAD_MAPPINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-CF2D860E-5BCB-4FA3-B45C-2531A54B36F6)
- [START_CREDENTIAL_ROTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-7E5A5A63-6D54-4341-862F-DC720DDED73A)
- [UPDATE_ADDON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-CA81E215-31A0-4DE4-96DD-166739BB9BD2)
- [UPDATE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-8A283B94-91FA-4E3B-B997-94F6866FB4B6)
- [UPDATE_CLUSTER_ENDPOINT_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-DFE668EB-02C3-47A8-86A4-6EA77BB41D42)
- [UPDATE_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-241C7363-95FE-4773-8F7A-E51F5903E137)
- [UPDATE_VIRTUAL_NODE_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-B1D29A13-2B54-40B1-87E1-986F80020285)
- [UPDATE_WORKLOAD_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ce_container_engine.html#ADSDK-GUID-37573906-E982-47ED-B285-644245B274F9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
