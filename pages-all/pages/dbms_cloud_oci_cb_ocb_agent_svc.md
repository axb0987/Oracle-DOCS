# Cloud Bridge OCB Agent SVC Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#dcoc-content-body)

## Cloud Bridge OCB Agent SVC Functions

Package: DBMS_CLOUD_OCI_CB_OCB_AGENT_SVC

### ADD_AGENT_DEPENDENCY Function

Add a dependency to the environment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`add_agent_dependency_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AGENT_COMPARTMENT Function

Moves an Agent resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`change_agent_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AGENT_DEPENDENCY_COMPARTMENT Function

Moves a AgentDependency resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`agent_dependency_id`

(required) A unique AgentDependency identifier.

`change_agent_dependency_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ENVIRONMENT_COMPARTMENT Function

Moves a source environment resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`change_environment_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AGENT Function

Creates an Agent.

Syntax
```

```

Parameters

Parameter Description

`create_agent_details`

(required) Details of the new Agent.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AGENT_DEPENDENCY Function

Creates an AgentDependency.

Syntax
```

```

Parameters

Parameter Description

`create_agent_dependency_details`

(required) Details for the new AgentDependency.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENVIRONMENT Function

Creates a source environment.

Syntax
```

```

Parameters

Parameter Description

`create_environment_details`

(required) Details of for the new source environment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AGENT Function

Deletes an Agent resource identified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AGENT_DEPENDENCY Function

Deletes the AgentDependency resource based on an identifier.

Syntax
```

```

Parameters

Parameter Description

`agent_dependency_id`

(required) A unique AgentDependency identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ENVIRONMENT Function

Deletes a the source environment resource identified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AGENT Function

Gets an Agent by identifier.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AGENT_DEPENDENCY Function

Gets an AgentDependency by identifier.

Syntax
```

```

Parameters

Parameter Description

`agent_dependency_id`

(required) A unique AgentDependency identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENVIRONMENT Function

Gets a source environment by identifier.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PLUGIN Function

Gets a plugin by identifier.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`plugin_name`

(required) Unique plugin identifier path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AGENT_DEPENDENCIES Function

Returns a list of AgentDependencies such as AgentDependencyCollection.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`agent_id`

(optional) A filter to return only resources that match the given Agent ID.

`environment_id`

(optional) A filter to return only resources that match the given environment ID.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

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

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AGENTS Function

Returns a list of Agents.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`environment_id`

(optional) A filter to return only resources that match the given environment ID.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`agent_id`

(optional) A filter to return only resources that match the given Agent ID.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLIANCE_IMAGES Function

Returns a list of Appliance Images.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENVIRONMENTS Function

Returns a list of source environments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources where their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`environment_id`

(optional) A filter to return only resources that match the given environment ID.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_AGENT_DEPENDENCY Function

Adds a dependency to the source environment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`remove_agent_dependency_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AGENT Function

Updates the Agent.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`update_agent_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AGENT_DEPENDENCY Function

Updates the AgentDependency.

Syntax
```

```

Parameters

Parameter Description

`agent_dependency_id`

(required) A unique AgentDependency identifier.

`update_agent_dependency_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ENVIRONMENT Function

Updates the source environment.

Syntax
```

```

Parameters

Parameter Description

`environment_id`

(required) Unique environment identifier.

`update_environment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PLUGIN Function

Updates the plugin.

Syntax
```

```

Parameters

Parameter Description

`agent_id`

(required) Unique Agent identifier path parameter.

`plugin_name`

(required) Unique plugin identifier path parameter.

`update_plugin_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Cloud Bridge OCB Agent SVC Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-65208046-6F26-4921-86BF-BCD87A4C0AF8)
- [ADD_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-91EE3E76-4456-444F-B497-36FE45B46FDE)
- [CHANGE_AGENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-9852604D-EF98-4C4C-8108-8BFBAD0BC654)
- [CHANGE_AGENT_DEPENDENCY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-F2FF0824-AE25-4864-BF26-CA7B5B0FBA4B)
- [CHANGE_ENVIRONMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-BB8F05C3-40E4-4384-98EA-77A1616AE77C)
- [CREATE_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-EAF31781-398F-4FB3-BB17-654111A1E9BD)
- [CREATE_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-15AE8D63-5451-4E0D-A526-566D4974BD10)
- [CREATE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-DD4829DF-18DA-4227-9EEF-0DD27F80CC01)
- [DELETE_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-933E4686-046C-4F0D-8D6D-86B6A5C27099)
- [DELETE_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-9DC42823-1D0C-475B-8E3C-8A23A6632818)
- [DELETE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-D1EF1BA8-C54C-4E5D-878E-C983F7C8A539)
- [GET_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-44D34C58-EB59-49E6-AEDF-60264A83CEB9)
- [GET_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-5F7F0A87-7BE9-4685-AD2B-A0C577618941)
- [GET_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-88D4B06A-102B-4016-9786-DE95A2F63407)
- [GET_PLUGIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-A561A798-D61B-4D69-9F6C-F1B04049B1CF)
- [LIST_AGENT_DEPENDENCIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-BDA1B673-D0D5-4AF5-9AEC-08F10F11CBAA)
- [LIST_AGENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-B73924CF-02BF-499E-A8F4-F8FB07427318)
- [LIST_APPLIANCE_IMAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-5FF6717A-4042-4AED-9CAD-E420D0238A2C)
- [LIST_ENVIRONMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-62E61F3B-9585-47A7-BB2E-D4066C9B24F7)
- [REMOVE_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-A00A79E1-10ED-41D7-AD6E-B0EA679D57B8)
- [UPDATE_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-C0724915-C02F-47D8-B029-DC33B33A947F)
- [UPDATE_AGENT_DEPENDENCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-D9C3F27B-E95C-4219-95F2-81A560870D31)
- [UPDATE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-F8743600-5BC1-4C7D-8975-02922F79AC4E)
- [UPDATE_PLUGIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_ocb_agent_svc.html#ADSDK-GUID-01852FAE-8CE3-4DF9-8F90-563AA522F8D9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
