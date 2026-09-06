# Data Science Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#dcoc-content-body)

## Data Science Functions

Package: DBMS_CLOUD_OCI_DSC_DATA_SCIENCE

### ACTIVATE_MODEL Function

Activates the model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ACTIVATE_MODEL_DEPLOYMENT Function

Activates the model deployment.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ACTIVATE_NOTEBOOK_SESSION Function

Activates the notebook session.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_JOB_RUN Function

Cancels an IN_PROGRESS job run.

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_PIPELINE_RUN Function

Cancel a PipelineRun.

Syntax
```

```

Parameters

Parameter Description

`pipeline_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancels a work request that has not started.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATA_SCIENCE_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves a private endpoint into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`data_science_private_endpoint_id`

(required) The unique ID for a Data Science private endpoint.

`change_data_science_private_endpoint_compartment_details`

(required) Details for changing a private endpoint's compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_JOB_COMPARTMENT Function

Changes a job's compartment

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`change_job_compartment_details`

(required) Details for changing the compartment of a job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_JOB_RUN_COMPARTMENT Function

Changes a job run's compartment

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`change_job_run_compartment_details`

(required) Details for changing the compartment of a job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MODEL_COMPARTMENT Function

Moves a model resource into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`change_model_compartment_details`

(required) Details for changing the compartment of a model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MODEL_DEPLOYMENT_COMPARTMENT Function

Moves a model deployment into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`change_model_deployment_compartment_details`

(required) Details for changing the compartment of a model deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MODEL_VERSION_SET_COMPARTMENT Function

Moves a modelVersionSet resource into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`model_version_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`change_model_version_set_compartment_details`

(required) Details for changing the compartment of a model version set.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NOTEBOOK_SESSION_COMPARTMENT Function

Moves a notebook session resource into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`change_notebook_session_compartment_details`

(required) Details for changing the compartment of a notebook session.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PIPELINE_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`change_pipeline_compartment_details`

(required) Details for the compartment move.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PIPELINE_RUN_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`pipeline_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`change_pipeline_run_compartment_details`

(required) Details for the compartment move.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PROJECT_COMPARTMENT Function

Moves a project resource into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`change_project_compartment_details`

(required) Details for changing the compartment of a project.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_SCIENCE_PRIVATE_ENDPOINT Function

Creates a Data Science private endpoint to be used by a Data Science resource.

Syntax
```

```

Parameters

Parameter Description

`create_data_science_private_endpoint_details`

(required) The parameters required to create a private endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) Details for creating a new job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB_ARTIFACT Function

Uploads a job artifact.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`content_length`

(optional) The content length of the body.

`job_artifact`

(required) The job artifact to upload.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`content_disposition`

(optional) This header is for specifying a filename during upload. It is used to identify the file type and validate if the file type is supported. Example: `--content-disposition \"attachment; filename=hello-world.py\"`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB_RUN Function

Creates a job run.

Syntax
```

```

Parameters

Parameter Description

`create_job_run_details`

(required) Details for creating a new job run.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL Function

Creates a new model.

Syntax
```

```

Parameters

Parameter Description

`create_model_details`

(required) Details for creating a new model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL_ARTIFACT Function

Creates model artifact for specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`content_length`

(optional) The content length of the body.

`model_artifact`

(required) The model artifact to upload.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`content_disposition`

(optional) This header allows you to specify a filename during upload. This file name is used to dispose of the file contents while downloading the file. If this optional field is not populated in the request, then the OCID of the model is used for the file name when downloading. Example: `{\"Content-Disposition\": \"attachment\" \"filename\"=\"model.tar.gz\" \"Content-Length\": \"2347\" \"Content-Type\": \"application/gzip\"}`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL_DEPLOYMENT Function

Creates a new model deployment.

Syntax
```

```

Parameters

Parameter Description

`create_model_deployment_details`

(required) Details for creating a new model deployment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL_PROVENANCE Function

Creates provenance information for the specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`create_model_provenance_details`

(required) Provenance information for specified model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL_VERSION_SET Function

Creates a new modelVersionSet.

Syntax
```

```

Parameters

Parameter Description

`create_model_version_set_details`

(required) Details for creating a new modelVersionSet.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NOTEBOOK_SESSION Function

Creates a new notebook session.

Syntax
```

```

Parameters

Parameter Description

`create_notebook_session_details`

(required) Details for creating a new notebook session.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PIPELINE Function

Creates a new Pipeline.

Syntax
```

```

Parameters

Parameter Description

`create_pipeline_details`

(required) Details for the new Pipeline.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PIPELINE_RUN Function

Creates a new PipelineRun.

Syntax
```

```

Parameters

Parameter Description

`create_pipeline_run_details`

(required) Details for the new PipelineRun.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROJECT Function

Creates a new project.

Syntax
```

```

Parameters

Parameter Description

`create_project_details`

(required) Details for creating a new project.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STEP_ARTIFACT Function

Upload the artifact for a step in the pipeline.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`step_name`

(required) Unique Step identifier in a pipeline.

`content_length`

(optional) The content length of the body.

`step_artifact`

(required) The step artifact to upload.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`content_disposition`

(optional) This header allows you to specify a filename during upload. This file name is used to dispose of the file contents while downloading the file. If this optional field is not populated in the request, then the OCID of the model is used for the file name when downloading. Example: `{\"Content-Disposition\": \"attachment\" \"filename\"=\"model.tar.gz\" \"Content-Length\": \"2347\" \"Content-Type\": \"application/gzip\"}`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_MODEL Function

Deactivates the model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_MODEL_DEPLOYMENT Function

Deactivates the model deployment.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_NOTEBOOK_SESSION Function

Deactivates the notebook session.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_SCIENCE_PRIVATE_ENDPOINT Function

Deletes a private endpoint using `privateEndpointId`.

Syntax
```

```

Parameters

Parameter Description

`data_science_private_endpoint_id`

(required) The unique ID for a Data Science private endpoint.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JOB Function

Deletes a job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`delete_related_job_runs`

(optional) Delete all JobRuns associated with this job.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JOB_RUN Function

Deletes a job run.

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MODEL Function

Deletes the specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MODEL_DEPLOYMENT Function

Deletes the specified model deployment. Any unsaved work in this model deployment is lost.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MODEL_VERSION_SET Function

Deletes the specified modelVersionSet.

Syntax
```

```

Parameters

Parameter Description

`model_version_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`is_delete_related_models`

(optional) By default, this parameter is false. A model version set can only be deleted if all the models associate with it are already in the DELETED state. You can optionally specify the deleteRelatedModels boolean query parameters to true, which deletes all associated models for you.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NOTEBOOK_SESSION Function

Deletes the specified notebook session. Any unsaved work in this notebook session are lost.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PIPELINE Function

Deletes a Pipeline resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`delete_related_pipeline_runs`

(optional) A boolean value to specify whether to delete related PipelineRuns or not.

`delete_related_job_runs`

(optional) A boolean value to specify whether to delete related jobRuns or not.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PIPELINE_RUN Function

Deletes a PipelineRun resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`pipeline_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`delete_related_job_runs`

(optional) A boolean value to specify whether to delete related jobRuns or not.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROJECT Function

Deletes the specified project. This operation fails unless all associated resources (notebook sessions or models) are in a DELETED state. You must delete all associated resources before deleting a project.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_MODEL_ARTIFACT Function

Export model artifact from source to the service bucket

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`export_model_artifact_details`

(required) Model artifact source details for exporting.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_SCIENCE_PRIVATE_ENDPOINT Function

Retrieves an private endpoint using a `privateEndpointId`.

Syntax
```

```

Parameters

Parameter Description

`data_science_private_endpoint_id`

(required) The unique ID for a Data Science private endpoint.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB Function

Gets a job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_ARTIFACT_CONTENT Function

Downloads job artifact content for specified job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`range`

(optional) Optional byte range to fetch, as described in[RFC 7233](https://tools.ietf.org/html/rfc7232#section-2.1), section 2.1. Note that only a single range of bytes is supported.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_RUN Function

Gets a job run.

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL Function

Gets the specified model's information.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL_ARTIFACT_CONTENT Function

Downloads model artifact content for specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`range`

(optional) Optional byte range to fetch, as described in[RFC 7233](https://tools.ietf.org/html/rfc7232#section-2.1), section 2.1. Note that only a single range of bytes is supported.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL_DEPLOYMENT Function

Retrieves the model deployment for the specified `modelDeploymentId`.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL_PROVENANCE Function

Gets provenance information for specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL_VERSION_SET Function

Gets the specified model version set information.

Syntax
```

```

Parameters

Parameter Description

`model_version_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NOTEBOOK_SESSION Function

Gets the specified notebook session's information.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PIPELINE Function

Gets a Pipeline by identifier.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PIPELINE_RUN Function

Gets a PipelineRun by identifier.

Syntax
```

```

Parameters

Parameter Description

`pipeline_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROJECT Function

Gets the specified project's information.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STEP_ARTIFACT_CONTENT Function

Download the artifact for a step in the pipeline.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`step_name`

(required) Unique Step identifier in a pipeline.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`range`

(optional) Optional byte range to fetch, as described in[RFC 7233](https://tools.ietf.org/html/rfc7232#section-2.1), section 2.1. Note that only a single range of bytes is supported.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the specified work request's information.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_JOB_ARTIFACT Function

Gets job artifact metadata.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_MODEL_ARTIFACT Function

Gets model artifact metadata for specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_STEP_ARTIFACT Function

Get the artifact metadata for a step in the pipeline.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`step_name`

(required) Unique Step identifier in a pipeline.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_MODEL_ARTIFACT Function

Import model artifact from service bucket

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`import_model_artifact_details`

(required) Model artifact source details for importing.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_SCIENCE_PRIVATE_ENDPOINTS Function

Lists all Data Science private endpoints in the specified compartment. The query must include compartmentId. The query can also include one other parameter. If the query doesn't include compartmentId, or includes compartmentId with two or more other parameters, then an error is returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The lifecycle state of the private endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`sort_by`

(optional) The field used to sort the results. Multiple fields aren't supported.

Allowed values are: 'timeCreated'

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`data_science_resource_type`

(optional) Resource types in the Data Science service such as notebooks.

Allowed values are: 'NOTEBOOK_SESSION'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FAST_LAUNCH_JOB_CONFIGS Function

List fast launch capable job configs in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_RUNS Function

List out job runs.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETED', 'NEEDS_ATTENTION'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_SHAPES Function

List job shapes available in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOBS Function

List jobs in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODEL_DEPLOYMENT_SHAPES Function

Lists the valid model deployment shapes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODEL_DEPLOYMENTS Function

Lists all model deployments in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING', 'DELETED', 'NEEDS_ATTENTION'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, results are shown in descending order. When you sort by `displayName`, results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODEL_VERSION_SETS Function

Lists model version sets in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`name`

(optional) A filter to return only resources that match the entire name given.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order.

Allowed values are: 'timeCreated', 'name', 'lifecycleState'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODELS Function

Lists models in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`model_version_set_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the name of the model version set.

`version_label`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by version label.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'ACTIVE', 'DELETED', 'FAILED', 'INACTIVE'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. All other fields default to ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName', 'lifecycleState'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NOTEBOOK_SESSION_SHAPES Function

Lists the valid notebook session shapes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NOTEBOOK_SESSIONS Function

Lists the notebook sessions in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PIPELINE_RUNS Function

Returns a list of PipelineRuns.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`pipeline_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) The current state of the PipelineRun.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeAccepted`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeAccepted', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PIPELINES Function

Returns a list of Pipelines.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`project_id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) The current state of the Pipeline.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROJECTS Function

Lists projects in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`display_name`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by its user-friendly name.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED'

`created_by`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Lists work request errors for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists work request logs for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists work requests in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) &lt;b&gt;Filter&lt;/b&gt; results by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resource type.

`operation_type`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the type of the operation associated with the work request.

Allowed values are: 'NOTEBOOK_SESSION_CREATE', 'NOTEBOOK_SESSION_DELETE', 'NOTEBOOK_SESSION_ACTIVATE', 'NOTEBOOK_SESSION_DEACTIVATE', 'MODELVERSIONSET_DELETE', 'EXPORT_MODEL_ARTIFACT', 'IMPORT_MODEL_ARTIFACT', 'MODEL_DEPLOYMENT_CREATE', 'MODEL_DEPLOYMENT_DELETE', 'MODEL_DEPLOYMENT_ACTIVATE', 'MODEL_DEPLOYMENT_DEACTIVATE', 'MODEL_DEPLOYMENT_UPDATE', 'PROJECT_DELETE', 'WORKREQUEST_CANCEL', 'JOB_DELETE', 'PIPELINE_CREATE', 'PIPELINE_DELETE', 'PIPELINE_RUN_CREATE', 'PIPELINE_RUN_CANCEL', 'PIPELINE_RUN_DELETE', 'PRIVATE_ENDPOINT_CREATE', 'PRIVATE_ENDPOINT_DELETE', 'PRIVATE_ENDPOINT_MOVE', 'PRIVATE_ENDPOINT_UPDATE'

`status`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by work request status.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. See[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, the results are shown in descending order. All other fields default to ascending order.

Allowed values are: 'operationType', 'status', 'timeAccepted'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_SCIENCE_PRIVATE_ENDPOINT Function

Updates a private endpoint using a `privateEndpointId`. If changes to a private endpoint match a previously defined private endpoint, then a 409 status code is returned. This indicates that a conflict has been detected.

Syntax
```

```

Parameters

Parameter Description

`data_science_private_endpoint_id`

(required) The unique ID for a Data Science private endpoint.

`update_data_science_private_endpoint_details`

(required) Details for updating a private endpoint.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB Function

Updates a job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`update_job_details`

(required) Details for updating a job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB_RUN Function

Updates a job run.

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`update_job_run_details`

(required) Details for updating a job.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL Function

Updates the properties of a model. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`update_model_details`

(required) Details for updating a model. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL_DEPLOYMENT Function

Updates the properties of a model deployment. Some of the properties of `modelDeploymentConfigurationDetails` or `CategoryLogDetails` can also be updated with zero down time when the model deployment's lifecycle state is ACTIVE or NEEDS_ATTENTION i.e `instanceShapeName`, `instanceCount` and `modelId`, separately `loadBalancerShape` or `CategoryLogDetails` can also be updated independently. All of the fields can be updated when the deployment is in the INACTIVE lifecycle state. Changes will take effect the next time the model deployment is activated.

Syntax
```

```

Parameters

Parameter Description

`model_deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`update_model_deployment_details`

(required) Details for updating a model deployment. Some of the properties of `modelDeploymentConfigurationDetails` or `CategoryLogDetails` can also be updated with zero down time when the model deployment's lifecycle state is ACTIVE or NEEDS_ATTENTION i.e `instanceShapeName`, `instanceCount` and `modelId`, separately `loadBalancerShape` or `CategoryLogDetails` can also be updated independently. All of the fields can be updated when the deployment is in the INACTIVE lifecycle state. Changes will take effect the next time the model deployment is activated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL_PROVENANCE Function

Updates the provenance information for the specified model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`update_model_provenance_details`

(required) Provenance information for the specified model.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL_VERSION_SET Function

Updates the properties of a model version set. User can update the `description` property.

Syntax
```

```

Parameters

Parameter Description

`model_version_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`update_model_version_set_details`

(required) Details for updating a model version set. You can update `description` property only.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NOTEBOOK_SESSION Function

Updates the properties of a notebook session. You can update the `displayName`, `freeformTags`, and `definedTags` properties. When the notebook session is in the INACTIVE lifecycle state, you can update `notebookSessionConfigurationDetails` and change `shape`, `subnetId`, and `blockStorageSizeInGBs`. Changes to the `notebookSessionConfigurationDetails` take effect the next time the `ActivateNotebookSession` action is invoked on the notebook session resource.

Syntax
```

```

Parameters

Parameter Description

`notebook_session_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`update_notebook_session_details`

(required) Details for updating a notebook session. `notebookSessionConfigurationDetails` can only be updated while the notebook session is in the `INACTIVE` state. Changes to the `notebookSessionConfigurationDetails` take effect the next time the `ActivateNotebookSession` action is invoked on the notebook session resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PIPELINE Function

Updates the Pipeline.

Syntax
```

```

Parameters

Parameter Description

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`update_pipeline_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PIPELINE_RUN Function

Updates the PipelineRun.

Syntax
```

```

Parameters

Parameter Description

`pipeline_run_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`update_pipeline_run_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROJECT Function

Updates the properties of a project. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`update_project_details`

(required) Details for updating a project. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, then provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datascience.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Data Science Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-93E7D2C2-3827-4A85-BDA9-F99B61038C6D)
- [ACTIVATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-5991480F-2AFC-4454-BE61-2312EE062B8B)
- [ACTIVATE_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-74AE60CF-5DC0-4ABD-B402-FB75BFCB09A7)
- [ACTIVATE_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-93B5B932-A9FF-4110-B1AE-2F1CFDB675E5)
- [CANCEL_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-E264CD2D-57A1-49C2-A0CB-AB4D989D440A)
- [CANCEL_PIPELINE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-59BD1B93-0B86-44D4-91E0-C0CA05134D3C)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-16694F2C-0202-4354-A499-5A5FB854414C)
- [CHANGE_DATA_SCIENCE_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-261CB76D-0035-4D12-8497-FDB0E8A6FFC2)
- [CHANGE_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-ECFAF25E-D10E-4021-B7F0-78B5686D5F19)
- [CHANGE_JOB_RUN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-3E384B90-4FD8-49D0-8B7A-EAA19DF7D42A)
- [CHANGE_MODEL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-48A0613C-75EE-4FCA-A682-F8ED732ADEC3)
- [CHANGE_MODEL_DEPLOYMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-ACD4885A-7E88-4AA9-8B7B-352B50B72C67)
- [CHANGE_MODEL_VERSION_SET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-9C58C71F-63D7-473E-8EBC-138BCD74DB28)
- [CHANGE_NOTEBOOK_SESSION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-84766C7C-A23A-4090-808A-3CD8F4248262)
- [CHANGE_PIPELINE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-E0F70746-AB21-4B1E-AEC1-5B1E7EEE4A42)
- [CHANGE_PIPELINE_RUN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-8F562646-5C26-4AA8-ABE4-147F9518416B)
- [CHANGE_PROJECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-7EC32A3A-2C50-42B6-AD07-D1CE0247B1DB)
- [CREATE_DATA_SCIENCE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-0125558A-8A71-4770-B6AA-949851A1589A)
- [CREATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-1E7E9EE6-A74A-4A1A-94FC-F7395CA5EE0E)
- [CREATE_JOB_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-5C6DDC00-FD43-45A9-933A-DBC159AE398F)
- [CREATE_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-937E7C93-5333-41A2-AD94-A684E10D06F3)
- [CREATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-E0F17C6F-C59E-43E3-89BC-2FF39F0C0B1B)
- [CREATE_MODEL_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-635CC79D-CA38-499E-A1DA-3E1E73C19395)
- [CREATE_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-D95C6C3D-E33F-418D-AF7F-A2C5E02D1176)
- [CREATE_MODEL_PROVENANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-423A6F1C-80B8-493A-87A4-592206876863)
- [CREATE_MODEL_VERSION_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-B302998C-5403-4739-B9A3-8A7CBBB789AF)
- [CREATE_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-C7EFAD9C-7077-4E91-891B-409C4760FF2D)
- [CREATE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-72FE7FC6-77C3-4E3E-9EDF-DB5FA748BE45)
- [CREATE_PIPELINE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-AEC8B87D-52B3-4D87-9326-CE6C5FE9F364)
- [CREATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-B5412D0D-A7A5-46CA-A860-D09AC42BB54C)
- [CREATE_STEP_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-7F620960-7566-4ABA-84DD-C27EEAAD2C38)
- [DEACTIVATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-EAC1715C-D4C7-4F79-93BA-07F6271CCCED)
- [DEACTIVATE_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-0DD33218-4702-472A-9962-1DE5D5B449FE)
- [DEACTIVATE_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-D74B0514-EEF4-424B-9CB8-103618E15DA5)
- [DELETE_DATA_SCIENCE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-25D591CF-D14D-45A8-8960-B96EC678EC64)
- [DELETE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-0BB9A388-3638-4BF1-A5C6-3B83283D6C84)
- [DELETE_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-BF9EF6B8-6AFF-401B-AD97-C117E741DDC1)
- [DELETE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-C7B46E52-A840-4A49-9B36-48A5D36671B8)
- [DELETE_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-7B9EDB10-9A06-4583-8465-EC46E13F2A33)
- [DELETE_MODEL_VERSION_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-543E7501-23B9-4B84-AE70-FF76EEE435B3)
- [DELETE_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-E672E6A0-E60A-407A-9F3E-410996442F4A)
- [DELETE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-3D3E3024-2B8F-45A8-983C-A3FB62AECC08)
- [DELETE_PIPELINE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-BFDFFF52-E8F8-4256-8586-4C755E1942B5)
- [DELETE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-262E75AD-30D5-472B-8A98-C5F296924102)
- [EXPORT_MODEL_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-5D9D2B84-4843-47E5-A0C0-013B6367951C)
- [GET_DATA_SCIENCE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-33642A40-6559-4941-8A03-0A3F23481BC5)
- [GET_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-55F200E4-2ADC-4787-8F41-B4873DA14C47)
- [GET_JOB_ARTIFACT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-ECA1F130-6CED-4FF9-92BD-F75EC90A7E6F)
- [GET_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F38BE1D4-C5DB-4B22-B436-C9378DEB1243)
- [GET_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-B64C3B7C-8094-4686-9B54-380148BE941C)
- [GET_MODEL_ARTIFACT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F9697D55-1931-489B-9D5D-A495D5CDF557)
- [GET_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-2B9D7DF5-5E52-4AB6-9A20-6C1CB370CC1A)
- [GET_MODEL_PROVENANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-136856CD-527C-46DC-AFCD-41EE2A8ACEAD)
- [GET_MODEL_VERSION_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-98064EC9-5194-4CD1-84D3-B356CAC4D05B)
- [GET_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-76941623-1AE3-4A9E-BDC4-5ADAEA0C6F7C)
- [GET_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-3071C72D-C352-4871-8FDF-C54BB821F1A7)
- [GET_PIPELINE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-970F631C-9504-4B4E-9926-1A3A68069305)
- [GET_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F58AADE9-1E62-4853-9837-ECC692C546A9)
- [GET_STEP_ARTIFACT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-1C3D0553-19C1-4558-A5A7-9AFCBCD5241D)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-1E75F90B-DC3F-4266-BBD0-E7BCC311B1DE)
- [HEAD_JOB_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F72EBFA0-6A68-4151-B379-DB7AFFF5DE80)
- [HEAD_MODEL_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-53208093-B815-42F3-AA65-002F204D3A1C)
- [HEAD_STEP_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-825A2E08-213C-4023-A31E-569A3AFF1993)
- [IMPORT_MODEL_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-5A68F6BC-0CAB-462D-9A4D-A445CFF05A01)
- [LIST_DATA_SCIENCE_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-DC0299DC-EE30-4071-A37C-707BBF3907B5)
- [LIST_FAST_LAUNCH_JOB_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-AD847B78-C53A-474E-A325-62D7E58E857A)
- [LIST_JOB_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-7B7B77DE-7457-45D2-8528-C9F07FE5244C)
- [LIST_JOB_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-32897EDD-D40B-4887-9A8E-1EEDEA3695BA)
- [LIST_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F2F086C2-DC20-437E-BBAF-97426DDF605F)
- [LIST_MODEL_DEPLOYMENT_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-F2DF5B1D-5595-448D-BDBD-73671A80BE69)
- [LIST_MODEL_DEPLOYMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-94CEFDDA-4A1D-408E-8383-CE35A19593F4)
- [LIST_MODEL_VERSION_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-61AB7703-DBF2-4897-81DD-2CD68D65D67D)
- [LIST_MODELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-67007BBB-6513-4AE5-9944-EC8B1E5E5A40)
- [LIST_NOTEBOOK_SESSION_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-0D5C8668-E617-497C-B842-2607CE92C0B3)
- [LIST_NOTEBOOK_SESSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-99E0F246-E9CE-42D4-8212-A5EAC1216C5A)
- [LIST_PIPELINE_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-2E7CF0BF-9106-4E93-98C0-C1EBEF9B080F)
- [LIST_PIPELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-9314EFB8-B1EA-4BC9-BDF9-80D6F6E22769)
- [LIST_PROJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-22ADCE1C-14C2-49A6-9415-F220CF30708A)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-03CE484B-69F9-402B-8A9A-25B6B9F374B0)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-4902968A-2D4E-4CDC-8512-3BE0BAC2A781)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-EC7E44FA-38E4-4F66-8C33-6B4DF277ACA7)
- [UPDATE_DATA_SCIENCE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-A21451A6-FF08-4959-89D5-4BD226F0DE62)
- [UPDATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-B380E1FF-20BA-4E38-9757-C1B34C410147)
- [UPDATE_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-1C246936-80AC-4449-9CB6-853235DB9BF1)
- [UPDATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-D7B1AE69-2ED4-446E-B03E-B26AD8874D15)
- [UPDATE_MODEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-836BA7EA-6E54-4814-A73B-CA8EE41E2DFC)
- [UPDATE_MODEL_PROVENANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-094CE5B1-F48F-4F54-887A-353B4F2EFE22)
- [UPDATE_MODEL_VERSION_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-7928AEEF-9AA0-4E27-B0DF-0CF0E07AE680)
- [UPDATE_NOTEBOOK_SESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-B11B6108-1CD6-4B51-A01A-0AC201BE6991)
- [UPDATE_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-6B6B5E72-4874-4BAD-9A93-605E70C7C207)
- [UPDATE_PIPELINE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-247CCD95-C056-4EE8-A735-F0F9ACD631DB)
- [UPDATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dsc_data_science.html#ADSDK-GUID-902D2CB1-7923-4EE5-A8BF-E42638A3662A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
