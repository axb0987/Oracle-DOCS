# VBS Instance Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#dcoc-content-body)

## VBS Instance Common Types

### DBMS_CLOUD_OCI_VBS_INST_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_CHANGE_VBS_INSTANCE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_VBS_INST_CREATE_VBS_INSTANCE_DETAILS_T Type

The information about new VbsInstance.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier

`name`

(required) Service Instance Name

`display_name`

(required) Display Name

`is_resource_usage_agreement_granted`

(optional) Whether VBS is authorized to create and use resources in the customer tenancy

`resource_compartment_id`

(optional) Compartment where VBS may create additional resources for the service instance

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_VBS_INST_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_VBS_INST_UPDATE_VBS_INSTANCE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Display Name

`is_resource_usage_agreement_granted`

(optional) Whether VBS is authorized to create and use resources in the customer tenancy

`resource_compartment_id`

(optional) Compartment where VBS may create additional resources for the service instance

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_T Type

Visual Builder Studio service instance

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`name`

(required) Service instance name (unique identifier)

`display_name`

(required) Service instance display name

`compartment_id`

(required) Compartment of the service instance

`is_resource_usage_agreement_granted`

(optional) Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy

`resource_compartment_id`

(optional) Compartment where VBS may create additional resources for the service instance

`vbs_access_url`

(optional) Public web URL for accessing the VBS service instance

`time_created`

(optional) The time the the VbsInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the VbsInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the VbsInstance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_T Type

Summary of the Visual Builder Studio service instance

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`name`

(required) Service instance name (unique identifier)

`display_name`

(required) Service instance display name

`compartment_id`

(required) Compartment of the service instance

`is_resource_usage_agreement_granted`

(optional) Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy

`time_created`

(optional) The time the the VbsInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the VbsInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the VbsInstance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vbs_inst_vbs_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_COLLECTION_T Type

Wrapped list of Visual Builder Studio service instances

Syntax
```

```

Fields

Field Description

`items`

(required) The Visual Builder Studio service instances

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

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

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_vbs_inst_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_T Type

A VBS Instance related work request

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_VBS_INSTANCE', 'UPDATE_VBS_INSTANCE', 'DELETE_VBS_INSTANCE', 'MOVE_VBS_INSTANCE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_vbs_inst_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of errors encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`items`

(required) The errors.

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_vbs_inst_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of log messages from the execution of a work request.

Syntax
```

```

Fields

Field Description

`items`

(required) The log messages.

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_VBS_INSTANCE', 'UPDATE_VBS_INSTANCE', 'DELETE_VBS_INSTANCE', 'MOVE_VBS_INSTANCE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_vbs_inst_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_COLLECTION_T Type

A list of VBS instance related work requests.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [VBS Instance Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-E19CF8FF-812A-415D-8DB1-F787C7FEDF4E)
- [DBMS_CLOUD_OCI_VBS_INST_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-46101835-0DA7-4779-B993-6BCC88C5A913)
- [DBMS_CLOUD_OCI_VBS_INST_CHANGE_VBS_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-211B3334-E077-43E7-8A13-5943C5515BE7)
- [DBMS_CLOUD_OCI_VBS_INST_CREATE_VBS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-5567F02C-A3A3-4EF3-B8AF-D5FA6DE21BE2)
- [DBMS_CLOUD_OCI_VBS_INST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-3202F555-4609-47B3-BE24-EB1C6159767C)
- [DBMS_CLOUD_OCI_VBS_INST_UPDATE_VBS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-434A077D-6356-4D5B-B205-B0E119324DFB)
- [DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-C792B85D-D484-4B03-A6E8-5802CCC6B740)
- [DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-D2678034-DF52-4DDA-93FB-503D62ECF271)
- [DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-8532BAF1-F6D0-4A20-ACA8-9987BE371E8C)
- [DBMS_CLOUD_OCI_VBS_INST_VBS_INSTANCE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-BE99AF4B-0B48-487D-8914-978FEBC05D4C)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-AD8C8510-1191-4E1B-9B27-95CEF00EBEAF)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-D0FCB53C-0AD2-444A-8362-89574769F1B5)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-0DCE2C6A-2C5F-49F2-B5F0-E06D0ED448CA)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-BE022E8B-4AA3-4A50-B22E-33CD4C6D7A95)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-7C7CB65A-1A8D-4173-9E28-EA0CA2A67F42)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-441DA2D7-2146-4281-B9BB-A0C11D2DCC4F)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-E1F700E6-F6B3-42EF-97B5-766D41D4D43A)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-5AB5274C-48FE-4F33-AD58-EA8C767E6BC6)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-50BFEEEA-B4C3-4461-992F-56C4530F796B)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-76EAF87A-1F78-4B34-BCFC-3DAA114A52F3)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-C1DE52E9-D641-4FA1-ACF6-B137F69C2C7A)
- [DBMS_CLOUD_OCI_VBS_INST_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vbs_inst_t.html#ADSDK-GUID-E6E80BF9-3632-41D6-B717-9429BC663318)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
