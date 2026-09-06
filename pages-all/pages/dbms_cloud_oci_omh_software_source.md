# OS Management Hub Software Source Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#dcoc-content-body)

## OS Management Hub Software Source Functions

Package: DBMS_CLOUD_OCI_OMH_SOFTWARE_SOURCE

### CHANGE_AVAILABILITY_OF_SOFTWARE_SOURCES Function

Updates the availability for a list of specified software sources.

Syntax
```

```

Parameters

Parameter Description

`change_availability_of_software_sources_details`

(required) Request body that contains a list of software sources whose availability needs to be updated.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENTITLEMENT Function

Registers the necessary entitlement credentials for OS vendor software sources.

Syntax
```

```

Parameters

Parameter Description

`create_entitlement_details`

(required) Details for creating entitlements.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SOFTWARE_SOURCE Function

Creates a new versioned or custom software source.

Syntax
```

```

Parameters

Parameter Description

`create_software_source_details`

(required) Details for the new software source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SOFTWARE_SOURCE Function

Deletes the specified software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ERRATUM Function

Gets information about the specified erratum by its advisory name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the resources to list. This parameter is required.

`name`

(required) The erratum name (e.g. ELSA-2023-34678).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODULE_STREAM Function

Gets information about the specified module stream in a software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`module_name`

(required) The name of the module.

`stream_name`

(required) The name of the stream of the containing module.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODULE_STREAM_PROFILE Function

Gets information about the specified module stream profile in a software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`profile_name`

(required) The name of the profile of the containing module stream.

`module_name`

(required) The name of a module.

`stream_name`

(required) The name of the stream of the containing module.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PACKAGE_GROUP Function

Gets information about the specified package group from a software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`package_group_id`

(required) The unique package group identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SOFTWARE_PACKAGE Function

Gets information about the specified software package.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`software_package_name`

(required) The name of the software package.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SOFTWARE_SOURCE Function

Gets information about the specified software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENTITLEMENTS Function

Lists entitlements in the specified tenancy OCID. Filter the list against a variety of criteria including but not limited to its CSI, and vendor name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the resources to list. This parameter is required.

`csi`

(optional) A filter to return entitlements that match the given CSI.

`vendor_name`

(optional) A filter to return only profiles that match the given vendorName.

Allowed values are: 'ORACLE'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort entitlements by. Only one sort order may be provided.

Allowed values are: 'csi', 'vendorName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ERRATA Function

Lists all of the currently available errata. Filter the list against a variety of criteria including but not limited to its name, classification type, advisory severity, and OS family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the resources to list. This parameter is required.

`name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

`name_contains`

(optional) A filter to return resources that may partially match the erratum name given.

`classification_type`

(optional) A filter to return only packages that match the given update classification type.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`os_family`

(optional) A filter to return only profiles that match the given osFamily.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`advisory_severity`

(optional) The advisory severity.

Allowed values are: 'LOW', 'MODERATE', 'IMPORTANT', 'CRITICAL'

`time_issue_date_start`

(optional) The issue date after which to list all errata, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`time_issue_date_end`

(optional) The issue date before which to list all errata, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort errata by. Only one sort order may be provided. Default order for timeIssued is descending. Default order for name is ascending. If no value is specified timeIssued is default.

Allowed values are: 'timeIssued', 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAM_PROFILES Function

Lists module stream profiles from the specified software source OCID. Filter the list against a variety of criteria including but not limited to its module name, stream name, and (profile) name.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`name`

(optional) The name of the entity to be queried.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for moduleName is ascending.

Allowed values are: 'moduleName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAMS Function

Lists module streams from the specified software source OCID. Filter the list against a variety of criteria including but not limited to its module name and (stream) name.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`name`

(optional) The name of the entity to be queried.

`is_latest`

(optional) A boolean variable that is used to list only the latest versions of packages, module streams, and stream profiles when set to true. All packages, module streams, and stream profiles are returned when set to false.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for moduleName is ascending.

Allowed values are: 'moduleName'

`module_name_contains`

(optional) A filter to return resources that may partially match the module name given.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PACKAGE_GROUPS Function

Lists package groups that associate with the specified software source OCID. Filter the list against a variety of criteria including but not limited to its name, and package group type.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`name`

(optional) The name of the entity to be queried.

`name_contains`

(optional) A filter to return resources that may partially match the name given.

`group_type`

(optional) A filter to return only package groups of the specified type.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

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

### LIST_SOFTWARE_PACKAGES Function

Lists software packages in the specified software source. Filter the list against a variety of criteria including but not limited to its name.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`is_latest`

(optional) A boolean variable that is used to list only the latest versions of packages, module streams, and stream profiles when set to true. All packages, module streams, and stream profiles are returned when set to false.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

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

### LIST_SOFTWARE_SOURCE_VENDORS Function

Lists available software source vendors. Filter the list against a variety of criteria including but not limited to its name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the resources to list. This parameter is required.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort software source vendors by. Only one sort order may be provided. Default order for name is ascending.

Allowed values are: 'name'

`name`

(optional) The name of the entity to be queried.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SOFTWARE_SOURCES Function

Lists software sources that match the specified tenancy or software source OCID. Filter the list against a variety of criteria including but not limited to its name, status, architecture, and OS family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`software_source_id`

(optional) The OCID for the software source.

`software_source_type`

(optional) The type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

`vendor_name`

(optional) A filter to return only profiles that match the given vendorName.

Allowed values are: 'ORACLE'

`os_family`

(optional) A filter to return only instances whose OS family type matches the given OS family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) A filter to return only instances whose architecture type matches the given architecture.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`availability`

(optional) The availabilities of the software source for a tenant.

Allowed values are: 'AVAILABLE', 'SELECTED', 'RESTRICTED'

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`display_name_not_equal_to`

(optional) A multi filter to return resources that do not contains the given display names.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleStates.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_SOFTWARE_SOURCE_MODULE_STREAMS Function

Lists modules from a list of software sources. Filter the list against a variety of criteria including the module name.

Syntax
```

```

Parameters

Parameter Description

`search_software_source_module_streams_details`

(required) Request body that takes a list of software sources and any search filters.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_SOFTWARE_SOURCE_MODULES Function

Lists modules from a list of software sources. Filter the list against a variety of criteria including the (module) name.

Syntax
```

```

Parameters

Parameter Description

`search_software_source_modules_details`

(required) Request body that takes a list of software sources and any search filters.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_SOFTWARE_SOURCE_PACKAGE_GROUPS Function

Searches the package groups from the specified list of software sources. Filter the list against a variety of criteria including but not limited to its name, and group type.

Syntax
```

```

Parameters

Parameter Description

`search_software_source_package_groups_details`

(required) Request body that takes in a list of software sources and other search parameters.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SOFTWARE_SOURCE Function

Updates the specified software source's details, including but not limited to name, description, and tags.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The software source OCID.

`update_software_source_details`

(required) The information to be updated.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Hub Software Source Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-22C7ECB1-89F0-45DA-B5A2-15023A35E847)
- [CHANGE_AVAILABILITY_OF_SOFTWARE_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-B0C915D8-59CA-4F11-B9A5-76C4F1B7474C)
- [CREATE_ENTITLEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-6DCEEC6B-A56D-4DE3-A53F-59259CD1B8FE)
- [CREATE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-CE5C65E8-6CA2-4021-8880-1AEDA4EBF44A)
- [DELETE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-E203A563-3FC3-4BE7-BD6E-33469C9AD682)
- [GET_ERRATUM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-C0B3715A-C423-478E-9B58-13B5EEE8B0B8)
- [GET_MODULE_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-F52A4ED4-2F5D-4ECE-BF36-4E6BD59BB1F0)
- [GET_MODULE_STREAM_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-52150874-380A-47C2-B579-087F67C4BC09)
- [GET_PACKAGE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-EBD713BB-1C79-49E6-8801-50ABF0F1E036)
- [GET_SOFTWARE_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-7999B9FE-BC76-4AC7-B26B-84FCC7F1B6EC)
- [GET_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-AA81DA22-F1E7-4614-BFF4-DAA3A86D7FAD)
- [LIST_ENTITLEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-C61A2025-39C9-421C-B8D3-9D2202E44A77)
- [LIST_ERRATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-1A0B3969-142A-4D00-BB37-50660F15F194)
- [LIST_MODULE_STREAM_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-6C0C063C-C7AE-4FD6-A7BE-F191F3143162)
- [LIST_MODULE_STREAMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-99CA60EE-4573-4E14-AA3D-87BC7A183297)
- [LIST_PACKAGE_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-0A1DE3B9-5382-4F67-939C-CE86E5220FBF)
- [LIST_SOFTWARE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-1AB931A7-6CF0-4A82-8DB5-47D2925B2335)
- [LIST_SOFTWARE_SOURCE_VENDORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-D64FB132-4F25-4AB5-A869-3C8E0A3E8ED6)
- [LIST_SOFTWARE_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-CF92634B-288B-489F-80A4-2CD744E4C3D0)
- [SEARCH_SOFTWARE_SOURCE_MODULE_STREAMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-277520B6-2A33-446D-BC03-495B80611279)
- [SEARCH_SOFTWARE_SOURCE_MODULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-085BCE97-682A-4A8B-B7FF-733609738794)
- [SEARCH_SOFTWARE_SOURCE_PACKAGE_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-88E532EB-9D62-46C0-9428-F6031E6C1107)
- [UPDATE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_software_source.html#ADSDK-GUID-7079C9BB-D753-4DC4-9ED1-5015618DA0A1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
