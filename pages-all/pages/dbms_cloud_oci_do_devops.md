# DevOps Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#dcoc-content-body)

## DevOps Functions

Package: DBMS_CLOUD_OCI_DO_DEVOPS

### APPROVE_DEPLOYMENT Function

Submit stage approval.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) Unique deployment identifier.

`approve_deployment_details`

(required) The stage information for approval.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_BUILD_RUN Function

Cancels the build run based on the build run ID provided in the request.

Syntax
```

```

Parameters

Parameter Description

`cancel_build_run_details`

(required) Parameter details required to cancel a build run.

`build_run_id`

(required) Unique build run identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_DEPLOYMENT Function

Cancels a deployment resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) Unique deployment identifier.

`cancel_deployment_details`

(required) The information regarding the deployment to be canceled.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_SCHEDULED_CASCADING_PROJECT_DELETION Function

Cascading operation that restores Project and child resources from a DELETING state to an active state

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PROJECT_COMPARTMENT Function

Moves a project resource from one compartment OCID to another.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`change_project_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BUILD_PIPELINE Function

Creates a new build pipeline.

Syntax
```

```

Parameters

Parameter Description

`create_build_pipeline_details`

(required) Details for the new build pipeline.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BUILD_PIPELINE_STAGE Function

Creates a new stage.

Syntax
```

```

Parameters

Parameter Description

`create_build_pipeline_stage_details`

(required) Details for the new stage.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BUILD_RUN Function

Starts a build pipeline run for a predefined build pipeline. Please ensure the completion of any work request for creation/updation of Build Pipeline before starting a Build Run.

Syntax
```

```

Parameters

Parameter Description

`create_build_run_details`

(required) Parameter details required to create a new build run.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION Function

Creates a new connection.

Syntax
```

```

Parameters

Parameter Description

`create_connection_details`

(required) Details for the new connection.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOY_ARTIFACT Function

Creates a new deployment artifact.

Syntax
```

```

Parameters

Parameter Description

`create_deploy_artifact_details`

(required) Details for the new deployment artifact.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOY_ENVIRONMENT Function

Creates a new deployment environment.

Syntax
```

```

Parameters

Parameter Description

`create_deploy_environment_details`

(required) Details for the new deployment environment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOY_PIPELINE Function

Creates a new deployment pipeline.

Syntax
```

```

Parameters

Parameter Description

`create_deploy_pipeline_details`

(required) Details for the new deployment pipeline.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOY_STAGE Function

Creates a new deployment stage.

Syntax
```

```

Parameters

Parameter Description

`create_deploy_stage_details`

(required) Details for the new deployment stage.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOYMENT Function

Creates a new deployment.

Syntax
```

```

Parameters

Parameter Description

`create_deployment_details`

(required) Details for the new deployment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) Details for the new project.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REPOSITORY Function

Creates a new repository.

Syntax
```

```

Parameters

Parameter Description

`create_repository_details`

(required) Details for the new repository.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TRIGGER Function

Creates a new trigger.

Syntax
```

```

Parameters

Parameter Description

`create_trigger_details`

(required) Details for the new trigger.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BUILD_PIPELINE Function

Deletes a build pipeline resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_id`

(required) Unique build pipeline identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BUILD_PIPELINE_STAGE Function

Deletes a stage based on the stage ID provided in the request.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_stage_id`

(required) Unique stage identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION Function

Deletes a connection resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) Unique connection identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOY_ARTIFACT Function

Deletes a deployment artifact resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_artifact_id`

(required) Unique artifact identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOY_ENVIRONMENT Function

Deletes a deployment environment resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_environment_id`

(required) Unique environment identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOY_PIPELINE Function

Deletes a deployment pipeline resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_pipeline_id`

(required) Unique pipeline identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOY_STAGE Function

Deletes a deployment stage resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_stage_id`

(required) Unique stage identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROJECT Function

Deletes a project resource by identifier

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REF Function

Deletes a Repository's Ref by its name. Returns an error if the name is ambiguous. Can be disambiguated by using full names like \"heads/&lt;name&gt;\" or \"tags/&lt;name&gt;\".

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(required) A filter to return only resources that match the given reference name.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPOSITORY Function

Deletes a repository resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TRIGGER Function

Deletes a trigger resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`trigger_id`

(required) Unique trigger identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BUILD_PIPELINE Function

Retrieves a build pipeline by identifier.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_id`

(required) Unique build pipeline identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BUILD_PIPELINE_STAGE Function

Retrieves a stage based on the stage ID provided in the request.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_stage_id`

(required) Unique stage identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BUILD_RUN Function

Returns the details of a build run for a given build run ID.

Syntax
```

```

Parameters

Parameter Description

`build_run_id`

(required) Unique build run identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMMIT Function

Retrieves a repository's commit by commit ID.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`commit_id`

(required) A filter to return only resources that match the given commit ID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMMIT_DIFF Function

Compares two revisions for their differences. Supports comparison between two references or commits.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`target_version`

(required) The commit or reference name that represents the newer changes against the base version.

`base_version`

(optional) The commit or reference name to compare changes against. If base version is not provided, the difference goes against an empty tree.

`is_comparison_from_merge_base`

(optional) Boolean value to indicate whether to use merge base or most recent revision.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION Function

Retrieves a connection by identifier.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) Unique connection identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOY_ARTIFACT Function

Retrieves a deployment artifact by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_artifact_id`

(required) Unique artifact identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOY_ENVIRONMENT Function

Retrieves a deployment environment by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_environment_id`

(required) Unique environment identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOY_PIPELINE Function

Retrieves a deployment pipeline by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_pipeline_id`

(required) Unique pipeline identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOY_STAGE Function

Retrieves a deployment stage by identifier.

Syntax
```

```

Parameters

Parameter Description

`deploy_stage_id`

(required) Unique stage identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOYMENT Function

Retrieves a deployment by identifier.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) Unique deployment identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FILE_DIFF Function

Gets the line-by-line difference between file on different commits. This API will be deprecated on Wed, 29 Mar 2023 01:00:00 GMT as it does not get recognized when filePath has '/'. This will be replaced by \"/repositories/{repositoryId}/file/diffs\"

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`file_path`

(required) Path to a file within a repository.

`base_version`

(required) The branch to compare changes against.

`target_version`

(required) The branch where changes are coming from.

`is_comparison_from_merge_base`

(optional) Boolean to indicate whether to use merge base or most recent revision.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MIRROR_RECORD Function

Returns either current mirror record or last successful mirror record for a specific mirror repository.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`mirror_record_type`

(required) The field of mirror record type. Only one mirror record type can be provided: current - The current mirror record. lastSuccessful - The last successful mirror record.

Allowed values are: 'current', 'lastSuccessful'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OBJECT Function

Retrieves blob of specific branch name/commit ID and file path.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`file_path`

(optional) A filter to return only commits that affect any of the specified paths.

`ref_name`

(optional) A filter to return only resources that match the given reference name.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OBJECT_CONTENT Function

Retrieve contents of a specified object.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`sha`

(required) The SHA of a blob or tree.

`file_path`

(optional) A filter to return only commits that affect any of the specified paths.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROJECT Function

Retrieves a project by identifier.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REF Function

Retrieves a repository's reference by its name with preference for branches over tags if the name is ambiguous. This can be disambiguated by using full names like \"heads/&lt;name&gt;\" or \"tags/&lt;name&gt;\".

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(required) A filter to return only resources that match the given reference name.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPO_FILE_DIFF Function

Gets the line-by-line difference between file on different commits.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`base_version`

(required) The branch to compare changes against.

`target_version`

(required) The branch where changes are coming from.

`file_path`

(optional) A filter to return only commits that affect any of the specified paths.

`is_comparison_from_merge_base`

(optional) Boolean to indicate whether to use merge base or most recent revision.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPO_FILE_LINES Function

Retrieve lines of a specified file. Supports starting line number and limit.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`revision`

(required) Retrieve file lines from specific revision.

`file_path`

(optional) A filter to return only commits that affect any of the specified paths.

`start_line_number`

(optional) Line number from where to start returning file lines.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPOSITORY Function

Retrieves a repository by identifier.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`fields`

(optional) Fields parameter can contain multiple flags useful in deciding the API functionality.

Allowed values are: 'branchCount', 'commitCount', 'sizeInBytes'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPOSITORY_ARCHIVE_CONTENT Function

Returns the archived repository information.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(optional) A filter to return only resources that match the given reference name.

`format`

(optional) The archive format query parameter for downloading repository endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPOSITORY_FILE_LINES Function

Retrieve lines of a specified file. Supports starting line number and limit. This API will be deprecated on Wed, 29 Mar 2023 01:00:00 GMT as it does not get recognized when filePath has '/'. This will be replaced by \"/repositories/{repositoryId}/file/lines\"

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`file_path`

(required) Path to a file within a repository.

`revision`

(required) Retrieve file lines from specific revision.

`start_line_number`

(optional) Line number from where to start returning file lines.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRIGGER Function

Retrieves a trigger by identifier.

Syntax
```

```

Parameters

Parameter Description

`trigger_id`

(required) Unique trigger identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the asynchronous work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTHORS Function

Retrieve a list of all the authors.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(optional) A filter to return only resources that match the given reference name.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BUILD_PIPELINE_STAGES Function

Returns a list of all stages in a compartment or build pipeline.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`build_pipeline_id`

(optional) The OCID of the parent build pipeline.

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return the stages that matches the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BUILD_PIPELINES Function

Returns a list of build pipelines.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only build pipelines that matches the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BUILD_RUNS Function

Returns a list of build run summary.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`build_pipeline_id`

(optional) Unique build pipeline identifier.

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only build runs that matches the given lifecycle state.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMMIT_DIFFS Function

Compares two revisions and lists the differences. Supports comparison between two references or commits.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`base_version`

(required) The commit or reference name to compare changes against.

`target_version`

(required) The commit or reference name where changes are coming from.

`is_comparison_from_merge_base`

(optional) Boolean value to indicate whether to use merge base or most recent revision.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMMITS Function

Returns a list of commits.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(optional) A filter to return only resources that match the given reference name.

`exclude_ref_name`

(optional) A filter to exclude commits that match the given reference name.

`file_path`

(optional) A filter to return only commits that affect any of the specified paths.

`timestamp_greater_than_or_equal_to`

(optional) A filter to return commits only created after the specified timestamp value.

`timestamp_less_than_or_equal_to`

(optional) A filter to return commits only created before the specified timestamp value.

`commit_message`

(optional) A filter to return any commits that contains the given message.

`author_name`

(optional) A filter to return any commits that are pushed by the requested author.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTIONS Function

Returns a list of connections.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only connections that matches the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`connection_type`

(optional) A filter to return only resources that match the given connection type.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOY_ARTIFACTS Function

Returns a list of deployment artifacts.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only DeployArtifacts that matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOY_ENVIRONMENTS Function

Returns a list of deployment environments.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`lifecycle_state`

(optional) A filter to return only DeployEnvironments that matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOY_PIPELINES Function

Returns a list of deployment pipelines.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`project_id`

(optional) unique project identifier

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only DeployPipelines that matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOY_STAGES Function

Retrieves a list of deployment stages.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`deploy_pipeline_id`

(optional) The ID of the parent pipeline.

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only deployment stages that matches the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENTS Function

Returns a list of deployments.

Syntax
```

```

Parameters

Parameter Description

`deploy_pipeline_id`

(optional) The ID of the parent pipeline.

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`project_id`

(optional) unique project identifier

`lifecycle_state`

(optional) A filter to return only Deployments that matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`time_created_less_than`

(optional) Search for DevOps resources that were created before a specific date. Specifying this parameter corresponding to `timeCreatedLessThan` parameter will retrieve all assessments created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_created_greater_than_or_equal_to`

(optional) Search for DevOps resources that were created after a specific date. Specifying this parameter corresponding to `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all security assessments created after the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MIRROR_RECORDS Function

Returns a list of mirror entry in history within 30 days.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATHS Function

Retrieves a list of files and directories in a repository.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref`

(optional) The name of branch/tag or commit hash it points to. If names conflict, order of preference is commit &gt; branch &gt; tag. You can disambiguate with \"heads/foobar\" and \"tags/foobar\". If left blank repository's default branch will be used.

`paths_in_subtree`

(optional) Flag to determine if files must be retrived recursively. Flag is False by default.

`folder_path`

(optional) The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order is ascending. If no value is specified name is default.

Allowed values are: 'type', 'sizeInBytes', 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment in which to list resources.

`id`

(optional) Unique identifier or OCID for listing a single resource by ID.

`lifecycle_state`

(optional) A filter to return only Projects that matches the given lifecycleState.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REFS Function

Returns a list of references.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_type`

(optional) Reference type to distinguish between branch and tag. If it is not specified, all references are returned.

Allowed values are: 'BRANCH', 'TAG'

`commit_id`

(optional) Commit ID in a repository.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`ref_name`

(optional) A filter to return only resources that match the given reference name.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for reference name is ascending. Default order for reference type is ascending. If no value is specified reference name is default.

Allowed values are: 'refType', 'refName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPOSITORIES Function

Returns a list of repositories given a compartment ID or a project ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`project_id`

(optional) unique project identifier

`repository_id`

(optional) Unique repository identifier.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycle state matches the given lifecycle state.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for name is ascending. If no value is specified time created is default.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRIGGERS Function

Returns a list of triggers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment in which to list resources.

`project_id`

(optional) unique project identifier

`lifecycle_state`

(optional) A filter to return only triggers that matches the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) Unique trigger identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment in which to list resources.

`work_request_id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources where the lifecycle state matches the given operation status.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'WAITING', 'NEEDS_ATTENTION'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use. Use either ascending or descending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.

Allowed values are: 'timeAccepted'

`operation_type_multi_value_query`

(optional) A filter to return only resources where their Operation Types matches the parameter operation types

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MIRROR_REPOSITORY Function

Synchronize a mirrored repository to the latest version from external providers.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_REPOSITORY_REF Function

Creates a new reference or updates an existing one.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`ref_name`

(required) A filter to return only resources that match the given reference name.

`put_repository_ref_details`

(required) The information to create a reference with the type specified in the query.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SCHEDULE_CASCADING_PROJECT_DELETION Function

Cascading operation that marks Project and child DevOps resources in a DELETING state for a retention period

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BUILD_PIPELINE Function

Updates the build pipeline.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_id`

(required) Unique build pipeline identifier.

`update_build_pipeline_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BUILD_PIPELINE_STAGE Function

Updates the stage based on the stage ID provided in the request.

Syntax
```

```

Parameters

Parameter Description

`build_pipeline_stage_id`

(required) Unique stage identifier.

`update_build_pipeline_stage_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BUILD_RUN Function

Updates the build run.

Syntax
```

```

Parameters

Parameter Description

`build_run_id`

(required) Unique build run identifier.

`update_build_run_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONNECTION Function

Updates the connection.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) Unique connection identifier.

`update_connection_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOY_ARTIFACT Function

Updates the deployment artifact.

Syntax
```

```

Parameters

Parameter Description

`deploy_artifact_id`

(required) Unique artifact identifier.

`update_deploy_artifact_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOY_ENVIRONMENT Function

Updates the deployment environment.

Syntax
```

```

Parameters

Parameter Description

`deploy_environment_id`

(required) Unique environment identifier.

`update_deploy_environment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOY_PIPELINE Function

Updates the deployment pipeline.

Syntax
```

```

Parameters

Parameter Description

`deploy_pipeline_id`

(required) Unique pipeline identifier.

`update_deploy_pipeline_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOY_STAGE Function

Updates the deployment stage.

Syntax
```

```

Parameters

Parameter Description

`deploy_stage_id`

(required) Unique stage identifier.

`update_deploy_stage_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOYMENT Function

Updates the deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) Unique deployment identifier.

`update_deployment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROJECT Function

Updates the project.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) Unique project identifier.

`update_project_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REPOSITORY Function

Updates the repository.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) Unique repository identifier.

`update_repository_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TRIGGER Function

Updates the trigger.

Syntax
```

```

Parameters

Parameter Description

`trigger_id`

(required) Unique trigger identifier.

`update_trigger_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_CONNECTION Function

Return whether the credentials of the connection are valid.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) Unique connection identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated earlier due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://devops.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [DevOps Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-D39DB358-E151-4216-95F9-77D48E41B98A)
- [APPROVE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-9CAB7A71-B907-4B48-9E3A-F9B0A48DF6B7)
- [CANCEL_BUILD_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A4C40B0D-86DE-4358-A123-1E87D0D40C55)
- [CANCEL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-E01BD59F-3EB9-4435-899E-29647B1A898C)
- [CANCEL_SCHEDULED_CASCADING_PROJECT_DELETION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-171F8B0C-0606-4476-84E3-CB232F675E86)
- [CHANGE_PROJECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-574E23B5-9A7D-454F-A2E8-114EF7D48697)
- [CREATE_BUILD_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-772B8EC5-A441-4769-B0C3-08D434CE8C48)
- [CREATE_BUILD_PIPELINE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-8BAC43C5-71E4-4C9A-8C03-5EFD44A68106)
- [CREATE_BUILD_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A8444DB0-3112-4478-892E-33888FBD4778)
- [CREATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-634BF3A8-5F69-4437-9002-8B4B9C89012B)
- [CREATE_DEPLOY_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-F484563C-43C8-442B-89A4-08E068357942)
- [CREATE_DEPLOY_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-F1D61D7C-AA3A-49C4-A38C-E56D16CBB5FD)
- [CREATE_DEPLOY_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-C41627A0-6D86-468C-A3D5-1FB2D6E9946F)
- [CREATE_DEPLOY_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-2B47A52E-1E70-46B1-B782-AFEB4AC5057A)
- [CREATE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-DE96123E-A11C-49B4-A33B-504220B4F22F)
- [CREATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-AD425081-6791-4692-B72F-0BEEBF5C9605)
- [CREATE_REPOSITORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-B5FE803E-EBE9-46CB-A25C-26FDF2AF150C)
- [CREATE_TRIGGER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-6D9121EE-049A-431B-8B93-2C0DB361F191)
- [DELETE_BUILD_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-845866C8-1BC7-4453-806D-A5A9E3AAD749)
- [DELETE_BUILD_PIPELINE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-1A60D307-205B-40AC-998F-FE82C4A0D198)
- [DELETE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-FBDFA28B-ABA5-47C3-83C6-4BF291027561)
- [DELETE_DEPLOY_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-8686A122-E8A6-43EF-BF91-896E870E9838)
- [DELETE_DEPLOY_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-96456E2C-5DF3-4CE0-9DCB-89971E6C3E8C)
- [DELETE_DEPLOY_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-E9A40A98-46BD-4FFD-897C-77581FBB913A)
- [DELETE_DEPLOY_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-7DF7C010-2B14-427B-AA8C-8875B9A3B404)
- [DELETE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-6BC13ECB-2E11-41CD-8F4F-A658EE4E10DB)
- [DELETE_REF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-3B230863-F63D-4279-BBF5-9A929E6EB85C)
- [DELETE_REPOSITORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-2921B30E-A107-4B18-8850-479460EB5F6C)
- [DELETE_TRIGGER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-6D3D9446-8E12-44D4-926D-677A368F9BA1)
- [GET_BUILD_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-70A978E7-9F8E-493C-B544-083CB02A2218)
- [GET_BUILD_PIPELINE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-DACAB730-0A87-4A33-9676-2611339A0492)
- [GET_BUILD_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A8EBF045-6CF3-4DCA-BC3D-F80D2A7FBF63)
- [GET_COMMIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-7A7C5C6F-D8A8-4EB7-A9B8-3017DA429D6F)
- [GET_COMMIT_DIFF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-7744750C-7C49-4DF4-AE34-B3A27CC0BE90)
- [GET_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-158EF0B4-91E0-4863-BE4F-359614130D71)
- [GET_DEPLOY_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A2D21488-526A-409D-84D6-85AFCDBF49B6)
- [GET_DEPLOY_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-63181880-4EEF-4F7E-BD5B-B19D89EFF93F)
- [GET_DEPLOY_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-0EB7A91A-19A1-48B2-8FE7-676B7DBA3FBC)
- [GET_DEPLOY_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-CC1BDD08-1BFD-4C2D-852B-2CAD641848FE)
- [GET_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A1C015ED-E2D5-4CF0-BF48-94DC2EE6A268)
- [GET_FILE_DIFF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-78C045EB-2069-4E76-830E-790D5C403729)
- [GET_MIRROR_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-B736BA13-20D8-49FD-A86E-9E6A4CBAE181)
- [GET_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-EB4FB317-DD9C-4363-B6DC-9A94EC6C6A85)
- [GET_OBJECT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-9237E476-AC48-46A5-B9EF-0521D29D964B)
- [GET_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-31BA4F77-D2FC-43FD-901D-40623D69CDD1)
- [GET_REF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-23CAF6A1-006A-4A93-8C10-B8CBA3B2B754)
- [GET_REPO_FILE_DIFF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A0EDECD5-614E-41B6-BE5C-952CEC4CE051)
- [GET_REPO_FILE_LINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-8DFFE4FD-45B9-4635-BCBA-C2613018F58C)
- [GET_REPOSITORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-82261EAC-B04A-437F-9E73-F8C41648DA54)
- [GET_REPOSITORY_ARCHIVE_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-337A79B8-6F81-4E5F-9130-81D8A1BCA4A3)
- [GET_REPOSITORY_FILE_LINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-4439F3E2-EA94-4B35-8029-D24B54D12146)
- [GET_TRIGGER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-9A0EAA8E-C3AE-4DD1-AEBE-4362640266E2)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-BB0F0D6B-3328-488C-B18C-C0517FD22B43)
- [LIST_AUTHORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-CF29F97C-3448-4CCD-A7E8-EA52341FED5B)
- [LIST_BUILD_PIPELINE_STAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-ACFF8A5A-F75F-4F73-91A4-0C7E3DFD6947)
- [LIST_BUILD_PIPELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-15890A42-1F32-4BE0-993D-DAB2D12DC44A)
- [LIST_BUILD_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-1934E751-D14E-4547-9CB1-AC6DFA54CCCB)
- [LIST_COMMIT_DIFFS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-DA57FB5E-1730-4672-A3C0-0A3611FC7AAF)
- [LIST_COMMITS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-35C91A05-F70F-48C9-BF2F-1DCF378EF889)
- [LIST_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-0429C38E-4775-46FA-841B-27087D46B3F0)
- [LIST_DEPLOY_ARTIFACTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-43B19F2B-9C07-4D79-AFCF-D86BAC9FE237)
- [LIST_DEPLOY_ENVIRONMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-7DA9B9B5-28D8-495E-BCE9-37CEA339B129)
- [LIST_DEPLOY_PIPELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-9DB4ED6F-F8BE-4DF5-9056-1BE18759D73B)
- [LIST_DEPLOY_STAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-69FF461B-3019-485D-9689-1415C66E6A95)
- [LIST_DEPLOYMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-C466199B-4DD4-4426-BCBB-9F1B25C3ABA3)
- [LIST_MIRROR_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-D74C1640-DF11-4C59-A4BA-529348A4EFB7)
- [LIST_PATHS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-BFD34FF6-025A-4CA9-B8AC-42E7378C3973)
- [LIST_PROJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A3B2F362-7739-4E44-B15D-0922D490F9A9)
- [LIST_REFS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-6F3E58D3-01B3-4C7B-A2CD-CFA0BF868455)
- [LIST_REPOSITORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-E7A09840-7764-4F2E-9E79-678DF1D5D86D)
- [LIST_TRIGGERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-9769DF52-41F7-41DD-A9C5-D7B354A400E2)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-DC1715B4-406F-4AC9-BA73-42E473988A7A)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-40EFAC0F-E8EB-40A0-A08C-361C0FDBFC62)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-823681F5-DC28-4B06-8DD4-A737B251291E)
- [MIRROR_REPOSITORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-63266BAF-BEA0-4466-B490-D276F31ADBA5)
- [PUT_REPOSITORY_REF Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-3D2F77A8-6F04-4CB9-A637-3B8EF9852564)
- [SCHEDULE_CASCADING_PROJECT_DELETION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-48868B3C-F147-4CE0-83BF-71396D6D2CAA)
- [UPDATE_BUILD_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-396C6E5C-A01F-419E-A9DE-C34C1D9A0A95)
- [UPDATE_BUILD_PIPELINE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-1A96EE87-46CB-4A2E-B73D-47057599DB38)
- [UPDATE_BUILD_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-231BCA44-A593-41EA-B2EB-03B4F958AC97)
- [UPDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-5E3B3936-397C-4CC2-AD99-B416ACC3BEF7)
- [UPDATE_DEPLOY_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-A62A1C25-0381-43D6-9F51-DD7CAF80FFAE)
- [UPDATE_DEPLOY_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-915BC1B0-EC0A-4A3D-BA35-A91D274C344E)
- [UPDATE_DEPLOY_PIPELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-84FFA7A9-0644-4F39-A1BB-443E19DBAC62)
- [UPDATE_DEPLOY_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-F0BBAEF7-8A85-4CF7-85B2-A45656DFB260)
- [UPDATE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-45011BD7-D3B2-4CFE-A9DD-40B431F80BAE)
- [UPDATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-894A6134-1BDC-48F9-9B46-FE872B955A11)
- [UPDATE_REPOSITORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-77E9A230-A432-415D-871D-0C4911007738)
- [UPDATE_TRIGGER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-119893E3-5542-45E1-8A9F-809632851F49)
- [VALIDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_do_devops.html#ADSDK-GUID-7DF988F2-9006-4436-BFAF-B68250039BD2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
