# OS Management Hub Managed Instance Group Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#dcoc-content-body)

## OS Management Hub Managed Instance Group Functions

Package: DBMS_CLOUD_OCI_OMH_MANAGED_INSTANCE_GROUP

### ATTACH_MANAGED_INSTANCES_TO_MANAGED_INSTANCE_GROUP Function

Adds managed instances to the specified managed instance group. After the managed instances have been added, then operations can be performed on the managed instance group which will then apply to all managed instances in the group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`attach_managed_instances_to_managed_instance_group_details`

(required) Details for managed instances to attach to the managed instance group.

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

### ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_GROUP Function

Attaches software sources to the specified managed instance group. The software sources must be compatible with the content for the managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`attach_software_sources_to_managed_instance_group_details`

(required) Details for software sources to attach to the managed instance group.

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

### CREATE_MANAGED_INSTANCE_GROUP Function

Creates a new managed instance group.

Syntax
```

```

Parameters

Parameter Description

`create_managed_instance_group_details`

(required) Details for the new managed instance group.

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

### DELETE_MANAGED_INSTANCE_GROUP Function

Deletes a specified managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

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

### DETACH_MANAGED_INSTANCES_FROM_MANAGED_INSTANCE_GROUP Function

Removes a managed instance from the specified managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`detach_managed_instances_from_managed_instance_group_details`

(required) Details for managed instances to detach from the managed instance group.

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

### DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_GROUP Function

Detaches software sources from a group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`detach_software_sources_from_managed_instance_group_details`

(required) Details for software sources to attach to the specified managed instance group.

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

### DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP Function

Disables a module stream on a managed instance group. After the stream is disabled, it is no longer possible to install the profiles that are contained by the stream. All installed profiles must be removed prior to disabling a module stream.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`disable_module_stream_on_managed_instance_group_details`

(required) Details for modules to disable on the managed instance group.

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

### ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP Function

Enables a module stream on a managed instance group. After the stream is enabled, it is possible to install the profiles that are contained by the stream. Enabling a stream that is already enabled will succeed. Attempting to enable a different stream for a module that already has a stream enabled results in an error.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`enable_module_stream_on_managed_instance_group_details`

(required) Details for modules to enable on the managed instance group.

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

### GET_MANAGED_INSTANCE_GROUP Function

Gets information about the specified managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_GROUP Function

Installs a profile for an module stream. The stream must be enabled before a profile can be installed. If a module stream defines multiple profiles, each one can be installed independently.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`install_module_stream_profile_on_managed_instance_group_details`

(required) Details for profiles to install on the managed instance group.

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

### INSTALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP Function

Installs package(s) on each managed instance in a managed instance group. The package must be compatible with the instances in the managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`install_packages_on_managed_instance_group_details`

(required) Details for packages to install on the specified managed instance group.

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

### LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULES Function

Lists available modules that for the specified managed instance group. Filter the list against a variety of criteria including but not limited to its name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`name`

(optional) The resource name.

`name_contains`

(optional) A filter to return resources that may partially match the name given.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for name is ascending.

Allowed values are: 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGES Function

Lists available packages on the specified managed instances group. Filter the list against a variety of criteria including but not limited to the package name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

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

`is_latest`

(optional) A boolean variable that is used to list only the latest versions of packages, module streams, and stream profiles when set to true. All packages, module streams, and stream profiles are returned when set to false.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_SOFTWARE_SOURCES Function

Lists available software sources for a specified managed instance group. Filter the list against a variety of criteria including but not limited to its name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

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

### LIST_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGES Function

Lists installed packages on the specified managed instances group. Filter the list against a variety of criteria including but not limited to the package name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`time_install_date_start`

(optional) The install date after which to list all packages, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`time_install_date_end`

(optional) The install date before which to list all packages, in ISO 8601 format. Example: 2017-07-14T02:40:00.000Z

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeInstalled is descending. Default order for displayName is ascending.

Allowed values are: 'timeInstalled', 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_GROUP_MODULES Function

Retrieve a list of module streams, along with a summary of their status, from a managed instance group. Filters may be applied to select a subset of module streams based on the filter criteria. The 'moduleName' attribute filters against the name of a module. It accepts strings of the format \"&lt;module&gt;\". If this attribute is defined, only streams that belong to the specified module are included in the result set. If it is not defined, the request is not subject to this filter. The \"status\" attribute filters against the state of a module stream. Valid values are \"ENABLED\", \"DISABLED\", and \"ACTIVE\". If the attribute is set to \"ENABLED\", only module streams that are enabled are included in the result set. If the attribute is set to \"DISABLED\", only module streams that are not enabled are included in the result set. If the attribute is set to \"ACTIVE\", only module streams that are active are included in the result set. If the attribute is not defined, the request is not subject to this filter. When sorting by the display name, the result set is sorted first by the module name and then by the stream name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`name`

(optional) The resource name.

`name_contains`

(optional) A filter to return resources that may partially match the name given.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for name is ascending.

Allowed values are: 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_GROUPS Function

Lists managed instance groups that match the specified compartment or managed instance group OCID. Filter the list against a variety of criteria including but not limited to its name, status, architecture, and OS family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`managed_instance_group_id`

(optional) The OCID of the managed instance group for which to list resources.

`software_source_id`

(optional) The OCID for the software source.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

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

(optional) A filter to return only resources their lifecycle state matches the given lifecycle state.

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

### MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_GROUP Function

Perform an operation involving modules, streams, and profiles on a managed instance group. Each operation may enable or disable an arbitrary amount of module streams, and install or remove an arbitrary number of module stream profiles. When the operation is complete, the state of the modules, streams, and profiles on the managed instance group will match the state indicated in the operation. Each module stream specified in the list of module streams to enable will be in the \"ENABLED\" state upon completion of the operation. If there was already a stream of that module enabled, any work required to switch from the current stream to the new stream is performed implicitly. Each module stream specified in the list of module streams to disable will be in the \"DISABLED\" state upon completion of the operation. Any profiles that are installed for the module stream will be removed as part of the operation. Each module stream profile specified in the list of profiles to install will be in the \"INSTALLED\" state upon completion of the operation, indicating that any packages that are part of the profile are installed on the managed instance. If the module stream containing the profile is not enabled, it will be enabled as part of the operation. There is an exception when attempting to install a stream of a profile when another stream of the same module is enabled. It is an error to attempt to install a profile of another module stream, unless enabling the new module stream is explicitly included in this operation. Each module stream profile specified in the list of profiles to remove will be in the \"AVAILABLE\" state upon completion of the operation. The status of packages within the profile after the operation is complete is defined by the package manager on the managed instance group. Operations that contain one or more elements that are not allowed are rejected. The result of this request is a work request object. The returned work request is the parent of a structure of other work requests. Taken as a whole, this structure indicates the entire set of work to be performed to complete the operation. This interface can also be used to perform a dry run of the operation rather than committing it to a managed instance group. If a dry run is requested, the OS Management Hub service will evaluate the operation against the current module, stream, and profile state on the managed instance. It will calculate the impact of the operation on all modules, streams, and profiles on the managed instance, including those that are implicitly impacted by the operation. The work request resulting from a dry run behaves differently than a work request resulting from a committable operation. Dry run work requests are always singletons and never have children. The impact of the operation is returned using the log and error facilities of work requests. The impact of operations that are allowed by the OS Management Hub service are communicated as one or more work request log entries. Operations that are not allowed by the OS Management Hub service are communicated as one or more work request error entries. Each entry, for either logs or errors, contains a structured message containing the results of one or more operations.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`manage_module_streams_on_managed_instance_group_details`

(required) A description of an operation to perform against the modules, streams, and profiles of a managed instance group

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

### REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_GROUP Function

Removes a profile for a module stream that is installed on a managed instance group. If a module stream is provided, rather than a fully qualified profile, all profiles that have been installed for the module stream will be removed.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`remove_module_stream_profile_from_managed_instance_group_details`

(required) Details for profiles to remove from the managed instance group.

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

### REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_GROUP Function

Removes package(s) from each managed instance in a specified managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`remove_packages_from_managed_instance_group_details`

(required) Details for packages to remove from the managed instance group.

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

### UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP Function

Updates all packages on each managed instance in the specified managed instance group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`update_all_packages_on_managed_instance_group_details`

(required) Details for update operation on the managed instance group.

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

### UPDATE_MANAGED_INSTANCE_GROUP Function

Updates the specified managed instance group's name, description, and tags.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) The managed instance group OCID.

`update_managed_instance_group_details`

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

- [OS Management Hub Managed Instance Group Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-9B872A3C-2DF9-49C9-AD50-26BF58A9A5AA)
- [ATTACH_MANAGED_INSTANCES_TO_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-703E0D3C-E8BF-4EA7-906C-3016D0DF2802)
- [ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-7C673824-28C1-4C2F-A226-442867D180D9)
- [CREATE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-3103B40C-7034-4990-B7C1-5202E3F8BD2B)
- [DELETE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-E2B4032C-218B-435A-8ECC-BCE194483FE4)
- [DETACH_MANAGED_INSTANCES_FROM_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-09F03A91-99E3-49B2-BB90-E6F020A87CBD)
- [DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-94F3C4F5-60D7-4D28-AB3F-F8DF42D2C4B0)
- [DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-421CAE1D-1FE8-4AA2-B7C0-B4991F827489)
- [ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-47C59F06-225A-4660-ABEE-16315A4BEB6E)
- [GET_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-39D577E1-AF57-4A6F-9D68-AB753D3AFA45)
- [INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-0CA4B43A-D449-49EA-98B2-FDAEB588E2A2)
- [INSTALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-625D952B-5063-4E31-B5D7-68784C51524B)
- [LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-E35E14DB-EC58-4698-BBDB-94930DAB1CBF)
- [LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-FAC69E3B-E813-4B03-A79D-AC7C2DEFCF33)
- [LIST_MANAGED_INSTANCE_GROUP_AVAILABLE_SOFTWARE_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-7D61D504-567D-4AF6-A9D3-B7B99E6C25DA)
- [LIST_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-ED34198C-9636-4C61-B833-78821E5DEB00)
- [LIST_MANAGED_INSTANCE_GROUP_MODULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-39E8ADAF-572D-41A0-953D-789BD58A30C7)
- [LIST_MANAGED_INSTANCE_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-07EE46A9-025C-4D8E-A8ED-125D61FE8C43)
- [MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-D68BB7F7-A2A7-4503-B456-ADB7266DF478)
- [REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-A0094546-2BD3-49A8-AEA1-18C6A3219042)
- [REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-5C430027-BB30-40BC-BF93-8BD9C9D3CF3E)
- [UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-9EB100F5-333C-48C3-89CE-E7A3B9438E02)
- [UPDATE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance_group.html#ADSDK-GUID-9AB11733-47D6-4E2B-AD47-FCCB9A46321F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
