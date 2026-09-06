# Service Connector Hub Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#dcoc-content-body)

## Service Connector Hub Common Types

### DBMS_CLOUD_OCI_SCH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_CHANGE_SERVICE_CONNECTOR_COMPARTMENT_DETAILS_T Type

The configuration details for moving a service connector to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the service connector to.

### DBMS_CLOUD_OCI_SCH_SOURCE_DETAILS_T Type

An object that represents the source of the flow defined by the service connector. An example source is the VCNFlow logs within the NetworkLogs group. For more information about flows defined by service connectors, see[Service Connector Hub Overview](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm). For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

Fields

Field Description

`kind`

(required) The type descriminator.

Allowed values are: 'logging', 'monitoring', 'streaming'

### DBMS_CLOUD_OCI_SCH_TASK_DETAILS_T Type

An object that represents a task within the flow defined by the service connector. An example task is a filter for error logs. For more information about flows defined by service connectors, see[Service Connector Hub Overview](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm). For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

Fields

Field Description

`kind`

(required) The type descriminator.

Allowed values are: 'function', 'logRule'

### DBMS_CLOUD_OCI_SCH_TARGET_DETAILS_T Type

An object that represents the target of the flow defined by the service connector. An example target is a stream (Streaming service). For more information about flows defined by service connectors, see[Service Connector Hub Overview](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm). For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

Fields

Field Description

`kind`

(required) The type descriminator.

Allowed values are: 'functions', 'loggingAnalytics', 'monitoring', 'notifications', 'objectStorage', 'streaming'

### DBMS_CLOUD_OCI_SCH_TASK_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_sch_task_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_CREATE_SERVICE_CONNECTOR_DETAILS_T Type

The configuration details for creating a service connector.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the comparment to create the service connector in.

`description`

(optional) The description of the resource. Avoid entering confidential information.

`source`

(required)

`tasks`

(optional) The list of tasks.

`target`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SCH_DIMENSION_VALUE_DETAILS_T Type

Instructions for extracting the value corresponding to the specified dimension key: Either extract the value as-is (static) or derive the value from a path (evaluated).

Syntax
```

```

Fields

Field Description

`kind`

(required) The type of dimension value: static or evaluated.

Allowed values are: 'jmesPath', 'static'

### DBMS_CLOUD_OCI_SCH_DIMENSION_DETAILS_T Type

A dimension name and value.

Syntax
```

```

Fields

Field Description

`name`

(required) Dimension key. A valid dimension key includes only printable ASCII, excluding periods (.) and spaces. Custom dimension keys are acceptable. Avoid entering confidential information. Due to use by Service Connector Hub, the following dimension names are reserved: `connectorId`, `connectorName`, `connectorSourceType`. For information on valid dimension keys and values, see`METRIC_DATA_DETAILS`Function. Example: `type`

`dimension_value`

(required)

### DBMS_CLOUD_OCI_SCH_ERROR_T Type

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

### DBMS_CLOUD_OCI_SCH_FUNCTION_TASK_DETAILS_T Type

The Functions task. Batch input for a function can be limited by either size or time. The first limit reached determines the boundary of the batch. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_function_task_details_t`is a subtype of the`dbms_cloud_oci_sch_task_details_t`type.

Fields

Field Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the function to be used as a task.

`batch_size_in_kbs`

(optional) Size limit (kilobytes) for batch sent to invoke the function.

`batch_time_in_sec`

(optional) Time limit (seconds) for batch sent to invoke the function.

### DBMS_CLOUD_OCI_SCH_FUNCTIONS_TARGET_DETAILS_T Type

The function used for the Functions target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_functions_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the function.

### DBMS_CLOUD_OCI_SCH_JMES_PATH_DIMENSION_VALUE_T Type

Evaluated type of dimension value.

Syntax
```

```

`dbms_cloud_oci_sch_jmes_path_dimension_value_t`is a subtype of the`dbms_cloud_oci_sch_dimension_value_details_t`type.

Fields

Field Description

`path`

(required) The location to use for deriving the dimension value (evaluated). The path must start with `logContent` in an acceptable notation style with supported[JMESPath selectors](https://jmespath.org/specification.html): expression with dot and index operator (`.` and ``METRIC_DATA_DETAILS`Function. The returned value depends on the results of evaluation. If the evaluated value is valid, then the evaluated value is returned without double quotes. (Any front or trailing double quotes are trimmed before returning the value. For example, the evaluated value `\"compartmentId\"` is returned as `compartmentId`.) If the evaluated value is invalid, then the returned value is `SCH_EVAL_INVALID_VALUE`. If the evaluated value is empty, then the returned value is `SCH_EVAL_VALUE_EMPTY`.

### DBMS_CLOUD_OCI_SCH_STREAMING_CURSOR_DETAILS_T Type

The type of[cursor](https://docs.oracle.com/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm#usingcursors), which determines the starting point from which the stream will be consumed.

Syntax
```

```

Fields

Field Description

`kind`

(required) The type descriminator.

Allowed values are: 'LATEST', 'TRIM_HORIZON'

### DBMS_CLOUD_OCI_SCH_LATEST_STREAMING_CURSOR_T Type

`LATEST` cursor type. Sets the starting point for consuming the stream at messages published after saving the service connector. For more information about Streaming cursors, see[Using Cursors](https://docs.oracle.com/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm#usingcursors).

Syntax
```

```

`dbms_cloud_oci_sch_latest_streaming_cursor_t`is a subtype of the`dbms_cloud_oci_sch_streaming_cursor_details_t`type.

### DBMS_CLOUD_OCI_SCH_LOG_RULE_TASK_DETAILS_T Type

The log rule task. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_log_rule_task_details_t`is a subtype of the`dbms_cloud_oci_sch_task_details_t`type.

Fields

Field Description

`condition`

(required) A filter or mask to limit the source used in the flow defined by the service connector.

### DBMS_CLOUD_OCI_SCH_LOG_SOURCE_T Type

The logs for this Logging source.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the log source.

`log_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log group.

`log_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log.

### DBMS_CLOUD_OCI_SCH_LOGGING_ANALYTICS_TARGET_DETAILS_T Type

The log group used for the Logging Analytics target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_logging_analytics_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`log_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Logging Analytics log group.

`log_source_identifier`

(optional) Identifier of the log source that you want to use for processing data received from the service connector source. Applies to `StreamingSource` only. Equivalent to `name` at`LOG_ANALYTICS_SOURCE`Type.

### DBMS_CLOUD_OCI_SCH_LOG_SOURCE_TBL Type

Nested table type of dbms_cloud_oci_sch_log_source_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_LOGGING_SOURCE_DETAILS_T Type

The Logging source. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_logging_source_details_t`is a subtype of the`dbms_cloud_oci_sch_source_details_t`type.

Fields

Field Description

`log_sources`

(required) The logs for this Logging source.

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_NAMESPACE_DETAILS_T Type

Discriminator for namespaces in the compartment-specific list.

Syntax
```

```

Fields

Field Description

`kind`

(required) The type discriminator.

Allowed values are: 'selected'

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_T Type

A compartment-specific list of metric namespaces to retrieve data from.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric namespaces you want to use for the Monitoring source.

`namespace_details`

(required)

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_METRIC_DETAILS_T Type

The metrics to query for the specified metric namespace.

Syntax
```

```

Fields

Field Description

`kind`

(required) The type descriminator.

Allowed values are: 'all'

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_ALL_METRICS_T Type

Discriminator for metrics in the compartment-specific list.

Syntax
```

```

`dbms_cloud_oci_sch_monitoring_source_all_metrics_t`is a subtype of the`dbms_cloud_oci_sch_monitoring_source_metric_details_t`type.

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_TBL Type

Nested table type of dbms_cloud_oci_sch_monitoring_source_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_DETAILS_T Type

The Monitoring source. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_monitoring_source_details_t`is a subtype of the`dbms_cloud_oci_sch_source_details_t`type.

Fields

Field Description

`monitoring_sources`

(required) The list of metric namespaces to retrieve data from.

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_T Type

A metric namespace for the compartment-specific list.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The source service or application to use when querying for metric data points. Must begin with `oci_`. Example: `oci_computeagent`

`metrics`

(required)

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_TBL Type

Nested table type of dbms_cloud_oci_sch_monitoring_source_selected_namespace_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_DETAILS_T Type

The namespaces for the compartment-specific list.

Syntax
```

```

`dbms_cloud_oci_sch_monitoring_source_selected_namespace_details_t`is a subtype of the`dbms_cloud_oci_sch_monitoring_source_namespace_details_t`type.

Fields

Field Description

`namespaces`

(required) The namespaces for the compartment-specific list.

### DBMS_CLOUD_OCI_SCH_DIMENSION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_sch_dimension_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_MONITORING_TARGET_DETAILS_T Type

The metric and metric namespace used for the Monitoring target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_monitoring_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric.

`metric_namespace`

(required) The namespace of the metric. Example: `oci_computeagent`

`metric`

(required) The name of the metric. Example: `CpuUtilization`

`dimensions`

(optional) List of dimension names and values.

### DBMS_CLOUD_OCI_SCH_NOTIFICATIONS_TARGET_DETAILS_T Type

The topic used for the Notifications target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_notifications_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic.

`enable_formatted_messaging`

(optional) Whether to apply a simplified, user-friendly format to the message. Applies only when friendly formatting is supported by the service connector source and the subscription protocol. Example: `true`

### DBMS_CLOUD_OCI_SCH_OBJECT_STORAGE_TARGET_DETAILS_T Type

The bucket used for the Object Storage target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_object_storage_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`namespace`

(optional) The namespace.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information.

`object_name_prefix`

(optional) The prefix of the objects. Avoid entering confidential information.

`batch_rollover_size_in_m_bs`

(optional) The batch rollover size in megabytes.

`batch_rollover_time_in_ms`

(optional) The batch rollover time in milliseconds.

### DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_T Type

The configuration details of the flow defined by the service connector. For more information about flows defined by service connectors, see[Service Connector Hub Overview](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`description`

(optional) The description of the resource. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the service connector.

`time_created`

(required) The date and time when the service connector was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(required) The date and time when the service connector was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the service connector.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, the message might provide actionable information for a resource in a `FAILED` state.

`source`

(optional)

`tasks`

(optional) The list of tasks.

`target`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_SUMMARY_T Type

A summary of properties for the specified service connector.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`description`

(optional) The description of the resource. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the service connector.

`time_created`

(required) The date and time when the service connector was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(required) The date and time when the service connector was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the service connector.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, the message might provide actionable information for a resource in a `FAILED` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_sch_service_connector_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_COLLECTION_T Type

Collection of service connector property summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of items.

### DBMS_CLOUD_OCI_SCH_STATIC_DIMENSION_VALUE_T Type

Static type of dimension value (passed as-is).

Syntax
```

```

`dbms_cloud_oci_sch_static_dimension_value_t`is a subtype of the`dbms_cloud_oci_sch_dimension_value_details_t`type.

Fields

Field Description

`value`

(required) The data extracted from the specified dimension value (passed as-is). Unicode characters only. For information on valid dimension keys and values, see`METRIC_DATA_DETAILS`Function.

### DBMS_CLOUD_OCI_SCH_STREAMING_SOURCE_DETAILS_T Type

The Streaming source.

Syntax
```

```

`dbms_cloud_oci_sch_streaming_source_details_t`is a subtype of the`dbms_cloud_oci_sch_source_details_t`type.

Fields

Field Description

`stream_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream.

`l_cursor`

(optional)

### DBMS_CLOUD_OCI_SCH_STREAMING_TARGET_DETAILS_T Type

The stream used for the Streaming target. For configuration instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create).

Syntax
```

```

`dbms_cloud_oci_sch_streaming_target_details_t`is a subtype of the`dbms_cloud_oci_sch_target_details_t`type.

Fields

Field Description

`stream_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream.

### DBMS_CLOUD_OCI_SCH_TRIM_HORIZON_STREAMING_CURSOR_T Type

`TRIM_HORIZON` cursor type. Sets the starting point for consuming the stream at the oldest available message in the stream. For more information about Streaming cursors, see[Using Cursors](https://docs.oracle.com/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm#usingcursors).

Syntax
```

```

`dbms_cloud_oci_sch_trim_horizon_streaming_cursor_t`is a subtype of the`dbms_cloud_oci_sch_streaming_cursor_details_t`type.

### DBMS_CLOUD_OCI_SCH_UPDATE_SERVICE_CONNECTOR_DETAILS_T Type

The configuration details for updating a service connector.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`description`

(optional) The description of the resource. Avoid entering confidential information.

`source`

(optional)

`tasks`

(optional) The list of the tasks.

`target`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_RESOURCE_T Type

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

(required) An OCID or other unique identifier for the resource affected by the work request.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_sch_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_T Type

An object representing an asynchronous work flow. Many of the API requests you use to create and configure service connectors do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility for in-progress work flows. For more information about work requests, see[Viewing the State of a Work Request](https://docs.oracle.com/iaas/Content/service-connector-hub/workrequests.htm).

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of action the work request represents.

Allowed values are: 'CREATE_SERVICE_CONNECTOR', 'UPDATE_SERVICE_CONNECTOR', 'DELETE_SERVICE_CONNECTOR', 'ACTIVATE_SERVICE_CONNECTOR', 'DEACTIVATE_SERVICE_CONNECTOR'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time when the request was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_started`

(optional) The date and time when the request was started. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_finished`

(optional) The date and time when the object finished. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_sch_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_COLLECTION_T Type

Collection of work requests.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of items.

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The date and time when the error occurred. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_sch_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_COLLECTION_T Type

Collection of work request errors.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of items.

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The date and time when the log message was written. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_sch_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Collection of work request logs.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of items.

- [Service Connector Hub Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-719FC7F5-1671-47C9-9E46-EAC12616ABF7)
- [DBMS_CLOUD_OCI_SCH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-041EA933-2C76-4EE0-898E-7B5D839780DF)
- [DBMS_CLOUD_OCI_SCH_CHANGE_SERVICE_CONNECTOR_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-A9108325-1605-4BFF-B414-FB10D050A533)
- [DBMS_CLOUD_OCI_SCH_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-0F79C2F9-FE11-4191-9BAA-726FF50854F8)
- [DBMS_CLOUD_OCI_SCH_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-87DF24BF-57AF-46DC-BB89-E6AEB81C9139)
- [DBMS_CLOUD_OCI_SCH_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-00A86849-7ED2-462B-A3FF-99EEF3B1839B)
- [DBMS_CLOUD_OCI_SCH_TASK_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-79D02F72-A24B-4AC3-AEEE-0DF6B3E2A774)
- [DBMS_CLOUD_OCI_SCH_CREATE_SERVICE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-E3E66168-7C6F-4F29-A734-234582FB6C00)
- [DBMS_CLOUD_OCI_SCH_DIMENSION_VALUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-A880EF8A-D926-49EB-98AC-EC4DA5E91EB5)
- [DBMS_CLOUD_OCI_SCH_DIMENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-EABFBBA4-A7A1-4A31-BB7B-F8865B3BAFEC)
- [DBMS_CLOUD_OCI_SCH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-B4FF1467-20F3-4EDC-AAFC-D46E1A0DFDF0)
- [DBMS_CLOUD_OCI_SCH_FUNCTION_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-6573AF8D-DB6A-45B5-96FA-27928082E7FC)
- [DBMS_CLOUD_OCI_SCH_FUNCTIONS_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-82235F75-AC88-4939-86AC-2797540E323E)
- [DBMS_CLOUD_OCI_SCH_JMES_PATH_DIMENSION_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-0A64FAE6-446A-4E0B-BF51-85306A902F2B)
- [DBMS_CLOUD_OCI_SCH_STREAMING_CURSOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-3F5DBDA6-692B-47A7-A2A8-4999AF81D794)
- [DBMS_CLOUD_OCI_SCH_LATEST_STREAMING_CURSOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-0DC64F9B-76A2-45E1-98AC-045ED66FD04F)
- [DBMS_CLOUD_OCI_SCH_LOG_RULE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-73D2B010-5FD9-42A7-93FC-8F58FE80A8F6)
- [DBMS_CLOUD_OCI_SCH_LOG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-E9C2BBF3-3D3D-470A-93FA-0F243184C717)
- [DBMS_CLOUD_OCI_SCH_LOGGING_ANALYTICS_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-90F1C003-8DA4-4233-95EC-10DF2BA4B1FC)
- [DBMS_CLOUD_OCI_SCH_LOG_SOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-EFF3AA14-91CE-4995-BEBB-53D12F2A61EA)
- [DBMS_CLOUD_OCI_SCH_LOGGING_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-8B7B220A-61F8-4C9D-8B10-D912C5DEC5C1)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-DA8F8DCE-A00B-45C6-AAF5-850CC05DA928)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-B8C9167E-9C9E-446B-B864-22866874EF3D)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_METRIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-0F201F37-380B-4B18-AA33-24D362C3A915)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_ALL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-439456A7-96E8-45FF-970F-FF73DD6954A7)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-5E0F0C77-C744-4010-B124-18513C1476B7)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-2819E8C7-9A76-4A54-A94E-D1910DC8AAA9)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-17680551-39CA-423C-B5BB-0407C839DA99)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-9CBF6814-F966-42AF-8D72-9DEDDA7B62B6)
- [DBMS_CLOUD_OCI_SCH_MONITORING_SOURCE_SELECTED_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-D853DF93-EDD1-40A2-8F5A-F0B6AD342D68)
- [DBMS_CLOUD_OCI_SCH_DIMENSION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-2975E274-D0ED-4A07-A332-027D17C28003)
- [DBMS_CLOUD_OCI_SCH_MONITORING_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-58F0C8FA-ECBB-42CB-9C0B-B105D9DDE833)
- [DBMS_CLOUD_OCI_SCH_NOTIFICATIONS_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-6F3E6D95-45A8-4261-B9B0-B151822E5D34)
- [DBMS_CLOUD_OCI_SCH_OBJECT_STORAGE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-609EB60A-75C0-44B3-949E-035F06FB6CAA)
- [DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-B2F2D538-C2A9-4364-A0F2-1CCB1C1F09DC)
- [DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-2DDDB561-63D2-4A12-A154-8C9DC0CE84BC)
- [DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-9B893186-16C5-44F6-A332-AB3C4025A174)
- [DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-BBE863FE-8FAA-40CD-8686-595CAC573164)
- [DBMS_CLOUD_OCI_SCH_STATIC_DIMENSION_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-00BF556A-D47B-481C-9E1A-6678DA334137)
- [DBMS_CLOUD_OCI_SCH_STREAMING_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-1AA116BE-09FD-487F-8547-BD32E6A4EF60)
- [DBMS_CLOUD_OCI_SCH_STREAMING_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-7C767CD9-70B6-4EBA-91B4-028D171092A1)
- [DBMS_CLOUD_OCI_SCH_TRIM_HORIZON_STREAMING_CURSOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-AF01E8B5-B576-4CBF-A0F8-E1922EC5FC53)
- [DBMS_CLOUD_OCI_SCH_UPDATE_SERVICE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-5F638212-3596-4289-B96F-C2179FDC9CC9)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-B2E76AA3-707D-4F75-9579-6B49348215BC)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-BA5C59D5-7E28-4A37-80B5-3E4E1A97275B)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-F3B51A3B-0279-44C0-811B-1D10313A7741)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-2E2F3CE8-3D71-46B6-AA4C-81492DCBBDB8)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-4EE5B235-6BFB-499C-9B3F-81DB40E02632)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-E0B04C22-92D1-431A-9B5A-1C82EE26B214)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-3C4B4527-FCB5-49E7-A33D-15492BE449A0)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-AE1C0C90-2136-4145-8A74-9FE54749D9FE)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-3F67E854-9024-4C3B-A37B-29CD1F0602E1)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-E1EBFCEF-E536-4F6B-AF6F-67E425068937)
- [DBMS_CLOUD_OCI_SCH_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/sch_t.html#ADSDK-GUID-31890E75-3AB5-4ABF-B6A2-B27E801B265C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
