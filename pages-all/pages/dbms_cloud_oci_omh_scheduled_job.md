# OS Management Hub Scheduled Job Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#dcoc-content-body)

## OS Management Hub Scheduled Job Functions

Package: DBMS_CLOUD_OCI_OMH_SCHEDULED_JOB

### CREATE_SCHEDULED_JOB Function

Creates a new scheduled job.

Syntax
```

```

Parameters

Parameter Description

`create_scheduled_job_details`

(required) Details for the new scheduled job.

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

### DELETE_SCHEDULED_JOB Function

Deletes the specified scheduled job.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The OCID of the scheduled job.

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

### GET_SCHEDULED_JOB Function

Gets information about the specified scheduled job.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The OCID of the scheduled job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULED_JOBS Function

Lists scheduled jobs that match the specified compartment or scheduled job OCID. Filter the list against a variety of criteria including but not limited to its display name, lifecycle state, operation type, and schedule type.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`managed_instance_id`

(optional) The OCID of the managed instance for which to list resources.

`managed_instance_group_id`

(optional) The OCID of the managed instance group for which to list resources.

`managed_compartment_id`

(optional) The OCID of the managed compartment for which to list resources.

`lifecycle_stage_id`

(optional) The OCID of the lifecycle stage for which to list resources.

`operation_type`

(optional) The operation type for which to list resources.

Allowed values are: 'INSTALL_PACKAGES', 'UPDATE_PACKAGES', 'REMOVE_PACKAGES', 'UPDATE_ALL', 'UPDATE_SECURITY', 'UPDATE_BUGFIX', 'UPDATE_ENHANCEMENT', 'UPDATE_OTHER', 'UPDATE_KSPLICE_USERSPACE', 'UPDATE_KSPLICE_KERNEL', 'MANAGE_MODULE_STREAMS', 'SWITCH_MODULE_STREAM', 'ATTACH_SOFTWARE_SOURCES', 'DETACH_SOFTWARE_SOURCES', 'SYNC_MANAGEMENT_STATION_MIRROR', 'PROMOTE_LIFECYCLE'

`schedule_type`

(optional) The schedule type for which to list resources.

Allowed values are: 'ONETIME', 'RECURRING'

`time_start`

(optional) The start time after which to list all schedules, in ISO 8601 format. Example: 2017-07-14T02:40:00.000Z

`time_end`

(optional) The cut-off time before which to list all upcoming schedules, in ISO 8601 format. Example: 2017-07-14T02:40:00.000Z

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

`is_restricted`

(optional) If true, will only filter out restricted scheduled job.

`id`

(optional) The OCID of the scheduled job.

`compartment_id_in_subtree`

(optional) Default is false. When set to true ,returns results from {compartmentId} or any of its subcompartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RUN_SCHEDULED_JOB_NOW Function

Triggers an already created RECURRING scheduled job to run immediately instead of waiting for its next regularly scheduled time. This operation does not support ONETIME scheduled job.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The OCID of the scheduled job.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SCHEDULED_JOB Function

Updates the specified scheduled job's name, description, and other details, such as next execution and recurrence.

Syntax
```

```

Parameters

Parameter Description

`scheduled_job_id`

(required) The OCID of the scheduled job.

`update_scheduled_job_details`

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

- [OS Management Hub Scheduled Job Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-0C79C7DF-DB74-4567-AB8F-B9DF2081E286)
- [CREATE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-52793DF3-45A0-4538-8FC9-99CBFD82D0D0)
- [DELETE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-251CE4D0-4A7E-431C-904E-CBCFF1701E66)
- [GET_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-502F8B2C-4331-4F6F-8398-CABBBC77D795)
- [LIST_SCHEDULED_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-99BE28EE-B556-469B-B05F-062CB8EBC670)
- [RUN_SCHEDULED_JOB_NOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-EB7C9026-4A06-43A5-BEFC-12ADF86529E9)
- [UPDATE_SCHEDULED_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_scheduled_job.html#ADSDK-GUID-AEB14C58-DFBA-4DF7-9A3B-F39FA54AFC79)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
