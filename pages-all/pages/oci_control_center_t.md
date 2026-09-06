# OCI Control Center Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#dcoc-content-body)

## OCI Control Center Common Types

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_DIMENSION_VALUE_T Type

The dimension value for the given dimension name as key.

Syntax
```

```

Fields

Field Description

`dimension_value`

(optional) The value of the dimension.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_ERROR_T Type

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

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_SUMMARY_T Type

A summary of the properties that define a metric.

Syntax
```

```

Fields

Field Description

`metric_name`

(required) The name of the metric.

`dimensions`

(optional) Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oci_control_center_metric_property_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_COLLECTION_T Type

A list of available metrics and their associated properties such as dimensions.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of MetricPropertySummary objects.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_SUMMARY_T Type

A summary of the source service or application emitting the metric.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) The name of the source service emitting the metric.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oci_control_center_namespace_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_COLLECTION_T Type

The list of source services called namespaces emitting metrics that you can explore using OCI Control Center.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of NamespaceSummary objects.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_REQUEST_SUMMARIZED_METRIC_DATA_DETAILS_T Type

The request details for retrieving aggregated data. Use the query and optional properties to filter the returned results.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) The source service or application to use when searching for metric data points to aggregate. For a list of valid namespaces, see`LIST_NAMESPACES`Function.

`metric_name`

(required) The name of a metric for retrieving aggregated data. For a list of valid metrics for a given namespace, see`LIST_METRIC_PROPERTIES`Function.

`compartment_id`

(required) The OCID of the compartment to use for authorization to read metrics. To use the root compartment, provide the tenancyId.

`dimensions`

(optional) Qualifiers to use when searching for metric data. For a list of valid dimensions for a given metric, see`LIST_METRIC_PROPERTIES`Function.

`start_time`

(optional) The beginning of the sampled time range to use when searching for metric data points. Format is defined by &lt;a href=\"https://www.rfc-editor.org/rfc/rfc3339\"&gt;RFC3339&lt;/a&gt;. The response includes metric data points for the sampled time. Example 2019-02-01T02:02:29.600Z

`end_time`

(optional) The end of the sampled time range to use when searching for metric data points. Format is defined by &lt;a href=\"https://www.rfc-editor.org/rfc/rfc3339\"&gt;RFC3339&lt;/a&gt;. The response excludes metric data points for sampled time. Example 2019-02-01T02:02:29.600Z

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_T Type

The recorded metric value at a specific timestamp.

Syntax
```

```

Fields

Field Description

`sample_time`

(optional) The time at which the metric data was recorded.

`resolution`

(optional) The duration over which the metric data is aggregated. Supported values: `1m`-`60m`, `1h`-`24h`, `1d`.

`dimensions`

(optional) Qualifiers provided in the definition of the returned metric. Available dimensions vary by metric namespace.

`aggregation_method`

(optional) The aggregation method used for aggregating the metric values. The aggregation method depends on the metric itself.

`aggregated_value`

(optional) The aggregated metric value for the specified request.

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_TBL Type

Nested table type of dbms_cloud_oci_oci_control_center_summarized_metric_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_COLLECTION_T Type

A list of aggregated metric data objects with properties.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of SummarizedMetricData items.

- [OCI Control Center Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-AB96F159-1BF3-4478-90BA-4CC1CE504E29)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-721EB873-DA57-41C4-8192-7FC31A93509D)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_DIMENSION_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-0EEC54EF-7390-4D93-82E6-427A14F9F7BE)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-FCE6A580-3CEF-433B-889A-05467F7DFA41)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-734C3ED7-EA4A-48AD-A396-01E3D26D719E)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-BDF47EC3-063F-42BC-B5C9-CB316F4FF453)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_METRIC_PROPERTY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-87A94E79-4AFB-4881-96FF-B6997333C4B7)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-EB263BCF-31E5-4439-A087-084A34D42202)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-154CA2EF-2235-467D-ABBF-D9389685D644)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_NAMESPACE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-26F37FC6-AD1E-4554-A1BC-68499BA0D703)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_REQUEST_SUMMARIZED_METRIC_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-B704A5FB-E512-4EAA-9D88-D028601F975A)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-B93F25B5-AE40-4CF0-9347-B1FC04DE28F8)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-3B4B3B3E-9677-45F1-999E-5B052C980524)
- [DBMS_CLOUD_OCI_OCI_CONTROL_CENTER_SUMMARIZED_METRIC_DATA_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oci_control_center_t.html#ADSDK-GUID-5EBDC219-BCAA-4BD6-995A-CE47CF8EA55D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
