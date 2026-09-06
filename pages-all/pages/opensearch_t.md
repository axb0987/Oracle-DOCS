# OpenSearch Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#dcoc-content-body)

## OpenSearch Common Types

### DBMS_CLOUD_OCI_OPENSEARCH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_BACKUP_EVENT_DETAILS_T Type

Details about a cluster backup event.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The OCID of the OpenSearch cluster for the cluster backup.

`backup_state`

(required) The result of the cluster backup operation.

Allowed values are: 'DELETED', 'SUCCESS', 'FAILED'

`snapshot_name`

(optional) The name of the cluster backup.

`time_started`

(required) The date and time the cluster backup event started. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(required) The date and time the cluster backup event started. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`backup_size`

(optional) The cluster backup size in GB.

### DBMS_CLOUD_OCI_OPENSEARCH_BACKUP_OPENSEARCH_CLUSTER_DETAILS_T Type

Information about an OpenSearch cluster backup.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the cluster backup is located.

`display_name`

(required) The name of the cluster backup. Avoid entering confidential information.

### DBMS_CLOUD_OCI_OPENSEARCH_CHANGE_OPENSEARCH_CLUSTER_BACKUP_COMPARTMENT_DETAILS_T Type

Details about the compartment that the cluster backup should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the cluster backup should be moved.

### DBMS_CLOUD_OCI_OPENSEARCH_CHANGE_OPENSEARCH_CLUSTER_COMPARTMENT_DETAILS_T Type

Details about the compartment that the OpenSearch cluster should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the cluster should be moved.

### DBMS_CLOUD_OCI_OPENSEARCH_CREATE_OPENSEARCH_CLUSTER_DETAILS_T Type

The configuration details for a new OpenSearch cluster.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the cluster. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment to create the cluster in.

`software_version`

(required) The version of the software the cluster is running.

`master_node_count`

(required) The number of master nodes to configure for the cluster.

`master_node_host_type`

(required) The instance type for the cluster's master nodes.

Allowed values are: 'FLEX', 'BM'

`master_node_host_bare_metal_shape`

(optional) The bare metal shape for the cluster's master nodes.

`master_node_host_ocpu_count`

(required) The number of OCPUs to configure for the cluser's master nodes.

`master_node_host_memory_gb`

(required) The amount of memory in GB, to configure per node for the cluster's master nodes.

`data_node_count`

(required) The number of data nodes to configure for the cluster.

`data_node_host_type`

(required) TThe instance type for the cluster's data nodes.

Allowed values are: 'FLEX', 'BM'

`data_node_host_bare_metal_shape`

(optional) The bare metal shape for the cluster's data nodes.

`data_node_host_ocpu_count`

(required) The number of OCPUs to configure for the cluster's data nodes.

`data_node_host_memory_gb`

(required) The amount of memory in GB, to configure per node for the cluster's data nodes.

`data_node_storage_gb`

(required) The amount of storage in GB, to configure per node for the cluster's data nodes.

`opendashboard_node_count`

(required) The number of OpenSearch Dashboard nodes to configure for the cluster.

`opendashboard_node_host_ocpu_count`

(required) The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.

`opendashboard_node_host_memory_gb`

(required) The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.

`vcn_id`

(required) The OCID of the cluster's VCN.

`subnet_id`

(required) The OCID of the cluster's subnet.

`vcn_compartment_id`

(required) The OCID for the compartment where the cluster's VCN is located.

`subnet_compartment_id`

(required) The OCID for the compartment where the cluster's subnet is located.

`security_mode`

(optional) The security mode of the cluster.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'ENFORCING'

`security_master_user_name`

(optional) The name of the master user that are used to manage security config

`security_master_user_password_hash`

(optional) The password hash of the master user that are used to manage security config

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_ERROR_T Type

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

### DBMS_CLOUD_OCI_OPENSEARCH_EXPORT_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type

Information about the cluster backup to export.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment where the Object Storage resources for the cluster backup are located.

`object_storage_namespace`

(required) The Object Storage namespace for the cluster backup export operation.

`object_storage_bucket_name`

(required) The name of the Object Storage bucket for the cluster backup export operation.

`object_storage_prefix`

(optional) The prefix within the Object Storage bucket for the cluster backup export operation.

`snapshot_name`

(required) The name of the snapshot for the cluster backup export operation.

`repository_name`

(required) The name of the repository containing the snapshots for the cluster backup export operation.

`prefix`

(required) The prefix within object storage bucket for the cluster backup export operation.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_GET_MANIFEST_RESPONSE_T Type

The response returned for the get manifest call.

Syntax
```

```

Fields

Field Description

`serialized_manifest`

(optional) The serialized manifest response.

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_T Type

An OpenSearch cluster resource. An OpenSearch cluster is set of instances that provide OpenSearch functionality in OCI Search Service with OpenSearch. For more information, see[About Search Service with OpenSearch](https://docs.oracle.com/iaas/Content/search-opensearch/Concepts/ociopensearch.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the cluster.

`display_name`

(required) The name of the cluster. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment where the cluster is located.

`lifecycle_state`

(required) The current state of the cluster.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The amount of time in milliseconds since the cluster was created.

`time_updated`

(optional) The amount of time in milliseconds since the cluster was updated.

`time_deleted`

(optional) The amount of time in milliseconds since the cluster was updated.

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the cluster.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`software_version`

(required) The software version the cluster is running.

`total_storage_gb`

(required) The size in GB of the cluster's total storage.

`opensearch_fqdn`

(required) The fully qualified domain name (FQDN) for the cluster's API endpoint.

`opensearch_private_ip`

(required) The cluster's private IP address.

`opendashboard_fqdn`

(required) The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.

`opendashboard_private_ip`

(required) The private IP address for the cluster's OpenSearch Dashboard.

`master_node_count`

(required) The number of master nodes configured for the cluster.

`master_node_host_type`

(required) The instance type for the cluster's master nodes.

Allowed values are: 'FLEX', 'BM'

`master_node_host_bare_metal_shape`

(optional) The bare metal shape for the cluster's master nodes.

`master_node_host_ocpu_count`

(required) The number of OCPUs configured for cluster's master nodes.

`master_node_host_memory_gb`

(required) The amount of memory in GB, for the cluster's master nodes.

`data_node_count`

(required) The number of data nodes configured for the cluster.

`data_node_host_type`

(required) The instance type for the cluster's data nodes.

Allowed values are: 'FLEX', 'BM'

`data_node_host_bare_metal_shape`

(optional) The bare metal shape for the cluster's data nodes.

`data_node_host_ocpu_count`

(required) The number of OCPUs configured for the cluster's data nodes.

`data_node_host_memory_gb`

(required) The amount of memory in GB, for the cluster's data nodes.

`data_node_storage_gb`

(required) The amount of storage in GB, to configure per node for the cluster's data nodes.

`opendashboard_node_count`

(required) The number of OpenSearch Dashboard nodes configured for the cluster.

`opendashboard_node_host_ocpu_count`

(required) The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.

`opendashboard_node_host_memory_gb`

(required) The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.

`vcn_id`

(required) The OCID of the cluster's VCN.

`subnet_id`

(required) The OCID of the cluster's subnet.

`vcn_compartment_id`

(required) The OCID for the compartment where the cluster's VCN is located.

`subnet_compartment_id`

(required) The OCID for the compartment where the cluster's subnet is located.

`fqdn`

(optional) The fully qualified domain name (FQDN) for the cluster's API endpoint.

`availability_domains`

(required) The availability domains to distribute the cluser nodes across.

`security_mode`

(optional) The security mode of the cluster.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'ENFORCING'

`security_master_user_name`

(optional) The name of the master user that are used to manage security config

`security_master_user_password_hash`

(optional) The password hash of the master user that are used to manage security config

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_T Type

An OpenSearch cluster backup resource. An cluster is set of instances that provide OpenSearch functionality in OCI Search Service with OpenSearch. For more information, see[Cluster Backups](https://docs.oracle.com/iaas/Content/search-opensearch/Concepts/ociopensearchbackups.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the cluster backup.

`display_name`

(optional) The name of the cluster backup. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment where the cluster backup is located.

`backup_type`

(required) Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.

Allowed values are: 'SCHEDULED', 'MANUAL'

`time_created`

(optional) The date and time the cluster backup was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the cluster backup was updated. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The current state of the cluster backup.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) Additional information about the current lifecycle state of the cluster backup.

`source_cluster_id`

(required) The OCID of the source OpenSearch cluster for the cluster backup.

`namespace`

(optional) The Object Storage namespace for the cluster backup.

`bucket_name`

(optional) The name of the Object Storage bucket for the cluster backup.

`prefix`

(optional) The prefix within the Object Storage bucket for the cluster backup.

`time_expired`

(optional) The date and time the cluster backup expires. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`backup_size`

(optional) The size in GB of the cluster backup.

`source_cluster_display_name`

(optional) The name of the source OpenSearch cluster for the cluster backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_SUMMARY_T Type

The summary of information about an OpenSearch cluster backup.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the cluster backup.

`display_name`

(optional) The name of the cluster backup. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment where the cluster backup is located.

`backup_type`

(required) Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.

`source_cluster_id`

(required) The OCID of the source OpenSearch cluster for the cluster backup.

`time_created`

(optional) The date and time the cluster backup was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the cluster backup was updated. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The current state of the cluster backup.

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the cluster backup.

`time_expired`

(optional) The date and time the cluster backup expires. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`backup_size`

(optional) The size in GB of the cluster backup.

`source_cluster_display_name`

(optional) The name of the source OpenSearch cluster for the cluster backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opensearch_opensearch_cluster_backup_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_COLLECTION_T Type

The list of cluster backups returned in a cluster backup search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of cluster backups.

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_SUMMARY_T Type

The summary of information about an OpenSearch cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the cluster.

`display_name`

(optional) The name of the cluster. Avoid entering confidential information.

`compartment_id`

(required) The OCID for the compartment where the cluster is located.

`time_created`

(optional) The date and time the cluster was created. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the cluster was updated. Format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the cluster.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`software_version`

(required) The software version the cluster is running.

`total_storage_gb`

(required) The total amount of storage in GB, for the cluster.

`lifecycle_state`

(optional) The current state of the cluster.

`availability_domains`

(optional) The availability domains to distribute the cluser nodes across.

`security_mode`

(optional) The security mode of the cluster.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'ENFORCING'

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opensearch_opensearch_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_COLLECTION_T Type

The list of OpenSearch clusters returned in a cluster search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of clusters.

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_SUMMARY_T Type

A description of Opensearch versions

Syntax
```

```

Fields

Field Description

`version`

(required) The version of OpenSearch.

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opensearch_opensearch_versions_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_COLLECTION_T Type

The list of OpenSearch versions returned in an OpenSearch version search.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of OpenSearch versions.

### DBMS_CLOUD_OCI_OPENSEARCH_RESIZE_OPENSEARCH_CLUSTER_HORIZONTAL_DETAILS_T Type

The node count configuration to update on an existing OpenSearch cluster for[horizontal resizing](https://docs.oracle.com/iaas/Content/search-opensearch/Tasks/resizingacluster.htm#horizontalresize).

Syntax
```

```

Fields

Field Description

`master_node_count`

(optional) The number of master nodes to configure for the cluster.

`data_node_count`

(optional) The number of data nodes to configure for the cluster.

`opendashboard_node_count`

(optional) The number of OpenSearch Dashboard nodes to configure for the cluster.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_RESIZE_OPENSEARCH_CLUSTER_VERTICAL_DETAILS_T Type

The OCPU and memory configuration to update on an existing OpenSearch cluster for[vertical resizing](https://docs.oracle.com/iaas/Content/search-opensearch/Tasks/resizingacluster.htm#vertical).

Syntax
```

```

Fields

Field Description

`master_node_host_ocpu_count`

(optional) The number of OCPUs to configure for the cluster's master nodes.

`master_node_host_memory_gb`

(optional) The amount of memory in GB, to configure for the cluster's master nodes.

`data_node_host_ocpu_count`

(optional) The number of OCPUs to configure for the cluster's data nodes.

`data_node_host_memory_gb`

(optional) The amount of memory in GB, to configure for the cluster's data nodes.

`data_node_storage_gb`

(optional) The amount of storage in GB, to configure per node for the cluster's data nodes.

`opendashboard_node_host_ocpu_count`

(optional) The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.

`opendashboard_node_host_memory_gb`

(optional) The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_RESTORE_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type

Information about the source OpenSearch cluster to restore the cluster backup from.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The name of the source OpenSearch cluster for the cluster backup.

### DBMS_CLOUD_OCI_OPENSEARCH_RESTORE_OPENSEARCH_CLUSTER_DETAILS_T Type

Information about the OpenSearch cluster backup to restore.

Syntax
```

```

Fields

Field Description

`opensearch_cluster_backup_id`

(required) The OCID of the cluster backup to restore.

`compartment_id`

(required) The OCID of the compartment where the cluster backup is located.

`prefix`

(optional) The prefix for the indices in the cluster backup.

### DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CHECKIN_DETAILS_T Type

Information about the update checkin event.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The OCID of the OpenSearch cluster.

### DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CLUSTER_HARDENED_IMAGE_DETAILS_T Type

Information about the cluster's hardened image.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The OCID of the OpenSearch cluster.

### DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CLUSTER_STATUS_DETAILS_T Type

Information about the update cluster event.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The OCID of the OpenSearch cluster.

`lifecycle_state`

(required) The state of the cluster after the cluster was updated.

### DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type

Information about the cluster backup to update.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the cluster backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_OPENSEARCH_CLUSTER_DETAILS_T Type

The configuration to update on an existing OpenSearch cluster. Software version and security config are not allowed to be updated at the same time.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the cluster. Avoid entering confidential information.

`software_version`

(optional)

`security_mode`

(optional) The security mode of the cluster.

Allowed values are: 'DISABLED', 'PERMISSIVE', 'ENFORCING'

`security_master_user_name`

(optional) The name of the master user that are used to manage security config

`security_master_user_password_hash`

(optional) The password hash of the master user that are used to manage security config

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_RESOURCE_T Type

A resource that is created or operated on by an asynchronous operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The OCID of the resource the work request affects.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_opensearch_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of operation that spawned the work request.

Allowed values are: 'CREATE_OPENSEARCH_CLUSTER', 'UPDATE_OPENSEARCH_CLUSTER', 'DELETE_OPENSEARCH_CLUSTER', 'MOVE_OPENSEARCH_CLUSTER', 'RESTORE_OPENSEARCH_CLUSTER', 'BACKUP_OPENSEARCH_CLUSTER', 'UPDATE_OPENSEARCH_CLUSTER_BACKUP', 'MOVE_OPENSEARCH_CLUSTER_BACKUP', 'DELETE_OPENSEARCH_CLUSTER_BACKUP', 'UPDATE_OPENSEARCH_CLUSTER_SECURITY_CONFIG'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources that are affected by the work request.

`percent_complete`

(required) The percentage complete of the operation tracked by the work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_started`

(optional) The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_opensearch_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequests.

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. For a list of error codes, see[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable string describing the error that occurred.

`l_timestamp`

(required) The day and time the error occured, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_opensearch_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_COLLECTION_T Type

The list of work request errors returned in a work request error search.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The day and time the log message was written, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_opensearch_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

The list of work request log entries returned in a work request log search.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request log entries.

- [OpenSearch Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-5A37D3FC-CB95-40E8-A741-7CC4D5C10FF7)
- [DBMS_CLOUD_OCI_OPENSEARCH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-9E40475A-C564-4C21-BB9F-2AD44C3ECBB1)
- [DBMS_CLOUD_OCI_OPENSEARCH_BACKUP_EVENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-1CADF505-0AD5-491C-9A1F-A22EE9101A1F)
- [DBMS_CLOUD_OCI_OPENSEARCH_BACKUP_OPENSEARCH_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-2FE27820-8D15-4611-AF97-8AF789E8BE06)
- [DBMS_CLOUD_OCI_OPENSEARCH_CHANGE_OPENSEARCH_CLUSTER_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-1AA7BF16-257C-4875-87A0-7DFEA3B55AA8)
- [DBMS_CLOUD_OCI_OPENSEARCH_CHANGE_OPENSEARCH_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-640F1D51-E93E-4019-9F82-814A5387CD99)
- [DBMS_CLOUD_OCI_OPENSEARCH_CREATE_OPENSEARCH_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-7A020708-22F5-4C22-997D-2C3669111639)
- [DBMS_CLOUD_OCI_OPENSEARCH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-16247CC7-FECD-4926-82D9-E13E87EE0F8E)
- [DBMS_CLOUD_OCI_OPENSEARCH_EXPORT_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-FEA7C35B-2850-43B6-8FA9-93CC9E16E400)
- [DBMS_CLOUD_OCI_OPENSEARCH_GET_MANIFEST_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-E527AE5D-1AEA-496F-AE17-E97322FD188A)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-3A95916E-1D05-4275-BB2C-F40E4FB78F93)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-38B87F06-A64B-4A8C-B8B7-E2D6B3BF2DA2)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-546E257C-E3E4-4ED2-8896-8A28EACDDC47)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-5F4B170A-2B11-477E-BA8D-DE7DF7A939BE)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_BACKUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-8DD80184-593D-48D2-A1C3-3B0E01411312)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-0B0076FE-DC94-4810-B23C-8439FE237838)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-ED546839-5C95-4CCA-9928-29A4C0139C4F)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-EE17FE16-A79F-4A8C-AC3D-CDF1B9DF3C10)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-DBC144DC-D2F1-4966-B2DC-2D807BB337E8)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-8BF0EFA2-71C3-42FA-8555-4ED6DA63E3FC)
- [DBMS_CLOUD_OCI_OPENSEARCH_OPENSEARCH_VERSIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-50C7EE2A-9484-4031-837C-63AF022EA59F)
- [DBMS_CLOUD_OCI_OPENSEARCH_RESIZE_OPENSEARCH_CLUSTER_HORIZONTAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-93D0A026-B428-4A60-A814-5A1F0CF5D8BA)
- [DBMS_CLOUD_OCI_OPENSEARCH_RESIZE_OPENSEARCH_CLUSTER_VERTICAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-94E5384C-9C09-421A-92AD-561359AF783E)
- [DBMS_CLOUD_OCI_OPENSEARCH_RESTORE_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-8FEA301F-8117-44C3-AC3C-9D28F1BD8696)
- [DBMS_CLOUD_OCI_OPENSEARCH_RESTORE_OPENSEARCH_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-2E653FA8-7C0E-41BA-AFA2-3756E3E79AF2)
- [DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CHECKIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-EF7AC510-D0EA-4F8C-BD52-4FC1F3E83775)
- [DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CLUSTER_HARDENED_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-79972036-D2A1-480D-819A-A8E766D3CC22)
- [DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_CLUSTER_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-82E09655-4DB7-4D80-9014-2BEF420BEDD2)
- [DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_OPENSEARCH_CLUSTER_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-0DAD0D12-00D1-46DA-BF7B-E9A7BAB4F353)
- [DBMS_CLOUD_OCI_OPENSEARCH_UPDATE_OPENSEARCH_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-64A588F0-4D33-4FC9-A515-2A68C5427B81)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-74AA3B7D-470B-45FF-A521-9F6A8A495582)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-D3182569-F09C-4A8B-83A4-82DDAB4A3B73)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-2AA279DC-F7A4-453D-8E7F-BEBECF756266)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-1EAA938A-A2CF-4EA1-A8BE-1100222F5F5A)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-2C674A77-448F-4FBB-9AB5-C57029CCEAF1)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-64E409A7-0931-41CC-8662-5A2012ABF089)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-F4B427C5-297B-4152-86BA-5BCA84CE4228)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-03F19715-A6BD-488F-82DC-713CB6ECD12F)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-45B1E15E-2D4C-4067-B6C4-E5EF7F30C3B8)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-368FCFC2-DB80-476C-A73B-15E757F8D90D)
- [DBMS_CLOUD_OCI_OPENSEARCH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opensearch_t.html#ADSDK-GUID-FA21431D-8EA6-42D6-8080-1E834791B690)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
