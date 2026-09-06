# Monitoring Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#dcoc-content-body)

## Monitoring Functions

Package: DBMS_CLOUD_OCI_MN_MONITORING

### CHANGE_ALARM_COMPARTMENT Function

Moves an alarm into a different compartment within the same tenancy. For more information, see[Moving an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm).

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`change_alarm_compartment_details`

(required) The configuration details for moving an alarm.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ALARM Function

Creates a new alarm in the specified compartment. For more information, see[Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`create_alarm_details`

(required) Document for creating an alarm.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ALARM Function

Deletes the specified alarm. For more information, see[Deleting an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/delete-alarm.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALARM Function

Gets the specified alarm. For more information, see[Getting an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALARM_HISTORY Function

Get the history of the specified alarm. For more information, see[Getting History of an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`alarm_historytype`

(optional) The type of history entries to retrieve. State history (STATE_HISTORY) or state transition history (STATE_TRANSITION_HISTORY). If not specified, entries of both types are retrieved. Example: `STATE_HISTORY`

Allowed values are: 'STATE_HISTORY', 'STATE_TRANSITION_HISTORY'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Default: 1000 Example: 500

`timestamp_greater_than_or_equal_to`

(optional) A filter to return only alarm history entries with timestamps occurring on or after the specified date and time. Format defined by RFC3339. Example: `2019-01-01T01:00:00.789Z`

`timestamp_less_than`

(optional) A filter to return only alarm history entries with timestamps occurring before the specified date and time. Format defined by RFC3339. Example: `2019-01-02T01:00:00.789Z`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALARMS Function

Lists the alarms for the specified compartment. For more information, see[Listing Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment. Example: `ocid1.compartment.oc1..exampleuniqueID`

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Default: 1000 Example: 500

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.

`lifecycle_state`

(optional) A filter to return only alarms that match the given lifecycle state exactly. When not specified, only alarms in the ACTIVE lifecycle state are listed.

`sort_by`

(optional) The field to use when sorting returned alarm definitions. Only one sorting level is provided. Example: `severity`

Allowed values are: 'displayName', 'severity'

`sort_order`

(optional) The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC). Example: `ASC`

Allowed values are: 'ASC', 'DESC'

`compartment_id_in_subtree`

(optional) When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALARMS_STATUS Function

List the status of each alarm in the specified compartment. Status is collective, across all metric streams in the alarm. To list alarm status for each metric stream, use`RETRIEVE_DIMENSION_STATES`Function. For more information, see[Listing Alarm Statuses](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm-status.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment. Example: `ocid1.compartment.oc1..exampleuniqueID`

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`compartment_id_in_subtree`

(optional) When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Default: 1000 Example: 500

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.

`sort_by`

(optional) The field to use when sorting returned alarm definitions. Only one sorting level is provided. Example: `severity`

Allowed values are: 'displayName', 'severity'

`sort_order`

(optional) The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC). Example: `ASC`

Allowed values are: 'ASC', 'DESC'

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a resource that is monitored by the metric that you are searching for. Example: `ocid1.instance.oc1.phx.exampleuniqueID`

`service_name`

(optional) A filter to return only resources that match the given service name exactly. Use this filter to list all alarms containing metric streams that match the *exact* service-name dimension. Example: `logging-analytics`

`entity_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the entity monitored by the metric that you are searching for. Example: `ocid1.instance.oc1.phx.exampleuniqueID`

`status`

(optional) The status of the metric stream to use for alarm filtering. For example, set `StatusQueryParam` to \"FIRING\" to filter results to metric streams of the alarm with that status. Default behaviour is to return alarms irrespective of metric streams' status. Example: `FIRING`

Allowed values are: 'FIRING', 'OK'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_METRICS Function

Returns metric definitions that match the criteria specified in the request. Compartment OCID required. For more information, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm). For information about metrics, see[Metrics Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment. Example: `ocid1.compartment.oc1..exampleuniqueID`

`list_metrics_details`

(required) The dimensions used to filter metrics.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Default: 1000 Example: 500

`compartment_id_in_subtree`

(optional) When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### POST_METRIC_DATA Function

Publishes raw metric data points to the Monitoring service. For a data point to be posted, its timestamp must be near current time (less than two hours in the past and less than 10 minutes in the future). For more information about publishing metrics, see[Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)and[Custom Metrics Walkthrough](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/custom-metrics-walkthrough.htm). For information about developing a metric-posting client, see[Developer Guide](https://docs.oracle.com/iaas/Content/API/Concepts/devtoolslanding.htm). For an example client, see[MonitoringMetricPostExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/MonitoringMetricPostExample.java). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). Per-call limits information follows. * Dimensions per metric group*. Maximum: 20. Minimum: 1. * Unique metric streams*. Maximum: 50. * Transactions Per Second (TPS) per-tenancy limit for this operation: 50. *A metric group is the combination of a given metric, metric namespace, and tenancy for the purpose of determining limits. A dimension is a qualifier provided in a metric definition. A metric stream is an individual set of aggregated data for a metric with zero or more dimension values. For more information about metric-related concepts, see[Monitoring Concepts](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts). **Note:** The endpoints for this operation differ from other Monitoring operations. Replace the string `telemetry` with `telemetry-ingestion` in the endpoint, as in the following example: https://telemetry-ingestion.eu-frankfurt-1.oraclecloud.com

Syntax
```

```

Parameters

Parameter Description

`post_metric_data_details`

(required) An array of metric objects containing raw metric data points to be posted to the Monitoring service.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`content_encoding`

(optional) The optional Content-Encoding header that defines the content encodings that were applied to the payload.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_ALARM_SUPPRESSION Function

Removes any existing suppression for the specified alarm. For more information, see[Removing Suppression from an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/remove-alarm-suppression.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRIEVE_DIMENSION_STATES Function

Lists the current alarm status of each metric stream, where status is derived from the metric stream's last associated transition. Optionally filter by status value and one or more dimension key-value pairs. For more information, see[Listing Metric Stream Status in an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Default: 1000 Example: 500

`retrieve_dimension_states_details`

(optional) The configuration details for retrieving the current alarm status of each metric stream.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_METRICS_DATA Function

Returns aggregated data that match the criteria specified in the request. Compartment OCID required. For more information, see[Querying Metric Data](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Creating a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment. Example: `ocid1.compartment.oc1..exampleuniqueID`

`summarize_metrics_data_details`

(required) The dimensions used to filter for metrics.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`compartment_id_in_subtree`

(optional) When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ALARM Function

Updates the specified alarm. For more information, see[Updating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm.htm). For important limits information, see[Limits on Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits). This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, or transactions, per second (TPS) for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an alarm.

`update_alarm_details`

(required) Document for updating an alarm.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://telemetry.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Monitoring Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-1D7BF3A1-CEAE-4D9C-A8E4-3291C95C5506)
- [CHANGE_ALARM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-075D2D37-7718-4769-8D84-E7B6A9E3E5DE)
- [CREATE_ALARM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-1418E415-7C08-4533-9B30-B42E1233C0EB)
- [DELETE_ALARM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-F6FD2A9E-1626-4BEC-9B80-3497CABB4DAB)
- [GET_ALARM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-57FE1DDD-8453-45D6-A7D7-6E1EF54E8EE9)
- [GET_ALARM_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-492A9182-6808-42E5-BEBE-1025B4F2C679)
- [LIST_ALARMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-CF38A510-7537-47C3-BFE4-B1007F810C44)
- [LIST_ALARMS_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-132EC092-3A4D-42B7-9B78-4E1BEE138225)
- [LIST_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-DD49A69B-BE0C-482C-8D8C-7B8DDB0DA62A)
- [POST_METRIC_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-ABED7368-846E-49FF-A4C1-967992DC3CCF)
- [REMOVE_ALARM_SUPPRESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-CD882D4F-11EA-4A22-AC29-E06267AC9AF0)
- [RETRIEVE_DIMENSION_STATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-8F65AEDF-8B4B-4F28-9368-C120618A770B)
- [SUMMARIZE_METRICS_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-969FC89C-4878-47BA-851D-584F82B56B1B)
- [UPDATE_ALARM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mn_monitoring.html#ADSDK-GUID-10A79B0E-8907-43B3-9B9A-39F65DD613D5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
