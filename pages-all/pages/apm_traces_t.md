# Application Performance Monitoring Traces Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#dcoc-content-body)

## Application Performance Monitoring Traces Common Types

### DBMS_CLOUD_OCI_APM_TRACES_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SNAPSHOT_DETAIL_T Type

A generic key value pair object, which contains information such as the thread ID, thread name, and thread state.

Syntax
```

```

Fields

Field Description

`key`

(optional) Name of the property.

`value`

(optional) Value of the property.

### DBMS_CLOUD_OCI_APM_TRACES_STACK_TRACE_ELEMENT_T Type

Stack trace element.

Syntax
```

```

Fields

Field Description

`method_name`

(optional) Name of the method containing the execution point.

`file_name`

(optional) Name of the source file containing the execution point.

`line_number`

(optional) Line number of the source line containing the execution point.

`class_name`

(optional) Name of the class containing the execution point.

`weightage`

(optional) The weight distribution that denotes the percentage occurrence of a method in the captured snapshots.

### DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_ABS_T

A branching tree with aggregated stack trace.

Syntax
```

```

Fields

Field Description

`stack_trace_element`

(optional)

### DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_ABS_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_aggregated_stack_trace_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_T Type

A branching tree with aggregated stack trace.

Syntax
```

```

Fields

Field Description

`children`

(optional) List of child aggregated stack trace to represent branches.

### DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_aggregated_stack_trace_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SNAPSHOT_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_snapshot_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_SNAPSHOT_T Type

Aggregated snapshots of all spans.

Syntax
```

```

Fields

Field Description

`details`

(required) Aggregated snapshot details.

`aggregated_stack_traces`

(required) List of aggregated stack trace.

### DBMS_CLOUD_OCI_APM_TRACES_ERROR_T Type

Details of an error that occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_DETAILS_T Type

Request object containing the query to be run against the trace data.

Syntax
```

```

Fields

Field Description

`query_text`

(optional) Application Performance Monitoring defined query string that filters and retrieves trace data results.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_ABS_T

Summary of the datatype, unit and related metadata of an individual row element of a query result row that is returned.

Syntax
```

```

Fields

Field Description

`data_type`

(optional) Datatype of the query result row element.

`unit`

(optional) Granular unit in which the query result row element's data is represented.

`display_name`

(optional) Alias name if an alias is used for the query result row element or an assigned display name from the query language in some default cases.

`expression`

(optional) Actual show expression in the user typed query that produced this column.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_ABS_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_query_result_row_type_summary_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_T Type

Summary of the datatype, unit and related metadata of an individual row element of a query result row that is returned.

Syntax
```

```

Fields

Field Description

`query_result_row_type_summaries`

(optional) A query result row type summary object that represents a nested table structure.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_query_result_row_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_GROUPED_BY_SUMMARY_T Type

Summary of the attribute based on which the query results are grouped.

Syntax
```

```

Fields

Field Description

`query_results_grouped_by_column`

(optional) Column or attribute in the query result, which is a group by value.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_ORDERED_BY_SUMMARY_T Type

Summary of the sort and order by attribute based on which the query results are organized.

Syntax
```

```

Fields

Field Description

`query_results_ordered_by`

(optional) Attribute by which the query results are sorted.

`query_results_sort_order`

(optional) The sort order for the attribute, either 'ASC' or 'DESC'.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_GROUPED_BY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_query_results_grouped_by_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_ORDERED_BY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_query_results_ordered_by_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_METADATA_SUMMARY_T Type

Summary containing the metadata about the query result set.

Syntax
```

```

Fields

Field Description

`query_result_row_type_summaries`

(optional) A collection of QueryResultRowTypeSummary objects that describe the type and properties of the individual row elements of the query rows being returned. The i-th element in this list contains the QueryResultRowTypeSummary of the i-th key-value pair in the QueryResultRowData map.

`source_name`

(optional) Source of the query result set (traces, spans, and so on).

`query_results_grouped_by`

(optional) Columns or attributes of the query rows which are group by values. This is a list of ResultsGroupedBy summary objects, and the list will contain as many elements as the attributes and aggregate functions in the group by clause in the select query.

`query_results_ordered_by`

(optional) Order by which the query results are organized. This is a list of queryResultsOrderedBy summary objects, and the list will contain more than one OrderedBy summary object, if the sort was multidimensional.

`time_series_interval_in_mins`

(optional) Interval for the time series function in minutes.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_T Type

Object that represents a single row of the query result. It contains the queryResultRowData object that contains the actual data represented by the elements of the query result row, and a queryResultRowMetadata object that contains the metadata about the data contained in the query result row.

Syntax
```

```

Fields

Field Description

`query_result_row_data`

(required) A map containing the actual data represented by a single row of the query result. The key is the column name or attribute specified in the show clause, or an aggregate function in the show clause. The value is the actual value of that attribute or aggregate function of the corresponding single row of the query result set. If an alias name is specified for an attribute or an aggregate function, then the key will be the alias name specified in the show clause. If an alias name is not specified for the group by aggregate function in the show clause, then the corresponding key will be the appropriate aggregate_function_name_column_name (For example: count(traces) will be keyed as count_traces). The datatype of the value is presented in the queryResultRowTypeSummaries list in the queryResultMetadata structure, where the i-th queryResultRowTypeSummary object represents the datatype of the i-th value when this map is iterated in order.

`query_result_row_metadata`

(required) A map containing metadata or add-on data for the data presented in the queryResultRowData map. Data required to present drill down information from the queryResultRowData is presented as key-value pairs.

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_query_result_row_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_RESPONSE_T Type

A response containing a collection of query rows (selected attributes and aggregations) filtered, grouped and sorted by the specified criteria from the query that is run, and the associated summary describing the corresponding query result metadata.

Syntax
```

```

Fields

Field Description

`query_result_metadata_summary`

(required)

`query_result_rows`

(required) A collection of objects with each object representing an individual row of the query result set. The total number of objects returned in this collection correspond to the total number of rows returned by the actual query that is run against the queried entity.

### DBMS_CLOUD_OCI_APM_TRACES_QUICK_PICK_SUMMARY_T Type

Summary of the Quick Pick query objects.

Syntax
```

```

Fields

Field Description

`quick_pick_name`

(required) Quick Pick name for the query.

`quick_pick_query`

(required) Query for the Quick Pick.

### DBMS_CLOUD_OCI_APM_TRACES_TAG_T Type

Definition of a tag which is a key-value pair.

Syntax
```

```

Fields

Field Description

`tag_name`

(required) Key that specifies the tag name.

`tag_value`

(required) Value associated with the tag key.

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_T Type

Definition of a log which is a key-value pair of log data.

Syntax
```

```

Fields

Field Description

`log_key`

(required) Key that specifies the log name.

`log_value`

(required) Value associated with the log key.

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_span_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_COLLECTION_T Type

Definition of span log collection object.

Syntax
```

```

Fields

Field Description

`time_created`

(optional) Timestamp at which the log is created.

`span_logs`

(optional) List of logs associated with the span at the given timestamp.

### DBMS_CLOUD_OCI_APM_TRACES_TAG_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_COLLECTION_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_span_log_collection_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_T Type

Definition of a span object.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier (spanId) for the span. Note that this field is defined as spanKey in the API and it maps to the spanId in the trace data in Application Performance Monitoring.

`parent_span_key`

(optional) Unique parent identifier for the span if one exists. For root spans this will be null.

`trace_key`

(required) Unique identifier for the trace.

`time_started`

(required) Span start time. Timestamp when the span was started.

`time_ended`

(required) Span end time. Timestamp when the span was completed.

`duration_in_ms`

(required) Total span duration in milliseconds.

`operation_name`

(required) Span name associated with the trace. This is usually the method or URI of the request.

`service_name`

(optional) Service name associated with the span.

`kind`

(optional) Kind associated with the span.

`tags`

(optional) List of tags associated with the span.

`logs`

(optional) List of logs associated with the span.

`is_error`

(required) Indicates if the span has an error.

### DBMS_CLOUD_OCI_APM_TRACES_STACK_TRACE_ELEMENT_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_stack_trace_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_THREAD_SNAPSHOT_T Type

Thread snapshot.

Syntax
```

```

Fields

Field Description

`time_stamp`

(optional) Snapshot time.

`thread_snapshot_details`

(optional) Snapshot details.

`stack_trace`

(optional) Stack trace.

### DBMS_CLOUD_OCI_APM_TRACES_THREAD_SNAPSHOT_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_thread_snapshot_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_ABS_T

Definition of a span snapshot object.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier (spanId) for the trace span.

`span_name`

(optional) Span name associated with the trace.

`time_started`

(required) Start time of the span.

`time_ended`

(required) End time of the span.

`span_snapshot_details`

(optional) Span snapshots properties.

`thread_snapshots`

(optional) Thread snapshots.

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_ABS_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_span_snapshot_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_T Type

Definition of a span snapshot object.

Syntax
```

```

Fields

Field Description

`children`

(optional) An array of child span snapshots.

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_span_snapshot_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_TRACE_SERVICE_SUMMARY_T Type

Summary of the spans in a trace by service.

Syntax
```

```

Fields

Field Description

`span_service_name`

(required) Name associated with the service.

`total_spans`

(required) Number of spans for serviceName in the trace.

`error_spans`

(required) Number of spans with errors for serviceName in the trace.

### DBMS_CLOUD_OCI_APM_TRACES_TRACE_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_trace_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_TRACE_SPAN_SUMMARY_T Type

Summary of the information pertaining to the spans in the trace window that is being queried.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier (traceId) for the trace that represents the span set. Note that this field is defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance Monitoring.

`root_span_operation_name`

(optional) Root span name associated with the trace. This is the flow start operation name. Null is displayed if the root span is not yet completed.

`time_earliest_span_started`

(required) Start time of the earliest span in the span collection.

`time_latest_span_ended`

(required) End time of the span that most recently ended in the span collection.

`span_count`

(required) The number of spans that have been processed by the system for the trace. Note that there could be additional spans that have not been processed or reported yet if the trace is still in progress.

`error_span_count`

(required) The number of spans with errors that have been processed by the system for the trace. Note that the number of spans with errors will be less than or equal to the total number of spans in the trace.

`root_span_service_name`

(optional) Service associated with the trace.

`time_root_span_started`

(optional) Start time of the root span for the span collection.

`time_root_span_ended`

(optional) End time of the root span for the span collection.

`root_span_duration_in_ms`

(optional) Time taken for the root span operation to complete in milliseconds.

`trace_duration_in_ms`

(required) Time between the start of the earliest span and the end of the most recent span in milliseconds.

`is_fault`

(required) Boolean flag that indicates whether the trace has an error.

`trace_status`

(required) The status of the trace. The trace statuses are defined as follows: complete - a root span has been recorded, but there is no information on the errors. success - a complete root span is recorded there is a successful error type and error code - HTTP 200. incomplete - the root span has not yet been received. error - the root span returned with an error. There may or may not be an associated error code or error type.

`trace_error_type`

(required) Error type of the trace.

`trace_error_code`

(required) Error code of the trace.

`service_summaries`

(optional) A summary of the spans by service.

### DBMS_CLOUD_OCI_APM_TRACES_SPAN_TBL Type

Nested table type of dbms_cloud_oci_apm_traces_span_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_TRACES_TRACE_T Type

Definition of a trace object.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier (traceId) for the trace that represents the span set. Note that this field is defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance Monitoring.

`root_span_operation_name`

(optional) Root span name associated with the trace. This is the flow start operation name. Null is displayed if the root span is not yet completed.

`time_earliest_span_started`

(optional) Start time of the earliest span in the span collection.

`time_latest_span_ended`

(optional) End time of the span that most recently ended in the span collection.

`span_count`

(optional) The number of spans that have been processed by the system for the trace. Note that there could be additional spans that have not been processed or reported yet if the trace is still in progress.

`error_span_count`

(optional) The number of spans with errors that have been processed by the system for the trace. Note that the number of spans with errors will be less than or equal to the total number of spans in the trace.

`root_span_service_name`

(optional) Service associated with the trace.

`time_root_span_started`

(optional) Start time of the root span for the span collection.

`time_root_span_ended`

(optional) End time of the root span for the span collection.

`root_span_duration_in_ms`

(optional) Time taken for the root span operation to complete in milliseconds.

`trace_duration_in_ms`

(optional) Time between the start of the earliest span and the end of the most recent span in milliseconds.

`is_fault`

(optional) Boolean flag that indicates whether the trace has an error.

`trace_status`

(optional) The status of the trace. The trace statuses are defined as follows: complete - a root span has been recorded, but there is no information on the errors. success - a complete root span is recorded there is a successful error type and error code - HTTP 200. incomplete - the root span has not yet been received. error - the root span returned with an error. There may or may not be an associated error code or error type.

`trace_error_type`

(optional) Error type of the trace.

`trace_error_code`

(optional) Error code of the trace.

`service_summaries`

(optional) A summary of the spans by service.

`span_summary`

(optional)

`spans`

(required) An array of spans in the trace.

### DBMS_CLOUD_OCI_APM_TRACES_TRACE_SNAPSHOT_T Type

Definition of a trace snapshot object.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier (traceId) for the trace that represents the span set. Note that this field is defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance Monitoring.

`time_started`

(optional) Start time of the trace.

`time_ended`

(optional) End time of the trace.

`trace_snapshot_details`

(optional) Trace snapshots properties.

`span_snapshots`

(required) List of spans.

- [Application Performance Monitoring Traces Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-78C168C1-DC3F-4D56-9014-CE6919E3D5EA)
- [DBMS_CLOUD_OCI_APM_TRACES_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-C368512F-D6FA-4005-B9C0-5EB82AE72E7A)
- [DBMS_CLOUD_OCI_APM_TRACES_SNAPSHOT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-1850CD6C-DBAC-4F21-96B5-C6B30D95AF58)
- [DBMS_CLOUD_OCI_APM_TRACES_STACK_TRACE_ELEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-DA373CEA-432B-44FE-9429-3659C0EC77B3)
- [DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-95A5B92B-35C1-40EF-96E3-CD13B6845F37)
- [DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-A0630742-9D3B-463A-B63B-A8EC06B783A8)
- [DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-51D3E94D-C04B-42C9-BE58-2C8B3510F8F6)
- [DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_STACK_TRACE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-65447FC2-AA0C-42A5-A438-34FA760BF907)
- [DBMS_CLOUD_OCI_APM_TRACES_SNAPSHOT_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-14DFB344-2337-47A3-8DCD-100E8AAE54FE)
- [DBMS_CLOUD_OCI_APM_TRACES_AGGREGATED_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-272B5645-1D64-4BE0-B487-AC152D4C5466)
- [DBMS_CLOUD_OCI_APM_TRACES_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-F3A6EC7A-534B-43DA-B809-CCEF276ACBC1)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-069EF442-34F3-4DE0-A785-14AF6C904FB1)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-87C7DC5B-9DE4-4C0B-A2CA-74E5127BC3AA)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-6EFE5F6D-43C2-4A2C-9B90-646F5059C623)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-6843FAB0-A3B8-4A07-BD4C-E103826D1862)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-31F6E07F-8241-4429-A88E-49F2EA685FE4)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_GROUPED_BY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-A66A4009-234C-44AC-9233-303D72DF2732)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_ORDERED_BY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-299F0AE3-DB78-4123-9E27-5F23A5D4D779)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_GROUPED_BY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-C9D6B789-FA5B-4113-95AC-A7B0B62BB52F)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULTS_ORDERED_BY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-19D42CA8-F83D-4F38-845F-AC0A890BB0EA)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-0BA412F0-6249-4062-83B4-9AEC52249DE3)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-F1983304-6897-429F-8E1C-8C8D6F8A4F26)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_ROW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-570B2D99-2494-42DE-9107-88D3F1DE79F5)
- [DBMS_CLOUD_OCI_APM_TRACES_QUERY_RESULT_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-CC8E5C86-9D17-4198-9AFE-60B6A4B81B5D)
- [DBMS_CLOUD_OCI_APM_TRACES_QUICK_PICK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-F64F9B9F-4CF2-4DBA-8C78-90BE51E04C41)
- [DBMS_CLOUD_OCI_APM_TRACES_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-75A30A60-B62F-4EF5-BE70-A2DA2028EFDB)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-82536B6A-CA83-449A-AEBE-2D02D011B284)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-BC878864-D269-4264-91B3-F27EAA26DD89)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-9E5D5700-DDEF-4195-BD75-B2620B91994B)
- [DBMS_CLOUD_OCI_APM_TRACES_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-73061411-D412-4F40-BC41-48A99456D257)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_LOG_COLLECTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-E16CD775-A8C9-4C83-B188-F8B0D4397570)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-978FFB18-4A51-430C-BFD9-833718C4E876)
- [DBMS_CLOUD_OCI_APM_TRACES_STACK_TRACE_ELEMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-A7A05CD9-BF0C-47F0-AF36-4C5D73C39CDF)
- [DBMS_CLOUD_OCI_APM_TRACES_THREAD_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-C71C1528-1AB2-413A-863C-6753F20C5968)
- [DBMS_CLOUD_OCI_APM_TRACES_THREAD_SNAPSHOT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-43AD90DD-8173-45EF-9AD4-47B7FF854DA6)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-755B4AC4-65FF-49CD-BB8D-C240A3C1A440)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-A40EA038-5BD1-4F1F-9FD0-D879F5E9B0FA)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-1569D37E-B7BF-44AE-8A23-F342C1F1B30F)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_SNAPSHOT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-8081001A-F3E3-48A3-90AC-266F8C330904)
- [DBMS_CLOUD_OCI_APM_TRACES_TRACE_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-5DB86255-7072-4857-9DBB-5578CA004138)
- [DBMS_CLOUD_OCI_APM_TRACES_TRACE_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-A45A6A32-EF3C-4A91-9C1D-90597A1A5D73)
- [DBMS_CLOUD_OCI_APM_TRACES_TRACE_SPAN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-D69EC401-1939-47AA-8876-B77A8C794408)
- [DBMS_CLOUD_OCI_APM_TRACES_SPAN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-D66053C2-9C0C-46C9-A511-5EF353CEDAED)
- [DBMS_CLOUD_OCI_APM_TRACES_TRACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-E33CD859-DFF5-4486-854B-EEDBA49A0E6D)
- [DBMS_CLOUD_OCI_APM_TRACES_TRACE_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_traces_t.html#ADSDK-GUID-F6BAE2A1-4F7A-4B09-8446-F0B8E3DCE07E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
