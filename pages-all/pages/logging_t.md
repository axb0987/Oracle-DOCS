# Logging Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#dcoc-content-body)

## Logging Common Types

### DBMS_CLOUD_OCI_LOGGING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_ARCHIVING_T Type

Log archiving configuration.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) True if archiving enabled. This field is now deprecated, you should use Service Connector Hub to enable archiving.

### DBMS_CLOUD_OCI_LOGGING_PARAMETER_T Type

Parameters that a resource category supports.

Syntax
```

```

Fields

Field Description

`name`

(required) Parameter name.

`l_type`

(required)

Allowed values are: 'integer', 'string', 'boolean'

`pattern`

(optional) Java regex pattern to validate a parameter value.

### DBMS_CLOUD_OCI_LOGGING_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_logging_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_CATEGORY_T Type

Categories for resources.

Syntax
```

```

Fields

Field Description

`name`

(optional) Category name.

`display_name`

(optional) Category display name. Avoid entering confidential information.

`parameters`

(optional) Parameters the category supports.

### DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_GROUP_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the resource should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_LOG_GROUP_DETAILS_T Type

Contains details indicating which log group the log should move to.

Syntax
```

```

Fields

Field Description

`target_log_group_id`

(optional) Log group OCID.

### DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_SAVED_SEARCH_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the resource should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_LOGGING_CHANGE_UNIFIED_AGENT_CONFIGURATION_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the resource should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_LOGGING_SOURCE_T Type

The source the log object comes from.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The log source. * **OCISERVICE:** Oracle Service.

Allowed values are: 'OCISERVICE'

### DBMS_CLOUD_OCI_LOGGING_CONFIGURATION_T Type

Log object configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment that the resource belongs to.

`source`

(required)

`archiving`

(optional)

### DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_DETAILS_T Type

The details to create a log object.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`log_type`

(required) The logType that the log object is for, whether custom or service.

Allowed values are: 'CUSTOM', 'SERVICE'

`is_enabled`

(optional) Whether or not this resource is currently enabled.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`configuration`

(optional)

`retention_duration`

(optional) Log retention duration in 30-day increments (30, 60, 90 and so on until 180).

### DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_GROUP_DETAILS_T Type

The details to create a log group.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_SAVED_SEARCH_DETAILS_T Type

A LogSavedSearch that can be used to save and share a given search result.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`query`

(required) The search query that is saved.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_SERVICE_CONFIGURATION_DETAILS_T Type

Top level Unified Agent service configuration object.

Syntax
```

```

Fields

Field Description

`configuration_type`

(required) Type of Unified Agent service configuration.

Allowed values are: 'LOGGING'

### DBMS_CLOUD_OCI_LOGGING_GROUP_ASSOCIATION_DETAILS_T Type

Groups using the configuration.

Syntax
```

```

Fields

Field Description

`group_list`

(optional) list of group/dynamic group ids associated with this configuration.

### DBMS_CLOUD_OCI_LOGGING_CREATE_UNIFIED_AGENT_CONFIGURATION_DETAILS_T Type

Unified Agent configuration creation object.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`is_enabled`

(required) Whether or not this resource is currently enabled.

`service_configuration`

(required)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`description`

(optional) Description for this resource.

`group_association`

(optional)

### DBMS_CLOUD_OCI_LOGGING_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOGGING_GROK_PATTERN_T Type

Grok pattern object.

Syntax
```

```

Fields

Field Description

`pattern`

(required) The Grok pattern.

`name`

(optional) The name key to tag this Grok pattern.

`field_time_key`

(optional) Specify the time field for the event time. If the event doesn't have this field, the current time is used.

`field_time_format`

(optional) Process value using the specified format. This is available only when time_type is a string.

`field_time_zone`

(optional) Use the specified time zone. The time value can be parsed or formatted in the specified time zone.

### DBMS_CLOUD_OCI_LOGGING_LOG_T Type

Represents a log object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`tenancy_id`

(optional) The OCID of the tenancy.

`log_group_id`

(required) Log group OCID.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`log_type`

(required) The logType that the log object is for, whether custom or service.

Allowed values are: 'CUSTOM', 'SERVICE'

`is_enabled`

(optional) Whether or not this resource is currently enabled.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`configuration`

(optional)

`lifecycle_state`

(required) The pipeline state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`retention_duration`

(optional) Log retention duration in 30-day increments (30, 60, 90 and so on until 180).

`compartment_id`

(optional) The OCID of the compartment that the resource belongs to.

### DBMS_CLOUD_OCI_LOGGING_LOG_GROUP_T Type

Represents a LogGroup object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`lifecycle_state`

(optional) The log group object state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

### DBMS_CLOUD_OCI_LOGGING_LOG_GROUP_SUMMARY_T Type

Log group configuration summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`lifecycle_state`

(optional) The log group object state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

### DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_T Type

A LogSavedSearch that can be used to save and share a given search result.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`description`

(optional) Description for this resource.

`query`

(required) The search query that is saved.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`lifecycle_state`

(optional) The state of the LogSavedSearch

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

### DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_T Type

A summary of a LogSavedSearch that can be used to save and share a given search result.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`description`

(optional) Description for this resource.

`query`

(optional) The search query that is saved.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`lifecycle_state`

(optional) The state of the LogSavedSearch

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

### DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_logging_log_saved_search_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_COLLECTION_T Type

A collection of LogSavedSearchSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) The Saved Seach Summaries

### DBMS_CLOUD_OCI_LOGGING_LOG_SUMMARY_T Type

Log object configuration summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`log_group_id`

(required) Log group OCID.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`is_enabled`

(optional) Whether or not this resource is currently enabled.

`lifecycle_state`

(required) The pipeline state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`log_type`

(required) The logType that the log object is for, whether custom or service.

Allowed values are: 'CUSTOM', 'SERVICE'

`configuration`

(optional)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`retention_duration`

(optional) Log retention duration in 30-day increments (30, 60, 90 and so on until 180).

`compartment_id`

(optional) The OCID of the compartment that the resource belongs to.

### DBMS_CLOUD_OCI_LOGGING_OCI_SERVICE_T Type

OCI service logging configuration.

Syntax
```

```

`dbms_cloud_oci_logging_oci_service_t`is a subtype of the`dbms_cloud_oci_logging_source_t`type.

Fields

Field Description

`service`

(required) Service generating log.

`l_resource`

(required) The unique identifier of the resource emitting the log.

`category`

(required) Log object category.

`parameters`

(optional) Log category parameters are stored here.

### DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_RECORD_INPUT_T Type

Record section of OperationalMetricsSource object.

Syntax
```

```

Fields

Field Description

`namespace`

(required) Namespace to emit the operational metrics.

`resource_group`

(optional) Resource group to emit the operational metrics.

### DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_SOURCE_T Type

Unified monitoring agent operational metrics source object.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the unified monitoring agent operational metrics source object.

Allowed values are: 'UMA_METRICS'

`metrics`

(optional) List of unified monitoring agent operational metrics.

`record_input`

(optional)

### DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_DESTINATION_T Type

Unified monitoring agent operational metrics destination object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

### DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_CONFIGURATION_T Type

Unified monitoring agent operational metrics configuration object.

Syntax
```

```

Fields

Field Description

`source`

(required)

`destination`

(required)

### DBMS_CLOUD_OCI_LOGGING_CATEGORY_TBL Type

Nested table type of dbms_cloud_oci_logging_category_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_RESOURCE_TYPE_T Type

Type of resource that a service provides.

Syntax
```

```

Fields

Field Description

`name`

(optional) Resource type name.

`categories`

(optional) Categories for resources.

### DBMS_CLOUD_OCI_LOGGING_RESOURCE_TYPE_TBL Type

Nested table type of dbms_cloud_oci_logging_resource_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_SERVICE_SUMMARY_T Type

Summary of services that are integrated with public logging.

Syntax
```

```

Fields

Field Description

`tenant_id`

(required) Tenant OCID.

`namespace`

(optional) Apollo project namespace, if any.

`service_principal_name`

(required) Service ID as set in Service Principal.

`endpoint`

(required) Service endpoint.

`name`

(required) User-friendly service name.

`id`

(optional) Service ID.

`resource_types`

(required) Type of resource that a service provides.

### DBMS_CLOUD_OCI_LOGGING_SOURCE_UPDATE_DETAILS_T Type

Source updated configuration.

Syntax
```

```

Fields

Field Description

`parameters`

(optional) Log category parameters are stored here.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_PARSER_T Type

Source parser object.

Syntax
```

```

Fields

Field Description

`parser_type`

(required) Type of fluent parser.

Allowed values are: 'AUDITD', 'CRI', 'JSON', 'TSV', 'CSV', 'NONE', 'SYSLOG', 'APACHE2', 'APACHE_ERROR', 'MSGPACK', 'REGEXP', 'MULTILINE', 'GROK', 'MULTILINE_GROK'

`field_time_key`

(optional) Specifies the time field for the event time. If the event doesn't have this field, the current time is used.

`types`

(optional) Specify types for converting a field into another type. For example, With this configuration: &lt;parse&gt; @type csv keys time,host,req_id,user time_key time &lt;/parse&gt; This incoming event: \"2013/02/28 12:00:00,192.168.0.1,111,-\" is parsed as: 1362020400 (2013/02/28/ 12:00:00) record: { \"host\" : \"192.168.0.1\", \"req_id\" : \"111\", \"user\" : \"-\" }

`null_value_pattern`

(optional) Specify the null value pattern.

`is_null_empty_string`

(optional) If true, an empty string field is replaced with a null value.

`is_estimate_current_event`

(optional) If true, use Fluent::EventTime.now(current time) as a timestamp when the time_key is specified.

`is_keep_time_key`

(optional) If true, keep the time field in the record.

`timeout_in_milliseconds`

(optional) Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_APACHE2_PARSER_T Type

Apache 2 log parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_apache2_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_APACHE_ERROR_PARSER_T Type

Apache error log parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_apache_error_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_AUDITD_PARSER_T Type

auditd parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_auditd_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_T Type

Top Unified Agent configuration object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`lifecycle_state`

(required) The pipeline state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`is_enabled`

(required) Whether or not this resource is currently enabled.

`configuration_state`

(required) State of unified agent service configuration.

Allowed values are: 'VALID', 'INVALID'

`service_configuration`

(required)

`group_association`

(required)

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_SUMMARY_T Type

Unified Agent configuration summary object returned by the list API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource.

`compartment_id`

(required) The OCID of the compartment that the resource belongs to.

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(optional) Time the resource was created.

`time_last_modified`

(optional) Time the resource was last modified.

`lifecycle_state`

(required) The pipeline state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'DELETING', 'FAILED'

`is_enabled`

(required) Whether or not this resource is currently enabled.

`configuration_type`

(required) Type of Unified Agent service configuration.

Allowed values are: 'LOGGING'

`configuration_state`

(required) State of unified agent service configuration.

Allowed values are: 'VALID', 'INVALID'

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_logging_unified_agent_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_COLLECTION_T Type

Results of a UnifiedAgentConfiguration search. Contains UnifiedAgentConfigurationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of UnifiedAgentConfigurationSummary.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_JSON_PARSER_T Type

JSON parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_json_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`time_type`

(optional) JSON parser time type.

Allowed values are: 'FLOAT', 'UNIXTIME', 'STRING'

`time_format`

(optional) Process time value using the specified format.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CRI_PARSER_T Type

CRI parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_cri_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`is_merge_cri_fields`

(optional) If you don't need stream or logtag fields, set this to false.

`nested_parser`

(optional) Optional nested JSON Parser for CRI. Supported fields are fieldTimeKey, timeFormat, and isKeepTimeKey.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CSV_PARSER_T Type

CSV Parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_csv_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`delimiter`

(optional) CSV delimiter.

`keys`

(required) CSV keys.

### DBMS_CLOUD_OCI_LOGGING_GROK_PATTERN_TBL Type

Nested table type of dbms_cloud_oci_logging_grok_pattern_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_GROK_PARSER_T Type

Grok parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_grok_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`grok_name_key`

(optional) Grok name key.

`grok_failure_key`

(optional) Grok failure key.

`patterns`

(required) Grok pattern object.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_SOURCE_T Type

Logging source object.

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name for the source.

`source_type`

(required) Unified schema logging source type.

Allowed values are: 'LOG_TAIL', 'WINDOWS_EVENT_LOG'

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_DESTINATION_T Type

Logging destination object.

Syntax
```

```

Fields

Field Description

`log_object_id`

(required) The OCID of the resource.

`operational_metrics_configuration`

(optional)

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_SOURCE_TBL Type

Nested table type of dbms_cloud_oci_logging_unified_agent_logging_source_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_CONFIGURATION_T Type

Unified Agent logging service configuration object.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_logging_configuration_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_service_configuration_details_t`type.

Fields

Field Description

`sources`

(required) Logging source object.

`destination`

(required)

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MSGPACK_PARSER_T Type

Msgpack parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_msgpack_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MULTILINE_GROK_PARSER_T Type

Multiline grok parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_multiline_grok_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`grok_name_key`

(optional) Grok name key.

`grok_failure_key`

(optional) Grok failure key.

`multi_line_start_regexp`

(optional) Multiline start regexp pattern.

`patterns`

(required) Grok pattern object.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MULTILINE_PARSER_T Type

Multiline parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_multiline_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`format_firstline`

(optional) First line pattern format.

`format`

(required) Mutiline pattern format.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_NONE_PARSER_T Type

This parser signifies a non-parser, and puts the entire log line in a message_key.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_none_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`message_key`

(optional) Specifies the field name to contain logs.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_REGEX_PARSER_T Type

Regexp parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_regex_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`expression`

(required) Regex pattern.

`time_format`

(optional) Time format.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_SYSLOG_PARSER_T Type

Syslog Parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_syslog_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`time_format`

(optional) Time format.

`rfc5424_time_format`

(optional) RFC 5424 time format.

`message_format`

(optional) Syslog message format.

Allowed values are: 'RFC3164', 'RFC5424', 'AUTO'

`is_with_priority`

(optional) Specifies with priority or not. Corresponds to the Fluentd with_priority parameter.

`is_support_colonless_ident`

(optional) Specifies whether or not to support colonless ident. Corresponds to the Fluentd support_colonless_ident parameter.

`syslog_parser_type`

(optional) Syslog parser type.

Allowed values are: 'STRING', 'REGEXP'

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_TAIL_LOG_SOURCE_T Type

Tail log source object.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_tail_log_source_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_logging_source_t`type.

Fields

Field Description

`paths`

(required) Absolute paths for log source files. Wildcards can be used.

`parser`

(optional)

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_TSV_PARSER_T Type

TSV Parser.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_tsv_parser_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_parser_t`type.

Fields

Field Description

`delimiter`

(optional) TSV delimiter.

`keys`

(required) TSV keys.

### DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_WINDOWS_EVENT_SOURCE_T Type

Windows events log source object.

Syntax
```

```

`dbms_cloud_oci_logging_unified_agent_windows_event_source_t`is a subtype of the`dbms_cloud_oci_logging_unified_agent_logging_source_t`type.

Fields

Field Description

`channels`

(required) Windows event log channels.

### DBMS_CLOUD_OCI_LOGGING_UPDATE_CONFIGURATION_DETAILS_T Type

The updatable configuration properties.

Syntax
```

```

Fields

Field Description

`source`

(required)

`archiving`

(optional)

### DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_DETAILS_T Type

Update log object properties.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`is_enabled`

(optional) Whether or not this resource is currently enabled.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`retention_duration`

(optional) Log retention duration in 30-day increments (30, 60, 90 and so on until 180).

`configuration`

(optional)

### DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_GROUP_DETAILS_T Type

The details to update a log group.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_SAVED_SEARCH_DETAILS_T Type

The update details to update a LogSavedSearch.

Syntax
```

```

Fields

Field Description

`name`

(optional) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description for this resource.

`query`

(optional) The search query that is saved.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_LOGGING_UPDATE_UNIFIED_AGENT_CONFIGURATION_DETAILS_T Type

Update Object for the Unified Agent configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.

`is_enabled`

(required) Whether or not this resource is currently enabled.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`description`

(optional) Description for this resource.

`service_configuration`

(required)

`group_association`

(optional)

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource, at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The resource identifier the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_logging_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_T Type

A work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The work request OCID.

`operation_type`

(required) The type of work the work request is doing.

Allowed values are: 'CREATE_LOG', 'UPDATE_LOG', 'DELETE_LOG', 'MOVE_LOG', 'CREATE_LOG_GROUP', 'UPDATE_LOG_GROUP', 'DELETE_LOG_GROUP', 'MOVE_LOG_GROUP', 'CREATE_CONFIGURATION', 'UPDATE_CONFIGURATION', 'DELETE_CONFIGURATION', 'MOVE_CONFIGURATION'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELLING', 'CANCELED'

`compartment_id`

(required) The work request's compartment OCID.

`resources`

(required) The resources this work request affects.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The time the work request was accepted.

`time_started`

(optional) The time the work request was started.

`time_finished`

(optional) The time the work request was finished.

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed at https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339-formatted date and time string.

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_LOG_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339-formatted date and time string.

### DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_SUMMARY_T Type

A summary of a work request.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the work request.

`operation_type`

(optional) The type of work the work request is doing.

Allowed values are: 'CREATE_LOG', 'UPDATE_LOG', 'DELETE_LOG', 'MOVE_LOG', 'CREATE_LOG_GROUP', 'UPDATE_LOG_GROUP', 'DELETE_LOG_GROUP', 'MOVE_LOG_GROUP', 'CREATE_CONFIGURATION', 'UPDATE_CONFIGURATION', 'DELETE_CONFIGURATION', 'MOVE_CONFIGURATION'

`status`

(optional) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELLING', 'CANCELED'

`compartment_id`

(optional) The OCID of the work request's compartment.

`resources`

(optional) The resources this work request affects.

`percent_complete`

(optional) Percentage of the request completed.

`time_accepted`

(optional) The time the work request was accepted.

`time_started`

(optional) The time the work request was started.

`time_finished`

(optional) The time the work request was finished.

- [Logging Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A45FDD91-342E-4ACE-BA1E-71607D021022)
- [DBMS_CLOUD_OCI_LOGGING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-7D5D1774-CF1F-458A-B157-4F095D06EE14)
- [DBMS_CLOUD_OCI_LOGGING_ARCHIVING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-8987005C-AA93-4E15-AE22-E047D2F63114)
- [DBMS_CLOUD_OCI_LOGGING_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-8FFBDAFB-0416-47FC-A8EA-00B31CC24EBB)
- [DBMS_CLOUD_OCI_LOGGING_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-B1BE9054-A02A-4B57-BCCC-61727E74E461)
- [DBMS_CLOUD_OCI_LOGGING_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-FA7F13C4-3ABD-4588-B977-9476E5506E0C)
- [DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-122F1E83-0ED3-44DE-B4DA-9EBB1488B78B)
- [DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_LOG_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-EEFF2F0C-F3E8-4314-8CFE-F56A76B4831A)
- [DBMS_CLOUD_OCI_LOGGING_CHANGE_LOG_SAVED_SEARCH_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-222E6407-5BFE-4FA6-AFC9-461738E89018)
- [DBMS_CLOUD_OCI_LOGGING_CHANGE_UNIFIED_AGENT_CONFIGURATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-ACD47799-C7B8-4922-AA78-1CED3B743C1E)
- [DBMS_CLOUD_OCI_LOGGING_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-3AB1ACC0-D4E9-48FB-87A0-4DA6EF19E3A9)
- [DBMS_CLOUD_OCI_LOGGING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-B561074A-34BC-49D9-B75A-E3FD354297B2)
- [DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-F6E598F9-7A09-4E36-9B20-BA155D0EF7AC)
- [DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A71B13E4-7CD8-444C-8547-C904035898D9)
- [DBMS_CLOUD_OCI_LOGGING_CREATE_LOG_SAVED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-3B1C795A-607F-4DAE-86BD-CCC3E78F1906)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_SERVICE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-BF87C4BA-CA98-4D9A-9D92-7F810D9CC1E5)
- [DBMS_CLOUD_OCI_LOGGING_GROUP_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-EFA93490-74A0-4832-8348-F1C3A223476F)
- [DBMS_CLOUD_OCI_LOGGING_CREATE_UNIFIED_AGENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A7BA4D5F-9488-467B-8682-0867225865CA)
- [DBMS_CLOUD_OCI_LOGGING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-039B1DDA-168B-4B66-92BA-5E750A4EE4DF)
- [DBMS_CLOUD_OCI_LOGGING_GROK_PATTERN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-4878C9C9-EB27-4946-ADDE-303F3942FF35)
- [DBMS_CLOUD_OCI_LOGGING_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-0BEF75D2-A37A-4C47-B1F6-688CCDFFDF13)
- [DBMS_CLOUD_OCI_LOGGING_LOG_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-EBF27130-3291-4971-85C5-4D21825D18A9)
- [DBMS_CLOUD_OCI_LOGGING_LOG_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-934FEAFA-AF1A-497D-88B9-528598C0151B)
- [DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-4C104A40-6617-45D6-81EF-FB06B0CBD009)
- [DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-0B54F262-EB18-4C45-AA40-0667DBD416B2)
- [DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-75A324AD-2F07-41D8-AA29-5C2138AC9015)
- [DBMS_CLOUD_OCI_LOGGING_LOG_SAVED_SEARCH_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-4B253FEA-56A7-4C7C-B501-E1706F99B620)
- [DBMS_CLOUD_OCI_LOGGING_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-63A5B82E-6831-4AF7-84C7-E44709509B66)
- [DBMS_CLOUD_OCI_LOGGING_OCI_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-86230555-C0BA-42FE-B633-A38A4072B940)
- [DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_RECORD_INPUT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-0D669150-3938-444E-A66A-24A8DB7B78F9)
- [DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-5A5C92EA-37EA-4BD7-947F-FFE66CE4AB97)
- [DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_DESTINATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-1CA64BF8-CA76-4F3E-AFA5-503A6EB95863)
- [DBMS_CLOUD_OCI_LOGGING_OPERATIONAL_METRICS_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-5078AD36-9BFE-48B6-92EB-5B13AD21E505)
- [DBMS_CLOUD_OCI_LOGGING_CATEGORY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A3381B2A-4BB9-4253-A865-0229737574DD)
- [DBMS_CLOUD_OCI_LOGGING_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-F7DF5125-62A0-44F3-9A0D-4EE2AD05F844)
- [DBMS_CLOUD_OCI_LOGGING_RESOURCE_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-8C303ABA-E0C4-408D-AB97-C59B4A535D08)
- [DBMS_CLOUD_OCI_LOGGING_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-CEF08837-6A2F-44C2-93D7-18B18895CB6D)
- [DBMS_CLOUD_OCI_LOGGING_SOURCE_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-6622F05D-D07D-4B6E-B1EE-016B0C3A0AA8)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-7D344836-CFDB-4B10-9A90-143455E94FC6)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_APACHE2_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A6F52ED2-CC61-44AC-8A31-3F41E048749D)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_APACHE_ERROR_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-5B0DB30C-4E4F-4300-8A76-1A076D86F47B)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_AUDITD_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-96C90666-8FF5-4EE6-8F5C-9669943E9445)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A9E8EB64-2E60-417E-92EB-4835FC110E13)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-713BBBDD-7C99-4E59-9D2F-E95FEEAD495A)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-C637CE16-F2F5-4559-A42D-2A238EBBAB2E)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-57A81D82-FEA3-4887-8EB8-BD1035E948A1)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_JSON_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-19720C41-BEDC-4694-A0F3-876F003E3CF6)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CRI_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-A25FF4E7-2009-4C1F-998F-FA2673FD2E0D)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_CSV_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-3F590DB6-BEDF-4CC4-A2C1-5854AD2E834E)
- [DBMS_CLOUD_OCI_LOGGING_GROK_PATTERN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-9908C498-2939-4469-8F01-3F11DFACF01B)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_GROK_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-8C4AF6E1-442F-45C5-8518-51143A52C230)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-DC5504C0-D17D-485C-B5DA-CE4F46DD631D)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_DESTINATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-74B03128-0E52-4050-A976-B9213186609C)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_SOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-FC7E32B3-079D-41BA-A060-9BE6AD0DFFA8)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_LOGGING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-292646AB-3C62-4A18-A007-5593B3AFC74A)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MSGPACK_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-9049AD49-6519-4E77-A87E-DE7B3FCAAEF4)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MULTILINE_GROK_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-00C7A65F-6FAC-49FC-8F65-4D0576773FE6)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_MULTILINE_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-800C17CF-3526-4333-8DF7-F37B5E9049D0)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_NONE_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-675768B0-DED2-4A3F-BF3C-8DD59CA45C8D)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_REGEX_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-B747E0B6-F4B7-4220-8A57-8F7B7C1372D6)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_SYSLOG_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-B2377D85-60D7-4677-A590-1C3995CE4DE8)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_TAIL_LOG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-E4AA84C8-B262-4236-B392-D0E0E8CDEB63)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_TSV_PARSER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-71DAFD3D-50BE-4A0D-AAD9-99D7B7ADE20C)
- [DBMS_CLOUD_OCI_LOGGING_UNIFIED_AGENT_WINDOWS_EVENT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-290562FC-E10C-4FC4-B1E1-BCE64579D633)
- [DBMS_CLOUD_OCI_LOGGING_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-C8716557-1E32-4CAB-92EC-26C8312AB5F7)
- [DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-710411B6-FD95-4CC0-9DAE-360E1AC2AEC7)
- [DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-35124AA5-3853-4DF2-B307-CAE70CF969B5)
- [DBMS_CLOUD_OCI_LOGGING_UPDATE_LOG_SAVED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-D89658E6-3626-4777-B2CC-0FDBE916C5E3)
- [DBMS_CLOUD_OCI_LOGGING_UPDATE_UNIFIED_AGENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-784CF888-DC23-4B99-BC62-E7D4B131E728)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-CD619574-5141-4C42-8611-67B51281627A)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-2F99426E-44D5-4222-B46B-75230E6ADFF6)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-31627157-1AA7-4B6B-8F65-EDC9358CCB8D)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-D5BEF897-46BB-4F50-9BDF-E0B7F8EC345A)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-ED028235-225B-407F-A441-728EEFD25B9F)
- [DBMS_CLOUD_OCI_LOGGING_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_t.html#ADSDK-GUID-7769EB06-9DA2-4264-929B-600E7CF4E60E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
