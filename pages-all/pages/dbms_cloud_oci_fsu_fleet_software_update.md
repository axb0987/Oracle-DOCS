# Fleet Software Update Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#dcoc-content-body)

## Fleet Software Update Functions

Package: DBMS_CLOUD_OCI_FSU_FLEET_SOFTWARE_UPDATE

### ABORT_FSU_DISCOVERY Function

Aborts Exadata Fleet Update Discovery in progress.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_FSU_COLLECTION_TARGETS Function

Adds targets to an existing Exadata Fleet Update Collection. Targets that are already part of a different Collection with an active Fleet Software Update Cycle cannot be added. This operation can only be performed on Collections that do not have an Action executing under an active Fleet Software Update Cycle. Additionally, during an active Fleet Software Update Cycle, targets can be added only prior to executing an Apply Action. This will require running a new Stage Action for the active Cycle.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`add_fsu_collection_targets_details`

(required) The Targets to be added into the Exadata Fleet Update Collection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_FSU_ACTION Function

Cancels a scheduled Action. Only applicable for Actions that have not started executing.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FSU_ACTION_COMPARTMENT Function

Moves a Exadata Fleet Update Action resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`change_fsu_action_compartment_details`

(required) The compartment where the Exadata Fleet Update Action will be moved to.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FSU_COLLECTION_COMPARTMENT Function

Moves a Exadata Fleet Update Collection resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`change_fsu_collection_compartment_details`

(required) The compartment where the Exadata Fleet Update Collection will be moved to.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FSU_CYCLE_COMPARTMENT Function

Moves a Exadata Fleet Update Cycle resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fsu_cycle_id`

(required) Unique Exadata Fleet Update Cycle identifier.

`change_fsu_cycle_compartment_details`

(required) The compartment where the Exadata Fleet Update Cycle will be moved to.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FSU_DISCOVERY_COMPARTMENT Function

Moves a Exadata Fleet Update Discovery resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`change_fsu_discovery_compartment_details`

(required) The compartment where the Exadata Fleet Update Discovery will be moved to

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CLONE_FSU_CYCLE Function

Clones existing Exadata Fleet Update Cycle details into a new Exadata Fleet Update Cycle resource.

Syntax
```

```

Parameters

Parameter Description

`fsu_cycle_id`

(required) Unique Exadata Fleet Update Cycle identifier.

`clone_fsu_cycle_details`

(required) The Exadata Fleet Update Cycle properties to be updated in the cloned Cycle instead of using the existing values.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FSU_ACTION Function

Creates a new Exadata Fleet Update Action.

Syntax
```

```

Parameters

Parameter Description

`create_fsu_action_details`

(required) Details for the new Exadata Fleet Update Action.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FSU_COLLECTION Function

Creates a new Exadata Fleet Update Collection.

Syntax
```

```

Parameters

Parameter Description

`create_fsu_collection_details`

(required) Details for the new Exadata Fleet Update Collection.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FSU_CYCLE Function

Creates a new Exadata Fleet Update Cycle.

Syntax
```

```

Parameters

Parameter Description

`create_fsu_cycle_details`

(required) Details for the new Exadata Fleet Update Cycle.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FSU_DISCOVERY Function

Creates a new Exadata Fleet Update Discovery.

Syntax
```

```

Parameters

Parameter Description

`create_fsu_discovery_details`

(required) Details for the new Exadata Fleet Update Discovery.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FSU_ACTION Function

Deletes a Exadata Fleet Update Action resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FSU_COLLECTION Function

Deletes a Exadata Fleet Update Collection resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FSU_CYCLE Function

Deletes a Exadata Fleet Update Cycle resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_cycle_id`

(required) Unique Exadata Fleet Update Cycle identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FSU_DISCOVERY Function

Deletes a Exadata Fleet Update Discovery resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FSU_JOB Function

Deletes the Exadata Fleet Update Job resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_ACTION Function

Gets a Exadata Fleet Update Action by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_ACTION_OUTPUT_CONTENT Function

Gets the Exadata Fleet Update Action Output content as a binary file (string). This will only include the output from FAILED Exadata Fleet Update Jobs. No content in case there are no FAILED jobs.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_COLLECTION Function

Gets a Exadata Fleet Update Collection by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_CYCLE Function

Gets a Exadata Fleet Update Cycle by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_cycle_id`

(required) Unique Exadata Fleet Update Cycle identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_DISCOVERY Function

Gets a Exadata Fleet Update Discovery by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_JOB Function

Gets a Exadata Fleet Update Job by identifier.

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FSU_JOB_OUTPUT_CONTENT Function

Get the Exadata Fleet Update Job Output content as a binary file (string).

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the specified ID.

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

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_ACTIONS Function

Gets a list of all Exadata Fleet Update Actions in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`fsu_cycle_id`

(optional) A filter to return only resources whose fsuCycleId matches the given fleetSoftwareUpdateCycleId.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'UPDATING', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'UNKNOWN', 'DELETING', 'DELETED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`l_type`

(optional) A filter to return only resources whose type matches the given type.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_COLLECTION_TARGETS Function

Gets a list of all Targets that are members of a specific Exadata Fleet Update Collection.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`target_id`

(optional) A filter to return a resource whose target OCID matches the given OCID.

`status`

(optional) A filter to return only entries whose status matches the given status.

Allowed values are: 'IDLE', 'EXECUTING_JOB', 'JOB_FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided.

Allowed values are: 'currentVersion', 'status'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_COLLECTIONS Function

Gets a list of all Exadata Fleet Update Collections in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`l_type`

(optional) A filter to return only resources whose type matches the given type.

Allowed values are: 'DB', 'GI'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_CYCLES Function

Gets a list of all Exadata Fleet Update Cycles in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`fsu_collection_id`

(optional) A filter to return only resources whose fsuCollectionId matches the given fsuCollectionId.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'IN_PROGRESS', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'DELETING', 'DELETED'

`collection_type`

(optional) A filter to return only resources whose Collection type matches the given type.

Allowed values are: 'DB', 'GI'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`target_version`

(optional) A filter to return only entries whose targetVersion matches the given targetVersion.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_DISCOVERIES Function

Returns a list of Exadata Fleet Update Discoveries resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_DISCOVERY_TARGETS Function

Gets a list of all Targets in the results of a Exadata Fleet Update Discovery.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`target_id`

(optional) A filter to return a resource whose target OCID matches the given OCID.

`status`

(optional) A filter to return only entries whose status matches the given status.

Allowed values are: 'IDLE', 'EXECUTING_JOB', 'JOB_FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided.

Allowed values are: 'currentVersion', 'status'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_JOB_OUTPUTS Function

Lists the Exadata Fleet Update Job Output messages, if any.

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FSU_JOBS Function

Lists all the Exadata Fleet Update Jobs associated to the specified Exadata Fleet Update Action.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'UNKNOWN', 'TERMINATED', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'WAITING', 'CANCELING', 'CANCELED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a paginated list of errors for a specified Work Request..

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

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a paginated list of logs for a specified Work Request.

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

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the compartment in which to list resources.

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

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_FSU_COLLECTION_TARGETS Function

Removes targets from an existing Exadata Fleet Update Collection. This operation can only be performed on Collections that do not have an Action executing under an active Fleet Software Update Cycle. Additionally, during an active Fleet Software Update Cycle, targets can be removed only prior to executing an Apply Action.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`remove_fsu_collection_targets_details`

(required) The Targets to be removed from the Exadata Fleet Update Collection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESUME_FSU_ACTION Function

Resumes an Action that has batches of targets waiting to execute.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRY_FSU_JOB Function

Retry a failed Job, only while the current Action is being executed. After the Action reaches a terminal state, a new Action of the same kind is required to retry on failed targets.

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FSU_ACTION Function

Updates the Exadata Fleet Update Action identified by the ID.

Syntax
```

```

Parameters

Parameter Description

`fsu_action_id`

(required) Unique Exadata Fleet Update Action identifier.

`update_fsu_action_details`

(required) The Exadata Fleet Update Action details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FSU_COLLECTION Function

Updates the Exadata Fleet Update Collection identified by the ID.

Syntax
```

```

Parameters

Parameter Description

`fsu_collection_id`

(required) Unique Exadata Fleet Update Collection identifier.

`update_fsu_collection_details`

(required) The Exadata Fleet Update Collection details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FSU_CYCLE Function

Updates the Exadata Fleet Update Cycle identified by the ID.

Syntax
```

```

Parameters

Parameter Description

`fsu_cycle_id`

(required) Unique Exadata Fleet Update Cycle identifier.

`update_fsu_cycle_details`

(required) The Exadata Fleet Update Cycle details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FSU_DISCOVERY Function

Updates the Exadata Fleet Update Discovery identified by the ID.

Syntax
```

```

Parameters

Parameter Description

`fsu_discovery_id`

(required) Unique Exadata Fleet Update Discovery identifier.

`update_fsu_discovery_details`

(required) The Exadata Fleet Update Discovery details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FSU_JOB Function

Updates Exadata Fleet Update Job resource details.

Syntax
```

```

Parameters

Parameter Description

`fsu_job_id`

(required) The OCID of the Exadata Fleet Update Job.

`update_fsu_job_details`

(required) The Exadata Fleet Update Job details to be updated.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fleet-software-update.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Fleet Software Update Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-041B3169-4442-4CA8-B372-EBA1202AD786)
- [ABORT_FSU_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-E0B3F7E5-3F47-4692-BB27-9DAC2690342E)
- [ADD_FSU_COLLECTION_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-951074C5-D98A-4225-B5E2-EBD89893E865)
- [CANCEL_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-10CDE4E0-AF04-4801-A304-116DBBDB065A)
- [CHANGE_FSU_ACTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-EE4B9E1D-EB8F-47EC-8A12-01E34FC884EB)
- [CHANGE_FSU_COLLECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-3B2E2B6F-9318-48A0-90FB-38A7A486CB29)
- [CHANGE_FSU_CYCLE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-FE4E1DBF-E1B2-4083-AF88-969ECCD2250F)
- [CHANGE_FSU_DISCOVERY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-63BE41F5-B640-4DB3-93CF-4DC97AAE5358)
- [CLONE_FSU_CYCLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-F31E5D39-0092-4969-8B44-E4C68370022B)
- [CREATE_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-22074439-029A-4A6D-9759-F8327BA1A490)
- [CREATE_FSU_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-B8825C61-FA82-4D7A-A238-6CF7F4CAF62D)
- [CREATE_FSU_CYCLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-60F9A8A0-6A94-4056-AD2F-855476416AFB)
- [CREATE_FSU_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-65D31218-F2C4-4F34-9A38-E1BC76125616)
- [DELETE_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-C34CE74E-B51B-4FE4-8283-3A17DCDD9152)
- [DELETE_FSU_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-FDFA9800-83B4-4513-8E51-167A8357C7CF)
- [DELETE_FSU_CYCLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-DFBED08E-0278-4BCE-A6D0-4708256C7383)
- [DELETE_FSU_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-9EED505A-A6CB-40AC-B543-C7E4450BC182)
- [DELETE_FSU_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-8D248C6E-E611-40AF-B6F1-7024D345C96A)
- [GET_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-94BD360C-AF96-46AC-B028-A44F9AA146C1)
- [GET_FSU_ACTION_OUTPUT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-577F323B-B5B3-4848-B659-D33477A36353)
- [GET_FSU_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-1D208659-4C12-4E44-A4C5-976BB740D499)
- [GET_FSU_CYCLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-19D9CA25-CE4A-4A22-A2DD-46F93B8C9952)
- [GET_FSU_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-8793E1B8-A337-4019-A64E-14829FD8DCCB)
- [GET_FSU_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-30945B6C-5742-4643-9118-E00616490A4B)
- [GET_FSU_JOB_OUTPUT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-6235FD21-9642-41E9-AFCC-463FA7E1374D)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-981BCBAE-B99B-4769-92A2-98C036B2AE0F)
- [LIST_FSU_ACTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-168035A9-A11A-4909-9F88-B697481E9547)
- [LIST_FSU_COLLECTION_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-B0D1A688-967A-4280-BE26-CE6B0A19B5E8)
- [LIST_FSU_COLLECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-BEB5B1A2-04F0-4465-A13F-9406018A2C04)
- [LIST_FSU_CYCLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-368EEE44-2EDD-4E46-A65D-7063D09545F1)
- [LIST_FSU_DISCOVERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-9294F4A3-C74E-417C-80AD-E43DB1A55F5B)
- [LIST_FSU_DISCOVERY_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-838F38ED-496B-466C-9631-BF0FF428E6B5)
- [LIST_FSU_JOB_OUTPUTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-50A9F73F-5349-4A6C-93DC-4A4CDEC8A579)
- [LIST_FSU_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-BCDFEDC3-AD78-40FD-A8FD-01CA0E769263)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-D5739238-A54A-497C-AFB6-396C0CCD528A)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-B18B038F-C6B1-4E3F-829D-82C16EF5A729)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-9432CA4D-D467-453B-84B6-A678D04A9257)
- [REMOVE_FSU_COLLECTION_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-B4456291-C0FB-4DE8-8614-07D82E161AC0)
- [RESUME_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-A5B6C758-00A3-433D-A174-9BCE793356FA)
- [RETRY_FSU_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-8F0DDA49-5848-47F3-B64D-92A1225B06C8)
- [UPDATE_FSU_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-D2F2564B-7D7D-40AE-8A5E-4A9455655C7C)
- [UPDATE_FSU_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-436AA50F-75F8-4CB7-B8EA-05E751B7F16F)
- [UPDATE_FSU_CYCLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-367C13AF-C957-428E-94B4-C1954B9BEF4D)
- [UPDATE_FSU_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-DB0C023D-EC10-42E9-954D-7CAA8103AE1D)
- [UPDATE_FSU_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fsu_fleet_software_update.html#ADSDK-GUID-4B8B626E-3092-49E7-BCC8-2A868ABA1AA9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
