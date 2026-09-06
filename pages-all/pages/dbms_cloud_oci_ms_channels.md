# MySQL Channels Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#dcoc-content-body)

## MySQL Channels Functions

Package: DBMS_CLOUD_OCI_MS_CHANNELS

### CREATE_CHANNEL Function

Creates a Channel to establish replication from a source to a target.

Syntax
```

```

Parameters

Parameter Description

`create_channel_details`

(required) The parameters of the request to create the Channel.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CHANNEL Function

Deletes the specified Channel.

Syntax
```

```

Parameters

Parameter Description

`channel_id`

(required) The Channel[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CHANNEL Function

Gets the full details of the specified Channel, including the user-specified configuration parameters (passwords are omitted), as well as information about the state of the Channel, its sources and targets.

Syntax
```

```

Parameters

Parameter Description

`channel_id`

(required) The Channel[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`if_none_match`

(optional) For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CHANNELS Function

Lists all the Channels that match the specified filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`db_system_id`

(optional) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`channel_id`

(optional) The OCID of the Channel.

`display_name`

(optional) A filter to return only the resource matching the given display name exactly.

`lifecycle_state`

(optional) The LifecycleState of the Channel.

`is_enabled`

(optional) If true, returns only Channels that are enabled. If false, returns only Channels that are disabled.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.

Allowed values are: 'displayName', 'timeCreated'

`sort_order`

(optional) The sort order to use (ASC or DESC).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`page`

(optional) The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESET_CHANNEL Function

Resets the specified Channel by purging its cached information, leaving the Channel as if it had just been created. This operation is only accepted in Inactive Channels.

Syntax
```

```

Parameters

Parameter Description

`channel_id`

(required) The Channel[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESUME_CHANNEL Function

Resumes an enabled Channel that has become Inactive due to an error. The resume operation requires that the error that cause the Channel to become Inactive has already been fixed, otherwise the operation may fail.

Syntax
```

```

Parameters

Parameter Description

`channel_id`

(required) The Channel[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CHANNEL Function

Updates the properties of the specified Channel. If the Channel is Active the Update operation will asynchronously apply the new configuration parameters to the Channel and the Channel may become temporarily unavailable. Otherwise, the new configuration will be applied the next time the Channel becomes Active.

Syntax
```

```

Parameters

Parameter Description

`channel_id`

(required) The Channel[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_channel_details`

(required) The parameters of the request to update the Channel.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [MySQL Channels Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-BA785433-80E3-492C-B337-EA02400F1FBE)
- [CREATE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-6286D5B1-3B7C-47A7-AD6B-0A222309262D)
- [DELETE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-651B4ACE-8AED-4A1F-81E7-7626FBD137A2)
- [GET_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-559B52F6-EFEC-4A62-82CF-D165DA6AB2AB)
- [LIST_CHANNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-D9BBAF57-E4FF-40EC-ACD8-71B03CDC3A5C)
- [RESET_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-D1109030-D16F-4CF2-A6F3-F546B00B3714)
- [RESUME_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-AD972BB3-D856-412B-8818-8C51DBA47A76)
- [UPDATE_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_channels.html#ADSDK-GUID-7222022C-EE68-4B54-BDB9-73F91C8707D2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
