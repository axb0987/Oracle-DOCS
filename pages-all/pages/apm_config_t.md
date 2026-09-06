# Application Performance Monitoring Config Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#dcoc-content-body)

## Application Performance Monitoring Config Common Types

### DBMS_CLOUD_OCI_APM_CONFIG_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_APDEX_T Type

An Apdex configuration rule. The Apdex score is computed based on how the response time of a span compares to two predefined threshold values. The first threshold defines the maximum response time that is considered satisfactory for the end user. The second one defines the maximum response time that is considered tolerable. All times larger than that will be considered frustrating for the end user. An Apdex configuration rule works by selecting a subset of spans based on a filter expression and applying the two threshold comparisons to compute a score for each of the selected spans. The rule has an \"isApplyToErrorSpans\" property that controls whether or not to compute the Apdex for spans that have been marked as errors. If this property is set to \"true\", then the Apdex score for error spans is computed in the same way as for non-error ones. If set to \"false\", then computation for error spans is skipped, and the score is set to \"frustrating\" regardless of the configured thresholds. The default is \"false\". The \"isEnabled\" property controls whether or not an Apdex score is computed and can be used to disable Apdex score for certain spans. The default is \"true\". The \"priority\" property specifies the importance of the rule within a rule set. Lower values indicate a higher priority. Rules with higher priorities are evaluated first in the rule set. The priority of the rules must be unique within a rule set.

Syntax
```

```

Fields

Field Description

`filter_text`

(required) The string that defines the Span Filter expression.

`priority`

(required) The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are ignored. Rules within the same rule set cannot have the same priority.

`is_enabled`

(optional) Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable Apdex score for spans that do not need or require it. The default is \"true\".

`satisfied_response_time`

(optional) The maximum response time in milliseconds that is considered \"satisfactory\" for the end user.

`tolerating_response_time`

(optional) The maximum response time in milliseconds that is considered \"tolerable\" for the end user. A response time beyond this threshold is considered \"frustrating\". This value cannot be lower than \"satisfiedResponseTime\".

`is_apply_to_error_spans`

(optional) Specifies whether an Apdex score should be computed for error spans. Setting it to \"true\" means that the Apdex score is computed in the usual way. Setting it to \"false\" skips the Apdex computation and sets the Apdex score to \"frustrating\" regardless of the configured thresholds. The default is \"false\".

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

### DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_T Type

A configuration item, which has a number of mutually exclusive properties that can be used to set specific portions of the configuration.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item. An OCID is generated when the item is created.

`config_type`

(required) The type of configuration item.

Allowed values are: 'SPAN_FILTER', 'METRIC_GROUP', 'APDEX', 'OPTIONS'

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`created_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a user.

`updated_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a user.

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONFIG_APDEX_TBL Type

Nested table type of dbms_cloud_oci_apm_config_apdex_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_APDEX_RULES_T Type

The set of Apdex rules to be used in Apdex computation. In the current version, only one rule set can exist in the configuration.

Syntax
```

```

`dbms_cloud_oci_apm_config_apdex_rules_t`is a subtype of the`dbms_cloud_oci_apm_config_config_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`rules`

(optional)

### DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_SUMMARY_T Type

A description of a configuration item. It specifies all the properties that define the configuration item.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item. An OCID is generated when the item is created.

`config_type`

(required) The type of configuration item.

Allowed values are: 'SPAN_FILTER', 'METRIC_GROUP', 'APDEX', 'OPTIONS'

`time_created`

(optional) The time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-12T22:47:12.613Z`

`time_updated`

(optional) The time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2020-02-13T22:47:12.613Z`

`created_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a user.

`updated_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a user.

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONFIG_APDEX_RULES_SUMMARY_T Type

The set of Apdex rules used in Apdex computation.

Syntax
```

```

`dbms_cloud_oci_apm_config_apdex_rules_summary_t`is a subtype of the`dbms_cloud_oci_apm_config_config_summary_t`type.

Fields

Field Description

`rules`

(optional)

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

### DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_apm_config_config_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_COLLECTION_T Type

A collection of configuration items.

Syntax
```

```

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_APM_CONFIG_CREATE_CONFIG_DETAILS_T Type

The request body used to create new configuration items. It must specify the configuration type of the item, as well as the actual data to populate the item with.

Syntax
```

```

Fields

Field Description

`config_type`

(required) The type of configuration item.

Allowed values are: 'SPAN_FILTER', 'METRIC_GROUP', 'APDEX', 'OPTIONS'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONFIG_CREATE_APDEX_RULES_DETAILS_T Type

The set of Apdex rules to be used in Apdex computation. In the current version, only one rule set may exist per configuration, and attempting to create a rule set if it already exists results in an error.

Syntax
```

```

`dbms_cloud_oci_apm_config_create_apdex_rules_details_t`is a subtype of the`dbms_cloud_oci_apm_config_create_config_details_t`type.

Fields

Field Description

`rules`

(required)

`display_name`

(required) The name by which a configuration entity is displayed to the end user.

### DBMS_CLOUD_OCI_APM_CONFIG_DIMENSION_T Type

A dimension is a label that is used to describe or group metrics.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the dimension.

`value_source`

(optional) The source to populate the dimension. This must not be specified.

### DBMS_CLOUD_OCI_APM_CONFIG_METRIC_T Type

A metric is a quantitative measurement of an entity.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the metric. This must be a known metric name.

`value_source`

(optional) This must not be set.

`unit`

(optional) The unit of the metric.

`description`

(optional) A description of the metric.

### DBMS_CLOUD_OCI_APM_CONFIG_DIMENSION_TBL Type

Nested table type of dbms_cloud_oci_apm_config_dimension_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_METRIC_TBL Type

Nested table type of dbms_cloud_oci_apm_config_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_CREATE_METRIC_GROUP_DETAILS_T Type

A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to process. The set is then published to a namespace, which is a product level subdivision of metrics.

Syntax
```

```

`dbms_cloud_oci_apm_config_create_metric_group_details_t`is a subtype of the`dbms_cloud_oci_apm_config_create_config_details_t`type.

Fields

Field Description

`display_name`

(required) The name by which a configuration entity is displayed to the end user.

`filter_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.

`namespace`

(optional) The namespace to which the metrics are published. It must be one of several predefined namespaces.

`dimensions`

(optional) A list of dimensions for the metric. This variable should not be used.

`metrics`

(required) The list of metrics in this group.

### DBMS_CLOUD_OCI_APM_CONFIG_CREATE_OPTIONS_DETAILS_T Type

An Options object represents configuration options.

Syntax
```

```

`dbms_cloud_oci_apm_config_create_options_details_t`is a subtype of the`dbms_cloud_oci_apm_config_create_config_details_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`options`

(optional) The options are stored here as JSON.

`l_group`

(optional) A string that specifies the group that an OPTIONS item belongs to.

`description`

(optional) An optional string that describes what the options are intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_CREATE_SPAN_FILTER_DETAILS_T Type

A named setting that specifies the filter criteria to match a subset of the spans.

Syntax
```

```

`dbms_cloud_oci_apm_config_create_span_filter_details_t`is a subtype of the`dbms_cloud_oci_apm_config_create_config_details_t`type.

Fields

Field Description

`display_name`

(required) The name by which a configuration entity is displayed to the end user.

`filter_text`

(required) The string that defines the Span Filter expression.

`description`

(optional) An optional string that describes what the filter is intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_ERROR_T Type

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

### DBMS_CLOUD_OCI_APM_CONFIG_METRIC_GROUP_T Type

A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to process. The set is then published to a namespace, which is a product level subdivision of metrics.

Syntax
```

```

`dbms_cloud_oci_apm_config_metric_group_t`is a subtype of the`dbms_cloud_oci_apm_config_config_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.

`namespace`

(optional) The namespace to which the metrics are published. It must be one of several predefined namespaces.

`dimensions`

(optional) A list of dimensions for the metric. This variable should not be used.

`metrics`

(optional) The list of metrics in this group.

### DBMS_CLOUD_OCI_APM_CONFIG_METRIC_GROUP_SUMMARY_T Type

A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to process. The set is then published to a namespace, which is a product level subdivision of metrics.

Syntax
```

```

`dbms_cloud_oci_apm_config_metric_group_summary_t`is a subtype of the`dbms_cloud_oci_apm_config_config_summary_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.

`namespace`

(optional) The namespace to which the metrics are published. It must be one of several predefined namespaces.

`dimensions`

(optional) A list of dimensions for the metric. This variable should not be used.

`metrics`

(optional) The list of metrics in this group.

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_T Type

Namespaces represent a product level subdivision by name.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the namespace.

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_TBL Type

Nested table type of dbms_cloud_oci_apm_config_namespace_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_COLLECTION_T Type

Collection of available namespaces.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of available namespaces.

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_T Type

Metric associated with a namespace.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the metric.

`l_type`

(required) Type of metric.

Allowed values are: 'COUNTER', 'GAUGE'

`unit`

(optional) Unit of the metric.

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_TBL Type

Nested table type of dbms_cloud_oci_apm_config_namespace_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_COLLECTION_T Type

Collection of available namespace metrics.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of available namespace metrics.

### DBMS_CLOUD_OCI_APM_CONFIG_OPTIONS_T Type

An object that represents configuration options.

Syntax
```

```

`dbms_cloud_oci_apm_config_options_t`is a subtype of the`dbms_cloud_oci_apm_config_config_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`options`

(optional) The options are stored here as JSON.

`l_group`

(optional) A string that specifies the group that an OPTIONS item belongs to.

`description`

(optional) An optional string that describes what the options are intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_OPTIONS_SUMMARY_T Type

An Options object represents configuration options.

Syntax
```

```

`dbms_cloud_oci_apm_config_options_summary_t`is a subtype of the`dbms_cloud_oci_apm_config_config_summary_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`options`

(optional) The options are stored here as JSON.

`l_group`

(optional) A string that specifies the group that an OPTIONS item belongs to.

`description`

(optional) An optional string that describes what the options are intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_RETRIEVE_NAMESPACE_METRICS_DETAILS_T Type

The request body used to retrieve metrics for the specified namespace.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the namespace.

### DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_REFERENCE_T Type

Describes an item that references the span filter.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item. An OCID is generated when the item is created.

`config_type`

(optional) The type of configuration item.

Allowed values are: 'SPAN_FILTER', 'METRIC_GROUP', 'APDEX', 'OPTIONS'

`options_group`

(optional) A string that specifies the group that an OPTIONS item belongs to.

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

### DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_REFERENCE_TBL Type

Nested table type of dbms_cloud_oci_apm_config_span_filter_reference_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_T Type

A named setting that specifies the filter criteria to match a subset of the spans.

Syntax
```

```

`dbms_cloud_oci_apm_config_span_filter_t`is a subtype of the`dbms_cloud_oci_apm_config_config_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_text`

(optional) The string that defines the Span Filter expression.

`in_use_by`

(optional) The list of configuration items that reference the span filter.

`description`

(optional) An optional string that describes what the span filter is intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_SUMMARY_T Type

A named setting that specifies the span filter criteria to match a subset of the spans.

Syntax
```

```

`dbms_cloud_oci_apm_config_span_filter_summary_t`is a subtype of the`dbms_cloud_oci_apm_config_config_summary_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_text`

(optional) The string that defines the Span Filter expression.

`in_use_by`

(optional) The list of configuration items that reference the span filter.

`description`

(optional) An optional string that describes what the filter is intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_CONFIG_DETAILS_T Type

The request body used to update the configuration item. It must specify the data to update the item with.

Syntax
```

```

Fields

Field Description

`config_type`

(required) The type of configuration item.

Allowed values are: 'SPAN_FILTER', 'METRIC_GROUP', 'APDEX', 'OPTIONS'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_APDEX_RULES_DETAILS_T Type

The set of Apdex rules to be used in Apdex computation.

Syntax
```

```

`dbms_cloud_oci_apm_config_update_apdex_rules_details_t`is a subtype of the`dbms_cloud_oci_apm_config_update_config_details_t`type.

Fields

Field Description

`rules`

(required)

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

### DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_METRIC_GROUP_DETAILS_T Type

A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to process. The set is then published to a namespace, which is a product level subdivision of metrics.

Syntax
```

```

`dbms_cloud_oci_apm_config_update_metric_group_details_t`is a subtype of the`dbms_cloud_oci_apm_config_update_config_details_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.

`namespace`

(optional) The namespace to which the metrics are published. It must be one of several predefined namespaces.

`dimensions`

(optional) A list of dimensions for the metric. This variable should not be used.

`metrics`

(optional) The list of metrics in this group.

### DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_OPTIONS_DETAILS_T Type

An Options object represents configuration options.

Syntax
```

```

`dbms_cloud_oci_apm_config_update_options_details_t`is a subtype of the`dbms_cloud_oci_apm_config_update_config_details_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`options`

(optional) The options are stored here as JSON.

`l_group`

(optional) A string that specifies the group that an OPTIONS item belongs to.

`description`

(optional) An optional string that describes what the options are intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_SPAN_FILTER_DETAILS_T Type

A named setting that specifies the filter criteria to match a subset of the spans.

Syntax
```

```

`dbms_cloud_oci_apm_config_update_span_filter_details_t`is a subtype of the`dbms_cloud_oci_apm_config_update_config_details_t`type.

Fields

Field Description

`display_name`

(optional) The name by which a configuration entity is displayed to the end user.

`filter_text`

(optional) The string that defines the Span Filter expression.

`description`

(optional) An optional string that describes what the filter is intended or used for.

### DBMS_CLOUD_OCI_APM_CONFIG_VALIDATE_SPAN_FILTER_PATTERN_DETAILS_T Type

The request body used to validate a Span Filter pattern.

Syntax
```

```

Fields

Field Description

`filter_text`

(required) The string that defines the Span Filter expression.

- [Application Performance Monitoring Config Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-A841D9CE-C8D4-4E40-B1CF-677324328B1B)
- [DBMS_CLOUD_OCI_APM_CONFIG_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-117424BF-AE6D-4B3F-A5C7-21864318BC44)
- [DBMS_CLOUD_OCI_APM_CONFIG_APDEX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-A7354BD1-DCE3-4A91-8235-9CAC26F603ED)
- [DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-5C5B2B68-E957-491E-90A2-570C12602151)
- [DBMS_CLOUD_OCI_APM_CONFIG_APDEX_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-DADE6D20-A5C5-4913-A856-F65995A1361E)
- [DBMS_CLOUD_OCI_APM_CONFIG_APDEX_RULES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-C620BCC3-7977-4087-A412-C5D45E9B3E90)
- [DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-6241C41A-99F4-4925-B18F-F9BCF146D3D3)
- [DBMS_CLOUD_OCI_APM_CONFIG_APDEX_RULES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-1C9DE2EE-64B8-4CEE-B2E1-B6D50E12DC27)
- [DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-6825E67A-64EA-4649-B4C1-C525BCED4E1D)
- [DBMS_CLOUD_OCI_APM_CONFIG_CONFIG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-5C78C7A5-FE02-4831-BD99-3537282750D3)
- [DBMS_CLOUD_OCI_APM_CONFIG_CREATE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-3E4ACF20-2C60-4C7C-85E0-FAB6E5120167)
- [DBMS_CLOUD_OCI_APM_CONFIG_CREATE_APDEX_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-774A03BB-15B0-402C-83CF-4C913F7E4909)
- [DBMS_CLOUD_OCI_APM_CONFIG_DIMENSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-4CCD6FE2-82A9-41B9-86E7-E839FD276138)
- [DBMS_CLOUD_OCI_APM_CONFIG_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-369E2BD6-916F-4746-A05C-B5745B48CCD9)
- [DBMS_CLOUD_OCI_APM_CONFIG_DIMENSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-0F63110B-B4F2-4B63-9459-45CEA3EF443E)
- [DBMS_CLOUD_OCI_APM_CONFIG_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-512C33E1-A9EB-4292-8BEA-E7DC11E69477)
- [DBMS_CLOUD_OCI_APM_CONFIG_CREATE_METRIC_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-B6E97685-3B37-498C-90DD-16DDBDA80B6C)
- [DBMS_CLOUD_OCI_APM_CONFIG_CREATE_OPTIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-161785B7-8E5E-4244-B32C-65A11B13BA9C)
- [DBMS_CLOUD_OCI_APM_CONFIG_CREATE_SPAN_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-CC74C480-B7FC-49F7-ABD0-E327503EF9E4)
- [DBMS_CLOUD_OCI_APM_CONFIG_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-A1DBFFA3-6623-4970-A47C-7379969959F2)
- [DBMS_CLOUD_OCI_APM_CONFIG_METRIC_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-BA606636-8B26-47EF-A25E-AB1850A6A9A7)
- [DBMS_CLOUD_OCI_APM_CONFIG_METRIC_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-487CA2EF-57E2-4244-95BB-7890678B6BD0)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-9634ED55-9E4A-4393-9376-66D9D8C57F05)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-56B0FCF4-F647-4AA7-BF48-7D253F0FE60B)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-43DE07F6-33B9-498A-A86D-8A23A00E3CC4)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-9B343164-C662-4BED-B6F4-1790B866E5BD)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-BDAEB790-6FAF-4FAF-A12E-52EA77857704)
- [DBMS_CLOUD_OCI_APM_CONFIG_NAMESPACE_METRIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-2CEF99C8-FB83-47FA-8024-4C9D547AE616)
- [DBMS_CLOUD_OCI_APM_CONFIG_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-D5D31CFA-0BCD-4248-9887-E29A95A3BEAA)
- [DBMS_CLOUD_OCI_APM_CONFIG_OPTIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-9558E797-49A6-4505-B05E-E2989E87F2A7)
- [DBMS_CLOUD_OCI_APM_CONFIG_RETRIEVE_NAMESPACE_METRICS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-945BD744-B5D1-4A18-A93E-8B44EDE19290)
- [DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-D044FD93-D0AB-463F-BAD2-286BCF81D9C1)
- [DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_REFERENCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-E5D6ED21-4AFB-4111-9B78-16D893539957)
- [DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-D41C8CD5-0E29-4343-9D1C-E38F7717F9F0)
- [DBMS_CLOUD_OCI_APM_CONFIG_SPAN_FILTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-6FD8E8E5-E490-4D5F-96E2-8D47BC9840B8)
- [DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-AB46332A-D9CD-4206-A052-D7EBFBCFA205)
- [DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_APDEX_RULES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-BED2623D-57BC-4119-BDEF-F1725CD3760D)
- [DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_METRIC_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-06945EA7-323E-4533-9D4F-11BD57CDBF59)
- [DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_OPTIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-BC4B342C-72F3-4050-BE24-5119739B3653)
- [DBMS_CLOUD_OCI_APM_CONFIG_UPDATE_SPAN_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-8789440B-816C-423E-815A-B17B741E2E14)
- [DBMS_CLOUD_OCI_APM_CONFIG_VALIDATE_SPAN_FILTER_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/apm_config_t.html#ADSDK-GUID-783230BD-469E-4465-A46D-C410404B7204)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
