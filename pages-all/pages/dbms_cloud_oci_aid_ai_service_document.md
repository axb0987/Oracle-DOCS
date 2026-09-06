# AI Document Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#dcoc-content-body)

## AI Document Functions

Package: DBMS_CLOUD_OCI_AID_AI_SERVICE_DOCUMENT

### ANALYZE_DOCUMENT Function

Perform different types of document analysis.

Syntax
```

```

Parameters

Parameter Description

`analyze_document_details`

(required) The details of how to analyze a document.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_PROCESSOR_JOB Function

Cancel a processor job.

Syntax
```

```

Parameters

Parameter Description

`processor_job_id`

(required) Processor job id.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancel the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MODEL_COMPARTMENT Function

Moves a model from one compartment to another. When provided, If-Match is checked against the ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) A unique model identifier.

`change_model_compartment_details`

(required) The details of the move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PROJECT_COMPARTMENT Function

Move a project from one compartment to another. When provided, If-Match is checked against the ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) A unique project identifier.

`change_project_compartment_details`

(required) The deatils of the move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL Function

Create a new model.

Syntax
```

```

Parameters

Parameter Description

`create_model_details`

(required) The metadata about the new model.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROCESSOR_JOB Function

Create a processor job for document analysis.

Syntax
```

```

Parameters

Parameter Description

`create_processor_job_details`

(required) The details for creating the processor job.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROJECT Function

Create a new project.

Syntax
```

```

Parameters

Parameter Description

`create_project_details`

(required) The new Project's details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MODEL Function

Delete a model by identifier.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) A unique model identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROJECT Function

Delete a project by identifier.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) A unique project identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL Function

Get a model by identifier.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) A unique model identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROCESSOR_JOB Function

Get the details of a processor job.

Syntax
```

```

Parameters

Parameter Description

`processor_job_id`

(required) Processor job id.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROJECT Function

Get a project by identifier.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) A unique project identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODELS Function

Returns a list of models in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`project_id`

(optional) The ID of the project for which to list the objects.

`lifecycle_state`

(optional) The filter to match models with the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The filter to find the model with the given identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROJECTS Function

Returns a list of projects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The filter to match projects with the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The filter to find the project with the given identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a (paginated) list of errors for a given work request.

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

(optional) The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) A filter to return only resources whose lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_MODEL Function

Updates the model metadata only selected path parameter.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) A unique model identifier.

`patch_model_details`

(required) The model metadata to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL Function

Updates the model metadata.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) A unique model identifier.

`update_model_details`

(required) The model metadata to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROJECT Function

Update the project metadata.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) A unique project identifier.

`update_project_details`

(required) The project metadata to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://document.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [AI Document Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-8F607235-CB7F-48FE-8823-5196A389B66D)
- [ANALYZE_DOCUMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-79894395-745C-43AD-BA98-2C622F214EE3)
- [CANCEL_PROCESSOR_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-4989CAFD-71E0-4CFB-B170-A8FAD9D89BEB)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-B71C0277-3B03-47D3-BB4B-FFA16FA36313)
- [CHANGE_MODEL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-5C85E498-05AE-4B63-B227-1097047D613C)
- [CHANGE_PROJECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-6DA471A5-0665-416A-9EE0-6B54DA592249)
- [CREATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-49A1ABB3-02A6-4B9C-9164-4ED524B47A03)
- [CREATE_PROCESSOR_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-7D1EE6FD-63D2-4FBD-8D8C-CE0D3170FE98)
- [CREATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-3AD5853C-31D3-4E0D-995C-E607E987ECE5)
- [DELETE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-8AB04955-1C62-4305-BF44-ED2EC242C19D)
- [DELETE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-6B3D068D-173E-4072-88EB-D28D5FA9912E)
- [GET_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-F6D750E0-763E-4609-8A75-C39D5053CFA2)
- [GET_PROCESSOR_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-FF584D13-97E5-4E98-A63E-9E0D0726DCC1)
- [GET_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-549BE1DC-81B8-483A-89E2-E9DD8EEE2082)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-207ADB9D-2155-4CDC-970B-54B6FCEA36E5)
- [LIST_MODELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-42EFFBE2-5FDF-4698-A761-1CC78F967F90)
- [LIST_PROJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-6A355D32-20B3-4499-B647-7EBB8855F148)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-E11F0DDF-9E79-4E2B-B4C1-CCAAC6255C9F)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-873F7727-565C-4205-9A8F-97B5F812D898)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-3F60AE47-0313-495B-B4F9-75C50FEFCECB)
- [PATCH_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-D18450E1-09EE-4A34-A81F-6833376844BA)
- [UPDATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-A1C2C632-631D-4811-A990-92F1A06840E4)
- [UPDATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_aid_ai_service_document.html#ADSDK-GUID-BEC7E419-32EF-4933-98B1-06F832F2743D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
