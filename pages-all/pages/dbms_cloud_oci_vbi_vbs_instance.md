# VBS Instance Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#dcoc-content-body)

## VBS Instance Functions

Package: DBMS_CLOUD_OCI_VBI_VBS_INSTANCE

### CHANGE_VBS_INSTANCE_COMPARTMENT Function

Moves a VbsInstance resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`vbs_instance_id`

(required) unique VbsInstance identifier

`change_vbs_instance_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VBS_INSTANCE Function

Creates a new VbsInstance.

Syntax
```

```

Parameters

Parameter Description

`create_vbs_instance_details`

(required) Details for the new VbsInstance.

`idcs_access_token`

(optional) IDCS personal acceess token identifying IDCS user and stripe for the VBS service

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VBS_INSTANCE Function

Deletes a VbsInstance resource by identifier

Syntax
```

```

Parameters

Parameter Description

`vbs_instance_id`

(required) unique VbsInstance identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VBS_INSTANCE Function

Gets a VbsInstance by identifier

Syntax
```

```

Parameters

Parameter Description

`vbs_instance_id`

(required) unique VbsInstance identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VBS_INSTANCES Function

Returns a list of VbsInstances.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) unique VbsInstance identifier

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

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

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VBS_INSTANCE Function

Updates the VbsInstance

Syntax
```

```

Parameters

Parameter Description

`vbs_instance_id`

(required) unique VbsInstance identifier

`update_vbs_instance_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://vbstudio.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [VBS Instance Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-C5009C8E-A1FE-4638-98C2-26014FE2B173)
- [CHANGE_VBS_INSTANCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-9C395FFA-B02B-481F-8C09-B652AAB31EE5)
- [CREATE_VBS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-325FCC97-A76F-41EC-986F-37AEC3A7D9F7)
- [DELETE_VBS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-D36F985A-3470-44B3-B15B-97BEC81C2373)
- [GET_VBS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-2B0307C1-FA2F-45E3-A55A-28BE0B369A4A)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-9B86542B-2E97-46C5-B3B0-E4A1B75030F4)
- [LIST_VBS_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-1C4BDB85-60D3-4A13-A10D-FE709AA33BE9)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-673D5408-12AA-4DE5-BCCE-37312E1438FF)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-44DC2E72-1D57-407C-8D79-1BDC703310E9)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-C57CF643-7C91-494F-A281-ED5164899EEF)
- [UPDATE_VBS_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_vbi_vbs_instance.html#ADSDK-GUID-1CBE60F2-83FE-4B72-AC3E-792DE9E266DA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
