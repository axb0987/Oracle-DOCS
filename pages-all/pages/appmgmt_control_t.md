# Application Management Control Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#dcoc-content-body)

## Application Management Control Common Types

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_ERROR_T Type

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_T Type

Description of Monitored Instance.

Syntax
```

```

Fields

Field Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored instance.

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`display_name`

(optional) A user-friendly name of the monitored instance. It is binded to[Compute Instance](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm). DisplayName is fetched from[Core Service API](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Instance/).

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Used to invoke manage operations on Management Agent Cloud Service.

`time_created`

(optional) The time the MonitoredInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the MonitoredInstance was updated. An RFC3339 formatted datetime string

`monitoring_state`

(optional) Monitoring status. Can be either enabled or disabled.

Allowed values are: 'ENABLED', 'DISABLED'

`lifecycle_state`

(optional) The current state of the monitored instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_SUMMARY_T Type

Summary of the monitored instance.

Syntax
```

```

Fields

Field Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of monitored instance.

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`display_name`

(optional) A user-friendly name of the monitored instance. It is binded to[Compute Instance](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm). DisplayName is fetched from[Core Service API](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Instance/).

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) The current state of the monitored instance.

`monitoring_state`

(optional) Monitoring status. Can be either enabled or disabled.

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_appmgmt_control_monitored_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_COLLECTION_T Type

Results of a monitored instance search. Contains MonitoredInstanceSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of monitored instances.

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_appmgmt_control_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'ACTIVATE_RESOURCE_MONITORING_PLUGIN', 'PUBLISH_TOP_PROCESSES_METRICS'

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_appmgmt_control_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_appmgmt_control_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'ACTIVATE_RESOURCE_MONITORING_PLUGIN', 'PUBLISH_TOP_PROCESSES_METRICS'

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

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_appmgmt_control_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Application Management Control Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-957F6570-8D38-4075-A8E9-0A9A9F85A649)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-1E98E066-147C-4240-A217-514C5336FF8B)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-7B4DFFA3-4EF9-4A7F-B274-84CCA92115EC)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-50909CF1-F47B-473C-9CE2-20207F403C7B)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-A7C7CEA0-1519-43D9-9428-BE7D4E2D56B3)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-FB4E437C-8F5C-462F-8C2B-27FC93635DFD)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_MONITORED_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-45BCA23F-92F6-467A-BD03-C1A1714ED6CA)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-89C70981-FC24-4C37-813B-45280DCD8AD4)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-2B938790-A788-4192-92A3-240BC0BA12D0)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-174E60A5-D8F6-4DE4-AD65-62787DEE768C)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-7F8FF7D0-8CE0-4BC9-AE72-7A63E52C1C55)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-8CBCE73E-B274-41EA-8164-611286A8067C)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-FB495BC8-D4D3-4D78-A071-8D7A6714B43E)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-7CEB7C70-5639-461E-8771-33E7AC1871D0)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-81BEDDE9-A7D0-47B7-A699-F3512452C9F1)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-6B63DB15-F299-4A1D-8C86-76B4B5CEBE3C)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-BE536F96-03F8-4760-B0F6-A61F98531D66)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-C958AC80-978D-4F3C-A069-3EC31213B453)
- [DBMS_CLOUD_OCI_APPMGMT_CONTROL_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/appmgmt_control_t.html#ADSDK-GUID-2D17E93B-50E4-4D0F-B249-89978026C831)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
