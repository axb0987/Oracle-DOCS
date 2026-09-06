# Monitoring Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#dcoc-content-body)

## Monitoring Common Types

### DBMS_CLOUD_OCI_MONITORING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_AGGREGATED_DATAPOINT_T Type

A timestamp-value pair returned for the specified request.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) The date and time associated with the value of this data point. Format defined by RFC3339. Example: `2019-02-01T01:02:29.600Z`

`value`

(required) Numeric value of the metric. Example: `10.4`

### DBMS_CLOUD_OCI_MONITORING_SUPPRESSION_T Type

The configuration details for suppressing an alarm. For information about alarms, see[Alarms Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview).

Syntax
```

```

Fields

Field Description

`description`

(optional) Human-readable reason for suppressing alarm notifications. It does not have to be unique, and it's changeable. Avoid entering confidential information. Oracle recommends including tracking information for the event or associated work, such as a ticket number. Example: `Planned outage due to change IT-1234.`

`time_suppress_from`

(required) The start date and time for the suppression to take place, inclusive. Format defined by RFC3339. Example: `2019-02-01T01:02:29.600Z`

`time_suppress_until`

(required) The end date and time for the suppression to take place, inclusive. Format defined by RFC3339. Example: `2019-02-01T02:02:29.600Z`

### DBMS_CLOUD_OCI_MONITORING_ALARM_T Type

The properties that define an alarm. For information about alarms, see[Alarms Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the alarm.

`display_name`

(required) A user-friendly name for the alarm. It does not have to be unique, and it's changeable. This value determines the title of each alarm notification. Example: `High CPU Utilization`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the alarm.

`metric_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric being evaluated by the alarm.

`metric_compartment_id_in_subtree`

(optional) When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false. Example: `true`

`namespace`

(required) The source service or application emitting the metric that is evaluated by the alarm. Example: `oci_computeagent`

`resource_group`

(optional) Resource group to match for metric data retrieved by the alarm. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Example: `frontend-fleet`

`query`

(required) The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval depend on the specified time range. More interval values are supported for smaller time ranges. You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For information about writing MQL expressions, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For details about MQL, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example of threshold alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) &gt; 85 ----- Example of absence alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent() -----

`resolution`

(optional) The time between calculated aggregation windows for the alarm. Supported value: `1m`

`pending_duration`

(optional) The period of time that the condition defined in the alarm must persist before the alarm state changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the alarm must persist in breaching the condition for five minutes before the alarm updates its state to \"FIRING\". The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H` for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M. Under the default value of PT1M, the first evaluation that breaches the alarm updates the state to \"FIRING\". The alarm updates its status to \"OK\" when the breaching condition has been clear for the most recent minute. Example: `PT5M`

`severity`

(required) The perceived type of response required when the alarm is in the \"FIRING\" state. Example: `CRITICAL`

Allowed values are: 'CRITICAL', 'ERROR', 'WARNING', 'INFO'

`body`

(optional) The human-readable content of the delivered alarm notification. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Example: `High CPU usage alert. Follow runbook instructions for resolution.`

`is_notifications_per_metric_dimension_enabled`

(optional) When set to `true`, splits alarm notifications per metric stream. When set to `false`, groups alarm notifications across metric streams.

`message_format`

(optional) The format to use for alarm notifications. The formats are: * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format. * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only. * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to Email subscription types only.

Allowed values are: 'RAW', 'PRETTY_JSON', 'ONS_OPTIMIZED'

`destinations`

(required) A list of destinations for alarm notifications. Each destination is represented by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a related resource, such as a`NOTIFICATION_TOPIC`Type. Supported destination services: Notifications , Streaming. Limit: One destination per supported destination service.

`repeat_notification_duration`

(optional) The frequency for re-submitting alarm notifications, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D. Default value: null (notifications are not re-submitted). Example: `PT2H`

`suppression`

(optional) The configuration details for suppressing an alarm.

`is_enabled`

(required) Whether the alarm is enabled. Example: `true`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(required) The current lifecycle state of the alarm. Example: `DELETED`

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the alarm was created. Format defined by RFC3339. Example: `2019-02-01T01:02:29.600Z`

`time_updated`

(required) The date and time the alarm was last updated. Format defined by RFC3339. Example: `2019-02-03T01:02:29.600Z`

### DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_ENTRY_T Type

A timestamped alarm state entry for a metric stream.

Syntax
```

```

Fields

Field Description

`dimensions`

(required) Indicator of the metric stream associated with the alarm state entry. Includes one or more dimension key-value pairs.

`status`

(required) Transition state (status value) associated with the alarm state entry. Example: `FIRING`

Allowed values are: 'FIRING', 'OK'

`l_timestamp`

(required) Transition time associated with the alarm state entry. Format defined by RFC3339. Example: `2022-02-01T01:02:29.600Z`

### DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_monitoring_alarm_dimension_states_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_COLLECTION_T Type

The list of current alarm state entries for each metric stream that matches the filters.

Syntax
```

```

Fields

Field Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the alarm to retrieve alarm state entries for.

`is_enabled`

(required) Whether the alarm is enabled. Example: `true`

`is_notifications_per_metric_dimension_enabled`

(required) When set to `true`, splits alarm notifications per metric stream. When set to `false`, groups alarm notifications across metric streams.

`items`

(required) Array of alarm state entries.

### DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_ENTRY_T Type

An alarm history entry indicating a description of the entry and the time that the entry occurred. If the entry corresponds to a state transition, such as OK to Firing, then the entry also includes a transition timestamp.

Syntax
```

```

Fields

Field Description

`summary`

(required) Description for this alarm history entry. Example 1 - alarm state history entry: `The alarm state is FIRING` Example 2 - alarm state transition history entry: `State transitioned from OK to Firing`

`l_timestamp`

(required) Timestamp for this alarm history entry. Format defined by RFC3339. Example: `2019-02-01T01:02:29.600Z`

`timestamp_triggered`

(optional) Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing. Available for state transition entries only. Note: A three-minute lag for this value accounts for any late-arriving metrics. Example: `2019-02-01T0:59:00.789Z`

### DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_monitoring_alarm_history_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_COLLECTION_T Type

The configuration details for retrieving alarm history.

Syntax
```

```

Fields

Field Description

`alarm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the alarm to retrieve history for.

`is_enabled`

(required) Whether the alarm is enabled. Example: `true`

`entries`

(required) The set of history entries retrieved for the alarm.

### DBMS_CLOUD_OCI_MONITORING_ALARM_STATUS_SUMMARY_T Type

A summary of properties for the specified alarm and its current evaluation status. For information about alarms, see[Alarms Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the alarm.

`display_name`

(required) The configured name of the alarm. Example: `High CPU Utilization`

`severity`

(required) The configured severity of the alarm. Example: `CRITICAL`

Allowed values are: 'CRITICAL', 'ERROR', 'WARNING', 'INFO'

`timestamp_triggered`

(required) Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing. Note: A three-minute lag for this value accounts for any late-arriving metrics. Example: `2019-02-01T01:02:29.600Z`

`status`

(required) The status of this alarm. Status is collective, across all metric streams in the alarm. To list alarm status for each metric stream, use`RETRIEVE_DIMENSION_STATES`Function. Example: `FIRING`

Allowed values are: 'FIRING', 'OK', 'SUSPENDED'

`suppression`

(optional) The configuration details for suppressing an alarm.

### DBMS_CLOUD_OCI_MONITORING_ALARM_SUMMARY_T Type

A summary of properties for the specified alarm. For information about alarms, see[Alarms Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the alarm.

`display_name`

(required) A user-friendly name for the alarm. It does not have to be unique, and it's changeable. This value determines the title of each alarm notification. Example: `High CPU Utilization`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the alarm.

`metric_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric being evaluated by the alarm.

`namespace`

(required) The source service or application emitting the metric that is evaluated by the alarm. Example: `oci_computeagent`

`query`

(required) The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval depend on the specified time range. More interval values are supported for smaller time ranges. Supported grouping functions: `grouping()`, `groupBy()`. For information about writing MQL expressions, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For details about MQL, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example of threshold alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) &gt; 85 ----- Example of absence alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent() -----

`severity`

(required) The perceived severity of the alarm with regard to the affected system. Example: `CRITICAL`

Allowed values are: 'CRITICAL', 'ERROR', 'WARNING', 'INFO'

`destinations`

(required) A list of destinations for alarm notifications. Each destination is represented by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a related resource, such as a`NOTIFICATION_TOPIC`Type. Supported destination services: Notifications , Streaming. Limit: One destination per supported destination service.

`suppression`

(optional) The configuration details for suppressing an alarm.

`is_enabled`

(required) Whether the alarm is enabled. Example: `true`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(required) The current lifecycle state of the alarm. Example: `DELETED`

### DBMS_CLOUD_OCI_MONITORING_CHANGE_ALARM_COMPARTMENT_DETAILS_T Type

The configuration details for moving an alarm.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the alarm to.

### DBMS_CLOUD_OCI_MONITORING_CREATE_ALARM_DETAILS_T Type

The configuration details for creating an alarm.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name for the alarm. It does not have to be unique, and it's changeable. Avoid entering confidential information. This value determines the title of each alarm notification. Example: `High CPU Utilization`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the alarm.

`metric_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric being evaluated by the alarm.

`metric_compartment_id_in_subtree`

(optional) When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false. Example: `true`

`namespace`

(required) The source service or application emitting the metric that is evaluated by the alarm. Example: `oci_computeagent`

`resource_group`

(optional) Resource group that you want to match. A null value returns only metric data that has no resource groups. The alarm retrieves metric data associated with the specified resource group only. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Avoid entering confidential information. Example: `frontend-fleet`

`query`

(required) The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval depend on the specified time range. More interval values are supported for smaller time ranges. You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For information about writing MQL expressions, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For details about MQL, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example of threshold alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) &gt; 85 ----- Example of absence alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent() -----

`resolution`

(optional) The time between calculated aggregation windows for the alarm. Supported value: `1m`

`pending_duration`

(optional) The period of time that the condition defined in the alarm must persist before the alarm state changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the alarm must persist in breaching the condition for five minutes before the alarm updates its state to \"FIRING\". The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H` for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M. Under the default value of PT1M, the first evaluation that breaches the alarm updates the state to \"FIRING\". The alarm updates its status to \"OK\" when the breaching condition has been clear for the most recent minute. Example: `PT5M`

`severity`

(required) The perceived type of response required when the alarm is in the \"FIRING\" state. Example: `CRITICAL`

`body`

(optional) The human-readable content of the delivered alarm notification. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Avoid entering confidential information. Example: `High CPU usage alert. Follow runbook instructions for resolution.`

`is_notifications_per_metric_dimension_enabled`

(optional) When set to `true`, splits alarm notifications per metric stream. When set to `false`, groups alarm notifications across metric streams. Example: `true`

`message_format`

(optional) The format to use for alarm notifications. The formats are: * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format. * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only. * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to Email subscription types only.

Allowed values are: 'RAW', 'PRETTY_JSON', 'ONS_OPTIMIZED'

`destinations`

(required) A list of destinations for alarm notifications. Each destination is represented by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a related resource, such as a`NOTIFICATION_TOPIC`Type. Supported destination services: Notifications , Streaming. Limit: One destination per supported destination service.

`repeat_notification_duration`

(optional) The frequency for re-submitting alarm notifications, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D. Default value: null (notifications are not re-submitted). Example: `PT2H`

`suppression`

(optional) The configuration details for suppressing an alarm.

`is_enabled`

(required) Whether the alarm is enabled. Example: `true`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_MONITORING_DATAPOINT_T Type

Metric value for a specific timestamp.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) Timestamp for this metric value. Format defined by RFC3339. For a data point to be posted, its timestamp must be near current time (less than two hours in the past and less than 10 minutes in the future). Example: `2019-02-01T01:02:29.600Z`

`value`

(required) Numeric value of the metric. Example: `10.23`

`l_count`

(optional) The number of occurrences of the associated value in the set of data. Default is 1. Value must be greater than zero.

### DBMS_CLOUD_OCI_MONITORING_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_MONITORING_DATAPOINT_TBL Type

Nested table type of dbms_cloud_oci_monitoring_datapoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_DETAILS_T Type

A metric object containing raw metric data points to be posted to the Monitoring service.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The source service or application emitting the metric. A valid namespace value starts with an alphabetical character and includes only alphanumeric characters and underscores. The \"oci_\" prefix is reserved. Avoid entering confidential information. Example: `my_namespace`

`resource_group`

(optional) Resource group to assign to the metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Avoid entering confidential information. Example: `frontend-fleet`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to use for metrics.

`name`

(required) The name of the metric. A valid name value starts with an alphabetical character and includes only alphanumeric characters, dots, underscores, hyphens, and dollar signs. The `oci_` prefix is reserved. Avoid entering confidential information. Example: `my_app.success_rate`

`dimensions`

(required) Qualifiers provided in a metric definition. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair. A valid dimension key includes only printable ASCII, excluding spaces. The character limit for a dimension key is 256. A valid dimension value includes only Unicode characters. The character limit for a dimension value is 512. Empty strings are not allowed for keys or values. Avoid entering confidential information. Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`

`metadata`

(optional) Properties describing metrics. These are not part of the unique fields identifying the metric. Each metadata item takes the form of a key-value pair. The character limit for a metadata key is 256. The character limit for a metadata value is 256. Example: `\"unit\": \"bytes\"`

`datapoints`

(required) A list of metric values with timestamps. At least one data point is required per call. For a data point to be posted, its timestamp must be near current time (less than two hours in the past and less than 10 minutes in the future).

### DBMS_CLOUD_OCI_MONITORING_FAILED_METRIC_RECORD_T Type

The record of a single metric object that failed input validation and the reason for the failure.

Syntax
```

```

Fields

Field Description

`message`

(required) An error message indicating the reason that the indicated metric object failed input validation.

`metric_data`

(required) Identifier of a metric object that failed input validation.

### DBMS_CLOUD_OCI_MONITORING_LIST_METRICS_DETAILS_T Type

The request details for retrieving metric definitions. Specify optional properties to filter the returned results. Use an asterisk (&amp;#42;) as a wildcard character, placed anywhere in the string. For example, to search for all metrics with names that begin with \"disk\", specify \"name\" as \"disk&amp;#42;\". If no properties are specified, then all metric definitions within the request scope are returned.

Syntax
```

```

Fields

Field Description

`name`

(optional) The metric name to use when searching for metric definitions. Example: `CpuUtilization`

`namespace`

(optional) The source service or application to use when searching for metric definitions. Example: `oci_computeagent`

`resource_group`

(optional) Resource group that you want to match. A null value returns only metric data that has no resource groups. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Example: `frontend-fleet`

`dimension_filters`

(optional) Qualifiers that you want to use when searching for metric definitions. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair. Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`

`group_by`

(optional) Group metrics by these fields in the response. For example, to list all metric namespaces available in a compartment, groupBy the \"namespace\" field. Supported fields: namespace, name, resourceGroup. If `groupBy` is used, then `dimensionFilters` is ignored. Example - group by namespace: `[ \"namespace\" ]`

`sort_by`

(optional) The field to use when sorting returned metric definitions. Only one sorting level is provided. Example: `NAMESPACE`

Allowed values are: 'NAMESPACE', 'NAME', 'RESOURCEGROUP'

`sort_order`

(optional) The sort order to use when sorting returned metric definitions. Ascending (ASC) or descending (DESC). Example: `ASC`

Allowed values are: 'ASC', 'DESC'

### DBMS_CLOUD_OCI_MONITORING_METRIC_T Type

The properties that define a metric. For information about metrics, see[Metrics Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview).

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the metric. Example: `CpuUtilization`

`namespace`

(optional) The source service or application emitting the metric. Example: `oci_computeagent`

`resource_group`

(optional) Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Example: `frontend-fleet`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources monitored by the metric.

`dimensions`

(optional) Qualifiers provided in a metric definition. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair. Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`

### DBMS_CLOUD_OCI_MONITORING_AGGREGATED_DATAPOINT_TBL Type

Nested table type of dbms_cloud_oci_monitoring_aggregated_datapoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_T Type

The set of aggregated data returned for a metric. For information about metrics, see[Metrics Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview). Limits information for returned data follows. * Data points: 100,000. * Metric streams* within data points: 2,000. * Time range returned for 1-day resolution: 90 days. * Time range returned for 1-hour resolution: 90 days. * Time range returned for 5-minute resolution: 30 days. * Time range returned for 1-minute resolution: 7 days. *A metric stream is an individual set of aggregated data for a metric with zero or more dimension values. Metric streams cannot be aggregated across metric groups. A metric group is the combination of a given metric, metric namespace, and tenancy for the purpose of determining limits. For more information about metric-related concepts, see[Monitoring Concepts](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts).

Syntax
```

```

Fields

Field Description

`namespace`

(required) The reference provided in a metric definition to indicate the source service or application that emitted the metric. Example: `oci_computeagent`

`resource_group`

(optional) Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Example: `frontend-fleet`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resources that the aggregated data was returned from.

`name`

(required) The name of the metric. Example: `CpuUtilization`

`dimensions`

(required) Qualifiers provided in the definition of the returned metric. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair. Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`

`metadata`

(optional) The references provided in a metric definition to indicate extra information about the metric. Example: `\"unit\": \"bytes\"`

`resolution`

(optional) The time between calculated aggregation windows. Use with the query interval to vary the frequency for returning aggregated data points. For example, use a query interval of 5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute frequency. The resolution must be equal or less than the interval in the query. The default resolution is 1m (one minute). Supported values: `1m`-`60m`, `1h`-`24h`, `1d`. Example: `5m`

`aggregated_datapoints`

(required) The list of timestamp-value pairs returned for the specified request. Metric values are rolled up to the start time specified in the request. For important limits information related to data points, see MetricData Reference at the top of this page.

### DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_monitoring_metric_data_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_POST_METRIC_DATA_DETAILS_T Type

An array of metric objects containing raw metric data points to be posted to the Monitoring service.

Syntax
```

```

Fields

Field Description

`metric_data`

(required) A metric object containing raw metric data points to be posted to the Monitoring service.

`batch_atomicity`

(optional) Batch atomicity behavior. Requires either partial or full pass of input validation for metric objects in PostMetricData requests. The default value of NON_ATOMIC requires a partial pass: at least one metric object in the request must pass input validation, and any objects that failed validation are identified in the returned summary, along with their error messages. A value of ATOMIC requires a full pass: all metric objects in the request must pass input validation. Example: `NON_ATOMIC`

Allowed values are: 'ATOMIC', 'NON_ATOMIC'

### DBMS_CLOUD_OCI_MONITORING_FAILED_METRIC_RECORD_TBL Type

Nested table type of dbms_cloud_oci_monitoring_failed_metric_record_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MONITORING_POST_METRIC_DATA_RESPONSE_DETAILS_T Type

The response object returned from a PostMetricData operation.

Syntax
```

```

Fields

Field Description

`failed_metrics_count`

(required) The number of metric objects that failed input validation.

`failed_metrics`

(optional) A list of records identifying metric objects that failed input validation and the reasons for the failures.

### DBMS_CLOUD_OCI_MONITORING_RETRIEVE_DIMENSION_STATES_DETAILS_T Type

The configuration details for retrieving the alarm state entries. Filter retrieved alarm state entries by status value and dimension key-value pairs.

Syntax
```

```

Fields

Field Description

`dimension_filters`

(optional) A filter to return only alarm state entries that match the exact set of specified dimension key-value pairs. If you specify `\"availabilityDomain\": \"phx-ad-1\"` but the alarm state entry corresponds to the set `\"availabilityDomain\": \"phx-ad-1\"` and `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`, then no results are returned.

`status`

(optional) A filter to return only alarm state entries that match the status value. Example: `FIRING`

### DBMS_CLOUD_OCI_MONITORING_SUMMARIZE_METRICS_DATA_DETAILS_T Type

The request details for retrieving aggregated data. Use the query and optional properties to filter the returned results.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The source service or application to use when searching for metric data points to aggregate. Example: `oci_computeagent`

`resource_group`

(optional) Resource group that you want to match. A null value returns only metric data that has no resource groups. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Example: `frontend-fleet`

`query`

(required) The Monitoring Query Language (MQL) expression to use when searching for metric data points to aggregate. The query must specify a metric, statistic, and interval. Supported values for interval depend on the specified time range. More interval values are supported for smaller time ranges. You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. Construct your query to avoid exceeding limits on returned data. See`METRIC_DATA`Type. For details about Monitoring Query Language (MQL), see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example: `CpuUtilization[1m].sum()`

`start_time`

(optional) The beginning of the time range to use when searching for metric data points. Format is defined by RFC3339. The response includes metric data points for the startTime. Default value: the timestamp 3 hours before the call was sent. Example: `2019-02-01T01:02:29.600Z`

`end_time`

(optional) The end of the time range to use when searching for metric data points. Format is defined by RFC3339. The response excludes metric data points for the endTime. Default value: the timestamp representing when the call was sent. Example: `2019-02-01T02:02:29.600Z`

`resolution`

(optional) The time between calculated aggregation windows. Use with the query interval to vary the frequency for returning aggregated data points. For example, use a query interval of 5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute frequency. The resolution must be equal or less than the interval in the query. The default resolution is 1m (one minute). Supported values: `1m`-`60m`, `1h`-`24h`, `1d`. Example: `5m`

### DBMS_CLOUD_OCI_MONITORING_UPDATE_ALARM_DETAILS_T Type

The configuration details for updating an alarm.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the alarm. It does not have to be unique, and it's changeable. Avoid entering confidential information. This value determines the title of each alarm notification. Example: `High CPU Utilization`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the alarm.

`metric_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the metric being evaluated by the alarm.

`metric_compartment_id_in_subtree`

(optional) When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false. Example: `true`

`namespace`

(optional) The source service or application emitting the metric that is evaluated by the alarm. Example: `oci_computeagent`

`resource_group`

(optional) Resource group that you want to match. A null value returns only metric data that has no resource groups. The alarm retrieves metric data associated with the specified resource group only. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Avoid entering confidential information. Example: `frontend-fleet`

`query`

(optional) The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval depend on the specified time range. More interval values are supported for smaller time ranges. You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For information about writing MQL expressions, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For details about MQL, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example of threshold alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) &gt; 85 ----- Example of absence alarm: ----- CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent() -----

`resolution`

(optional) The time between calculated aggregation windows for the alarm. Supported value: `1m`

`pending_duration`

(optional) The period of time that the condition defined in the alarm must persist before the alarm state changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the alarm must persist in breaching the condition for five minutes before the alarm updates its state to \"FIRING\". The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H` for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M. Under the default value of PT1M, the first evaluation that breaches the alarm updates the state to \"FIRING\". The alarm updates its status to \"OK\" when the breaching condition has been clear for the most recent minute. Example: `PT5M`

`severity`

(optional) The perceived severity of the alarm with regard to the affected system. Example: `CRITICAL`

`body`

(optional) The human-readable content of the delivered alarm notification. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Avoid entering confidential information. Example: `High CPU usage alert. Follow runbook instructions for resolution.`

`is_notifications_per_metric_dimension_enabled`

(optional) When set to `true`, splits alarm notifications per metric stream. When set to `false`, groups alarm notifications across metric streams.

`message_format`

(optional) The format to use for alarm notifications. The formats are: * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format. * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only. * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to Email subscription types only.

Allowed values are: 'RAW', 'PRETTY_JSON', 'ONS_OPTIMIZED'

`destinations`

(optional) A list of destinations for alarm notifications. Each destination is represented by the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a related resource, such as a`NOTIFICATION_TOPIC`Type. Supported destination services: Notifications , Streaming. Limit: One destination per supported destination service.

`repeat_notification_duration`

(optional) The frequency for re-submitting alarm notifications, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D. Default value: null (notifications are not re-submitted). Example: `PT2H`

`suppression`

(optional) The configuration details for suppressing an alarm.

`is_enabled`

(optional) Whether the alarm is enabled. Example: `true`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Monitoring Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-A0788AF0-0414-4D2B-A093-682058132FCD)
- [DBMS_CLOUD_OCI_MONITORING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-F66B9BAB-9D70-415D-97C8-A9FD2214CD3B)
- [DBMS_CLOUD_OCI_MONITORING_AGGREGATED_DATAPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-06A7BCC8-9EF5-46EB-8824-460D5A786DDE)
- [DBMS_CLOUD_OCI_MONITORING_SUPPRESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-9BF85E1F-0EC5-4153-910F-A5F955DC2F36)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-4DF01E65-5AF0-4B82-A71B-BB123C54BDD4)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-B75206D6-D169-4237-9149-7EC844279442)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-08AFD66C-CC77-4397-8706-DA787AEF9D68)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_DIMENSION_STATES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-AD5623DA-15A7-4DB9-8DC6-959CE8361952)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-D526D499-6BDE-4C83-8CC5-8F4999147676)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-867F3F07-E7DD-4B1B-9D3E-701F73907BD4)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_HISTORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-527ED04B-C190-4220-AA1D-7B790EE3C4B4)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_STATUS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-99F54BBB-81FB-4AFD-8669-2F52ED31A768)
- [DBMS_CLOUD_OCI_MONITORING_ALARM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-15EBA959-BB18-482D-9596-0A1BC6628A9F)
- [DBMS_CLOUD_OCI_MONITORING_CHANGE_ALARM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-373DEE1F-318E-4B2C-94E0-D7F90B0EC5AF)
- [DBMS_CLOUD_OCI_MONITORING_CREATE_ALARM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-0BCF63AC-0F56-4856-A4A3-B2A51159B329)
- [DBMS_CLOUD_OCI_MONITORING_DATAPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-3623A0FC-F8D6-4B57-A381-F976E37423DF)
- [DBMS_CLOUD_OCI_MONITORING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-A812B12D-1AFB-441D-AFA5-CE703FCE4F25)
- [DBMS_CLOUD_OCI_MONITORING_DATAPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-1C80871C-9D4F-444F-B7C5-C5686D2096E3)
- [DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-917A8C28-905A-4815-ABDC-B90640AE138F)
- [DBMS_CLOUD_OCI_MONITORING_FAILED_METRIC_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-13769220-8B2F-4E4D-AF63-9C68F741EAB4)
- [DBMS_CLOUD_OCI_MONITORING_LIST_METRICS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-0E257075-16D1-453B-BA85-DEDB11762D6D)
- [DBMS_CLOUD_OCI_MONITORING_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-D5B15C6C-E8FC-4181-9B69-4FB1669EF3A7)
- [DBMS_CLOUD_OCI_MONITORING_AGGREGATED_DATAPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-3E34229F-C320-48AA-B9F3-99D184DEBA0B)
- [DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-A2F46864-3635-485E-8FD7-A945CBB0B288)
- [DBMS_CLOUD_OCI_MONITORING_METRIC_DATA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-DAC6398C-7404-4524-A549-A8B7D8ABA2FB)
- [DBMS_CLOUD_OCI_MONITORING_POST_METRIC_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-7525FCD9-2031-46DC-93C5-48BE5A2C56BE)
- [DBMS_CLOUD_OCI_MONITORING_FAILED_METRIC_RECORD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-DC6A9095-7C62-4813-8D38-55A600F07AA5)
- [DBMS_CLOUD_OCI_MONITORING_POST_METRIC_DATA_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-CA591012-698C-4EAA-8873-DCBCFDA00CAE)
- [DBMS_CLOUD_OCI_MONITORING_RETRIEVE_DIMENSION_STATES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-10BA6435-4807-4BCB-8380-DA1627E160DD)
- [DBMS_CLOUD_OCI_MONITORING_SUMMARIZE_METRICS_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-556580A0-3D34-4F04-86FB-D8B3DA920649)
- [DBMS_CLOUD_OCI_MONITORING_UPDATE_ALARM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/monitoring_t.html#ADSDK-GUID-72FC33F4-C13D-44A2-901E-56734EABC127)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
