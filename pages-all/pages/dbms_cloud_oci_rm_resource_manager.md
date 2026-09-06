# Resource Manger Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#dcoc-content-body)

## Resource Manger Functions

Package: DBMS_CLOUD_OCI_RM_RESOURCE_MANAGER

### CANCEL_JOB Function

Indicates the intention to cancel the specified job. Cancellation of the job is not immediate, and may be delayed, or may not happen at all. You can optionally choose forced cancellation by setting `isForced` to true. A forced cancellation can result in an incorrect state file. For example, the state file might not reflect the exact state of the provisioned resources.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`is_forced`

(optional) Indicates whether a forced cancellation is requested for the job while it was running. A forced cancellation can result in an incorrect state file. For example, the state file might not reflect the exact state of the provisioned resources.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CONFIGURATION_SOURCE_PROVIDER_COMPARTMENT Function

Moves a configuration source provider into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`change_configuration_source_provider_compartment_details`

(required) Defines the properties of changeConfigurationSourceProviderCompartment operation.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves a private endpoint to a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`change_private_endpoint_compartment_details`

(required) Defines the properties of changePrivateEndpointCompartment operation.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_STACK_COMPARTMENT Function

Moves a stack (and its associated jobs) into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`change_stack_compartment_details`

(required) Defines the properties of changeStackCompartment operation.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TEMPLATE_COMPARTMENT Function

Moves a template into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`change_template_compartment_details`

(required) The details for moving a template to a different compartment.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONFIGURATION_SOURCE_PROVIDER Function

Creates a configuration source provider in the specified compartment. For more information, see[To create a configuration source provider](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#CreateConfigurationSourceProvider).

Syntax
```

```

Parameters

Parameter Description

`create_configuration_source_provider_details`

(required) The properties for creating a ConfigurationSourceProvider.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB Function

Creates a job.

Syntax
```

```

Parameters

Parameter Description

`create_job_details`

(required) The properties for a request to create a job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PRIVATE_ENDPOINT Function

Creates a private endpoint in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_private_endpoint_details`

(required) Creation details for a private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STACK Function

Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see[Creating Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack.htm).

Syntax
```

```

Parameters

Parameter Description

`create_stack_details`

(required) The properties for creating a stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TEMPLATE Function

Creates a private template in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_template_details`

(required) The configuration details for creating a template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONFIGURATION_SOURCE_PROVIDER Function

Deletes the specified configuration source provider.

Syntax
```

```

Parameters

Parameter Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PRIVATE_ENDPOINT Function

Deletes the specified private endpoint.

Syntax
```

```

Parameters

Parameter Description

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STACK Function

Deletes the specified stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TEMPLATE Function

Deletes the specified template.

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_STACK_DRIFT Function

Checks drift status for the specified stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`detect_stack_drift_details`

(optional) The details for detecting drift in a stack

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIGURATION_SOURCE_PROVIDER Function

Gets the properties of the specified configuration source provider.

Syntax
```

```

Parameters

Parameter Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB Function

Gets the properties of the specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_DETAILED_LOG_CONTENT Function

Returns the Terraform detailed log content for the specified job in plain text.[Learn about Terraform detailed log.](https://www.terraform.io/docs/internals/debugging.html)

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_LOGS Function

Returns console log entries for the specified job in JSON format.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`l_type`

(optional) A filter that returns only logs of a specified type.

`level_greater_than_or_equal_to`

(optional) A filter that returns only log entries that match a given severity level or greater.

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`timestamp_greater_than_or_equal_to`

(optional) Time stamp specifying the lower time limit for which logs are returned in a query. Format is defined by RFC3339. Example: `2020-01-01T12:00:00.000Z`

`timestamp_less_than_or_equal_to`

(optional) Time stamp specifying the upper time limit for which logs are returned in a query. Format is defined by RFC3339. Example: `2020-02-01T12:00:00.000Z`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_LOGS_CONTENT Function

Returns the raw log file for the specified job in text format. The file includes a maximum of 100,000 log entries.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_TF_CONFIG Function

Returns the Terraform configuration for the specified job in zip format. If no zip file is found, returns an error.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_TF_PLAN Function

Returns the output of the specified Terraform plan job in binary or JSON format. For information about running Terraform plan jobs, see[Creating Plan Jobs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job.htm).

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`tf_plan_format`

(optional) The output format of the Terraform plan.

Allowed values are: 'BINARY', 'JSON'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_TF_STATE Function

Returns the Terraform state for the specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_ENDPOINT Function

Gets the specified private endpoint.

Syntax
```

```

Parameters

Parameter Description

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REACHABLE_IP Function

Gets the reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint. Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint.

Syntax
```

```

Parameters

Parameter Description

`private_ip`

(required) The IP address of the resource in the private subnet.

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STACK Function

Gets the specified stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STACK_TF_CONFIG Function

Returns the Terraform configuration file for the specified stack in zip format. Returns an error if no zip file is found.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STACK_TF_STATE Function

Returns the Terraform state for the specified stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TEMPLATE Function

Gets the specified template.

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TEMPLATE_LOGO Function

Returns the Terraform logo file in .logo format for the specified template. Returns an error if no logo file is found.

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TEMPLATE_TF_CONFIG Function

Returns the Terraform configuration file in zip format for the specified template. Returns an error if no zip file is found.

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Returns the specified work request.

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

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONFIGURATION_SOURCE_PROVIDERS Function

Lists configuration source providers according to the specified filter. - For `compartmentId`, lists all configuration source providers in the matching compartment. - For `configurationSourceProviderId`, lists the matching configuration source provider.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`configuration_source_provider_id`

(optional) A filter to return only configuration source providers that match the provided[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.

`sort_by`

(optional) The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`config_source_provider_type`

(optional) A filter to return only configuration source providers of the specified type (GitHub or GitLab).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_ASSOCIATED_RESOURCES Function

Gets the list of resources associated with the specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`terraform_resource_type`

(optional) A filter to return only specified resource types. For more information about resource types supported for the Oracle Cloud Infrastructure[OCI] provider, see [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_OUTPUTS Function

Gets the list of outputs associated with the specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOBS Function

Lists jobs according to the specified filter. By default, the list is ordered by time created. - To list all jobs in a stack, provide the stack[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). - To list all jobs in a compartment, provide the compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). - To return a specific job, provide the job[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). (Equivalent to`GET_STACK`Function.)

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`stack_id`

(optional) The stack[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)on which to filter.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)on which to query for jobs.

`lifecycle_state`

(optional) A filter that returns all resources that match the specified lifecycle state. The state value is case-insensitive. Allowable values: - ACCEPTED - IN_PROGRESS - FAILED - SUCCEEDED - CANCELING - CANCELED

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.

`sort_by`

(optional) The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRIVATE_ENDPOINTS Function

Lists private endpoints according to the specified filter. - For `compartmentId`, lists all private endpoints in the matching compartment. - For `privateEndpointId`, lists the matching private endpoint.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`sort_by`

(optional) The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_DISCOVERY_SERVICES Function

Returns a list of supported services for[Resource Discovery](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resource-discovery.htm). For reference on service names, see the[Terraform provider documentation](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STACK_ASSOCIATED_RESOURCES Function

Gets the list of resources associated with the specified stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`terraform_resource_type`

(optional) A filter to return only specified resource types. For more information about resource types supported for the Oracle Cloud Infrastructure[OCI] provider, see [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STACK_RESOURCE_DRIFT_DETAILS Function

Lists drift status details for each resource defined in the specified stack. The drift status details for a given resource indicate differences, if any, between the actual state and the expected (defined) state for that resource. The drift status details correspond to the specified work request (`workRequestId`). If no work request is specified, then the drift status details correspond to the latest completed work request for the stack.

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`work_request_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`resource_drift_status`

(optional) A filter that returns only resources that match the given drift status. The value is case-insensitive. Allowable values - - NOT_CHECKED - MODIFIED - IN_SYNC - DELETED

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STACKS Function

Lists stacks according to the specified filter. - If called using the compartment ID, returns all stacks in the specified compartment. - If called using the stack ID, returns the specified stack. (See also`GET_STACK`Function.)

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)on which to query for a stack.

`lifecycle_state`

(optional) A filter that returns only those resources that match the specified lifecycle state. The state value is case-insensitive. For more information about stack lifecycle states, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates). Allowable values: - CREATING - ACTIVE - DELETING - DELETED - FAILED

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.

`sort_by`

(optional) The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TEMPLATE_CATEGORIES Function

Lists template categories.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TEMPLATES Function

Lists templates according to the specified filter. The attributes `compartmentId` and `templateCategoryId` are required unless `templateId` is specified.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`template_category_id`

(optional) Unique identifier for the template category. Possible values are `0` (Quickstarts), `1` (Service), `2` (Architecture), and `3` (Private). Template category labels are displayed in the Console page listing templates. Quickstarts, Service, and Architecture templates (categories 0, 1, and 2) are available in all compartments. Each private template (category 3) is available in the compartment where it was created.

`template_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.

`sort_by`

(optional) The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TERRAFORM_VERSIONS Function

Returns a list of supported Terraform versions for use with stacks.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(optional) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in the specified compartment or for the specified resource.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that exist in the compartment, identified by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIGURATION_SOURCE_PROVIDER Function

Updates the properties of the specified configuration source provider. For more information, see[To edit a configuration source provider](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#EditConfigurationSourceProvider).

Syntax
```

```

Parameters

Parameter Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`update_configuration_source_provider_details`

(required) Updated information provided for the ConfigurationSourceProvider.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB Function

Updates the specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`update_job_details`

(required) Updates properties for the specified job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PRIVATE_ENDPOINT Function

Updates the specified private endpoint.

Syntax
```

```

Parameters

Parameter Description

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`update_private_endpoint_details`

(required) Update details for a private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STACK Function

Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see[Updating Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack.htm).

Syntax
```

```

Parameters

Parameter Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`update_stack_details`

(required) The details for updating a stack.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TEMPLATE Function

Updates the specified template.

Syntax
```

```

Parameters

Parameter Description

`template_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the template.

`update_template_details`

(required) The details for updating a template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://resourcemanager.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Resource Manger Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-58491D22-9E72-4995-BDA4-7CC64EEC591F)
- [CANCEL_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-AABEB8C9-3F22-4895-BBB4-D17784B77D45)
- [CHANGE_CONFIGURATION_SOURCE_PROVIDER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-7C8A0B1E-0356-42A7-B295-EBE79A1576C4)
- [CHANGE_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-81F02174-E933-4D9A-B161-A92D2B4DB206)
- [CHANGE_STACK_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-B07966CA-F0D1-4237-8AAB-D92B93A684EE)
- [CHANGE_TEMPLATE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-DC17F19D-6CF5-4A97-8000-178B4E6E1A37)
- [CREATE_CONFIGURATION_SOURCE_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-E4D59771-B469-4B20-BCCA-4DDC9E93B68E)
- [CREATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-562AD284-5F87-47A8-B895-EB6333BD6E60)
- [CREATE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-539535F5-49BE-44FA-A333-B9A5D56222CB)
- [CREATE_STACK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-1C2BD5C7-438C-4A69-8310-D13B78A23FF4)
- [CREATE_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-73E85F54-1B14-4122-9B8B-562D2E041528)
- [DELETE_CONFIGURATION_SOURCE_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-4ED144E1-61F5-4357-855D-D5A2F2A24E28)
- [DELETE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-2346A643-AF71-40CE-8AE8-519142A8E7B3)
- [DELETE_STACK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-B4D26E01-EE06-4042-A8EB-F82E68AD2621)
- [DELETE_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-B6A3BEF6-828A-48F5-8FA9-613C87776F06)
- [DETECT_STACK_DRIFT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-7920A08C-7E99-4E19-AB7E-91BD74866789)
- [GET_CONFIGURATION_SOURCE_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-7AC50C52-B7E9-498E-955C-1C64E041F4E3)
- [GET_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-1A25DB02-BF01-4456-B2B0-772C6C188A71)
- [GET_JOB_DETAILED_LOG_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-2931C48F-EA17-47EE-8122-58D916643235)
- [GET_JOB_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-1BFFD20D-D583-4914-8F29-B2AC2EC9816C)
- [GET_JOB_LOGS_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-1279A916-5FDF-40E3-85CD-B4C3E0D2CBBD)
- [GET_JOB_TF_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-8572D9B5-60B1-4088-B83D-9696F73591B0)
- [GET_JOB_TF_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-2956A7EF-6613-4FDE-8CA9-3133C27F8677)
- [GET_JOB_TF_STATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-A0A3E291-00DC-4897-8E23-AF4B8BBD26C3)
- [GET_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-97987C58-5D2D-410E-AEAB-F580FF2A93F9)
- [GET_REACHABLE_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-3A72D835-55D9-4E3A-91A9-598D0FF7595A)
- [GET_STACK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-359BC71C-DCA5-4D02-B502-95FC6FA5399D)
- [GET_STACK_TF_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-55FBE7E9-07DB-47ED-8E76-AC61A5361B2B)
- [GET_STACK_TF_STATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-56C4D32B-4FE1-4A69-838C-2609F00F2CAD)
- [GET_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-46A23713-3482-4B4F-B569-5A1C2D0D3E16)
- [GET_TEMPLATE_LOGO Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-779684C3-4E0D-4E55-8BD8-EE0C76BBF71E)
- [GET_TEMPLATE_TF_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-57E9FCBD-856D-4F9E-9E49-28A5E30CBAB3)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-89EF68AE-6853-4427-9A98-CA11A55C83C4)
- [LIST_CONFIGURATION_SOURCE_PROVIDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-DD5D8098-0CE9-424A-8845-2E874B38CBAB)
- [LIST_JOB_ASSOCIATED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-D0FCDB89-9204-4C4D-B59B-447D0B036A19)
- [LIST_JOB_OUTPUTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-AB270E76-AF48-4122-8E7A-845616A1C568)
- [LIST_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-C1985286-71D5-459C-863F-41F26216160B)
- [LIST_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-1B307FD6-C9B9-4F17-A73C-AF0F5E577027)
- [LIST_RESOURCE_DISCOVERY_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-5E902A0C-9E7D-407E-858F-209C8F5DF9AB)
- [LIST_STACK_ASSOCIATED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-79895E0E-59FC-440C-B993-78F2EF17556B)
- [LIST_STACK_RESOURCE_DRIFT_DETAILS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-C32A133F-B47D-4849-9F2F-6AD46DBF5B77)
- [LIST_STACKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-A69D14A1-039F-49BF-BA3E-FAC39A7AD4CB)
- [LIST_TEMPLATE_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-018DD28B-A116-4B01-A813-C4D5856125CA)
- [LIST_TEMPLATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-AA3C90C3-8C23-4C86-9917-8D2E18657D18)
- [LIST_TERRAFORM_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-B96BF094-19C6-40DA-AF30-DEE0E38416D7)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-F6D60D37-6FE3-4885-8D62-3E4A32FD818F)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-0BD4CFFD-6602-4CF3-B363-4EADF47D1911)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-3E0FD89B-D0DA-44FF-ADC2-C3C49622AB54)
- [UPDATE_CONFIGURATION_SOURCE_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-A7DEA246-507F-4710-983A-966755C9ED48)
- [UPDATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-16AA2628-8F36-40A4-B95C-1B24C03DDBF7)
- [UPDATE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-F439E43A-9FB2-48E9-9F0C-6D8066C27F82)
- [UPDATE_STACK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-70023BC4-C562-42D1-9F63-0C2CA13087E7)
- [UPDATE_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rm_resource_manager.html#ADSDK-GUID-722462B5-AC68-4382-BBEA-3CEEAE06F494)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
