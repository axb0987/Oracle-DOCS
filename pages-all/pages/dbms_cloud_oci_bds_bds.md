# BDS Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#dcoc-content-body)

## BDS Functions

Package: DBMS_CLOUD_OCI_BDS_BDS

### ACTIVATE_BDS_METASTORE_CONFIGURATION Function

Activate specified metastore configuration.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_config_id`

(required) The metastore configuration ID

`activate_bds_metastore_configuration_details`

(required) The request body when activating specified metastore configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_AUTO_SCALING_CONFIGURATION Function

Add an autoscale configuration to the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_auto_scaling_configuration_details`

(required) Details for creating an autoscale configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_BLOCK_STORAGE Function

Adds block storage to existing worker/compute only worker nodes. The same amount of storage will be added to all worker/compute only worker nodes. No change will be made to storage that is already attached. Block storage cannot be removed.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_block_storage_details`

(required) Details for the added block storage.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_CLOUD_SQL Function

Adds Cloud SQL to your cluster. You can use Cloud SQL to query against non-relational data stored in multiple big data sources, including Apache Hive, HDFS, Oracle NoSQL Database, and Apache HBase. Adding Cloud SQL adds a query server node to the cluster and creates cell servers on all the worker nodes in the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_cloud_sql_details`

(required) Details for the Cloud SQL capability

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_KAFKA Function

Adds Kafka to a cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_kafka_details`

(required) Details of the Kafka broker nodes to employ to enable the service.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_MASTER_NODES Function

Increases the size (scales out) of a cluster by adding master nodes. The added master nodes will have the same shape and will have the same amount of attached block storage as other master nodes in the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_master_nodes_details`

(required) Details for the newly added nodes.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_UTILITY_NODES Function

Increases the size (scales out) of a cluster by adding utility nodes. The added utility nodes will have the same shape and will have the same amount of attached block storage as other utility nodes in the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_utility_nodes_details`

(required) Details for the newly added nodes.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_WORKER_NODES Function

Increases the size (scales out) a cluster by adding worker nodes(data/compute). The added worker nodes will have the same shape and will have the same amount of attached block storage as other worker nodes in the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`add_worker_nodes_details`

(required) Details for the newly added nodes.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CERTIFICATE_SERVICE_INFO Function

A list of services and their certificate details.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`certificate_service_info_details`

(required) Details for certificate service info

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_BDS_INSTANCE_COMPARTMENT Function

Moves a Big Data Service cluster into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`change_bds_instance_compartment_details`

(required) Details for the comparment change.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SHAPE Function

Changes the size of a cluster by scaling up or scaling down the nodes. Nodes are scaled up or down by changing the shapes of all the nodes of the same type to the next larger or smaller shape. The node types are master, utility, worker, and Cloud SQL. Only nodes with VM-STANDARD shapes can be scaled.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`change_shape_details`

(required) Individual change shape settings per node type. You can change the shape of master, worker, utility and Cloud SQL nodes.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BDS_API_KEY Function

Create an API key on behalf of the specified user.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`create_bds_api_key_details`

(required) Create a new user's API key.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BDS_INSTANCE Function

Creates a Big Data Service cluster.

Syntax
```

```

Parameters

Parameter Description

`create_bds_instance_details`

(required) Details for the new cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BDS_METASTORE_CONFIGURATION Function

Create and activate external metastore configuration.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`create_bds_metastore_configuration_details`

(required) The request body when creating and activating external metastore configuration.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BDS_API_KEY Function

Deletes the user's API key represented by the provided ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`api_key_id`

(required) The API key identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BDS_INSTANCE Function

Deletes the cluster identified by the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BDS_METASTORE_CONFIGURATION Function

Delete the BDS metastore configuration represented by the provided ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_config_id`

(required) The metastore configuration ID

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_CERTIFICATE Function

Disabling TLS/SSL for various ODH services running on the BDS cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`disable_certificate_details`

(required) Details for disabling certificate.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_CERTIFICATE Function

Configuring TLS/SSL for various ODH services running on the BDS cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`enable_certificate_details`

(required) Details for configuring certificate.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXECUTE_BOOTSTRAP_SCRIPT Function

Execute bootstrap script.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`execute_bootstrap_script_details`

(required) Details of the bootstrap script to execute on this cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTO_SCALING_CONFIGURATION Function

Returns details of the autoscale configuration identified by the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`auto_scaling_configuration_id`

(required) Unique Oracle-assigned identifier of the autoscale configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BDS_API_KEY Function

Returns the user's API key information for the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`api_key_id`

(required) The API key identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BDS_INSTANCE Function

Returns information about the Big Data Service cluster identified by the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BDS_METASTORE_CONFIGURATION Function

Returns the BDS Metastore configuration information for the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_config_id`

(required) The metastore configuration ID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OS_PATCH_DETAILS Function

Get the details of an os patch

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`os_patch_version`

(required) The version of the OS patch.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Returns the status of the work request identified by the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_OS_PATCH Function

Install an os patch on a cluster

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`install_os_patch_details`

(required) Details of the target os patch that will be installed

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_PATCH Function

Install the specified patch to this cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`install_patch_details`

(required) Details of the patch to be installed.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTO_SCALING_CONFIGURATIONS Function

Returns information about the autoscaling configurations for a cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`bds_instance_id`

(required) The OCID of the cluster.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The state of the autoscale configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BDS_API_KEYS Function

Returns a list of all API keys associated with this Big Data Service cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`lifecycle_state`

(optional) The state of the API key.

`user_id`

(optional) The OCID of the user for whom the API key belongs.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BDS_INSTANCES Function

Returns a list of all Big Data Service clusters in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(optional) The state of the cluster.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BDS_METASTORE_CONFIGURATIONS Function

Returns a list of metastore configurations ssociated with this Big Data Service cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_type`

(optional) The type of the metastore in the metastore configuration

`metastore_id`

(optional) The OCID of the Data Catalog metastore in the metastore configuration

`lifecycle_state`

(optional) The lifecycle state of the metastore in the metastore configuration

`bds_api_key_id`

(optional) The ID of the API key that is associated with the external metastore in the metastore configuration

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OS_PATCHES Function

List all available os patches for a given cluster

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATCH_HISTORIES Function

List the patch history of this cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) The status of the patch.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`patch_version`

(optional) The version of the patch

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`patch_type`

(optional) The type of a BDS patch history entity.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATCHES Function

List all the available patches for this cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a paginated list of errors for a work request identified by the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a paginated list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment.

`resource_id`

(optional) The OCID of the resource.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_AUTO_SCALING_CONFIGURATION Function

Deletes an autoscale configuration.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`auto_scaling_configuration_id`

(required) Unique Oracle-assigned identifier of the autoscale configuration.

`remove_auto_scaling_configuration_details`

(required) Details for the autoscale configuration

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_CLOUD_SQL Function

Removes Cloud SQL from the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`remove_cloud_sql_details`

(required) Details for the Cloud SQL capability

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_KAFKA Function

Remove Kafka from the cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`remove_kafka_details`

(required) Details for the Kafka capability.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_NODE Function

Remove a single node of a Big Data Service cluster

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`remove_node_details`

(required) Details for the node to be removed.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RENEW_CERTIFICATE Function

Renewing TLS/SSL for various ODH services running on the BDS cluster.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`renew_certificate_details`

(required) Details for renewing certificate.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTART_NODE Function

Restarts a single node of a Big Data Service cluster

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`restart_node_details`

(required) Details for restarting the node.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_BDS_INSTANCE Function

Starts the BDS cluster that was stopped earlier.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`start_bds_instance_details`

(required) Parameters for starting a cluster

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_BDS_INSTANCE Function

Stops the BDS cluster that can be started at later point of time.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`stop_bds_instance_details`

(required) Parameters for stopping a cluster

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_BDS_METASTORE_CONFIGURATION Function

Test specified metastore configuration.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_config_id`

(required) The metastore configuration ID

`test_bds_metastore_configuration_details`

(required) Request body for testing BDS metastore configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_BDS_OBJECT_STORAGE_CONNECTION Function

Test access to specified Object Storage bucket using the API key.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`api_key_id`

(required) The API key identifier.

`test_bds_object_storage_connection_details`

(required) Parameters required to validate access to the specified Object Storage bucket using the API key.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTO_SCALING_CONFIGURATION Function

Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`auto_scaling_configuration_id`

(required) Unique Oracle-assigned identifier of the autoscale configuration.

`update_auto_scaling_configuration_details`

(required) Details for update an autoscaling configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BDS_INSTANCE Function

Updates the Big Data Service cluster identified by the given ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`update_bds_instance_details`

(required) Details for the cluster to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BDS_METASTORE_CONFIGURATION Function

Update the BDS metastore configuration represented by the provided ID.

Syntax
```

```

Parameters

Parameter Description

`bds_instance_id`

(required) The OCID of the cluster.

`metastore_config_id`

(required) The metastore configuration ID

`update_bds_metastore_configuration_details`

(required) Request body for updating BDS metastore configuration.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://bigdataservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [BDS Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-7AE03597-4CCB-49C8-A832-86F26E4F206F)
- [ACTIVATE_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-890396D4-510A-4A63-BBB2-C6370FD729E3)
- [ADD_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-412A2DD0-2BD8-4FF4-BE15-4B853DBC6397)
- [ADD_BLOCK_STORAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-AD6118BC-3CEB-456E-80EE-4874EE9EB631)
- [ADD_CLOUD_SQL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-C3956309-6244-43C5-815C-D71A9727427F)
- [ADD_KAFKA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-5E3781EE-7C17-491E-8A54-3D3E461F01CC)
- [ADD_MASTER_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-999FD3B1-D123-4480-8587-D6012A866A81)
- [ADD_UTILITY_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-48A5B1A7-622E-4A23-98A9-9E17B1452977)
- [ADD_WORKER_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-1256AAA6-E204-41F7-A828-799852791BE3)
- [CERTIFICATE_SERVICE_INFO Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-8C94C127-174D-4F08-83B2-90C98EF34BA3)
- [CHANGE_BDS_INSTANCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-17CF622A-80D6-4B34-A488-6D51A5FD8CD0)
- [CHANGE_SHAPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-C2DCD494-657C-4599-A158-2E3EDF0770E4)
- [CREATE_BDS_API_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-1D59DF6E-7CFE-433E-ABED-BDD84AA34EFC)
- [CREATE_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-088C0D22-49B0-4991-8E24-F5F729AA6033)
- [CREATE_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-60FC1A8A-3704-442F-8911-5217A4331946)
- [DELETE_BDS_API_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-9796BBF6-511D-4266-9AA5-4DF882923525)
- [DELETE_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-6F53A0FD-EE5D-4413-BE68-BAE1E471E722)
- [DELETE_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-E19F064E-44B1-4DC2-AD68-A9DC1CB2D5BB)
- [DISABLE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-83103103-11A6-4A90-81D4-C38AD645BD96)
- [ENABLE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-F5E2EC93-25EA-4EF5-9F12-8F0FCB57F7A2)
- [EXECUTE_BOOTSTRAP_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-74012D52-AEB4-457B-BDF7-8F5A92EF1DE5)
- [GET_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-EE6DDF45-BFF7-4D94-8E9C-97235130ED49)
- [GET_BDS_API_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-67A08AB7-030C-414B-8234-F49DD25CAA81)
- [GET_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-C0A17DAA-FBCC-4B08-AAB1-6922FAC628A3)
- [GET_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-4515F44B-8B76-4492-9970-7E066392CB47)
- [GET_OS_PATCH_DETAILS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-834A1A75-AFE1-413B-A1B0-C31FB1D0FBAA)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-6CAD2A17-AA02-4F2A-8944-530004A30E6A)
- [INSTALL_OS_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-9C8FB2B5-B585-42A9-A95A-48BDE2D6552C)
- [INSTALL_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-841A2039-756E-40B3-9ECB-D5836FC7FA13)
- [LIST_AUTO_SCALING_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-6A7D538E-46B3-4319-9965-4AD0AE2FF22E)
- [LIST_BDS_API_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-E00A2493-4EE0-4726-92FD-18AA4C7DD0C6)
- [LIST_BDS_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-3AC57E1D-FB1C-4854-A909-896FE79CB2FB)
- [LIST_BDS_METASTORE_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-3C06C80C-905C-4611-905F-73654612DF42)
- [LIST_OS_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-87A5A7F3-DEC8-49E7-AA9D-BBFF17C87442)
- [LIST_PATCH_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-31FA4478-18B0-4B44-B6AD-0FD75FDD83B6)
- [LIST_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-C4B92854-EBEA-45DA-B5F0-B20BCF6E9665)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-EC74742C-48D0-45A1-820A-8EE936023B18)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-C136A9C8-14F2-464C-A326-D168E7809C56)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-EA3538C6-DE38-41AE-AE4B-EB2999BDCAFB)
- [REMOVE_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-283EBC04-534C-474D-B411-77B22E22205C)
- [REMOVE_CLOUD_SQL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-3299A111-142C-4AC4-B231-F07FC37F9ECC)
- [REMOVE_KAFKA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-3DC21071-712B-446C-B370-3F537824CD4B)
- [REMOVE_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-A944FACD-9700-4973-994D-21E813C8EFE6)
- [RENEW_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-8AD8648B-A782-405B-B685-DA6FFE938ED7)
- [RESTART_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-F90EB4CF-A224-4F63-91EA-975301AA888F)
- [START_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-8CA8CA40-C55B-46E2-B8B9-0FA70501A77D)
- [STOP_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-021CD247-5B49-4197-BD65-3FC0CF0C60F5)
- [TEST_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-6A202B19-FFAE-484B-8027-C328E2ED43E1)
- [TEST_BDS_OBJECT_STORAGE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-593F7412-8E73-4A32-B578-BEC417DCE2E2)
- [UPDATE_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-8C574B07-F2B4-4F2F-A62A-E56B7DD888A3)
- [UPDATE_BDS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-D7B7E3BA-84A6-4B29-A559-251C01F55267)
- [UPDATE_BDS_METASTORE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bds_bds.html#ADSDK-GUID-511E4040-6091-407D-A28C-EEC370E4717F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
