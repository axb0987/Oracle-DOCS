# EM Warehouse Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#dcoc-content-body)

## EM Warehouse Common Types

### DBMS_CLOUD_OCI_EM_WAREHOUSE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_CHANGE_EM_WAREHOUSE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_EM_WAREHOUSE_CREATE_EM_WAREHOUSE_DETAILS_T Type

The information about new EmWarehouse.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) EmWarehouse Identifier

`em_bridge_id`

(required) EMBridge Identifier

`compartment_id`

(required) Compartment Identifier

`operations_insights_warehouse_id`

(required) operations Insights Warehouse Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_INSTANCES_DETAILS_T Type

Results of a emWarehouse search. Contains boh EmWarehouseSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`em_id`

(required) operations Insights Warehouse Identifier

`targets_count`

(optional) EmInstance Target count

`em_host`

(optional) emHost name

`em_discoverer_url`

(optional) emdDiscoverer url

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_T Type

Description of EmWarehouse.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) operations Insights Warehouse Identifier

`latest_etl_run_status`

(optional) Data Flow Run Status

`latest_etl_run_message`

(optional) Data Flow Run Status Message

`latest_etl_run_time`

(optional) Data Flow Run Total Time

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) EmWarehouse Identifier, can be renamed

`compartment_id`

(required) Compartment Identifier

`em_warehouse_type`

(required) Type of the EmWarehouse.

`em_bridge_id`

(optional) EMBridge Identifier

`time_created`

(required) The time the the EmWarehouse was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the EmWarehouse was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the EmWarehouse.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_SUMMARY_T Type

Summary of the EmWarehouse.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) operations Insights Warehouse Identifier

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) EmWarehouse Identifier, can be renamed

`compartment_id`

(required) Compartment Identifier

`em_warehouse_type`

(required) Type of the EmWarehouse.

`em_bridge_id`

(optional) EMBridge Identifier

`latest_etl_run_status`

(optional) Data Flow Run Status

`latest_etl_run_message`

(optional) Data Flow Run Status Message

`latest_etl_run_time`

(optional) Data Flow Run Total Time

`time_created`

(required) The time the the EmWarehouse was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the EmWarehouse was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the EmWarehouse.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_em_warehouse_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_COLLECTION_T Type

Results of a emWarehouse search. Contains boh EmWarehouseSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of emWarehouses.

### DBMS_CLOUD_OCI_EM_WAREHOUSE_ERROR_T Type

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_SUMMARY_T Type

Contains summary of a run.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier

`data_read_in_bytes`

(optional) Data read by the dataflow run

`data_written`

(optional) Data written by the dataflow run

`lifecycle_state`

(optional) The current state of the etlRun.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'FAILED', 'SUCCEEDED'

`display_name`

(optional) The name of the ETLRun.

`lifecycle_details`

(optional) Details of the lifecycle state

`run_duration_in_milliseconds`

(optional) Dataflow run duration

`time_created`

(optional) Time when the dataflow run was created

`time_updated`

(optional) Time when the dataflow run was updated

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_etl_run_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_COLLECTION_T Type

The runs list.

Syntax
```

```

Fields

Field Description

`items`

(required) List of runs

### DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_INSTANCES_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_em_instances_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_RESOURCE_USAGE_T Type

The resource usage information.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) operations Insights Warehouse Identifier

`id`

(required) Unique identifier that is immutable on creation

`em_instance_count`

(optional) EmInstanceCount

`targets_count`

(optional) EmInstance Target count

`em_instances`

(optional) List of emInstances

`schema_name`

(optional) schema name

### DBMS_CLOUD_OCI_EM_WAREHOUSE_UPDATE_EM_WAREHOUSE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) Compartment Identifier

`em_bridge_id`

(optional) EMBridge Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_EM_WAREHOUSE', 'UPDATE_EM_WAREHOUSE', 'DELETE_EM_WAREHOUSE', 'MOVE_EM_WAREHOUSE'

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_EM_WAREHOUSE', 'UPDATE_EM_WAREHOUSE', 'DELETE_EM_WAREHOUSE', 'MOVE_EM_WAREHOUSE'

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

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_em_warehouse_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [EM Warehouse Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-8C24F2D1-23D8-4694-B2CF-2B8D41DFEB13)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-1A4CA685-77B4-4C2F-815C-0B72FF2F6B14)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_CHANGE_EM_WAREHOUSE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-1895EA1E-67AE-43F7-BAA7-BA4B224F1AB6)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_CREATE_EM_WAREHOUSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-B620DA36-E0B0-45B3-858E-48C8177C6846)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_INSTANCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-016B8DFE-A333-48C8-9F08-495471C3E587)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-DE8B5C32-E5B9-4CA8-AE81-5B9AA9F2CDA9)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-427EE782-946B-4874-8AD1-675F8F49CC24)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-F96260C8-D53C-4C3F-B56F-9AB4ADF42CC5)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_WAREHOUSE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-E0C8DE03-DDC2-4346-AE7E-CA5850C4561A)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-7E5CD6C9-968F-4510-AE47-279035551861)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-93F7E25C-EFA4-4494-8A05-48DF6522229E)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-6DF6D4D1-401B-4F46-8FFF-6E565763B07D)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_ETL_RUN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-05A65837-6D0A-4B42-9621-DAD99B0ECBE9)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_EM_INSTANCES_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-D55ED2D1-1A36-46BD-B396-766C34FDCFA6)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_RESOURCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-DC60C627-BBAD-4FB1-A678-F76E401D9A0E)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_UPDATE_EM_WAREHOUSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-6DF02E9E-F51E-42CA-8E48-0792D134B3AA)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-B5EB8655-33EE-434E-AFBE-239AF35D87D9)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-6F6A5F45-C59E-4448-9EA6-8B54B400C052)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-3D50D2D2-F743-462E-BC7C-7ACBED707AE9)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-8BCE7987-D628-4BC7-95B4-A957C36D1D86)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-C8B0B294-DDD8-46BA-BB89-0BCF378ACC91)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-56356825-32A2-46C6-907E-EC39F4B6BBB9)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-20AE294A-14CF-47A5-8F86-3C60176CB98C)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-54C184C5-3C87-4506-806A-852059B3D84D)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-16F11460-EED4-4002-BA3F-5EB34990F9F8)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-36A80074-7696-4511-B31C-8BECC243ED16)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-0AFCD046-66E5-41FB-A914-326AC99074CF)
- [DBMS_CLOUD_OCI_EM_WAREHOUSE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/em_warehouse_t.html#ADSDK-GUID-52B51306-0A16-4195-9351-1AC27201A294)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
