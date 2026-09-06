# Management Agent Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#dcoc-content-body)

## Management Agent Functions

Package: DBMS_CLOUD_OCI_MA_MANAGEMENT_AGENT

### CREATE_MANAGEMENT_AGENT_INSTALL_KEY Function

User creates a new install key as part of this API.

Syntax
```

```

Parameters

Parameter Description

`create_management_agent_install_key_details`

(required) Details of the Agent install Key

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGEMENT_AGENT Function

Deletes a Management Agent resource by identifier

Syntax
```

```

Parameters

Parameter Description

`management_agent_id`

(required) Unique Management Agent identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGEMENT_AGENT_INSTALL_KEY Function

Deletes a Management Agent install Key resource by identifier

Syntax
```

```

Parameters

Parameter Description

`management_agent_install_key_id`

(required) Unique Management Agent Install Key identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WORK_REQUEST Function

Cancel the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEPLOY_PLUGINS Function

Deploys Plugins to a given list of agentIds.

Syntax
```

```

Parameters

Parameter Description

`deploy_plugins_details`

(required) Details of Plugins to be deployed for a given list of Management Agents.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTO_UPGRADABLE_CONFIG Function

Get the AutoUpgradable configuration for all agents in a tenancy. The supplied compartmentId must be a tenancy root.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGEMENT_AGENT Function

Gets complete details of the inventory of a given agent id

Syntax
```

```

Parameters

Parameter Description

`management_agent_id`

(required) Unique Management Agent identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGEMENT_AGENT_INSTALL_KEY Function

Gets complete details of the Agent install Key for a given key id

Syntax
```

```

Parameters

Parameter Description

`management_agent_install_key_id`

(required) Unique Management Agent Install Key identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGEMENT_AGENT_INSTALL_KEY_CONTENT Function

Returns a file with Management Agent install Key in it

Syntax
```

```

Parameters

Parameter Description

`management_agent_install_key_id`

(required) Unique Management Agent Install Key identifier

`opc_request_id`

(optional) The client request ID for tracing.

`plugin_name`

(optional) Filter to return input plugin names uncommented in the output.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABILITY_HISTORIES Function

Lists the availability history records of Management Agent

Syntax
```

```

Parameters

Parameter Description

`management_agent_id`

(required) Unique Management Agent identifier

`opc_request_id`

(optional) The client request ID for tracing.

`time_availability_status_ended_greater_than`

(optional) Filter to limit the availability history results to that of time after the input time including the boundary record. Defaulted to current date minus one year. The date and time to be given as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_availability_status_started_less_than`

(optional) Filter to limit the availability history results to that of time before the input time including the boundary record Defaulted to current date. The date and time to be given as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Default order for timeAvailabilityStatusStarted is descending.

Allowed values are: 'timeAvailabilityStatusStarted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_AGENT_IMAGES Function

Get supported agent image information

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for platformType is descending. Default order for version is descending. If no value is specified platformType is default.

Allowed values are: 'platformType', 'version'

`name`

(optional) A filter to return only resources that match the entire platform name given.

`lifecycle_state`

(optional) Filter to return only Management Agents in the particular lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`install_type`

(optional) A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.

Allowed values are: 'AGENT', 'GATEWAY'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_AGENT_INSTALL_KEYS Function

Returns a list of Management Agent installed Keys.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`compartment_id_in_subtree`

(optional) if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.

`access_level`

(optional) Value of this is always \"ACCESSIBLE\" and any other value is not supported.

`lifecycle_state`

(optional) Filter to return only Management Agents in the particular lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) The display name for which the Key needs to be listed.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_AGENT_PLUGINS Function

Returns a list of managementAgentPlugins.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`display_name`

(optional) Filter to return only Management Agent Plugins having the particular display name.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) Filter to return only Management Agents in the particular lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`platform_type`

(optional) Filter to return only results having the particular platform type.

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`agent_id`

(optional) The ManagementAgentID of the agent from which the Management Agents to be filtered.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_AGENTS Function

Returns a list of Management Agents. If no explicit page size limit is specified, it will default to 1000 when compartmentIdInSubtree is true and 5000 otherwise. The response is limited to maximum 1000 records when compartmentIdInSubtree is true.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`plugin_name`

(optional) Filter to return only Management Agents having the particular Plugin installed. A special pluginName of 'None' can be provided and this will return only Management Agents having no plugin installed.

`version`

(optional) Filter to return only Management Agents having the particular agent version.

`display_name`

(optional) Filter to return only Management Agents having the particular display name.

`lifecycle_state`

(optional) Filter to return only Management Agents in the particular lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`availability_status`

(optional) Filter to return only Management Agents in the particular availability status.

Allowed values are: 'ACTIVE', 'SILENT', 'NOT_AVAILABLE'

`host_id`

(optional) Filter to return only Management Agents having the particular agent host id.

`platform_type`

(optional) Filter to return only results having the particular platform type.

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`is_customer_deployed`

(optional) true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.

`install_type`

(optional) A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.

Allowed values are: 'AGENT', 'GATEWAY'

`gateway_id`

(optional) Filter to return only results having the particular gatewayId.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName', 'host', 'availabilityStatus', 'platformType', 'pluginDisplayNames', 'version'

`opc_request_id`

(optional) The client request ID for tracing.

`compartment_id_in_subtree`

(optional) if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.

`access_level`

(optional) When the value is \"ACCESSIBLE\", insufficient permissions for a compartment will filter out resources in that compartment without rejecting the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment to which a request will be scoped.

`agent_id`

(optional) The ManagementAgentID of the agent from which the Management Agents to be filtered.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`status`

(optional) The OperationStatus of the workRequest

Allowed values are: 'CREATED', 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`l_type`

(optional) The OperationType of the workRequest

Allowed values are: 'DEPLOY_PLUGIN', 'UPGRADE_PLUGIN', 'CREATE_UPGRADE_PLUGINS', 'AGENTIMAGE_UPGRADE'

`time_created_greater_than_or_equal_to`

(optional) Filter for items with timeCreated greater or equal to provided value. given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SET_AUTO_UPGRADABLE_CONFIG Function

Sets the AutoUpgradable configuration for all agents in a tenancy. The supplied compartmentId must be a tenancy root.

Syntax
```

```

Parameters

Parameter Description

`set_auto_upgradable_config_details`

(required) Details of the AutoUpgradable configuration for agents of the tenancy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_MANAGEMENT_AGENT_COUNTS Function

Gets count of the inventory of agents for a given compartment id, group by, and isPluginDeployed parameters. Supported groupBy parameters: availabilityStatus, platformType, version

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`group_by`

(required) The field by which to group Management Agents. Currently, only one groupBy dimension is supported at a time.

Allowed values are: 'availabilityStatus', 'platformType', 'version'

`has_plugins`

(optional) When set to true then agents that have at least one plugin deployed will be returned. When set to false only agents that have no plugins deployed will be returned.

`install_type`

(optional) A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.

Allowed values are: 'AGENT', 'GATEWAY'

`compartment_id_in_subtree`

(optional) if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_MANAGEMENT_AGENT_PLUGIN_COUNTS Function

Gets count of the inventory of management agent plugins for a given compartment id and group by parameter. Supported groupBy parameter: pluginName

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to which a request will be scoped.

`group_by`

(required) The field by which to group Management Agent Plugins

Allowed values are: 'pluginName'

`compartment_id_in_subtree`

(optional) if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGEMENT_AGENT Function

API to update the console managed properties of the Management Agent.

Syntax
```

```

Parameters

Parameter Description

`management_agent_id`

(required) Unique Management Agent identifier

`update_management_agent_details`

(required) Details required for changing the console managed properties of the Management Agent.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGEMENT_AGENT_INSTALL_KEY Function

API to update the modifiable properties of the Management Agent install key.

Syntax
```

```

Parameters

Parameter Description

`management_agent_install_key_id`

(required) Unique Management Agent Install Key identifier

`update_management_agent_install_key_details`

(required) Details required for changing the modifiable properties of the Management Agent install key.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://management-agent.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Management Agent Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-3E9E0088-3B64-4C97-9F49-FD2F7FD376F3)
- [CREATE_MANAGEMENT_AGENT_INSTALL_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-CAF01BB8-7C32-4508-89E5-D6996A94C1A3)
- [DELETE_MANAGEMENT_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-A82A7FB5-BE57-4CD1-B835-67266A642BFC)
- [DELETE_MANAGEMENT_AGENT_INSTALL_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-8CB147F4-36E2-4A7A-A9D2-9F594D0C918B)
- [DELETE_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-183BCFCB-A38B-42F4-915F-5D8E7ABE6020)
- [DEPLOY_PLUGINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-175E54C1-2004-407A-B4F5-8706406D374D)
- [GET_AUTO_UPGRADABLE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-61F0BE92-B255-4C75-951D-990E40958FC0)
- [GET_MANAGEMENT_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-CA7625C5-DFA0-4016-B073-EBAC0F4C9B5F)
- [GET_MANAGEMENT_AGENT_INSTALL_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-170471BB-3559-4D1C-B02B-217C1D4C0A0F)
- [GET_MANAGEMENT_AGENT_INSTALL_KEY_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-0D9F5677-EA7F-4C33-B815-8E0088F8918E)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-12E87DA4-AA6B-4460-B853-9D2CAE394F1D)
- [LIST_AVAILABILITY_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-8B286CA9-E25F-4C9E-BEEB-88E1CB53EFE9)
- [LIST_MANAGEMENT_AGENT_IMAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-611A1100-1CD8-4AA9-B205-B4EA67F89B05)
- [LIST_MANAGEMENT_AGENT_INSTALL_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-AB596125-A1F3-4D57-AD2F-4927E9C43A02)
- [LIST_MANAGEMENT_AGENT_PLUGINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-BB4A82A3-962C-4B43-8BB0-FEF659AC0D1F)
- [LIST_MANAGEMENT_AGENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-2A8CD772-1C24-4E55-A29A-06B3EA2F3EFD)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-9AEA3E7D-9B89-4583-9A63-7B943CADDA58)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-014C8810-836C-4063-B433-8B645E16D527)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-81F4E3DC-F34E-4C76-B038-9B8931CAC3BD)
- [SET_AUTO_UPGRADABLE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-B69594DD-2156-4E05-92AA-DBB3EE4E94E6)
- [SUMMARIZE_MANAGEMENT_AGENT_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-42A427B9-00D9-43E6-A319-E8C857F5B305)
- [SUMMARIZE_MANAGEMENT_AGENT_PLUGIN_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-6046B6C8-4220-403E-8D1C-EF10404C3FB3)
- [UPDATE_MANAGEMENT_AGENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-4686A6B7-2906-4595-B42C-73AE2979278F)
- [UPDATE_MANAGEMENT_AGENT_INSTALL_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ma_management_agent.html#ADSDK-GUID-414AA032-8BF3-41BB-B385-E3EAE82DD3EC)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
