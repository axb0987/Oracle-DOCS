# OPA Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#dcoc-content-body)

## OPA Common Types

### DBMS_CLOUD_OCI_OPA_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_ATTACHMENT_DETAILS_T Type

Description of an attachment for an instance

Syntax
```

```

Fields

Field Description

`target_role`

(required) The role of the target attachment. * `PARENT` - The target instance is the parent of this attachment. * `CHILD` - The target instance is the child of this attachment.

Allowed values are: 'PARENT', 'CHILD'

`is_implicit`

(required) * If role == `PARENT`, the attached instance was created by this service instance * If role == `CHILD`, this instance was created from attached instance on behalf of a user

`target_id`

(required) The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.

`target_instance_url`

(required) The dataplane instance URL of the attached instance

`target_service_type`

(required) The type of the target instance, such as \"FUSION\".

### DBMS_CLOUD_OCI_OPA_CHANGE_OPA_INSTANCE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPA_CREATE_OPA_INSTANCE_DETAILS_T Type

The information about new OpaInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) OpaInstance Identifier. User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.

`description`

(optional) Description of the Oracle Process Automation instance.

`compartment_id`

(required) Compartment Identifier

`consumption_model`

(optional) Parameter specifying which entitlement to use for billing purposes

`shape_name`

(required) Shape of the instance.

`metering_type`

(optional) MeteringType Identifier

`idcs_at`

(optional) IDCS Authentication token. This is required for all realms with IDCS. This property is optional, as it is not required for non-IDCS realms.

`is_breakglass_enabled`

(optional) indicates if breakGlass is enabled for the opa instance.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPA_ERROR_T Type

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

### DBMS_CLOUD_OCI_OPA_ATTACHMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opa_attachment_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_T Type

Description of OpaInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) OpaInstance Identifier, can be renamed

`description`

(optional) Description of the Process Automation instance.

`compartment_id`

(required) Compartment Identifier

`instance_url`

(optional) OPA Instance URL

`consumption_model`

(optional) The entitlement used for billing purposes

Allowed values are: 'UCM', 'GOV', 'SAAS'

`shape_name`

(required) Shape of the instance.

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`metering_type`

(optional) MeteringType Identifier

Allowed values are: 'EXECUTION_PACK', 'USERS', 'EMPLOYEE', 'NAMED_USER'

`time_created`

(required) The time when OpaInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the OpaInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the OpaInstance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`identity_app_guid`

(optional) This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.

`identity_app_display_name`

(optional) This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.

`identity_domain_url`

(optional) This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.

`identity_app_opc_service_instance_guid`

(optional) This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.

`is_breakglass_enabled`

(optional) indicates if breakGlass is enabled for the opa instance.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`attachments`

(optional) A list of associated attachments to other services

### DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_SUMMARY_T Type

Summary of the OpaInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) OpaInstance Identifier, can be renamed

`description`

(optional) Description of the Process Automation instance.

`compartment_id`

(required) Compartment Identifier

`instance_url`

(optional) OPA Instance URL

`consumption_model`

(optional) Parameter specifying which entitlement to use for billing purposes

`shape_name`

(required) Shape of the instance.

`metering_type`

(optional) MeteringType Identifier

`time_created`

(required) The time the the OpaInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the OpaInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the OpaInstance.

`is_breakglass_enabled`

(optional) indicates if breakGlass is enabled for the opa instance.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opa_opa_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_COLLECTION_T Type

Results of a opaInstance search. Contains boh OpaInstanceSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of opaInstances.

### DBMS_CLOUD_OCI_OPA_UPDATE_OPA_INSTANCE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) OpaInstance Identifier

`description`

(optional) Description of the Oracle Process Automation instance.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_opa_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_OPA_INSTANCE', 'UPDATE_OPA_INSTANCE', 'DELETE_OPA_INSTANCE', 'MOVE_OPA_INSTANCE', 'CREATE_OPA_INSTANCE_ATTACHMENT', 'DELETE_OPA_INSTANCE_ATTACHMENT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_opa_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_opa_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_OPA_INSTANCE', 'UPDATE_OPA_INSTANCE', 'DELETE_OPA_INSTANCE', 'MOVE_OPA_INSTANCE', 'CREATE_OPA_INSTANCE_ATTACHMENT', 'DELETE_OPA_INSTANCE_ATTACHMENT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opa_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [OPA Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-F1727AF6-3029-4D4A-A820-FC2AB0D8E1B5)
- [DBMS_CLOUD_OCI_OPA_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-56233869-AD0A-4D61-B0A1-F96D75E4503B)
- [DBMS_CLOUD_OCI_OPA_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-7CE994A7-B833-4AF0-958F-C40E4E7C5D4D)
- [DBMS_CLOUD_OCI_OPA_CHANGE_OPA_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-7E268F21-15E9-4641-9EF3-C378BFA7A32A)
- [DBMS_CLOUD_OCI_OPA_CREATE_OPA_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-392B8543-254D-4D7B-AA40-A7F8D8FD307B)
- [DBMS_CLOUD_OCI_OPA_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-EC152C09-36BE-496C-88F6-3E648AB5F357)
- [DBMS_CLOUD_OCI_OPA_ATTACHMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-8BD8BD7E-C1D6-450E-8DED-BE61CC65CC3A)
- [DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-8B21D064-ADB0-4FBA-A793-A83581F6528E)
- [DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-9BE2C5F6-40FA-4A46-86F0-6732C1C0E716)
- [DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-432C07B4-9CBF-42C5-9F59-909024436388)
- [DBMS_CLOUD_OCI_OPA_OPA_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-9FE0BA39-2BAF-4991-AF5D-C3403D15D5E9)
- [DBMS_CLOUD_OCI_OPA_UPDATE_OPA_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-CF589BBD-0C85-48FD-B6B4-A39A8CBB219B)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-90D546AA-CDAB-4D8F-B67C-F1EA92AF706B)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-95390140-3A9B-4E56-B108-0335B4160472)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-B2CCCB6C-0F22-4F5A-91EC-9FC09965ED39)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-16E480ED-8F37-4D6A-898F-B2A6D37CB3FF)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-15CFB379-D5BB-4F6D-A074-3AF88FCAC5BE)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-C15339E7-C2E0-424F-A7DF-330AE2095BFF)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-0773AAEE-5E36-4F0E-84A8-16E47C880CDF)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-88F3DA26-01A8-4D0C-8ECD-5CDCB967B467)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-F6CF5E08-E1D3-4ADB-8EFD-16248383095E)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-2B262B42-24F8-4986-B98D-C16120B9D0DA)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-145300BA-453C-41A6-98A0-68B10AB5EFE3)
- [DBMS_CLOUD_OCI_OPA_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opa_t.html#ADSDK-GUID-02E54B4F-7A4D-4A39-8AB6-B2548FDC435D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
