# Cloud Bridge Discovery Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#dcoc-content-body)

## Cloud Bridge Discovery Functions

Package: DBMS_CLOUD_OCI_CB_DISCOVERY

### CHANGE_ASSET_SOURCE_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

`change_asset_source_compartment_details`

(required) Details for the compartment move.

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

### CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT Function

Moves the specified discovery schedule into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`discovery_schedule_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`change_discovery_schedule_compartment_details`

(required) Information about the compartment in to which the discovery schedule should be moved.

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

### CREATE_ASSET_SOURCE Function

Creates an asset source.

Syntax
```

```

Parameters

Parameter Description

`create_asset_source_details`

(required) Details for the new asset source.

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

### CREATE_DISCOVERY_SCHEDULE Function

Creates the discovery schedule.

Syntax
```

```

Parameters

Parameter Description

`create_discovery_schedule_details`

(required) Information about the discovery schedule being created.

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

### DELETE_ASSET_SOURCE Function

Deletes the asset source by ID.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

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

### DELETE_DISCOVERY_SCHEDULE Function

Deletes the specified discovery schedule.

Syntax
```

```

Parameters

Parameter Description

`discovery_schedule_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

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

### GET_ASSET_SOURCE Function

Gets the asset source by ID.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DISCOVERY_SCHEDULE Function

Reads information about the specified discovery schedule.

Syntax
```

```

Parameters

Parameter Description

`discovery_schedule_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASSET_SOURCE_CONNECTIONS Function

Gets known connections to the asset source by the asset source ID.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASSET_SOURCES Function

Returns a list of asset sources.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`asset_source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending order.

Allowed values are: 'timeCreated', 'displayName'

`lifecycle_state`

(optional) The current state of the asset source.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING', 'NEEDS_ATTENTION'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_SCHEDULES Function

Lists discovery schedules.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`lifecycle_state`

(optional) The current state of the discovery schedule.

Allowed values are: 'ACTIVE', 'DELETED'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending order.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_ASSET_SOURCE Function

Initiates the process of asset metadata synchronization with the related asset source.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

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

### UPDATE_ASSET_SOURCE Function

Updates the asset source.

Syntax
```

```

Parameters

Parameter Description

`asset_source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asset source.

`update_asset_source_details`

(required) Asset source information to be updated.

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

### UPDATE_DISCOVERY_SCHEDULE Function

Updates the specified discovery schedule.

Syntax
```

```

Parameters

Parameter Description

`update_discovery_schedule_details`

(required) Discovery schedule information to be updated.

`discovery_schedule_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

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

- [Cloud Bridge Discovery Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-300E716D-5F17-47AE-AC3A-D03629C3F30A)
- [CHANGE_ASSET_SOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-CC4B1DB1-8B5E-4337-8D76-956F0FE9777E)
- [CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-5D67D91A-C09F-439E-A137-E89CC90E7543)
- [CREATE_ASSET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-B4270E0D-184D-4984-94ED-E8E2B3C44610)
- [CREATE_DISCOVERY_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-CED725B8-F730-4BAC-9689-C8DF9834ACE5)
- [DELETE_ASSET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-9A51FF23-89C0-4EC2-A78A-6A191D41FBCA)
- [DELETE_DISCOVERY_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-D35F6E60-A49C-49D4-BDA9-8117D8977B52)
- [GET_ASSET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-462FF04C-EC34-43B3-A0EF-4C603CF61959)
- [GET_DISCOVERY_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-F6A42419-40C9-440E-B194-72E6396D19A0)
- [LIST_ASSET_SOURCE_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-92638AD1-F913-4448-8EDB-23CF25FD1350)
- [LIST_ASSET_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-7E0C5A5B-96D2-46FB-9858-FBA94D16AF96)
- [LIST_DISCOVERY_SCHEDULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-B3FAB8AB-F6FE-494A-80F4-A8AE1A47DE6C)
- [REFRESH_ASSET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-7B5FF1D4-583B-4CFB-A4A4-1BDFFE81D561)
- [UPDATE_ASSET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-CA790E21-1A07-4962-829B-33726A3D1A6B)
- [UPDATE_DISCOVERY_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_discovery.html#ADSDK-GUID-3964743F-84A6-4CC1-B377-08EAD695A69C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
