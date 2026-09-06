# OS Management Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#dcoc-content-body)

## OS Management Common Types

### DBMS_CLOUD_OCI_OS_MANAGEMENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ADD_PACKAGES_TO_SOFTWARE_SOURCE_DETAILS_T Type

List of software package names

Syntax
```

```

Fields

Field Description

`package_names`

(required) the list of package names

### DBMS_CLOUD_OCI_OS_MANAGEMENT_API_ERROR_T Type

Error Information

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ATTACH_CHILD_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE_DETAILS_T Type

Information for attaching a software source to a managed instance

Syntax
```

```

Fields

Field Description

`software_source_id`

(required) OCID for the Software Source

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ATTACH_PARENT_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE_DETAILS_T Type

Information for attaching a software source to a managed instance

Syntax
```

```

Fields

Field Description

`software_source_id`

(required) OCID for the Software Source

### DBMS_CLOUD_OCI_OS_MANAGEMENT_AUTONOMOUS_SETTINGS_T Type

Managed Instance with Autonomous settings

Syntax
```

```

Fields

Field Description

`is_auto_update_enabled`

(optional) True if daily updates are enabled

### DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_T Type

A software source which can be added to a managed instance. Once a software source is added, packages from that software source can be installed on that managed instance.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`compartment_id`

(required) OCID for the Compartment

`display_name`

(required) User friendly name for the software source

`parent_id`

(optional) OCID for the parent software source, if there is one

`parent_name`

(optional) Display name of the parent software source, if there is one

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ID_T Type

An id along with a name to simplify display for a user

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`display_name`

(required) User friendly name

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_ID_T Type

Identifying information for the specified software source

Syntax
```

```

Fields

Field Description

`name`

(optional) software source name

`id`

(required) software source identifier

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ID_TBL Type

Nested table type of dbms_cloud_oci_os_management_id_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_ID_TBL Type

Nested table type of dbms_cloud_oci_os_management_software_source_id_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_UPDATE_SUMMARY_T Type

An update available for a managed instance

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package available for update. NOTE - This is not an OCID

`update_type`

(optional) The purpose of this update.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`l_type`

(required) Type of the package

`installed_version`

(required) Version of the installed package

`available_version`

(required) Version of the package available for update

`architecture`

(optional) The architecture for which this package was built

`errata`

(optional) List of errata containing this update

`related_cves`

(optional) List of CVEs applicable to this erratum

`software_sources`

(optional) list of software sources that provide the software package

### DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_WINDOWS_UPDATE_SUMMARY_T Type

An update available for installation on the Windows managed instance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Windows Update name

`name`

(required) Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

`update_type`

(required) The purpose of this update.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`is_eligible_for_installation`

(optional) Indicates whether the update can be installed using OSMS.

Allowed values are: 'INSTALLABLE', 'NOT_INSTALLABLE', 'UNKNOWN'

`is_reboot_required_for_installation`

(optional) Indicates whether a reboot may be required to complete installation of this update.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_MANAGED_INSTANCE_GROUP_COMPARTMENT_DETAILS_T Type

Compartment id for a managed instance group

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_SCHEDULED_JOB_COMPARTMENT_DETAILS_T Type

Compartment id for a scheduled job

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_SOFTWARE_SOURCE_COMPARTMENT_DETAILS_T Type

Compartment id for a software source

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CRASH_EVENT_SYSTEM_INFORMATION_T Type

Detailed information about system at the time of the crash.

Syntax
```

```

Fields

Field Description

`architecture`

(optional) system architecture

Allowed values are: 'IA_32', 'X86_64', 'AARCH64', 'SPARC', 'AMD64_DEBIAN'

`ksplice_effective_kernel_version`

(optional) Active ksplice kernel version (uptrack-uname -r)

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`os_name`

(optional) Operating System Name (OCA value)

`os_kernel_release`

(optional) Operating System Kernel Release (uname -v)

`os_kernel_version`

(optional) Operating System Kernel Version (uname -r)

`os_system_version`

(optional) Version of the OS (VERSION from /etc/os-release)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type

Detail information for creating a managed instance group

Syntax
```

```

Fields

Field Description

`display_name`

(required) Managed Instance Group identifier

`description`

(optional) Information specified by the user about the managed instance group

`compartment_id`

(required) OCID for the Compartment

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`os_family`

(optional) The Operating System type of the managed instance(s) on which this scheduled job will operate. If not specified, this defaults to Linux.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_PACKAGE_NAME_T Type

Identifying information for the specified package

Syntax
```

```

Fields

Field Description

`name`

(required) package identifier

### DBMS_CLOUD_OCI_OS_MANAGEMENT_PACKAGE_NAME_TBL Type

Nested table type of dbms_cloud_oci_os_management_package_name_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_SCHEDULED_JOB_DETAILS_T Type

Information for creating a Scheduled Job

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID for the Compartment

`display_name`

(required) Scheduled Job name

`description`

(optional) Details describing the Scheduled Job.

`schedule_type`

(required) the type of scheduling this Scheduled Job follows

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(required) the desired time for the next execution of this Scheduled Job

`interval_type`

(optional) the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

Allowed values are: 'HOUR', 'DAY', 'WEEK', 'MONTH'

`interval_value`

(optional) the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

`managed_instances`

(optional) The list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups). Either this or the managedInstanceGroups must be supplied.

`managed_instance_groups`

(optional) The list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances). Either this or managedInstances must be supplied.

`operation_type`

(required) the type of operation this Scheduled Job performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`update_type`

(optional) Type of the update (only if operation type is UPDATEALL)

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`package_names`

(optional) the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`update_names`

(optional) The unique names of the Windows Updates (only if operation type is INSTALL). This is only applicable when the osFamily is for Windows managed instances.

`os_family`

(optional) The Operating System type of the managed instance(s) on which this scheduled job will operate. If not specified, this defaults to Linux.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_SOFTWARE_SOURCE_DETAILS_T Type

Description of a software source to be created on the management system

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID for the Compartment

`display_name`

(required) User friendly name for the software source

`description`

(optional) Information specified by the user about the software source

`arch_type`

(required) The architecture type supported by the Software Source

Allowed values are: 'IA_32', 'X86_64', 'AARCH64', 'SPARC', 'AMD64_DEBIAN'

`maintainer_name`

(optional) Name of the person maintaining this software source

`maintainer_email`

(optional) Email address of the person maintaining this software source

`maintainer_phone`

(optional) Phone number of the person maintaining this software source

`checksum_type`

(optional) The yum repository checksum type used by this software source

Allowed values are: 'SHA1', 'SHA256', 'SHA384', 'SHA512'

`parent_id`

(optional) OCID for the parent software source, if there is one

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_DETACH_CHILD_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE_DETAILS_T Type

Information for detaching a software source from a managed instance

Syntax
```

```

Fields

Field Description

`software_source_id`

(required) OCID for the Software Source

### DBMS_CLOUD_OCI_OS_MANAGEMENT_DETACH_PARENT_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE_DETAILS_T Type

Information for detaching a software source from a managed instance

Syntax
```

```

Fields

Field Description

`software_source_id`

(required) OCID for the Software Source

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SUMMARY_T Type

Summary information for a software package

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID

`l_type`

(required) Type of the package

`version`

(required) Version of the package

`architecture`

(optional) the architecture for which this software was built

`checksum`

(optional) checksum of the package

`checksum_type`

(optional) type of the checksum

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_software_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ERRATUM_T Type

Details about the erratum.

Syntax
```

```

Fields

Field Description

`name`

(required) Advisory name

`id`

(required) OCID for the Erratum.

`compartment_id`

(required) OCID for the Compartment.

`synopsis`

(optional) Summary description of the erratum.

`issued`

(optional) date the erratum was issued

`description`

(optional) Details describing the erratum.

`updated`

(optional) most recent date the erratum was updated

`advisory_type`

(optional) Type of the erratum.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`l_from`

(optional) Information specifying from where the erratum was release.

`solution`

(optional) Information describing how the erratum can be resolved.

`references`

(optional) Information describing how to find more information about the erratum.

`affected_instances`

(optional) list of managed instances to this erratum

`related_cves`

(optional) list of CVEs applicable to this erratum

`software_sources`

(optional) list of Software Sources

`packages`

(optional) list of Packages affected by this erratum

### DBMS_CLOUD_OCI_OS_MANAGEMENT_ERRATUM_SUMMARY_T Type

Important changes for software. This can include security | advisories, bug fixes, or enhancements.

Syntax
```

```

Fields

Field Description

`name`

(required) Advisory name

`id`

(required) OCID for the Erratum.

`compartment_id`

(required) OCID for the Compartment.

`synopsis`

(optional) Summary description of the erratum.

`issued`

(optional) date the erratum was issued

`updated`

(optional) most recent date the erratum was updated

`advisory_type`

(optional) Type of the erratum.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`related_cves`

(optional) list of CVEs applicable to this erratum

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_T Type

Description of Event.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier of the event

`instance_id`

(optional) OCI identifier of the instance where the event occurred

`compartment_id`

(optional) OCI identifier of the compartement where the instance is

`tenancy_id`

(optional) OCID identifier of the instance tenancy.

`summary`

(optional) human readable description of the event

`l_timestamp`

(optional) Time of the occurrence of the event

`event_fingerprint`

(optional) Unique ID used to group event with the same characteristics together. The list of such groups of event can be retrieved via /recurringEvents/{EventFingerprint}

`l_count`

(optional) Event occurrence count. Number of time the event has happen on the system.

`event_type`

(required) Type of the Event.

Allowed values are: 'KERNEL_OOPS', 'KERNEL_CRASH', 'CRASH', 'EXPLOIT_ATTEMPT', 'COMPLIANCE', 'TUNING_SUGGESTION', 'TUNING_APPLIED', 'SECURITY', 'ERROR', 'WARNING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_SUMMARY_T Type

Summary of the Event.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier of the event

`instance_id`

(required) Unique OCI identifier of the instance where the event occurred

`summary`

(optional) human readable description of the event

`event_type`

(required) Type of the event.

Allowed values are: 'KERNEL_OOPS', 'KERNEL_CRASH', 'CRASH', 'EXPLOIT_ATTEMPT', 'COMPLIANCE', 'TUNING_SUGGESTION', 'TUNING_APPLIED', 'SECURITY', 'ERROR', 'WARNING'

`l_count`

(optional) Event occurrence count. Number of time the same event happened on the system.

`l_timestamp`

(optional) Time of the occurrence of the event

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_COLLECTION_T Type

Results of a event search. Contains both EventSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of events.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_CONTENT_T Type

Information about the data collected as a ZIP file when the event occurred.

Syntax
```

```

Fields

Field Description

`content_availability`

(optional) Status of the event content

Allowed values are: 'NOT_AVAILABLE', 'AVAILABLE_ON_INSTANCE', 'AVAILABLE_ON_SERVICE', 'AVAILABLE_ON_INSTANCE_AND_SERVICE', 'AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS'

`instance_path`

(optional) Path to the event content on the instance

`l_size`

(optional) size in bytes of the event content (size of the zip file uploaded)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_REPORT_T Type

Summary about event occurrences on a system.

Syntax
```

```

Fields

Field Description

`l_count`

(required) count of events currently registered on the system.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLABLE_PACKAGE_SUMMARY_T Type

A software package available for install on a managed instance

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID

`l_type`

(required) Type of the package

`version`

(required) Version of the package

`architecture`

(optional) The architecture for which this package was built

`software_sources`

(optional) list of software sources that provide the software package

### DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLED_PACKAGE_SUMMARY_T Type

A software package installed on a managed instance

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID

`l_type`

(required) Type of the package

`version`

(required) Version of the installed package

`architecture`

(optional) The architecture for which this package was built

`install_time`

(optional) Install time of the package

`issued`

(optional) date the package was issued by a providing erratum (if available)

`software_sources`

(optional) list of software sources that provide the software package

### DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLED_WINDOWS_UPDATE_SUMMARY_T Type

A Windows update installed on the Windows managed instance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Windows Update name

`name`

(required) Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

`update_type`

(required) The purpose of this update.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_VM_CORE_INFORMATION_T Type

VMcore information.

Syntax
```

```

Fields

Field Description

`component`

(optional) Kernel module responsible of the crash.

`backtrace`

(optional) Crash backtrace.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_CRASH_EVENT_T Type

Information about a Kernel Crash.

Syntax
```

```

`dbms_cloud_oci_os_management_kernel_crash_event_t`is a subtype of the`dbms_cloud_oci_os_management_event_t`type.

Fields

Field Description

`reason`

(optional) reason of the crash

`time_first_occurred`

(optional) First occurrence time of the event

`vmcore`

(optional)

`content`

(optional)

`system`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_OOPS_EVENT_T Type

Information about a Kernel Oops.

Syntax
```

```

`dbms_cloud_oci_os_management_kernel_oops_event_t`is a subtype of the`dbms_cloud_oci_os_management_event_t`type.

Fields

Field Description

`reason`

(optional) reason of the crash

`time_first_occurred`

(optional) First occurrence time of the event

`vmcore`

(optional)

`content`

(optional)

`system`

(optional)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_DETAILS_T Type

Updatable information for a module stream

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module

`stream_name`

(required) The name of a stream of the specified module

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_DETAILS_T Type

Updatable information for a module stream profile

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module

`stream_name`

(required) The name of a stream of the specified module

`profile_name`

(required) The name of a profile of the specified module stream

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_module_stream_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_module_stream_profile_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_DETAILS_T Type

The set of changes to make to the state of the modules, streams, and profiles on a managed instance

Syntax
```

```

Fields

Field Description

`is_dry_run`

(optional) Indicates if this operation is a dry run or if the operation should be commited. If set to true, the result of the operation will be evaluated but not committed. If set to false, the operation is committed to the managed instance. The default is false.

`enable`

(optional) The set of module streams to enable.

`disable`

(optional) The set of module streams to disable.

`install`

(optional) The set of module stream profiles to install.

`remove`

(optional) The set of module stream profiles to remove.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_T Type

Detail information for an OCI Compute instance that is being managed

Syntax
```

```

Fields

Field Description

`display_name`

(required) Managed Instance identifier

`id`

(required) OCID for the managed instance

`description`

(optional) Information specified by the user about the managed instance

`last_checkin`

(optional) Time at which the instance last checked in

`last_boot`

(optional) Time at which the instance last booted

`updates_available`

(optional) Number of updates available to be installed

`os_name`

(optional) Operating System Name

`os_version`

(optional) Operating System Version

`os_kernel_version`

(optional) Operating System Kernel Version

`compartment_id`

(required) OCID for the Compartment

`status`

(optional) status of the managed instance.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING'

`parent_software_source`

(optional) the parent (base) Software Source attached to the Managed Instance

`child_software_sources`

(optional) list of child Software Sources attached to the Managed Instance

`managed_instance_groups`

(optional) The ids of the managed instance groups of which this instance is a member.

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`is_reboot_required`

(optional) Indicates whether a reboot is required to complete installation of updates.

`notification_topic_id`

(optional) OCID of the ONS topic used to send notification to users

`ksplice_effective_kernel_version`

(optional) The ksplice effective kernel version

`is_data_collection_authorized`

(optional) True if user allow data collection for this instance

`autonomous`

(optional) if present, indicates the Managed Instance is an autonomous instance. Holds all the Autonomous specific information

`security_updates_available`

(optional) Number of security type updates available to be installed

`bug_updates_available`

(optional) Number of bug fix type updates available to be installed

`enhancement_updates_available`

(optional) Number of enhancement type updates available to be installed

`other_updates_available`

(optional) Number of non-classified updates available to be installed

`scheduled_job_count`

(optional) Number of scheduled jobs associated with this instance

`work_request_count`

(optional) Number of work requests associated with this instance

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_GROUP_T Type

Detail information for a managed instance group

Syntax
```

```

Fields

Field Description

`display_name`

(required) Managed Instance Group identifier

`id`

(required) OCID for the managed instance group

`description`

(optional) Information specified by the user about the managed instance group

`compartment_id`

(required) OCID for the Compartment

`managed_instances`

(optional) list of Managed Instances in the group

`lifecycle_state`

(optional) The current state of the Software Source.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_GROUP_SUMMARY_T Type

An group of managed instances that will be managed together

Syntax
```

```

Fields

Field Description

`display_name`

(required) user settable name

`id`

(required) OCID for the managed instance group

`compartment_id`

(required) OCID for the Compartment

`description`

(optional) Information specified by the user about the managed instance group

`managed_instance_count`

(optional) Number of managed instances in this managed instance group

`lifecycle_state`

(optional) The current state of the Software Source.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_SUMMARY_T Type

An OCI Compute instance that is being managed

Syntax
```

```

Fields

Field Description

`display_name`

(required) user settable name

`id`

(required) OCID for the managed instance

`last_checkin`

(optional) Time at which the instance last checked in

`last_boot`

(optional) Time at which the instance last booted

`updates_available`

(optional) Number of updates available to be installed

`compartment_id`

(required) OCID for the Compartment

`description`

(optional) Information specified by the user about the managed instance

`status`

(optional) status of the managed instance.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING'

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`is_reboot_required`

(optional) Indicates whether a reboot is required to complete installation of updates.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_T Type

A module stream provided by a software source

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream

`stream_name`

(required) The name of the stream

`is_default`

(optional) Indicates if this stream is the default for its module.

`software_source_id`

(optional) The OCID of the software source that provides this module stream.

`architecture`

(optional) The architecture for which the packages in this module stream were built

`description`

(optional) A description of the contents of the module stream

`profiles`

(optional) A list of profiles that are part of the stream. Each element in the list is the name of a profile. The name is suitable to use as an argument to other OS Management APIs that interact directly with module stream profiles. However, it is not URL encoded.

`packages`

(optional) A list of packages that are contained by the stream. Each element in the list is the name of a package. The name is suitable to use as an argument to other OS Management APIs that interact directly with packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_SUMMARY_T Type

Summary information pertaining to a module stream profile on a managed instance

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream profile

`stream_name`

(required) The name of the stream that contains the profile

`profile_name`

(required) The name of the profile

`status`

(required) The status of the profile. A profile with the \"INSTALLED\" status indicates that the profile has been installed. A profile with the \"AVAILABLE\" status indicates that the profile is not installed, but can be.

Allowed values are: 'INSTALLED', 'AVAILABLE'

`time_modified`

(optional) The date and time of the last status change for this profile, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_module_stream_profile_on_managed_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_ON_MANAGED_INSTANCE_SUMMARY_T Type

Summary information pertaining to a module stream on a managed instance

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream.

`stream_name`

(required) The name of the stream.

`status`

(required) The status of the stream A stream with the \"ENABLED\" status can be used as a source for installing profiles. Streams with this status are also \"ACTIVE\". A stream with the \"DISABLED\" status cannot be the source for installing profiles. To install profiles and packages from this stream, it must be enabled. A stream with the \"ACTIVE\" status can be used as a source for installing profiles. The packages that comprise the stream are also used when a matching package is installed directly. In general, a stream can have this status if it is the default stream for the module and no stream has been explicitly enabled.

Allowed values are: 'ENABLED', 'DISABLED', 'ACTIVE'

`profiles`

(optional) The set of profiles that the module stream contains.

`software_source_id`

(optional) The OCID of the software source that provides this module stream.

`time_modified`

(optional) The date and time of the last status change for this profile, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_T Type

A module stream profile provided by a software source

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream profile

`stream_name`

(required) The name of the stream that contains the profile

`profile_name`

(required) The name of the profile

`is_default`

(optional) Indicates if this profile is the default for its module stream.

`description`

(optional) A description of the contents of the module stream profile

`packages`

(required) A list of packages that constitute the profile. Each element in the list is the name of a package. The name is suitable to use as an argument to other OS Management APIs that interact directly with packages.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_SUMMARY_T Type

Summary information pertaining to a module stream profile provided by a software source

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream profile

`stream_name`

(required) The name of the stream that contains the profile

`profile_name`

(required) The name of the profile

### DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_SUMMARY_T Type

Summary information pertaining to a module stream provided by a software source

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of the module that contains the stream.

`stream_name`

(required) The name of the stream.

`software_source_id`

(optional) The OCID of the software source that provides this module stream.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_RECURRENCE_T Type

An object for representing a recurrence time interval

Syntax
```

```

Fields

Field Description

`interval_type`

(required) the interval period for the recurrence

Allowed values are: 'MINUTES', 'HOURS', 'DAYS', 'WEEKS'

`interval_value`

(required) the value for the interval period for the recurrence

### DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_SUMMARY_T Type

Event occurrence on managed instances.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier of the event

`instance_id`

(required) OCID identifier of the instance

`l_timestamp`

(optional) time occurence

### DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_os_management_related_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_COLLECTION_T Type

Results of a event occurence search. Contains RelatedEventSummary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of event occurrence.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_REMOVE_PACKAGES_FROM_SOFTWARE_SOURCE_DETAILS_T Type

List of software package names

Syntax
```

```

Fields

Field Description

`package_names`

(required) the list of package names

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SCHEDULED_JOB_T Type

Detailed information about a Scheduled Job

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the Scheduled Job

`compartment_id`

(optional) OCID for the Compartment

`display_name`

(required) Scheduled Job name

`description`

(optional) Details describing the Scheduled Job.

`schedule_type`

(optional) the type of scheduling this Scheduled Job follows

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(optional) the time of the next execution of this Scheduled Job

`time_last_execution`

(optional) the time of the last execution of this Scheduled Job

`interval_type`

(optional) the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

Allowed values are: 'HOUR', 'DAY', 'WEEK', 'MONTH'

`interval_value`

(optional) the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

`managed_instances`

(optional) the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)

`managed_instance_groups`

(optional) the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)

`operation_type`

(optional) the type of operation this Scheduled Job performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`update_type`

(optional) Type of the update (only if operation type is UPDATEALL)

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`package_names`

(optional) the names of the updates (only if operation type is INSTALL/UPDATE/REMOVE)

`work_requests`

(optional) list of Work Requests associated with this Scheduled Job

`lifecycle_state`

(optional) The current state of the Scheduled Job.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`update_names`

(optional) The unique names of the Windows Updates (only if operation type is INSTALL). This is only applicable when the osFamily is for Windows managed instances.

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`is_restricted`

(optional) true, if the schedule job has its update capabilities restricted. (Used to track Autonomous Scheduled Job)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SCHEDULED_JOB_SUMMARY_T Type

Basic information about a Scheduled Job

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the Scheduled Job

`display_name`

(required) Scheduled Job name

`compartment_id`

(optional) OCID for the Compartment

`schedule_type`

(optional) the type of scheduling this Scheduled Job follows

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(optional) the time/date of the next scheduled execution of this Scheduled Job

`time_last_execution`

(optional) the time/date of the last execution of this Scheduled Job

`managed_instances`

(optional) the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)

`managed_instance_groups`

(optional) the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)

`operation_type`

(optional) the type of operation this Scheduled Job performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`lifecycle_state`

(optional) The current state of the Scheduled Job.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`is_restricted`

(optional) true, if the schedule job has its update capabilities restricted. (Used to track Autonomous Scheduled Job)

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_DEPENDENCY_T Type

A dependency for a software package

Syntax
```

```

Fields

Field Description

`dependency`

(optional) the software package's dependency

`dependency_type`

(optional) the type of the dependency

`dependency_modifier`

(optional) the modifier for the dependency

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_FILE_T Type

A file associated with a package

Syntax
```

```

Fields

Field Description

`path`

(optional) file path

`l_type`

(optional) type of the file

`time_modified`

(optional) The date and time of the last modification to this file, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`checksum`

(optional) checksum of the file

`checksum_type`

(optional) type of the checksum

`size_in_bytes`

(optional) size of the file in bytes

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_DEPENDENCY_TBL Type

Nested table type of dbms_cloud_oci_os_management_software_package_dependency_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_FILE_TBL Type

Nested table type of dbms_cloud_oci_os_management_software_package_file_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_T Type

The details for a software package

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID

`l_type`

(required) Type of the package

`version`

(required) Version of the package

`architecture`

(optional) the architecture for which this software was built

`last_modified_date`

(optional) date of the last update to the package

`checksum`

(optional) checksum of the package

`checksum_type`

(optional) type of the checksum

`description`

(optional) description of the package

`size_in_bytes`

(optional) size of the package in bytes

`dependencies`

(optional) list of dependencies for the software package

`files`

(optional) list of files for the software package

`software_sources`

(optional) list of software sources that provide the software package

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SEARCH_SUMMARY_T Type

Summary information for a software package

Syntax
```

```

Fields

Field Description

`display_name`

(required) Package name

`name`

(required) Unique identifier for the package. NOTE - This is not an OCID

`l_type`

(required) Type of the package

`version`

(required) Version of the package

`architecture`

(optional) the architecture for which this software was built

`summary`

(optional) a summary description of the software package

`advisory_type`

(optional) Type of the erratum.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`errata`

(optional) List of errata containing this software package

`software_sources`

(optional) list of software sources that provide the software package

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_T Type

A software source contains a collection of packages

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the Software Source

`compartment_id`

(required) OCID for the Compartment

`display_name`

(required) User friendly name for the software source

`description`

(optional) Information specified by the user about the software source

`repo_type`

(required) Type of the Software Source

`arch_type`

(optional) The architecture type supported by the Software Source

Allowed values are: 'IA_32', 'X86_64', 'AARCH64', 'SPARC', 'AMD64_DEBIAN'

`url`

(required) URL for the repostiory

`parent_id`

(optional) OCID for the parent software source, if there is one

`parent_name`

(optional) Display name the parent software source, if there is one

`checksum_type`

(optional) The yum repository checksum type used by this software source

Allowed values are: 'SHA1', 'SHA256', 'SHA384', 'SHA512'

`maintainer_name`

(optional) Name of the person maintaining this software source

`maintainer_email`

(optional) Email address of the person maintaining this software source

`maintainer_phone`

(optional) Phone number of the person maintaining this software source

`gpg_key_url`

(optional) URL of the GPG key for this software source

`gpg_key_id`

(optional) ID of the GPG key for this software source

`gpg_key_fingerprint`

(optional) Fingerprint of the GPG key for this software source

`status`

(optional) status of the software source.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING'

`lifecycle_state`

(optional) The current state of the Software Source.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`packages`

(optional) Number of packages

`associated_managed_instances`

(optional) list of the Managed Instances associated with this Software Sources

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_SUMMARY_T Type

A software source contains a collection of packages

Syntax
```

```

Fields

Field Description

`id`

(required) OCID for the Software Source

`description`

(optional) Information specified by the user about the software source

`compartment_id`

(required) OCID for the Compartment

`display_name`

(required) User friendly name for the software source

`repo_type`

(required) Type of the Software Source

`status`

(optional) status of the software source.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING'

`packages`

(optional) Number of packages

`lifecycle_state`

(optional) The current state of the software source.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`parent_id`

(optional) OCID for the parent software source, if there is one

`parent_name`

(optional) Display name the parent software source, if there is one

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_EVENT_DETAILS_T Type

Information for updating an event associated with a managed instance

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MANAGED_INSTANCE_DETAILS_T Type

Information to update a managed instance

Syntax
```

```

Fields

Field Description

`notification_topic_id`

(optional) OCID of the ONS topic used to send notification to users

`is_data_collection_authorized`

(optional) True if user allow data collection for this instance

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type

Information for updating a managed instance group

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Managed Instance Group identifier

`description`

(optional) Information specified by the user about the managed instance group

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_PROFILE_DETAILS_T Type

Information detailing the state of a module stream profile

Syntax
```

```

Fields

Field Description

`profile_name`

(required) The name of the profile of the parent stream

`status`

(required) The status of the profile. A profile with the \"INSTALLED\" status indicates that the profile has been installed. A profile with the \"AVAILABLE\" status indicates that the profile is not installed, but can be.

Allowed values are: 'INSTALLED', 'AVAILABLE'

`is_default`

(optional) Indicates if the module stream profile is the default

`time_modified`

(required) The date and time of the last status change for this object, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_PROFILE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_update_module_stream_profile_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_DETAILS_T Type

Information detailing the state of a module stream

Syntax
```

```

Fields

Field Description

`stream_name`

(required) The name of the stream of the parent module

`status`

(required) The status of the stream A stream with the \"ENABLED\" status can be used as a source for installing profiles. Streams with this status are also \"ACTIVE\". A stream with the \"DISABLED\" status cannot be the source for installing profiles. To install profiles and packages from this stream, it must be enabled. A stream with the \"ACTIVE\" status can be used as a source for installing profiles. The packages that comprise the stream are also used when a matching package is installed directly. In general, a stream can have this status if it is the default stream for the module and no stream has been explicitly enabled.

Allowed values are: 'ENABLED', 'DISABLED', 'ACTIVE'

`time_modified`

(required) The date and time of the last status change for this object, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`software_source_name`

(optional) The name of the software source that publishes this stream.

`software_source_url`

(optional) The URL of the software source that publishes this stream.

`is_default`

(optional) Indicates if the module stream is the default

`profiles`

(optional) The profiles of the stream

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_update_module_stream_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_DETAILS_T Type

A description of a module and its stream

Syntax
```

```

Fields

Field Description

`module_name`

(required) The name of a module

`streams`

(optional) The streams of the module

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_os_management_update_module_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_STATE_DETAILS_T Type

A complete description of the state of modules on a managed instance

Syntax
```

```

Fields

Field Description

`modules`

(optional) The modules known to a managed instance

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_SCHEDULED_JOB_DETAILS_T Type

Information for updating a Scheduled Job

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Scheduled Job name

`description`

(optional) Details describing the Scheduled Job.

`schedule_type`

(optional) the type of scheduling this Scheduled Job follows

Allowed values are: 'ONETIME', 'RECURRING'

`time_next_execution`

(optional) the desired time for the next execution of this Scheduled Job

`interval_type`

(optional) the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

Allowed values are: 'HOUR', 'DAY', 'WEEK', 'MONTH'

`interval_value`

(optional) the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

`operation_type`

(optional) the type of operation this Scheduled Job performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`update_type`

(optional) Type of the update (only if operation type is UPDATEALL)

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT', 'OTHER', 'KSPLICE', 'ALL'

`package_names`

(optional) the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)

`update_names`

(optional) The unique names of the Windows Updates (only if operation type is INSTALL). This is only applicable when the osFamily is for Windows managed instances.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_SOFTWARE_SOURCE_DETAILS_T Type

Information for updating a software source on the management system

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User friendly name for the software source

`description`

(optional) Information specified by the user about the software source

`maintainer_name`

(optional) Name of the person maintaining this software source

`maintainer_email`

(optional) Email address of the person maintaining this software source

`maintainer_phone`

(optional) Phone number of the person maintaining this software source

`checksum_type`

(optional) The yum repository checksum type used by this software source

Allowed values are: 'SHA1', 'SHA256', 'SHA384', 'SHA512'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WINDOWS_UPDATE_T Type

An update available for a Windows managed instance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Windows Update name.

`name`

(required) Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

`description`

(optional) Information about the Windows Update.

`update_type`

(required) The purpose of this update.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`size_in_bytes`

(optional) size of the package in bytes

`is_eligible_for_installation`

(optional) Indicates whether the update can be installed using OSMS.

Allowed values are: 'INSTALLABLE', 'NOT_INSTALLABLE', 'UNKNOWN'

`installation_requirements`

(optional) List of requirements forinstalling on a managed instances

Allowed values are: 'EULA_ACCEPTANCE_REQUIRED', 'SOFTWARE_MEDIA_REQUIRED', 'USER_INTERACTION_REQUIRED'

`is_reboot_required_for_installation`

(optional) Indicates whether a reboot may be required to complete installation of this update.

`kb_article_ids`

(optional) List of the Microsoft Knowledge Base Article Ids related to this Windows Update.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WINDOWS_UPDATE_SUMMARY_T Type

An update available for a Windows managed instance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Windows Update name

`name`

(required) Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`

`update_type`

(required) The purpose of this update.

Allowed values are: 'SECURITY', 'BUG', 'ENHANCEMENT', 'OTHER'

`installable`

(optional) Indicates whether the update can be installed using OSMS.

Allowed values are: 'INSTALLABLE', 'NOT_INSTALLABLE', 'UNKNOWN'

`is_reboot_required_for_installation`

(optional) Indicates whether a reboot may be required to complete installation of this update.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_RESOURCE_T Type

A resource created, operated on or used by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type for the work request.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively. If the request failed for that resource, the state will be FAILED.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'FAILED', 'IN_PROGRESS', 'INSTALLED', 'REMOVED'

`identifier`

(required) The identifier of the resource. Not all resources will have an id.

`name`

(optional) The name of the resource. Not all resources will have a name specified.

`entity_uri`

(required) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_os_management_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) the type of operation this Work Request performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`status`

(required) status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELLING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`description`

(optional) Description of the type of work.

`message`

(optional) A progress or error message, if there is any.

`managed_instance_id`

(optional)

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

`parent_id`

(optional) The parent of this work request, if one exists.

`children_ids`

(optional) A list of the IDs of any children of this work request

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_ERROR_T Type

Human readable error message describing why the work request failed

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(optional) The date and time the error happened, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_T Type

Human readable log message describing what the work request is doing

Syntax
```

```

Fields

Field Description

`message`

(required) A human readable log message.

`l_timestamp`

(required) The date and time the error happened, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_SUMMARY_T Type

A work request summary

Syntax
```

```

Fields

Field Description

`operation_type`

(required) the type of operation this Work Request performs

Allowed values are: 'INSTALL', 'UPDATE', 'REMOVE', 'UPDATEALL', 'ENABLEMODULESTREAM', 'DISABLEMODULESTREAM', 'SWITCHMODULESTREAM', 'INSTALLMODULESTREAMPROFILE', 'REMOVEMODULESTREAMPROFILE', 'COMPOUND'

`status`

(required) status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELLING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`description`

(optional) Description of the type of work.

`message`

(optional) A progress or error message, if there is any.

`percent_complete`

(optional) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`os_family`

(optional) The Operating System type of the managed instance.

Allowed values are: 'LINUX', 'WINDOWS', 'ALL'

- [OS Management Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-125CCCDD-FAA3-4CBD-B144-0B0F3D9C8E17)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-785F30E1-CB8E-4489-84AD-DF03086FCF65)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ADD_PACKAGES_TO_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-78F37A22-D6EF-43E6-B192-4B7AA526B9BC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_API_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-E93560C5-E5F6-4BD7-84C9-B19373437988)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ATTACH_CHILD_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F8E109D6-676A-4C54-B979-FC566B10DAC5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ATTACH_PARENT_SOFTWARE_SOURCE_TO_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-94406F0A-77B3-4F7B-9561-1124A6871F2F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_AUTONOMOUS_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-28922131-EED7-4855-9465-730488AD0F0B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-20859366-3ADF-4330-A73A-3F413D9EA530)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-1E4E36B6-B610-489D-A112-C8E9D5C0642F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-FDFC9A8A-3B65-4907-BE3B-63F0DB8FC63A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ID_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-0C6F889B-BABF-406B-B7A0-7919EC639961)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_ID_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F7C6E266-2EF0-4F69-A231-DCAB5EE5D1C2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-D360BCD0-52CE-4D1B-82A3-8B2DCB80C22C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_AVAILABLE_WINDOWS_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-528FED41-500C-4AAF-AF83-A9C9557E8D86)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_MANAGED_INSTANCE_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-68A96279-B719-4522-A25A-175E896F1D64)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_SCHEDULED_JOB_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F4E2262D-6B7E-4F41-89DD-28661218D96A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CHANGE_SOFTWARE_SOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-23C4A9BF-F02C-4561-AB07-60AEA19548C4)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CRASH_EVENT_SYSTEM_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F50363D6-220C-4ABA-9905-E256EFCC59BE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-5BD05864-F491-4479-868B-7C9F3144C10C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_PACKAGE_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-7C7145F3-E9F9-46B8-9D6F-2A205BA465E0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_PACKAGE_NAME_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-613ADBAE-6EAC-4876-83BD-AAAED97AC6CE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_SCHEDULED_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B33D6845-1ECE-4958-865F-46F7D814592C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_CREATE_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-BF4539B6-FF64-47CF-A1F0-FC0C8D091B14)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_DETACH_CHILD_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-8CF6BFAB-0FDD-403F-A4C3-47BC490E19F8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_DETACH_PARENT_SOFTWARE_SOURCE_FROM_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B22B5824-1B59-493E-B9A4-7F24432D632A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B6D92688-106C-4798-BC29-E60B6E64F52A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-22ABF5BC-3072-4881-9796-386F32865653)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ERRATUM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-FD1A10DD-EB24-407C-8E62-38DF32BF7CE5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_ERRATUM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B859E699-CCBB-42B4-814D-BEECECE7D660)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-7FF68F36-0588-4864-AFBC-AAFE1E43E232)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-1A47B5B6-D69E-42EA-8E8F-1FF80928E814)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-BE89E08B-1398-4448-8566-7C5943AA7086)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-1F254743-AA2B-4E54-B713-17785D168D59)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_CONTENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-56F7AEEA-B4CE-4543-B6AF-803E1A7A4846)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_EVENT_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-49262391-4764-4D79-B446-0F503BC4EE02)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLABLE_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-2A73DDCB-D628-4D6E-AAE3-10FB08ECCF58)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLED_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-A03AF203-95AD-4F25-9776-A6129EE06E8D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_INSTALLED_WINDOWS_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-1C7C1FE5-77A9-46CE-B0A8-252156E7A9F7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_VM_CORE_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B552856C-4FB0-4F47-BAA2-65D266998649)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_CRASH_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-87B09987-AE3A-491A-80B8-BA6D06A44482)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_KERNEL_OOPS_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-E0E764E8-1C98-4BCD-A1CC-0D0BB5FF5803)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-B9798053-E668-476B-AC06-22BFA8833F09)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-2F7ED0E9-D9AB-4688-9F7F-766DF61B5E4D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-2A1E43DE-222E-4EB7-A0BF-D4D6555A454C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-737B3ABA-A3BD-4715-874D-0E2EA29E48C9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGE_MODULE_STREAMS_ON_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-E3A2C1F7-AB89-4613-A9E3-FA78DFC1DA80)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-49B824A5-880C-4BBE-A1AF-A6299DD4B8A9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-2E89FC8D-6CB4-4036-A16E-7E76A8383257)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F722DF9B-5537-4F20-AF44-9FFF3CAF73D0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MANAGED_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-A74314FF-C5B6-44AA-875A-1008F332EE37)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-20278D8C-68E9-487E-BA11-89092B87847B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-FA87B17B-436D-4677-A227-6C360AA25B33)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_ON_MANAGED_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-369749C4-E72D-46F1-8B7E-9E014CFD7641)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_ON_MANAGED_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-641E5A11-FDDA-4A06-8BB0-EFE52ADFCA4E)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-0504AE68-05DB-4372-AA22-DE7381447FEB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-3A280687-7126-4D2F-91A1-F6CA6F218B2F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_MODULE_STREAM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-8E929C32-D84C-4729-A077-1F4300D4BB8D)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_RECURRENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F281C372-CE15-42F9-9456-642BF203271C)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-83F241EB-DAB7-452B-80B7-A7485369BA0A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-CF632B99-07BE-44F1-A707-24FB7F2B79C2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_RELATED_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-A9B2F02A-ACFF-4B71-A742-A214825592FB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_REMOVE_PACKAGES_FROM_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-766EE5A1-7905-49B4-B10F-4C03EB8FCF26)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SCHEDULED_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-71E2C0DF-7256-4470-A211-D5088F22B173)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SCHEDULED_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-C676688D-3666-4F76-9C95-1927BB233136)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_DEPENDENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-53D220AC-1927-486A-9A08-B84C4FCC31E8)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-A0A7D789-E900-43B5-BD32-52450B4D4175)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_DEPENDENCY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-AD5A6BC9-8B1E-4053-BEC0-45011630B10B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_FILE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-521AF45D-54C3-4C3B-B8B3-B068414E6DEE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-13FBCF95-67F1-48E7-95AA-1E668A895879)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_PACKAGE_SEARCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-8AC7C05E-5E0B-4FC9-A626-55EED44D1B39)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-95F8C309-A307-4F6E-86CB-7E977E4F80F7)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_SOFTWARE_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-A556D92B-9CFF-48FF-BF33-AF10599D70B9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_EVENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-0A1D8DF9-E318-411E-8EAE-3D0BCB5A9A37)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MANAGED_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-4D8D4A0F-E65F-4204-BA7C-18D5EFC3A5DE)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MANAGED_INSTANCE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-F7BE860E-3810-447D-ACFD-B77496720A0A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-8884DE5D-14F4-4697-AABE-B0A767799B92)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_PROFILE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-6A3CF149-2A79-4FE6-9B7F-DCBEB088938A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-52B7DFFE-F63E-4D07-9177-C90AF70959F5)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-32395D12-E4DA-44C4-B67D-992E3AA7204B)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-49D7C104-3FB7-40BB-8725-32AF04F3E3A0)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-613E416E-9B08-4FDF-B0AF-ABF750B003EB)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_MODULE_STREAM_STATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-979D7BB0-6F8E-4770-B1AE-1373D0A576DD)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_SCHEDULED_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-7ADAF5D0-DECF-4026-A143-BCAB12C26A57)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_UPDATE_SOFTWARE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-DE6C62A2-6733-44C0-AC1B-65549697ED11)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WINDOWS_UPDATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-C4782F4A-C3B9-41B6-BA4B-C9E14F2E052A)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WINDOWS_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-824044D6-2AAF-476A-9B32-87B32B3CD707)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-742B6C07-8658-4502-94BF-DC23B69C3DD2)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-EC2F66D7-FD23-48A0-90AB-DBD9F9DD8CF9)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-4F5DC78E-02EB-4CB6-BE9E-669E3A0FBF2F)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-0A2D78DF-37A9-42B9-A65F-9E101996ACCC)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-889F4A5E-A519-4D02-B33D-8341EAE5CE86)
- [DBMS_CLOUD_OCI_OS_MANAGEMENT_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/os_management_t.html#ADSDK-GUID-9C201A8E-00F7-4153-ACE8-473AF995C2F7)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
