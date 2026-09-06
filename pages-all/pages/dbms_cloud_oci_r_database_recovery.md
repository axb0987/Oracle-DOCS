# Recovery Database Recovery Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#dcoc-content-body)

## Recovery Database Recovery Functions

Package: DBMS_CLOUD_OCI_R_DATABASE_RECOVERY

### CHANGE_PROTECTED_DATABASE_COMPARTMENT Function

Moves a protected database resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`protected_database_id`

(required) The protected database OCID.

`change_protected_database_compartment_details`

(required) The configuration details required to move a protected database from the existing compartment to a specified compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PROTECTION_POLICY_COMPARTMENT Function

Moves a protection policy resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`protection_policy_id`

(required) The protection policy OCID.

`change_protection_policy_compartment_details`

(required) The configuration details required to move a protection policy from the existing compartment to a specified compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_RECOVERY_SERVICE_SUBNET_COMPARTMENT Function

Moves a recovery service subnet resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`recovery_service_subnet_id`

(required) The recovery service subnet OCID.

`change_recovery_service_subnet_compartment_details`

(required) The configuration details required to move a Recovery Service subnet from the existing compartment to a specified compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROTECTED_DATABASE Function

Creates a new Protected Database.

Syntax
```

```

Parameters

Parameter Description

`create_protected_database_details`

(required) Describes the parameters required to create a protected database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROTECTION_POLICY Function

Creates a new Protection Policy.

Syntax
```

```

Parameters

Parameter Description

`create_protection_policy_details`

(required) Describes the parameters required to create a custom protection policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RECOVERY_SERVICE_SUBNET Function

Creates a new Recovery Service Subnet.

Syntax
```

```

Parameters

Parameter Description

`create_recovery_service_subnet_details`

(required) Describes the parameters required to create a recovery service subnet.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROTECTED_DATABASE Function

Deletes a protected database based on the specified protected database ID.

Syntax
```

```

Parameters

Parameter Description

`protected_database_id`

(required) The protected database OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROTECTION_POLICY Function

Deletes a specified protection policy. You can delete custom policies only. Deleting a Oracle predefined policies will result in status code 405 Method Not Allowed.

Syntax
```

```

Parameters

Parameter Description

`protection_policy_id`

(required) The protection policy OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RECOVERY_SERVICE_SUBNET Function

Deletes a specified recovery service subnet.

Syntax
```

```

Parameters

Parameter Description

`recovery_service_subnet_id`

(required) The recovery service subnet OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FETCH_PROTECTED_DATABASE_CONFIGURATION Function

Downloads the network service configuration file 'tnsnames.ora' for a specified protected database. Applies to user-defined recovery systems only.

Syntax
```

```

Parameters

Parameter Description

`protected_database_id`

(required) The protected database OCID.

`fetch_protected_database_configuration_details`

(optional) Which configuration to get

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROTECTED_DATABASE Function

Gets information about a specified protected database.

Syntax
```

```

Parameters

Parameter Description

`protected_database_id`

(required) The protected database OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROTECTION_POLICY Function

Gets information about a specified protection policy.

Syntax
```

```

Parameters

Parameter Description

`protection_policy_id`

(required) The protection policy OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECOVERY_SERVICE_SUBNET Function

Gets information about a specified recovery service subnet.

Syntax
```

```

Parameters

Parameter Description

`recovery_service_subnet_id`

(required) The recovery service subnet OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request based on the specified ID

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROTECTED_DATABASES Function

Lists the protected databases based on the specified parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment OCID.

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire 'displayname' given.

`id`

(optional) The protected database OCID.

`protection_policy_id`

(optional) The protection policy OCID.

`recovery_service_subnet_id`

(optional) The recovery service subnet OCID.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are: - TIMECREATED - DISPLAYNAME

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROTECTION_POLICIES Function

Gets a list of protection policies based on the specified parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment OCID.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire 'displayname' given.

`protection_policy_id`

(optional) The protection policy OCID.

`owner`

(optional) A filter to return only the policies that match the owner as 'Customer' or 'Oracle'.

Allowed values are: 'oracle', 'customer'

`limit`

(optional) The maximum number of items to return. Specify a value greater than 4.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are: - TIMECREATED - DISPLAYNAME

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECOVERY_SERVICE_SUBNETS Function

Returns a list of Recovery Service Subnets.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment OCID.

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle state. Allowed values are: - CREATING - UPDATING - ACTIVE - DELETING - DELETED - FAILED

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire 'displayname' given.

`id`

(optional) The recovery service subnet OCID.

`vcn_id`

(optional) The OCID of the virtual cloud network (VCN) associated with the recovery service subnet.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are: - TIMECREATED - DISPLAYNAME

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return per page.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return per page.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The compartment OCID.

`work_request_id`

(optional) Unique Oracle-assigned identifier of the work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return per page.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are: - ASC - DESC

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROTECTED_DATABASE Function

Updates the Protected Database

Syntax
```

```

Parameters

Parameter Description

`protected_database_id`

(required) The protected database OCID.

`update_protected_database_details`

(required) Describes the parameters required to update a protected database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROTECTION_POLICY Function

Updates the specified protection policy.

Syntax
```

```

Parameters

Parameter Description

`protection_policy_id`

(required) The protection policy OCID.

`update_protection_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RECOVERY_SERVICE_SUBNET Function

Updates the specified recovery service subnet.

Syntax
```

```

Parameters

Parameter Description

`recovery_service_subnet_id`

(required) The recovery service subnet OCID.

`update_recovery_service_subnet_details`

(required) Describes the parameters required to update a recovery service subnet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://recovery.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Recovery Database Recovery Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-0F177540-B1F8-4256-840B-0FB6E51353E0)
- [CHANGE_PROTECTED_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-E3F7960A-CB6F-4E76-9C71-7BCD1A565A22)
- [CHANGE_PROTECTION_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-EFCB8DA8-77E9-4DD7-9CBF-E4C47F94A57D)
- [CHANGE_RECOVERY_SERVICE_SUBNET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-624A7326-E422-401E-8BCA-E56A84764CCF)
- [CREATE_PROTECTED_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-D6798C83-7D5F-43EB-8C86-FA611C7C979B)
- [CREATE_PROTECTION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-3BC0CFD2-037D-408E-864A-F98DE52DA15B)
- [CREATE_RECOVERY_SERVICE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-161830DF-D532-4C68-9AFF-6253B284033E)
- [DELETE_PROTECTED_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-87A798A3-BD2C-42F3-9A5F-408C5F025694)
- [DELETE_PROTECTION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-97F9B3FE-BF76-45C4-AF6C-13D3E55EC98E)
- [DELETE_RECOVERY_SERVICE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-6AFA382B-23E1-4827-A063-7F0410B6203A)
- [FETCH_PROTECTED_DATABASE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-924BAF5B-711D-4DC8-BA4E-FF78B36DB2C0)
- [GET_PROTECTED_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-DD6D5BE4-215F-4F82-9472-97A2931B64D8)
- [GET_PROTECTION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-D9AD1D25-B2E1-4DB1-8BDE-0C2FE8415107)
- [GET_RECOVERY_SERVICE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-1FE20A1B-82B5-49EF-B7A5-4516EE64B3EC)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-F9527B90-F68A-4812-A87F-6B2532DF53D6)
- [LIST_PROTECTED_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-12678681-2EE4-4B7D-9B21-FFE5F9BD5127)
- [LIST_PROTECTION_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-6E121556-9B3B-45AF-A485-27DA7A909145)
- [LIST_RECOVERY_SERVICE_SUBNETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-4424D072-D61E-47DF-98F9-75833A187F15)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-4BA94383-6781-485C-A9A6-D7C876E6C569)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-8A74C933-50E7-4F70-A5B5-E8552DC9676E)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-BBA2A2D6-9BD5-4D08-ADCC-D334B74D572F)
- [UPDATE_PROTECTED_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-9E78FFE6-EEAB-437B-A8F3-D103A6072EFD)
- [UPDATE_PROTECTION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-BD005138-F29A-4D66-9044-66C71E5A6D77)
- [UPDATE_RECOVERY_SERVICE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_r_database_recovery.html#ADSDK-GUID-4EA29E83-90C2-48F8-8333-08E2DD81B863)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
