# OS Management Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#dcoc-content-body)

## OS Management Functions

Package: DBMS_CLOUD_OCI_OM_OS_MANAGEMENT

### ADD_PACKAGES_TO_SOFTWARE_SOURCE Function

Adds a given list of Software Packages to a specific Software Source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`add_packages_to_software_source_details`

(required) A list of package identifiers

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_CHILD_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE Function

Adds a child software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`attach_child_software_source_to_managed_instance_details`

(required) Details for attaching a Software Source to a Managed Instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_MANAGED_INSTANCE_TO_MANAGED_INSTANCE_GROUP Function

Adds a Managed Instance to a Managed Instance Group. After the Managed Instance has been added, then operations can be performed on the Managed Instance Group which will then apply to all Managed Instances in the group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`managed_instance_id`

(required) OCID for the managed instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_PARENT_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE Function

Adds a parent software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance. Software sources that have this software source as a parent will be able to be added to this managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`attach_parent_software_source_to_managed_instance_details`

(required) Details for attaching a Software Source to a Managed Instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MANAGED_INSTANCE_GROUP_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`change_managed_instance_group_compartment_details`

(required) OCID for the compartment to which the resource will be moved.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SCHEDULED_JOB_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`change_scheduled_job_compartment_details`

(required) OCID for the compartment to which the resource will be moved.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SOFTWARE_SOURCE_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`change_software_source_compartment_details`

(required) OCID for the compartment to which the resource will be moved.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MANAGED_INSTANCE_GROUP Function

Creates a new Managed Instance Group on the management system. This will not contain any managed instances after it is first created, and they must be added later.

Syntax
```

```

Parameters

Parameter Description

`create_managed_instance_group_details`

(required) Details about a Managed Instance Group to create

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SCHEDULED_JOB Function

Creates a new Scheduled Job to perform a specific package operation on a set of managed instances or managed instance groups. Can be created as a one-time execution in the future, or as a recurring execution that repeats on a defined interval.

Syntax
```

```

Parameters

Parameter Description

`create_scheduled_job_details`

(required) Details about a Scheduled Job to create

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SOFTWARE_SOURCE Function

Creates a new custom Software Source on the management system. This will not contain any packages after it is first created, and they must be added later.

Syntax
```

```

Parameters

Parameter Description

`create_software_source_details`

(required) Details about a Sofware Source to create

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGED_INSTANCE_GROUP Function

Deletes a Managed Instance Group from the management system

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SCHEDULED_JOB Function

Cancels an existing Scheduled Job on the management system

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SOFTWARE_SOURCE Function

Deletes a custom Software Source on the management system

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_CHILD_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE Function

Removes a child software source from a managed instance. Packages will no longer be able to be installed from these software sources.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`detach_child_software_source_from_managed_instance_details`

(required) Details for detaching a Software Source from a Managed Instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_MANAGED_INSTANCE_FROM_MANAGED_INSTANCE_GROUP Function

Removes a Managed Instance from a Managed Instance Group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`managed_instance_id`

(required) OCID for the managed instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_PARENT_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE Function

Removes a software source from a managed instance. All child software sources will also be removed from the managed instance. Packages will no longer be able to be installed from these software sources.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`detach_parent_software_source_from_managed_instance_details`

(required) Details for detaching a Software Source from a Managed Instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) OCID for the managed instance

`module_name`

(required) The name of a module.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) OCID for the managed instance

`module_name`

(required) The name of a module.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ERRATUM Function

Returns a specific erratum.

Syntax
```

```

Parameters

Parameter Description

`erratum_id`

(required) The OCID of the erratum.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_INSTANCE Function

Returns a specific Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_INSTANCE_GROUP Function

Returns a specific Managed Instance Group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODULE_STREAM Function

Retrieve a detailed description of a module stream from a software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`module_name`

(required) The name of the module

`stream_name`

(required) The name of the stream of the containing module

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODULE_STREAM_PROFILE Function

Retrieve a detailed description of a module stream profile from a software source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`module_name`

(required) The name of the module

`stream_name`

(required) The name of the stream of the containing module

`profile_name`

(required) The name of the profile of the containing module stream

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEDULED_JOB Function

Gets the detailed information for the Scheduled Job with the given ID.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SOFTWARE_PACKAGE Function

Returns a specific Software Package.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`software_package_name`

(required) The id of the software package.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SOFTWARE_SOURCE Function

Returns a specific Software Source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WINDOWS_UPDATE Function

Returns a Windows Update object.

Syntax
```

```

Parameters

Parameter Description

`windows_update`

(required) The Windows Update

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the detailed information for the work request with the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_ALL_PACKAGE_UPDATES_ON_MANAGED_INSTANCE Function

Install all of the available package updates for the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`update_type`

(optional) The type of updates to be applied

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_ALL_UPDATES_ON_MANAGED_INSTANCE_GROUP Function

Install all of the available updates for the Managed Instance Group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`update_type`

(optional) The type of updates to be applied

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_ALL_WINDOWS_UPDATES_ON_MANAGED_INSTANCE Function

Install all of the available Windows updates for the managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`update_type`

(optional) The type of updates to be applied

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) OCID for the managed instance

`module_name`

(required) The name of a module.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`profile_name`

(optional) The name of the profile of the containing module stream

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_PACKAGE_ON_MANAGED_INSTANCE Function

Installs a package on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`software_package_name`

(required) Package name

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_PACKAGE_UPDATE_ON_MANAGED_INSTANCE Function

Updates a package on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`software_package_name`

(required) Package name

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTALL_WINDOWS_UPDATE_ON_MANAGED_INSTANCE Function

Installs a Windows update on a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`windows_update_name`

(required) Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_PACKAGES_FOR_MANAGED_INSTANCE Function

Returns a list of packages available for install on the Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_SOFTWARE_SOURCES_FOR_MANAGED_INSTANCE Function

Returns a list of available software sources for a Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_UPDATES_FOR_MANAGED_INSTANCE Function

Returns a list of available updates for a Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_WINDOWS_UPDATES_FOR_MANAGED_INSTANCE Function

Returns a list of available Windows updates for a Managed Instance. This is only applicable to Windows instances.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`is_eligible_for_installation`

(optional) Indicator of whether the update can be installed using OSMS.

Allowed values are: 'INSTALLABLE', 'NOT_INSTALLABLE', 'UNKNOWN'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ERRATA Function

Returns a list of all of the currently available Errata in the system

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`erratum_id`

(optional) The OCID of the erratum.

`advisory_name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

`time_issue_date_start`

(optional) The issue date after which to list all errata, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`time_issue_date_end`

(optional) The issue date before which to list all errata, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort errata by. Only one sort order may be provided. Default order for ISSUEDATE is descending. Default order for ADVISORYNAME is ascending. If no value is specified ISSUEDATE is default.

Allowed values are: 'ISSUEDATE', 'ADVISORYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_ERRATA Function

Returns a list of errata relevant to the Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCE_GROUPS Function

Returns a list of all Managed Instance Groups.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) The current lifecycle state for the object.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`os_family`

(optional) The OS family for which to list resources.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_INSTANCES Function

Returns a list of all Managed Instances.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The OS family for which to list resources.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAM_PROFILES Function

Retrieve a list of module stream profiles from a software source. Filters may be applied to select a subset of module stream profiles based on the filter criteria. The \"moduleName\", \"streamName\", and \"profileName\" attributes combine to form a set of filters on the list of module stream profiles. If a \"moduleName\" is provided, only profiles that belong to that module are returned. If both a \"moduleName\" and \"streamName\" are given, only profiles belonging to that module stream are returned. Finally, if all three are given then only the particular profile indicated by the triple is returned. It is not valid to supply a \"streamName\" without a \"moduleName\". It is also not valid to supply a \"profileName\" without a \"streamName\".

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`profile_name`

(optional) The name of the profile of the containing module stream

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAM_PROFILES_ON_MANAGED_INSTANCE Function

Retrieve a list of module stream profiles, along with a summary of their of their status, from a managed instance. Filters may be applied to select a subset of profiles based on the filter criteria. The \"moduleName\", \"streamName\", and \"profileName\" attributes combine to form a set of filters on the list of module stream profiles. If a \"modulName\" is provided, only profiles that belong to that module are returned. If both a \"moduleName\" and \"streamName\" are given, only profiles belonging to that module stream are returned. Finally, if all three are given then only the particular profile indicated by the triple is returned. It is not valid to supply a \"streamName\" without a \"moduleName\". It is also not valid to supply a \"profileName\" without a \"streamName\". The \"status\" attribute filters against the state of a module stream profile. Valid values are \"INSTALLED\" and \"AVAILABLE\". If the attribute is set to \"INSTALLED\", only module stream profiles that are installed are included in the result set. If the attribute is set to \"AVAILABLE\", only module stream profiles that are not installed are included in the result set. If the attribute is not defined, the request is not subject to this filter. When sorting by display name, the result set is sorted first by module name, then by stream name, and finally by profile name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`profile_name`

(optional) The name of the profile of the containing module stream

`profile_status`

(optional) The status of the profile. A profile with the \"INSTALLED\" status indicates that the profile has been installed. A profile with the \"AVAILABLE\" status indicates that the profile is not installed, but can be.

Allowed values are: 'INSTALLED', 'AVAILABLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAMS Function

Retrieve a list of module streams from a software source. Filters may be applied to select a subset of module streams based on the filter criteria. The 'moduleName' attribute filters against the name of a module. It accepts strings of the format \"&lt;module&gt;\". If this attribute is defined, only streams that belong to the specified module are included in the result set. If it is not defined, the request is not subject to this filter. The 'streamName' attribute filters against the name of a stream of a module. If this attribute is defined, only the particular module stream that matches both the module and stream names is included in the result set. It is not valid to supply 'streamName' without also supplying a 'moduleName'. When sorting by display name, the result set is sorted first by module name, then by stream name.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODULE_STREAMS_ON_MANAGED_INSTANCE Function

Retrieve a list of module streams, along with a summary of their status, from a managed instance. Filters may be applied to select a subset of module streams based on the filter criteria. The 'moduleName' attribute filters against the name of a module. It accepts strings of the format \"&lt;module&gt;\". If this attribute is defined, only streams that belong to the specified module are included in the result set. If it is not defined, the request is not subject to this filter. The \"status\" attribute filters against the state of a module stream. Valid values are \"ENABLED\", \"DISABLED\", and \"ACTIVE\". If the attribute is set to \"ENABLED\", only module streams that are enabled are included in the result set. If the attribute is set to \"DISABLED\", only module streams that are not enabled are included in the result set. If the attribute is set to \"ACTIVE\", only module streams that are active are included in the result set. If the attribute is not defined, the request is not subject to this filter. When sorting by the display name, the result set is sorted first by the module name and then by the stream name.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`module_name`

(optional) The name of a module. This parameter is required if a streamName is specified.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`stream_status`

(optional) The status of the stream A stream with the \"ENABLED\" status can be used as a source for installing profiles. Streams with this status are also \"ACTIVE\". A stream with the \"DISABLED\" status cannot be the source for installing profiles. To install profiles and packages from this stream, it must be enabled. A stream with the \"ACTIVE\" status can be used as a source for installing profiles. The packages that comprise the stream are also used when a matching package is installed directly. In general, a stream can have this status if it is the default stream for the module and no stream has been explicitly enabled.

Allowed values are: 'ENABLED', 'DISABLED', 'ACTIVE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PACKAGES_INSTALLED_ON_MANAGED_INSTANCE Function

Returns a list of installed packages on the Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULED_JOBS Function

Returns a list of all of the currently active Scheduled Jobs in the system

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`managed_instance_id`

(optional) The ID of the managed instance for which to list resources.

`managed_instance_group_id`

(optional) The ID of the managed instace group for which to list resources.

`operation_type`

(optional) The operation type for which to list resources

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`lifecycle_state`

(optional) The current lifecycle state for the object.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The OS family for which to list resources.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`is_restricted`

(optional) If true, will only filter out restricted Autonomous Linux Scheduled Job

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SOFTWARE_SOURCE_PACKAGES Function

Lists Software Packages in a Software Source

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SOFTWARE_SOURCES Function

Returns a list of all Software Sources.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`lifecycle_state`

(optional) The current lifecycle state for the object.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_UPCOMING_SCHEDULED_JOBS Function

Returns a list of all of the Scheduled Jobs whose next execution time is at or before the specified time.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_end`

(required) The cut-off time before which to list all upcoming schedules, in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`tag_name`

(optional) The name of the tag.

`tag_value`

(optional) The value for the tag.

`lifecycle_state`

(optional) The current lifecycle state for the object.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The OS family for which to list resources.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WINDOWS_UPDATES Function

Returns a list of Windows Updates.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WINDOWS_UPDATES_INSTALLED_ON_MANAGED_INSTANCE Function

Returns a list of installed Windows updates for a Managed Instance. This is only applicable to Windows instances.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`compartment_id`

(optional) The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Gets the errors for the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists the log entries for the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`managed_instance_id`

(optional) The ID of the managed instance for which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The OS family for which to list resources.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE Function

Perform an operation involving modules, streams, and profiles on a managed instance. Each operation may enable or disable an arbitrary amount of module streams, and install or remove an arbitrary number of module stream profiles. When the operation is complete, the state of the modules, streams, and profiles on the managed instance will match the state indicated in the operation. Each module stream specified in the list of module streams to enable will be in the \"ENABLED\" state upon completion of the operation. If there was already a stream of that module enabled, any work required to switch from the current stream to the new stream is performed implicitly. Each module stream specified in the list of module streams to disable will be in the \"DISABLED\" state upon completion of the operation. Any profiles that are installed for the module stream will be removed as part of the operation. Each module stream profile specified in the list of profiles to install will be in the \"INSTALLED\" state upon completion of the operation, indicating that any packages that are part of the profile are installed on the managed instance. If the module stream containing the profile is not enabled, it will be enabled as part of the operation. There is an exception when attempting to install a stream of a profile when another stream of the same module is enabled. It is an error to attempt to install a profile of another module stream, unless enabling the new module stream is explicitly included in this operation. Each module stream profile specified in the list of profiles to remove will be in the \"AVAILABLE\" state upon completion of the operation. The status of packages within the profile after the operation is complete is defined by the package manager on the managed instance. Operations that contain one or more elements that are not allowed are rejected. The result of this request is a WorkRequest object. The returned WorkRequest is the parent of a structure of other WorkRequests. Taken as a whole, this structure indicates the entire set of work to be performed to complete the operation. This interface can also be used to perform a dry run of the operation rather than committing it to a managed instance. If a dry run is requested, the OS Management Service will evaluate the operation against the current module, stream, and profile state on the managed instance. It will calculate the impact of the operation on all modules, streams, and profiles on the managed instance, including those that are implicitly impacted by the operation. The WorkRequest resulting from a dry run behaves differently than a WorkRequest resulting from a committable operation. Dry run WorkRequests are always singletons and never have children. The impact of the operation is returned using the log and error facilities of WorkRequests. The impact of operations that are allowed by the OS Management Service are communicated as one or more work request log entries. Operations that are not allowed by the OS Management Service are communicated as one or more work requst error entries. Each entry, for either logs or errors, contains a structured message containing the results of one or more operations.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`manage_module_streams_on_managed_instance_details`

(required) A description of an operation to perform against the modules, streams, and profiles of a managed instance

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) OCID for the managed instance

`module_name`

(required) The name of a module.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`profile_name`

(optional) The name of the profile of the containing module stream

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_PACKAGE_FROM_MANAGED_INSTANCE Function

Removes an installed package from a managed instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`software_package_name`

(required) Package name

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_PACKAGES_FROM_SOFTWARE_SOURCE Function

Removes a given list of Software Packages from a specific Software Source.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`remove_packages_from_software_source_details`

(required) A list of package identifiers

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RUN_SCHEDULED_JOB_NOW Function

This will trigger an already created Scheduled Job to being executing immediately instead of waiting for its next regularly scheduled time.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_SOFTWARE_PACKAGES Function

Searches all of the available Software Sources and returns any/all Software Packages matching the search criteria.

Syntax
```

```

Parameters

Parameter Description

`software_package_name`

(optional) the identifier for the software package (not an OCID)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`cve_name`

(optional) The name of the CVE as published. Example: `CVE-2006-4535`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SKIP_NEXT_SCHEDULED_JOB_EXECUTION Function

This will force an already created Scheduled Job to skip its next regularly scheduled execution

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) OCID for the managed instance

`module_name`

(required) The name of a module.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`stream_name`

(optional) The name of the stream of the containing module. This parameter is required if a profileName is specified.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGED_INSTANCE Function

Updates a specific Managed Instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) OCID for the managed instance

`update_managed_instance_details`

(required) Details about a Managed Instance to update

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGED_INSTANCE_GROUP Function

Updates a specific Managed Instance Group.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_group_id`

(required) OCID for the managed instance group

`update_managed_instance_group_details`

(required) Details about a Managed Instance Group to update

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SCHEDULED_JOB Function

Updates an existing Scheduled Job on the management system.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The ID of the scheduled job.

`update_scheduled_job_details`

(required) Details about a Scheduled Job to update

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SOFTWARE_SOURCE Function

Updates an existing custom Software Source on the management system.

Syntax
```

```

Parameters

Parameter Description

`software_source_id`

(required) The OCID of the software source.

`update_software_source_details`

(required) Details about a Sofware Source to update

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-82003610-8523-48FE-B55C-43631C3C1928)
- [ADD_PACKAGES_TO_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-906BAE77-15A6-4511-95DD-EF144390BDD4)
- [ATTACH_CHILD_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-6AB14A21-B263-4B21-B5EE-452FF79455E1)
- [ATTACH_MANAGED_INSTANCE_TO_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D873E369-032C-4C3D-950B-050B19C037DF)
- [ATTACH_PARENT_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-9217B771-9C37-4AA1-B85D-7A9304943FBE)
- [CHANGE_MANAGED_INSTANCE_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D098DAFF-7EF4-4F32-9677-9FA00ECEAD50)
- [CHANGE_SCHEDULED_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-63048088-F443-45D2-8429-8DA22549C2E5)
- [CHANGE_SOFTWARE_SOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-A09E04E9-B8D4-4E21-8831-D45AE67F874A)
- [CREATE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-AAFF04BE-E8A9-4E9F-9DD3-650EF84D885E)
- [CREATE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F3D0CD93-853A-4BAF-8CC4-4015321CB654)
- [CREATE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-BA4A63B4-80C0-4165-8ED8-5E90086934A5)
- [DELETE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-EF33B3B7-8660-432D-98A9-76225E274B81)
- [DELETE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F41CC150-0F15-4055-A6C1-723C7D4F6574)
- [DELETE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F7C05284-AEBF-428E-9A0C-B9C792B008BE)
- [DETACH_CHILD_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-90113F34-9F14-41FA-A3E5-7C99B51A8DB7)
- [DETACH_MANAGED_INSTANCE_FROM_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-77738119-93ED-4EFA-B517-5DE87D81299B)
- [DETACH_PARENT_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-CAB9E84C-4CEF-434B-ACA8-72864CFB3913)
- [DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-809797C8-B809-401B-8F3A-4D7DAF18171A)
- [ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D584E659-225C-448E-A310-21A43C435F51)
- [GET_ERRATUM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-4841C10C-C5AF-49F9-9043-18A182A0ACEE)
- [GET_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-26F514D7-436A-4FB2-B381-9079990A5466)
- [GET_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-ADFDA1D7-4201-4422-9EBD-37CA2C534648)
- [GET_MODULE_STREAM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-135B548B-7D27-44C6-A4CD-68CFF1A7EDF6)
- [GET_MODULE_STREAM_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-28C5D1D6-13E4-4080-9DA7-85FDFDACEACD)
- [GET_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-18F81581-BCC1-485D-A8DF-0CA499D55E90)
- [GET_SOFTWARE_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-1CF29932-C4DC-4B5C-A4B0-460757400271)
- [GET_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-03A75014-7075-4B1C-BA76-6864D7664557)
- [GET_WINDOWS_UPDATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-B5B76BBA-C4A5-4744-970C-07D4EDDBD71B)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-9C908800-D56D-43FF-A008-F00417209384)
- [INSTALL_ALL_PACKAGE_UPDATES_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-DEAF4B82-CB9E-4FB8-86C2-B108EE7680AE)
- [INSTALL_ALL_UPDATES_ON_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-95400C37-F3FE-4296-A49E-05708A14B0D7)
- [INSTALL_ALL_WINDOWS_UPDATES_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-68217F4D-12F5-4AE6-89C4-79D2A3295276)
- [INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D6068450-3B9B-4C16-96F0-370A818982E6)
- [INSTALL_PACKAGE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-84E2B305-7C75-4D68-B8A3-1CD04908BBB6)
- [INSTALL_PACKAGE_UPDATE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F76833B7-EBBB-4DF1-B548-5A11461F1A04)
- [INSTALL_WINDOWS_UPDATE_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-563076A3-F08D-406B-92BA-2CE3421BE1E0)
- [LIST_AVAILABLE_PACKAGES_FOR_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-FAD9894C-CC98-418E-B5B9-E2DED40F1D74)
- [LIST_AVAILABLE_SOFTWARE_SOURCES_FOR_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-5F90AE34-4717-4BA3-B451-1A18FB3CA876)
- [LIST_AVAILABLE_UPDATES_FOR_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-0C380FF3-58B7-4ED7-B7A3-22DCBCEBD1B7)
- [LIST_AVAILABLE_WINDOWS_UPDATES_FOR_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-FEA177F7-A026-4335-AADD-69BEC147137F)
- [LIST_ERRATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-01A1E0F9-AAF4-4D7D-A92B-8E6DCD21BD6F)
- [LIST_MANAGED_INSTANCE_ERRATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D4CDE4CA-E350-4B02-99CC-DB6D0C8AC0D1)
- [LIST_MANAGED_INSTANCE_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-166F37D1-D9A0-4C05-8FC8-91E8F5DE309F)
- [LIST_MANAGED_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-BF704810-0514-436E-BAD9-018928B2084C)
- [LIST_MODULE_STREAM_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-B1140B9E-B19E-4D7D-9C6B-3570F4D5C00D)
- [LIST_MODULE_STREAM_PROFILES_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-43B04BF4-2B2D-497D-B577-AE0136BC679C)
- [LIST_MODULE_STREAMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-6835EAB4-4EC8-480E-9FFC-858ADDA4695C)
- [LIST_MODULE_STREAMS_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F1352BDE-3633-46EB-86C5-6C094B9C699C)
- [LIST_PACKAGES_INSTALLED_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-1DDDE90F-AD0E-4785-921A-33E6B3E2A631)
- [LIST_SCHEDULED_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-335DD15B-DEDC-4CAB-916B-6C89EA21D3DD)
- [LIST_SOFTWARE_SOURCE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-735A2415-78F9-406D-BB22-32077F1C3E9A)
- [LIST_SOFTWARE_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F8ACDBCC-A623-4C33-BCE1-CA215C347FBC)
- [LIST_UPCOMING_SCHEDULED_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-08913755-F4EF-4918-AC2D-946F5FD88E4F)
- [LIST_WINDOWS_UPDATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-0B26D27C-DC4F-45C9-B2CE-1EF1D09C9E2C)
- [LIST_WINDOWS_UPDATES_INSTALLED_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-9EA2E5EF-0F87-4B7C-B609-52C1D7C63ED1)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-A504164F-C5EC-4743-8730-D2D6AE84AAA3)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D3D69AF0-3D9F-4A3A-AEE9-078B1C9B1773)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F8FC8C16-ADAB-4ED5-B8D4-97831204AA3F)
- [MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-09B4DA75-9226-4FCB-B1F0-6DBB2B446BCB)
- [REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-441827FE-510E-42D6-9DDC-8803530C17B7)
- [REMOVE_PACKAGE_FROM_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-06D0288C-4297-4EA3-A614-C3A2FB5C439C)
- [REMOVE_PACKAGES_FROM_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-60F122D2-DFB6-4873-88D7-DB5B6844D91A)
- [RUN_SCHEDULED_JOB_NOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-49B09421-76FE-4FB3-86AE-0D4BD5A7284B)
- [SEARCH_SOFTWARE_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-F2FFA22A-DD9A-4A4B-A932-9F45A567B3DF)
- [SKIP_NEXT_SCHEDULED_JOB_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-FD9E40B1-24A0-440F-BD4A-1088B11AA6A1)
- [SWITCH_MODULE_STREAM_ON_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-2128AF76-9A07-4CE9-AC59-58BEF61A2E5E)
- [UPDATE_MANAGED_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-C55B5D7F-3A5C-4284-8DD6-66090FDE806D)
- [UPDATE_MANAGED_INSTANCE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-2436C3AE-917C-4FBC-B27F-DB926D20D634)
- [UPDATE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-D6103678-503F-4DC0-B089-34F0BB45BE65)
- [UPDATE_SOFTWARE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_os_management.html#ADSDK-GUID-8178C6A1-30BC-47B0-9863-B43F54B4D232)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
