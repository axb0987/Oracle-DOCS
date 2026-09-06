# OS Management Hub Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#dcoc-content-body)

## OS Management Hub Common Types

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_DETAILS_T Type

The details of the user-friendly names to be used for actions.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the resulting job. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) User specified information about the resulting job. Does not have to be unique, and it's changeable. Avoid entering confidential information.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCES_DETAILS_T Type

The details about the managed instances.

Syntax
```

```

Fields

Field Description

`managed_instances`

(required) The list of managed instance OCIDs to be attached/detached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_MANAGED_INSTANCES_TO_LIFECYCLE_STAGE_DETAILS_T Type

The managed instances to attach to the lifecycle stage.

Syntax
```

```

Fields

Field Description

`managed_instance_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_MANAGED_INSTANCES_TO_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The managed instance OCIDs to attach to the managed instance group.

Syntax
```

```

Fields

Field Description

`managed_instances`

(optional) The list of managed instance OCIDs to be attached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_DETAILS_T Type

The details about the software sources to be attached.

Syntax
```

```

Fields

Field Description

`software_sources`

(required) The list of software source OCIDs to be attached/detached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The software sources OCIDs to attach to the managed instance group.

Syntax
```

```

Fields

Field Description

`software_sources`

(optional) The list of software sources OCIDs to be attached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_DETAILS_T Type

Identifying information for the specified software source.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the software source.

`display_name`

(optional) Software source name.

`description`

(optional) Software source description.

`software_source_type`

(optional) Type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_source_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_SUMMARY_T Type

A software package summary.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name.

`name`

(required) Unique identifier for the package.

`l_type`

(required) Type of the package.

`version`

(required) Version of the installed package.

`architecture`

(optional) The architecture for which this package was built.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`software_sources`

(optional) list of software sources that provide the software package.

`package_classification`

(required) classifier for child instances of this object.

Allowed values are: 'INSTALLED', 'AVAILABLE', 'UPDATABLE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_SUMMARY_T Type

A software package available for install on a managed instance.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_available_package_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_package_summary_t`type.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_available_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_COLLECTION_T Type

Results of an available package search on a managed instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of available packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_T Type

A software source which can be added to a managed instance. Once a software source is added, packages from that software source can be installed on that managed instance.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation.

`compartment_id`

(required) The OCID for the compartment.

`display_name`

(required) User friendly name for the software source.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_available_software_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_COLLECTION_T Type

Results of searching for available software sources for a managed instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of available software sources.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_AVAILABILITY_T Type

An object that contains a software source OCID and its availability.

Syntax
```

```

Fields

Field Description

`software_source_id`

(required) The OCID for a vendor software source.

`availability`

(required) Possible availabilities of a software source.

Allowed values are: 'AVAILABLE', 'SELECTED', 'RESTRICTED'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_AVAILABILITY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_source_availability_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CHANGE_AVAILABILITY_OF_SOFTWARE_SOURCES_DETAILS_T Type

Request body that contains a list of software sources whose availability needs to be updated.

Syntax
```

```

Fields

Field Description

`software_source_availabilities`

(optional) List of objects containing software source ids and its availability.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ID_T Type

An id along with a name to simplify display for a user.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource that is immutable on creation.

`display_name`

(required) User friendly name.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_FILTER_T Type

Used to select packages from VendorSoftwareSources to create/update CustomSoftwareSources.

Syntax
```

```

Fields

Field Description

`package_name`

(optional) The package name.

`package_name_pattern`

(optional) The package name pattern.

`package_version`

(optional) The package version, which is denoted by 'version-release', or 'epoch:version-release'.

`filter_type`

(required) The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_FILTER_T Type

Used to select module stream/profiles from VendorSoftwareSources to create/update CustomSoftwareSources.

Syntax
```

```

Fields

Field Description

`module_name`

(required) Module name.

`profile_name`

(optional) Profile name.

`stream_name`

(optional) Stream name.

`filter_type`

(required) The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_FILTER_T Type

Used to select groups from VendorSoftwareSources to create/update CustomSoftwareSources.

Syntax
```

```

Fields

Field Description

`package_groups`

(optional) List of package group names.

`filter_type`

(required) The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_FILTER_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_package_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_FILTER_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_stream_profile_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_FILTER_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_package_group_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_FILTER_T Type

Used to apply filters to a VendorSoftwareSource to create/update CustomSoftwareSources.

Syntax
```

```

Fields

Field Description

`package_filters`

(optional) The list of package filters.

`module_stream_profile_filters`

(optional) The list of module stream/profile filters.

`package_group_filters`

(optional) The list of group filters.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SOFTWARE_SOURCE_DETAILS_T Type

Description of a software source to be created.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the software source.

`display_name`

(required) User friendly name for the software source.

`description`

(optional) Information specified by the user about the software source.

`software_source_type`

(required) Type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ID_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_id_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type

Description of a custom software source to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_custom_software_source_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_software_source_details_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

`custom_software_source_filter`

(optional)

`is_automatically_updated`

(optional) Indicates whether service should automatically update the custom software source for the user.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_ENTITLEMENT_DETAILS_T Type

Creates an entitlement for the specified compartment OCID and CSI.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the entitlement.

`csi`

(required) A Customer Support Identifier (CSI) is a unique key given to a customer to unlock software sources. It uniquely identifies the entitlement.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_PROFILE_DETAILS_T Type

The information about new registration profile.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the tenancy containing the registration profile.

`description`

(optional) The description of the registration profile.

`management_station_id`

(optional) The OCID of the management station.

`profile_type`

(required) The type of registration profile. Either SOFTWARESOURCE, GROUP or LIFECYCLE.

Allowed values are: 'SOFTWARESOURCE', 'GROUP', 'LIFECYCLE', 'STATION'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_GROUP_PROFILE_DETAILS_T Type

Description of a group registration profile to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_group_profile_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_profile_details_t`type.

Fields

Field Description

`managed_instance_group_id`

(required) The OCID of the managed instance group from which the registration profile will inherit its software sources.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_STAGE_DETAILS_T Type

The information about a lifecycle stage.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`rank`

(required) User specified rank for the lifecycle stage. Rank determines the hierarchy of the lifecycle stages for a given lifecycle environment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_STAGE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_create_lifecycle_stage_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_ENVIRONMENT_DETAILS_T Type

Creates a lifecycle environment. A lifecycle environment is a user-defined pipeline to deliver curated, versioned content in a prescribed, methodical manner.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the lifecycle environment.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) User specified information about the lifecycle environment.

`stages`

(required) User specified list of ranked lifecycle stages to be created for the lifecycle environment.

`arch_type`

(required) The CPU architecture of the managed instance(s) in the lifecycle environment.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(required) The operating system type of the managed instance(s) in the lifecycle environment.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_PROFILE_DETAILS_T Type

Description of a lifecycle registration profile to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_lifecycle_profile_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_profile_details_t`type.

Fields

Field Description

`lifecycle_stage_id`

(required) The OCID of the lifecycle stage from which the registration profile will inherit its software source.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The information about new managed instance group.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name for the managed instance group. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Details about the managed instance group.

`compartment_id`

(required) The OCID of the tenancy containing the managed instance group.

`os_family`

(required) The operating system type of the managed instance(s) that this managed instance group will contain.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The CPU architecture type of the managed instance(s) that this managed instance group will contain.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`software_source_ids`

(required) The list of software source OCIDs available to the managed instances in the managed instance group.

`managed_instance_ids`

(optional) The list of managed instance OCIDs to be added to the managed instance group.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_PROXY_CONFIGURATION_DETAILS_T Type

Information for creating a proxy configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) To enable or disable the proxy (default true)

`hosts`

(optional) List of hosts

`port`

(optional) Port that the proxy will use

`forward`

(optional) URL that the proxy will forward to

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MIRROR_CONFIGURATION_DETAILS_T Type

Information for creating a mirror configuration

Syntax
```

```

Fields

Field Description

`directory`

(required) Directory for the mirroring

`port`

(required) Default port for the mirror

`sslport`

(required) Default sslport for the mirror

`sslcert`

(optional) Local path for the sslcert

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MANAGEMENT_STATION_DETAILS_T Type

Information for creating an ManagementStation

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the Management Station.

`display_name`

(required) Management Station name

`description`

(optional) Details describing the Management Station config.

`hostname`

(required) Name of the host

`proxy`

(required)

`mirror`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_T Type

Updatable information for a module stream.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(required) The name of a stream of the specified module.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_T Type

Updatable information for a module stream profile.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(required) The name of a stream of the specified module.

`profile_name`

(required) The name of a profile of the specified module stream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_stream_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_stream_profile_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_IN_SCHEDULED_JOB_DETAILS_T Type

The set of changes to make to the state of the modules, streams, and profiles on the managed target.

Syntax
```

```

Fields

Field Description

`enable`

(optional) The set of module streams to enable.

`disable`

(optional) The set of module streams to disable.

`install`

(optional) The set of module stream profiles to install.

`remove`

(optional) The set of module stream profiles to remove.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_OPERATION_T Type

Defines an operation in a scheduled job.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of operation this scheduled job performs.

Allowed values are: 'INSTALL_PACKAGES', 'UPDATE_PACKAGES', 'REMOVE_PACKAGES', 'UPDATE_ALL', 'UPDATE_SECURITY', 'UPDATE_BUGFIX', 'UPDATE_ENHANCEMENT', 'UPDATE_OTHER', 'UPDATE_KSPLICE_USERSPACE', 'UPDATE_KSPLICE_KERNEL', 'MANAGE_MODULE_STREAMS', 'SWITCH_MODULE_STREAM', 'ATTACH_SOFTWARE_SOURCES', 'DETACH_SOFTWARE_SOURCES', 'SYNC_MANAGEMENT_STATION_MIRROR', 'PROMOTE_LIFECYCLE'

`package_names`

(optional) The names of the target packages (only if operation type is INSTALL_PACKAGES/UPDATE_PACKAGES/REMOVE_PACKAGES).

`manage_module_streams_details`

(optional)

`switch_module_streams_details`

(optional)

`software_source_ids`

(optional) The OCIDs for the software sources (only if operation type is ATTACH_SOFTWARE_SOURCES/DETACH_SOFTWARE_SOURCES).

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_scheduled_job_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SCHEDULED_JOB_DETAILS_T Type

Information for creating a scheduled job.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the scheduled job.

`display_name`

(optional) Scheduled job name.

`description`

(optional) Details describing the scheduled job.

`schedule_type`

(required) The type of scheduling this scheduled job follows.

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(required) The desired time for the next execution of this scheduled job.

`recurring_rule`

(optional) The recurring rule for a recurring scheduled job.

`managed_instance_ids`

(optional) The list of managed instance OCIDs this scheduled job operates on. Either this or managedInstanceGroupIds, or managedCompartmentIds, or lifecycleStageIds must be supplied.

`managed_instance_group_ids`

(optional) The list of managed instance group OCIDs this scheduled job operates on. Either this or managedInstanceIds, or managedCompartmentIds, or lifecycleStageIds must be supplied.

`managed_compartment_ids`

(optional) The list of target compartment OCIDs if this scheduled job operates on a compartment level. Either this or managedInstanceIds, or managedInstanceGroupIds, or lifecycleStageIds must be supplied.

`lifecycle_stage_ids`

(optional) The list of lifecycle stage OCIDs this scheduled job operates on. Either this or managedInstanceIds, or managedInstanceGroupIds, or managedCompartmentIds must be supplied.

`is_subcompartment_included`

(optional) Whether to create jobs for all compartments in the tenancy when managedCompartmentIds specifies the tenancy OCID.

`operations`

(required) The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SOFTWARE_SOURCE_PROFILE_DETAILS_T Type

Description of a software source registration profile to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_software_source_profile_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_profile_details_t`type.

Fields

Field Description

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`os_family`

(required) The operating system family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The architecture type.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`software_source_ids`

(required) The list of software source OCIDs that the registration profile will use.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_STATION_PROFILE_DETAILS_T Type

Description of a group registration profile to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_station_profile_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_profile_details_t`type.

Fields

Field Description

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`os_family`

(optional) The operating system family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The architecture type.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_VERSIONED_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type

Description of a versioned custom software source to be created.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_create_versioned_custom_software_source_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_create_software_source_details_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

`custom_software_source_filter`

(optional)

`software_source_version`

(required) The version to assign to this custom software source.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_T Type

A software source contains a collection of packages.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the software source.

`compartment_id`

(required) The OCID of the tenancy containing the software source.

`display_name`

(required) User friendly name for the software source.

`time_created`

(required) The date and time the software source was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`description`

(optional) Information specified by the user about the software source.

`software_source_type`

(required) Type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

`availability`

(required) Possible availabilities of a software source.

Allowed values are: 'AVAILABLE', 'SELECTED', 'RESTRICTED'

`repo_id`

(required) The Repo ID for the software source.

`os_family`

(required) The OS family the software source belongs to.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The architecture type supported by the software source.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`lifecycle_state`

(optional) The current state of the software source.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`package_count`

(optional) Number of packages.

`url`

(required) URL for the repository.

`checksum_type`

(optional) The yum repository checksum type used by this software source.

Allowed values are: 'SHA1', 'SHA256', 'SHA384', 'SHA512'

`gpg_key_url`

(optional) URL of the GPG key for this software source.

`gpg_key_id`

(optional) ID of the GPG key for this software source.

`gpg_key_fingerprint`

(optional) Fingerprint of the GPG key for this software source.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_T Type

A custom software source contains a custom collection of packages.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_custom_software_source_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

`custom_software_source_filter`

(optional)

`is_automatically_updated`

(optional) Indicates whether service should automatically update the custom software source for the user.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_SUMMARY_T Type

A software source contains a collection of packages.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID for the software source.

`compartment_id`

(required) The OCID of the tenancy containing the software source.

`display_name`

(required) User friendly name for the software source.

`repo_id`

(required) The Repo ID for the software source.

`url`

(required) URL for the repository.

`time_created`

(required) The date and time the software source was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) The date and time of when the software source was updated as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`description`

(optional) Information specified by the user about the software source.

`software_source_type`

(required) Type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

`availability`

(required) Possible availabilities of a software source.

Allowed values are: 'AVAILABLE', 'SELECTED', 'RESTRICTED'

`os_family`

(required) The OS family the software source belongs to.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The architecture type supported by the software source.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`package_count`

(optional) Number of packages.

`lifecycle_state`

(optional) The current state of the software source.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_SUMMARY_T Type

A custom software source contains a custom collection of packages.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_custom_software_source_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_summary_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_MANAGED_INSTANCES_FROM_LIFECYCLE_STAGE_DETAILS_T Type

The managed instances to detach from the lifecycle stage.

Syntax
```

```

Fields

Field Description

`managed_instance_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_MANAGED_INSTANCES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The managed instance OCIDs to detach from the managed instance group.

Syntax
```

```

Fields

Field Description

`managed_instances`

(optional) The list of managed instance OCIDs to be detached.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_DETAILS_T Type

The details about the software sources to be detached.

Syntax
```

```

Fields

Field Description

`software_sources`

(required) The list of software source OCIDs to be attached/detached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The software sources OCIDs to detach from the managed instance group.

Syntax
```

```

Fields

Field Description

`software_sources`

(optional) The list of software sources OCIDs to be detached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type

The details of the module stream to be disabled on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The work request details for the module stream operation on the managed instance group.

Syntax
```

```

Fields

Field Description

`module_name`

(optional) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type

The details of the module stream to be enabled on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The work request details for the module stream operation on the managed instance group.

Syntax
```

```

Fields

Field Description

`module_name`

(optional) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_SUMMARY_T Type

A summary of an entitlement.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the entitlement.

`csi`

(required) The Customer Support Identifier (CSI). CSI is a unique key given to a customer to unlock software sources. It uniquely identifies the entitlement.

`vendor_name`

(required) The vendor for the entitlement.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_entitlement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_COLLECTION_T Type

Results of a Entitlement search. Contains boh EntitlementSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Entitlement.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_SUMMARY_T Type

Summary information for a software package.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name.

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID.

`l_type`

(required) Type of the package.

`version`

(required) Version of the package.

`architecture`

(optional) The architecture for which this software was built.

`checksum`

(optional) Checksum of the package.

`checksum_type`

(optional) Type of the checksum.

`is_latest`

(optional) Indicates whether this package is the latest version.

`software_sources`

(optional) List of software sources that provide the software package.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_T Type

Details about the erratum.

Syntax
```

```

Fields

Field Description

`name`

(required) Advisory name.

`synopsis`

(optional) Summary description of the erratum.

`time_issued`

(optional) Date the erratum was issued, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`description`

(optional) Details describing the erratum.

`time_updated`

(optional) Most recent date the erratum was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`classification_type`

(optional) Type of the erratum.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`l_from`

(optional) Information specifying from where the erratum was release.

`solution`

(optional) Information describing how the erratum can be resolved.

`references`

(optional) Information describing how to find more information about. the erratum.

`related_cves`

(optional) List of CVEs applicable to this erratum.

`repositories`

(optional) List of repository identifiers.

`packages`

(optional) List of Packages affected by this erratum.

`os_families`

(optional) List of affected OS families.

`advisory_severity`

(optional) The severity for a security advisory, otherwise, null.

Allowed values are: 'LOW', 'MODERATE', 'IMPORTANT', 'CRITICAL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_SUMMARY_T Type

Important changes for software. This can include security advisories, bug fixes, or enhancements.

Syntax
```

```

Fields

Field Description

`name`

(required) Advisory name.

`synopsis`

(optional) Summary description of the erratum.

`time_issued`

(optional) Date the erratum was issued, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) Most recent date the erratum was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`classification_type`

(optional) Type of the erratum.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`related_cves`

(optional) List of CVEs applicable to this erratum.

`os_families`

(optional) List of affected OS families.

`advisory_severity`

(optional) The severity advisory. Only valid for security type advisories.

Allowed values are: 'LOW', 'MODERATE', 'IMPORTANT', 'CRITICAL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_erratum_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_COLLECTION_T Type

Results of a Erratum search. Contains boh ErratumSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Errata.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_DETAILS_T Type

Identifying information for the specified managed instance group.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the managed instance group.

`display_name`

(optional) Managed instance group displayName.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_T Type

Description of registration profile.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the profile that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the registration profile.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) The description of the registration profile.

`management_station_id`

(optional) The OCID of the management station.

`profile_type`

(optional) The type of Profile. One of SOFTWARESOURCE, GROUP or LIFECYCLE.

Allowed values are: 'SOFTWARESOURCE', 'GROUP', 'LIFECYCLE', 'STATION'

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`os_family`

(required) The operating system family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The architecture type.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`time_created`

(optional) The time the the registration profile was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the registration profile.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_GROUP_PROFILE_T Type

Definition of a registration profile of type GROUP.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_group_profile_t`is a subtype of the`dbms_cloud_oci_os_management_hub_profile_t`type.

Fields

Field Description

`managed_instance_group`

(required)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_DETAILS_T Type

The details of the module stream profile to be installed on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`profile_name`

(optional) The name of a profile of the specified module stream.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The work request details for the module stream profile operation on the managed instance group.

Syntax
```

```

Fields

Field Description

`module_name`

(optional) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`profile_name`

(optional) The name of a profile of the specified module stream.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_PACKAGES_ON_MANAGED_INSTANCE_DETAILS_T Type

The details about the software packages to be installed.

Syntax
```

```

Fields

Field Description

`package_names`

(required) The list of package names.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The names of the packages to be installed on the managed instance group.

Syntax
```

```

Fields

Field Description

`package_names`

(optional) The list of package names.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_SUMMARY_T Type

A software package installed on a managed instance.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_installed_package_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_package_summary_t`type.

Fields

Field Description

`time_installed`

(required) The date and time the package was installed, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_issued`

(optional) The date and time the package was issued by a providing erratum (if available), as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_installed_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_COLLECTION_T Type

Results of an installed package search on a managed instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of installed packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_DETAILS_T Type

Identifying information for the specified managed instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the managed instance.

`display_name`

(optional) Managed instance name.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_T Type

Defines the lifecycle stage.

Syntax
```

```

Fields

Field Description

`id`

(optional) The lifecycle stage OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the lifecycle stage.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`lifecycle_environment_id`

(optional) The OCID of the lifecycle environment for the lifecycle stage.

`rank`

(required) User specified rank for the lifecycle stage. Rank determines the hierarchy of the lifecycle stages for a given lifecycle environment.

`os_family`

(optional) The operating system type of the target instances.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The CPU architecture of the target instances.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`managed_instance_ids`

(optional) The list of managed instances specified lifecycle stage.

`software_source_id`

(optional)

`time_created`

(optional) The time the lifecycle stage was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the lifecycle stage was last modified. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the lifecycle stage.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_lifecycle_stage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_T Type

Contains versioned software source content and lifecycle stages for a managed instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the lifecycle environment.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) User specified information about the lifecycle environment.

`stages`

(required) User specified list of lifecycle stages to be created for the lifecycle environment.

`managed_instance_ids`

(optional) The list of managed instance OCIDs specified in the lifecycle stage.

`lifecycle_state`

(required) The current state of the lifecycle environment.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`os_family`

(required) The operating system type of the target instances.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(required) The CPU architecture of the target instances.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`time_created`

(required) The time the lifecycle environment was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the lifecycle environment was last modified. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_SUMMARY_T Type

Defines the lifecycle stage summary.

Syntax
```

```

Fields

Field Description

`id`

(optional) The lifecycle stage OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the lifecycle stage.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`lifecycle_environment_id`

(optional) The OCID of the lifecycle environment for the lifecycle stage.

`lifecycle_environment_display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`rank`

(required) User specified rank for the lifecycle stage. Rank determines the hierarchy of the lifecycle stages for a given lifecycle environment.

`os_family`

(optional) The operating system type of the target instances.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The CPU architecture of the target instances.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`managed_instances`

(optional) The number of managed instances attached to the lifecycle stage.

`software_source_id`

(optional)

`time_created`

(optional) The time the lifecycle stage was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the lifecycle stage was last modified. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the lifecycle environment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_lifecycle_stage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_SUMMARY_T Type

Summary of the lifecycle environment.

Syntax
```

```

Fields

Field Description

`id`

(required) The lifecycle environment OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the lifecycle environment.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(required) User specified information about the lifecycle environment.

`stages`

(required) User specified list of lifecycle stages to be created for the lLifecycle environment.

`lifecycle_state`

(optional) The current state of the lifecycle environment.

`arch_type`

(required) The CPU architecture of the target managed instance.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(required) The operating system type of the target managed instance.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`vendor_name`

(required) The software source vendor name.

Allowed values are: 'ORACLE'

`time_created`

(optional) The time the lifecycle environment was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the lifecycle environment was modified. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_lifecycle_environment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_COLLECTION_T Type

Results of a lifecycle environment search. Contains both lifecycle environment summary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of lifecycle environments.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_DETAILS_T Type

Identifying information for the specified lifecycle environment.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the lifecycle environment.

`display_name`

(optional) Lifecycle environment name.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_DETAILS_T Type

Identifying information for the specified lifecycle stage.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the lifecycle stage.

`display_name`

(optional) Lifecycle stage name.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_PROFILE_T Type

Definition of a registration profile of type LIFECYCLE.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_lifecycle_profile_t`is a subtype of the`dbms_cloud_oci_os_management_hub_profile_t`type.

Fields

Field Description

`lifecycle_environment`

(optional)

`lifecycle_stage`

(required)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_COLLECTION_T Type

Results of a lifecycle stage search. Contains both lifecycle stage summary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of lifecycle stages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_DETAILS_T Type

The set of changes to make to the state of the modules, streams, and profiles on a managed instance

Syntax
```

```

Fields

Field Description

`is_dry_run`

(optional) Indicates if this operation is a dry run or if the operation should be committed. If set to true, the result of the operation will be evaluated but not committed. If set to false, the operation is committed to the managed instance. The default is false.

`enable`

(optional) The set of module streams to enable.

`disable`

(optional) The set of module streams to disable.

`install`

(optional) The set of module stream profiles to install.

`remove`

(optional) The set of module stream profiles to remove.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The set of changes to make to the state of the modules, streams, and profiles on a managed instance group.

Syntax
```

```

Fields

Field Description

`is_dry_run`

(optional) Indicates if this operation is a dry run or if the operation should be committed. If set to true, the result of the operation will be evaluated but not committed. If set to false, the operation is committed to the managed instance(s). The default is false.

`enable`

(optional) The set of module streams to enable.

`disable`

(optional) The set of module streams to disable.

`install`

(optional) The set of module stream profiles to install.

`remove`

(optional) The set of module stream profiles to remove.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_T Type

Detail information for an OCI Compute instance that is being managed.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID for the managed instance.

`display_name`

(required) Managed instance identifier.

`description`

(optional) Information specified by the user about the managed instance.

`tenancy_id`

(required) The OCID for the tenancy this managed instance resides in.

`compartment_id`

(required) The OCID for the compartment this managed instance resides in.

`location`

(optional) location of the managed instance.

Allowed values are: 'ON_PREMISE', 'OCI_COMPUTE', 'AZURE', 'EC2'

`time_last_checkin`

(optional) Time at which the instance last checked in, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_last_boot`

(optional) Time at which the instance last booted, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`os_name`

(optional) Operating System Name.

`os_version`

(optional) Operating System Version.

`os_kernel_version`

(optional) Operating System Kernel Version.

`ksplice_effective_kernel_version`

(optional) The ksplice effective kernel version.

`architecture`

(optional) The CPU architecture type of the managed instance.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`status`

(required) status of the managed instance.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING', 'REGISTRATION_ERROR'

`profile`

(optional) The content profile of this instance.

`is_management_station`

(optional) Whether this managed instance is acting as an on-premise management station.

`primary_management_station_id`

(optional) The OCID of a management station to be used as the preferred primary.

`secondary_management_station_id`

(optional) The OCID of a management station to be used as the preferred secondary.

`software_sources`

(optional) The list of software sources currently attached to the managed instance.

`managed_instance_group`

(optional)

`lifecycle_environment`

(optional)

`lifecycle_stage`

(optional)

`is_reboot_required`

(optional) Indicates whether a reboot is required to complete installation of updates.

`installed_packages`

(optional) Number of packages installed on the system.

`updates_available`

(optional) Number of updates available to be installed.

`security_updates_available`

(optional) Number of security type updates available to be installed.

`bug_updates_available`

(optional) Number of bug fix type updates available to be installed.

`enhancement_updates_available`

(optional) Number of enhancement type updates available to be installed.

`other_updates_available`

(optional) Number of non-classified updates available to be installed.

`scheduled_job_count`

(optional) Number of scheduled jobs associated with this instance.

`work_request_count`

(optional) Number of work requests associated with this instance.

`time_created`

(optional) The date and time the work request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) The date and time the work request was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_SUMMARY_T Type

A metric emitted by managed instance resource.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of this metric.

Allowed values are: 'TOTAL_INSTANCE_COUNT', 'INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT', 'INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT', 'NORMAL_INSTANCE_COUNT', 'ERROR_INSTANCE_COUNT', 'WARNING_INSTANCE_COUNT', 'UNREACHABLE_INSTANCE_COUNT', 'REGISTRATION_FAILED_INSTANCE_COUNT', 'INSTANCE_SECURITY_UPDATES_COUNT', 'INSTANCE_BUGFIX_UPDATES_COUNT'

`dimensions`

(required) Qualifiers provided in a metric definition. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair. Example: `\"managedInstanceId\": \"ocid1.managementagent.123\"`

`l_count`

(required) The value of this metric.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_analytic_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_COLLECTION_T Type

Collection of ManagedInstanceAnalyticSummary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of managed instance analytic summary.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_SUMMARY_T Type

Summary of the ManagedInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID for the managed instance.

`display_name`

(required) Managed instance identifier.

`description`

(optional) Information specified by the user about the managed instance.

`tenancy_id`

(required) The OCID for the tenancy this managed instance resides in.

`compartment_id`

(required) The OCID for the compartment this managed instance resides in.

`location`

(optional) Location of the managed instance.

Allowed values are: 'ON_PREMISE', 'OCI_COMPUTE', 'AZURE', 'EC2'

`architecture`

(optional) The CPU architecture type of the managed instance.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`status`

(required) status of the managed instance.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING', 'REGISTRATION_ERROR'

`managed_instance_group`

(optional)

`lifecycle_environment`

(optional)

`lifecycle_stage`

(optional)

`is_reboot_required`

(optional) Indicates whether a reboot is required to complete installation of updates.

`updates_available`

(optional) Number of updates available to be installed.

`is_management_station`

(optional) Whether this managed instance is acting as an on-premise management station.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_COLLECTION_T Type

Results of a managed instance search. Contains both managed instance summary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of managed instances.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_NAME_SUMMARY_T Type

A simple representation of a package using its displayName and NEVRA parts.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Full package NEVRA name - this value should be unique.

`name`

(required) The name of the software package.

`l_type`

(optional) Type of the package.

`version`

(optional) Version of the installed package.

`architecture`

(optional) The architecture for which this package was built.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_NAME_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_package_name_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_T Type

An erratum associated with a managed instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The identifier of the erratum.

`advisory_type`

(required) The type of the erratum.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`time_issued`

(optional) The date and time the package was issued by a providing erratum (if available), as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`synopsis`

(optional) Summary description of the erratum.

`related_cves`

(optional) List of CVEs applicable to this erratum.

`packages`

(required) The list of Packages affected by this erratum.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_erratum_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_COLLECTION_T Type

Results of an errata search on a managed instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of errata.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_T Type

Description of managed instance group.

Syntax
```

```

Fields

Field Description

`id`

(required) The managed instance group OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the tenancy containing the managed instance group.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Details describing the managed instance group.

`time_created`

(optional) The time the managed instance group was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the managed instance group was last modified. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the managed instance group.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`os_family`

(optional) The operating system type of the instances in the managed instance group.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The CPU architecture of the instances in the managed instance group.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`software_source_ids`

(optional) The list of software sources that the managed instance group will use.

`software_sources`

(optional) The list of software sources that the managed instance group will use.

`managed_instance_ids`

(optional) The list of managed instances OCIDs attached to the managed instance group.

`managed_instance_count`

(optional) The number of Managed Instances in the managed instance group.

`pending_job_count`

(optional) The number of scheduled jobs pending against the managed instance group.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_SUMMARY_T Type

Summary information pertaining to a module stream profile provided by a software source.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the module that is available to be enabled on the managed instance group.

`software_source_id`

(optional) The OCID of the software source that provides this module.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_group_available_module_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_COLLECTION_T Type

Results of a module stream profile search. Contains both ModuleStreamProfileSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of module stream profile.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_SUMMARY_T Type

Summary information pertaining to an available package for a managed instance group.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name.

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID.

`l_type`

(required) Type of the package.

`version`

(required) Version of the installed package.

`architecture`

(optional) The architecture for which this package was built.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`software_sources`

(optional) List of software sources that provide the software package.

`is_latest`

(optional) Flag to return only latest package versions.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_group_available_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_COLLECTION_T Type

Results of an available package search on a managed instance group.

Syntax
```

```

Fields

Field Description

`items`

(required) List of available packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_SUMMARY_T Type

Summary of the managed instance group.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy containing the managed instance groups to list.

`display_name`

(optional) A user-friendly name for the managed instance group. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) managed instance group Description.

`managed_instance_count`

(optional) The number of Managed Instances in the managed instance group.

`time_created`

(optional) The time the managed instance group was created. An RFC3339 formatted datetime string.

`time_modified`

(optional) The time the managed instance group was last modified. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the managed instance group.

`os_family`

(optional) The operating system type of the instances in the managed instance group.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The CPU architecture of the instances in the managed instance group.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_COLLECTION_T Type

Results of a managed instance group search. Contains both managed instance group summary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of managed instance groups.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_SUMMARY_T Type

Summary information pertaining to an installed package on a managed instance group.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the package that is installed on the managed instance group.

`architecture`

(required) The architecture of the package that is installed on the managed instance group.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_group_installed_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_COLLECTION_T Type

Results of a search for installed packages on a managed instance group.

Syntax
```

```

Fields

Field Description

`items`

(required) List of installed packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_SUMMARY_T Type

Summary information pertaining to a module on a managed instance group.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the module that contains the stream.

`enabled_stream`

(optional) The name of the module that contains the stream.

`installed_profiles`

(optional) The list of installed profiles under the currently enabled module stream.

`software_source_id`

(optional) The OCID of the software source that provides this module stream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_group_module_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_COLLECTION_T Type

Results of a search for module streams on a managed instance group. Contains both ModuleStreamOnManagedInstanceGroupSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of module streams.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_SUMMARY_T Type

Summary information pertaining to a module on a managed instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The module name.

`enabled_stream`

(optional) The stream that is enabled in the module.

`installed_profiles`

(optional) List of installed profiles in the enabled stream of the module.

`active_streams`

(optional) List of streams that are active in the module.

`disabled_streams`

(optional) List of streams that are disabled in the module.

`software_source_id`

(optional) The OCID of the software source that provides this module and the associated streams.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_managed_instance_module_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_COLLECTION_T Type

Results of a search for module streams on a managed instance. Contains both ManagedInstanceModuleSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of module streams.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SYNC_STATUS_T Type

Status summary of all repos

Syntax
```

```

Fields

Field Description

`unsynced`

(required) Total of mirrors in 'failed' state

`queued`

(required) Total of mirrors in 'queued' state

`syncing`

(required) Total of mirrors in 'syncing' state

`synced`

(required) Total of mirrors in 'synced' state

`failed`

(required) Total of mirrors in 'failed' state

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROXY_CONFIGURATION_T Type

Information for a proxy configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) To enable or disable the proxy (default true)

`hosts`

(optional) List of hosts

`port`

(optional) Port that the proxy will use

`forward`

(optional) URL that the proxy will forward to

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_CONFIGURATION_T Type

Information for a mirror configuration

Syntax
```

```

Fields

Field Description

`directory`

(required) Directory for the mirroring

`port`

(required) Default port for the mirror

`sslport`

(required) Default sslport for the mirror

`sslcert`

(optional) Local path for the sslcert

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_T Type

Detailed information about an ManagementStation config

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the ManagementStation config

`managed_instance_id`

(optional) OCID for the Instance associated with the Management Station.

`compartment_id`

(required) The OCID of the tenancy containing the Management Station.

`scheduled_job_id`

(optional) OCID of the Scheduled Job for mirror sync

`profile_id`

(optional) OCID of the Profile associated with the Station

`display_name`

(required) ManagementStation name

`description`

(optional) Details describing the ManagementStation config.

`hostname`

(required) Name of the host

`overall_state`

(optional) Current state of the mirroring

Allowed values are: 'NORMAL', 'REGISTRATIONERROR', 'SYNCING', 'SYNCFAILED', 'WARNING', 'ERROR', 'UNAVAILABLE'

`overall_percentage`

(optional) A decimal number representing the completeness percentage

`mirror_capacity`

(optional) A decimal number representing the mirror capacity

`total_mirrors`

(optional) A decimal number representing the total of repos

`mirror_sync_status`

(optional)

`proxy`

(required)

`mirror`

(required)

`lifecycle_state`

(optional) The current state of the Management Station config.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_SUMMARY_T Type

Summary of the Management Station.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the Management Station

`managed_instance_id`

(optional) OCID for the Instance associated with the Management Station

`compartment_id`

(required) The OCID of the tenancy containing the Management Station.

`profile_id`

(optional) OCID of the Registration Profile associated with the Management Station

`scheduled_job_id`

(optional) OCID of the Scheduled Job for mirror sync

`time_next_execution`

(optional) the time/date of the next scheduled execution of the Scheduled Job

`display_name`

(required) ManagementStation name

`description`

(optional) Details describing the Management Station config.

`hostname`

(required) Name of the host

`overall_state`

(optional) Current state of the mirroring

Allowed values are: 'NORMAL', 'REGISTRATIONERROR', 'SYNCING', 'SYNCFAILED', 'WARNING', 'ERROR', 'UNAVAILABLE'

`overall_percentage`

(optional) A decimal number representing the completeness percentage

`mirror_capacity`

(optional) A decimal number representing the mirror capacity

`lifecycle_state`

(optional) The current state of the Management Station config.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_management_station_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_COLLECTION_T Type

Results of a managementstation search. Contains boh ManagementStationSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of managementStations.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_DETAILS_T Type

The config details of the management stations to be configured for a managed instance.

Syntax
```

```

Fields

Field Description

`primary_management_station_id`

(required) The OCID of a management station to be used as the preferred primary.

`secondary_management_station_id`

(optional) The OCID of a management station to be used as the preferred secondary.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SUMMARY_T Type

Summary of a Mirror

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of a software source

`display_name`

(optional) Display name of the mirror

`l_type`

(optional) Type of the mirror

Allowed values are: 'CUSTOM', 'VENDOR', 'VERSIONED'

`os_family`

(optional) The OS family the Software Source belongs to

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The architecture type supported by the Software Source

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`state`

(required) Current state of the mirror

Allowed values are: 'UNSYNCED', 'QUEUED', 'SYNCING', 'SYNCED', 'FAILED'

`percentage`

(required) A decimal number representing the completness percentage

`time_last_synced`

(required) Timestamp of the last time the mirror was sync

`log`

(required) The current log from the management station plugin.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_mirror_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRRORS_COLLECTION_T Type

List of mirrors associated with a Management Station

Syntax
```

```

Fields

Field Description

`items`

(required) List of mirrors

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SUMMARY_T Type

Summary information pertaining to a module provided by a software source.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the module.

`streams`

(optional) List of stream names.

`software_source_id`

(required) The software source that provides the module.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_COLLECTION_T Type

Results of a Module search. Contains module summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Modules.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SPEC_DETAILS_T Type

Details about a specific appstream module.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the module.

`stream`

(optional) The stream of the module.

`profile`

(optional) The module profile to be used.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_T Type

A module stream provided by a software source.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream.

`name`

(required) The name of the stream.

`is_default`

(optional) Indicates if this stream is the default for its module.

`software_source_id`

(optional) The OCID of the software source that provides this module stream.

`arch_type`

(optional) The architecture for which the packages in this module stream were built.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`description`

(optional) A description of the contents of the module stream.

`profiles`

(optional) A list of profiles that are part of the stream. Each element in the list is the name of a profile. The name is suitable to use as an argument to other OS Management Hub APIs that interact directly with module stream profiles. However, it is not URL encoded.

`packages`

(optional) A list of packages that are contained by the stream. Each element in the list is the name of a package. The name is suitable to use as an argument to other OS Management Hub APIs that interact directly with packages.

`is_latest`

(optional) Indicates whether this module stream is the latest.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_SUMMARY_T Type

Summary information pertaining to a module stream provided by a software source.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the stream.

`module_name`

(required) The name of the module that contains the stream.

`profiles`

(required) List of profiles in the stream.

`is_latest`

(optional) Indicates whether this module stream is the latest.

`software_source_id`

(optional) The software source id for the the module stream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_stream_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_COLLECTION_T Type

Results of a ModuleStream search. Contains both ModuleStreamSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ModuleStream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_BODY_T Type

The details of the module stream to be enabled/disabled on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_T Type

A module stream profile provided by a software source.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream profile.

`stream_name`

(required) The name of the stream that contains the profile.

`name`

(required) The name of the profile.

`is_default`

(optional) Indicates if this profile is the default for its module stream.

`description`

(optional) A description of the contents of the module stream profile.

`packages`

(required) A list of packages that constitute the profile. Each element in the list is the name of a package. The name is suitable to use as an argument to other OS Management Hub APIs that interact directly with packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_SUMMARY_T Type

Summary information pertaining to a module stream profile provided by a software source.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream profile.

`stream_name`

(required) The name of the stream that contains the profile.

`name`

(required) The name of the profile.

`is_default`

(optional) Indicates if this profile is the default for its module stream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_stream_profile_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_COLLECTION_T Type

Results of a ModuleStreamProfile search. Contains both ModuleStreamProfileSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ModuleStreamProfile.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_BODY_T Type

The details of the module stream profile to be installed/removed on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`profile_name`

(optional) The name of a profile of the specified module stream.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_T Type

Yum/DNF package group, category or environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Package group identifier.

`name`

(required) Package group name.

`repositories`

(optional) the IDs of the package group's repositories.

`description`

(optional) description of the package group.

`is_user_visible`

(optional) Indicates if this package group is visible by users.

`is_default`

(optional) Indicates if this package group is the default.

`group_type`

(optional) Indicates if this is a group, category or environment.

Allowed values are: 'GROUP', 'ENVIRONMENT', 'CATEGORY'

`display_order`

(optional) Indicates the order to display category or environment.

`packages`

(required) The list of packages in the package group.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_SUMMARY_T Type

Yum/DNF package group that associated with a software source.

Syntax
```

```

Fields

Field Description

`id`

(required) Package group identifier.

`name`

(required) Package group name.

`description`

(optional) description of the package group.

`is_user_visible`

(optional) Indicates if this package group is visible by users.

`is_default`

(optional) Indicates if this package group is the default.

`repositories`

(optional) the IDs of the package group's repositories.

`group_type`

(optional) Indicates if this is a group, category or environment.

`display_order`

(optional) Indicates the order to display category or environment.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_package_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_COLLECTION_T Type

Results of a package group search. Contains both package group summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of package groups.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_SUMMARY_T Type

Summary of the registration profile.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the profile that is immutable on creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) The description of the registration profile.

`compartment_id`

(required) The OCID of the tenancy containing the registration profile.

`management_station_id`

(optional) The OCID of the management station.

`profile_type`

(optional) The type of registration profile. Either SOFTWARESOURCE, GROUP or LIFECYCLE.

Allowed values are: 'SOFTWARESOURCE', 'GROUP', 'LIFECYCLE', 'STATION'

`vendor_name`

(optional) The software source vendor name.

Allowed values are: 'ORACLE'

`os_family`

(optional) The operating system family.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) The architecture type.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`time_created`

(optional) The time the the Onboarding was created. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the registration profile.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_profile_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_COLLECTION_T Type

Results of a registration profile search. Contains both registration profile summary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of registration profiles.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROMOTE_SOFTWARE_SOURCE_TO_LIFECYCLE_STAGE_DETAILS_T Type

A versioned custom software source OCID (softwareSourceId) is required when promoting software source content to lifecycle stage rank one. Software source content must be promoted to lifecycle stage rank one before being eligible for promotion to subsequent lifecycle stages, else an error is returned. Software source content is expected to be promoted in order starting with lifecycle stage rank one, followed by rank two, then rank three and so on. When promoting software source content to lifecycle stage rank two, three, four or five, softwareSourceId is optional. If a softwareSourceId is provided for a lifecycle stage between two and five, the system validates that the softwareSourceId is already promoted to the previous lifecycle stage. If the softwareSourceId from the previous lifecycle stage does not match the provided softwareSourceId an error returns. If a softwareSourceId is not provided for a lifecycle stage between two and five, the system promotes the softwareSourceId from the previous lifecycle stage. If the previous lifecycle stage has no SourceSource content an error returns.

Syntax
```

```

Fields

Field Description

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_DETAILS_T Type

The details of the module stream profile to be removed on a managed instance.

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`profile_name`

(optional) The name of a profile of the specified module stream.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The work request details for the module stream profile operation on the managed instance group.

Syntax
```

```

Fields

Field Description

`module_name`

(optional) The name of a module.

`stream_name`

(optional) The name of a stream of the specified module.

`profile_name`

(optional) The name of a profile of the specified module stream.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_DETAILS_T Type

The details about the software packages to be removed.

Syntax
```

```

Fields

Field Description

`package_names`

(required) The list of package names.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The names of the packages to be removed from the managed instance group.

Syntax
```

```

Fields

Field Description

`package_names`

(optional) The list of package names.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_T Type

Detailed information about a scheduled job.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the scheduled job.

`display_name`

(required) Scheduled job name.

`compartment_id`

(required) The OCID of the compartment containing the scheduled job.

`description`

(optional) Details describing the scheduled job.

`schedule_type`

(required) The type of scheduling this scheduled job follows.

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(required) The time of the next execution of this scheduled job.

`time_last_execution`

(optional) The time of the last execution of this scheduled job.

`recurring_rule`

(optional) The recurring rule for a RECURRING scheduled job.

`managed_instance_ids`

(optional) The list of managed instance OCIDs this scheduled job operates on (mutually exclusive with managedInstanceGroupIds, managedCompartmentIds and lifecycleStageIds).

`managed_instance_group_ids`

(optional) The list of managed instance group OCIDs this scheduled job operates on (mutually exclusive with managedInstances, managedCompartmentIds and lifecycleStageIds).

`managed_compartment_ids`

(optional) The list of target compartment OCIDs if this scheduled job operates on a compartment level (mutually exclusive with managedInstances, managedInstanceGroupIds and lifecycleStageIds).

`lifecycle_stage_ids`

(optional) The list of target lifecycle stage OCIDs if this scheduled job operates on lifecycle stages (mutually exclusive with managedInstances, managedInstanceGroupIds and managedCompartmentIds).

`is_subcompartment_included`

(optional) Whether to create jobs for all compartments in the tenancy when managedCompartmentIds specifies the tenancy OCID.

`operations`

(required) The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).

`work_request_ids`

(optional) The list of work request OCIDs associated with this scheduled job.

`time_created`

(required) The time this scheduled job was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this scheduled job was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the scheduled job.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`is_restricted`

(optional) true, if the schedule job has its update/deletion capabilities restricted. (Used to track scheduled job for management station syncing).

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_SUMMARY_T Type

Summary of the scheduled job.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the scheduled job.

`display_name`

(required) Scheduled job name.

`compartment_id`

(required) The OCID of the compartment containing the scheduled job.

`schedule_type`

(required) The type of scheduling this scheduled job follows.

Allowed values are: 'ONETIME', 'RECURRING'

`time_created`

(required) The time this scheduled job was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time this scheduled job was updated. An RFC3339 formatted datetime string.

`time_next_execution`

(required) The time/date of the next scheduled execution of this scheduled job.

`time_last_execution`

(optional) The time/date of the last execution of this scheduled job.

`managed_instance_ids`

(optional) The list of managed instance OCIDs this scheduled job operates on (mutually exclusive with managedInstanceGroupIds, managedCompartmentIds and lifecycleStageIds).

`managed_instance_group_ids`

(optional) The list of managed instance group OCIDs this scheduled job operates on (mutually exclusive with managedInstances, managedCompartmentIds and lifecycleStageIds).

`managed_compartment_ids`

(optional) The list of target compartment OCIDs if this scheduled job operates on a compartment level (mutually exclusive with managedInstances, managedInstanceGroupIds and lifecycleStageIds).

`lifecycle_stage_ids`

(optional) The list of target lifecycle stage OCIDs if this scheduled job operates on lifecycle stages (mutually exclusive with managedInstances, managedInstanceGroupIds and managedCompartmentIds).

`operations`

(required) The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).

`lifecycle_state`

(required) The current state of the scheduled job.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_restricted`

(optional) true, if the schedule job has its update/deletion capabilities restricted. (Used to track scheduled job for management station syncing).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_scheduled_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_COLLECTION_T Type

Results of a scheduled job search. Contains boh ScheduledJobSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of scheduled jobs.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_MODULE_STREAMS_DETAILS_T Type

Contains a list of software sources to get the combined list of module streams from all of those software sources.

Syntax
```

```

Fields

Field Description

`software_source_ids`

(required) List of software source OCIDs.

`sort_order`

(optional) The sort order.

Allowed values are: 'ASC', 'DESC'

`module_name`

(optional) The name of a module.

`sort_by`

(optional) The field to sort by.

Allowed values are: 'MODULENAME'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_MODULES_DETAILS_T Type

Contains a list of software sources to get the combined list of modules from all of those software sources.

Syntax
```

```

Fields

Field Description

`software_source_ids`

(required) List of software source OCIDs.

`sort_order`

(optional) The sort order.

Allowed values are: 'ASC', 'DESC'

`name`

(optional) The name of a module.

`name_contains`

(optional) filters results, allowing only those with a name which contains the string.

`sort_by`

(optional) The field to sort by.

Allowed values are: 'NAME'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_PACKAGE_GROUPS_DETAILS_T Type

Contains a list of software sources to get the list of associated package groups.

Syntax
```

```

Fields

Field Description

`software_source_ids`

(required) List of software source OCIDs.

`sort_order`

(optional) The sort order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by.

Allowed values are: 'NAME'

`name_contains`

(optional) filters results, allowing only those with a Name which contains the string.

`group_type`

(optional) Indicates if this is a group, category or environment.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_DEPENDENCY_T Type

A dependency for a software package.

Syntax
```

```

Fields

Field Description

`dependency`

(optional) The software package's dependency.

`dependency_type`

(optional) The type of the dependency.

`dependency_modifier`

(optional) The modifier for the dependency.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_FILE_T Type

A file associated with a package.

Syntax
```

```

Fields

Field Description

`path`

(optional) File path.

`l_type`

(optional) Type of the file.

`time_modified`

(optional) The date and time of the last modification to this file, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`checksum`

(optional) Checksum of the file.

`checksum_type`

(optional) Type of the checksum.

`size_in_bytes`

(optional) Size of the file in bytes.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_DEPENDENCY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_package_dependency_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_FILE_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_package_file_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_T Type

The details for a software package.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name.

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID.

`l_type`

(required) Type of the package.

`version`

(required) Version of the package.

`architecture`

(optional) The architecture for which this software was built

`last_modified_date`

(optional) Date of the last update to the package.

`checksum`

(optional) Checksum of the package.

`checksum_type`

(optional) Type of the checksum.

`description`

(optional) Description of the package.

`size_in_bytes`

(optional) Size of the package in bytes.

`dependencies`

(optional) List of dependencies for the software package.

`files`

(optional) List of files for the software package.

`software_sources`

(optional) List of software sources that provide the software package.

`is_latest`

(optional) Indicates whether this package is the latest version.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_COLLECTION_T Type

Results of a software package search. Contains boh software package summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of software packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGES_DETAILS_T Type

The details about the software packages to be installed/removed/updated.

Syntax
```

```

Fields

Field Description

`package_names`

(required) The list of package names.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_COLLECTION_T Type

Results of a SoftwareSource search. Contains boh SoftwareSourceSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of SoftwareSources.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_PROFILE_T Type

Definition of a registration profile of type SoftwareSource.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_software_source_profile_t`is a subtype of the`dbms_cloud_oci_os_management_hub_profile_t`type.

Fields

Field Description

`software_sources`

(required) The list of software sources that the registration profile will use.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_SUMMARY_T Type

Software vendor name, list of osFamily and archType.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the vendor providing the software source.

Allowed values are: 'ORACLE'

`os_families`

(required) List of corresponding osFamilies.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_types`

(required) List of corresponding archTypes.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_software_source_vendor_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_COLLECTION_T Type

Results of a SoftwareSourceVendor search. Contains boh SoftwareSourceVendorSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of SoftwareSourceVendor.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCES_DETAILS_T Type

The details about the software sources to be attached/detached.

Syntax
```

```

Fields

Field Description

`software_sources`

(required) The list of software source OCIDs to be attached/detached.

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_STATION_PROFILE_T Type

Definition of a registration profile of type STATION.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_station_profile_t`is a subtype of the`dbms_cloud_oci_os_management_hub_profile_t`type.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SWITCH_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type

The details of the module stream to be version switched on a managed instance.

Syntax
```

```

Fields

Field Description

`work_request_details`

(optional)

`module_name`

(required) The name of a module.

`stream_name`

(required) The name of a stream of the specified module.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SYNCHRONIZE_MIRRORS_DETAILS_T Type

Details for syncing selected mirrors

Syntax
```

```

Fields

Field Description

`software_source_list`

(required) List of Software Source OCIDs to synchronize

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_SUMMARY_T Type

A software package available for install on a managed instance.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_updatable_package_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_package_summary_t`type.

Fields

Field Description

`installed_version`

(optional) The version of this upgradable package already installed on the instance.

`update_type`

(required) The classification of this update.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER'

`errata`

(optional) List of errata containing this update.

`related_cves`

(optional) List of CVEs applicable to this erratum.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_updatable_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_COLLECTION_T Type

Results of an updatable package search on a managed instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of updatable packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The work request details for the update operation on the managed instance group.

Syntax
```

```

Fields

Field Description

`update_types`

(optional) The type of updates to be applied.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE_KERNEL', 'KSPLICE_USERSPACE', 'ALL'

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCES_IN_COMPARTMENT_DETAILS_T Type

The details about the package types to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment being targeted by this operation.

`update_types`

(optional) The type of updates to be applied.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE_KERNEL', 'KSPLICE_USERSPACE', 'ALL'

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_SOFTWARE_SOURCE_DETAILS_T Type

Information for updating a software source.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the tenancy containing the software source.

`display_name`

(optional) User friendly name for the software source.

`description`

(optional) Information specified by the user about the software source.

`software_source_type`

(optional) Type of the software source.

Allowed values are: 'VENDOR', 'CUSTOM', 'VERSIONED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type

Information for updating a custom or software source.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_update_custom_software_source_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_update_software_source_details_t`type.

Fields

Field Description

`vendor_software_sources`

(optional) List of vendor software sources.

`custom_software_source_filter`

(optional)

`is_automatically_updated`

(optional) Indicates whether service should automatically update the custom software source for the user.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_STAGE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`id`

(required) The lifecycle stage OCID that is immutable on creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_STAGE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_update_lifecycle_stage_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_ENVIRONMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) User specified information about the lifecycle environment. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`stages`

(optional) The list of lifecycle stages to be updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGED_INSTANCE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`primary_management_station_id`

(optional) The OCID of a management station to be used as the preferred primary.

`secondary_management_station_id`

(optional) The OCID of a management station to be used as the preferred secondary.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the managed instance group job. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) User specified information about the managed instance group. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PROXY_CONFIGURATION_DETAILS_T Type

Information for updating a proxy configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) To enable or disable the proxy (default true)

`hosts`

(optional) List of hosts

`port`

(optional) Port that the proxy will use

`forward`

(optional) URL that the proxy will forward to

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MIRROR_CONFIGURATION_DETAILS_T Type

Information for updating a mirror configuration

Syntax
```

```

Fields

Field Description

`directory`

(required) Directory for the mirroring

`port`

(required) Default port for the mirror

`sslport`

(required) Default sslport for the mirror

`sslcert`

(optional) Local path for the sslcert

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGEMENT_STATION_DETAILS_T Type

Information for updating an ManagementStation

Syntax
```

```

Fields

Field Description

`display_name`

(optional) ManagementStation name

`description`

(optional) Details describing the ManagementStation config.

`hostname`

(optional) Name of the host

`proxy`

(optional)

`mirror`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PACKAGES_ON_MANAGED_INSTANCE_DETAILS_T Type

The details about the software packages to be updated.

Syntax
```

```

Fields

Field Description

`package_names`

(optional) The list of package names.

`update_types`

(optional) The type of updates to be applied.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE_KERNEL', 'KSPLICE_USERSPACE', 'ALL'

`work_request_details`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PROFILE_DETAILS_T Type

Information for updating a registration profile

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Details describing the scheduled job.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_SCHEDULED_JOB_DETAILS_T Type

Information for updating a scheduled job.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Scheduled job name.

`description`

(optional) Details describing the scheduled job.

`schedule_type`

(optional) The type of scheduling this scheduled job follows.

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(optional) The desired time for the next execution of this scheduled job.

`recurring_rule`

(optional) The recurring rule for a recurring scheduled job.

`operations`

(optional) The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_VENDOR_SOFTWARE_SOURCE_DETAILS_T Type

Information for updating a vendor source. Tags only.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_update_vendor_software_source_details_t`is a subtype of the`dbms_cloud_oci_os_management_hub_update_software_source_details_t`type.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_WORK_REQUEST_DETAILS_T Type

Detail information for updating a work request.

Syntax
```

```

Fields

Field Description

`status`

(required) status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`percent_complete`

(optional) The percentage complete of the operation tracked by this work request.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`description`

(optional) A short description about the work request.

`display_name`

(optional) A short display for about the work request.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VENDOR_SOFTWARE_SOURCE_T Type

A vendor software source contains a collection of packages.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_vendor_software_source_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_t`type.

Fields

Field Description

`vendor_name`

(required) Name of the vendor providing the software source.

Allowed values are: 'ORACLE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VENDOR_SOFTWARE_SOURCE_SUMMARY_T Type

A vendor software source summary summarizes a vendor software source.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_vendor_software_source_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_summary_t`type.

Fields

Field Description

`vendor_name`

(required) Name of the vendor providing the software source.

Allowed values are: 'ORACLE'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VERSIONED_CUSTOM_SOFTWARE_SOURCE_T Type

An immutable custom software source that is assigned a version and contains a custom collection of packages.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_versioned_custom_software_source_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

`custom_software_source_filter`

(optional)

`software_source_version`

(required) The version to assign to this custom software source.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VERSIONED_CUSTOM_SOFTWARE_SOURCE_SUMMARY_T Type

An immutable custom software source that is assigned a version and contains a custom collection of packages.

Syntax
```

```

`dbms_cloud_oci_os_management_hub_versioned_custom_software_source_summary_t`is a subtype of the`dbms_cloud_oci_os_management_hub_software_source_summary_t`type.

Fields

Field Description

`vendor_software_sources`

(required) List of vendor software sources.

`software_source_version`

(required) The version to assign to this custom software source.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that the work request affects.

Allowed values are: 'INSTANCE', 'GROUP', 'COMPARTMENT', 'LIFECYCLE_ENVIRONMENT', 'SOFTWARE_SOURCE'

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

`name`

(optional) The name of the resource. Not all resources will have a name specified.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_MANAGEMENT_STATION_DETAILS_T Type

Details about management station actions.

Syntax
```

```

Fields

Field Description

`management_station_version`

(optional) Target version to update the management station software.

`config`

(optional) Target config needed for set management station config.

`software_source_ids`

(optional) Optional list for mirrors to sync.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SPEC_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_module_spec_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_T Type

Describes a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'INSTALL_PACKAGES', 'REMOVE_PACKAGES', 'UPDATE_PACKAGES', 'UPDATE_ALL_PACKAGES', 'UPDATE_SECURITY', 'UPDATE_BUGFIX', 'UPDATE_ENHANCEMENT', 'UPDATE_OTHER', 'UPDATE_KSPLICE_KERNEL', 'UPDATE_KSPLICE_USERSPACE', 'ENABLE_MODULE_STREAMS', 'DISABLE_MODULE_STREAMS', 'SWITCH_MODULE_STREAM', 'INSTALL_MODULE_PROFILES', 'REMOVE_MODULE_PROFILES', 'SET_SOFTWARE_SOURCES', 'LIST_PACKAGES', 'SET_MANAGEMENT_STATION_CONFIG', 'SYNC_MANAGEMENT_STATION_MIRROR', 'UPDATE_MANAGEMENT_STATION_SOFTWARE', 'UPDATE', 'MODULE_ACTIONS', 'LIFECYCLE_PROMOTION', 'CREATE_SOFTWARE_SOURCE', 'UPDATE_SOFTWARE_SOURCE'

`status`

(required) Status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`description`

(optional) A short description about the work request.

`display_name`

(optional) A short display name for the work request.

`message`

(optional) A progress or error message, if there is any.

`parent_id`

(optional) The OCID of the parent work request, if there is any.

`children_id`

(optional) The list of OCIDs for the child work requests.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource it affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The list of OCIDs for the resources affected by the work request.

`package_names`

(optional) A list of package names to be installed/updated/removed.

`module_specs`

(optional) The list of appstream modules being operated on.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_created`

(required) The date and time the work request was created - as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) The date and time the work request was created - as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the work request was started - as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the work request was finished - as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`initiator_id`

(optional) The OCID of the resource that initiated the work request.

`management_station`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm).

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a work request error search. Contains both work request error items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request error objects.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a work request log search. Contains both work request log items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request log entries.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_T Type

The summary of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'INSTALL_PACKAGES', 'REMOVE_PACKAGES', 'UPDATE_PACKAGES', 'UPDATE_ALL_PACKAGES', 'UPDATE_SECURITY', 'UPDATE_BUGFIX', 'UPDATE_ENHANCEMENT', 'UPDATE_OTHER', 'UPDATE_KSPLICE_KERNEL', 'UPDATE_KSPLICE_USERSPACE', 'ENABLE_MODULE_STREAMS', 'DISABLE_MODULE_STREAMS', 'SWITCH_MODULE_STREAM', 'INSTALL_MODULE_PROFILES', 'REMOVE_MODULE_PROFILES', 'SET_SOFTWARE_SOURCES', 'LIST_PACKAGES', 'SET_MANAGEMENT_STATION_CONFIG', 'SYNC_MANAGEMENT_STATION_MIRROR', 'UPDATE_MANAGEMENT_STATION_SOFTWARE', 'UPDATE', 'MODULE_ACTIONS', 'LIFECYCLE_PROMOTION', 'CREATE_SOFTWARE_SOURCE', 'UPDATE_SOFTWARE_SOURCE'

`status`

(required) Status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`description`

(optional) A short description about the work request.

`display_name`

(optional) A short display name for the work request.

`message`

(optional) A progress or error message, if there is any.

`parent_id`

(optional) The OCID of the parent work request.

`children_id`

(optional) The list of OCIDs for the child work requests.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`percent_complete`

(optional) The percentage complete of the operation tracked by this work request.

`time_created`

(required) The date and time the request was created - as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_hub_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a work request search. Contains both work request items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request summary objects.

- [OS Management Hub Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A0904281-4807-42B3-996F-C3A6B35024EB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-5F3580E9-62D6-4D00-937F-87B81FF486EC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6E03EA2A-5F77-4BD8-B8FD-5ADB358AF882)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B3461C8E-B67D-4AA3-859D-94C1773E6C0A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_MANAGED_INSTANCES_TO_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-80306AEE-C022-455D-8C97-72A0800C28BD)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_MANAGED_INSTANCES_TO_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-770F99BE-FDDB-4F04-9EB4-D705A8CF714B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F559419E-3966-41C1-AB09-84F12483A797)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ATTACH_SOFTWARE_SOURCES_TO_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-602BF80C-8000-4EA7-A636-3EBE0C0ED365)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-57D84699-8B8A-428D-BD18-3F2BB0826506)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-662E8461-ED32-4484-A06C-575704072468)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-0158885E-A212-4648-8407-A71133E38A4F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-167E322C-63CF-4856-A840-F598909A1E6F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-40722C7B-D9AE-457F-BF29-4547C638A046)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EAED2BBA-7D79-4CAF-A048-9979E9B443EC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-CA6D964C-1388-4FF6-91B2-C29BAD36CE67)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-341E94F3-A5FA-4240-9C91-355E07E86942)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_AVAILABLE_SOFTWARE_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-CAF34A39-AD09-49A9-B9E8-262836503C93)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_AVAILABILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4222E9E9-CFAA-42E6-8302-8CB20BB52CBC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_AVAILABILITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E11AC9F2-5450-416D-8384-9894A22D3E6E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CHANGE_AVAILABILITY_OF_SOFTWARE_SOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-98D85914-F122-4772-8766-CF9DF7758CD8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A6D7716E-7C85-4E7D-A9A7-D6388FDC472D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-648D8F43-5E6F-4FAE-861B-378FE1BDDDB5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-22B17596-EDDF-4B32-AE68-ADD95481428D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-33A74953-2C94-4BAD-B9F9-6C5EC9DC8254)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-26063172-DF63-455D-ABD2-6FD7CB8F7654)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6F4185D8-D22E-4F84-8BED-4BA387A2ED9A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-64115AD0-C309-4E1F-9B79-FA66E6972D68)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-CD4187B3-0306-4919-A36A-1DD57606B2B3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-379F3F96-DD6B-42DF-84EE-24324B315922)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ID_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6D303EAD-59A7-4AED-BCE7-B18F79D93F00)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-0CCB0B4B-AF47-436E-9433-ABFC14B248E2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_ENTITLEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6E13DEBB-B563-47DA-B388-A3D34DBD809D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-3026F503-912A-4F1E-82E5-17CD20668583)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_GROUP_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D4643427-EF3F-43AB-8434-937E739185C2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-745728F4-87D2-4DC1-8A5F-62B4D8F66BBF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_STAGE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2055F636-D549-466E-A100-8C882970F8DB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-07B6EE5F-AF26-4AD5-A0CB-89D80ECC696B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_LIFECYCLE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-1CB0EB72-8F9B-49E3-B26F-B116D396AEB4)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-16FB8F81-6AF2-42CB-BF66-976420764C9A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_PROXY_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2D0321D4-B1D4-43FF-8F83-3FA47D473FDF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MIRROR_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B0D62842-503D-470D-B044-2BF4890A54FE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_MANAGEMENT_STATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-08EB1308-028F-402A-A99C-48892224C38D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D2F23A20-C4DE-48A5-83ED-6F49D7884447)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-32D8DF31-F17F-4A02-B7DC-1A40F02ADF5A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E84E9E3A-758A-47BF-95C7-38850D1E893C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-21F0FA16-B281-479E-A82F-1FB7AB2CD963)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_IN_SCHEDULED_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D13B1D7D-AACC-4D33-9852-27B79488A3D6)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F57AF6A8-3238-44F6-A292-45C61F1EFF15)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E795C407-FD20-4D0A-8188-74C7F341B808)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SCHEDULED_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D82A4405-07D4-40CD-BDAB-3E892B91E362)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_SOFTWARE_SOURCE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A5110A2C-AA64-4190-AECF-F73A18942166)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_STATION_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-72C51C4A-5F61-413F-B1DF-7D7D1BB065E9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CREATE_VERSIONED_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BA6B8598-73DE-4F71-A43C-69025A995A0F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DBF68D5B-60D0-4DF1-8BE3-271AF3597354)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-80AD0DB8-DDF8-474D-AA94-B0F17987FB0B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-635DD1B8-5B8F-428D-8952-E0E3D5CB4254)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_CUSTOM_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-ACF8FF26-D2F0-44FE-8C15-9580FED3B375)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_MANAGED_INSTANCES_FROM_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C3273EE1-D49A-4C10-9F0C-4167D61371E1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_MANAGED_INSTANCES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-57A0B32F-FF22-4EC4-A10E-1F9E012A6D24)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2C263985-CF32-41F1-92F6-F2347619B8E9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DETACH_SOFTWARE_SOURCES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E32D8845-94F1-4033-801B-E8697D08F827)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-12AF1EB5-F808-4F8A-868F-D57869458D19)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_DISABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-5C5A766D-BBD2-4D55-A56E-1A0CCD79B7AB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E66ED4FF-7911-49CB-B010-46F21913CE63)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENABLE_MODULE_STREAM_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B3B2F3AB-F4EC-41B7-80A3-3DA3B7E068D1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-90B9498C-5102-4D89-9D8D-985CA55F1BE7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2C09BE69-B6E5-412C-99A7-790BC397C53D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ENTITLEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-16DCD86F-2EFD-4E42-8AC1-8F466B2F56DE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D727AF54-AB77-46F9-8BFC-2D657587B71C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-470A1AEA-5320-486D-A181-9FE8712AF79D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-8A4BD4C3-D632-41E1-BBB2-7A0974D9A980)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-328AB6C5-DB74-43E8-AF8C-6D6FB7AE2EB6)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DD9D0A3C-D39C-44D9-B832-7201252FF63B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERRATUM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BC195FCB-B3E4-428A-BA5A-F77097170C33)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-5C2FA6CD-ACA0-4956-A7C4-60232A258077)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7E64F971-1DCA-4493-8D3B-DF43771A3644)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E44B8DD9-E384-4C77-8371-09EE8D95B9F8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_GROUP_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E91BDB37-6F1B-4382-978E-A74ECFAB03CE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E68D7D9F-AEDD-4984-8AE0-4975C0ACF7FD)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EEEBADDE-85B9-463D-B0F1-95067DC6133F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_PACKAGES_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2F091258-B316-4651-B140-C86460E4DF5B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-61A29970-45EA-4C13-8EF2-547542080F16)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-348D7DDF-F980-4918-AC04-5FB9537C11B7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-22544F82-A04B-47E0-873E-7A61D23E5BE1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_INSTALLED_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2D5FDFBB-9E2D-48BA-A777-E10CC5D4E7DC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C1395545-F390-4048-BCC8-2268600F2792)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E59E85DF-6276-44EA-B1A9-E11C835F9E65)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-66EC3B81-36CB-4762-BAE9-C4185092B443)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-3FE66770-1185-419F-AA96-E1D564431A49)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B8D95501-0F6B-4C66-B3B0-5FA72D145F19)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F3552704-C96D-40A1-A9B7-A06DDA401BBB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-9C353711-0AEF-4FE0-BAA3-90B0765C3630)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7955E60F-28B8-4D68-B6AC-77E586DE4058)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-39989D99-1AD8-428C-B44F-304D7E0020C6)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A989F07D-2720-45A4-8933-253C029EE87C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-8E1EB94B-BD7E-4FC9-A2AF-03EB8343D8AF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F4F1E7A4-0474-4D71-B3CB-4111C9741A66)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FE12063F-3BC8-4683-A7E3-0F0E106518D4)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_LIFECYCLE_STAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-137BC92F-F426-40A9-B2FB-0026037FB92E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FB941B42-BD50-4C77-8A10-DB1277132037)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-20ECCBBE-DC8E-41D0-A78B-39DAEB34FF2A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-61B0736B-DF20-4691-B09C-23E419FA7EA0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F0543036-0BB9-4E68-8A59-7493939E38EE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C16D92FA-AF01-4D49-9012-C7FAD2DAF46E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ANALYTIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-00895EE3-F985-4560-8121-88801CAA8973)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C5A523CA-4BA2-445B-8886-0478A262A658)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-52B03A39-B24E-4799-965F-6858632D3EDA)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B988766C-A4EB-4453-84EE-417D668F9920)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_NAME_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-044A213D-349F-43EE-B3AF-CE6D905A39E6)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_NAME_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E9437A7A-65FA-4C9F-9FFF-BAC7E4CA4936)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C3A3AF92-4861-4409-B61D-8CDC7AA56A30)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6511F145-BD15-4C24-86B9-2C19D9E862EE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_ERRATUM_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C812E53B-4FC1-4502-9572-6ABA0D7FB317)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-AC3E3987-FA53-43DB-91B5-4FFC2C7280A5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EFFADBD0-C794-4E5B-B690-C11557A0FE32)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EDD8D2CE-0CF1-491F-9BBE-783E2D5EEF75)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_MODULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-8B1B0A7D-B182-4E1A-87CA-4184F3265BEF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BAFF2A29-2BBA-4895-B38F-11BA7B2FE35D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7A06ACF3-6AA0-44EB-9D5D-E23A4563EEB7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_AVAILABLE_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-476BA637-049C-4F4E-B2A8-5599406C9A91)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E919A0CE-0712-4B21-A662-27B919AE6601)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E20E82A0-ABD0-4375-8BD6-7B40A274D0AC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B2D3C01D-9F0F-4D48-B5F9-380CD1456619)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F131EB71-9C4D-4BFB-9CC0-47E333475802)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FE7F1A1A-F72C-447E-868B-C96BDB41C2BC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_INSTALLED_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A292FE58-84BC-4038-BDFB-B848CEE75A63)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F6BD3254-216D-4B8C-B33A-41E8BEA5BC28)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-56D0878A-3B00-4763-83A1-D4BEB04A9577)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_GROUP_MODULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-3838D691-31ED-4B73-8503-09D6CDA29E70)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FBF0AD95-E5CB-411A-A7A1-54FA8FAA563F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2D9624E5-4B48-4F85-B05D-CE0D49195823)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGED_INSTANCE_MODULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-57ECF141-716A-484E-9E64-79DD62622843)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SYNC_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-8140B949-E4AC-4233-B43E-4C41079A3D2E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROXY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-1D65826B-E12A-44E3-ADC1-B82AFBD34DD7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-70A7E0AB-E617-437E-BC6A-94F900BDB37D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-82F65057-6CBB-4D49-8D65-2B55D630848D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7855F54A-19BC-4733-B46B-1B3BCDBA825D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A3EC8C37-3EAC-4CA2-9027-88BC38AEA84A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E52A9C90-457F-4690-8A8E-82CD51B20B42)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MANAGEMENT_STATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7BEE1744-B1E3-4E7A-BE67-9786FC09B958)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E73A52B4-15BF-4F39-BF9E-4B6D3F781F3B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRROR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B1650272-EE10-416F-84D3-2BD138A12A00)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MIRRORS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C424C5CA-8D03-41AA-B70B-09642B7ECF6F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FC1A7E1C-11DC-4B59-B378-FB0BD9788831)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-3F47A596-4E10-4F1C-94AD-3EEB544C6FB8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7005FCD9-FD9F-4503-88E2-B4FE0AF4A43E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SPEC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-991667A8-AF3A-4158-BA3C-3C0C6D5CA082)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F6577087-5F32-40EB-B8AF-C1EAB56A6193)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-47C307E7-1D0C-4112-BBCE-79EFD512ACA3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-216083C8-58D6-4850-9629-FFC0A4C67C52)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-0FF9AD4C-D8C0-4F6E-9483-B1FE25DA259B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_DETAILS_BODY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BC9B1D3D-A3DE-4DE7-9C17-BE0485670EF5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C9D1F561-BC1B-4C94-ACE1-8C188EBFA731)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-74B5D78B-CF37-4705-9E31-2B9A8467BAF1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-437A9908-6A85-4D7C-8E72-2AA5D32D16B1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4FF473D2-3A93-4370-9F75-285BAE447A25)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_STREAM_PROFILE_DETAILS_BODY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2CCA2779-24B0-4B64-A75D-1D0D60097CB7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-CC35F110-0726-40D7-B965-DDBC88831F43)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-09A24254-5228-4FAA-A918-F91E9422A12C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DE4AD67A-FCEA-4CEF-B460-EA2FBBF5AAF3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PACKAGE_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-50D69617-810E-417A-82E8-BC8C5ECA6B66)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EBCD562C-330C-4DAE-BA4B-63481F06B6A3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C7A81BD2-5C3B-4FA1-901B-095828375E4E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROFILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E6C057DA-B964-420D-9980-C5817E69E167)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_PROMOTE_SOFTWARE_SOURCE_TO_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-1C05508C-FF2A-41FF-B4FF-C87194E209AE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-390D4E72-6B86-41C1-9FFF-4C0DDDDF325A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_MODULE_STREAM_PROFILE_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-3957F9CE-5DD3-4D4E-8656-FBACC6B3A3F0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A2153BDD-2C28-497D-8569-E5C4A711CE01)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_REMOVE_PACKAGES_FROM_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-24800CB3-BF1F-4540-A56C-E32E145CAEF7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-328561E8-7FBC-4F1C-ACF8-CCEA339B943C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-9158DF9A-1955-489B-B90D-8EA60CF00072)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DDDE440C-B59E-4A6A-9FF2-200CACA0E7F7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SCHEDULED_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E5B454E9-D2BE-4699-BBCD-3EEA1D199E01)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_MODULE_STREAMS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-5600C05F-A4B5-4D63-8CDB-0A9CC33E4249)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_MODULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6D0E414A-BD5C-450F-A4E1-647CABCE7D6A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SEARCH_SOFTWARE_SOURCE_PACKAGE_GROUPS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-AB74EAA5-1E38-4328-A880-955C25C621A5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_DEPENDENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DEC9EC39-6E74-44C7-91DB-35F13EC3D0EB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-20B1670D-751D-4F9C-967D-1EA40E34D4B1)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_DEPENDENCY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D1029D7F-B2AB-498E-9758-9E5E0FAB2A26)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_FILE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EA36FF21-8A5A-42BF-B79A-52C39E337C14)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F34C7485-3143-4A31-822B-522E2BB2F2EF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4013D068-7EE5-449E-9579-9A3280BF689A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_PACKAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-F49A4CC6-7E9E-4202-8C0F-4A6AFE1A4BB4)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EEF1D705-093A-4482-A7D5-43280947BFB0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-8E343D25-7B3A-4164-B77D-A338BEC8ABE9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DE24E95D-BCC2-4444-B846-C9C9173A1885)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-90598A3A-9ADF-4A78-9F9C-ECC6D9A1B3A3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7B629F26-CEFC-4BE3-AA2B-7BD6059EB669)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCE_VENDOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C7958FB6-A402-4442-A3E2-C7339DD5B1AD)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SOFTWARE_SOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-680C0613-1910-44B9-9B58-9436DEF72DBF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_STATION_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4BC3A44D-F9CE-4EE5-9E7B-E5AF019388D3)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SWITCH_MODULE_STREAM_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-AC0BE09E-A85E-4515-9D3A-A206E91EB02B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_SYNCHRONIZE_MIRRORS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C8C2F99E-7026-416A-9DC4-925126CE2562)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-30F5CEBD-966D-43C2-A158-28F9D79A4F8C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-02519DF3-6B2A-4AE4-A065-9771BC2D16A9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATABLE_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4CE3EE6D-A132-429D-B419-FD14CAF4EA8C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C3B172CB-2AD1-4221-88CA-9C2D5661F9C5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_ALL_PACKAGES_ON_MANAGED_INSTANCES_IN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BC43CF11-A13A-40CE-8AFD-14C1E62F2E38)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-0C01AF9D-8E65-4D3E-BFF2-6278373EC338)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_CUSTOM_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-729C969D-9219-41E8-9715-2D993FA4070A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-0831DEB4-DED8-4B26-B274-29F63058EA13)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_STAGE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-10F775BE-9185-4A3A-BBA4-D84C0302FAD8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_LIFECYCLE_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E84FEA20-1322-45B6-AB9B-753B830E0F29)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-6D079CFA-DEBA-4E4A-9F5E-3AF3F850A674)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2A116B61-17CA-49C3-AC1F-E7AB83A31CFD)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PROXY_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-A0150AA7-A675-49E2-948D-B037AF8FAB6E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MIRROR_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-C4BEBECC-4E1E-410E-AEFC-BEFDAFCEF83B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_MANAGEMENT_STATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-9485DA0A-20A7-48C7-8C77-5B28FE53B358)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PACKAGES_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-088F20E1-26D8-4257-93C6-6A8DCF45E23D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-E823BA80-4F13-4EE4-AD48-7D30B7F44A68)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_SCHEDULED_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-955643C5-218D-4179-BE01-1D39A0E43437)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_VENDOR_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-5014E638-052A-411D-8D1B-7EB93BB7296A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_UPDATE_WORK_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DF25069F-8D00-4A6E-9125-0160542395B4)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VENDOR_SOFTWARE_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-EA4D258C-7F15-464C-8A74-F3CDC11977EB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VENDOR_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-BEA00645-616C-47BD-85C7-3456E3703C90)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VERSIONED_CUSTOM_SOFTWARE_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-551685D1-4DD0-4296-8196-391BAF71EB7A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_VERSIONED_CUSTOM_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-547597BD-C478-449F-AF08-E5FFEC39BC73)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B754D64D-09D5-441F-9A68-AC43FD5E64D6)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_MANAGEMENT_STATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-2D105DD5-3B26-40BF-AFE0-26A7F8375DC9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-B68D7E10-8243-4F97-BF7C-C122FDF98CA2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_MODULE_SPEC_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-01CEEF55-33A0-496B-9749-25815899E7EF)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-617D9EC2-7E1C-44EE-BC64-F71A6BE1B8E7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-7BD4DC3B-5F00-4A3B-9C88-9D549E58BD5D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-DF479F61-166C-4A56-A72F-6578CBCBB983)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-FD69807F-2C74-4340-A27D-672B2437BBBB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-4295AA90-E6AA-4FA2-9337-B4F844AE0838)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D1E6A706-C33A-4FEF-9F95-85C9B21A1D94)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-62CFAE13-B73B-438B-9314-3D1AE5035675)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-D433AFF5-6DB6-47B2-AACE-7CC2BC102E8B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-35CCC504-E593-466C-9A62-81212A37BB7E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_HUB_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_hub_t.html#ADSDK-GUID-1ABB18BC-F8E8-48F0-A398-00E19ED37694)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
