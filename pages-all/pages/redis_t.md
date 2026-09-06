# Redis Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#dcoc-content-body)

## Redis Common Types

### DBMS_CLOUD_OCI_REDIS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_CHANGE_REDIS_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the compartment into which the Redis cluster should be moved.

### DBMS_CLOUD_OCI_REDIS_CREATE_REDIS_CLUSTER_DETAILS_T Type

The configuration details for a new Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the compartment that contains the Redis cluster.

`node_count`

(required) The number of nodes in the Redis cluster.

`software_version`

(required) The Redis version that the cluster is running.

`node_memory_in_g_bs`

(required) The amount of memory allocated to the Redis cluster's nodes, in gigabytes.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster's subnet.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_REDIS_ERROR_T Type

Specifies details for an error.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string for the error that occured.

### DBMS_CLOUD_OCI_REDIS_NODE_T Type

The details of each node in the Redis cluster.

Syntax
```

```

Fields

Field Description

`private_endpoint_fqdn`

(required) The fully qualified domain name (FQDN) of the API endpoint to access a specific node.

`private_endpoint_ip_address`

(required) The private IP address of the API endpoint to access a specific node.

`display_name`

(required) A user-friendly name of a Redis cluster node.

### DBMS_CLOUD_OCI_REDIS_NODE_TBL Type

Nested table type of dbms_cloud_oci_redis_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_NODE_COLLECTION_T Type

The collection of Redis cluster nodes.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of node objects.

### DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_T Type

A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the compartment that contains the Redis cluster.

`lifecycle_state`

(optional) The current state of the Redis cluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, the message might provide actionable information for a resource in `FAILED` state.

`node_count`

(required) The number of nodes in the Redis cluster.

`node_memory_in_g_bs`

(required) The amount of memory allocated to the Redis cluster's nodes, in gigabytes.

`primary_fqdn`

(required) The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's primary node.

`primary_endpoint_ip_address`

(required) The private IP address of the API endpoint for the Redis cluster's primary node.

`replicas_fqdn`

(required) The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's replica nodes.

`replicas_endpoint_ip_address`

(required) The private IP address of the API endpoint for the Redis cluster's replica nodes.

`software_version`

(required) The Redis version that the cluster is running.

Allowed values are: 'V7_0_5'

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster's subnet.

`time_created`

(optional) The date and time the Redis cluster was created. An[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The date and time the Redis cluster was updated. An[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)formatted datetime string.

`node_collection`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_SUMMARY_T Type

Summary of information about a Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the compartment that contains the Redis cluster.

`lifecycle_state`

(optional) The current state of the Redis cluster.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, the message might provide actionable information for a resource in `FAILED` state.

`node_count`

(required) The number of nodes in the Redis cluster.

`node_memory_in_g_bs`

(required) The amount of memory allocated to the Redis cluster's nodes, in gigabytes.

`primary_fqdn`

(required) The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's primary node.

`primary_endpoint_ip_address`

(required) The private IP address of the API endpoint for the Redis cluster's primary node.

`replicas_fqdn`

(required) The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's replica nodes.

`replicas_endpoint_ip_address`

(required) The private IP address of the API endpoint for the Redis cluster's replica nodes.

`software_version`

(required) The Redis version that the cluster is running.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the Redis cluster's subnet.

`time_created`

(optional) The date and time the Redis cluster was created. An[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The date and time the Redis cluster was updated. An[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_redis_redis_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_COLLECTION_T Type

A list of Redis clusters that match filter criteria, if any. A Redis cluster is a memory-based storage solution. For more information, see[OCI Caching Service with Redis](https://docs.oracle.com/iaas/Content/redis/home.htm).

Syntax
```

```

Fields

Field Description

`items`

(required) The list of Redis clusters.

### DBMS_CLOUD_OCI_REDIS_UPDATE_REDIS_CLUSTER_DETAILS_T Type

The configuration to update for an existing Redis cluster.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`node_count`

(optional) The number of nodes in the Redis cluster.

`node_memory_in_g_bs`

(optional) The amount of memory allocated to the Redis cluster's nodes, in gigabytes.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_RESOURCE_T Type

The resources that are affected by the work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the `IN_PROGRESS` state until work is complete for that resource at which point it will transition to `CREATED`, `UPDATED`, or `DELETED`, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the resource the work request affects.

`entity_uri`

(optional) The URI path that you can use for a GET to access the resource metadata

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_redis_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of operation that spawned the work request.

Allowed values are: 'CREATE_REDIS_CLUSTER', 'UPDATE_REDIS_CLUSTER', 'DELETE_REDIS_CLUSTER', 'MOVE_REDIS_CLUSTER', 'FAILOVER_REDIS_CLUSTER', 'CREATE_REDIS_CONFIG_SET', 'UPDATE_REDIS_CONFIG_SET', 'DELETE_REDIS_CONFIG_SET', 'MOVE_REDIS_CONFIG_SET'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by the work request.

`percent_complete`

(required) The percentage complete of the operation tracked by the work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_started`

(optional) The date and time the work request was started, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_finished`

(optional) The date and time the work request completed, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed at[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string for the error that occured.

`l_timestamp`

(required) The time and time the error occured.

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_redis_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of errors for a work request.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request errors.

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written.

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_redis_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of logs for the specified work request.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request logs.

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of operation that spawned the work request.

Allowed values are: 'CREATE_REDIS_CLUSTER', 'UPDATE_REDIS_CLUSTER', 'DELETE_REDIS_CLUSTER', 'MOVE_REDIS_CLUSTER', 'FAILOVER_REDIS_CLUSTER', 'CREATE_REDIS_CONFIG_SET', 'UPDATE_REDIS_CONFIG_SET', 'DELETE_REDIS_CONFIG_SET', 'MOVE_REDIS_CONFIG_SET'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle)of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_started`

(optional) The date and time the work request was started, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_finished`

(optional) The date and time the work request completed, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_redis_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_COLLECTION_T Type

A list of work requests.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work requests.

- [Redis Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-D29DE7C6-B7FE-42C6-AEA0-720099CF7499)
- [DBMS_CLOUD_OCI_REDIS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-F8B3B05A-64E4-4553-9D5C-FCD3EC7936D2)
- [DBMS_CLOUD_OCI_REDIS_CHANGE_REDIS_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-B0DB271E-1F24-4CFF-8332-B0A87119DE66)
- [DBMS_CLOUD_OCI_REDIS_CREATE_REDIS_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-C315F9FC-07F0-4800-A975-43B1873B2118)
- [DBMS_CLOUD_OCI_REDIS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-3189015B-DB09-464C-8225-9D5F76DE2240)
- [DBMS_CLOUD_OCI_REDIS_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-416FA2B5-35E7-4C5E-831B-AB653BE0DDAA)
- [DBMS_CLOUD_OCI_REDIS_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-93FB246A-B21C-4B5C-B37C-79B6361A29DE)
- [DBMS_CLOUD_OCI_REDIS_NODE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-67EA1256-FDD3-43E2-83E1-5382339DBDA9)
- [DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-43EED178-E91B-4713-BD8A-571658F02AF9)
- [DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-B3A3A195-01B9-449F-AA34-0B9B85BE2DC9)
- [DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-66E5F2AD-F99F-4DA4-9575-A2BD2AE74C84)
- [DBMS_CLOUD_OCI_REDIS_REDIS_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-C31E879D-49AE-4A45-9582-E1F5347DE22F)
- [DBMS_CLOUD_OCI_REDIS_UPDATE_REDIS_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-5720F1ED-E244-47D2-BE72-22E7A8ED8EBD)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-8B1971EA-C593-4D7D-86F8-D80D90A7B57E)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-FA496C57-AD64-4729-873A-9268D1AB1083)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-4813C2D0-989E-4AE6-8E32-2AC4C0417E50)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-40736003-17ED-424A-9EBF-99F50ACFE153)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-C0BB3FE1-F166-46C7-91AD-47E2289CA0D8)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-029CCF66-D83C-4191-AE62-A4AAECDF188C)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-3721E839-A323-4C6B-AEE5-53EA7B171890)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-625712DC-6963-41CC-B548-5C63FBF058CF)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-CCC1F197-34A8-4E8D-9023-7B06D1B87921)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-78E96E90-7E2F-4FD9-BB54-014C100F9D9F)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-4E55BEE9-48F8-42ED-BECC-1EE557C550AA)
- [DBMS_CLOUD_OCI_REDIS_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/redis_t.html#ADSDK-GUID-888180CE-99AB-4150-86AA-BCC38ED4D5D6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
