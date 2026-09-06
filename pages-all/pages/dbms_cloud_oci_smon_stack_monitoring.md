# Stack Monitoring Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#dcoc-content-body)

## Stack Monitoring Functions

Package: DBMS_CLOUD_OCI_SMON_STACK_MONITORING

### ASSOCIATE_MONITORED_RESOURCES Function

Create an association between two monitored resources. Associations can be created between resources from different compartments as long they are in same tenancy. User should have required access in both the compartments.

Syntax
```

```

Parameters

Parameter Description

`associate_monitored_resources_details`

(required) Details to create association between two resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CONFIG_COMPARTMENT Function

Moves the configuration item to another compartment. Basically, this will disable any configuration for this configuration type in thie compartment, and will enable it in the new one. For example, if for a HOST resource type, the configuration with AUTO_PROMOTE in the configuration type and TRUE as value is moved, automatic discovery will not take place in this compartment any more, but in the new one. So this operation will have the same effect as deleting the configuration item in the old compartment and recreating it in another compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`config_id`

(required) Unique Config identifier.

`change_config_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_METRIC_EXTENSION_COMPARTMENT Function

Moves a Metric Extension resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`change_metric_extension_compartment_details`

(required) The information required to change compartment of given Metric Extension resource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MONITORED_RESOURCE_COMPARTMENT Function

Moves a monitored resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`change_monitored_resource_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MONITORED_RESOURCE_TASK_COMPARTMENT Function

Moves a stack monitoring resource task from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_task_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of stack monitoring resource task.

`change_monitored_resource_task_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BASELINEABLE_METRIC Function

Creates the specified Baseline-able metric

Syntax
```

```

Parameters

Parameter Description

`create_baselineable_metric_details`

(required) Baseline metric

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONFIG Function

Creates a configuration item, for example to define whether resources of a specific type should be discovered automatically. For example, when a new Management Agent gets registered in a certain compartment, this Management Agent can potentially get promoted to a HOST resource. The configuration item will determine if HOST resources in the selected compartment will be discovered automatically.

Syntax
```

```

Parameters

Parameter Description

`create_config_details`

(required) Details for the new configuration.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DISCOVERY_JOB Function

API to create discovery Job and submit discovery Details to agent.

Syntax
```

```

Parameters

Parameter Description

`create_discovery_job_details`

(required) Summary of source and credential discovery details.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_METRIC_EXTENSION Function

Creates a new metric extension resource for a given compartment

Syntax
```

```

Parameters

Parameter Description

`create_metric_extension_details`

(required) Details required for creating new Metric Extension

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MONITORED_RESOURCE Function

Creates a new monitored resource for the given resource type with the details and submits a work request for promoting the resource to agent. Once the resource is successfully added to agent, resource state will be marked active.

Syntax
```

```

Parameters

Parameter Description

`create_monitored_resource_details`

(required) Details for the new monitored resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`external_resource_id`

(optional) Generally used by DBaaS to send the Database OCID stored on the DBaaS. The same will be passed to resource service to enable Stack Monitoring Service on DBM. This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource. If this header is not set as part of the request, then an id will be generated and stored for the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MONITORED_RESOURCE_TASK Function

Create a new stack monitoring resource task.

Syntax
```

```

Parameters

Parameter Description

`create_monitored_resource_task_details`

(required) Details to create the new stack monitoring resource task.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MONITORED_RESOURCE_TYPE Function

Creates a new monitored resource type.

Syntax
```

```

Parameters

Parameter Description

`create_monitored_resource_type_details`

(required) Details for the new monitored resource type.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BASELINEABLE_METRIC Function

Deletes the Baseline-able metric for the given id

Syntax
```

```

Parameters

Parameter Description

`baselineable_metric_id`

(required) Identifier for the metric

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONFIG Function

Deletes a configuration identified by the id.

Syntax
```

```

Parameters

Parameter Description

`config_id`

(required) Unique Config identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DISCOVERY_JOB Function

Deletes a DiscoveryJob by identifier

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The Discovery Job ID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_METRIC_EXTENSION Function

Deletes a metric extension by identifier

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MONITORED_RESOURCE Function

Delete monitored resource by the given identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). By default, only the specified resource is deleted. If the parameter 'isDeleteMembers' is set to true, then the member resources will be deleted too. If the operation fails partially, the deleted entries will not be rolled back.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_delete_members`

(optional) If this query parameter is specified and set to true, all the member resources will be deleted before deleting the specified resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MONITORED_RESOURCE_TYPE Function

Deletes a monitored resource type by identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_type_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource type.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_DATABASE Function

Disable external database resource monitoring. All the references in DBaaS, DBM and resource service will be deleted as part of this operation.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_METRIC_EXTENSION Function

Submits a request to disable matching metric extension Id for the given Resource IDs

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`disable_metric_extension_details`

(required) The list of Resource IDs for which given metric extension needs to be disabled

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISASSOCIATE_MONITORED_RESOURCES Function

Removes associations between two monitored resources.

Syntax
```

```

Parameters

Parameter Description

`disassociate_monitored_resources_details`

(required) Disassociate resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_METRIC_EXTENSION Function

Submits a request to enable matching metric extension Id for the given Resource IDs

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`enable_metric_extension_details`

(required) The list of Resource IDs for which given metric extension needs to be enabled

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EVALUATE_BASELINEABLE_METRIC Function

Evaluates metric for anomalies for the given data points

Syntax
```

```

Parameters

Parameter Description

`evaluate_baselineable_metric_details`

(required) Metric details

`baselineable_metric_id`

(required) Identifier for the metric

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_METRIC_EXTENSION Function

Export generates a template used to create new metric extension resources similar to matching metric extension id. Response is a file that contains metric extension definition with placeholders for fields to be changed.

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BASELINEABLE_METRIC Function

Get the Baseline-able metric for the given id

Syntax
```

```

Parameters

Parameter Description

`baselineable_metric_id`

(required) Identifier for the metric

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIG Function

Gets the details of a configuration.

Syntax
```

```

Parameters

Parameter Description

`config_id`

(required) Unique Config identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DISCOVERY_JOB Function

API to get the details of discovery Job by identifier.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The Discovery Job ID

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_METRIC_EXTENSION Function

Gets a Metric Extension by identifier

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MONITORED_RESOURCE Function

Get monitored resource for the given identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MONITORED_RESOURCE_TASK Function

Gets stack monitoring resource task details by identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_task_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of stack monitoring resource task.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MONITORED_RESOURCE_TYPE Function

Gets a monitored resource type by identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_type_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource type.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BASELINEABLE_METRICS Function

List of summary of baseline-able metrics for a given resource group if specified.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`resource_group`

(optional) Resource Group

`name`

(optional) Metric Name

`metric_namespace`

(optional) A filter to return monitored resource types that has the matching namespace.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id`

(optional) The ID of the compartment in which data is listed.

`baselineable_metric_id`

(optional) Identifier for the metric

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order is ascending.

Allowed values are: 'name', 'namespace', 'resourceGroup'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONFIGS Function

Get a list of configurations in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which data is listed.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`l_type`

(optional) A filter to return only configuration items for a given config type.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the Config.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' and 'configType' is ascending.

Allowed values are: 'timeCreated', 'configType', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_JOB_LOGS Function

API to get all the logs of a Discovery Job.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The Discovery Job ID

`log_type`

(optional) The log type like INFO, WARNING, ERROR, SUCCESS

Allowed values are: 'INFO', 'WARNING', 'ERROR', 'SUCCESS'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for logType is ascending.

Allowed values are: 'timeCreated', 'logType'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_JOBS Function

API to get the details of all Discovery Jobs.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which data is listed.

`name`

(optional) A filter to return only discovery jobs that match the entire resource name given.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending. Default order for resourceName is ascending.

Allowed values are: 'timeUpdated', 'resourceName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_METRIC_EXTENSIONS Function

Returns a list of metric extensions

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which data is listed.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for resources is ascending.

Allowed values are: 'NAME', 'TIME_CREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`resource_type`

(optional) A filter to return resources based on resource type.

`name`

(optional) A filter to return resources based on name.

`status`

(optional) A filter to return resources based on status e.g. Draft or Published

Allowed values are: 'DRAFT', 'PUBLISHED'

`lifecycle_state`

(optional) A filter to return metric extensions based on Lifecycle State

Allowed values are: 'ACTIVE', 'DELETED'

`enabled_on_resource_id`

(optional) A filter to return metric extensions based on input resource Id on which metric extension is enabled

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MONITORED_RESOURCE_TASKS Function

Returns a list of stack monitoring resource tasks in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for which stack monitoring resource tasks should be listed.

`status`

(optional) A filter to return only resources that matches with lifecycleState given.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeUpdated' is descending.

Allowed values are: 'timeUpdated'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MONITORED_RESOURCE_TYPES Function

Returns list of resource types accessible to the customer. There are two types of resource types - System resource types and User resource types. System resource types are available out of the box in the stack monitoring resource service and are accessible to all the tenant users. User resource types are created in the context of a tenancy and are visible only for the tenancy. By default, both System resource types and User resource types are returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy for which monitored resource types should be listed.

`name`

(optional) A filter to return monitored resource types that match exactly with the resource type name given.

`status`

(optional) A filter to return only resources that matches with lifecycleState given.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_exclude_system_types`

(optional) A filter to exclude system resource types. If set to true, system resource types will be excluded.

`metric_namespace`

(optional) A filter to return monitored resource types that has the matching namespace.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeUpdated' is descending. Default order for 'name' is ascending.

Allowed values are: 'timeUpdated', 'name'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to return and should be a query string parameter called \"fields\" of an array type, provide the values as enums, and use collectionFormat. MonitoredResourceType Id, name and compartment will be added by default.

`exclude_fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return all the information except the fields requested to be excluded (excludeFields) by the client. In this mechanism, the client sends the exclude field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to exlude and to return and should be a query string parameter called \"excludeFields\" of an array type, provide the values as enums, and use collectionFormat.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MONITORED_RESOURCES Function

Returns a list of monitored resources.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which data is listed.

`name`

(optional) A filter to return resources that match exact resource name.

`work_request_id`

(optional) A filter to return resources which were impacted as part of this work request identifier.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for resources is ascending.

Allowed values are: 'NAME', 'TIME_CREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending. If no value is specified timestamp is default.

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending. If no value is specified timestamp is default.

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the compartment in which data is listed.

`work_request_id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MANAGE_LICENSE Function

Each resource is assigned a license based on which features are enabled for it. User is charged differently based on license. Specify the license type to be updated for the parent resource in the topology. The license type value is propagated to the member resources as well. Member resource is a resource which has \"contains\" association with the resource.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`manage_license_details`

(required) New license information.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_METRIC_EXTENSION Function

Publish the Metric Extension identified by the id

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_MONITORED_RESOURCES_SUMMARIZED_COUNT Function

Gets resource count based on the aggregation criteria specified using \"groupBy\" parameter.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which data is listed.

`group_by`

(optional) The field to group by. Default group by is 'resourceType'.

Allowed values are: 'resourceType', 'license', 'parentResourceId'

`license`

(optional) Filter to return resource counts that match with the given licence edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`resource_type`

(optional) A filter to return resource counts that match exact resource type.

`sort_by`

(optional) If this query parameter is specified, the result is sorted by this query parameter value.

Allowed values are: 'count'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_ASSOCIATED_RESOURCES Function

List all associated resources recursively up-to a specified level, for the monitored resources of type specified.

Syntax
```

```

Parameters

Parameter Description

`search_associated_resources_details`

(required) Search Criteria for the listing the monitored resources for given type and compartmentId.

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to return and should be a query string parameter called \"fields\" of an array type, provide the values as enums, and use collectionFormat.

`exclude_fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return all the information except the fields requested to be excluded (excludeFields) by the client. In this mechanism, the client sends the exclude field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to exlude and to return and should be a query string parameter called \"excludeFields\" of an array type, provide the values as enums, and use collectionFormat.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_MONITORED_RESOURCE_ASSOCIATIONS Function

Search associations in the given compartment based on the search criteria.

Syntax
```

```

Parameters

Parameter Description

`search_monitored_resource_associations_details`

(required) Search criteria for listing monitored resource associations.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_MONITORED_RESOURCE_MEMBERS Function

List the member resources for the given monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`search_monitored_resource_members_details`

(required) Search criteria for listing member monitored resources.

`sort_by`

(optional) If this query parameter is specified, the result is sorted by this query parameter value.

Allowed values are: 'resourceName', 'resourceType', 'sourceResourceType'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_MONITORED_RESOURCES Function

Gets a list of all monitored resources in a compartment for the given search criteria.

Syntax
```

```

Parameters

Parameter Description

`search_monitored_resources_details`

(required) Search Criteria for listing monitored resources.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to return and should be a query string parameter called \"fields\" of an array type, provide the values as enums, and use collectionFormat.

`exclude_fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs, to return all the information except the fields requested to be excluded (excludeFields) by the client. In this mechanism, the client sends the exclude field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to exlude and to return and should be a query string parameter called \"excludeFields\" of an array type, provide the values as enums, and use collectionFormat.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_METRIC_EXTENSION Function

Performs test of Metric Extension on a specific resource Id

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`test_metric_extension_details`

(required) It contains OCID of resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AND_PROPAGATE_TAGS Function

Provided tags will be added or updated in the existing list of tags for the affected resources. Resources to be updated are identified based on association types specified. If association types not specified, then tags will be updated only for the resource identified by the given monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`update_and_propagate_tags_details`

(required) The tags to be updated.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BASELINEABLE_METRIC Function

Updates the Baseline-able metric for the given id

Syntax
```

```

Parameters

Parameter Description

`update_baselineable_metric_details`

(required) Baseline metric

`baselineable_metric_id`

(required) Identifier for the metric

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIG Function

Updates the configuration identified by the id given.

Syntax
```

```

Parameters

Parameter Description

`config_id`

(required) Unique Config identifier.

`update_config_details`

(required) The details of the configuration to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_METRIC_EXTENSION Function

Updates the Metric Extension

Syntax
```

```

Parameters

Parameter Description

`metric_extension_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the metric extension resource.

`update_metric_extension_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MONITORED_RESOURCE Function

Update monitored resource by the given identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Note that \"properties\" object, if specified, will entirely replace the existing object, as part this operation.

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource.

`update_monitored_resource_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MONITORED_RESOURCE_TASK Function

Update stack monitoring resource task by the given identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_task_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of stack monitoring resource task.

`update_monitored_resource_task_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MONITORED_RESOURCE_TYPE Function

Update the Monitored Resource Type identified by the identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`monitored_resource_type_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored resource type.

`update_monitored_resource_type_details`

(required) The information to be updated for the given resource type id.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://stack-monitoring.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Stack Monitoring Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4CCC0B5B-3BDA-4FB3-8CC8-CB35C7BE4458)
- [ASSOCIATE_MONITORED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7D25766E-92F6-4781-94CB-49D2C6A19258)
- [CHANGE_CONFIG_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-162EA9F8-207A-4E00-A792-8CF573E85CC0)
- [CHANGE_METRIC_EXTENSION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-1E408B5B-F001-4F94-B9EF-05B1205C9434)
- [CHANGE_MONITORED_RESOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-AE71838E-C33F-4679-BBD3-085BC0235590)
- [CHANGE_MONITORED_RESOURCE_TASK_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-005E695B-6B64-4195-BF5B-D95BC20CE865)
- [CREATE_BASELINEABLE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-DB207F40-B215-43F0-8D98-A347FD4FEF0C)
- [CREATE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F5859436-8FB5-42A4-A57A-D26FCCB011C8)
- [CREATE_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-296E3F26-5FF5-45D2-8442-CF3FFB4BCF7E)
- [CREATE_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-5B3333A4-2EAA-4DA2-BC0F-CCD6A66DAE9A)
- [CREATE_MONITORED_RESOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E8F59148-F7F5-4A6F-9337-E64130865B12)
- [CREATE_MONITORED_RESOURCE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-2219106C-E6B7-4349-A393-4641C0881ABC)
- [CREATE_MONITORED_RESOURCE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-AF16458C-4C71-4FED-9425-6B60433DE99C)
- [DELETE_BASELINEABLE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4A34BF23-3807-4F5E-9345-8EF979D9D94C)
- [DELETE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F01FF7EA-062D-4FF8-AFB7-3E0C5F43937F)
- [DELETE_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-17BF7630-D83D-4E67-8311-B34A5F79A0BC)
- [DELETE_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E4511E75-0915-42BC-98F6-5B22269E7147)
- [DELETE_MONITORED_RESOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-55799A7C-4318-493F-B628-5F8CA1091CBB)
- [DELETE_MONITORED_RESOURCE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-852C3E7F-A35D-4167-AC6E-9C7D1BF997CF)
- [DISABLE_EXTERNAL_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4A6B79D4-FC88-40F6-8CD9-2C5420187AE0)
- [DISABLE_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-99C7218E-43C5-4518-BE23-BFFFC95678BC)
- [DISASSOCIATE_MONITORED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-58A393DE-B779-4272-880A-32604DE135FB)
- [ENABLE_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-52368C7E-9E12-4052-8F9C-2F53AFD349CB)
- [EVALUATE_BASELINEABLE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E4F3F8F6-D193-473E-9E8B-0F25068AB501)
- [EXPORT_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E74F0760-99F8-4069-BB8F-45AF049D82D5)
- [GET_BASELINEABLE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7424AFF6-9ACE-46D8-8E6B-B4A035F4C275)
- [GET_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-02E14DA0-25DA-48C9-860B-80C5D14D1DC9)
- [GET_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F412A78C-64E0-47CF-AD6F-43638984E218)
- [GET_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-211B46E5-E6FA-4310-8D61-2E68369903CA)
- [GET_MONITORED_RESOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7D3C23FB-7703-44E0-97A7-5C4A0BAE07B6)
- [GET_MONITORED_RESOURCE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-559E17D6-AD27-4D85-B432-66F08A1F9442)
- [GET_MONITORED_RESOURCE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E36C6524-7236-4593-9B03-88FBCE3C2D72)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7282886C-BB00-4956-AB96-2821A4A11A31)
- [LIST_BASELINEABLE_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4A052A26-A33B-4154-A890-6626C2321CD3)
- [LIST_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4EFFF10B-2E24-42B7-95FA-9F9E64B46344)
- [LIST_DISCOVERY_JOB_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-C4C691BC-F6A6-469D-8CFD-FC24CDFF1E9C)
- [LIST_DISCOVERY_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-077B5C4B-D11C-4411-8364-86D1F4C4D2C1)
- [LIST_METRIC_EXTENSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-CF334119-176B-402E-B774-0771DB40BBB4)
- [LIST_MONITORED_RESOURCE_TASKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-AFAD26EF-F1AF-4012-AB13-7744DFBB4AAB)
- [LIST_MONITORED_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-5AF7B804-8CE9-4606-B5DE-E2C5ABCBB9F6)
- [LIST_MONITORED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-3AA4D3C6-C5C0-41FD-B235-1709BD4E5728)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-3C62327B-FA18-4D0E-BEA1-AA3F8C12C858)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7EFE20F4-26D4-4D8A-A506-E155D35E5E2C)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-408D3FD9-5845-488C-A883-952FC123BF07)
- [MANAGE_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F803DCEB-6CE9-4285-A4E6-5CBA29B16FF6)
- [PUBLISH_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-D906EEB5-7657-4C51-A825-7BB11074268F)
- [REQUEST_MONITORED_RESOURCES_SUMMARIZED_COUNT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F1B2613E-5433-46C2-B328-93DB0F7F5BD1)
- [SEARCH_ASSOCIATED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-BC1B59F6-94FC-41EA-85D4-79396DA7F706)
- [SEARCH_MONITORED_RESOURCE_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-BBC01D23-56E0-419A-BD85-6F057690D9A3)
- [SEARCH_MONITORED_RESOURCE_MEMBERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-DEE6CB1A-E602-4E2A-A543-0322A89202E6)
- [SEARCH_MONITORED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-1B60F9B6-D4E4-4FC8-86AA-2E83FB3C2E4A)
- [TEST_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-E966B7F6-7AD0-467A-B49E-35003962E008)
- [UPDATE_AND_PROPAGATE_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-F7AD1DEC-9666-4A66-A187-A23F25B29978)
- [UPDATE_BASELINEABLE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-4D47C00C-DE46-4251-ACEA-ECA73496C475)
- [UPDATE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-7070F157-21F2-47F7-83DE-4EFB9268533F)
- [UPDATE_METRIC_EXTENSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-095F76CA-430E-4885-9D1B-BC0F353BD078)
- [UPDATE_MONITORED_RESOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-6DB45D98-3824-404A-BBB5-ECA87369BBEC)
- [UPDATE_MONITORED_RESOURCE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-D1608543-FFD1-4A02-854A-17062A179CD4)
- [UPDATE_MONITORED_RESOURCE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smon_stack_monitoring.html#ADSDK-GUID-72D5F8A6-9242-4232-BE39-EA9A5E63F1C4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
