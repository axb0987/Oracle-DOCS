# Disaster Recovery Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#dcoc-content-body)

## Disaster Recovery Functions

Package: DBMS_CLOUD_OCI_DR_DISASTER_RECOVERY

### ASSOCIATE_DR_PROTECTION_GROUP Function

Create an association between the DR protection group identified by *drProtectionGroupId* and another DR protection group.

Syntax
```

```

Parameters

Parameter Description

`associate_dr_protection_group_details`

(required) Details for creating an association between two DR protection groups.

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_DR_PLAN_EXECUTION Function

Cancel the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`cancel_dr_plan_execution_details`

(required) Details for canceling the DR plan execution.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancel the work request identified by *workRequestId*.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID (OCID) of the asynchronous request. Example: `ocid1.workrequest.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DR_PROTECTION_GROUP_COMPARTMENT Function

Move the DR protection group identified by *drProtectionGroupId* to a different compartment.

Syntax
```

```

Parameters

Parameter Description

`change_dr_protection_group_compartment_details`

(required) Details for changing the DR protection group compartment.

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DR_PLAN Function

Create a DR plan of the specified DR plan type.

Syntax
```

```

Parameters

Parameter Description

`create_dr_plan_details`

(required) Details for creating the new DR plan.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DR_PLAN_EXECUTION Function

Execute a DR plan for a DR protection group.

Syntax
```

```

Parameters

Parameter Description

`create_dr_plan_execution_details`

(required) Details for creating the DR plan execution.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DR_PROTECTION_GROUP Function

Create a DR protection group.

Syntax
```

```

Parameters

Parameter Description

`create_dr_protection_group_details`

(required) Details for creating the DR protection group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DR_PLAN Function

Delete the DR plan identified by *drPlanId*.

Syntax
```

```

Parameters

Parameter Description

`dr_plan_id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DR_PLAN_EXECUTION Function

Delete the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DR_PROTECTION_GROUP Function

Delete the DR protection group identified by *drProtectionGroupId*.

Syntax
```

```

Parameters

Parameter Description

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISASSOCIATE_DR_PROTECTION_GROUP Function

Delete the association between the DR protection group identified by *drProtectionGroupId*. and its peer DR protection group.

Syntax
```

```

Parameters

Parameter Description

`disassociate_dr_protection_group_details`

(required) Details for deleting the association between two DR protection groups.

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DR_PLAN Function

Get details for the DR plan identified by *drPlanId*.

Syntax
```

```

Parameters

Parameter Description

`dr_plan_id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DR_PLAN_EXECUTION Function

Get details for the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DR_PROTECTION_GROUP Function

Get the DR protection group identified by *drProtectionGroupId*.

Syntax
```

```

Parameters

Parameter Description

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Get the status of the work request identified by *workRequestId*.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID (OCID) of the asynchronous request. Example: `ocid1.workrequest.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IGNORE_DR_PLAN_EXECUTION Function

Ignore the failed group or step in DR plan execution identified by *drPlanExecutionId* and resume execution.

Syntax
```

```

Parameters

Parameter Description

`ignore_dr_plan_execution_details`

(required) Details for ignoring the failed group or step and resuming execution.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DR_PLAN_EXECUTIONS Function

Get a summary list of all DR plan executions for a DR protection group.

Syntax
```

```

Parameters

Parameter Description

`dr_protection_group_id`

(required) The OCID of the DR protection group. Mandatory query param. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`lifecycle_state`

(optional) A filter to return only DR plan executions that match the given lifecycle state.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'DELETING', 'DELETED', 'PAUSING', 'PAUSED', 'RESUMING'

`dr_plan_execution_id`

(optional) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`dr_plan_execution_type`

(optional) The DR plan execution type.

Allowed values are: 'SWITCHOVER', 'SWITCHOVER_PRECHECK', 'FAILOVER', 'FAILOVER_PRECHECK', 'START_DRILL', 'START_DRILL_PRECHECK', 'STOP_DRILL', 'STOP_DRILL_PRECHECK'

`display_name`

(optional) A filter to return only resources that match the given display name. Example: `MyResourceDisplayName`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default. Example: `MyResourceDisplayName`

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DR_PLANS Function

Get a summary list of all DR plans for a DR protection group.

Syntax
```

```

Parameters

Parameter Description

`dr_protection_group_id`

(required) The OCID of the DR protection group. Mandatory query param. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`lifecycle_state`

(optional) A filter to return only DR plans that match the given lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`dr_plan_id`

(optional) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`dr_plan_type`

(optional) The DR plan type.

Allowed values are: 'SWITCHOVER', 'FAILOVER', 'START_DRILL', 'STOP_DRILL'

`display_name`

(optional) A filter to return only resources that match the given display name. Example: `MyResourceDisplayName`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default. Example: `MyResourceDisplayName`

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DR_PROTECTION_GROUPS Function

Get a summary list of all DR protection groups in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID (OCID) of the compartment in which to list resources. Example: `ocid1.compartment.oc1..uniqueID`

`lifecycle_state`

(optional) A filter to return only DR protection groups that match the given lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`dr_protection_group_id`

(optional) The OCID of the DR protection group. Optional query param. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`display_name`

(optional) A filter to return only resources that match the given display name. Example: `MyResourceDisplayName`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default. Example: `MyResourceDisplayName`

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`role`

(optional) The DR protection group Role.

Allowed values are: 'PRIMARY', 'STANDBY', 'UNCONFIGURED'

`lifecycle_sub_state`

(optional) A filter to return only DR protection groups that match the given lifecycle sub-state.

Allowed values are: 'DR_DRILL_IN_PROGRESS'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Get a list of work request errors for the work request identified by *workRequestId*.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID (OCID) of the asynchronous request. Example: `ocid1.workrequest.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Get a list of logs for the work request identified by *workRequestId*.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID (OCID) of the asynchronous request. Example: `ocid1.workrequest.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The ID (OCID) of the compartment in which to list resources. Example: `ocid1.compartment.oc1..uniqueID`

`work_request_id`

(optional) The ID (OCID) of the asynchronous work request. Example: `ocid1.workrequest.oc1..uniqueID`

`status`

(optional) A filter to return only resources whose lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'NEEDS_ATTENTION'

`resource_id`

(optional) The ID (OCID) of the resource affected by the work request. Example: `ocid1.drplanexecution.oc1..uniqueID`

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PAUSE_DR_PLAN_EXECUTION Function

Pause the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`pause_dr_plan_execution_details`

(required) Details for pausing the DR plan execution.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESUME_DR_PLAN_EXECUTION Function

Resume the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`resume_dr_plan_execution_details`

(required) Details for resuming the DR plan execution.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRY_DR_PLAN_EXECUTION Function

Retry the failed group or step in DR plan execution identified by *drPlanExecutionId* and resume execution.

Syntax
```

```

Parameters

Parameter Description

`retry_dr_plan_execution_details`

(required) Details for retrying execution of the failed group or step.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DR_PLAN Function

Update the DR plan identified by *drPlanId*.

Syntax
```

```

Parameters

Parameter Description

`update_dr_plan_details`

(required) Details for updating the DR plan.

`dr_plan_id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DR_PLAN_EXECUTION Function

Update the DR plan execution identified by *drPlanExecutionId*.

Syntax
```

```

Parameters

Parameter Description

`update_dr_plan_execution_details`

(required) Details for updating the DR plan execution.

`dr_plan_execution_id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DR_PROTECTION_GROUP Function

Update the DR protection group identified by *drProtectionGroupId*.

Syntax
```

```

Parameters

Parameter Description

`update_dr_protection_group_details`

(required) Details for updating the the DR protection group.

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DR_PROTECTION_GROUP_ROLE Function

Update the role of the DR protection group identified by *drProtectionGroupId*.

Syntax
```

```

Parameters

Parameter Description

`update_dr_protection_group_role_details`

(required) The role details for the DR protection group to be updated.

`dr_protection_group_id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://disaster-recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Disaster Recovery Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-CD64918A-B159-4F9A-BA9C-38D9A2939406)
- [ASSOCIATE_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-357E5E69-BC3B-4608-B1A3-668EA3728A8D)
- [CANCEL_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-C0C76BBF-479B-4E10-B888-1300CECA759B)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-9369EA5F-98B8-4BDF-9C05-E3F9C183CBEC)
- [CHANGE_DR_PROTECTION_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-5F0D626C-939B-428B-AE00-3C544390ECE9)
- [CREATE_DR_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-C5A09D7B-B8F6-4081-9472-8D842F5B8E1C)
- [CREATE_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-B3450187-DD45-4A43-AA33-113457F36098)
- [CREATE_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-F65EEEA0-5BE2-411B-B76B-FFE8FC1F83D7)
- [DELETE_DR_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-2203D448-FB9E-4BF3-B0D5-45712649975D)
- [DELETE_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-0C583CBA-EF21-4939-9714-C9F37E81A5BF)
- [DELETE_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-CDB0354C-7577-4090-A95D-256F99BED975)
- [DISASSOCIATE_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-1645DD54-7210-4275-8ED9-81FDE4ABC65A)
- [GET_DR_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-D40F14AF-2BF5-416C-BB43-8656BFE263A7)
- [GET_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-BFBCB318-AB4B-4A55-B25A-F4AC8A29C2BC)
- [GET_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-EA498B64-0094-4F0F-8EB7-93305EE8B547)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-1CCA88D4-7849-4523-BE27-F7A547DA5BC7)
- [IGNORE_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-F39C91C0-CCDA-42E1-8FC9-AD2A3BF8F1EE)
- [LIST_DR_PLAN_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-325FF1B8-35B0-4BCC-BD87-F05449DC5579)
- [LIST_DR_PLANS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-51B490D3-EB8E-466A-9387-AF028ABC47B3)
- [LIST_DR_PROTECTION_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-230EA222-B18B-4EE4-B697-20816779E943)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-54FC589C-1A1D-40D2-B2DA-914CFD4CD1BC)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-8CABEFC5-68B1-4B40-A7D4-DFB9D5DF7935)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-404D6446-1575-4574-9545-824E8BF5F339)
- [PAUSE_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-4BA54D0D-DD5F-4E0E-AF2D-550C2DB61B37)
- [RESUME_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-261E49E4-836B-4CC2-A957-F0CC1F3C1197)
- [RETRY_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-95AEB57D-5B2E-4E0E-8591-49219929C70E)
- [UPDATE_DR_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-E50ABA5C-EF76-4208-B5B3-C66DA7AEBC16)
- [UPDATE_DR_PLAN_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-8E5CF881-B47E-440C-8E02-1F4E91459D47)
- [UPDATE_DR_PROTECTION_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-F76780AD-8B3E-4009-9C5C-DCE28D9668E7)
- [UPDATE_DR_PROTECTION_GROUP_ROLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dr_disaster_recovery.html#ADSDK-GUID-F71C1C4E-3396-4853-8291-F3A4B03597C5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
