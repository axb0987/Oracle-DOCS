# Application Performance Monitoring Synthetics Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#dcoc-content-body)

## Application Performance Monitoring Synthetics Common Types

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_EXECUTION_T Type

Details of a vantage point execution.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the vantage point.

`executions`

(optional) List of execution times in milliseconds.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_EXECUTION_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_vantage_point_execution_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATE_NETWORK_DATA_DETAILS_T Type

Details of the vantage point and corresponding execution times.

Syntax
```

```

Fields

Field Description

`vantage_point_execution_times`

(required) List of VantagePointExecution items.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_NODE_T Type

Details of the vantage point node.

Syntax
```

```

Fields

Field Description

`id`

(optional) ID of the vantage point node.

`name`

(required) Name of the vantage point node.

`display_name`

(optional) Display name of the vantage point node.

`geo_info`

(optional) Geographical information of the vantage point node.

`outgoing_links`

(optional) Outgoing links from the vantage point node.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_LINK_T Type

Details of the link between two nodes.

Syntax
```

```

Fields

Field Description

`id`

(required) ID of the link.

`source`

(optional) ID of the source node.

`destination`

(optional) ID of the destination node.

`repeat_count`

(optional) Number of times the link is repeated.

`forwarding_loss`

(optional) Average packet loss.

`delay_in_milliseconds`

(optional) Difference of the packet response time between source and destination nodes, in milliseconds.

`min_delay_in_milliseconds`

(optional) Minimum delay in milliseconds.

`max_delay_in_milliseconds`

(optional) Maximum delay in milliseconds.

`paths`

(optional) List of all path IDs of which this link is part of.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_NODE_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_vantage_point_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATED_NETWORK_DATA_T Type

Details of the aggregated network data.

Syntax
```

```

Fields

Field Description

`result_state`

(required) Status of the aggregated network data result.

Allowed values are: 'SUCCESS', 'FAILURE', 'PARTIAL'

`vantage_point_nodes`

(optional) List of vantage point nodes.

`nodes_by_level`

(optional) An array of node arrays where each internal array corresponds to nodes at one level.

`links`

(optional) Map of link objects.

`error_details`

(optional) String containing error details.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATED_NETWORK_DATA_RESULT_T Type

The aggregated network results.

Syntax
```

```

Fields

Field Description

`aggregated_network_data`

(required)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_AVAILABILITY_CONFIGURATION_T Type

Monitor availability configuration details.

Syntax
```

```

Fields

Field Description

`max_allowed_failures_per_interval`

(optional) Maximum number of failed runs allowed in an interval. If an interval has more failed runs than the specified value, then the interval will be classified as UNAVAILABLE.

`min_allowed_runs_per_interval`

(optional) Minimum number of runs allowed in an interval. If an interval has fewer runs than the specified value, then the interval will be classified as UNKNOWN and will be excluded from the availability calculations.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DNS_CONFIGURATION_T Type

Information about the DNS settings.

Syntax
```

```

Fields

Field Description

`is_override_dns`

(optional) If isOverrideDns is true, then DNS settings will be overridden.

`override_dns_ip`

(optional) Attribute to override the DNS IP value. This value will be honored only if isOverrideDns is set to true.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VERIFY_TEXT_T Type

Details to verify text.

Syntax
```

```

Fields

Field Description

`text`

(optional) Verification text in the response.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_NETWORK_CONFIGURATION_T Type

Details of the network configuration.

Syntax
```

```

Fields

Field Description

`number_of_hops`

(optional) Number of hops.

`probe_per_hop`

(optional) Number of probes per hop.

`transmission_rate`

(optional) Number of probe packets sent out simultaneously.

`protocol`

(optional) Type of protocol.

Allowed values are: 'ICMP', 'TCP'

`probe_mode`

(optional) Type of probe mode when TCP protocol is selected.

Allowed values are: 'SACK', 'SYN'

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_CONFIGURATION_T Type

Details of monitor configuration.

Syntax
```

```

Fields

Field Description

`config_type`

(optional) Type of configuration.

Allowed values are: 'BROWSER_CONFIG', 'SCRIPTED_BROWSER_CONFIG', 'REST_CONFIG', 'SCRIPTED_REST_CONFIG', 'NETWORK_CONFIG'

`is_failure_retried`

(optional) If isFailureRetried is enabled, then a failed call will be retried.

`dns_configuration`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VERIFY_TEXT_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_verify_text_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_BROWSER_MONITOR_CONFIGURATION_T Type

Configuration details for the BROWSER monitor type.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_browser_monitor_configuration_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_monitor_configuration_t`type.

Fields

Field Description

`is_certificate_validation_enabled`

(optional) If certificate validation is enabled, then the call will fail in case of certification errors.

`is_default_snapshot_enabled`

(optional) If disabled, auto snapshots are not collected.

`verify_texts`

(optional) Verifies all the search strings present in the response. If any search string is not present in the response, then it will be considered as a failure.

`verify_response_codes`

(optional) Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_CLIENT_CERTIFICATE_T Type

Client certificate in PEM format.

Syntax
```

```

Fields

Field Description

`file_name`

(required) Name of the certificate file. The name should not contain any confidential information.

`content`

(required) Content of the client certificate file.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_PRIVATE_KEY_T Type

The private key associated with the client certificate in PEM format.

Syntax
```

```

Fields

Field Description

`file_name`

(required) Name of the private key file.

`content`

(required) Content of the private key file.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_CLIENT_CERTIFICATE_DETAILS_T Type

Details for client certificate.

Syntax
```

```

Fields

Field Description

`client_certificate`

(optional)

`private_key`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DVP_STACK_DETAILS_T Type

Details of a Dedicated Vantage Point (DVP) stack in Resource Manager.

Syntax
```

```

Fields

Field Description

`dvp_stack_type`

(required) Type of stack.

Allowed values are: 'ORACLE_RM_STACK'

`dvp_version`

(required) Version of the dedicated vantage point.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_DEDICATED_VANTAGE_POINT_DETAILS_T Type

Details of the request body used to create a new dedicated vantage point.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.

`dvp_stack_details`

(required)

`l_region`

(required) Name of the region.

`status`

(optional) Status of the dedicated vantage point.

Allowed values are: 'ENABLED', 'DISABLED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_T Type

Details of the script parameter that can be used to overwrite the parameter present in the script.

Syntax
```

```

Fields

Field Description

`param_name`

(required) Name of the parameter.

`param_value`

(required) Value of the parameter.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MAINTENANCE_WINDOW_SCHEDULE_T Type

Details required to schedule maintenance window.

Syntax
```

```

Fields

Field Description

`time_started`

(optional) Start time of the maintenance window, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_ended`

(optional) End time of the maintenance window, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_monitor_script_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_MONITOR_DETAILS_T Type

Details of the request body used to create a new monitor.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`monitor_type`

(required) Type of monitor.

Allowed values are: 'SCRIPTED_BROWSER', 'BROWSER', 'SCRIPTED_REST', 'REST', 'NETWORK'

`vantage_points`

(required) A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.

`script_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`status`

(optional) Enables or disables the monitor.

Allowed values are: 'ENABLED', 'DISABLED', 'INVALID'

`repeat_interval_in_seconds`

(required) Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.

`is_run_once`

(optional) If runOnce is enabled, then the monitor will run once.

`timeout_in_seconds`

(optional) Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.

`target`

(optional) Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is. For NETWORK monitor with TCP protocol, a port needs to be provided along with target. Example: 192.168.0.1:80

`script_parameters`

(optional) List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

`configuration`

(optional)

`availability_configuration`

(optional)

`maintenance_window_schedule`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_run_now`

(optional) If isRunNow is enabled, then the monitor will run immediately.

`scheduling_policy`

(optional) Scheduling policy to decide the distribution of monitor executions on vantage points.

Allowed values are: 'ALL', 'ROUND_ROBIN', 'BATCHED_ROUND_ROBIN'

`batch_interval_in_seconds`

(optional) Time interval between two runs in round robin batch mode (SchedulingPolicy - BATCHED_ROUND_ROBIN).

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_T Type

Details of the script parameters, paramName must be from the script content and these details can be used to overwrite the default parameter present in the script content.

Syntax
```

```

Fields

Field Description

`param_name`

(required) Name of the parameter.

`param_value`

(optional) Value of the parameter.

`is_secret`

(optional) If the parameter value is secret and should be kept confidential, then set isSecret to true.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_script_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_SCRIPT_DETAILS_T Type

Details of the request body used to create a new script. Only Side or JavaScript content types are supported and content should be in Side or JavaScript formats only.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`content_type`

(required) Content type of script.

Allowed values are: 'SIDE', 'JS'

`content`

(required) The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters. The format to set dynamic parameters is: `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;OS&gt;isParamValueSecret(true/false)&lt;/OS&gt;&lt;/ORAP&gt;`. Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false. Examples: With mandatory param name : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;/ORAP&gt;` With parameter name and value : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;/ORAP&gt;` Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.

`content_file_name`

(optional) File name of uploaded script content.

`parameters`

(optional) List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_STATUS_COUNT_MAP_T Type

Details of the monitor count per state. Example: `{ \"total\" : 5, \"enabled\" : 3 , \"disabled\" : 2, \"invalid\" : 0 }`

Syntax
```

```

Fields

Field Description

`total`

(required) Total number of monitors using the script.

`enabled`

(required) Number of enabled monitors using the script.

`disabled`

(required) Number of disabled monitors using the script.

`invalid`

(required) Number of invalid monitors using the script.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_T Type

The information about a dedicated vantage point.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated vantage point.

`display_name`

(required) Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.

`name`

(required) Unique permanent name of the dedicated vantage point. This is the same as the displayName.

`status`

(required) Status of the dedicated vantage point.

Allowed values are: 'ENABLED', 'DISABLED'

`dvp_stack_details`

(required)

`l_region`

(required) Name of the region.

`monitor_status_count_map`

(required)

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_SUMMARY_T Type

Information about dedicated vantage points.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated vantage point.

`display_name`

(required) Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.

`name`

(required) Unique permanent name of the vantage point.

`status`

(required) Status of the dedicated vantage point.

Allowed values are: 'ENABLED', 'DISABLED'

`dvp_stack_details`

(required)

`l_region`

(required) Name of the region.

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`monitor_status_count_map`

(required)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_dedicated_vantage_point_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_COLLECTION_T Type

The results of a dedicated vantage point search, which contains DedicatedVantagePointSummary items and other data in an APM domain.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DedicatedVantagePointSummary items.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_ERROR_T Type

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

### DBMS_CLOUD_OCI_APM_SYNTHETICS_GEO_SUMMARY_T Type

Geographic summary of a vantage point.

Syntax
```

```

Fields

Field Description

`admin_div_code`

(optional) The ISO 3166-2 code for this location's first-level administrative division, either a US state or Canadian province. Only included for locations in the US or Canada. For a list of codes, see Country Codes.

`city_name`

(optional) Common English-language name for the city.

`country_code`

(optional) The ISO 3166-1 alpha-2 country code. For a list of codes, see Country Codes.

`country_name`

(optional) The common English-language name for the country.

`latitude`

(optional) Degrees north of the equator.

`longitude`

(optional) Degrees east of the prime meridian.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_HEADER_T Type

Details of the header.

Syntax
```

```

Fields

Field Description

`header_name`

(required) Name of the header.

`header_value`

(optional) Value of the header.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_INFO_T Type

Details of the vantage point.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the vantage point.

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_INFO_T Type

Details of the script parameters in the monitor. isOverwritten specifies that the script parameters are overwritten in the monitor. If the user overwrites the parameter value in the monitor, then the overwritten values will be used to run the monitor.

Syntax
```

```

Fields

Field Description

`monitor_script_parameter`

(required)

`is_secret`

(required) Describes if the parameter value is secret and should be kept confidential. isSecret is specified in either CreateScript or UpdateScript API.

`is_overwritten`

(required) If parameter value is default or overwritten.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_INFO_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_vantage_point_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_INFO_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_monitor_script_parameter_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_T Type

The information about a monitor.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the monitor.

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`monitor_type`

(required) Type of monitor.

Allowed values are: 'SCRIPTED_BROWSER', 'BROWSER', 'SCRIPTED_REST', 'REST', 'NETWORK'

`vantage_points`

(required) List of public and dedicated vantage points where the monitor is running.

`vantage_point_count`

(required) Number of vantage points where monitor is running.

`script_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`script_name`

(required) Name of the script.

`status`

(required) Enables or disables the monitor.

Allowed values are: 'ENABLED', 'DISABLED', 'INVALID'

`repeat_interval_in_seconds`

(required) Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.

`is_run_once`

(required) If runOnce is enabled, then the monitor will run once.

`timeout_in_seconds`

(required) Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.

`target`

(optional) Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is. For NETWORK monitor with TCP protocol, a port needs to be provided along with target. Example: 192.168.0.1:80

`script_parameters`

(optional) List of script parameters. Example: `[{\"monitorScriptParameter\": {\"paramName\": \"userid\", \"paramValue\":\"testuser\"}, \"isSecret\": false, \"isOverwritten\": false}]`

`configuration`

(optional)

`availability_configuration`

(optional)

`maintenance_window_schedule`

(optional)

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_run_now`

(required) If isRunNow is enabled, then the monitor will run immediately.

`scheduling_policy`

(required) Scheduling policy to decide the distribution of monitor executions on vantage points.

Allowed values are: 'ALL', 'ROUND_ROBIN', 'BATCHED_ROUND_ROBIN'

`batch_interval_in_seconds`

(required) Time interval between two runs in round robin batch mode (SchedulingPolicy - BATCHED_ROUND_ROBIN).

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SUMMARY_T Type

Information about the monitor.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the monitor.

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`monitor_type`

(required) The type of monitor.

Allowed values are: 'SCRIPTED_BROWSER', 'BROWSER', 'SCRIPTED_REST', 'REST', 'NETWORK'

`vantage_points`

(required) List of public and dedicated vantage points where the monitor is running.

`vantage_point_count`

(required) Number of vantage points where monitor is running.

`script_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`script_name`

(required) Name of the script.

`status`

(required) Enables or disables the monitor.

Allowed values are: 'ENABLED', 'DISABLED', 'INVALID'

`repeat_interval_in_seconds`

(required) Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.

`is_run_once`

(required) If runOnce is enabled, then the monitor will run once.

`timeout_in_seconds`

(required) Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.

`target`

(optional) Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is. For NETWORK monitor with TCP protocol, a port needs to be provided along with target. Example: 192.168.0.1:80

`maintenance_window_schedule`

(optional)

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_run_now`

(required) If isRunNow is enabled, then the monitor will run immediately.

`scheduling_policy`

(required) Scheduling policy to decide the distribution of monitor executions on vantage points.

Allowed values are: 'ALL', 'ROUND_ROBIN', 'BATCHED_ROUND_ROBIN'

`batch_interval_in_seconds`

(required) Time interval between two runs in round robin batch mode (SchedulingPolicy - BATCHED_ROUND_ROBIN).

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_monitor_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_COLLECTION_T Type

The results of a monitor search, which contains both MonitorSummary items and other data in an APM domain.

Syntax
```

```

Fields

Field Description

`items`

(required) List of MonitorSummary items.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_DATA_T Type

Details of the monitor result data.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the data.

`byte_content`

(optional) Data content in byte format. Example: Zip or Screenshot.

`string_content`

(optional) Data content in string format. Example: HAR.

`l_timestamp`

(optional) The time when the data was generated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_DATA_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_monitor_result_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_T Type

The monitor result for a specific execution.

Syntax
```

```

Fields

Field Description

`result_type`

(optional) Type of result. Example: HAR, Screenshot, Log or Network.

`result_content_type`

(required) Type of result content. Example: Zip or Raw file.

`result_data_set`

(optional) Monitor result data set.

`monitor_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the monitor.

`vantage_point`

(optional) The name of the public or dedicated vantage point.

`execution_time`

(optional) The specific point of time when the result of an execution is collected.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_NETWORK_MONITOR_CONFIGURATION_T Type

Request configuration details for the NETWORK monitor type.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_network_monitor_configuration_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_monitor_configuration_t`type.

Fields

Field Description

`network_configuration`

(required)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_NODE_T Type

Details of the network node.

Syntax
```

```

Fields

Field Description

`id`

(required) ID of the network node.

`ip_address`

(optional) IP address of the network node.

`display_name`

(optional) Display name of the network node.

`geo_info`

(optional) Geographical information of the network node.

`outgoing_links`

(optional) Outgoing links from the network node.

`consecutive_anonymous_count`

(optional) Number of consecutive anonymous network nodes.

`l_level`

(optional) Level of the network node.

`avg_packet_response_time_in_ms`

(optional) Average packet response time in milliseconds.

`avg_packet_loss_percent`

(optional) Percentage of the average packet loss.

`l_type`

(optional) Type of network node.

Allowed values are: 'SOURCE', 'DESTINATION', 'ANONYMOUS', 'INTERNAL', 'DANGLING'

### DBMS_CLOUD_OCI_APM_SYNTHETICS_ORACLE_RM_STACK_T Type

Details of the Oracle Resource Manager stack, which is a subtype of the Dedicated Vantage Point stack.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_oracle_rm_stack_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_dvp_stack_details_t`type.

Fields

Field Description

`dvp_stack_id`

(required) Stack[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Resource Manager stack for dedicated vantage point.

`dvp_stream_id`

(required) Stream[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Resource Manager stack for dedicated vantage point.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_SUMMARY_T Type

Information about public vantage points.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`name`

(required) Unique permanent name of the vantage point.

`geo`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_public_vantage_point_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_COLLECTION_T Type

The results of a public vantage point search, which contains PublicVantagePointSummary items and other data in an APM domain.

Syntax
```

```

Fields

Field Description

`items`

(required) List of PublicVantagePointSummary items.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_HEADER_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_header_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_AUTHENTICATION_DETAILS_T Type

Details for request HTTP authentication.

Syntax
```

```

Fields

Field Description

`oauth_scheme`

(optional) Request HTTP OAuth scheme.

Allowed values are: 'NONE', 'BASIC'

`auth_user_name`

(optional) User name for authentication.

`auth_user_password`

(optional) User password for authentication.

`auth_token`

(optional) Authentication token.

`auth_url`

(optional) URL to get authentication token.

`auth_headers`

(optional) List of authentication headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`

`auth_request_method`

(optional) Request method.

Allowed values are: 'GET', 'POST'

`auth_request_post_body`

(optional) Request post body.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_QUERY_PARAM_T Type

Information about request query parameters.

Syntax
```

```

Fields

Field Description

`param_name`

(required) Name of request query parameter.

`param_value`

(optional) Value of request query parameter.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_QUERY_PARAM_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_request_query_param_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_REST_MONITOR_CONFIGURATION_T Type

Request configuration details for the REST monitor type.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_rest_monitor_configuration_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_monitor_configuration_t`type.

Fields

Field Description

`is_redirection_enabled`

(optional) If redirection is enabled, then redirects will be allowed while accessing target URL.

`is_certificate_validation_enabled`

(optional) If certificate validation is enabled, then call will fail for certificate errors.

`request_method`

(optional) Request HTTP method.

Allowed values are: 'GET', 'POST'

`req_authentication_scheme`

(optional) Request HTTP authentication scheme.

Allowed values are: 'OAUTH', 'NONE', 'BASIC', 'BEARER', 'RESOURCE_PRINCIPAL'

`req_authentication_details`

(optional)

`client_certificate_details`

(optional)

`request_headers`

(optional) List of request headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`

`request_query_params`

(optional) List of request query params. Example: `[{\"paramName\": \"sortOrder\", \"paramValue\": \"asc\"}]`

`request_post_body`

(optional) Request post body content.

`verify_response_content`

(optional) Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.

`verify_response_codes`

(optional) Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_INFO_T Type

Information about script parameters. isOverwritten specifies that the default parameter present in the script content is overwritten.

Syntax
```

```

Fields

Field Description

`script_parameter`

(required)

`is_overwritten`

(required) If parameter value is default or overwritten.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_INFO_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_script_parameter_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_T Type

The information about the script.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`content_type`

(required) Content type of the script.

Allowed values are: 'SIDE', 'JS'

`content`

(optional) The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters. The format to set dynamic parameters is: `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;OS&gt;isParamValueSecret(true/false)&lt;/OS&gt;&lt;/ORAP&gt;`. Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false. Examples: With mandatory param name : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;/ORAP&gt;` With parameter name and value : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;/ORAP&gt;` Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.

`time_uploaded`

(optional) The time the script was uploaded.

`content_size_in_bytes`

(optional) Size of the script content.

`content_file_name`

(optional) File name of the uploaded script content.

`parameters`

(optional) List of script parameters. Example: `[{\"scriptParameter\": {\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}, \"isOverwritten\": false}]`

`monitor_status_count_map`

(required)

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_SUMMARY_T Type

Information about the script.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`display_name`

(required) Unique name that can be edited. The name should not contain any confidential information.

`content_type`

(required) Content type of the script.

Allowed values are: 'SIDE', 'JS'

`monitor_status_count_map`

(required)

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_synthetics_script_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_COLLECTION_T Type

The results of a script search, which contains both ScriptSummary items and other data in an APM domain.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ScriptSummary items.

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPTED_BROWSER_MONITOR_CONFIGURATION_T Type

Configuration details for the SCRIPTED_BROWSER monitor type.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_scripted_browser_monitor_configuration_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_monitor_configuration_t`type.

Fields

Field Description

`is_certificate_validation_enabled`

(optional) If certificate validation is enabled, then the call will fail in case of certification errors.

`is_default_snapshot_enabled`

(optional) If disabled, auto snapshots are not collected.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPTED_REST_MONITOR_CONFIGURATION_T Type

Configuration details for the SCRIPTED_REST monitor type.

Syntax
```

```

`dbms_cloud_oci_apm_synthetics_scripted_rest_monitor_configuration_t`is a subtype of the`dbms_cloud_oci_apm_synthetics_monitor_configuration_t`type.

Fields

Field Description

`req_authentication_scheme`

(optional) Request HTTP authentication scheme.

Allowed values are: 'NONE', 'RESOURCE_PRINCIPAL'

`verify_response_codes`

(optional) Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_DEDICATED_VANTAGE_POINT_DETAILS_T Type

Details of the request body used to update a dedicated vantage point.

Syntax
```

```

Fields

Field Description

`status`

(optional) Status of the dedicated vantage point.

Allowed values are: 'ENABLED', 'DISABLED'

`dvp_stack_details`

(optional)

`l_region`

(optional) Name of the region.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_MONITOR_DETAILS_T Type

Details of the request body used to update a monitor.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Unique name that can be edited. The name should not contain any confidential information.

`vantage_points`

(optional) A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.

`script_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

`status`

(optional) Enables or disables the monitor.

Allowed values are: 'ENABLED', 'DISABLED', 'INVALID'

`repeat_interval_in_seconds`

(optional) Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.

`is_run_once`

(optional) If runOnce is enabled, then the monitor will run once.

`timeout_in_seconds`

(optional) Timeout in seconds. If isFailureRetried is true, then timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. If isFailureRetried is false, then timeout cannot be more than 50% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.

`target`

(optional) Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is. For NETWORK monitor with TCP protocol, a port needs to be provided along with target. Example: 192.168.0.1:80

`script_parameters`

(optional) List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

`configuration`

(optional)

`availability_configuration`

(optional)

`maintenance_window_schedule`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_run_now`

(optional) If isRunNow is enabled, then the monitor will run immediately.

`scheduling_policy`

(optional) Scheduling policy to decide the distribution of monitor executions on vantage points.

Allowed values are: 'ALL', 'ROUND_ROBIN', 'BATCHED_ROUND_ROBIN'

`batch_interval_in_seconds`

(optional) Time interval between two runs in round robin batch mode (SchedulingPolicy - BATCHED_ROUND_ROBIN).

### DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_SCRIPT_DETAILS_T Type

Details of the request body used to update a script. Only Side or JavaScript content types are supported and content should be in Side or JavaScript formats only.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Unique name that can be edited. The name should not contain any confidential information.

`content_type`

(optional) Content type of script.

Allowed values are: 'SIDE', 'JS'

`content`

(optional) The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters. The format to set dynamic parameters is: `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;OS&gt;isParamValueSecret(true/false)&lt;/OS&gt;&lt;/ORAP&gt;`. Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false. Examples: With mandatory param name : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;/ORAP&gt;` With parameter name and value : `&lt;ORAP&gt;&lt;ON&gt;param name&lt;/ON&gt;&lt;OV&gt;param value&lt;/OV&gt;&lt;/ORAP&gt;` Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.

`content_file_name`

(optional) File name of uploaded script content.

`parameters`

(optional) List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

- [Application Performance Monitoring Synthetics Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-30632B37-32FF-4B2D-B08C-4FA11B54CE7F)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-00860A83-4E52-4A42-9BB7-0BE15624EB1E)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-EA5FAAA4-95C6-46E3-800E-65454B808354)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6714F0A0-5BE3-4DF8-AF52-15A1F9299A1B)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_EXECUTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-F8DD1041-6F05-4162-9DE6-0FA64C87804B)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATE_NETWORK_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6A661FF1-D897-4753-915F-EF703863215A)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E95C69B3-0D81-435D-B6DD-0A2079039BF6)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-F6A6E181-B7C1-479D-816B-2D99707D18E5)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-AD5BE5B2-034E-4F87-8772-4A9F22BDC557)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATED_NETWORK_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-90D2FA0F-CCBD-4A55-80FD-DD10467EF19E)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_AGGREGATED_NETWORK_DATA_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-B8539AE9-24E1-4A28-B23F-2462030854C4)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_AVAILABILITY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-59EFA350-9708-40C3-91C2-D89F6D7DB869)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DNS_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-D6A3F1A3-6071-4616-BC0B-F4BB09312BD6)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VERIFY_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-1E3AFF41-E982-41E2-8E97-2F29FDA26758)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-F426B70A-3B34-4790-B235-7A51BC26DC80)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6D311871-566C-46ED-B390-DF619033B9CD)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VERIFY_TEXT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-72DF25E3-8F83-4E42-8A93-ADCAC604D88D)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_BROWSER_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-5DE1569A-C44F-4D2F-9C5D-9C82F96BAA35)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_CLIENT_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-CE057273-A0C1-4BF8-B0BC-2BA36406ABBB)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_PRIVATE_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-7DF01991-8FE8-4B65-AD40-8B52A0A34B86)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_CLIENT_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-ADB9584D-E27A-4635-81FA-8BC06BD73A83)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DVP_STACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-BC6E58EA-BD9F-4469-8DC1-059105A6CF79)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_DEDICATED_VANTAGE_POINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-A3F3AE08-B417-4EDC-BA38-DA9F61B48BC4)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-9DF985D5-1ACE-48F1-882B-EB31D3966C41)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MAINTENANCE_WINDOW_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-66631121-E779-4DFC-A98F-901071DD5D83)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-44D7DEED-C4DA-4337-A72B-88B4DC0ED70B)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-661CA774-371B-416B-9F8A-57994C15FA1E)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-44C0906D-AA34-486D-8BAE-214E6B698EA1)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-4DC2124F-FAD1-4E9D-8E36-34B15E868058)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_CREATE_SCRIPT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E7DE92FD-C467-4BEC-AC97-E07295B06B43)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_STATUS_COUNT_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-FEE38FEB-498F-41E6-83B9-C8D8AE12F0FD)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-03D89943-286F-4979-B805-B6591A1901E1)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-ED046444-B3CF-4B5F-969F-D30FA8A9AE58)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-1ABF5103-4B5E-4D37-99F7-FD1CBFA4B214)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_DEDICATED_VANTAGE_POINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-B0C37D4A-0389-4918-9244-426CA684F0CC)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-F7F44051-8A93-4D6C-BBA2-1429FFB90FF0)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_GEO_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-CD7A7CA2-7420-44BB-9A75-7A0ACAFB9761)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_HEADER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-2182A8DD-1541-4C16-B00A-3EDAED7C24AD)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E1141916-4768-4100-A0CF-F4016C7AAD41)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-C46919EF-5D31-48DD-993C-72B414832BC1)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_VANTAGE_POINT_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-4AF83B54-D730-404E-BC4D-423ACECFB2FF)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SCRIPT_PARAMETER_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-51A2DAF0-D680-4B7F-B46F-1FA0CBA99B4A)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E95A0F88-6137-4C02-93F1-043784130A7B)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-3B0745C2-2834-4A06-ADB3-C68CB922CF7C)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-337050F4-71E2-4EFA-9A67-FC1758023226)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-9F7951AF-115C-4B75-BD61-024C05D73780)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-927ED840-67C7-48A8-B3FD-004E6A075F97)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6D1C7D25-BDBA-4657-BBCD-2FF3887DFD37)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_MONITOR_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-99EBF2F6-C6C5-4BCA-8B76-57AA0E304052)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_NETWORK_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-0D7FE432-34CF-4C9F-8A7C-32B30C12B5BC)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-457FB5B0-ECE0-47D0-A3F2-EDDFD415E1AF)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_ORACLE_RM_STACK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-05418796-B645-49D2-9BB6-6B81B197E6F1)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E29B9486-3DFA-4812-9628-D5A345AD17B6)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-BF6E90D7-EAB4-45BD-8612-75D825DCB39D)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_PUBLIC_VANTAGE_POINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-154D3ED3-C6AA-4492-8261-41B3F482B0B9)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_HEADER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-BCF869EA-455D-484A-92C3-7EE06556A2DA)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_AUTHENTICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-43961020-D854-4094-AFFA-3B0AACC95804)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_QUERY_PARAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-9BDA28FD-ADE8-4289-AB28-07EAF8608294)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_REQUEST_QUERY_PARAM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-FCA79A3B-ED5C-414A-8F54-E1FFAB61FF6D)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_REST_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-727ED3DD-6933-48B9-A73E-FBF4EE6051A7)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-268AFD84-7032-432A-99C1-2BD4A1943F4E)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_PARAMETER_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-85031F20-A9F5-47E9-8BD3-9E996C2E7F33)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-7C765AD7-B574-4CAA-8F8D-AC568B3316DD)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-DDDFDF95-7A0A-4055-899E-0062270E3A07)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-7A9DC206-CAFA-474F-9EA9-011BC351D84D)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-02209103-FE53-4210-BDDA-0309FFC4D60A)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPTED_BROWSER_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-978AACEB-5980-429F-BF17-72B3189D7985)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_SCRIPTED_REST_MONITOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-D45AEE0A-BD56-4A09-8A5D-9C07A8657127)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_DEDICATED_VANTAGE_POINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6F065D98-2F38-4402-8CC4-1D0CBC86CD45)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_MONITOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-E4D146B5-1874-4CC7-99FE-F51F98FF6C60)
- [DBMS_CLOUD_OCI_APM_SYNTHETICS_UPDATE_SCRIPT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_synthetics_t.html#ADSDK-GUID-6CCCE3AD-7F6C-4632-AC8A-D9C1E95AA2C1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
