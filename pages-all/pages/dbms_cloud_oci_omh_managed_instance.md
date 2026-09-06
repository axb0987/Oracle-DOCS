# OS Management Hub Managed Instance Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#dcoc-content-body)

## OS Management Hub Managed Instance Functions

Package: DBMS_CLOUD_OCI_OMH_MANAGED_INSTANCE

### ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE Function

Adds software sources to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`attach_software_sources_to_managed_instance_details`

(required) Details of software sources to be attached to a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE Function

Removes software sources from a managed instance. Packages will no longer be able to be installed from these software sources.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`detach_software_sources_from_managed_instance_details`

(required) Details of software sources to be detached from a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function

Disables a module stream on a managed instance. After the stream is disabled, it is no longer possible to install the profiles that are contained by the stream. All installed profiles must be removed prior to disabling a module stream.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`disable_module_stream_on_managed_instance_details`

(required) The details of the module stream to be disabled on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function

Enables a module stream on a managed instance. After the stream is enabled, it is possible to install the profiles that are contained by the stream. Enabling a stream that is already enabled will succeed. Attempting to enable a different stream for a module that already has a stream enabled results in an error.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`enable_module_stream_on_managed_instance_details`

(required) The details of the module stream to be enabled on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### GET_MANAGED_INSTANCE Function

Gets information about the specified managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE Function

Installs a profile for an module stream. The stream must be enabled before a profile can be installed. If a module stream defines multiple profiles, each one can be installed independently.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`install_module_stream_profile_on_managed_instance_details`

(required) The details of the module stream profile to be installed on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### INSTALL_PACKAGES_ON_MANAGED_INSTANCE Function

Installs packages on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`install_packages_on_managed_instance_details`

(required) Details about packages to be installed on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### LIST_MANAGED_INSTANCE_AVAILABLE_PACKAGES Function

Returns a list of available packages for a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

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

### LIST_MANAGED_INSTANCE_AVAILABLE_SOFTWARE_SOURCES Function

Returns a list of available software sources for a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

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

### LIST_MANAGED_INSTANCE_ERRATA Function

Returns a list of applicable errata on the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`advisory_type`

(optional) A filter to return only errata that match the given advisory types.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT'

`name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

`name_contains`

(optional) A filter to return resources that may partially match the erratum name given.

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

### LIST_MANAGED_INSTANCE_INSTALLED_PACKAGES Function

Lists the packages that are installed on the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

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

### LIST_MANAGED_INSTANCE_MODULES Function

Retrieve a list of modules, along with streams of the modules, from a managed instance. Filters may be applied to select a subset of modules based on the filter criteria. The 'name' attribute filters against the name of a module. It accepts strings of the format \"&lt;string&gt;\". The 'nameContains' attribute filters against the name of a module based on partial match. It accepts strings of the format \"&lt;string&gt;\". If this attribute is defined, only matching modules are included in the result set. If it is not defined, the request is not subject to this filter.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

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

### LIST_MANAGED_INSTANCE_UPDATABLE_PACKAGES Function

Returns a list of updatable packages for a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`classification_type`

(optional) A filter to return only packages that match the given update classification type.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`advisory_name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

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

### LIST_MANAGED_INSTANCES Function

Lists managed instances that match the specified compartment or managed instance OCID. Filter the list against a variety of criteria including but not limited to its name, status, architecture, and OS version.

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

`managed_instance_id`

(optional) The OCID of the managed instance for which to list resources.

`status`

(optional) A filter to return only instances whose managed instance status matches the given status.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING', 'REGISTRATION_ERROR'

`arch_type`

(optional) A filter to return only instances whose architecture type matches the given architecture.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(optional) A filter to return only instances whose OS family type matches the given OS family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`is_management_station`

(optional) A filter to return only managed instances acting as management stations.

`l_group`

(optional) A filter to return only managed instances that are attached to the specified group.

`group_not_equal_to`

(optional) A filter to return only managed instances that are NOT attached to the specified group.

`lifecycle_stage`

(optional) A filter to return only managed instances that are associated with the specified lifecycle environment.

`lifecycle_stage_not_equal_to`

(optional) A filter to return only managed instances that are NOT associated with the specified lifecycle environment.

`is_attached_to_group_or_lifecycle_stage`

(optional) A filter to return only managed instances that are attached to the specified group or lifecycle environment.

`software_source_id`

(optional) The OCID for the software source.

`advisory_name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

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

### MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE Function

Perform an operation involving modules, streams, and profiles on a managed instance. Each operation may enable or disable an arbitrary amount of module streams, and install or remove an arbitrary number of module stream profiles. When the operation is complete, the state of the modules, streams, and profiles on the managed instance will match the state indicated in the operation. Each module stream specified in the list of module streams to enable will be in the \"ENABLED\" state upon completion of the operation. If there was already a stream of that module enabled, any work required to switch from the current stream to the new stream is performed implicitly. Each module stream specified in the list of module streams to disable will be in the \"DISABLED\" state upon completion of the operation. Any profiles that are installed for the module stream will be removed as part of the operation. Each module stream profile specified in the list of profiles to install will be in the \"INSTALLED\" state upon completion of the operation, indicating that any packages that are part of the profile are installed on the managed instance. If the module stream containing the profile is not enabled, it will be enabled as part of the operation. There is an exception when attempting to install a stream of a profile when another stream of the same module is enabled. It is an error to attempt to install a profile of another module stream, unless enabling the new module stream is explicitly included in this operation. Each module stream profile specified in the list of profiles to remove will be in the \"AVAILABLE\" state upon completion of the operation. The status of packages within the profile after the operation is complete is defined by the package manager on the managed instance. Operations that contain one or more elements that are not allowed are rejected. The result of this request is a work request object. The returned work request is the parent of a structure of other WorkRequests. Taken as a whole, this structure indicates the entire set of work to be performed to complete the operation. This interface can also be used to perform a dry run of the operation rather than committing it to a managed instance. If a dry run is requested, the OS Management Hub service will evaluate the operation against the current module, stream, and profile state on the managed instance. It will calculate the impact of the operation on all modules, streams, and profiles on the managed instance, including those that are implicitly impacted by the operation. The WorkRequest resulting from a dry run behaves differently than a WorkRequest resulting from a committable operation. Dry run WorkRequests are always singletons and never have children. The impact of the operation is returned using the log and error facilities of work requests. The impact of operations that are allowed by the OS Management Hub service are communicated as one or more work request log entries. Operations that are not allowed by the OS Management Hub service are communicated as one or more work request error entries. Each entry, for either logs or errors, contains a structured message containing the results of one or more operations.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`manage_module_streams_on_managed_instance_details`

(required) A description of an operation to perform against the modules, streams, and profiles of a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### REFRESH_SOFTWARE_ON_MANAGED_INSTANCE Function

Refresh all installed and updatable software information on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE Function

Removes a profile for a module stream that is installed on a managed instance. If a module stream is provided, rather than a fully qualified profile, all profiles that have been installed for the module stream will be removed.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`remove_module_stream_profile_from_managed_instance_details`

(required) The details of the module stream profile to be removed from a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### REMOVE_PACKAGES_FROM_MANAGED_INSTANCE Function

Removes an installed package from a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`remove_packages_from_managed_instance_details`

(required) Details about packages to be removed on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### SWITCH_MODULE_STREAM_ON_MANAGED_INSTANCE Function

Enables a new stream for a module that already has a stream enabled. If any profiles or packages from the original module are installed, switching to a new stream will remove the existing packages and install their counterparts in the new stream.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`switch_module_stream_on_managed_instance_details`

(required) The details of the module stream to be switched on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCES_IN_COMPARTMENT Function

Install all of the available package updates for all of the managed instances in a compartment.

Syntax
```

```

Parameters

Parameter Description

`update_all_packages_on_managed_instances_in_compartment_details`

(required) The details about package types are to be updated on all managed instances in a compartment.

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

### UPDATE_MANAGED_INSTANCE Function

Updates the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`update_managed_instance_details`

(required) Details about a managed instance to be updated.

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

### UPDATE_PACKAGES_ON_MANAGED_INSTANCE Function

Updates a package on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`update_packages_on_managed_instance_details`

(required) Details about packages to be updated on a managed instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

- [OS Management Hub Managed Instance Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-D727C047-197F-4999-BDF4-461A8B8DED32)
- [ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-F9B2DAAD-1EA8-494B-AC9E-DBA25E2386D6)
- [DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-D34EABF5-3DB5-4CCE-A7F4-AC524FD8C022)
- [DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-C0E54F5B-E1E0-4573-9951-341E9395B8D1)
- [ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-C9847B3C-B20D-44CE-A043-4F7FF8B77381)
- [GET_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-7D29704E-CC82-44A4-97B9-89039282BB9A)
- [INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-AB305F2A-A7DA-45E3-8728-26A2B2320BF0)
- [INSTALL_PACKAGES_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-F5718CD3-10CB-4465-B482-ABDBA55CC1A5)
- [LIST_MANAGED_INSTANCE_AVAILABLE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-CB516F90-073C-42CA-B90C-DF63AC9F823C)
- [LIST_MANAGED_INSTANCE_AVAILABLE_SOFTWARE_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-6587772E-D398-4E7B-A3C1-0C69EC5D7423)
- [LIST_MANAGED_INSTANCE_ERRATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-81DE87E7-0CDD-4708-81D8-28F3F172DC7A)
- [LIST_MANAGED_INSTANCE_INSTALLED_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-4FCDDD18-FA1C-494F-870D-FA21136DE63D)
- [LIST_MANAGED_INSTANCE_MODULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-5E30C355-A577-4630-8586-5DBE463ECDE0)
- [LIST_MANAGED_INSTANCE_UPDATABLE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-752FA2FB-66C8-43A4-BF38-F74DDEAD5B19)
- [LIST_MANAGED_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-A20C3A1C-7D91-44F5-8D54-0E4FAFAAF6B0)
- [MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-CB539F7A-3351-4378-B796-F85A2E01D9B9)
- [REFRESH_SOFTWARE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-EBF78C30-D0E3-4378-8435-102AB4A37108)
- [REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-151B9959-406A-4AD1-A469-A237A2E3EDE0)
- [REMOVE_PACKAGES_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-E8E99078-73A7-4ECC-B4B8-FF53D84CDCBD)
- [SWITCH_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-CC8C7460-ACCC-4F85-9272-A21B38ED959E)
- [UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCES_IN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-7F6CBECF-3E87-4651-81DB-A29E86B1C405)
- [UPDATE_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-6DC9F1E5-375C-4007-80E0-7512B393D737)
- [UPDATE_PACKAGES_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_managed_instance.html#ADSDK-GUID-B1C8689E-A343-4B75-8B15-29C17061F89B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
