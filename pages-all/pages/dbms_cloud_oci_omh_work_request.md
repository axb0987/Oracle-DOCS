# OS Management Hub Work Request Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#dcoc-content-body)

## OS Management Hub Work Request Functions

Package: DBMS_CLOUD_OCI_OMH_WORK_REQUEST

### GET_WORK_REQUEST Function

Gets information about the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Gets the errors for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Gets the logs for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists work requests that match the specified compartment or work request OCID. Filter the list against a variety of criteria including but not limited to its name, status, and operation type.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`work_request_id`

(optional) The OCID of the work request.

`status`

(optional) A filter to return work requests that match the given status.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The OCID of the resource affected by the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName'

`initiator_id`

(optional) The OCID of the schedule job that initiated the work request.

`parent_id`

(optional) The OCID of the parent work request.

`parent_resources_not_equal_to`

(optional) A filter to return the resources whose parent resources are not the same as the given resource OCID(s).

`operation_type`

(optional) The asynchronous operation tracked by this work request. The filter returns only resources that match the given OperationType.

Allowed values are: 'INSTALL_PACKAGES', 'REMOVE_PACKAGES', 'UPDATE_PACKAGES', 'UPDATE_ALL_PACKAGES', 'UPDATE_SECURITY', 'UPDATE_BUGFIX', 'UPDATE_ENHANCEMENT', 'UPDATE_OTHER', 'UPDATE_KSPLICE_KERNEL', 'UPDATE_KSPLICE_USERSPACE', 'ENABLE_MODULE_STREAMS', 'DISABLE_MODULE_STREAMS', 'SWITCH_MODULE_STREAM', 'INSTALL_MODULE_PROFILES', 'REMOVE_MODULE_PROFILES', 'SET_SOFTWARE_SOURCES', 'LIST_PACKAGES', 'SET_MANAGEMENT_STATION_CONFIG', 'SYNC_MANAGEMENT_STATION_MIRROR', 'UPDATE_MANAGEMENT_STATION_SOFTWARE', 'UPDATE', 'MODULE_ACTIONS', 'LIFECYCLE_PROMOTION', 'CREATE_SOFTWARE_SOURCE', 'UPDATE_SOFTWARE_SOURCE'

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Hub Work Request Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#ADSDK-GUID-F827E453-96FC-4F8A-857B-3A5F7051CC86)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#ADSDK-GUID-6F59F1F4-3955-4E47-AA66-B1D6025B4918)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#ADSDK-GUID-6B5E7756-FB23-4FFF-9B9A-8A874BBE87B3)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#ADSDK-GUID-2F690F9C-A5AA-4ECF-B36E-B17CEE1AE89E)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_work_request.html#ADSDK-GUID-33CDB667-09F3-473A-9898-9A32FC38F2E5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
