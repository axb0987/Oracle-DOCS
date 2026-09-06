# Data Integration Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#dcoc-content-body)

## Data Integration Functions

Package: DBMS_CLOUD_OCI_DI_DATA_INTEGRATION

### CHANGE_COMPARTMENT Function

Moves a workspace to a specified compartment.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`change_compartment_details`

(required) The information needed to move a workspace to a specified compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DIS_APPLICATION_COMPARTMENT Function

Moves a DIS Application to a specified compartment.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`dis_application_id`

(required) The OCID of the DIS Application.

`change_dis_application_compartment_details`

(required) The information needed to move a DIS Application to a specified compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION Function

Creates an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_application_details`

(required) The details needed to create an application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION_DETAILED_DESCRIPTION Function

Creates detailed description for an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_application_detailed_description_details`

(required) Detailed description of an application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION Function

Creates a connection under an existing data asset.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_connection_details`

(required) The information needed to create a connection.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION_VALIDATION Function

Creates a connection validation.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_connection_validation_details`

(required) The information needed to validate a connection.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COPY_OBJECT_REQUEST Function

Copy Metadata Object.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_copy_object_request_details`

(required) The details needed to copy metadata object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_ASSET Function

Creates a data asset with default connection.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_data_asset_details`

(required) The information needed to create a data asset.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_FLOW Function

Creates a new data flow in a project or folder ready for performing data integrations.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_data_flow_details`

(required) The details needed to create a new data flow.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_FLOW_VALIDATION Function

Accepts the data flow definition in the request payload and creates a data flow validation.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_data_flow_validation_details`

(required) The information needed to create the data flow validation for the data flow object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DIS_APPLICATION Function

Creates a DIS Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_dis_application_details`

(required) The details needed to create a DIS application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DIS_APPLICATION_DETAILED_DESCRIPTION Function

Creates detailed description for an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_dis_application_detailed_description_details`

(required) Detailed description of an application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENTITY_SHAPE Function

Creates the data entity shape using the shape from the data asset.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`schema_resource_name`

(required) The schema resource name used for retrieving schemas.

`create_entity_shape_details`

(required) The details needed to create the data entity shape.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXPORT_REQUEST Function

Export Metadata Object

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_export_request_details`

(required) The details needed to export metadata object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_PUBLICATION Function

Publish a DataFlow in a OCI DataFlow application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`create_external_publication_details`

(required) Details needed to publish a task to OCI DataFlow application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_PUBLICATION_VALIDATION Function

Validates a specific task.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`create_external_publication_validation_details`

(required) The information needed to create a task validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FOLDER Function

Creates a folder in a project or in another folder, limited to two levels of folders. | Folders are used to organize your design-time resources, such as tasks or data flows.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_folder_details`

(required) The details needed to create a folder.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FUNCTION_LIBRARY Function

Creates a function library in a project or in another function library, limited to two levels of function libraries. | FunctionLibraries are used to organize your design-time resources, such as tasks or data flows.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_function_library_details`

(required) The details needed to create a function Library.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IMPORT_REQUEST Function

Import Metadata Object

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_import_request_details`

(required) The details needed to import metadata object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PATCH Function

Creates a patch in an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_patch_details`

(required) Detailed needed to create a patch in an application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PIPELINE Function

Creates a new pipeline in a project or folder ready for performing task orchestration.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_pipeline_details`

(required) The details needed to create a new pipeline.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PIPELINE_VALIDATION Function

Accepts the data flow definition in the request payload and creates a pipeline validation.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_pipeline_validation_details`

(required) The information needed to create the data flow validation for the pipeline object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROJECT Function

Creates a project. Projects are organizational constructs within a workspace that you use to organize your design-time resources, such as tasks or data flows. Projects can be organized into folders.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_project_details`

(required) The details needed to create a project in a workspace.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SCHEDULE Function

Endpoint to create a new schedule

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_schedule_details`

(required) Request body parameter for Schedule details

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TASK Function

Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_task_details`

(required) The details needed to create a new task.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TASK_RUN Function

Creates a data integration task run for the specified task.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_task_run_details`

(required) The details needed to create a task run.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TASK_SCHEDULE Function

Endpoint to be used create TaskSchedule.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`create_task_schedule_details`

(required) Request body parameter for TaskSchedule details

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TASK_VALIDATION Function

Validates a specific task.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_task_validation_details`

(required) The information needed to create a task validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_USER_DEFINED_FUNCTION Function

Creates a new UserDefinedFunction in a function library ready for performing data integrations.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_user_defined_function_details`

(required) The details needed to create a new UserDefinedFunction.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_USER_DEFINED_FUNCTION_VALIDATION Function

Accepts the UserDefinedFunction definition in the request payload and creates a UserDefinedFunction validation.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`create_user_defined_function_validation_details`

(required) The information needed to create the UserDefinedFunction validation for the UserDefinedFunction object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_WORKSPACE Function

Creates a new Data Integration workspace ready for performing data integration tasks. To retrieve the OCID for the new workspace, use the opc-work-request-id returned by this API and call the`GET_WORK_REQUEST`Function API.

Syntax
```

```

Parameters

Parameter Description

`create_workspace_details`

(required) The information needed to create a new Data Integration workspace.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION Function

Removes an application using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION_DETAILED_DESCRIPTION Function

Deletes detailed description of an Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION Function

Removes a connection using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION_VALIDATION Function

Deletes a connection validation.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_validation_key`

(required) The key of the connection validation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COPY_OBJECT_REQUEST Function

Delete copy object request using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`copy_object_request_key`

(required) The key of the object to be copied, for example this could be the key of a project.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_ASSET Function

Removes a data asset using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_asset_key`

(required) The data asset key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_FLOW Function

Removes a data flow from a project or folder using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_flow_key`

(required) The data flow key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_FLOW_VALIDATION Function

Removes a data flow validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_flow_validation_key`

(required) The key of the dataflow validation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DIS_APPLICATION Function

Removes a DIS application using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`dis_application_id`

(required) The OCID of the DIS Application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DIS_APPLICATION_DETAILED_DESCRIPTION Function

Deletes detailed description of an Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXPORT_REQUEST Function

Delete export object request using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`export_request_key`

(required) The key of the object export object request

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_PUBLICATION Function

Removes a published object using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`external_publications_key`

(required) The external published object key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_PUBLICATION_VALIDATION Function

Removes a task validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`external_publication_validation_key`

(required) The external published object key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FOLDER Function

Removes a folder from a project using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`folder_key`

(required) The folder key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FUNCTION_LIBRARY Function

Removes a Function Library from a project using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`function_library_key`

(required) The functionLibrary key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IMPORT_REQUEST Function

Delete import object request using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`import_request_key`

(required) The key of the object export object request

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PATCH Function

Removes a patch using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`patch_key`

(required) The patch key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PIPELINE Function

Removes a pipeline from a project or folder using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`pipeline_key`

(required) The pipeline key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PIPELINE_VALIDATION Function

Removes a pipeline validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`pipeline_validation_key`

(required) The key of the pipeline validation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROJECT Function

Removes a project from the workspace using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`project_key`

(required) The project key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SCHEDULE Function

Endpoint to delete schedule.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`schedule_key`

(required) Schedule Key

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TASK Function

Removes a task using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TASK_RUN Function

Deletes a task run using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_run_key`

(required) The task run key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TASK_SCHEDULE Function

Endpoint to delete TaskSchedule.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_schedule_key`

(required) TaskSchedule Key

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TASK_VALIDATION Function

Removes a task validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_validation_key`

(required) The task validation key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_USER_DEFINED_FUNCTION Function

Removes a UserDefinedFunction from a function library using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`user_defined_function_key`

(required) The user defined function key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_USER_DEFINED_FUNCTION_VALIDATION Function

Removes a UserDefinedFunction validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`user_defined_function_validation_key`

(required) The key of the userDefinedFunction validation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORKSPACE Function

Deletes a Data Integration workspace resource using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`quiesce_timeout`

(optional) Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.

`is_force_operation`

(optional) Used to force close down the workspace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION Function

Retrieves an application using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION_DETAILED_DESCRIPTION Function

Retrieves detailed description of an Application

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPOSITE_STATE Function

This endpoint can be used to get composite state for a given aggregator

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`aggregator_key`

(required) Unique key of the aggregator for which we want to get the Composite State

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION Function

Retrieves the connection details using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION_VALIDATION Function

Retrieves a connection validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_validation_key`

(required) The key of the connection validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COPY_OBJECT_REQUEST Function

This endpoint can be used to get the summary/details of object being copied.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`copy_object_request_key`

(required) The key of the object to be copied, for example this could be the key of a project.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COUNT_STATISTIC Function

Retrieves statistics on a workspace. It returns an object with an array of property values, such as the number of projects, | applications, data assets, and so on.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`count_statistic_key`

(required) A unique key of the container object, such as workspace, project, and so on, to count statistics for. The statistics is fetched for the given key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_ASSET Function

Retrieves details of a data asset using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_asset_key`

(required) The data asset key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_ENTITY Function

Retrieves the data entity details with the given name from live schema.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`schema_resource_name`

(required) The schema resource name used for retrieving schemas.

`data_entity_key`

(required) The key of the data entity.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_FLOW Function

Retrieves a data flow using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_flow_key`

(required) The data flow key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`expand_references`

(optional) Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. &lt;br&gt;&lt;br&gt;&lt;B&gt;Example:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?expandReferences=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_FLOW_VALIDATION Function

Retrieves a data flow validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_flow_validation_key`

(required) The key of the dataflow validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPENDENT_OBJECT Function

Retrieves the details of a dependent object from an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`dependent_object_key`

(required) The dependent object key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DIS_APPLICATION Function

Retrieves an application using the specified OCID.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`dis_application_id`

(required) The OCID of the DIS Application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DIS_APPLICATION_DETAILED_DESCRIPTION Function

Retrieves detailed description of an Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXPORT_REQUEST Function

This endpoint can be used to get the summary/details of object being exported.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`export_request_key`

(required) The key of the object export object request

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_PUBLICATION Function

Retrieves a publshed object in an task using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`external_publications_key`

(required) The external published object key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_PUBLICATION_VALIDATION Function

Retrieves an external publication validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`external_publication_validation_key`

(required) The external published object key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FOLDER Function

Retrieves a folder using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`folder_key`

(required) The folder key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`projection`

(optional) This parameter allows users to specify which view of the object to return. CHILD_COUNT_STATISTICS - This option is used to get statistics on immediate children of the object by their type.

Allowed values are: 'CHILD_COUNT_STATISTICS'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUNCTION_LIBRARY Function

Retrieves a Function Library using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`function_library_key`

(required) The functionLibrary key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`projection`

(optional) This parameter allows users to specify which view of the object to return. CHILD_COUNT_STATISTICS - This option is used to get statistics on immediate children of the object by their type.

Allowed values are: 'CHILD_COUNT_STATISTICS'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IMPORT_REQUEST Function

This endpoint can be used to get the summary/details of object being imported.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`import_request_key`

(required) The key of the object export object request

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PATCH Function

Retrieves a patch in an application using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`patch_key`

(required) The patch key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PIPELINE Function

Retrieves a pipeline using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`pipeline_key`

(required) The pipeline key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`expand_references`

(optional) Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. &lt;br&gt;&lt;br&gt;&lt;B&gt;Example:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?expandReferences=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PIPELINE_VALIDATION Function

Retrieves a pipeline validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`pipeline_validation_key`

(required) The key of the pipeline validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROJECT Function

Retrieves a project using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`project_key`

(required) The project key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`projection`

(optional) This parameter allows users to specify which view of the object to return. CHILD_COUNT_STATISTICS - This option is used to get statistics on immediate children of the object by their type.

Allowed values are: 'CHILD_COUNT_STATISTICS'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLISHED_OBJECT Function

Retrieves the details of a published object from an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`published_object_key`

(required) The published object key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`expand_references`

(optional) Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. &lt;br&gt;&lt;br&gt;&lt;B&gt;Example:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?expandReferences=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REFERENCE Function

Retrieves a reference in an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`reference_key`

(required) The reference key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RUNTIME_OPERATOR Function

Retrieves a runtime operator using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`runtime_pipeline_key`

(required) Runtime Pipeline Key

`runtime_operator_key`

(required) Runtime Operator Key

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RUNTIME_PIPELINE Function

Retrieves a runtime pipeline using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`runtime_pipeline_key`

(required) Runtime Pipeline Key

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`expand_references`

(optional) Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. &lt;br&gt;&lt;br&gt;&lt;B&gt;Example:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?expandReferences=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEDULE Function

Retrieves schedule by schedule key

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`schedule_key`

(required) Schedule Key

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEMA Function

Retrieves a schema that can be accessed using the specified connection.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`schema_resource_name`

(required) The schema resource name used for retrieving schemas.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TASK Function

Retrieves a task using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`expand_references`

(optional) Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. &lt;br&gt;&lt;br&gt;&lt;B&gt;Example:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?expandReferences=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TASK_RUN Function

Retrieves a task run using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_run_key`

(required) The task run key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TASK_SCHEDULE Function

Endpoint used to get taskSchedule by its key

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_schedule_key`

(required) TaskSchedule Key

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TASK_VALIDATION Function

Retrieves a task validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_validation_key`

(required) The task validation key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TEMPLATE Function

This endpoint can be used to get an application template using a key.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`template_id`

(required) The OCID of the template.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_DEFINED_FUNCTION Function

Retrieves a UserDefinedFunction using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`user_defined_function_key`

(required) The user defined function key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_DEFINED_FUNCTION_VALIDATION Function

Retrieves a UserDefinedFunction validation using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`user_defined_function_validation_key`

(required) The key of the userDefinedFunction validation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Retrieves the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous work request to retrieve.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORKSPACE Function

Retrieves a Data Integration workspace using the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATIONS Function

Retrieves a list of applications and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`name`

(optional) Used to filter by the name of the object.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the published object.

`fields`

(optional) Specifies the fields to get for an object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTION_VALIDATIONS Function

Retrieves a list of connection validations within the specified workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTIONS Function

Retrieves a list of all connections.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_asset_key`

(required) Used to filter by the data asset key of the object.

`name`

(optional) Used to filter by the name of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Specifies the fields to get for an object.

`l_type`

(optional) Type of the object to filter the results with.

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COPY_OBJECT_REQUESTS Function

This endpoint can be used to get the list of copy object requests.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`name`

(optional) Used to filter by the name of the object.

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`copy_status`

(optional) Specifies copy status to use, either - ALL, SUCCESSFUL, IN_PROGRESS, QUEUED, FAILED .

Allowed values are: 'IN_PROGRESS', 'SUCCESSFUL', 'QUEUED', 'TERMINATING', 'TERMINATED', 'FAILED', 'ALL'

`projection`

(optional) This parameter allows users to specify which view of the copy object response to return. SUMMARY - Summary of the copy object response will be returned. This is the default option when no value is specified. DETAILS - Details of copy object response will be returned. This will include details of all the objects to be copied.

Allowed values are: 'SUMMARY', 'DETAILS'

`time_started_in_millis`

(optional) Specifies start time of a copy object request.

`time_ended_in_millis`

(optional) Specifies end time of a copy object request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_ASSETS Function

Retrieves a list of all data asset summaries.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Specifies the fields to get for an object.

`l_type`

(optional) Type of the object to filter the results with.

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`name`

(optional) Used to filter by the name of the object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_ENTITIES Function

Lists a summary of data entities from the data asset using the specified connection.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`schema_resource_name`

(required) The schema resource name used for retrieving schemas.

`name`

(optional) Used to filter by the name of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`l_type`

(optional) Type of the object to filter the results with.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Specifies the fields to get for an object.

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`name_list`

(optional) Used to filter by the name of the object.

`is_pattern`

(optional) This parameter can be used to specify whether entity search type is pattern search or not.

`include_types`

(optional) Artifact type which needs to be listed while listing Artifacts.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_FLOW_VALIDATIONS Function

Retrieves a list of data flow validations within the specified workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_FLOWS Function

Retrieves a list of data flows in a project or folder.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`folder_id`

(optional) Unique key of the folder.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPENDENT_OBJECTS Function

Retrieves a list of all dependent objects for a specific application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the published object.

`l_type`

(optional) Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. For Data Integration APIs, a filter based on type Task is used.

`type_in_subtree`

(optional) Used in association with type parameter. If value is true, then type all sub types of the given type parameter is considered. If value is false, then sub types are not considered. Default is false.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DIS_APPLICATION_TASK_RUN_LINEAGES Function

This endpoint can be used to list Task Run Lineages within a given time window.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`dis_application_id`

(required) The OCID of the DIS Application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`filter`

(optional) This filter parameter can be used to filter by model specific queryable fields of the object &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:-&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?filter=status eq Failed&lt;/B&gt; returns all objects that have a status field with value Failed&lt;/li&gt; &lt;/ul&gt;

`time_updated_greater_than`

(optional) This parameter allows users to get objects which were updated after a certain time. The format of timeUpdatedGreaterThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_updated_greater_than_or_equal_to`

(optional) This parameter allows users to get objects which were updated after and at a certain time. The format of timeUpdatedGreaterThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_upated_less_than`

(optional) This parameter allows users to get objects which were updated before a certain time. The format of timeUpatedLessThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_upated_less_than_or_equal_to`

(optional) This parameter allows users to get objects which were updated before and at a certain time. The format of timeUpatedLessThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DIS_APPLICATIONS Function

Retrieves a list of DIS Applications in a compartment and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`compartment_id`

(required) OCID of the compartment for which the list of DIS Applications is to be retrieved.

`name`

(optional) Used to filter by the name of the object.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the published object.

`fields`

(optional) Specifies the fields to get for an object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXPORT_REQUESTS Function

This endpoint can be used to get the list of export object requests.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`name`

(optional) Used to filter by the name of the object.

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`export_status`

(optional) Specifies export status to use, either - ALL, SUCCESSFUL, IN_PROGRESS, QUEUED, FAILED .

Allowed values are: 'IN_PROGRESS', 'SUCCESSFUL', 'QUEUED', 'TERMINATING', 'TERMINATED', 'FAILED'

`projection`

(optional) This parameter allows users to specify which view of the export object response to return. SUMMARY - Summary of the export object request will be returned. This is the default option when no value is specified. DETAILS - Details of export object request will be returned. This will include details of all the objects to be exported.

Allowed values are: 'SUMMARY', 'DETAILS'

`time_started_in_millis`

(optional) Specifies start time of a copy object request.

`time_ended_in_millis`

(optional) Specifies end time of a copy object request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_PUBLICATION_VALIDATIONS Function

Retrieves a lists of external publication validations in a workspace and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_PUBLICATIONS Function

Retrieves a list of external publications in an application and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FOLDERS Function

Retrieves a list of folders in a project and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`aggregator_key`

(optional) Used to filter by the project or the folder object.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FUNCTION_LIBRARIES Function

Retrieves a list of function libraries in a project and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`aggregator_key`

(optional) Used to filter by the project or the folder object.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPORT_REQUESTS Function

This endpoint can be used to get the list of import object requests.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`name`

(optional) Used to filter by the name of the object.

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`import_status`

(optional) Specifies import status to use, either - ALL, SUCCESSFUL, IN_PROGRESS, QUEUED, FAILED .

Allowed values are: 'IN_PROGRESS', 'SUCCESSFUL', 'QUEUED', 'TERMINATING', 'TERMINATED', 'FAILED'

`projection`

(optional) This parameter allows users to specify which view of the import object response to return. SUMMARY - Summary of the import object request will be returned. This is the default option when no value is specified. DETAILS - Details of import object request will be returned. This will include details of all the objects to be exported.

Allowed values are: 'SUMMARY', 'DETAILS'

`time_started_in_millis`

(optional) Specifies start time of a copy object request.

`time_ended_in_millis`

(optional) Specifies end time of a copy object request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATCH_CHANGES Function

Retrieves a list of patches in an application and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`name`

(optional) Used to filter by the name of the object.

`since_patch`

(optional) Specifies the patch key to query from.

`to_patch`

(optional) Specifies the patch key to query to.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATCHES Function

Retrieves a list of patches in an application and provides options to filter the list. For listing changes based on a period and logical objects changed, see ListPatchChanges API.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the published object.

`fields`

(optional) Specifies the fields to get for an object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PIPELINE_VALIDATIONS Function

Retrieves a list of pipeline validations within the specified workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PIPELINES Function

Retrieves a list of pipelines in a project or folder from within a workspace, the query parameter specifies the project or folder.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`aggregator_key`

(optional) Used to filter by the project or the folder object.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROJECTS Function

Retrieves a lists of projects in a workspace and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLISHED_OBJECTS Function

Retrieves a list of all the published objects for a specified application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`name_starts_with`

(optional) This parameter can be used to filter objects by the names starting with the given value.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`identifier`

(optional) Used to filter by the identifier of the published object.

`l_type`

(optional) Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. For Data Integration APIs, a filter based on type Task is used.

`type_in_subtree`

(optional) Used in association with type parameter. If value is true, then type all sub types of the given type parameter is considered. If value is false, then sub types are not considered. Default is false.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REFERENCES Function

Retrieves a list of references in an application. Reference objects are created when dataflows and tasks use objects, such as data assets and connections.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`name`

(optional) Used to filter by the name of the object.

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RUNTIME_OPERATORS Function

This endpoint can be used to list runtime operators with filtering options

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`runtime_pipeline_key`

(required) Runtime Pipeline Key

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`key`

(optional) Used to filter by the key of the object.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`aggregator_type`

(optional) Unique type of the aggregator

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RUNTIME_PIPELINES Function

This endpoint can be used to list runtime pipelines with filtering options

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`key`

(optional) Used to filter by the key of the object.

`aggregator_key`

(optional) Unique key of the aggregator

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`aggregator_type`

(optional) Unique type of the aggregator

`filter`

(optional) This filter parameter can be used to filter by model specific queryable fields of the object &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:-&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?filter=status eq Failed&lt;/B&gt; returns all objects that have a status field with value Failed&lt;/li&gt; &lt;/ul&gt;

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULES Function

Use this endpoint to list schedules.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`l_type`

(optional) Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. If this operator is not specified, then exact match is considered. &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=false&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEMAS Function

Retrieves a list of all the schemas that can be accessed using the specified connection.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`schema_resource_name`

(required) Schema resource name used for retrieving schemas.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Specifies the fields to get for an object.

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`name`

(optional) Used to filter by the name of the object.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`name_list`

(optional) Used to filter by the name of the object.

`include_types`

(optional) Artifact type which needs to be listed while listing Artifacts.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASK_RUN_LINEAGES Function

This endpoint can be used to list Task Run Lineages within a given time window.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`filter`

(optional) This filter parameter can be used to filter by model specific queryable fields of the object &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:-&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?filter=status eq Failed&lt;/B&gt; returns all objects that have a status field with value Failed&lt;/li&gt; &lt;/ul&gt;

`time_updated_greater_than`

(optional) This parameter allows users to get objects which were updated after a certain time. The format of timeUpdatedGreaterThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_updated_greater_than_or_equal_to`

(optional) This parameter allows users to get objects which were updated after and at a certain time. The format of timeUpdatedGreaterThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_upated_less_than`

(optional) This parameter allows users to get objects which were updated before a certain time. The format of timeUpatedLessThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`time_upated_less_than_or_equal_to`

(optional) This parameter allows users to get objects which were updated before and at a certain time. The format of timeUpatedLessThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASK_RUN_LOGS Function

Gets log entries for task runs using its key.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_run_key`

(required) The task run key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASK_RUNS Function

Retrieves a list of task runs and provides options to filter the list.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`key`

(optional) Used to filter by the key of the object.

`aggregator_key`

(optional) Used to filter by the project or the folder object.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`filter`

(optional) This filter parameter can be used to filter by model specific queryable fields of the object &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:-&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?filter=status eq Failed&lt;/B&gt; returns all objects that have a status field with value Failed&lt;/li&gt; &lt;/ul&gt;

`name_starts_with`

(optional) This parameter can be used to filter objects by the names starting with the given value.

`name_contains`

(optional) This parameter can be used to filter objects by the names that match partially or fully with the given value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASK_SCHEDULES Function

This endpoint can be used to get the list of all the TaskSchedule objects.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`l_type`

(optional) Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. If this operator is not specified, then exact match is considered. &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=false&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_enabled`

(optional) This filter parameter can be used to filter task schedule by its state.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASK_VALIDATIONS Function

Retrieves a list of task validations within the specified workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TASKS Function

Retrieves a list of all tasks in a specified project or folder.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`folder_id`

(optional) Unique key of the folder.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`key`

(optional) Used to filter by the key of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`l_type`

(optional) Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. If this operator is not specified, then exact match is considered. &lt;br&gt;&lt;br&gt;&lt;B&gt;Examples:&lt;/B&gt;&lt;br&gt; &lt;ul&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=false&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;li&gt;&lt;B&gt;?type=DATA_LOADER_TASK&amp;typeInSubtree=true&lt;/B&gt; returns all objects of type data loader task&lt;/li&gt; &lt;/ul&gt;

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TEMPLATES Function

This endpoint can be used to list application templates with filtering options.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the published object.

`fields`

(optional) Specifies the fields to get for an object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USER_DEFINED_FUNCTION_VALIDATIONS Function

Retrieves a list of UserDefinedFunctionvalidations within the specified workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`key`

(optional) Used to filter by the key of the object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`fields`

(optional) Specifies the fields to get for an object.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USER_DEFINED_FUNCTIONS Function

Retrieves a list of UserDefinedFunctions in a function library.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`function_library_key`

(optional) Unique key of the FunctionLibrary.

`fields`

(optional) Specifies the fields to get for an object.

`name`

(optional) Used to filter by the name of the object.

`identifier`

(optional) Used to filter by the identifier of the object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Retrieves a paginated list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous work request to retrieve.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Retrieves a paginated list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous work request to retrieve.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment containing the resources you want to list.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`workspace_id`

(optional) DIS workspace id

`work_request_status`

(optional) The work request status.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORKSPACES Function

Retrieves a list of Data Integration workspaces.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment containing the resources you want to list.

`name`

(optional) Used to filter by the name of the object.

`limit`

(optional) Sets the maximum number of results per page, or items to return in a paginated `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The lifecycle state of a resource. When specified, the operation only returns resources that match the given lifecycle state. When not specified, all lifecycle states are processed as a match.

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME', 'TIME_UPDATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_WORKSPACE Function

Starts a workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_WORKSPACE Function

Stops a workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`quiesce_timeout`

(optional) Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.

`is_force_operation`

(optional) Used to force close down the workspace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPLICATION Function

Updates an application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`update_application_details`

(required) The details needed to update an application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPLICATION_DETAILED_DESCRIPTION Function

Updates the detailed description of an Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`update_application_detailed_description_details`

(required) The details needed to update the detailed description of Application

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONNECTION Function

Updates a connection under a data asset.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`connection_key`

(required) The connection key.

`update_connection_details`

(required) The information needed to update a connection.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COPY_OBJECT_REQUEST Function

Updates the status of a copy object request.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`copy_object_request_key`

(required) The key of the object to be copied, for example this could be the key of a project.

`update_copy_object_request_details`

(required) The details needed to update the status of a copy object request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_ASSET Function

Updates a specific data asset with default connection.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_asset_key`

(required) The data asset key.

`update_data_asset_details`

(required) The information needed to update a data asset.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_FLOW Function

Updates a specific data flow.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`data_flow_key`

(required) The data flow key.

`update_data_flow_details`

(required) The details needed to updated a data flow.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DIS_APPLICATION Function

Updates a DIS Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`dis_application_id`

(required) The OCID of the DIS Application.

`update_dis_application_details`

(required) The details needed to update an application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DIS_APPLICATION_DETAILED_DESCRIPTION Function

Updates the detailed description of an Application.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`update_dis_application_detailed_description_details`

(required) The details needed to update the detailed description of Application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXPORT_REQUEST Function

Updates the status of a export object request.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`export_request_key`

(required) The key of the object export object request

`update_export_request_details`

(required) The details needed to update the status of a export object request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_PUBLICATION Function

Updates the external publication object.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`external_publications_key`

(required) The external published object key.

`update_external_publication_details`

(required) The information to be updated.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FOLDER Function

Updates a specific folder.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`folder_key`

(required) The folder key.

`update_folder_details`

(required) The details needed to update a folder.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FUNCTION_LIBRARY Function

Updates a specific Function Library.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`function_library_key`

(required) The functionLibrary key.

`update_function_library_details`

(required) The details needed to update a FunctionL ibrary.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IMPORT_REQUEST Function

Updates the status of a import object request.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`import_request_key`

(required) The key of the object export object request

`update_import_request_details`

(required) The details needed to update the status of a import object request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PIPELINE Function

Updates a specific pipeline.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`pipeline_key`

(required) The pipeline key.

`update_pipeline_details`

(required) The details needed to updated a pipeline.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROJECT Function

Updates a specific project.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`project_key`

(required) The project key.

`update_project_details`

(required) The details needed to update a project.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REFERENCE Function

Updates the application references. For example, to map a data asset to a different target object.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`reference_key`

(required) The reference key.

`update_reference_details`

(required) The details needed to update the references.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SCHEDULE Function

Endpoint used to update the schedule

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`schedule_key`

(required) Schedule Key

`update_schedule_details`

(required) Request body parameter for Schedule details

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TASK Function

Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`task_key`

(required) The task key.

`update_task_details`

(required) The details needed to update a task.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TASK_RUN Function

Updates the status of the task run. For example, aborts a task run.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_run_key`

(required) The task run key.

`update_task_run_details`

(required) The details needed to update the status of a task run.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TASK_SCHEDULE Function

Endpoint used to update the TaskSchedule

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`application_key`

(required) The application key.

`task_schedule_key`

(required) TaskSchedule Key

`update_task_schedule_details`

(required) Request body parameter for TaskSchedule details

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USER_DEFINED_FUNCTION Function

Updates a specific UserDefinedFunction.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`user_defined_function_key`

(required) The user defined function key.

`update_user_defined_function_details`

(required) The details needed to updated a UserDefinedFunction.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_WORKSPACE Function

Updates the specified Data Integration workspace.

Syntax
```

```

Parameters

Parameter Description

`workspace_id`

(required) The workspace ID.

`update_workspace_details`

(required) The information needed to update the workspace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dataintegration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Data Integration Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D0E70DBB-7226-4B69-944F-C9D2892A8BC2)
- [CHANGE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-EF6E9BDF-DA93-4445-AF0D-A7631B5F2449)
- [CHANGE_DIS_APPLICATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F94C9BFE-5E0A-4640-BC92-46831CDA0C4D)
- [CREATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-8F2FAC05-D9EE-4985-AD13-BD851CB06F92)
- [CREATE_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-B9AC1A2E-D1CC-4111-AF3B-5B6961765B39)
- [CREATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-3BAAA8A3-426E-4075-8C5A-6BE215914C54)
- [CREATE_CONNECTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D046E13D-0EBA-4589-B795-10D059093FE5)
- [CREATE_COPY_OBJECT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FF359EB1-ED61-440D-9C46-ED6A17668F21)
- [CREATE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A42AE755-9337-430D-B381-AF388907AA20)
- [CREATE_DATA_FLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A4A8E96C-A239-478A-8AA3-079D2ACF9017)
- [CREATE_DATA_FLOW_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6DF673DE-3E1A-4976-A85E-575B672518F2)
- [CREATE_DIS_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-5D6C626E-6962-45DE-AEAF-01A2F1818BC7)
- [CREATE_DIS_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7F81F311-778F-4709-91AB-DC33DBD2C062)
- [CREATE_ENTITY_SHAPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-DD61DF77-DF64-4F2B-B6DA-2F6BD912563F)
- [CREATE_EXPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-06224222-78F8-4BD8-853D-6C03C90177FC)
- [CREATE_EXTERNAL_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-26797933-7F6C-4CD7-A1FA-97A3D7D306BB)
- [CREATE_EXTERNAL_PUBLICATION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-8975BB1A-00D2-49B3-8A3E-8BA60C391E15)
- [CREATE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FBC23A43-CF70-43EC-936F-6F1274BF247A)
- [CREATE_FUNCTION_LIBRARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-612A020F-ADB2-4F43-9B36-861B74FB7D86)
- [CREATE_IMPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FEBAEFD5-FD7E-432E-8777-7585C00C246D)
- [CREATE_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-EF5FDEC5-3E54-42A5-90B4-6CC7F2F59AE1)
- [CREATE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FF046501-DEA6-4D89-8D8A-06AC1CB3B5F1)
- [CREATE_PIPELINE_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-296650E5-5AE7-49F6-9819-460DCDD3FA17)
- [CREATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-44BCFE0D-81B3-4CB7-BCA7-B6426F91D7E8)
- [CREATE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-9CC0951B-92A7-4EB1-B9EE-78C93AB2023E)
- [CREATE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-47F9B067-8D66-4BB9-8F39-5B61914502AD)
- [CREATE_TASK_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-3F90C0F8-3086-4D40-937B-5F3ABA253976)
- [CREATE_TASK_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-8257A3D0-26F1-4352-AA4F-E3BDD572BE5D)
- [CREATE_TASK_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-48DB52CD-F5A2-4B3D-A08A-4A3562FB28DE)
- [CREATE_USER_DEFINED_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A25C9057-6D7D-452F-B169-BDE019F6A6C1)
- [CREATE_USER_DEFINED_FUNCTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0E76E543-2AA7-4DC0-BBDD-23DE10FD0DF2)
- [CREATE_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-EDE78EE4-FC97-4433-ADFC-B3C7C7919324)
- [DELETE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-69308E07-5DFA-4A73-AAAF-752AD221B21B)
- [DELETE_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6EEA25A9-9FE0-43DF-9047-2FC0818861C4)
- [DELETE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-44B2FE54-3DB7-415C-BA27-0C8FE5260DA4)
- [DELETE_CONNECTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D666AE07-985A-4144-BB67-1213C2EA5D7C)
- [DELETE_COPY_OBJECT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-18AB0E64-3F06-43E2-9F7A-BB5C8FB7E5FA)
- [DELETE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-42EC3526-B084-4525-A146-8B404F4EA334)
- [DELETE_DATA_FLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A5331499-66D9-4ECF-BC6D-9EA011DC1EFF)
- [DELETE_DATA_FLOW_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-3DCD1758-8E43-45B8-B790-7FF5BD9DC2FC)
- [DELETE_DIS_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-86089059-1B83-4D53-B977-0DF3BA3C4238)
- [DELETE_DIS_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0A0E71BE-F79F-4AAA-B124-B0358546296D)
- [DELETE_EXPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0A665DB1-7D14-4130-9F0D-F17DB9399F6A)
- [DELETE_EXTERNAL_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0481A0C3-67AF-4354-BF4A-E82C5423C529)
- [DELETE_EXTERNAL_PUBLICATION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-183BE3FA-1764-47E9-9957-15AA8C1670D9)
- [DELETE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-69527615-AB45-4E93-8C3A-C5D01253B0DF)
- [DELETE_FUNCTION_LIBRARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FDF229EF-E1D8-4612-A2FB-68FB411A95BC)
- [DELETE_IMPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C07DCCCF-BA7A-417C-BF20-26F2987C0709)
- [DELETE_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4ADE8A06-03F9-4604-B624-21D7106214B3)
- [DELETE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4579C3D5-F55E-49EA-ABC5-E8C3D1CE602B)
- [DELETE_PIPELINE_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-664EC359-9520-48EB-928A-9982FEB969CF)
- [DELETE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-EF5E4DAF-70E4-4E86-A0F8-8D8415B7BA0D)
- [DELETE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-BC149068-2463-4553-9D6F-CF3F39661198)
- [DELETE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-B867A768-3CEC-4D7A-A429-2465FD387844)
- [DELETE_TASK_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D24FB3FC-D630-4CA8-9D4C-BEAA744D3ABE)
- [DELETE_TASK_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-26F8B025-B096-4668-AAB2-C111F4ED9482)
- [DELETE_TASK_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C7ADA348-E709-4DD2-88DF-FBE30DB3616D)
- [DELETE_USER_DEFINED_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-274B99E5-3F45-4A3F-BA14-655DB2079BD3)
- [DELETE_USER_DEFINED_FUNCTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FA55F14A-3512-4CB4-8159-794BE14B478A)
- [DELETE_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A7A702E8-E1F2-4A0D-8696-914883521953)
- [GET_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-1E1C5F9C-870C-4A71-AB13-DB52EC951D5B)
- [GET_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-EC6310E6-10E5-4CEB-BD7C-C8F9038ECFA5)
- [GET_COMPOSITE_STATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7B75FA39-C22F-4102-AC6C-531196A28983)
- [GET_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-1CEFA932-44B7-4AB2-A366-C650213E64C3)
- [GET_CONNECTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-299A06C0-510F-4D65-9D60-D2DA7AAFC21F)
- [GET_COPY_OBJECT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-8E783B12-EFAB-481A-8278-3F8F485F5414)
- [GET_COUNT_STATISTIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-16B59647-73CF-45DC-A16C-C82F0114F0BE)
- [GET_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-92EADB30-9A1E-4AB1-90D2-A5A55821984E)
- [GET_DATA_ENTITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2F9B153D-DDEA-4ACB-946F-D245F84D1885)
- [GET_DATA_FLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-AED8FA39-9C84-4722-9D5B-CE1B721DCCB7)
- [GET_DATA_FLOW_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-E346B64B-39A4-446E-B445-7E0D6D419E42)
- [GET_DEPENDENT_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6FCB05C0-81DE-4703-94D3-40E69B656072)
- [GET_DIS_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D6EA29FE-36BA-4A96-9C55-F56E62E92C7C)
- [GET_DIS_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-8BA24800-9A33-4FF9-9D67-39C76E680350)
- [GET_EXPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0063D89F-350F-4653-8910-64F82FE64FB6)
- [GET_EXTERNAL_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-855012E3-1C28-4FEC-8184-929EE4D4498D)
- [GET_EXTERNAL_PUBLICATION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FDC30816-3F21-43ED-8A51-BD76EDBF7997)
- [GET_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-3EBF6BDA-AE46-4E62-8FBF-DAF8C9D2DCD5)
- [GET_FUNCTION_LIBRARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F4856FC9-677B-4C1A-9F06-ED9748936F16)
- [GET_IMPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-20EC08BB-F22F-4352-B548-2DB406A04FC5)
- [GET_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C8BCED35-4715-4CD2-92EE-6E78B07B4411)
- [GET_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-29DD0236-C8FA-497A-9180-161BA3AFD89F)
- [GET_PIPELINE_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7614CDAB-649D-4CA5-9108-DA8CC30956A4)
- [GET_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6927D083-837B-453C-9EC5-A801C6BB76B6)
- [GET_PUBLISHED_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-9B5308FA-D269-4AA9-9F0F-CCE77EC1932E)
- [GET_REFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4E3622D3-DE8B-4F80-91D1-8B7CFA5A6DBF)
- [GET_RUNTIME_OPERATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-904E96EF-EEF5-4ACA-9393-4D836A1AFFAD)
- [GET_RUNTIME_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4A955846-C3F7-4790-90C6-C59675841BFF)
- [GET_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-664AAD42-33E4-4804-959F-05C8DD0F14B6)
- [GET_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6E64476F-5118-455E-9865-63E6245B8D44)
- [GET_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A71ADAA4-4919-4CA0-AD38-4FA91D500390)
- [GET_TASK_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4606C583-79B4-4A16-A360-30EF16527E16)
- [GET_TASK_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C3E3B373-435C-4DD6-B2E8-AA1C8BECC15D)
- [GET_TASK_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A352ECE6-62B8-42E5-91C2-04DFD5C9AE3B)
- [GET_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-14044E5E-4304-42EB-90B8-7A2CD1EAF5C9)
- [GET_USER_DEFINED_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-464AB112-1E5F-44E6-A4C9-B8966A0E99F8)
- [GET_USER_DEFINED_FUNCTION_VALIDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-9111132D-AA1C-44C0-808A-2FFE5CFFE911)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-0C8417E3-4491-4A20-9C2F-F8BB19AA05A1)
- [GET_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-05F63B1B-87E8-4826-8D70-9B72BF3D622F)
- [LIST_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-B75DD89F-33A7-4D1F-A4B3-5DEAA49EDE43)
- [LIST_CONNECTION_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-497484CE-ABFA-469B-9C41-02341540B1DD)
- [LIST_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2153A863-E32B-47E2-86B8-76D4CE709E10)
- [LIST_COPY_OBJECT_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-21CDFB87-8652-4164-9606-7604DD316469)
- [LIST_DATA_ASSETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-DE1F4290-0B27-4072-8236-9CEC96B23F51)
- [LIST_DATA_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6FF606DD-8071-45F7-A766-344B6077A43C)
- [LIST_DATA_FLOW_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F866FACA-3CEA-4AA2-A40C-DB6CAA339396)
- [LIST_DATA_FLOWS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2B6BF9A7-4409-44BC-B6E6-6099C638296E)
- [LIST_DEPENDENT_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A5326B63-225A-4CC8-BA8B-394EEC7597AD)
- [LIST_DIS_APPLICATION_TASK_RUN_LINEAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C51729FB-4871-4E3B-9F68-C2677FD04938)
- [LIST_DIS_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2F8E7C07-0F41-4F82-B69A-505122492D85)
- [LIST_EXPORT_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F21E33CD-55F0-493F-9BE6-E813C4740B3E)
- [LIST_EXTERNAL_PUBLICATION_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-B57386D0-7A2B-461F-9EAF-C85F5BF09285)
- [LIST_EXTERNAL_PUBLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7921C4D6-589B-4433-A35D-C319899CF355)
- [LIST_FOLDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-28DA69AD-11CA-4633-89D7-8BBA8133CAB3)
- [LIST_FUNCTION_LIBRARIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C3BBE177-A2CF-4556-BDB3-873FCEA92319)
- [LIST_IMPORT_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-AE01B713-983C-4AC9-B21B-CBCE733671D2)
- [LIST_PATCH_CHANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A7A28012-4A65-4CBB-BF51-41D3992F2AA3)
- [LIST_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C8FB192B-32F6-4ED0-ABA3-60C2C621B3DE)
- [LIST_PIPELINE_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-06CB312F-1A77-4ECE-BF4B-DC5D49AB0144)
- [LIST_PIPELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-877ADC22-487A-4071-80E4-766BC15AF3F2)
- [LIST_PROJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C5F7DD82-7DFD-4B32-9698-BE7AE9E34846)
- [LIST_PUBLISHED_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-384CC272-161F-4C50-8FDC-D79FE03AB3BF)
- [LIST_REFERENCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F1F55432-08AA-40C4-8F50-276C9897CDB8)
- [LIST_RUNTIME_OPERATORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-E95398D9-FEF6-4B75-9271-D9B739B924D1)
- [LIST_RUNTIME_PIPELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2D65D715-FE88-4ACB-96AD-FC5FA173FB7A)
- [LIST_SCHEDULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-5655F7D1-FC9C-4495-95FE-8D33E6EF5083)
- [LIST_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F466C731-77A2-471E-91BB-375B8033C6BC)
- [LIST_TASK_RUN_LINEAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-2ED8A61A-74F8-4106-8C51-6A5F3B3300B7)
- [LIST_TASK_RUN_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-D4728043-C093-4CDA-85EA-B94388BCAAC2)
- [LIST_TASK_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-63340170-E5FB-48F3-A32F-155CC1EC2A8E)
- [LIST_TASK_SCHEDULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-DDAAF331-6918-4DB7-BAAC-CF2C36AEA5BF)
- [LIST_TASK_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FC98E326-49C9-4C27-894E-899071487538)
- [LIST_TASKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-DD536811-AB9F-4B1A-B840-89A3E83F5BB9)
- [LIST_TEMPLATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6BE0BA6D-C621-4607-A54E-EB9E9D5405C8)
- [LIST_USER_DEFINED_FUNCTION_VALIDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-E55ACB75-19E2-4C3F-8645-4EA9B4E66D1A)
- [LIST_USER_DEFINED_FUNCTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7FB368ED-4E42-4EDD-9E8F-9B44C964A64A)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-E63B81BE-A681-4780-A8CD-3C5745575F8A)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-FB189E30-8655-4A78-9975-7C9C6C975C8F)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-A1945D04-37DF-461B-B4BC-D7CFAA949475)
- [LIST_WORKSPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7E687C76-34D9-4B5A-904F-D6041603F9CA)
- [START_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7F2C80F8-0553-46E6-9B08-9291B9649337)
- [STOP_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-486F9450-869A-4FFF-9264-53895355E803)
- [UPDATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-15C7F80D-D64A-4EBD-AD92-D8E6B550A78F)
- [UPDATE_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-F0E7BA27-4D54-42A2-B6D4-4329384A9D76)
- [UPDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-799B7564-352F-4B5F-8D44-BB297BC63B22)
- [UPDATE_COPY_OBJECT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-910450EA-086D-4624-834F-46578042FF60)
- [UPDATE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-BAD76699-E567-4F88-BEF3-D1EE55B517CD)
- [UPDATE_DATA_FLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-1C3978D8-4258-4FC0-837F-65943EC8FB1B)
- [UPDATE_DIS_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-6340EC87-CCFE-435C-9EDE-4AE2559C1BE9)
- [UPDATE_DIS_APPLICATION_DETAILED_DESCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-5340CE26-A7D2-4876-874D-6EF92D35BE69)
- [UPDATE_EXPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-854C429E-EB21-457D-89DE-0E2B9C7A7DC7)
- [UPDATE_EXTERNAL_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-7003820C-9530-47E4-A0F6-DEFCEE032136)
- [UPDATE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-1C450380-666B-40D4-A1B5-6ED5A56ACE2B)
- [UPDATE_FUNCTION_LIBRARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-B5A05F1A-2509-4635-B5F0-8709E093E58D)
- [UPDATE_IMPORT_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-60FD1B9D-D160-467A-A4C2-11B6B7DC26B5)
- [UPDATE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-397E9ADD-A16F-44F5-95BC-465FC4458BBF)
- [UPDATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-C729E6EF-3D00-4DEF-B09C-5B86575A111E)
- [UPDATE_REFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-E7898717-0163-4C88-AD8B-A574FFE8A104)
- [UPDATE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-4F5511B8-AB45-4031-8F45-F88594608695)
- [UPDATE_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-13F07529-7576-4E58-8806-CB46D804AA74)
- [UPDATE_TASK_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-78AD0707-8945-440E-8733-75479AE02A29)
- [UPDATE_TASK_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-34EB40FD-0D69-4575-ABF3-FB8089513887)
- [UPDATE_USER_DEFINED_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-3AE755A3-9AE3-4DA3-B608-EC855CEB0CEA)
- [UPDATE_WORKSPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_di_data_integration.html#ADSDK-GUID-CCF62589-109C-4407-BC45-6E88A93DEAF4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
