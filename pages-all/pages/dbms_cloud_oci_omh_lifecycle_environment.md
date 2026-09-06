# OS Management Hub Lifecycle Environment Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#dcoc-content-body)

## OS Management Hub Lifecycle Environment Functions

Package: DBMS_CLOUD_OCI_OMH_LIFECYCLE_ENVIRONMENT

### ATTACH_MANAGED_INSTANCES_TO_LIFECYCLE_STAGE Function

Attach(add) managed instances to a lifecycle stage. Once added operations can be applied to all managed instances in the lifecycle stage.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage.

`attach_managed_instances_to_lifecycle_stage_details`

(required) Details for managed instances to attach to the lifecycle stage.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LIFECYCLE_ENVIRONMENT Function

Creates a new lifecycle environment.

Syntax
```

```

Parameters

Parameter Description

`create_lifecycle_environment_details`

(required) Details for the new lifecycle environment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LIFECYCLE_ENVIRONMENT Function

Deletes a lifecycle environment.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_environment_id`

(required) The OCID of the lifecycle environment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_MANAGED_INSTANCES_FROM_LIFECYCLE_STAGE Function

Detach(remove) managed instance from a lifecycle stage.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage.

`detach_managed_instances_from_lifecycle_stage_details`

(required) Details for managed instances to detach from the lifecycle stage.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LIFECYCLE_ENVIRONMENT Function

Gets information about the specified lifecycle environment.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_environment_id`

(required) The OCID of the lifecycle environment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LIFECYCLE_STAGE Function

Gets information about the specified lifecycle stage.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIFECYCLE_ENVIRONMENTS Function

Lists lifecycle environments that match the specified compartment or lifecycle environment OCID. Filter the list against a variety of criteria including but not limited to its name, status, architecture, and OS family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`lifecycle_environment_id`

(optional) The OCID of the lifecycle environment.

`arch_type`

(optional) A filter to return only profiles that match the given archType.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(optional) A filter to return only profiles that match the given osFamily.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`lifecycle_state`

(optional) A filter to return only the lifecycle environments that match the display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIFECYCLE_STAGE_INSTALLED_PACKAGES Function

Lists installed packages on managed instances in a specified lifecycle stage. Filter the list against a variety of criteria including but not limited to the package name.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`lifecycle_state`

(optional) A filter to return only lifecycle stage whose lifecycle state matches the given lifecycle state.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIFECYCLE_STAGES Function

Lists lifecycle stages that match the specified compartment or lifecycle stage OCID. Filter the list against a variety of criteria including but not limited to its name, status, architecture, and OS family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`lifecycle_stage_id`

(optional) The OCID of the lifecycle stage.

`software_source_id`

(optional) The OCID for the software source.

`arch_type`

(optional) A filter to return only profiles that match the given archType.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(optional) A filter to return only profiles that match the given osFamily.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`lifecycle_state`

(optional) A filter to return only lifecycle stage whose lifecycle state matches the given lifecycle state.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PROMOTE_SOFTWARE_SOURCE_TO_LIFECYCLE_STAGE Function

Updates the versioned custom software source content for specified lifecycle stage.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage.

`promote_software_source_to_lifecycle_stage_details`

(required) Details for the software source promotion job.

`software_source_id`

(optional) The OCID for the software source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LIFECYCLE_ENVIRONMENT Function

Updates the specified lifecycle environment's name, description, stages, or tags.

Syntax
```

```

Parameters

Parameter Description

`lifecycle_environment_id`

(required) The OCID of the lifecycle environment.

`update_lifecycle_environment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Hub Lifecycle Environment Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-A3250EE0-E604-4836-B095-85B95AE6CE08)
- [ATTACH_MANAGED_INSTANCES_TO_LIFECYCLE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-FEF3C654-F540-4B90-9E96-DE5F721617C4)
- [CREATE_LIFECYCLE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-5F004D24-D57A-450E-93FF-51DDB49C0E7A)
- [DELETE_LIFECYCLE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-03B90E78-D3C6-4C82-AB47-AD303B1E2826)
- [DETACH_MANAGED_INSTANCES_FROM_LIFECYCLE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-3538AB71-2A23-4184-91B6-874426301C2C)
- [GET_LIFECYCLE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-E35D4C4B-C98A-402E-B10F-898377549B76)
- [GET_LIFECYCLE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-2BF92F01-CFDE-4B86-9B9D-992EA567A218)
- [LIST_LIFECYCLE_ENVIRONMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-1B466EF0-52A0-4C82-A938-B0A89B6D0BDC)
- [LIST_LIFECYCLE_STAGE_INSTALLED_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-5A44C7F7-E65C-4B8C-B362-35C42EC06FFD)
- [LIST_LIFECYCLE_STAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-57F62911-CC52-4300-98E4-C4D9DA691826)
- [PROMOTE_SOFTWARE_SOURCE_TO_LIFECYCLE_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-41D7F456-4AB5-4813-A74A-D5A2C573442E)
- [UPDATE_LIFECYCLE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_lifecycle_environment.html#ADSDK-GUID-F3D37565-BC76-4733-AADE-596F611077F9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
