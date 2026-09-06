# Fusion Apps Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#dcoc-content-body)

## Fusion Apps Functions

Package: DBMS_CLOUD_OCI_FA_FUSION_APPLICATIONS

### CHANGE_FUSION_ENVIRONMENT_COMPARTMENT Function

Moves a FusionEnvironment into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`change_fusion_environment_compartment_details`

(required) The details of change compartment request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FUSION_ENVIRONMENT_FAMILY_COMPARTMENT Function

Moves a FusionEnvironmentFamily into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`change_fusion_environment_family_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_MASKING_ACTIVITY Function

Creates a new DataMaskingActivity.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`create_data_masking_activity_details`

(required) Details for the new DataMaskingActivity.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FUSION_ENVIRONMENT Function

Creates a new FusionEnvironment.

Syntax
```

```

Parameters

Parameter Description

`create_fusion_environment_details`

(required) Details for the new FusionEnvironment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FUSION_ENVIRONMENT_ADMIN_USER Function

Create a FusionEnvironment admin user

Syntax
```

```

Parameters

Parameter Description

`create_fusion_environment_admin_user_details`

(required) The admin user to be created.

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FUSION_ENVIRONMENT_FAMILY Function

Creates a new FusionEnvironmentFamily.

Syntax
```

```

Parameters

Parameter Description

`create_fusion_environment_family_details`

(required) Details for the new FusionEnvironmentFamily.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REFRESH_ACTIVITY Function

Creates a new RefreshActivity.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`create_refresh_activity_details`

(required) Details for the new RefreshActivity.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_ATTACHMENT Function

Attaches a service instance to the fusion pod.

Syntax
```

```

Parameters

Parameter Description

`create_service_attachment_details`

(required) Details for the service attachment.

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FUSION_ENVIRONMENT Function

Deletes the Fusion environment identified by it's OCID.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FUSION_ENVIRONMENT_ADMIN_USER Function

Deletes the FusionEnvironment administrator user identified by the username.

Syntax
```

```

Parameters

Parameter Description

`admin_username`

(required) The admin user name for the fusion environment.

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FUSION_ENVIRONMENT_FAMILY Function

Deletes a FusionEnvironmentFamily resource by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REFRESH_ACTIVITY Function

Deletes a scheduled RefreshActivity resource by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`refresh_activity_id`

(required) The unique identifier (OCID) of the Refresh activity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_ATTACHMENT Function

Delete a service attachment by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`service_attachment_id`

(required) OCID of the Service Attachment

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_MASKING_ACTIVITY Function

Gets a DataMaskingActivity by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`data_masking_activity_id`

(required) Unique DataMasking run identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUSION_ENVIRONMENT Function

Gets a FusionEnvironment by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUSION_ENVIRONMENT_FAMILY Function

Retrieves a fusion environment family identified by its OCID.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUSION_ENVIRONMENT_FAMILY_LIMITS_AND_USAGE Function

Gets the number of environments (usage) of each type in the fusion environment family, as well as the limit that's allowed to be created based on the group's associated subscriptions.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUSION_ENVIRONMENT_FAMILY_SUBSCRIPTION_DETAIL Function

Gets the subscription details of an fusion environment family.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUSION_ENVIRONMENT_STATUS Function

Gets the status of a Fusion environment identified by its OCID.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REFRESH_ACTIVITY Function

Gets a RefreshActivity by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`refresh_activity_id`

(required) The unique identifier (OCID) of the Refresh activity.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEDULED_ACTIVITY Function

Gets a ScheduledActivity by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`scheduled_activity_id`

(required) Unique ScheduledActivity identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_ATTACHMENT Function

Gets a Service Attachment by identifier

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`service_attachment_id`

(required) OCID of the Service Attachment

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADMIN_USERS Function

List all FusionEnvironment admin users

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_MASKING_ACTIVITIES Function

Returns a list of DataMaskingActivities.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`lifecycle_state`

(optional) A filter that returns all resources that match the specified status

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FUSION_ENVIRONMENT_FAMILIES Function

Returns a list of FusionEnvironmentFamilies.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`fusion_environment_family_id`

(optional) The ID of the fusion environment family in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter that returns all resources that match the specified lifecycle state.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FUSION_ENVIRONMENTS Function

Returns a list of FusionEnvironments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`fusion_environment_family_id`

(optional) The ID of the fusion environment family in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter that returns all resources that match the specified lifecycle state.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REFRESH_ACTIVITIES Function

Returns a list of RefreshActivities.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`time_scheduled_start_greater_than_or_equal_to`

(optional) A filter that returns all resources that are scheduled after this date

`time_expected_finish_less_than_or_equal_to`

(optional) A filter that returns all resources that end before this date

`lifecycle_state`

(optional) A filter that returns all resources that match the specified status

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULED_ACTIVITIES Function

Returns a list of ScheduledActivities.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`time_scheduled_start_greater_than_or_equal_to`

(optional) A filter that returns all resources that are scheduled after this date

`time_expected_finish_less_than_or_equal_to`

(optional) A filter that returns all resources that end before this date

`run_cycle`

(optional) A filter that returns all resources that match the specified run cycle.

`lifecycle_state`

(optional) A filter that returns all resources that match the specified status

`scheduled_activity_association_id`

(optional) A filter that returns all resources that match the specified scheduledActivityAssociationId.

`scheduled_activity_phase`

(optional) A filter that returns all resources that match the specified scheduledActivityPhase.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_ATTACHMENTS Function

Returns a list of service attachments.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter that returns all resources that match the specified lifecycle state.

`service_instance_type`

(optional) A filter that returns all resources that match the specified lifecycle state.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TIME_AVAILABLE_FOR_REFRESHES Function

Gets available refresh time for this fusion environment

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

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

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'TIME_CREATED', 'DISPLAY_NAME'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`resource_id`

(optional) The ID of the a resource in which to list associated resources.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESET_FUSION_ENVIRONMENT_PASSWORD Function

Resets the password of the Fusion Environment Administrator.

Syntax
```

```

Parameters

Parameter Description

`reset_fusion_environment_password_details`

(required) The information to be updated.

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`admin_username`

(required) The admin user name for the fusion environment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FUSION_ENVIRONMENT Function

Updates the FusionEnvironment

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`update_fusion_environment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FUSION_ENVIRONMENT_FAMILY Function

Updates the FusionEnvironmentFamily

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the FusionEnvironmentFamily.

`update_fusion_environment_family_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REFRESH_ACTIVITY Function

Updates a scheduled RefreshActivity.

Syntax
```

```

Parameters

Parameter Description

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`refresh_activity_id`

(required) The unique identifier (OCID) of the Refresh activity.

`update_refresh_activity_details`

(required) Details for the updating scheduled RefreshActivity.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VERIFY_SERVICE_ATTACHMENT Function

Verify whether a service instance can be attached to the fusion pod

Syntax
```

```

Parameters

Parameter Description

`verify_service_attachment_details`

(required) Details for the service attachment.

`fusion_environment_id`

(required) unique FusionEnvironment identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://fusionapps.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Fusion Apps Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-D9797B31-951F-4F14-8C3C-007E5F0687BB)
- [CHANGE_FUSION_ENVIRONMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-11DD2EA9-9B31-4C8D-A602-D837EDE1EDA5)
- [CHANGE_FUSION_ENVIRONMENT_FAMILY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-CE0D6694-5F78-411C-9153-C1DA2C33C9B1)
- [CREATE_DATA_MASKING_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-9540AE30-8A7B-47D4-9A29-F7D2126B853A)
- [CREATE_FUSION_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-9AED7A53-0A05-425A-AE25-2BC82DA0DEF9)
- [CREATE_FUSION_ENVIRONMENT_ADMIN_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-C10706C4-50D7-48A5-910D-11D456D91B2B)
- [CREATE_FUSION_ENVIRONMENT_FAMILY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-C53047A1-61EE-4EB8-AFFE-566C6B655627)
- [CREATE_REFRESH_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-1CF18513-B73E-46C8-9AB2-986B5CFE1BEA)
- [CREATE_SERVICE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-489D0966-AE08-47BE-96D4-E48D187C54E7)
- [DELETE_FUSION_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-ADB10E98-3F99-424C-A60F-E89E777D388B)
- [DELETE_FUSION_ENVIRONMENT_ADMIN_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-C35871E5-7990-4510-8BF2-2A52B293C56B)
- [DELETE_FUSION_ENVIRONMENT_FAMILY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-4A8E21BF-AAF9-4CDD-AD04-AB1AC588B9FF)
- [DELETE_REFRESH_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-672EC207-C91F-4E59-A551-9F6F820BE0CD)
- [DELETE_SERVICE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-FD2D7D2D-6A9F-4968-A26F-C5674B73A8F6)
- [GET_DATA_MASKING_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-360DD932-F514-44D5-ADAB-5D095442F5B6)
- [GET_FUSION_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-2806B738-123A-4CF0-AF86-41A57F55269D)
- [GET_FUSION_ENVIRONMENT_FAMILY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-1A73DF19-5F3C-4295-8206-67E9D561813A)
- [GET_FUSION_ENVIRONMENT_FAMILY_LIMITS_AND_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-36885E32-482A-4E91-869A-4D012705CA4A)
- [GET_FUSION_ENVIRONMENT_FAMILY_SUBSCRIPTION_DETAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-CF73EA26-9047-49D7-8243-D247EEC7DF65)
- [GET_FUSION_ENVIRONMENT_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-E194F47C-F6F2-4395-90A8-6AA75BFD10A3)
- [GET_REFRESH_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-7A114E75-228A-4630-84EE-17B5AAB01383)
- [GET_SCHEDULED_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-85E41420-B1BE-43C6-803C-9C47FF986D67)
- [GET_SERVICE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-9C4E91B1-15DB-40DC-A53E-191988D9FE8B)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-344D445D-F365-4FDE-947F-748734F191E8)
- [LIST_ADMIN_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-C74FC333-4CA8-49D8-B16D-0DFDF1EA026F)
- [LIST_DATA_MASKING_ACTIVITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-3873E6C2-4219-45FB-A0F7-F53FF90A8637)
- [LIST_FUSION_ENVIRONMENT_FAMILIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-457E037F-9FBD-4941-903E-3BF3BD971C38)
- [LIST_FUSION_ENVIRONMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-F000BA37-B315-483E-88FC-B0B300FCDAE4)
- [LIST_REFRESH_ACTIVITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-15B46067-CA17-4D2A-8045-F903EF8F1DCE)
- [LIST_SCHEDULED_ACTIVITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-3EEA0349-65FC-4E17-97A0-FBB4F904BC9B)
- [LIST_SERVICE_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-D58D429B-BE3F-4958-AFFF-CFF3FEA63747)
- [LIST_TIME_AVAILABLE_FOR_REFRESHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-FDF687E9-01F6-422C-B3F7-18599CF179B0)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-16C1CA6E-9694-4054-AD89-129F637CB472)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-79D8E8F3-94D0-44DB-9B2B-1164B321D2B4)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-4FA856FE-192E-4BF6-8D0E-DA594709BF56)
- [RESET_FUSION_ENVIRONMENT_PASSWORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-824A3DC0-CAF6-496B-94EF-01385EC51ACE)
- [UPDATE_FUSION_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-B29D6E55-C423-49CC-B202-8ECA70BBD23A)
- [UPDATE_FUSION_ENVIRONMENT_FAMILY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-68B10690-6C2C-4243-9941-2809B1C7D742)
- [UPDATE_REFRESH_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-77E6B1BA-2C57-432A-8AA6-3529038046A0)
- [VERIFY_SERVICE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fa_fusion_applications.html#ADSDK-GUID-E3845390-E667-4DA3-AD57-9C8EEB96DCED)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
