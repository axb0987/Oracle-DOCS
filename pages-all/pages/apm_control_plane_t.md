# Application Performance Monitoring Control Plane Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#dcoc-content-body)

## Application Performance Monitoring Control Plane Common Types

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_APM_DOMAIN_T Type

Details of an APM domain.

Syntax
```

```

Fields

Field Description

`data_upload_endpoint`

(optional) The endpoint where the APM agents upload their observations and metrics.

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name of the APM domain, which can be updated.

`description`

(optional) Description of the APM domain.

`compartment_id`

(required) The OCID of the compartment corresponding to the APM domain.

`lifecycle_state`

(optional) The current lifecycle state of the APM domain.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_free_tier`

(optional) Indicates if this is an Always Free resource.

`time_created`

(optional) The time the APM domain was created, expressed in RFC 3339 timestamp format.

`time_updated`

(optional) The time the APM domain was updated, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_APM_DOMAIN_SUMMARY_T Type

Summary of an APM domain.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name of the APM domain, which can be updated.

`description`

(optional) Description of the APM domain.

`compartment_id`

(required) The OCID of the compartment corresponding to the APM domain.

`lifecycle_state`

(optional) The current lifecycle state of the APM domain.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_free_tier`

(optional) Indicates if this is an Always Free resource.

`time_created`

(optional) The time the APM domain was created, expressed in RFC 3339 timestamp format.

`time_updated`

(optional) The time the APM domain was updated, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_BASE_DOMAIN_DETAILS_T Type

Details for an APM domain.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name of the APM domain, which can be updated.

`description`

(optional) Description of the APM domain.

`compartment_id`

(required) The OCID of the compartment corresponding to the APM domain.

`lifecycle_state`

(optional) The current lifecycle state of the APM domain.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_free_tier`

(optional) Indicates if this is an Always Free resource.

`time_created`

(optional) The time the APM domain was created, expressed in RFC 3339 timestamp format.

`time_updated`

(optional) The time the APM domain was updated, expressed in RFC 3339 timestamp format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_BASE_KEY_DETAILS_T Type

The information about a Data Key.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.

`l_type`

(required) Type of the Data Key.

Allowed values are: 'PRIVATE', 'PUBLIC'

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_CHANGE_APM_DOMAIN_COMPARTMENT_DETAILS_T Type

The information needed for the change compartment operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the destination compartment for the APM domain.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_CREATE_APM_DOMAIN_DETAILS_T Type

The information about the new APM domain.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Display name of the APM domain.

`description`

(optional) Description of the APM domain.

`compartment_id`

(required) The OCID of the compartment corresponding to the APM domain.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_free_tier`

(optional) Indicates whether this is an \"Always Free\" resource. The default value is false.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_DATA_KEY_T Type

The information about a Data Key, including the Data Key's value.

Syntax
```

```

Fields

Field Description

`value`

(optional) Value of the Data Key.

`name`

(required) Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.

`l_type`

(required) Type of the Data Key.

Allowed values are: 'PRIVATE', 'PUBLIC'

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_DATA_KEY_SUMMARY_T Type

Summary of Data Key.

Syntax
```

```

Fields

Field Description

`value`

(optional) Value of the Data Key.

`name`

(required) Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.

`l_type`

(required) Type of the Data Key.

Allowed values are: 'PRIVATE', 'PUBLIC'

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_ERROR_T Type

The details of an error that occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_GENERATE_DATA_KEY_DETAILS_T Type

Details of the Data Key to be generated.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.

`l_type`

(required) Type of the Data Key.

Allowed values are: 'PRIVATE', 'PUBLIC'

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_REMOVE_DATA_KEY_DETAILS_T Type

Details of the Data Key to be removed.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_UPDATE_APM_DOMAIN_DETAILS_T Type

The information that can be updated by update APM domain operation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the APM domain.

`description`

(optional) Description of the APM domain.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type

The details of the resource that the work request affects.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_apm_control_plane_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_T Type

A description of work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_APM_DOMAIN', 'UPDATE_APM_DOMAIN', 'DELETE_APM_DOMAIN', 'GENERATE_DATA_KEYS', 'REMOVE_DATA_KEYS'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources affected by the work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed at[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occurred, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format.

### DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the error occurred, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format.

- [Application Performance Monitoring Control Plane Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-29ED6AAD-0064-40A7-B39D-FAC22B77AD0A)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-3AFD466B-B4A3-4A6D-8778-F8B20D88D7B1)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_APM_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-1774D7E4-61F8-49DE-AF09-A4FCC7EF62CA)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_APM_DOMAIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-7F8AAED4-7DD8-4F25-96C8-19F2E298898D)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_BASE_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-2EE4539E-428B-4E9C-BA3A-2A4723865117)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_BASE_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-D028A916-0682-4D8D-B9A3-2227A92E51F7)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_CHANGE_APM_DOMAIN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-D1D071B0-5960-4D95-8737-81BE0930D3DC)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_CREATE_APM_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-1E72D07C-034F-4810-BD9C-5DD1801FA295)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_DATA_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-4AD8EA4F-7131-49D9-96A1-1DA900BF4859)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_DATA_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-C80C96EB-EAA4-4F5F-972D-06FE0EAA8A1D)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-38DE5013-57BF-4627-99E2-26758AA52414)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_GENERATE_DATA_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-EF93E62A-17F8-4F06-AC65-FF0DE6A7080E)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_REMOVE_DATA_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-A9F75F29-62A9-4190-8F92-B030937F6ACD)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_UPDATE_APM_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-00A5E553-9FFB-4E7E-A385-E8DD744DB2DD)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-AA187C59-E83A-4F57-8F5B-1E6AAE17AC72)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-942530C8-48AB-4DC0-85CA-D6549A61F93D)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-994D565F-8524-4BC8-894A-FAA4ADF6EDFC)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-A468A83B-99EF-43B2-9322-44B8B4F3B025)
- [DBMS_CLOUD_OCI_APM_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_control_plane_t.html#ADSDK-GUID-87A2F61C-AE44-4F68-AD14-FBA88816DA94)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
